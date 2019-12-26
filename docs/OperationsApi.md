# tmapi.OperationsApi

All URIs are relative to *https://localhost:7008/tmapi/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**extract_documents_entities**](OperationsApi.md#extract_documents_entities) | **POST** /operations/entities | Entities extraction
[**extract_documents_facts**](OperationsApi.md#extract_documents_facts) | **POST** /operations/facts | Facts extraction
[**extract_documents_keywords**](OperationsApi.md#extract_documents_keywords) | **POST** /operations/keywords | Keywords extraction
[**extract_documents_sentiments**](OperationsApi.md#extract_documents_sentiments) | **POST** /operations/sentiments | Sentiments analysis
[**extract_documents_tokens**](OperationsApi.md#extract_documents_tokens) | **POST** /operations/tokens | Text parsing
[**extract_entities**](OperationsApi.md#extract_entities) | **GET** /operations/entities | Entities extraction
[**extract_facts**](OperationsApi.md#extract_facts) | **GET** /operations/facts | Facts extraction
[**extract_keywords**](OperationsApi.md#extract_keywords) | **GET** /operations/keywords | Keywords extraction
[**extract_sentiments**](OperationsApi.md#extract_sentiments) | **GET** /operations/sentiments | Sentiments analysis
[**extract_tokens**](OperationsApi.md#extract_tokens) | **GET** /operations/tokens | Text parsing
[**get_documents_languages**](OperationsApi.md#get_documents_languages) | **POST** /operations/languages | Language detection
[**get_languages**](OperationsApi.md#get_languages) | **GET** /operations/languages | Language detection


# **extract_documents_entities**
> EntitiesResponse extract_documents_entities(documents, positions=positions)

Entities extraction

The operation extracts entities from each file.

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
api_instance = tmapi.OperationsApi(tmapi.ApiClient(configuration))
documents = {"files":[{"content":"RWx2aXMgUHJlc2xleSB3YXMgYm9ybiBpbiBUdXBlbG8sIE1pc3Npc3NpcHBp","extension":"txt"}]} # Documents | Documents to process
positions = "none" # str | Positions format to be returned from server: - `none` - Don't return positions (**default**) - `symbol` - Symbol positions - `token` - Token positions  (optional)

try:
    # Entities extraction
    api_response = api_instance.extract_documents_entities(documents, positions=positions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->extract_documents_entities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **documents** | [**Documents**](Documents.md)| Documents to process | 
 **positions** | **str**| Positions format to be returned from server: - &#x60;none&#x60; - Don&#39;t return positions (**default**) - &#x60;symbol&#x60; - Symbol positions - &#x60;token&#x60; - Token positions  | [optional] 

### Return type

[**EntitiesResponse**](EntitiesResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extract_documents_facts**
> FactsResponse extract_documents_facts(documents, positions=positions)

Facts extraction

The operation extracts facts from each file. The term \"fact\" is used to denote phenomena, events, notions and relations between them which may be of interest to users.  

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
api_instance = tmapi.OperationsApi(tmapi.ApiClient(configuration))
documents = {"files":[{"content":"RWx2aXMgUHJlc2xleSB3YXMgYW4gQW1lcmljYW4gc2luZ2Vy","extension":"txt"}]} # Documents | Documents to process
positions = "none" # str | Positions format to be returned from server: - `none` - Don't return positions (**default**) - `symbol` - Symbol positions - `token` - Token positions  (optional)

try:
    # Facts extraction
    api_response = api_instance.extract_documents_facts(documents, positions=positions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->extract_documents_facts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **documents** | [**Documents**](Documents.md)| Documents to process | 
 **positions** | **str**| Positions format to be returned from server: - &#x60;none&#x60; - Don&#39;t return positions (**default**) - &#x60;symbol&#x60; - Symbol positions - &#x60;token&#x60; - Token positions  | [optional] 

### Return type

[**FactsResponse**](FactsResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extract_documents_keywords**
> KeywordsResponse extract_documents_keywords(documents, positions=positions)

Keywords extraction

The operation explores often mentioned terms in each file. The response returns keywords and other statistics extracted from each file.

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
api_instance = tmapi.OperationsApi(tmapi.ApiClient(configuration))
documents = {"files":[{"content":"VGhlIFNlbmF0ZSBBZ3JpY3VsdHVyZSBDb21taXR0ZWUgd2FzIGV4cGVjdGVkIHRvIGNvbnNpZGVyIHByb3Bvc2FscyB0aGF0IHdvdWxkIGxpbWl0IGFkanVzdG1lbnRzIGluIGNvdW50eSBsb2FuIHJhdGUgZGlmZmVyZW50aWFscyB3aGljaCB0cmlnZ2VyIGxhcmdlciBjb3JuIGFuZCB3aGVhdCBhY3JlYWdlIHJlZHVjdGlvbiByZXF1aXJlbWVudHMu","extension":"txt"}]} # Documents | Documents to process
positions = "none" # str | Positions format to be returned from server: - `none` - Don't return positions (**default**) - `symbol` - Symbol positions - `token` - Token positions  (optional)

try:
    # Keywords extraction
    api_response = api_instance.extract_documents_keywords(documents, positions=positions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->extract_documents_keywords: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **documents** | [**Documents**](Documents.md)| Documents to process | 
 **positions** | **str**| Positions format to be returned from server: - &#x60;none&#x60; - Don&#39;t return positions (**default**) - &#x60;symbol&#x60; - Symbol positions - &#x60;token&#x60; - Token positions  | [optional] 

### Return type

[**KeywordsResponse**](KeywordsResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extract_documents_sentiments**
> SentimentsResponse extract_documents_sentiments(documents, positions=positions)

Sentiments analysis

The operation extracts opinions and emotions related to something, identifies the subject, the object of evaluation and the evaluation itself in each file.  

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
api_instance = tmapi.OperationsApi(tmapi.ApiClient(configuration))
documents = {"files":[{"content":"VGhlIGJ1cmdlciB3YXMgZ3JlYXQsIGJ1dCB0aGUgd2FpdGVyIHdhcyB2ZXJ5IHJ1ZGUu","extension":"txt"}]} # Documents | Documents to process
positions = "none" # str | Positions format to be returned from server: - `none` - Don't return positions (**default**) - `symbol` - Symbol positions - `token` - Token positions  (optional)

try:
    # Sentiments analysis
    api_response = api_instance.extract_documents_sentiments(documents, positions=positions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->extract_documents_sentiments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **documents** | [**Documents**](Documents.md)| Documents to process | 
 **positions** | **str**| Positions format to be returned from server: - &#x60;none&#x60; - Don&#39;t return positions (**default**) - &#x60;symbol&#x60; - Symbol positions - &#x60;token&#x60; - Token positions  | [optional] 

### Return type

[**SentimentsResponse**](SentimentsResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extract_documents_tokens**
> TokensResponse extract_documents_tokens(documents)

Text parsing

Parse text in each file. The response returns the text which is divided into tokens and sentences, conducts morphological analysis, determines parts of speech, lemmas, etc. 

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
api_instance = tmapi.OperationsApi(tmapi.ApiClient(configuration))
documents = {"files":[{"content":"RWx2aXMgUHJlc2xleSB3YXMgYm9ybiBpbiBUdXBlbG8sIE1pc3Npc3NpcHBp","extension":"txt"}]} # Documents | Documents to process

try:
    # Text parsing
    api_response = api_instance.extract_documents_tokens(documents)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->extract_documents_tokens: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **documents** | [**Documents**](Documents.md)| Documents to process | 

### Return type

[**TokensResponse**](TokensResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extract_entities**
> EntitiesResponse extract_entities(text, positions=positions)

Entities extraction

The operation extracts entities from the text document. For example, an entity may represent a person’s name, a name of an organization, an e-mail address, a phone number, or a geographical location.  

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
api_instance = tmapi.OperationsApi(tmapi.ApiClient(configuration))
text = "Elvis Presley was born in Tupelo, Mississippi" # str | Document text to process
positions = "none" # str | Positions format to be returned from server: - `none` - Don't return positions (**default**) - `symbol` - Symbol positions - `token` - Token positions  (optional)

try:
    # Entities extraction
    api_response = api_instance.extract_entities(text, positions=positions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->extract_entities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text** | **str**| Document text to process | 
 **positions** | **str**| Positions format to be returned from server: - &#x60;none&#x60; - Don&#39;t return positions (**default**) - &#x60;symbol&#x60; - Symbol positions - &#x60;token&#x60; - Token positions  | [optional] 

### Return type

[**EntitiesResponse**](EntitiesResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extract_facts**
> FactsResponse extract_facts(text, positions=positions)

Facts extraction

The operation extracts facts from the text. The term \"fact\" is used to denote phenomena, events, notions and relations between them which may be of interest to users.

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
api_instance = tmapi.OperationsApi(tmapi.ApiClient(configuration))
text = "Elvis Presley was an American singer" # str | Document text to process
positions = "none" # str | Positions format to be returned from server: - `none` - Don't return positions (**default**) - `symbol` - Symbol positions - `token` - Token positions  (optional)

try:
    # Facts extraction
    api_response = api_instance.extract_facts(text, positions=positions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->extract_facts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text** | **str**| Document text to process | 
 **positions** | **str**| Positions format to be returned from server: - &#x60;none&#x60; - Don&#39;t return positions (**default**) - &#x60;symbol&#x60; - Symbol positions - &#x60;token&#x60; - Token positions  | [optional] 

### Return type

[**FactsResponse**](FactsResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extract_keywords**
> KeywordsResponse extract_keywords(text, positions=positions)

Keywords extraction

The operation explores often mentioned terms in the text. The response returns keywords and other statistics extracted from the text.

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
api_instance = tmapi.OperationsApi(tmapi.ApiClient(configuration))
text = "The Senate Agriculture Committee was expected to consider proposals that would limit adjustments in county loan rate differentials which trigger larger corn and wheat acreage reduction requirements." # str | Document text to process
positions = "none" # str | Positions format to be returned from server: - `none` - Don't return positions (**default**) - `symbol` - Symbol positions - `token` - Token positions  (optional)

try:
    # Keywords extraction
    api_response = api_instance.extract_keywords(text, positions=positions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->extract_keywords: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text** | **str**| Document text to process | 
 **positions** | **str**| Positions format to be returned from server: - &#x60;none&#x60; - Don&#39;t return positions (**default**) - &#x60;symbol&#x60; - Symbol positions - &#x60;token&#x60; - Token positions  | [optional] 

### Return type

[**KeywordsResponse**](KeywordsResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extract_sentiments**
> SentimentsResponse extract_sentiments(text, positions=positions)

Sentiments analysis

Extract sentiments from document

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
api_instance = tmapi.OperationsApi(tmapi.ApiClient(configuration))
text = "The burger was great, but the waiter was very rude." # str | Document text to process
positions = "none" # str | Positions format to be returned from server: - `none` - Don't return positions (**default**) - `symbol` - Symbol positions - `token` - Token positions  (optional)

try:
    # Sentiments analysis
    api_response = api_instance.extract_sentiments(text, positions=positions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->extract_sentiments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text** | **str**| Document text to process | 
 **positions** | **str**| Positions format to be returned from server: - &#x60;none&#x60; - Don&#39;t return positions (**default**) - &#x60;symbol&#x60; - Symbol positions - &#x60;token&#x60; - Token positions  | [optional] 

### Return type

[**SentimentsResponse**](SentimentsResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extract_tokens**
> TokensResponse extract_tokens(text)

Text parsing

Parse document text. The response returns the text which is divided into tokens and sentences, conducts morphological analysis, determines parts of speech, lemmas, etc. 

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
api_instance = tmapi.OperationsApi(tmapi.ApiClient(configuration))
text = "Elvis Presley was born in Tupelo, Mississippi" # str | Document text to process

try:
    # Text parsing
    api_response = api_instance.extract_tokens(text)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->extract_tokens: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text** | **str**| Document text to process | 

### Return type

[**TokensResponse**](TokensResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_documents_languages**
> LanguagesResponse get_documents_languages(documents)

Language detection

Automatically determine the language of each file.  The text encoding format of source files with the .txt extension must be strictly UTF-8. Otherwise, requests will not be executed. 

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
api_instance = tmapi.OperationsApi(tmapi.ApiClient(configuration))
documents = {"files":[{"content":"RWx2aXMgUHJlc2xleSB3YXMgYm9ybiBpbiBUdXBlbG8sIE1pc3Npc3NpcHBp","extension":"txt"}]} # Documents | Documents to process

try:
    # Language detection
    api_response = api_instance.get_documents_languages(documents)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->get_documents_languages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **documents** | [**Documents**](Documents.md)| Documents to process | 

### Return type

[**LanguagesResponse**](LanguagesResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_languages**
> LanguagesResponse get_languages(text)

Language detection

Detect the language of text documents

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
api_instance = tmapi.OperationsApi(tmapi.ApiClient(configuration))
text = "Elvis Presley was born in Tupelo, Mississippi" # str | Document text to process

try:
    # Language detection
    api_response = api_instance.get_languages(text)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->get_languages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text** | **str**| Document text to process | 

### Return type

[**LanguagesResponse**](LanguagesResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

