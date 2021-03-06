# coding: utf-8

"""
    Megaputer Text Mining API

    Megaputer Text Mining API  # noqa: E501

    OpenAPI spec version: 1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from tmapi.api_client import ApiClient


class LimitsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_limits(self, **kwargs):  # noqa: E501
        """Limits information  # noqa: E501

        To check current limitations, send the relevant request. Responses may be different depending on the type of the license acquired: - **Total limit for all operations.** The license establishes limits on the total number of requests for text unit processing. If the total number of text units is equal to or exceeds the limits, then all operations will be blocked.            - **Limit for each operation.** The license establishes limits on requests for text unit processing per each operation separately. If a number of text units NTU of any operation is equal to or exceeds the NTULimit, then this operation will be blocked. Other operations will be available until their NTU counters reach the maximum threshold.  - **Total limit on number of calls.** The license establishes limits on the total number of requests for text unit processing for a definite period. If the total number of text units is equal to or exceeds the number of requests specified for a certain period, then all operations will be blocked till the end of this period. The maximum number of periods - 2. The counter resets when a new period comes, for example, a new day or a new month. Users can send requests again until the maximum number of text units is reached in the specified period.  - **Limit on number of calls for each operation.** The license establishes limits on requests for text unit processing per each operation separately for definite period. If the number of processed text units for a single operation equals to or exceeds the number of requests specified for a certain period, then this operation will be blocked until the end of the specified period. Other operations will be available until their NTU counters reach a maximum threshold.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_limits(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_limits_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_limits_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_limits_with_http_info(self, **kwargs):  # noqa: E501
        """Limits information  # noqa: E501

        To check current limitations, send the relevant request. Responses may be different depending on the type of the license acquired: - **Total limit for all operations.** The license establishes limits on the total number of requests for text unit processing. If the total number of text units is equal to or exceeds the limits, then all operations will be blocked.            - **Limit for each operation.** The license establishes limits on requests for text unit processing per each operation separately. If a number of text units NTU of any operation is equal to or exceeds the NTULimit, then this operation will be blocked. Other operations will be available until their NTU counters reach the maximum threshold.  - **Total limit on number of calls.** The license establishes limits on the total number of requests for text unit processing for a definite period. If the total number of text units is equal to or exceeds the number of requests specified for a certain period, then all operations will be blocked till the end of this period. The maximum number of periods - 2. The counter resets when a new period comes, for example, a new day or a new month. Users can send requests again until the maximum number of text units is reached in the specified period.  - **Limit on number of calls for each operation.** The license establishes limits on requests for text unit processing per each operation separately for definite period. If the number of processed text units for a single operation equals to or exceeds the number of requests specified for a certain period, then this operation will be blocked until the end of the specified period. Other operations will be available until their NTU counters reach a maximum threshold.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_limits_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_limits" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/limits', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
