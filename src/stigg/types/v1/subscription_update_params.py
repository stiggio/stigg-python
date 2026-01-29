# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = [
    "SubscriptionUpdateParams",
    "Addon",
    "AppliedCoupon",
    "AppliedCouponConfiguration",
    "AppliedCouponDiscount",
    "AppliedCouponDiscountAmountsOff",
    "BillingInformation",
    "BillingInformationBillingAddress",
    "BillingInformationTaxID",
    "Budget",
    "Charge",
    "MinimumSpend",
    "MinimumSpendMinimum",
    "PriceOverride",
    "PriceOverridePrice",
    "SubscriptionEntitlement",
    "SubscriptionEntitlementMonthlyResetPeriodConfiguration",
    "SubscriptionEntitlementWeeklyResetPeriodConfiguration",
    "SubscriptionEntitlementYearlyResetPeriodConfiguration",
]


class SubscriptionUpdateParams(TypedDict, total=False):
    addons: Iterable[Addon]

    applied_coupon: Annotated[AppliedCoupon, PropertyInfo(alias="appliedCoupon")]

    await_payment_confirmation: Annotated[bool, PropertyInfo(alias="awaitPaymentConfirmation")]

    billing_information: Annotated[BillingInformation, PropertyInfo(alias="billingInformation")]

    billing_period: Annotated[Literal["MONTHLY", "ANNUALLY"], PropertyInfo(alias="billingPeriod")]

    budget: Optional[Budget]

    charges: Iterable[Charge]

    metadata: Dict[str, str]
    """Additional metadata for the subscription"""

    minimum_spend: Annotated[Optional[MinimumSpend], PropertyInfo(alias="minimumSpend")]

    price_overrides: Annotated[Iterable[PriceOverride], PropertyInfo(alias="priceOverrides")]

    promotion_code: Annotated[str, PropertyInfo(alias="promotionCode")]

    schedule_strategy: Annotated[
        Literal["END_OF_BILLING_PERIOD", "END_OF_BILLING_MONTH", "IMMEDIATE"], PropertyInfo(alias="scheduleStrategy")
    ]

    subscription_entitlements: Annotated[
        Iterable[SubscriptionEntitlement], PropertyInfo(alias="subscriptionEntitlements")
    ]

    trial_end_date: Annotated[Union[str, datetime], PropertyInfo(alias="trialEndDate", format="iso8601")]
    """Subscription trial end date"""


class Addon(TypedDict, total=False):
    addon_id: Required[Annotated[str, PropertyInfo(alias="addonId")]]
    """Addon ID"""

    quantity: Required[float]


class AppliedCouponConfiguration(TypedDict, total=False):
    start_date: Annotated[Union[str, datetime], PropertyInfo(alias="startDate", format="iso8601")]
    """Coupon start date"""


class AppliedCouponDiscountAmountsOff(TypedDict, total=False):
    amount: Required[float]

    currency: Literal[
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

    promotion_code: Annotated[Optional[str], PropertyInfo(alias="promotionCode")]


class BillingInformationBillingAddress(TypedDict, total=False):
    """Physical address"""

    city: str
    """City name"""

    country: str
    """Country code or name"""

    line1: str
    """Street address line 1"""

    line2: str
    """Street address line 2"""

    postal_code: Annotated[str, PropertyInfo(alias="postalCode")]
    """Postal or ZIP code"""

    state: str
    """State or province"""


class BillingInformationTaxID(TypedDict, total=False):
    type: Required[str]

    value: Required[str]


class BillingInformation(TypedDict, total=False):
    billing_address: Annotated[BillingInformationBillingAddress, PropertyInfo(alias="billingAddress")]
    """Physical address"""

    charge_on_behalf_of_account: Annotated[str, PropertyInfo(alias="chargeOnBehalfOfAccount")]

    coupon_id: Annotated[str, PropertyInfo(alias="couponId")]

    integration_id: Annotated[str, PropertyInfo(alias="integrationId")]

    invoice_days_until_due: Annotated[float, PropertyInfo(alias="invoiceDaysUntilDue")]

    is_backdated: Annotated[bool, PropertyInfo(alias="isBackdated")]

    is_invoice_paid: Annotated[bool, PropertyInfo(alias="isInvoicePaid")]

    metadata: Dict[str, object]
    """Additional metadata for the subscription"""

    proration_behavior: Annotated[
        Literal["INVOICE_IMMEDIATELY", "CREATE_PRORATIONS", "NONE"], PropertyInfo(alias="prorationBehavior")
    ]

    tax_ids: Annotated[Iterable[BillingInformationTaxID], PropertyInfo(alias="taxIds")]

    tax_percentage: Annotated[float, PropertyInfo(alias="taxPercentage")]

    tax_rate_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="taxRateIds")]


class Budget(TypedDict, total=False):
    has_soft_limit: Required[Annotated[bool, PropertyInfo(alias="hasSoftLimit")]]

    limit: Required[float]


class Charge(TypedDict, total=False):
    id: Required[str]
    """Charge ID"""

    quantity: Required[float]

    type: Required[Literal["FEATURE", "CREDIT"]]


class MinimumSpendMinimum(TypedDict, total=False):
    amount: Required[float]

    currency: Literal[
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


class MinimumSpend(TypedDict, total=False):
    minimum: Optional[MinimumSpendMinimum]


class PriceOverridePrice(TypedDict, total=False):
    amount: Required[float]

    currency: Literal[
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


class PriceOverride(TypedDict, total=False):
    feature_id: Required[Annotated[str, PropertyInfo(alias="featureId")]]
    """Feature ID"""

    price: PriceOverridePrice


class SubscriptionEntitlementMonthlyResetPeriodConfiguration(TypedDict, total=False):
    according_to: Required[
        Annotated[Literal["SubscriptionStart", "StartOfTheMonth"], PropertyInfo(alias="accordingTo")]
    ]


class SubscriptionEntitlementWeeklyResetPeriodConfiguration(TypedDict, total=False):
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


class SubscriptionEntitlementYearlyResetPeriodConfiguration(TypedDict, total=False):
    according_to: Required[Annotated[Literal["SubscriptionStart"], PropertyInfo(alias="accordingTo")]]


class SubscriptionEntitlement(TypedDict, total=False):
    id: str

    feature_id: Annotated[str, PropertyInfo(alias="featureId")]

    has_soft_limit: Annotated[bool, PropertyInfo(alias="hasSoftLimit")]

    has_unlimited_usage: Annotated[bool, PropertyInfo(alias="hasUnlimitedUsage")]

    monthly_reset_period_configuration: Annotated[
        SubscriptionEntitlementMonthlyResetPeriodConfiguration, PropertyInfo(alias="monthlyResetPeriodConfiguration")
    ]

    reset_period: Annotated[Literal["YEAR", "MONTH", "WEEK", "DAY", "HOUR"], PropertyInfo(alias="resetPeriod")]

    usage_limit: Annotated[float, PropertyInfo(alias="usageLimit")]

    weekly_reset_period_configuration: Annotated[
        SubscriptionEntitlementWeeklyResetPeriodConfiguration, PropertyInfo(alias="weeklyResetPeriodConfiguration")
    ]

    yearly_reset_period_configuration: Annotated[
        SubscriptionEntitlementYearlyResetPeriodConfiguration, PropertyInfo(alias="yearlyResetPeriodConfiguration")
    ]
