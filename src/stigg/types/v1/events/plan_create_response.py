# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["PlanCreateResponse", "Data", "DataDefaultTrialConfig", "DataDefaultTrialConfigBudget", "DataEntitlement"]


class DataDefaultTrialConfigBudget(BaseModel):
    """Budget configuration for the trial"""

    has_soft_limit: bool = FieldInfo(alias="hasSoftLimit")
    """Whether the budget limit is a soft limit (allows overage) or hard limit"""

    limit: float
    """The budget limit amount"""


class DataDefaultTrialConfig(BaseModel):
    """Default trial configuration for the plan"""

    duration: float
    """The duration of the trial in the specified units"""

    units: Literal["DAY", "MONTH"]
    """The time unit for the trial duration (DAY or MONTH)"""

    budget: Optional[DataDefaultTrialConfigBudget] = None
    """Budget configuration for the trial"""

    trial_end_behavior: Optional[Literal["CONVERT_TO_PAID", "CANCEL_SUBSCRIPTION"]] = FieldInfo(
        alias="trialEndBehavior", default=None
    )
    """Behavior when the trial ends (CONVERT_TO_PAID or CANCEL_SUBSCRIPTION)"""


class DataEntitlement(BaseModel):
    """Entitlement reference with type and identifier"""

    id: str
    """The unique identifier for the entity"""

    type: Literal["FEATURE", "CREDIT"]


class Data(BaseModel):
    """Plan configuration object"""

    id: str
    """The unique identifier for the entity"""

    billing_id: Optional[str] = FieldInfo(alias="billingId", default=None)
    """The unique identifier for the entity in the billing provider"""

    compatible_addon_ids: Optional[List[str]] = FieldInfo(alias="compatibleAddonIds", default=None)

    created_at: datetime = FieldInfo(alias="createdAt")
    """Timestamp of when the record was created"""

    default_trial_config: Optional[DataDefaultTrialConfig] = FieldInfo(alias="defaultTrialConfig", default=None)
    """Default trial configuration for the plan"""

    description: Optional[str] = None
    """The description of the package"""

    display_name: str = FieldInfo(alias="displayName")
    """The display name of the package"""

    entitlements: List[DataEntitlement]
    """List of entitlements of the package"""

    is_latest: Optional[bool] = FieldInfo(alias="isLatest", default=None)
    """Indicates if the package is the latest version"""

    metadata: Dict[str, str]
    """Metadata associated with the entity"""

    parent_plan_id: Optional[str] = FieldInfo(alias="parentPlanId", default=None)
    """The ID of the parent plan, if applicable"""

    pricing_type: Optional[Literal["FREE", "PAID", "CUSTOM"]] = FieldInfo(alias="pricingType", default=None)
    """The pricing type of the package"""

    product_id: str = FieldInfo(alias="productId")
    """The product id of the package"""

    status: Literal["DRAFT", "PUBLISHED", "ARCHIVED"]
    """The status of the package"""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """Timestamp of when the record was last updated"""

    version_number: int = FieldInfo(alias="versionNumber")
    """The version number of the package"""


class PlanCreateResponse(BaseModel):
    """Response object"""

    data: Data
    """Plan configuration object"""
