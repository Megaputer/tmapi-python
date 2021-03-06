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


class SentimentsResponseDocuments(object):
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
        'id': 'int',
        'sentiments': 'list[SentimentsResponseSentiments]'
    }

    attribute_map = {
        'id': 'id',
        'sentiments': 'sentiments'
    }

    def __init__(self, id=None, sentiments=None):  # noqa: E501
        """SentimentsResponseDocuments - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._sentiments = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if sentiments is not None:
            self.sentiments = sentiments

    @property
    def id(self):
        """Gets the id of this SentimentsResponseDocuments.  # noqa: E501

        Index of document in input documents array  # noqa: E501

        :return: The id of this SentimentsResponseDocuments.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SentimentsResponseDocuments.

        Index of document in input documents array  # noqa: E501

        :param id: The id of this SentimentsResponseDocuments.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def sentiments(self):
        """Gets the sentiments of this SentimentsResponseDocuments.  # noqa: E501

        Result of sentiments operation  # noqa: E501

        :return: The sentiments of this SentimentsResponseDocuments.  # noqa: E501
        :rtype: list[SentimentsResponseSentiments]
        """
        return self._sentiments

    @sentiments.setter
    def sentiments(self, sentiments):
        """Sets the sentiments of this SentimentsResponseDocuments.

        Result of sentiments operation  # noqa: E501

        :param sentiments: The sentiments of this SentimentsResponseDocuments.  # noqa: E501
        :type: list[SentimentsResponseSentiments]
        """

        self._sentiments = sentiments

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
        if not isinstance(other, SentimentsResponseDocuments):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
