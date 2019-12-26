import base64
import os
import sys
import unittest
import time

# import tmapi from local folder
sys.path.append(os.path.abspath(os.path.join(__file__ ,"../../")))
import tmapi

# credentials
USERNAME = 'user'
PASSWORD = ''
HOST = ''#'http://localhost:7007/tmapi/v1'

def getServerConnection():
    if getServerConnection.client is None:
        conf = tmapi.Configuration()
        conf.verify_ssl = False
        if USERNAME != '':
            conf.username = USERNAME
        if PASSWORD != '':
            conf.password = PASSWORD
        if HOST != '':
            conf.host = HOST
        getServerConnection.client = tmapi.ApiClient(conf)
    return getServerConnection.client
getServerConnection.client = None

def getDocuments(texts):    
    files = []
    for text in texts:    
        b64text = base64.b64encode(text.encode('utf-8')).decode('utf-8')
        files.append(tmapi.Document(b64text))
    return tmapi.Documents(files)

# texts
testTexts = [
    'Elvis Presley was born in Tupelo, Mississippi.', 
    'Elvis Presley was an American singer'] 

#test server info
class TestServerInfo(unittest.TestCase):        
    def test_server_info(self):
        api = tmapi.ServerApi(getServerConnection())
        info = api.get_server_info()
        self.assertGreater(len(info.languages), 0)
        self.assertGreater(len(info.operations), 0)

#test server limits
class TestServerLimits(unittest.TestCase):
    def test_server_limits(self):
        api = tmapi.LimitsApi(getServerConnection())
        # limits are usually empty in developer versions. check no exceptions
        api.get_limits()

# test language detection operation
class TestLanguageDetection(unittest.TestCase):
    def setUp(self):
        self.operations = tmapi.OperationsApi(getServerConnection())

    def test_language(self):
        res = self.operations.get_languages(testTexts[0])
        self.assertEqual(len(res.documents), 1)
        self.assertEqual(res.documents[0].language, 'English')

    def test_documents_language(self):
        documents = getDocuments(testTexts)
        res = self.operations.get_documents_languages(documents)
        self.assertEqual(len(res.documents), len(documents.files))        
        for doc in res.documents:
            self.assertEqual(doc.language, 'English')
                
# test operations
class TestOperations(unittest.TestCase):
    def setUp(self):
        self.operations = tmapi.OperationsApi(getServerConnection())
        self.sentimentsTexts = [
            'New menu is good but the place in Toronto is dirty.',
            'Pretty good food on average']
        self.documents = getDocuments(testTexts)

    def check_attrs(obj, attrs):
        if (attrs != None):
            objAttrs = getattr(obj, 'attributes', None)
            if (objAttrs == None):
                return False
            for a in attrs:
                if getattr(objAttrs, a, None) != None:
                    continue
                if a in objAttrs:
                    continue
                return False
        return True

    def run_operation(self, objectName, operation, text, attrs=None):
        res = getattr(self.operations, operation)(text)
        self.assertEqual(len(res.documents), 1)
        objects = getattr(res.documents[0], objectName)
        self.assertGreater(len(objects), 0)
        self.assertEqual(objects[0].positions, None)
        #check attributes
        if (attrs != None):
            for obj in objects:
                self.assertTrue(TestOperations.check_attrs(obj, attrs))
        #positions
        posr = getattr(self.operations, operation)(text, positions='token')
        self.assertEqual(len(posr.documents), 1)
        objects = getattr(posr.documents[0], objectName)
        self.assertGreater(len(objects[0].positions), 0)

    def run_documents_operation(self, objectName, operation, documents, attrs=None):
        res = getattr(self.operations, operation)(documents)
        self.assertEqual(len(res.documents), len(documents.files))
        for doc in res.documents:
            objects = getattr(doc, objectName)
            self.assertGreater(len(objects), 0)
            self.assertEqual(objects[0].positions, None)
            #check attributes
            if (attrs != None):
                for obj in objects:
                    self.assertTrue(TestOperations.check_attrs(obj, attrs))
        # positions
        posres = getattr(self.operations, operation)(documents, positions='token')
        self.assertEqual(len(posres.documents), len(documents.files))
        for doc in posres.documents:
            objects = getattr(doc, objectName)
            self.assertGreater(len(objects[0].positions), 0)

    # test tokens 
    def test_tokens(self):
        res = self.operations.extract_tokens(testTexts[0])
        self.assertEqual(len(res.documents), 1)
        self.assertEqual(len(res.documents[0].sentences), 1)
        self.assertGreater(len(res.documents[0].sentences[0].tokens), 0)

    def test_documents_tokens(self):
        res = self.operations.extract_documents_tokens(self.documents)
        self.assertEqual(len(res.documents), len(self.documents.files))
        for doc in res.documents:
            self.assertGreater(len(doc.sentences[0].tokens), 0)
    
    #test keywords
    def test_keywords(self):
        self.run_operation('keywords', 'extract_keywords', testTexts[0])

    def test_documents_keywords(self):
        self.run_documents_operation('keywords', 'extract_documents_keywords', self.documents)

    #test entities
    def test_entities(self):
        self.run_operation('entities', 'extract_entities', testTexts[0], ['Name', 'Confidence'])

    def test_documents_entities(self):
        self.run_documents_operation('entities', 'extract_documents_entities', self.documents, ['Name', 'Confidence'])

    #test sentiments
    def test_sentiments(self):
        self.run_operation('sentiments', 'extract_sentiments', self.sentimentsTexts[0], ['subject', 'object'])

    def test_documents_sentiments(self):
        self.run_documents_operation('sentiments', 'extract_documents_sentiments', getDocuments(self.sentimentsTexts), ['subject', 'object'])

    #test facts
    def test_facts(self):
        self.run_operation('facts', 'extract_facts', testTexts[0], ['Person', 'Confidence'])

    def test_documents_facts(self):
        self.run_documents_operation('facts', 'extract_documents_facts', self.documents, ['Person', 'Confidence'])

#test tasks
class TestTasks(unittest.TestCase):
    def setUp(self):
        self.tasks = tmapi.TasksApi(getServerConnection())
        self.documents = getDocuments(testTexts)

    def test_task_info(self):
        resId = self.tasks.create_task(['tokens'], self.documents, **{'async' : 1})
        taskId = resId['taskId']
        all = self.tasks.get_tasks_info([])
        self.assertGreater(len(all.tasks), 0)
        bFound = False
        for task in all.tasks:
            if task.id == taskId:
                bFound = True
                break
        self.assertTrue(bFound)
        info = self.tasks.get_tasks_info([taskId])
        self.assertEqual(info.tasks[0].id, taskId)

    def test_delete_task(self):
        resId = self.tasks.create_task(['tokens'], self.documents, **{'async' : 1})
        id = resId['taskId']
        info = self.tasks.get_tasks_info([id])
        self.assertGreater(len(info.tasks), 0)
        self.tasks.delete_tasks([id])
        info = self.tasks.get_tasks_info([id])
        self.assertEqual(info.tasks, None)        

    def test_sync_task(self):
        res = self.tasks.create_task(['entities'], self.documents)
        self.assertEqual(len(res['documents']), len(self.documents.files))
        self.assertGreater(len(res['documents'][0]['entities']), 0)

    def test_async_task(self):
        resId = self.tasks.create_task(['entities'], self.documents, **{'async' : 1})
        id = resId['taskId']
        # time.sleep(5)
        while True:
            info = self.tasks.get_tasks_info([id])
            # print(info.tasks)
            if info.tasks[0].done == 100:
                break
            time.sleep(1)
        # entity results
        resEntities = self.tasks.get_task_result(id, ['entities'])
        self.assertEqual(len(resEntities['documents']), len(self.documents.files))
        self.assertGreater(len(resEntities['documents'][0]['entities']), 0)        

    def test_multiple_task(self):
        operations = ['tokens', 'entities']
        taskIds = []
        # create tasks
        for operation in operations:
            id = self.tasks.create_task([operation], self.documents, **{'async' : 1})
            taskIds.append(id['taskId'])
        time.sleep(5)
        # wait till finished
        while True:
            info = self.tasks.get_tasks_info(taskIds)
            self.assertEqual(len(taskIds), len(info.tasks))
            allFinished = True
            for task in info.tasks:
                if task.done < 100:
                    allFinished = False
                    break
            if allFinished:
                break
            time.sleep(1)
        # check results
        for i in range(0, len(operations)):
            res = self.tasks.get_task_result(taskIds[i], [operations[i]])
            self.assertGreater(len(res['documents']), 0)
        # delete tasks
        self.tasks.delete_tasks(taskIds)
        info = self.tasks.get_tasks_info(taskIds)
        self.assertEqual(info.tasks, None)

# main
if __name__ == '__main__':
    # unittest.main(defaultTest='TestTasks.test_async_task')
    unittest.main()
