# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = [
    "EntitlementUpdateParams",
    "Credit",
    "Feature",
    "FeatureMonthlyResetPeriodConfiguration",
    "FeatureWeeklyResetPeriodConfiguration",
    "FeatureYearlyResetPeriodConfiguration",
]


class EntitlementUpdateParams(TypedDict, total=False):
    addon_id: Required[Annotated[str, PropertyInfo(alias="addonId")]]

    credit: Credit
    """Credit entitlement fields to update"""

    feature: Feature
    """Feature entitlement fields to update"""


class Credit(TypedDict, total=False):
    """Credit entitlement fields to update"""

    amount: float
    """Credit grant amount"""

    behavior: Literal["Increment", "Override"]
    """Entitlement behavior (Increment or Override)"""

    cadence: Literal["MONTH", "YEAR"]
    """Credit grant cadence (MONTH or YEAR)"""

    description: str
    """Description of the entitlement"""

    display_name_override: Annotated[str, PropertyInfo(alias="displayNameOverride")]
    """Override display name for the entitlement"""

    hidden_from_widgets: Annotated[
        List[Literal["PAYWALL", "CUSTOMER_PORTAL", "CHECKOUT"]], PropertyInfo(alias="hiddenFromWidgets")
    ]
    """Widget types where this entitlement is hidden"""

    is_custom: Annotated[bool, PropertyInfo(alias="isCustom")]
    """Whether this is a custom entitlement"""

    is_granted: Annotated[bool, PropertyInfo(alias="isGranted")]
    """Whether the entitlement is granted"""

    order: float
    """Display order of the entitlement"""


class FeatureMonthlyResetPeriodConfiguration(TypedDict, total=False):
    """Configuration for monthly reset period"""

    according_to: Required[
        Annotated[Literal["SubscriptionStart", "StartOfTheMonth"], PropertyInfo(alias="accordingTo")]
    ]
    """Reset anchor (SubscriptionStart or StartOfTheMonth)"""


class FeatureWeeklyResetPeriodConfiguration(TypedDict, total=False):
    """Configuration for weekly reset period"""

    according_to: Required[
        Annotated[
            Literal[
                "SubscriptionStart",
                "EverySunday",
                "EveryMonday",
                "EveryTuesday",
                "EveryWednesday",
                "EveryThursday",
                "EveryFriday",
                "EverySaturday",
            ],
            PropertyInfo(alias="accordingTo"),
        ]
    ]
    """Reset anchor (SubscriptionStart or specific day)"""


class FeatureYearlyResetPeriodConfiguration(TypedDict, total=False):
    """Configuration for yearly reset period"""

    according_to: Required[Annotated[Literal["SubscriptionStart"], PropertyInfo(alias="accordingTo")]]
    """Reset anchor (SubscriptionStart)"""


class Feature(TypedDict, total=False):
    """Feature entitlement fields to update"""

    behavior: Literal["Increment", "Override"]
    """Entitlement behavior (Increment or Override)"""

    description: str
    """Description of the entitlement"""

    display_name_override: Annotated[str, PropertyInfo(alias="displayNameOverride")]
    """Override display name for the entitlement"""

    enum_values: Annotated[SequenceNotStr[str], PropertyInfo(alias="enumValues")]
    """Allowed enum values for the feature entitlement"""

    has_soft_limit: Annotated[bool, PropertyInfo(alias="hasSoftLimit")]
    """Whether the usage limit is a soft limit"""

    has_unlimited_usage: Annotated[bool, PropertyInfo(alias="hasUnlimitedUsage")]
    """Whether usage is unlimited"""

    hidden_from_widgets: Annotated[
        List[Literal["PAYWALL", "CUSTOMER_PORTAL", "CHECKOUT"]], PropertyInfo(alias="hiddenFromWidgets")
    ]
    """Widget types where this entitlement is hidden"""

    is_custom: Annotated[bool, PropertyInfo(alias="isCustom")]
    """Whether this is a custom entitlement"""

    is_granted: Annotated[bool, PropertyInfo(alias="isGranted")]
    """Whether the entitlement is granted"""

    monthly_reset_period_configuration: Annotated[
        Optional[FeatureMonthlyResetPeriodConfiguration], PropertyInfo(alias="monthlyResetPeriodConfiguration")
    ]
    """Configuration for monthly reset period"""

    order: float
    """Display order of the entitlement"""

    reset_period: Annotated[Literal["YEAR", "MONTH", "WEEK", "DAY", "HOUR"], PropertyInfo(alias="resetPeriod")]
    """Period at which usage resets"""

    usage_limit: Annotated[Optional[int], PropertyInfo(alias="usageLimit")]
    """Maximum allowed usage for the feature"""

    weekly_reset_period_configuration: Annotated[
        Optional[FeatureWeeklyResetPeriodConfiguration], PropertyInfo(alias="weeklyResetPeriodConfiguration")
    ]
    """Configuration for weekly reset period"""

    yearly_reset_period_configuration: Annotated[
        Optional[FeatureYearlyResetPeriodConfiguration], PropertyInfo(alias="yearlyResetPeriodConfiguration")
    ]
    """Configuration for yearly reset period"""
