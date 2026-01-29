# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = [
    "PromotionalEntitlementGrantParams",
    "PromotionalEntitlement",
    "PromotionalEntitlementMonthlyResetPeriodConfiguration",
    "PromotionalEntitlementWeeklyResetPeriodConfiguration",
    "PromotionalEntitlementYearlyResetPeriodConfiguration",
]


class PromotionalEntitlementGrantParams(TypedDict, total=False):
    promotional_entitlements: Required[
        Annotated[Iterable[PromotionalEntitlement], PropertyInfo(alias="promotionalEntitlements")]
    ]
    """Promotional entitlements to grant"""


class PromotionalEntitlementMonthlyResetPeriodConfiguration(TypedDict, total=False):
    """
    The monthly reset period configuration of the entitlement, defined when reset period is monthly
    """

    according_to: Required[
        Annotated[Literal["SubscriptionStart", "StartOfTheMonth"], PropertyInfo(alias="accordingTo")]
    ]
    """Reset anchor (SubscriptionStart or StartOfTheMonth)"""


class PromotionalEntitlementWeeklyResetPeriodConfiguration(TypedDict, total=False):
    """
    The weekly reset period configuration of the entitlement, defined when reset period is weekly
    """

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


class PromotionalEntitlementYearlyResetPeriodConfiguration(TypedDict, total=False):
    """
    The yearly reset period configuration of the entitlement, defined when reset period is yearly
    """

    according_to: Required[Annotated[Literal["SubscriptionStart"], PropertyInfo(alias="accordingTo")]]
    """Reset anchor (SubscriptionStart)"""


class PromotionalEntitlement(TypedDict, total=False):
    """Single entitlement grant config"""

    custom_end_date: Required[
        Annotated[Union[str, datetime, None], PropertyInfo(alias="customEndDate", format="iso8601")]
    ]
    """The custom end date of the promotional entitlement"""

    enum_values: Required[Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="enumValues")]]
    """The enum values of the entitlement"""

    feature_id: Required[Annotated[str, PropertyInfo(alias="featureId")]]
    """The unique identifier of the entitlement feature"""

    has_soft_limit: Required[Annotated[Optional[bool], PropertyInfo(alias="hasSoftLimit")]]
    """Whether the entitlement has a soft limit"""

    has_unlimited_usage: Required[Annotated[Optional[bool], PropertyInfo(alias="hasUnlimitedUsage")]]
    """Whether the entitlement has an unlimited usage"""

    is_visible: Required[Annotated[Optional[bool], PropertyInfo(alias="isVisible")]]
    """Whether the entitlement is visible"""

    monthly_reset_period_configuration: Required[
        Annotated[
            Optional[PromotionalEntitlementMonthlyResetPeriodConfiguration],
            PropertyInfo(alias="monthlyResetPeriodConfiguration"),
        ]
    ]
    """
    The monthly reset period configuration of the entitlement, defined when reset
    period is monthly
    """

    period: Required[Literal["1 week", "1 month", "6 month", "1 year", "lifetime", "custom"]]
    """The grant period of the promotional entitlement"""

    reset_period: Required[
        Annotated[Optional[Literal["YEAR", "MONTH", "WEEK", "DAY", "HOUR"]], PropertyInfo(alias="resetPeriod")]
    ]
    """The reset period of the entitlement"""

    usage_limit: Required[Annotated[Optional[int], PropertyInfo(alias="usageLimit")]]
    """The usage limit of the entitlement"""

    weekly_reset_period_configuration: Required[
        Annotated[
            Optional[PromotionalEntitlementWeeklyResetPeriodConfiguration],
            PropertyInfo(alias="weeklyResetPeriodConfiguration"),
        ]
    ]
    """
    The weekly reset period configuration of the entitlement, defined when reset
    period is weekly
    """

    yearly_reset_period_configuration: Required[
        Annotated[
            Optional[PromotionalEntitlementYearlyResetPeriodConfiguration],
            PropertyInfo(alias="yearlyResetPeriodConfiguration"),
        ]
    ]
    """
    The yearly reset period configuration of the entitlement, defined when reset
    period is yearly
    """
