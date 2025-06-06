# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.geo_coordinate import GeoCoordinate  # noqa: F401,E501
from swagger_server import util


class SpatialClusteringBody(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, region_coordinates: List[GeoCoordinate]=None, timeframe: str=None, clustering_algorithm: str=None, min_points: int=None, epsilon: float=None):  # noqa: E501
        """SpatialClusteringBody - a model defined in Swagger

        :param region_coordinates: The region_coordinates of this SpatialClusteringBody.  # noqa: E501
        :type region_coordinates: List[GeoCoordinate]
        :param timeframe: The timeframe of this SpatialClusteringBody.  # noqa: E501
        :type timeframe: str
        :param clustering_algorithm: The clustering_algorithm of this SpatialClusteringBody.  # noqa: E501
        :type clustering_algorithm: str
        :param min_points: The min_points of this SpatialClusteringBody.  # noqa: E501
        :type min_points: int
        :param epsilon: The epsilon of this SpatialClusteringBody.  # noqa: E501
        :type epsilon: float
        """
        self.swagger_types = {
            'region_coordinates': List[GeoCoordinate],
            'timeframe': str,
            'clustering_algorithm': str,
            'min_points': int,
            'epsilon': float
        }

        self.attribute_map = {
            'region_coordinates': 'region_coordinates',
            'timeframe': 'timeframe',
            'clustering_algorithm': 'clustering_algorithm',
            'min_points': 'min_points',
            'epsilon': 'epsilon'
        }
        self._region_coordinates = region_coordinates
        self._timeframe = timeframe
        self._clustering_algorithm = clustering_algorithm
        self._min_points = min_points
        self._epsilon = epsilon

    @classmethod
    def from_dict(cls, dikt) -> 'SpatialClusteringBody':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The spatial_clustering_body of this SpatialClusteringBody.  # noqa: E501
        :rtype: SpatialClusteringBody
        """
        return util.deserialize_model(dikt, cls)

    @property
    def region_coordinates(self) -> List[GeoCoordinate]:
        """Gets the region_coordinates of this SpatialClusteringBody.


        :return: The region_coordinates of this SpatialClusteringBody.
        :rtype: List[GeoCoordinate]
        """
        return self._region_coordinates

    @region_coordinates.setter
    def region_coordinates(self, region_coordinates: List[GeoCoordinate]):
        """Sets the region_coordinates of this SpatialClusteringBody.


        :param region_coordinates: The region_coordinates of this SpatialClusteringBody.
        :type region_coordinates: List[GeoCoordinate]
        """

        self._region_coordinates = region_coordinates

    @property
    def timeframe(self) -> str:
        """Gets the timeframe of this SpatialClusteringBody.


        :return: The timeframe of this SpatialClusteringBody.
        :rtype: str
        """
        return self._timeframe

    @timeframe.setter
    def timeframe(self, timeframe: str):
        """Sets the timeframe of this SpatialClusteringBody.


        :param timeframe: The timeframe of this SpatialClusteringBody.
        :type timeframe: str
        """

        self._timeframe = timeframe

    @property
    def clustering_algorithm(self) -> str:
        """Gets the clustering_algorithm of this SpatialClusteringBody.


        :return: The clustering_algorithm of this SpatialClusteringBody.
        :rtype: str
        """
        return self._clustering_algorithm

    @clustering_algorithm.setter
    def clustering_algorithm(self, clustering_algorithm: str):
        """Sets the clustering_algorithm of this SpatialClusteringBody.


        :param clustering_algorithm: The clustering_algorithm of this SpatialClusteringBody.
        :type clustering_algorithm: str
        """
        allowed_values = ["DBSCAN", "HDBSCAN", "K-means"]  # noqa: E501
        if clustering_algorithm not in allowed_values:
            raise ValueError(
                "Invalid value for `clustering_algorithm` ({0}), must be one of {1}"
                .format(clustering_algorithm, allowed_values)
            )

        self._clustering_algorithm = clustering_algorithm

    @property
    def min_points(self) -> int:
        """Gets the min_points of this SpatialClusteringBody.

        Minimum points to form a cluster  # noqa: E501

        :return: The min_points of this SpatialClusteringBody.
        :rtype: int
        """
        return self._min_points

    @min_points.setter
    def min_points(self, min_points: int):
        """Sets the min_points of this SpatialClusteringBody.

        Minimum points to form a cluster  # noqa: E501

        :param min_points: The min_points of this SpatialClusteringBody.
        :type min_points: int
        """

        self._min_points = min_points

    @property
    def epsilon(self) -> float:
        """Gets the epsilon of this SpatialClusteringBody.

        Maximum distance between points in a cluster  # noqa: E501

        :return: The epsilon of this SpatialClusteringBody.
        :rtype: float
        """
        return self._epsilon

    @epsilon.setter
    def epsilon(self, epsilon: float):
        """Sets the epsilon of this SpatialClusteringBody.

        Maximum distance between points in a cluster  # noqa: E501

        :param epsilon: The epsilon of this SpatialClusteringBody.
        :type epsilon: float
        """

        self._epsilon = epsilon
