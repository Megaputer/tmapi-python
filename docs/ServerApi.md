# tmapi.ServerApi

All URIs are relative to *https://localhost:7008/tmapi/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_password**](ServerApi.md#change_password) | **POST** /change-password | Change password
[**get_server_info**](ServerApi.md#get_server_info) | **GET** /server | Server information


# **change_password**
> change_password(change_password_request)

Change password

Use this request to change the password.

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
api_instance = tmapi.ServerApi(tmapi.ApiClient(configuration))
change_password_request = tmapi.ChangePasswordRequest() # ChangePasswordRequest | Change password request

try:
    # Change password
    api_instance.change_password(change_password_request)
except ApiException as e:
    print("Exception when calling ServerApi->change_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **change_password_request** | [**ChangePasswordRequest**](ChangePasswordRequest.md)| Change password request | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_server_info**
> ServerInfo get_server_info()

Server information

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
api_instance = tmapi.ServerApi(tmapi.ApiClient(configuration))

try:
    # Server information
    api_response = api_instance.get_server_info()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServerApi->get_server_info: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ServerInfo**](ServerInfo.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

