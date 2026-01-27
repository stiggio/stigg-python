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

    applied_coupon: Annotated[AppliedCoupon, PropertyInfo(alias="appliedCoupon")]

    billable_features: Annotated[Iterable[BillableFeature], PropertyInfo(alias="billableFeatures")]

    billing_country_code: Annotated[str, PropertyInfo(alias="billingCountryCode")]

    billing_information: Annotated[BillingInformation, PropertyInfo(alias="billingInformation")]

    billing_period: Annotated[Literal["MONTHLY", "ANNUALLY"], PropertyInfo(alias="billingPeriod")]

    charges: Iterable[Charge]

    paying_customer_id: Annotated[str, PropertyInfo(alias="payingCustomerId")]

    resource_id: Annotated[str, PropertyInfo(alias="resourceId")]

    schedule_strategy: Annotated[
        Literal["END_OF_BILLING_PERIOD", "END_OF_BILLING_MONTH", "IMMEDIATE"], PropertyInfo(alias="scheduleStrategy")
    ]

    start_date: Annotated[Union[str, datetime], PropertyInfo(alias="startDate", format="iso8601")]
    """Subscription start date"""

    trial_override_configuration: Annotated[
        TrialOverrideConfiguration, PropertyInfo(alias="trialOverrideConfiguration")
    ]

    unit_quantity: Annotated[float, PropertyInfo(alias="unitQuantity")]


class Addon(TypedDict, total=False):
    addon_id: Required[Annotated[str, PropertyInfo(alias="addonId")]]
    """Addon ID"""

    quantity: int


class AppliedCouponConfiguration(TypedDict, total=False):
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
    amounts_off: Annotated[Optional[Iterable[AppliedCouponDiscountAmountsOff]], PropertyInfo(alias="amountsOff")]

    description: str

    duration_in_months: Annotated[float, PropertyInfo(alias="durationInMonths")]

    name: str

    percent_off: Annotated[float, PropertyInfo(alias="percentOff")]


class AppliedCoupon(TypedDict, total=False):
    billing_coupon_id: Annotated[str, PropertyInfo(alias="billingCouponId")]

    configuration: AppliedCouponConfiguration

    coupon_id: Annotated[str, PropertyInfo(alias="couponId")]

    discount: AppliedCouponDiscount

    promotion_code: Annotated[str, PropertyInfo(alias="promotionCode")]


class BillableFeature(TypedDict, total=False):
    feature_id: Required[Annotated[str, PropertyInfo(alias="featureId")]]
    """Feature ID"""

    quantity: Required[float]


class BillingInformationBillingAddress(TypedDict, total=False):
    city: str

    country: str

    line1: str

    line2: str

    postal_code: Annotated[str, PropertyInfo(alias="postalCode")]

    state: str


class BillingInformationTaxID(TypedDict, total=False):
    type: Required[str]

    value: Required[str]


class BillingInformation(TypedDict, total=False):
    billing_address: Annotated[BillingInformationBillingAddress, PropertyInfo(alias="billingAddress")]

    charge_on_behalf_of_account: Annotated[str, PropertyInfo(alias="chargeOnBehalfOfAccount")]

    integration_id: Annotated[str, PropertyInfo(alias="integrationId")]

    invoice_days_until_due: Annotated[float, PropertyInfo(alias="invoiceDaysUntilDue")]

    is_backdated: Annotated[bool, PropertyInfo(alias="isBackdated")]

    is_invoice_paid: Annotated[bool, PropertyInfo(alias="isInvoicePaid")]

    metadata: object

    proration_behavior: Annotated[
        Literal["INVOICE_IMMEDIATELY", "CREATE_PRORATIONS", "NONE"], PropertyInfo(alias="prorationBehavior")
    ]

    tax_ids: Annotated[Iterable[BillingInformationTaxID], PropertyInfo(alias="taxIds")]

    tax_percentage: Annotated[float, PropertyInfo(alias="taxPercentage")]

    tax_rate_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="taxRateIds")]


class Charge(TypedDict, total=False):
    id: Required[str]
    """Charge ID"""

    quantity: Required[float]

    type: Required[Literal["FEATURE", "CREDIT"]]


class TrialOverrideConfiguration(TypedDict, total=False):
    is_trial: Required[Annotated[bool, PropertyInfo(alias="isTrial")]]

    trial_end_behavior: Annotated[
        Literal["CONVERT_TO_PAID", "CANCEL_SUBSCRIPTION"], PropertyInfo(alias="trialEndBehavior")
    ]

    trial_end_date: Annotated[Union[str, datetime], PropertyInfo(alias="trialEndDate", format="iso8601")]
    """Trial end date"""
