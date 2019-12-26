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


class TokensResponseTokens(object):
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
        'word': 'str',
        'lemma': 'str',
        'part_of_speech': 'str',
        'modifier': 'object',
        'is_extension': 'int',
        'position': 'TokensResponsePosition'
    }

    attribute_map = {
        'word': 'word',
        'lemma': 'lemma',
        'part_of_speech': 'partOfSpeech',
        'modifier': 'modifier',
        'is_extension': 'isExtension',
        'position': 'position'
    }

    def __init__(self, word=None, lemma=None, part_of_speech=None, modifier=None, is_extension=None, position=None):  # noqa: E501
        """TokensResponseTokens - a model defined in OpenAPI"""  # noqa: E501

        self._word = None
        self._lemma = None
        self._part_of_speech = None
        self._modifier = None
        self._is_extension = None
        self._position = None
        self.discriminator = None

        if word is not None:
            self.word = word
        if lemma is not None:
            self.lemma = lemma
        if part_of_speech is not None:
            self.part_of_speech = part_of_speech
        if modifier is not None:
            self.modifier = modifier
        if is_extension is not None:
            self.is_extension = is_extension
        if position is not None:
            self.position = position

    @property
    def word(self):
        """Gets the word of this TokensResponseTokens.  # noqa: E501

        Word as in text  # noqa: E501

        :return: The word of this TokensResponseTokens.  # noqa: E501
        :rtype: str
        """
        return self._word

    @word.setter
    def word(self, word):
        """Sets the word of this TokensResponseTokens.

        Word as in text  # noqa: E501

        :param word: The word of this TokensResponseTokens.  # noqa: E501
        :type: str
        """

        self._word = word

    @property
    def lemma(self):
        """Gets the lemma of this TokensResponseTokens.  # noqa: E501

        A dictionary form of a word, e.g. given verb forms \"run\", \"ran\" and \"runs\", \"run\" is the lemma  # noqa: E501

        :return: The lemma of this TokensResponseTokens.  # noqa: E501
        :rtype: str
        """
        return self._lemma

    @lemma.setter
    def lemma(self, lemma):
        """Sets the lemma of this TokensResponseTokens.

        A dictionary form of a word, e.g. given verb forms \"run\", \"ran\" and \"runs\", \"run\" is the lemma  # noqa: E501

        :param lemma: The lemma of this TokensResponseTokens.  # noqa: E501
        :type: str
        """

        self._lemma = lemma

    @property
    def part_of_speech(self):
        """Gets the part_of_speech of this TokensResponseTokens.  # noqa: E501

        Assigns a word to a morphological category according to each syntactic functions.  # noqa: E501

        :return: The part_of_speech of this TokensResponseTokens.  # noqa: E501
        :rtype: str
        """
        return self._part_of_speech

    @part_of_speech.setter
    def part_of_speech(self, part_of_speech):
        """Sets the part_of_speech of this TokensResponseTokens.

        Assigns a word to a morphological category according to each syntactic functions.  # noqa: E501

        :param part_of_speech: The part_of_speech of this TokensResponseTokens.  # noqa: E501
        :type: str
        """
        allowed_values = ["Noun", "Verb", "Adverb", "Adjective", "Particle", "Pronoun", "Numeral", "Special", "Punctuation"]  # noqa: E501
        if part_of_speech not in allowed_values:
            raise ValueError(
                "Invalid value for `part_of_speech` ({0}), must be one of {1}"  # noqa: E501
                .format(part_of_speech, allowed_values)
            )

        self._part_of_speech = part_of_speech

    @property
    def modifier(self):
        """Gets the modifier of this TokensResponseTokens.  # noqa: E501

        One of the grammatical categories of a word, e.g. person for verbs or number for nouns. Each part of speech has its own set of modifiers.  The detailed list of parameters can be found in Help to TM API Server.   # noqa: E501

        :return: The modifier of this TokensResponseTokens.  # noqa: E501
        :rtype: object
        """
        return self._modifier

    @modifier.setter
    def modifier(self, modifier):
        """Sets the modifier of this TokensResponseTokens.

        One of the grammatical categories of a word, e.g. person for verbs or number for nouns. Each part of speech has its own set of modifiers.  The detailed list of parameters can be found in Help to TM API Server.   # noqa: E501

        :param modifier: The modifier of this TokensResponseTokens.  # noqa: E501
        :type: object
        """

        self._modifier = modifier

    @property
    def is_extension(self):
        """Gets the is_extension of this TokensResponseTokens.  # noqa: E501

        Indicates a way of writing a token with the previous one. It returns \"1\", if tokens are written as a single token. It returns \"0\", if tokens are written separately.   # noqa: E501

        :return: The is_extension of this TokensResponseTokens.  # noqa: E501
        :rtype: int
        """
        return self._is_extension

    @is_extension.setter
    def is_extension(self, is_extension):
        """Sets the is_extension of this TokensResponseTokens.

        Indicates a way of writing a token with the previous one. It returns \"1\", if tokens are written as a single token. It returns \"0\", if tokens are written separately.   # noqa: E501

        :param is_extension: The is_extension of this TokensResponseTokens.  # noqa: E501
        :type: int
        """
        allowed_values = [0, 1]  # noqa: E501
        if is_extension not in allowed_values:
            raise ValueError(
                "Invalid value for `is_extension` ({0}), must be one of {1}"  # noqa: E501
                .format(is_extension, allowed_values)
            )

        self._is_extension = is_extension

    @property
    def position(self):
        """Gets the position of this TokensResponseTokens.  # noqa: E501


        :return: The position of this TokensResponseTokens.  # noqa: E501
        :rtype: TokensResponsePosition
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this TokensResponseTokens.


        :param position: The position of this TokensResponseTokens.  # noqa: E501
        :type: TokensResponsePosition
        """

        self._position = position

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
        if not isinstance(other, TokensResponseTokens):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other