# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["UsageHistoryResponse", "Data", "DataMarker", "DataSeries", "DataSeriesPoint", "DataSeriesTag"]


class DataMarker(BaseModel):
    """Usage reset or change marker"""

    timestamp: datetime
    """Timestamp of the marker"""

    type: Literal["PERIODIC_RESET", "SUBSCRIPTION_CHANGE_RESET"]
    """Type of marker for a usage history point"""


class DataSeriesPoint(BaseModel):
    """Single usage data point"""

    is_reset_point: bool = FieldInfo(alias="isResetPoint")
    """
    Indicates whether there was usage reset in this point, see `markers` for details
    """

    timestamp: datetime
    """Timestamp of the usage history point"""

    value: float
    """Value of the usage history point"""


class DataSeriesTag(BaseModel):
    """Grouping tag key-value"""

    key: str
    """Key of the tag"""

    value: str
    """Value of the tag"""


class DataSeries(BaseModel):
    """Usage data points with tags"""

    points: List[DataSeriesPoint]
    """Points in the usage history series"""

    tags: List[DataSeriesTag]
    """Tags for the usage history series"""


class Data(BaseModel):
    """Historical usage time series"""

    markers: List[DataMarker]
    """Markers for events that affecting feature usage"""

    series: List[DataSeries]
    """Series of usage history"""


class UsageHistoryResponse(BaseModel):
    """Response object"""

    data: Data
    """Historical usage time series"""
