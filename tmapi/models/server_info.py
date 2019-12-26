# coding: utf-8

"""
    Megaputer Text Mining API

    Megaputer Text Mining API  # noqa: E501

    OpenAPI spec version: 1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class ServerInfo(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'version': 'str',
        'languages': 'list[str]',
        'operations': 'list[str]'
    }

    attribute_map = {
        'version': 'version',
        'languages': 'languages',
        'operations': 'operations'
    }

    def __init__(self, version=None, languages=None, operations=None):  # noqa: E501
        """ServerInfo - a model defined in OpenAPI"""  # noqa: E501

        self._version = None
        self._languages = None
        self._operations = None
        self.discriminator = None

        if version is not None:
            self.version = version
        if languages is not None:
            self.languages = languages
        if operations is not None:
            self.operations = operations

    @property
    def version(self):
        """Gets the version of this ServerInfo.  # noqa: E501

        Server version  # noqa: E501

        :return: The version of this ServerInfo.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ServerInfo.

        Server version  # noqa: E501

        :param version: The version of this ServerInfo.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def languages(self):
        """Gets the languages of this ServerInfo.  # noqa: E501

        List of supported languages  # noqa: E501

        :return: The languages of this ServerInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._languages

    @languages.setter
    def languages(self, languages):
        """Sets the languages of this ServerInfo.

        List of supported languages  # noqa: E501

        :param languages: The languages of this ServerInfo.  # noqa: E501
        :type: list[str]
        """

        self._languages = languages

    @property
    def operations(self):
        """Gets the operations of this ServerInfo.  # noqa: E501

        List of supported operations  # noqa: E501

        :return: The operations of this ServerInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._operations

    @operations.setter
    def operations(self, operations):
        """Sets the operations of this ServerInfo.

        List of supported operations  # noqa: E501

        :param operations: The operations of this ServerInfo.  # noqa: E501
        :type: list[str]
        """

        self._operations = operations

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ServerInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
