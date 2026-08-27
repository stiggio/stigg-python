# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ProductUpdateProductParams", "ProductSettings", "UsageResetCutoffRule"]


class ProductUpdateProductParams(TypedDict, total=False):
    description: Optional[str]
    """Description of the product"""

    display_name: Annotated[str, PropertyInfo(alias="displayName")]
    """Display name of the product"""

    metadata: Optional[Dict[str, str]]
    """Additional metadata for the product.

    When included, this replaces the product's entire metadata object rather than
    merging with the existing keys — omit the field to leave existing metadata
    untouched.
    """

    multiple_subscriptions: Annotated[bool, PropertyInfo(alias="multipleSubscriptions")]
    """Indicates if multiple subscriptions to this product are allowed"""

    product_settings: Annotated[ProductSettings, PropertyInfo(alias="productSettings")]

    usage_reset_cutoff_rule: Annotated[UsageResetCutoffRule, PropertyInfo(alias="usageResetCutoffRule")]
    """Rule defining when usage resets upon subscription update."""

    x_account_id: Annotated[str, PropertyInfo(alias="X-ACCOUNT-ID")]

    x_environment_id: Annotated[str, PropertyInfo(alias="X-ENVIRONMENT-ID")]


class ProductSettings(TypedDict, total=False):
    subscription_cancellation_time: Required[
        Annotated[
            Literal["END_OF_BILLING_PERIOD", "IMMEDIATE", "SPECIFIC_DATE"],
            PropertyInfo(alias="subscriptionCancellationTime"),
        ]
    ]
    """Time when the subscription will be cancelled"""

    subscription_end_setup: Required[
        Annotated[Literal["DOWNGRADE_TO_FREE", "CANCEL_SUBSCRIPTION"], PropertyInfo(alias="subscriptionEndSetup")]
    ]
    """Setup for the end of the subscription"""

    subscription_start_setup: Required[
        Annotated[Literal["PLAN_SELECTION", "TRIAL_PERIOD", "FREE_PLAN"], PropertyInfo(alias="subscriptionStartSetup")]
    ]
    """Setup for the start of the subscription"""

    downgrade_plan_id: Annotated[Optional[str], PropertyInfo(alias="downgradePlanId")]
    """ID of the plan to downgrade to at the end of the billing period.

    Only relevant when subscriptionEndSetup is DOWNGRADE_TO_FREE — ignored
    otherwise.
    """

    prorate_at_end_of_billing_period: Annotated[Optional[bool], PropertyInfo(alias="prorateAtEndOfBillingPeriod")]
    """
    Indicates if the subscription should be prorated at the end of the billing
    period
    """

    subscription_start_plan_id: Annotated[Optional[str], PropertyInfo(alias="subscriptionStartPlanId")]
    """ID of the plan to start the subscription with.

    Only relevant when subscriptionStartSetup is PLAN_SELECTION — ignored otherwise.
    """


class UsageResetCutoffRule(TypedDict, total=False):
    """Rule defining when usage resets upon subscription update."""

    behavior: Required[Literal["NEVER_RESET", "ALWAYS_RESET", "BILLING_PERIOD_CHANGE"]]
    """Behavior of the usage reset cutoff rule"""
