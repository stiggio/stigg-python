# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = [
    "SubscriptionPreviewParams",
    "Addon",
    "AppliedCoupon",
    "AppliedCouponConfiguration",
    "AppliedCouponDiscount",
    "AppliedCouponDiscountAmountsOff",
    "BillableFeature",
    "BillingInformation",
    "BillingInformationBillingAddress",
    "BillingInformationTaxID",
    "Charge",
    "TrialOverrideConfiguration",
]


class SubscriptionPreviewParams(TypedDict, total=False):
    customer_id: Required[Annotated[str, PropertyInfo(alias="customerId")]]
    """Customer ID"""

    plan_id: Required[Annotated[str, PropertyInfo(alias="planId")]]
    """Plan ID"""

    addons: Iterable[Addon]
    """Addons to include"""

    applied_coupon: Annotated[AppliedCoupon, PropertyInfo(alias="appliedCoupon")]
    """Coupon or discount to apply"""

    billable_features: Annotated[Iterable[BillableFeature], PropertyInfo(alias="billableFeatures")]
    """Billable features with quantities"""

    billing_country_code: Annotated[str, PropertyInfo(alias="billingCountryCode")]
    """ISO 3166-1 country code for localization"""

    billing_information: Annotated[BillingInformation, PropertyInfo(alias="billingInformation")]
    """Billing and tax configuration"""

    billing_period: Annotated[Literal["MONTHLY", "ANNUALLY"], PropertyInfo(alias="billingPeriod")]
    """Billing period (MONTHLY or ANNUALLY)"""

    charges: Iterable[Charge]
    """One-time or recurring charges"""

    paying_customer_id: Annotated[str, PropertyInfo(alias="payingCustomerId")]
    """Paying customer ID for delegated billing"""

    resource_id: Annotated[str, PropertyInfo(alias="resourceId")]
    """Resource ID for multi-instance subscriptions"""

    schedule_strategy: Annotated[
        Literal["END_OF_BILLING_PERIOD", "END_OF_BILLING_MONTH", "IMMEDIATE"], PropertyInfo(alias="scheduleStrategy")
    ]
    """When to apply subscription changes"""

    start_date: Annotated[Union[str, datetime], PropertyInfo(alias="startDate", format="iso8601")]
    """Subscription start date"""

    trial_override_configuration: Annotated[
        TrialOverrideConfiguration, PropertyInfo(alias="trialOverrideConfiguration")
    ]
    """Trial period override settings"""

    unit_quantity: Annotated[float, PropertyInfo(alias="unitQuantity")]
    """Unit quantity for per-unit pricing"""


class Addon(TypedDict, total=False):
    """Addon configuration"""

    addon_id: Required[Annotated[str, PropertyInfo(alias="addonId")]]
    """Addon ID"""

    quantity: int
    """Number of addon instances"""


class AppliedCouponConfiguration(TypedDict, total=False):
    """Coupon timing configuration"""

    start_date: Annotated[Union[str, datetime], PropertyInfo(alias="startDate", format="iso8601")]
    """Coupon start date"""


class AppliedCouponDiscountAmountsOff(TypedDict, total=False):
    amount: Required[float]
    """The price amount"""

    currency: Required[
        Literal[
            "usd",
            "aed",
            "all",
            "amd",
            "ang",
            "aud",
            "awg",
            "azn",
            "bam",
            "bbd",
            "bdt",
            "bgn",
            "bif",
            "bmd",
            "bnd",
            "bsd",
            "bwp",
            "byn",
            "bzd",
            "brl",
            "cad",
            "cdf",
            "chf",
            "cny",
            "czk",
            "dkk",
            "dop",
            "dzd",
            "egp",
            "etb",
            "eur",
            "fjd",
            "gbp",
            "gel",
            "gip",
            "gmd",
            "gyd",
            "hkd",
            "hrk",
            "htg",
            "idr",
            "ils",
            "inr",
            "isk",
            "jmd",
            "jpy",
            "kes",
            "kgs",
            "khr",
            "kmf",
            "krw",
            "kyd",
            "kzt",
            "lbp",
            "lkr",
            "lrd",
            "lsl",
            "mad",
            "mdl",
            "mga",
            "mkd",
            "mmk",
            "mnt",
            "mop",
            "mro",
            "mvr",
            "mwk",
            "mxn",
            "myr",
            "mzn",
            "nad",
            "ngn",
            "nok",
            "npr",
            "nzd",
            "pgk",
            "php",
            "pkr",
            "pln",
            "qar",
            "ron",
            "rsd",
            "rub",
            "rwf",
            "sar",
            "sbd",
            "scr",
            "sek",
            "sgd",
            "sle",
            "sll",
            "sos",
            "szl",
            "thb",
            "tjs",
            "top",
            "try",
            "ttd",
            "tzs",
            "uah",
            "uzs",
            "vnd",
            "vuv",
            "wst",
            "xaf",
            "xcd",
            "yer",
            "zar",
            "zmw",
            "clp",
            "djf",
            "gnf",
            "ugx",
            "pyg",
            "xof",
            "xpf",
        ]
    ]
    """The price currency"""


class AppliedCouponDiscount(TypedDict, total=False):
    """Ad-hoc discount configuration"""

    amounts_off: Annotated[Optional[Iterable[AppliedCouponDiscountAmountsOff]], PropertyInfo(alias="amountsOff")]
    """Fixed amounts off by currency"""

    description: str
    """Ad-hoc discount"""

    duration_in_months: Annotated[float, PropertyInfo(alias="durationInMonths")]
    """Duration in months"""

    name: str
    """Discount name"""

    percent_off: Annotated[float, PropertyInfo(alias="percentOff")]
    """Percentage discount"""


class AppliedCoupon(TypedDict, total=False):
    """Coupon or discount to apply"""

    billing_coupon_id: Annotated[str, PropertyInfo(alias="billingCouponId")]
    """Billing provider coupon ID"""

    configuration: AppliedCouponConfiguration
    """Coupon timing configuration"""

    coupon_id: Annotated[str, PropertyInfo(alias="couponId")]
    """Stigg coupon ID"""

    discount: AppliedCouponDiscount
    """Ad-hoc discount configuration"""

    promotion_code: Annotated[str, PropertyInfo(alias="promotionCode")]
    """Promotion code to apply"""


class BillableFeature(TypedDict, total=False):
    """Feature with quantity"""

    feature_id: Required[Annotated[str, PropertyInfo(alias="featureId")]]
    """Feature ID"""

    quantity: Required[float]
    """Quantity of feature units"""


class BillingInformationBillingAddress(TypedDict, total=False):
    """Billing address"""

    city: str

    country: str

    line1: str

    line2: str

    postal_code: Annotated[str, PropertyInfo(alias="postalCode")]

    state: str


class BillingInformationTaxID(TypedDict, total=False):
    """Tax exemption identifier"""

    type: Required[str]
    """Tax exemption type (e.g., vat, gst)"""

    value: Required[str]
    """Tax exemption identifier value"""


class BillingInformation(TypedDict, total=False):
    """Billing and tax configuration"""

    billing_address: Annotated[BillingInformationBillingAddress, PropertyInfo(alias="billingAddress")]
    """Billing address"""

    charge_on_behalf_of_account: Annotated[str, PropertyInfo(alias="chargeOnBehalfOfAccount")]
    """Connected account ID for platform billing"""

    integration_id: Annotated[str, PropertyInfo(alias="integrationId")]
    """Billing integration ID"""

    invoice_days_until_due: Annotated[float, PropertyInfo(alias="invoiceDaysUntilDue")]
    """Days until invoice is due"""

    is_backdated: Annotated[bool, PropertyInfo(alias="isBackdated")]
    """Whether subscription is backdated"""

    is_invoice_paid: Annotated[bool, PropertyInfo(alias="isInvoicePaid")]
    """Whether invoice is already paid"""

    metadata: object
    """Additional billing metadata"""

    proration_behavior: Annotated[
        Literal["INVOICE_IMMEDIATELY", "CREATE_PRORATIONS", "NONE"], PropertyInfo(alias="prorationBehavior")
    ]
    """Proration behavior"""

    tax_ids: Annotated[Iterable[BillingInformationTaxID], PropertyInfo(alias="taxIds")]
    """Customer tax IDs"""

    tax_percentage: Annotated[float, PropertyInfo(alias="taxPercentage")]
    """Tax percentage to apply"""

    tax_rate_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="taxRateIds")]
    """Tax rate IDs from billing provider"""


class Charge(TypedDict, total=False):
    """Charge item"""

    id: Required[str]
    """Charge ID"""

    quantity: Required[float]
    """Charge quantity"""

    type: Required[Literal["FEATURE", "CREDIT"]]
    """Charge type"""


class TrialOverrideConfiguration(TypedDict, total=False):
    """Trial period override settings"""

    is_trial: Required[Annotated[bool, PropertyInfo(alias="isTrial")]]
    """Whether to start as trial"""

    trial_end_behavior: Annotated[
        Literal["CONVERT_TO_PAID", "CANCEL_SUBSCRIPTION"], PropertyInfo(alias="trialEndBehavior")
    ]
    """Behavior when trial ends"""

    trial_end_date: Annotated[Union[str, datetime], PropertyInfo(alias="trialEndDate", format="iso8601")]
    """Trial end date"""
