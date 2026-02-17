# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["FeatureCreateFeatureParams", "EnumConfiguration", "UnitTransformation"]


class FeatureCreateFeatureParams(TypedDict, total=False):
    id: Required[str]
    """The unique identifier for the feature"""

    display_name: Required[Annotated[str, PropertyInfo(alias="displayName")]]
    """The display name for the feature"""

    feature_type: Required[Annotated[Literal["BOOLEAN", "NUMBER", "ENUM"], PropertyInfo(alias="featureType")]]
    """The type of the feature"""

    description: str
    """The description for the feature"""

    enum_configuration: Annotated[Iterable[EnumConfiguration], PropertyInfo(alias="enumConfiguration")]
    """The configuration data for the feature"""

    feature_status: Annotated[Literal["NEW", "SUSPENDED", "ACTIVE"], PropertyInfo(alias="featureStatus")]
    """The status of the feature"""

    feature_units: Annotated[str, PropertyInfo(alias="featureUnits")]
    """The units for the feature"""

    feature_units_plural: Annotated[str, PropertyInfo(alias="featureUnitsPlural")]
    """The plural units for the feature"""

    metadata: Dict[str, str]
    """The additional metadata for the feature"""

    meter_type: Annotated[Literal["None", "FLUCTUATING", "INCREMENTAL"], PropertyInfo(alias="meterType")]
    """The meter type for the feature"""

    unit_transformation: Annotated[Optional[UnitTransformation], PropertyInfo(alias="unitTransformation")]
    """Unit transformation to be applied to the reported usage"""


class EnumConfiguration(TypedDict, total=False):
    display_name: Required[Annotated[str, PropertyInfo(alias="displayName")]]
    """The display name for the enum configuration entity"""

    value: Required[str]
    """The unique value identifier for the enum configuration entity"""


class UnitTransformation(TypedDict, total=False):
    """Unit transformation to be applied to the reported usage"""

    divide: Required[int]
    """Divide usage by this number"""

    feature_units: Annotated[str, PropertyInfo(alias="featureUnits")]
    """Singular feature units after the transformation"""

    feature_units_plural: Annotated[str, PropertyInfo(alias="featureUnitsPlural")]
    """Plural feature units after the transformation"""

    round: Literal["UP", "DOWN"]
    """After division, either round the result up or down"""
