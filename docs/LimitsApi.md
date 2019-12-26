# tmapi.LimitsApi

All URIs are relative to *https://localhost:7008/tmapi/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_limits**](LimitsApi.md#get_limits) | **GET** /limits | Limits information


# **get_limits**
> object get_limits()

Limits information

To check current limitations, send the relevant request. Responses may be different depending on the type of the license acquired: - **Total limit for all operations.** The license establishes limits on the total number of requests for text unit processing. If the total number of text units is equal to or exceeds the limits, then all operations will be blocked.            - **Limit for each operation.** The license establishes limits on requests for text unit processing per each operation separately. If a number of text units NTU of any operation is equal to or exceeds the NTULimit, then this operation will be blocked. Other operations will be available until their NTU counters reach the maximum threshold.  - **Total limit on number of calls.** The license establishes limits on the total number of requests for text unit processing for a definite period. If the total number of text units is equal to or exceeds the number of requests specified for a certain period, then all operations will be blocked till the end of this period. The maximum number of periods - 2. The counter resets when a new period comes, for example, a new day or a new month. Users can send requests again until the maximum number of text units is reached in the specified period.  - **Limit on number of calls for each operation.** The license establishes limits on requests for text unit processing per each operation separately for definite period. If the number of processed text units for a single operation equals to or exceeds the number of requests specified for a certain period, then this operation will be blocked until the end of the specified period. Other operations will be available until their NTU counters reach a maximum threshold. 

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
api_instance = tmapi.LimitsApi(tmapi.ApiClient(configuration))

try:
    # Limits information
    api_response = api_instance.get_limits()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LimitsApi->get_limits: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

