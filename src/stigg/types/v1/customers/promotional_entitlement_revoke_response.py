# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "PromotionalEntitlementRevokeResponse",
    "Data",
    "DataResetPeriodConfiguration",
    "DataResetPeriodConfigurationYearlyResetPeriodConfig",
    "DataResetPeriodConfigurationMonthlyResetPeriodConfig",
    "DataResetPeriodConfigurationWeeklyResetPeriodConfig",
]


class DataResetPeriodConfigurationYearlyResetPeriodConfig(BaseModel):
    """Yearly reset configuration"""

    according_to: Literal["SubscriptionStart"] = FieldInfo(alias="accordingTo")
    """Reset anchor (SubscriptionStart)"""


class DataResetPeriodConfigurationMonthlyResetPeriodConfig(BaseModel):
    """Monthly reset configuration"""

    according_to: Literal["SubscriptionStart", "StartOfTheMonth"] = FieldInfo(alias="accordingTo")
    """Reset anchor (SubscriptionStart or StartOfTheMonth)"""


class DataResetPeriodConfigurationWeeklyResetPeriodConfig(BaseModel):
    """Weekly reset configuration"""

    according_to: Literal[
        "SubscriptionStart",
        "EverySunday",
        "EveryMonday",
        "EveryTuesday",
        "EveryWednesday",
        "EveryThursday",
        "EveryFriday",
        "EverySaturday",
    ] = FieldInfo(alias="accordingTo")
    """Reset anchor (SubscriptionStart or specific day)"""


DataResetPeriodConfiguration: TypeAlias = Union[
    DataResetPeriodConfigurationYearlyResetPeriodConfig,
    DataResetPeriodConfigurationMonthlyResetPeriodConfig,
    DataResetPeriodConfigurationWeeklyResetPeriodConfig,
    None,
]


class Data(BaseModel):
    """Granted feature entitlement"""

    id: str
    """Unique identifier for the entity"""

    created_at: datetime = FieldInfo(alias="createdAt")
    """Timestamp of when the record was created"""

    description: Optional[str] = None
    """The description of the entitlement"""

    end_date: Optional[datetime] = FieldInfo(alias="endDate", default=None)
    """The end date of the promotional entitlement"""

    enum_values: Optional[List[str]] = FieldInfo(alias="enumValues", default=None)
    """The enum values of the entitlement"""

    environment_id: str = FieldInfo(alias="environmentId")
    """The unique identifier for the environment"""

    feature_group_ids: Optional[List[str]] = FieldInfo(alias="featureGroupIds", default=None)
    """Feature group IDs associated with this entitlement"""

    feature_id: str = FieldInfo(alias="featureId")
    """The unique identifier of the entitlement feature"""

    has_soft_limit: Optional[bool] = FieldInfo(alias="hasSoftLimit", default=None)
    """Whether the entitlement has a soft limit"""

    has_unlimited_usage: Optional[bool] = FieldInfo(alias="hasUnlimitedUsage", default=None)
    """Whether the entitlement has an unlimited usage"""

    is_visible: bool = FieldInfo(alias="isVisible")
    """Whether the entitlement is visible"""

    period: Literal["1 week", "1 month", "6 month", "1 year", "lifetime", "custom"]
    """The grant period of the promotional entitlement"""

    reset_period: Optional[Literal["YEAR", "MONTH", "WEEK", "DAY", "HOUR"]] = FieldInfo(
        alias="resetPeriod", default=None
    )
    """The reset period of the entitlement"""

    reset_period_configuration: Optional[DataResetPeriodConfiguration] = FieldInfo(
        alias="resetPeriodConfiguration", default=None
    )
    """The reset period configuration of the entitlement"""

    start_date: datetime = FieldInfo(alias="startDate")
    """The start date of the entitlement"""

    status: Literal["Active", "Expired", "Paused"]
    """The status of the entitlement"""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """Timestamp of when the record was last updated"""

    usage_limit: Optional[float] = FieldInfo(alias="usageLimit", default=None)
    """The usage limit of the entitlement"""


class PromotionalEntitlementRevokeResponse(BaseModel):
    """Response object"""

    data: Data
    """Granted feature entitlement"""
