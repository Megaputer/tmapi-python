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


class Document(object):
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
        'content': 'str',
        'extension': 'str'
    }

    attribute_map = {
        'content': 'content',
        'extension': 'extension'
    }

    def __init__(self, content=None, extension='txt'):  # noqa: E501
        """Document - a model defined in OpenAPI"""  # noqa: E501

        self._content = None
        self._extension = None
        self.discriminator = None

        self.content = content
        if extension is not None:
            self.extension = extension

    @property
    def content(self):
        """Gets the content of this Document.  # noqa: E501

        Document content encoded in base64  # noqa: E501

        :return: The content of this Document.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this Document.

        Document content encoded in base64  # noqa: E501

        :param content: The content of this Document.  # noqa: E501
        :type: str
        """
        if content is None:
            raise ValueError("Invalid value for `content`, must not be `None`")  # noqa: E501

        self._content = content

    @property
    def extension(self):
        """Gets the extension of this Document.  # noqa: E501

        Document extension  # noqa: E501

        :return: The extension of this Document.  # noqa: E501
        :rtype: str
        """
        return self._extension

    @extension.setter
    def extension(self, extension):
        """Sets the extension of this Document.

        Document extension  # noqa: E501

        :param extension: The extension of this Document.  # noqa: E501
        :type: str
        """
        allowed_values = ["txt"]  # noqa: E501
        if extension not in allowed_values:
            raise ValueError(
                "Invalid value for `extension` ({0}), must be one of {1}"  # noqa: E501
                .format(extension, allowed_values)
            )

        self._extension = extension

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
        if not isinstance(other, Document):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
