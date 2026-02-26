# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["PlanUpdateParams", "DefaultTrialConfig", "DefaultTrialConfigBudget"]


class PlanUpdateParams(TypedDict, total=False):
    billing_id: Annotated[Optional[str], PropertyInfo(alias="billingId")]
    """The unique identifier for the entity in the billing provider"""

    compatible_addon_ids: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="compatibleAddonIds")]

    default_trial_config: Annotated[Optional[DefaultTrialConfig], PropertyInfo(alias="defaultTrialConfig")]
    """Default trial configuration for the plan"""

    description: Optional[str]
    """The description of the package"""

    display_name: Annotated[str, PropertyInfo(alias="displayName")]
    """The display name of the package"""

    metadata: Dict[str, str]
    """Metadata associated with the entity"""

    parent_plan_id: Annotated[Optional[str], PropertyInfo(alias="parentPlanId")]
    """The ID of the parent plan, if applicable"""


class DefaultTrialConfigBudget(TypedDict, total=False):
    """Budget configuration for the trial"""

    has_soft_limit: Required[Annotated[bool, PropertyInfo(alias="hasSoftLimit")]]
    """Whether the budget limit is a soft limit (allows overage) or hard limit"""

    limit: Required[float]
    """The budget limit amount"""


class DefaultTrialConfig(TypedDict, total=False):
    """Default trial configuration for the plan"""

    duration: Required[float]
    """The duration of the trial in the specified units"""

    units: Required[Literal["DAY", "MONTH"]]
    """The time unit for the trial duration (DAY or MONTH)"""

    budget: Optional[DefaultTrialConfigBudget]
    """Budget configuration for the trial"""

    trial_end_behavior: Annotated[
        Optional[Literal["CONVERT_TO_PAID", "CANCEL_SUBSCRIPTION"]], PropertyInfo(alias="trialEndBehavior")
    ]
    """Behavior when the trial ends (CONVERT_TO_PAID or CANCEL_SUBSCRIPTION)"""
