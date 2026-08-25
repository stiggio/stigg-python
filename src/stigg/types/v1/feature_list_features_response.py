# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "FeatureListFeaturesResponse",
    "EnumConfiguration",
    "Meter",
    "MeterAggregation",
    "MeterFilter",
    "MeterFilterCondition",
    "UnitTransformation",
]


class EnumConfiguration(BaseModel):
    display_name: str = FieldInfo(alias="displayName")
    """The display name for the enum configuration entity"""

    value: str
    """The unique value identifier for the enum configuration entity"""


class MeterAggregation(BaseModel):
    """How the matching events are aggregated into a usage value"""

    function: Literal["SUM", "MAX", "MIN", "AVG", "COUNT", "UNIQUE"]
    """Aggregation function applied to the matching events"""

    field: Optional[str] = None
    """Aggregation field name"""


class MeterFilterCondition(BaseModel):
    """Meter filter condition"""

    field: str
    """Condition field name"""

    operation: Literal[
        "EQUALS",
        "NOT_EQUALS",
        "GREATER_THAN",
        "GREATER_THAN_OR_EQUAL",
        "LESS_THAN",
        "LESS_THAN_OR_EQUAL",
        "IS_NULL",
        "IS_NOT_NULL",
        "CONTAINS",
        "STARTS_WITH",
        "ENDS_WITH",
        "IN",
    ]
    """Comparison applied to the condition field"""

    value: Optional[str] = None
    """Condition value"""

    values: Optional[List[str]] = None


class MeterFilter(BaseModel):
    """A set of conditions an event must all match"""

    conditions: List[MeterFilterCondition]
    """Conditions the event must match"""


class Meter(BaseModel):
    """Event meter that turns reported events into usage for a metered feature"""

    aggregation: MeterAggregation
    """How the matching events are aggregated into a usage value"""

    filters: List[MeterFilter]
    """Event filters. Conditions within a filter are ANDed, and filters are ORed"""


class UnitTransformation(BaseModel):
    """Unit transformation to be applied to the reported usage"""

    divide: float
    """Divide usage by this number"""

    feature_units: Optional[str] = FieldInfo(alias="featureUnits", default=None)
    """Singular feature units after the transformation"""

    feature_units_plural: Optional[str] = FieldInfo(alias="featureUnitsPlural", default=None)
    """Plural feature units after the transformation"""

    round: Literal["UP", "DOWN"]
    """After division, either round the result up or down"""


class FeatureListFeaturesResponse(BaseModel):
    """Feature configuration object"""

    id: str
    """The unique identifier for the feature"""

    created_at: datetime = FieldInfo(alias="createdAt")
    """Timestamp of when the record was created"""

    description: Optional[str] = None
    """The description for the feature"""

    display_name: str = FieldInfo(alias="displayName")
    """The display name for the feature"""

    enum_configuration: Optional[List[EnumConfiguration]] = FieldInfo(alias="enumConfiguration", default=None)
    """The configuration data for the feature"""

    feature_status: Literal["NEW", "SUSPENDED", "ACTIVE"] = FieldInfo(alias="featureStatus")
    """The status of the feature"""

    feature_type: Literal["BOOLEAN", "NUMBER", "ENUM"] = FieldInfo(alias="featureType")
    """The type of the feature"""

    feature_units: Optional[str] = FieldInfo(alias="featureUnits", default=None)
    """The units for the feature"""

    feature_units_plural: Optional[str] = FieldInfo(alias="featureUnitsPlural", default=None)
    """The plural units for the feature"""

    metadata: Dict[str, str]
    """The additional metadata for the feature"""

    meter: Optional[Meter] = None
    """Event meter that turns reported events into usage for a metered feature"""

    meter_type: Literal["None", "FLUCTUATING", "INCREMENTAL"] = FieldInfo(alias="meterType")
    """The meter type for the feature"""

    unit_transformation: Optional[UnitTransformation] = FieldInfo(alias="unitTransformation", default=None)
    """Unit transformation to be applied to the reported usage"""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """Timestamp of when the record was last updated"""
