# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = [
    "FeatureUpdateFeatureParams",
    "EnumConfiguration",
    "Meter",
    "MeterAggregation",
    "MeterFilter",
    "MeterFilterCondition",
    "UnitTransformation",
]


class FeatureUpdateFeatureParams(TypedDict, total=False):
    description: str
    """The description for the feature"""

    display_name: Annotated[str, PropertyInfo(alias="displayName")]
    """The display name for the feature"""

    enum_configuration: Annotated[Iterable[EnumConfiguration], PropertyInfo(alias="enumConfiguration")]
    """The configuration data for the feature"""

    feature_units: Annotated[str, PropertyInfo(alias="featureUnits")]
    """The units for the feature"""

    feature_units_plural: Annotated[str, PropertyInfo(alias="featureUnitsPlural")]
    """The plural units for the feature"""

    metadata: Dict[str, str]
    """The additional metadata for the feature"""

    meter: Meter

    unit_transformation: Annotated[Optional[UnitTransformation], PropertyInfo(alias="unitTransformation")]
    """Unit transformation to be applied to the reported usage"""


class EnumConfiguration(TypedDict, total=False):
    display_name: Required[Annotated[str, PropertyInfo(alias="displayName")]]
    """The display name for the enum configuration entity"""

    value: Required[str]
    """The unique value identifier for the enum configuration entity"""


class MeterAggregation(TypedDict, total=False):
    function: Required[Literal["SUM", "MAX", "MIN", "AVG", "COUNT", "UNIQUE"]]

    field: str


class MeterFilterCondition(TypedDict, total=False):
    field: Required[str]

    operation: Required[
        Literal[
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
    ]

    value: str

    values: SequenceNotStr[str]


class MeterFilter(TypedDict, total=False):
    conditions: Required[Iterable[MeterFilterCondition]]


class Meter(TypedDict, total=False):
    aggregation: Required[MeterAggregation]

    filters: Required[Iterable[MeterFilter]]


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
