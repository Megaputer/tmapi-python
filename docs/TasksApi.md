# tmapi.TasksApi

All URIs are relative to *https://localhost:7008/tmapi/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_task**](TasksApi.md#create_task) | **POST** /tasks | Create task
[**delete_tasks**](TasksApi.md#delete_tasks) | **DELETE** /tasks | Delete tasks
[**get_task_result**](TasksApi.md#get_task_result) | **GET** /tasks/result | Task result
[**get_tasks_info**](TasksApi.md#get_tasks_info) | **GET** /tasks | Tasks information


# **create_task**
> object create_task(operations, documents, async=async, positions=positions)

Create task

To create a task for performing several operations with text documents, specify required operations in the \"operations\" attribute in the request body. Tasks should be separated by a comma. The list of operations supported with the server could be retrieved via the request \"server\".  Created tasks are available to users until they are deleted by the DELETE method or the server is restarted. After restarting the server it is not possible to get information, to delete, or to get the result of the created tasks. The tasks will cease to exist as if they were deleted by the DELETE method. 

### Example

* Basic Authentication (BasicAuth): 
```python
from __future__ import print_function
import time
import tmapi
from tmapi.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = tmapi.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = tmapi.TasksApi(tmapi.ApiClient(configuration))
operations = ["tokens"] # list[str] | List of operations (languages, tokens, keywords, entities, sentiments, facts)
documents = {"files":[{"content":"VGhlIFNlbmF0ZSBBZ3JpY3VsdHVyZSBDb21taXR0ZWUgd2FzIGV4cGVjdGVkIHRvIGNvbnNpZGVyIHByb3Bvc2FscyB0aGF0IHdvdWxkIGxpbWl0IGFkanVzdG1lbnRzIGluIGNvdW50eSBsb2FuIHJhdGUgZGlmZmVyZW50aWFscyB3aGljaCB0cmlnZ2VyIGxhcmdlciBjb3JuIGFuZCB3aGVhdCBhY3JlYWdlIHJlZHVjdGlvbiByZXF1aXJlbWVudHMu","extension":"txt"}]} # Documents | Documents to process
async = 1 # int | Asynchorous execution flag: * `0` - Block execution until result is ready (**default**) * `1` - Return GUID of newly created task and run task asynchronously  (optional)
positions = "none" # str | Positions format to be returned from server: - `none` - Don't return positions (**default**) - `symbol` - Symbol positions - `token` - Token positions  (optional)

try:
    # Create task
    api_response = api_instance.create_task(operations, documents, async=async, positions=positions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->create_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operations** | [**list[str]**](str.md)| List of operations (languages, tokens, keywords, entities, sentiments, facts) | 
 **documents** | [**Documents**](Documents.md)| Documents to process | 
 **async** | **int**| Asynchorous execution flag: * &#x60;0&#x60; - Block execution until result is ready (**default**) * &#x60;1&#x60; - Return GUID of newly created task and run task asynchronously  | [optional] 
 **positions** | **str**| Positions format to be returned from server: - &#x60;none&#x60; - Don&#39;t return positions (**default**) - &#x60;symbol&#x60; - Symbol positions - &#x60;token&#x60; - Token positions  | [optional] 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tasks**
> object delete_tasks(ids)

Delete tasks

The operation allows to delete current user’s tasks specified in the ids parameter. Deleting tasks saves the server disk space. 

### Example

* Basic Authentication (BasicAuth): 
```python
from __future__ import print_function
import time
import tmapi
from tmapi.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = tmapi.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = tmapi.TasksApi(tmapi.ApiClient(configuration))
ids = ["FEFC8383-D7DB-4557-AFBA-D96CA9CD5808","14E115E2-BB0A-45E0-AACC-EC8600101031"] # list[str] | List of task identifiers

try:
    # Delete tasks
    api_response = api_instance.delete_tasks(ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->delete_tasks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[str]**](str.md)| List of task identifiers | 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task_result**
> object get_task_result(id, operations, positions=positions)

Task result

The operation allows to get the result of the specified task. The task GUID and relevant operations are required.  Before getting results of the task execution, first ensure that the task is completed (the done paremeter is 100, the error parameter is empty). 

### Example

* Basic Authentication (BasicAuth): 
```python
from __future__ import print_function
import time
import tmapi
from tmapi.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = tmapi.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = tmapi.TasksApi(tmapi.ApiClient(configuration))
id = "FEFC8383-D7DB-4557-AFBA-D96CA9CD5808" # str | Task identifier
operations = ["tokens"] # list[str] | List of operations (languages, tokens, keywords, entities, sentiments, facts)
positions = "none" # str | Positions format to be returned from server: - `none` - Don't return positions (**default**) - `symbol` - Symbol positions - `token` - Token positions  (optional)

try:
    # Task result
    api_response = api_instance.get_task_result(id, operations, positions=positions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->get_task_result: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Task identifier | 
 **operations** | [**list[str]**](str.md)| List of operations (languages, tokens, keywords, entities, sentiments, facts) | 
 **positions** | **str**| Positions format to be returned from server: - &#x60;none&#x60; - Don&#39;t return positions (**default**) - &#x60;symbol&#x60; - Symbol positions - &#x60;token&#x60; - Token positions  | [optional] 

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tasks_info**
> TaskInfo get_tasks_info(ids)

Tasks information

The operation allows to receive information about the specified tasks. A task unique identifier (GIUD) is required, which is returned when creating new asynchronous task. If the identifiers list is empty, the server will return information about all tasks of the current user. 

### Example

* Basic Authentication (BasicAuth): 
```python
from __future__ import print_function
import time
import tmapi
from tmapi.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = tmapi.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = tmapi.TasksApi(tmapi.ApiClient(configuration))
ids = ["FEFC8383-D7DB-4557-AFBA-D96CA9CD5808","14E115E2-BB0A-45E0-AACC-EC8600101031"] # list[str] | List of task identifiers

try:
    # Tasks information
    api_response = api_instance.get_tasks_info(ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->get_tasks_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[str]**](str.md)| List of task identifiers | 

### Return type

[**TaskInfo**](TaskInfo.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

