# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class DataTransformationResponse(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, message: str=None):  # noqa: E501
        """DataTransformationResponse - a model defined in Swagger

        :param message: The message of this DataTransformationResponse.  # noqa: E501
        :type message: str
        """
        self.swagger_types = {
            'message': str
        }

        self.attribute_map = {
            'message': 'message'
        }
        self._message = message

    @classmethod
    def from_dict(cls, dikt) -> 'DataTransformationResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The DataTransformationResponse of this DataTransformationResponse.  # noqa: E501
        :rtype: DataTransformationResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def message(self) -> str:
        """Gets the message of this DataTransformationResponse.


        :return: The message of this DataTransformationResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message: str):
        """Sets the message of this DataTransformationResponse.


        :param message: The message of this DataTransformationResponse.
        :type message: str
        """

        self._message = message
