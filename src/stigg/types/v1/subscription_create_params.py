# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SubscriptionCreateParams", "CheckoutOptions", "TrialOverrideConfiguration"]


class SubscriptionCreateParams(TypedDict, total=False):
    customer_id: Required[Annotated[str, PropertyInfo(alias="customerId")]]
    """Customer ID to provision the subscription for"""

    plan_id: Required[Annotated[str, PropertyInfo(alias="planId")]]
    """Plan ID to provision"""

    id: Optional[str]
    """Unique identifier for the subscription"""

    await_payment_confirmation: Annotated[bool, PropertyInfo(alias="awaitPaymentConfirmation")]
    """Whether to wait for payment confirmation before returning the subscription"""

    billing_period: Annotated[Literal["MONTHLY", "ANNUALLY"], PropertyInfo(alias="billingPeriod")]

    checkout_options: Annotated[CheckoutOptions, PropertyInfo(alias="checkoutOptions")]

    metadata: Dict[str, str]
    """Additional metadata for the subscription"""

    paying_customer_id: Annotated[Optional[str], PropertyInfo(alias="payingCustomerId")]
    """Optional paying customer ID for split billing scenarios"""

    resource_id: Annotated[Optional[str], PropertyInfo(alias="resourceId")]
    """Optional resource ID for multi-instance subscriptions"""

    trial_override_configuration: Annotated[
        TrialOverrideConfiguration, PropertyInfo(alias="trialOverrideConfiguration")
    ]


class CheckoutOptions(TypedDict, total=False):
    cancel_url: Required[Annotated[str, PropertyInfo(alias="cancelUrl")]]
    """URL to redirect to if checkout is canceled"""

    success_url: Required[Annotated[str, PropertyInfo(alias="successUrl")]]
    """URL to redirect to after successful checkout"""

    allow_promo_codes: Annotated[bool, PropertyInfo(alias="allowPromoCodes")]
    """Allow promotional codes during checkout"""

    allow_tax_id_collection: Annotated[bool, PropertyInfo(alias="allowTaxIdCollection")]
    """Allow tax ID collection during checkout"""

    collect_billing_address: Annotated[bool, PropertyInfo(alias="collectBillingAddress")]
    """Collect billing address during checkout"""

    collect_phone_number: Annotated[bool, PropertyInfo(alias="collectPhoneNumber")]
    """Collect phone number during checkout"""

    reference_id: Annotated[Optional[str], PropertyInfo(alias="referenceId")]
    """Optional reference ID for the checkout session"""


class TrialOverrideConfiguration(TypedDict, total=False):
    is_trial: Required[Annotated[bool, PropertyInfo(alias="isTrial")]]
    """Whether the subscription should start with a trial period"""

    trial_end_behavior: Annotated[
        Literal["CONVERT_TO_PAID", "CANCEL_SUBSCRIPTION"], PropertyInfo(alias="trialEndBehavior")
    ]
    """Behavior when trial ends: CONVERT_TO_PAID or CANCEL_SUBSCRIPTION"""

    trial_end_date: Annotated[Union[str, datetime], PropertyInfo(alias="trialEndDate", format="iso8601")]
    """Custom trial end date"""
