# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["CreditGetUsageResponse", "Data", "DataCurrency", "DataSeries", "DataSeriesPoint"]


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


class DataSeriesPoint(BaseModel):
    """A single data point in the credit usage time series"""

    timestamp: datetime
    """The timestamp of the data point"""

    value: float
    """The credit usage value at this point"""


class DataSeries(BaseModel):
    """Credit usage data for a single feature"""

    feature_id: str = FieldInfo(alias="featureId")
    """The feature ID"""

    feature_name: str = FieldInfo(alias="featureName")
    """The display name of the feature"""

    points: List[DataSeriesPoint]
    """Time-series data points for this feature"""

    total_credits: float = FieldInfo(alias="totalCredits")
    """Total credits consumed by this feature in the time range"""


class Data(BaseModel):
    """Credit usage data grouped by feature with time-series points"""

    currency: Optional[DataCurrency] = None
    """The custom currency used for credit measurement"""

    series: List[DataSeries]
    """Credit usage series grouped by feature"""


class CreditGetUsageResponse(BaseModel):
    """Response object"""

    data: Data
    """Credit usage data grouped by feature with time-series points"""
