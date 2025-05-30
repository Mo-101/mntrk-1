# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class RemoteSensingAugmentationRequest(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, dataset_url: str=None, augmentation_type: str=None):  # noqa: E501
        """RemoteSensingAugmentationRequest - a model defined in Swagger

        :param dataset_url: The dataset_url of this RemoteSensingAugmentationRequest.  # noqa: E501
        :type dataset_url: str
        :param augmentation_type: The augmentation_type of this RemoteSensingAugmentationRequest.  # noqa: E501
        :type augmentation_type: str
        """
        self.swagger_types = {
            'dataset_url': str,
            'augmentation_type': str
        }

        self.attribute_map = {
            'dataset_url': 'dataset_url',
            'augmentation_type': 'augmentation_type'
        }
        self._dataset_url = dataset_url
        self._augmentation_type = augmentation_type

    @classmethod
    def from_dict(cls, dikt) -> 'RemoteSensingAugmentationRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The RemoteSensingAugmentationRequest of this RemoteSensingAugmentationRequest.  # noqa: E501
        :rtype: RemoteSensingAugmentationRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def dataset_url(self) -> str:
        """Gets the dataset_url of this RemoteSensingAugmentationRequest.


        :return: The dataset_url of this RemoteSensingAugmentationRequest.
        :rtype: str
        """
        return self._dataset_url

    @dataset_url.setter
    def dataset_url(self, dataset_url: str):
        """Sets the dataset_url of this RemoteSensingAugmentationRequest.


        :param dataset_url: The dataset_url of this RemoteSensingAugmentationRequest.
        :type dataset_url: str
        """

        self._dataset_url = dataset_url

    @property
    def augmentation_type(self) -> str:
        """Gets the augmentation_type of this RemoteSensingAugmentationRequest.


        :return: The augmentation_type of this RemoteSensingAugmentationRequest.
        :rtype: str
        """
        return self._augmentation_type

    @augmentation_type.setter
    def augmentation_type(self, augmentation_type: str):
        """Sets the augmentation_type of this RemoteSensingAugmentationRequest.


        :param augmentation_type: The augmentation_type of this RemoteSensingAugmentationRequest.
        :type augmentation_type: str
        """

        self._augmentation_type = augmentation_type
