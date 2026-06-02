# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "CreditGetUsageResponse",
    "Data",
    "DataCurrency",
    "DataPagination",
    "DataSeries",
    "DataSeriesPoint",
    "DataSeriesTag",
]


class DataCurrency(BaseModel):
    """The custom currency used for credit measurement"""

    currency_id: str = FieldInfo(alias="currencyId")
    """The currency identifier"""

    display_name: str = FieldInfo(alias="displayName")
    """The display name of the currency"""

    plural: Optional[str] = None
    """Plural unit label"""

    singular: Optional[str] = None
    """Singular unit label"""

    symbol: Optional[str] = None
    """The currency symbol"""


class DataPagination(BaseModel):
    """Cursor-based pagination for the returned series.

    `next`/`prev` are opaque cursors; pass them back as `after`/`before` to traverse pages. The series axis is `groupBy` when provided, otherwise `featureId`
    """

    next: Optional[str] = None
    """
    Cursor for fetching the next page of results, or null if no additional pages
    exist
    """

    prev: Optional[str] = None
    """Cursor for fetching the previous page of results, or null if at the beginning"""


class DataSeriesPoint(BaseModel):
    """A single data point in the credit usage time series"""

    timestamp: datetime
    """The timestamp of the data point"""

    value: float
    """The credit usage value at this point"""


class DataSeriesTag(BaseModel):
    """Dimension key/value pair identifying a credit usage series"""

    key: str
    """The dimension key"""

    value: str
    """The dimension value for this series"""


class DataSeries(BaseModel):
    """Credit usage data for a single feature"""

    feature_id: Optional[str] = FieldInfo(alias="featureId", default=None)
    """The feature ID; null when grouping by dimensions only"""

    feature_name: Optional[str] = FieldInfo(alias="featureName", default=None)
    """The display name of the feature; null when grouping by dimensions only"""

    points: List[DataSeriesPoint]
    """Time-series data points for this feature"""

    total_credits: float = FieldInfo(alias="totalCredits")
    """Total credits consumed by this feature in the time range"""

    tags: Optional[List[DataSeriesTag]] = None
    """Dimension key/value pairs identifying this series when groupBy is applied"""


class Data(BaseModel):
    """Credit usage data grouped by feature with time-series points"""

    currency: Optional[DataCurrency] = None
    """The custom currency used for credit measurement"""

    pagination: DataPagination
    """Cursor-based pagination for the returned series.

    `next`/`prev` are opaque cursors; pass them back as `after`/`before` to traverse
    pages. The series axis is `groupBy` when provided, otherwise `featureId`
    """

    series: List[DataSeries]
    """Credit usage series grouped by feature"""


class CreditGetUsageResponse(BaseModel):
    """Response object"""

    data: Data
    """Credit usage data grouped by feature with time-series points"""
