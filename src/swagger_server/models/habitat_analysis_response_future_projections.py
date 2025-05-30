# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class HabitatAnalysisResponseFutureProjections(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, timeframe: str=None, projected_population: int=None, confidence_interval: float=None):  # noqa: E501
        """HabitatAnalysisResponseFutureProjections - a model defined in Swagger

        :param timeframe: The timeframe of this HabitatAnalysisResponseFutureProjections.  # noqa: E501
        :type timeframe: str
        :param projected_population: The projected_population of this HabitatAnalysisResponseFutureProjections.  # noqa: E501
        :type projected_population: int
        :param confidence_interval: The confidence_interval of this HabitatAnalysisResponseFutureProjections.  # noqa: E501
        :type confidence_interval: float
        """
        self.swagger_types = {
            'timeframe': str,
            'projected_population': int,
            'confidence_interval': float
        }

        self.attribute_map = {
            'timeframe': 'timeframe',
            'projected_population': 'projected_population',
            'confidence_interval': 'confidence_interval'
        }
        self._timeframe = timeframe
        self._projected_population = projected_population
        self._confidence_interval = confidence_interval

    @classmethod
    def from_dict(cls, dikt) -> 'HabitatAnalysisResponseFutureProjections':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The HabitatAnalysisResponse_future_projections of this HabitatAnalysisResponseFutureProjections.  # noqa: E501
        :rtype: HabitatAnalysisResponseFutureProjections
        """
        return util.deserialize_model(dikt, cls)

    @property
    def timeframe(self) -> str:
        """Gets the timeframe of this HabitatAnalysisResponseFutureProjections.


        :return: The timeframe of this HabitatAnalysisResponseFutureProjections.
        :rtype: str
        """
        return self._timeframe

    @timeframe.setter
    def timeframe(self, timeframe: str):
        """Sets the timeframe of this HabitatAnalysisResponseFutureProjections.


        :param timeframe: The timeframe of this HabitatAnalysisResponseFutureProjections.
        :type timeframe: str
        """
        allowed_values = ["30_days", "90_days", "1_year"]  # noqa: E501
        if timeframe not in allowed_values:
            raise ValueError(
                "Invalid value for `timeframe` ({0}), must be one of {1}"
                .format(timeframe, allowed_values)
            )

        self._timeframe = timeframe

    @property
    def projected_population(self) -> int:
        """Gets the projected_population of this HabitatAnalysisResponseFutureProjections.


        :return: The projected_population of this HabitatAnalysisResponseFutureProjections.
        :rtype: int
        """
        return self._projected_population

    @projected_population.setter
    def projected_population(self, projected_population: int):
        """Sets the projected_population of this HabitatAnalysisResponseFutureProjections.


        :param projected_population: The projected_population of this HabitatAnalysisResponseFutureProjections.
        :type projected_population: int
        """

        self._projected_population = projected_population

    @property
    def confidence_interval(self) -> float:
        """Gets the confidence_interval of this HabitatAnalysisResponseFutureProjections.


        :return: The confidence_interval of this HabitatAnalysisResponseFutureProjections.
        :rtype: float
        """
        return self._confidence_interval

    @confidence_interval.setter
    def confidence_interval(self, confidence_interval: float):
        """Sets the confidence_interval of this HabitatAnalysisResponseFutureProjections.


        :param confidence_interval: The confidence_interval of this HabitatAnalysisResponseFutureProjections.
        :type confidence_interval: float
        """

        self._confidence_interval = confidence_interval
