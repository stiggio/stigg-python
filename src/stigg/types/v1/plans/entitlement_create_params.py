# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = [
    "EntitlementCreateParams",
    "Entitlement",
    "EntitlementCredit",
    "EntitlementFeature",
    "EntitlementFeatureMonthlyResetPeriodConfiguration",
    "EntitlementFeatureWeeklyResetPeriodConfiguration",
    "EntitlementFeatureYearlyResetPeriodConfiguration",
]


class EntitlementCreateParams(TypedDict, total=False):
    entitlements: Required[Iterable[Entitlement]]
    """Entitlements to create"""


class EntitlementCredit(TypedDict, total=False):
    """Credit entitlement to create"""

    amount: Required[Optional[float]]
    """Credit grant amount"""

    cadence: Required[Literal["MONTH", "YEAR"]]
    """Credit grant cadence (MONTH or YEAR)"""

    custom_currency_id: Required[Annotated[str, PropertyInfo(alias="customCurrencyId")]]
    """The custom currency ID for the credit entitlement"""

    behavior: Literal["Increment", "Override"]
    """Entitlement behavior (Increment or Override)"""

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


class EntitlementFeatureMonthlyResetPeriodConfiguration(TypedDict, total=False):
    """Configuration for monthly reset period"""

    according_to: Required[
        Annotated[Literal["SubscriptionStart", "StartOfTheMonth"], PropertyInfo(alias="accordingTo")]
    ]
    """Reset anchor (SubscriptionStart or StartOfTheMonth)"""


class EntitlementFeatureWeeklyResetPeriodConfiguration(TypedDict, total=False):
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


class EntitlementFeatureYearlyResetPeriodConfiguration(TypedDict, total=False):
    """Configuration for yearly reset period"""

    according_to: Required[Annotated[Literal["SubscriptionStart"], PropertyInfo(alias="accordingTo")]]
    """Reset anchor (SubscriptionStart)"""


class EntitlementFeature(TypedDict, total=False):
    """Feature entitlement to create"""

    feature_id: Required[Annotated[str, PropertyInfo(alias="featureId")]]
    """The feature ID to attach the entitlement to"""

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
        Optional[EntitlementFeatureMonthlyResetPeriodConfiguration],
        PropertyInfo(alias="monthlyResetPeriodConfiguration"),
    ]
    """Configuration for monthly reset period"""

    order: float
    """Display order of the entitlement"""

    reset_period: Annotated[Literal["YEAR", "MONTH", "WEEK", "DAY", "HOUR"], PropertyInfo(alias="resetPeriod")]
    """Period at which usage resets"""

    usage_limit: Annotated[Optional[int], PropertyInfo(alias="usageLimit")]
    """Maximum allowed usage for the feature"""

    weekly_reset_period_configuration: Annotated[
        Optional[EntitlementFeatureWeeklyResetPeriodConfiguration], PropertyInfo(alias="weeklyResetPeriodConfiguration")
    ]
    """Configuration for weekly reset period"""

    yearly_reset_period_configuration: Annotated[
        Optional[EntitlementFeatureYearlyResetPeriodConfiguration], PropertyInfo(alias="yearlyResetPeriodConfiguration")
    ]
    """Configuration for yearly reset period"""


class Entitlement(TypedDict, total=False):
    """A single entitlement to create. Provide exactly one of feature or credit."""

    credit: EntitlementCredit
    """Credit entitlement to create"""

    feature: EntitlementFeature
    """Feature entitlement to create"""
