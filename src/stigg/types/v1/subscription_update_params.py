# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

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
    "Entitlement",
    "EntitlementFeature",
    "EntitlementFeatureMonthlyResetPeriodConfiguration",
    "EntitlementFeatureWeeklyResetPeriodConfiguration",
    "EntitlementFeatureYearlyResetPeriodConfiguration",
    "EntitlementCredit",
    "MinimumSpend",
    "PriceOverride",
]


class SubscriptionUpdateParams(TypedDict, total=False):
    addons: Iterable[Addon]

    applied_coupon: Annotated[AppliedCoupon, PropertyInfo(alias="appliedCoupon")]

    await_payment_confirmation: Annotated[bool, PropertyInfo(alias="awaitPaymentConfirmation")]

    billing_cycle_anchor: Annotated[Literal["UNCHANGED", "NOW"], PropertyInfo(alias="billingCycleAnchor")]

    billing_information: Annotated[BillingInformation, PropertyInfo(alias="billingInformation")]

    billing_period: Annotated[Literal["MONTHLY", "ANNUALLY"], PropertyInfo(alias="billingPeriod")]

    budget: Optional[Budget]

    charges: Iterable[Charge]

    entitlements: Iterable[Entitlement]

    metadata: Dict[str, str]
    """Additional metadata for the subscription"""

    minimum_spend: Annotated[Optional[MinimumSpend], PropertyInfo(alias="minimumSpend")]
    """Minimum spend amount"""

    price_overrides: Annotated[Iterable[PriceOverride], PropertyInfo(alias="priceOverrides")]

    promotion_code: Annotated[str, PropertyInfo(alias="promotionCode")]

    schedule_strategy: Annotated[
        Literal["END_OF_BILLING_PERIOD", "END_OF_BILLING_MONTH", "IMMEDIATE"], PropertyInfo(alias="scheduleStrategy")
    ]

    trial_end_date: Annotated[Union[str, datetime], PropertyInfo(alias="trialEndDate", format="iso8601")]
    """Subscription trial end date"""


class Addon(TypedDict, total=False):
    """Addon configuration"""

    id: Required[str]
    """Addon ID"""

    quantity: Required[int]
    """Number of addon instances"""


class AppliedCouponConfiguration(TypedDict, total=False):
    start_date: Annotated[Union[str, datetime], PropertyInfo(alias="startDate", format="iso8601")]
    """Coupon start date"""


class AppliedCouponDiscountAmountsOff(TypedDict, total=False):
    """Monetary amount with currency"""

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
    """ISO 4217 currency code"""


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
    """Stigg coupon ID"""

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

    metadata: Dict[str, str]
    """Additional metadata for the subscription"""

    proration_behavior: Annotated[
        Literal["INVOICE_IMMEDIATELY", "CREATE_PRORATIONS", "NONE"], PropertyInfo(alias="prorationBehavior")
    ]

    tax_ids: Annotated[Iterable[BillingInformationTaxID], PropertyInfo(alias="taxIds")]

    tax_percentage: Annotated[float, PropertyInfo(alias="taxPercentage")]

    tax_rate_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="taxRateIds")]


class Budget(TypedDict, total=False):
    has_soft_limit: Required[Annotated[bool, PropertyInfo(alias="hasSoftLimit")]]
    """Whether the budget is a soft limit"""

    limit: Required[float]
    """Maximum spending limit"""


class Charge(TypedDict, total=False):
    id: Required[str]
    """Charge ID"""

    quantity: Required[float]

    type: Required[Literal["FEATURE", "CREDIT"]]


class EntitlementFeatureMonthlyResetPeriodConfiguration(TypedDict, total=False):
    """Configuration for monthly reset period"""

    according_to: Required[
        Annotated[Literal["SubscriptionStart", "StartOfTheMonth"], PropertyInfo(alias="accordingTo")]
    ]
    """Reset anchor (SubscriptionStart or StartOfTheMonth)"""


class EntitlementFeatureWeeklyResetPeriodConfiguration(TypedDict, total=False):
    """Configuration for weekly reset period"""

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


class EntitlementFeatureYearlyResetPeriodConfiguration(TypedDict, total=False):
    """Configuration for yearly reset period"""

    according_to: Required[Annotated[Literal["SubscriptionStart"], PropertyInfo(alias="accordingTo")]]
    """Reset anchor (SubscriptionStart)"""


class EntitlementFeature(TypedDict, total=False):
    """Feature entitlement configuration for a subscription"""

    id: Required[str]
    """The feature ID to attach the entitlement to"""

    type: Required[Literal["FEATURE"]]
    """SubscriptionFeatureEntitlementRequest"""

    has_soft_limit: Annotated[bool, PropertyInfo(alias="hasSoftLimit")]
    """Whether the usage limit is a soft limit"""

    has_unlimited_usage: Annotated[bool, PropertyInfo(alias="hasUnlimitedUsage")]
    """Whether usage is unlimited"""

    monthly_reset_period_configuration: Annotated[
        Optional[EntitlementFeatureMonthlyResetPeriodConfiguration],
        PropertyInfo(alias="monthlyResetPeriodConfiguration"),
    ]
    """Configuration for monthly reset period"""

    reset_period: Annotated[Literal["YEAR", "MONTH", "WEEK", "DAY", "HOUR"], PropertyInfo(alias="resetPeriod")]
    """Period at which usage resets"""

    usage_limit: Annotated[int, PropertyInfo(alias="usageLimit")]
    """Maximum allowed usage for the feature"""

    weekly_reset_period_configuration: Annotated[
        Optional[EntitlementFeatureWeeklyResetPeriodConfiguration], PropertyInfo(alias="weeklyResetPeriodConfiguration")
    ]
    """Configuration for weekly reset period"""

    yearly_reset_period_configuration: Annotated[
        Optional[EntitlementFeatureYearlyResetPeriodConfiguration], PropertyInfo(alias="yearlyResetPeriodConfiguration")
    ]
    """Configuration for yearly reset period"""


class EntitlementCredit(TypedDict, total=False):
    """Credit entitlement configuration for a subscription"""

    id: Required[str]
    """The custom currency ID for the credit entitlement"""

    amount: Required[float]
    """Credit grant amount"""

    cadence: Required[Literal["MONTH", "YEAR"]]
    """Credit grant cadence (MONTH or YEAR)"""

    type: Required[Literal["CREDIT"]]
    """SubscriptionCreditEntitlementRequest"""


Entitlement: TypeAlias = Union[EntitlementFeature, EntitlementCredit]


class MinimumSpend(TypedDict, total=False):
    """Minimum spend amount"""

    amount: float
    """The price amount"""

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
    """The price currency"""


class PriceOverride(TypedDict, total=False):
    addon_id: Annotated[str, PropertyInfo(alias="addonId")]
    """Addon ID"""

    amount: float
    """The price amount"""

    base_charge: Annotated[bool, PropertyInfo(alias="baseCharge")]
    """Whether this is a base charge override"""

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
    """The price currency"""

    currency_id: Annotated[str, PropertyInfo(alias="currencyId")]
    """The corresponding custom currency id of the recurring credits price"""

    feature_id: Annotated[str, PropertyInfo(alias="featureId")]
    """Feature ID"""
