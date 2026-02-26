# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["Feature", "Data", "DataEnumConfiguration", "DataUnitTransformation"]


class DataEnumConfiguration(BaseModel):
    display_name: str = FieldInfo(alias="displayName")
    """The display name for the enum configuration entity"""

    value: str
    """The unique value identifier for the enum configuration entity"""


class DataUnitTransformation(BaseModel):
    """Unit transformation to be applied to the reported usage"""

    divide: float
    """Divide usage by this number"""

    feature_units: Optional[str] = FieldInfo(alias="featureUnits", default=None)
    """Singular feature units after the transformation"""

    feature_units_plural: Optional[str] = FieldInfo(alias="featureUnitsPlural", default=None)
    """Plural feature units after the transformation"""

    round: Literal["UP", "DOWN"]
    """After division, either round the result up or down"""


class Data(BaseModel):
    """Feature configuration object"""

    id: str
    """The unique identifier for the feature"""

    created_at: datetime = FieldInfo(alias="createdAt")
    """Timestamp of when the record was created"""

    description: Optional[str] = None
    """The description for the feature"""

    display_name: str = FieldInfo(alias="displayName")
    """The display name for the feature"""

    enum_configuration: Optional[List[DataEnumConfiguration]] = FieldInfo(alias="enumConfiguration", default=None)
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

    meter_type: Literal["None", "FLUCTUATING", "INCREMENTAL"] = FieldInfo(alias="meterType")
    """The meter type for the feature"""

    unit_transformation: Optional[DataUnitTransformation] = FieldInfo(alias="unitTransformation", default=None)
    """Unit transformation to be applied to the reported usage"""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """Timestamp of when the record was last updated"""


class Feature(BaseModel):
    """Response object"""

    data: Data
    """Feature configuration object"""
