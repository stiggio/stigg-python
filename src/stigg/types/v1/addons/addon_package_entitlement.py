# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from ...._utils import PropertyInfo
from ...._models import BaseModel

__all__ = [
    "AddonPackageEntitlement",
    "Data",
    "DataFeature",
    "DataFeatureResetPeriodConfiguration",
    "DataFeatureResetPeriodConfigurationYearlyResetPeriodConfig",
    "DataFeatureResetPeriodConfigurationMonthlyResetPeriodConfig",
    "DataFeatureResetPeriodConfigurationWeeklyResetPeriodConfig",
    "DataCredit",
]


class DataFeatureResetPeriodConfigurationYearlyResetPeriodConfig(BaseModel):
    """Yearly reset configuration"""

    according_to: Literal["SubscriptionStart"] = FieldInfo(alias="accordingTo")
    """Reset anchor (SubscriptionStart)"""


class DataFeatureResetPeriodConfigurationMonthlyResetPeriodConfig(BaseModel):
    """Monthly reset configuration"""

    according_to: Literal["SubscriptionStart", "StartOfTheMonth"] = FieldInfo(alias="accordingTo")
    """Reset anchor (SubscriptionStart or StartOfTheMonth)"""


class DataFeatureResetPeriodConfigurationWeeklyResetPeriodConfig(BaseModel):
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


DataFeatureResetPeriodConfiguration: TypeAlias = Union[
    DataFeatureResetPeriodConfigurationYearlyResetPeriodConfig,
    DataFeatureResetPeriodConfigurationMonthlyResetPeriodConfig,
    DataFeatureResetPeriodConfigurationWeeklyResetPeriodConfig,
    None,
]


class DataFeature(BaseModel):
    """Feature entitlement response"""

    id: str
    """Unique identifier of the entitlement"""

    behavior: Literal["Increment", "Override"]
    """Entitlement behavior (Increment or Override)"""

    created_at: datetime = FieldInfo(alias="createdAt")
    """Timestamp of when the record was created"""

    description: Optional[str] = None
    """Optional description of the entitlement"""

    display_name_override: Optional[str] = FieldInfo(alias="displayNameOverride", default=None)
    """Override display name for the entitlement"""

    enum_values: Optional[List[str]] = FieldInfo(alias="enumValues", default=None)
    """Allowed enum values (for feature entitlements)"""

    has_soft_limit: Optional[bool] = FieldInfo(alias="hasSoftLimit", default=None)
    """Whether the usage limit is a soft limit (for feature entitlements)"""

    has_unlimited_usage: Optional[bool] = FieldInfo(alias="hasUnlimitedUsage", default=None)
    """Whether usage is unlimited (for feature entitlements)"""

    hidden_from_widgets: List[Literal["PAYWALL", "CUSTOMER_PORTAL", "CHECKOUT"]] = FieldInfo(alias="hiddenFromWidgets")
    """Widget types where this entitlement is hidden"""

    is_custom: Optional[bool] = FieldInfo(alias="isCustom", default=None)
    """Whether this is a custom entitlement"""

    is_granted: bool = FieldInfo(alias="isGranted")
    """Whether the entitlement is granted"""

    order: Optional[float] = None
    """Display order of the entitlement"""

    reset_period: Optional[Literal["YEAR", "MONTH", "WEEK", "DAY", "HOUR"]] = FieldInfo(
        alias="resetPeriod", default=None
    )
    """Usage reset period (for feature entitlements)"""

    reset_period_configuration: Optional[DataFeatureResetPeriodConfiguration] = FieldInfo(
        alias="resetPeriodConfiguration", default=None
    )
    """Reset period configuration (for feature entitlements)"""

    type: Literal["FEATURE"]
    """Entitlement type (FEATURE or CREDIT)"""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """Timestamp of when the record was last updated"""

    usage_limit: Optional[float] = FieldInfo(alias="usageLimit", default=None)
    """Usage limit (for feature entitlements)"""


class DataCredit(BaseModel):
    """Credit entitlement response"""

    id: str
    """Unique identifier of the entitlement"""

    amount: Optional[float] = None
    """Credit amount (for credit entitlements)"""

    behavior: Literal["Increment", "Override"]
    """Entitlement behavior (Increment or Override)"""

    cadence: Optional[Literal["MONTH", "YEAR"]] = None
    """Credit grant cadence (for credit entitlements)"""

    created_at: datetime = FieldInfo(alias="createdAt")
    """Timestamp of when the record was created"""

    description: Optional[str] = None
    """Optional description of the entitlement"""

    display_name_override: Optional[str] = FieldInfo(alias="displayNameOverride", default=None)
    """Override display name for the entitlement"""

    hidden_from_widgets: List[Literal["PAYWALL", "CUSTOMER_PORTAL", "CHECKOUT"]] = FieldInfo(alias="hiddenFromWidgets")
    """Widget types where this entitlement is hidden"""

    is_custom: Optional[bool] = FieldInfo(alias="isCustom", default=None)
    """Whether this is a custom entitlement"""

    is_granted: bool = FieldInfo(alias="isGranted")
    """Whether the entitlement is granted"""

    order: Optional[float] = None
    """Display order of the entitlement"""

    type: Literal["CREDIT"]
    """Entitlement type (FEATURE or CREDIT)"""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """Timestamp of when the record was last updated"""


Data: TypeAlias = Annotated[Union[DataFeature, DataCredit], PropertyInfo(discriminator="type")]


class AddonPackageEntitlement(BaseModel):
    """Response object"""

    data: Data
    """Feature entitlement response"""
