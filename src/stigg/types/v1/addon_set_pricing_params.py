# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "AddonSetPricingParams",
    "MinimumSpend",
    "MinimumSpendMinimum",
    "OveragePricingModel",
    "OveragePricingModelPricePeriod",
    "OveragePricingModelPricePeriodCreditRate",
    "OveragePricingModelPricePeriodPrice",
    "OveragePricingModelPricePeriodTier",
    "OveragePricingModelPricePeriodTierFlatPrice",
    "OveragePricingModelPricePeriodTierUnitPrice",
    "OveragePricingModelEntitlement",
    "OveragePricingModelEntitlementMonthlyResetPeriodConfiguration",
    "OveragePricingModelEntitlementWeeklyResetPeriodConfiguration",
    "OveragePricingModelEntitlementYearlyResetPeriodConfiguration",
    "PricingModel",
    "PricingModelPricePeriod",
    "PricingModelPricePeriodCreditRate",
    "PricingModelPricePeriodPrice",
    "PricingModelPricePeriodTier",
    "PricingModelPricePeriodTierFlatPrice",
    "PricingModelPricePeriodTierUnitPrice",
    "PricingModelMonthlyResetPeriodConfiguration",
    "PricingModelWeeklyResetPeriodConfiguration",
    "PricingModelYearlyResetPeriodConfiguration",
]


class AddonSetPricingParams(TypedDict, total=False):
    pricing_type: Required[Annotated[Literal["FREE", "PAID", "CUSTOM"], PropertyInfo(alias="pricingType")]]
    """The pricing type (FREE, PAID, or CUSTOM)"""

    billing_id: Annotated[str, PropertyInfo(alias="billingId")]
    """Deprecated: billing integration ID"""

    minimum_spend: Annotated[Optional[Iterable[MinimumSpend]], PropertyInfo(alias="minimumSpend")]
    """Minimum spend configuration per billing period"""

    overage_billing_period: Annotated[
        Literal["ON_SUBSCRIPTION_RENEWAL", "MONTHLY"], PropertyInfo(alias="overageBillingPeriod")
    ]
    """When overage charges are billed"""

    overage_pricing_models: Annotated[Iterable[OveragePricingModel], PropertyInfo(alias="overagePricingModels")]
    """Array of overage pricing model configurations"""

    pricing_models: Annotated[Iterable[PricingModel], PropertyInfo(alias="pricingModels")]
    """Array of pricing model configurations"""


class MinimumSpendMinimum(TypedDict, total=False):
    """The minimum spend amount"""

    amount: Required[float]
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


class MinimumSpend(TypedDict, total=False):
    """Minimum spend configuration for a billing period."""

    billing_period: Required[Annotated[Literal["MONTHLY", "ANNUALLY"], PropertyInfo(alias="billingPeriod")]]
    """The billing period"""

    minimum: Required[MinimumSpendMinimum]
    """The minimum spend amount"""


class OveragePricingModelPricePeriodCreditRate(TypedDict, total=False):
    """Credit rate configuration for credit-based pricing"""

    amount: Required[float]
    """The credit rate amount"""

    currency_id: Required[Annotated[str, PropertyInfo(alias="currencyId")]]
    """The custom currency ID"""

    cost_formula: Annotated[str, PropertyInfo(alias="costFormula")]
    """Optional cost formula expression"""


class OveragePricingModelPricePeriodPrice(TypedDict, total=False):
    """The price amount and currency"""

    amount: Required[float]
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


class OveragePricingModelPricePeriodTierFlatPrice(TypedDict, total=False):
    """Flat price for this tier"""

    amount: Required[float]
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


class OveragePricingModelPricePeriodTierUnitPrice(TypedDict, total=False):
    """Per-unit price in this tier"""

    amount: Required[float]
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


class OveragePricingModelPricePeriodTier(TypedDict, total=False):
    """A tier in tiered pricing."""

    flat_price: Annotated[OveragePricingModelPricePeriodTierFlatPrice, PropertyInfo(alias="flatPrice")]
    """Flat price for this tier"""

    unit_price: Annotated[OveragePricingModelPricePeriodTierUnitPrice, PropertyInfo(alias="unitPrice")]
    """Per-unit price in this tier"""

    up_to: Annotated[float, PropertyInfo(alias="upTo")]
    """Upper bound of this tier (null for unlimited)"""


class OveragePricingModelPricePeriod(TypedDict, total=False):
    """Price configuration for a specific billing period."""

    billing_period: Required[Annotated[Literal["MONTHLY", "ANNUALLY"], PropertyInfo(alias="billingPeriod")]]
    """The billing period (MONTHLY or ANNUALLY)"""

    billing_country_code: Annotated[str, PropertyInfo(alias="billingCountryCode")]
    """ISO country code for localized pricing"""

    block_size: Annotated[float, PropertyInfo(alias="blockSize")]
    """Block size for usage-based pricing"""

    credit_grant_cadence: Annotated[
        Literal["BEGINNING_OF_BILLING_PERIOD", "MONTHLY"], PropertyInfo(alias="creditGrantCadence")
    ]
    """When credits are granted"""

    credit_rate: Annotated[OveragePricingModelPricePeriodCreditRate, PropertyInfo(alias="creditRate")]
    """Credit rate configuration for credit-based pricing"""

    price: OveragePricingModelPricePeriodPrice
    """The price amount and currency"""

    tiers: Iterable[OveragePricingModelPricePeriodTier]
    """Tiered pricing configuration"""


class OveragePricingModelEntitlementMonthlyResetPeriodConfiguration(TypedDict, total=False):
    """Monthly reset configuration"""

    according_to: Required[
        Annotated[Literal["SubscriptionStart", "StartOfTheMonth"], PropertyInfo(alias="accordingTo")]
    ]
    """Reset anchor (SubscriptionStart or StartOfTheMonth)"""


class OveragePricingModelEntitlementWeeklyResetPeriodConfiguration(TypedDict, total=False):
    """Weekly reset configuration"""

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


class OveragePricingModelEntitlementYearlyResetPeriodConfiguration(TypedDict, total=False):
    """Yearly reset configuration"""

    according_to: Required[Annotated[Literal["SubscriptionStart"], PropertyInfo(alias="accordingTo")]]
    """Reset anchor (SubscriptionStart)"""


class OveragePricingModelEntitlement(TypedDict, total=False):
    """Entitlement configuration for the overage feature"""

    feature_id: Required[Annotated[str, PropertyInfo(alias="featureId")]]
    """The feature ID for the entitlement"""

    has_soft_limit: Annotated[bool, PropertyInfo(alias="hasSoftLimit")]
    """Whether the limit is soft (allows overage)"""

    has_unlimited_usage: Annotated[bool, PropertyInfo(alias="hasUnlimitedUsage")]
    """Whether usage is unlimited"""

    monthly_reset_period_configuration: Annotated[
        OveragePricingModelEntitlementMonthlyResetPeriodConfiguration,
        PropertyInfo(alias="monthlyResetPeriodConfiguration"),
    ]
    """Monthly reset configuration"""

    reset_period: Annotated[Literal["YEAR", "MONTH", "WEEK", "DAY", "HOUR"], PropertyInfo(alias="resetPeriod")]
    """The usage reset period"""

    usage_limit: Annotated[float, PropertyInfo(alias="usageLimit")]
    """The usage limit before overage kicks in"""

    weekly_reset_period_configuration: Annotated[
        OveragePricingModelEntitlementWeeklyResetPeriodConfiguration,
        PropertyInfo(alias="weeklyResetPeriodConfiguration"),
    ]
    """Weekly reset configuration"""

    yearly_reset_period_configuration: Annotated[
        OveragePricingModelEntitlementYearlyResetPeriodConfiguration,
        PropertyInfo(alias="yearlyResetPeriodConfiguration"),
    ]
    """Yearly reset configuration"""


class OveragePricingModel(TypedDict, total=False):
    """Overage pricing model configuration."""

    billing_model: Required[
        Annotated[
            Literal["FLAT_FEE", "MINIMUM_SPEND", "PER_UNIT", "USAGE_BASED", "CREDIT_BASED"],
            PropertyInfo(alias="billingModel"),
        ]
    ]
    """The billing model for overages"""

    price_periods: Required[Annotated[Iterable[OveragePricingModelPricePeriod], PropertyInfo(alias="pricePeriods")]]
    """Price periods for overage pricing"""

    billing_cadence: Annotated[Literal["RECURRING", "ONE_OFF"], PropertyInfo(alias="billingCadence")]
    """The billing cadence for overages"""

    entitlement: OveragePricingModelEntitlement
    """Entitlement configuration for the overage feature"""

    feature_id: Annotated[str, PropertyInfo(alias="featureId")]
    """The feature ID for overage pricing"""

    top_up_custom_currency_id: Annotated[str, PropertyInfo(alias="topUpCustomCurrencyId")]
    """Custom currency ID for overage top-up"""


class PricingModelPricePeriodCreditRate(TypedDict, total=False):
    """Credit rate configuration for credit-based pricing"""

    amount: Required[float]
    """The credit rate amount"""

    currency_id: Required[Annotated[str, PropertyInfo(alias="currencyId")]]
    """The custom currency ID"""

    cost_formula: Annotated[str, PropertyInfo(alias="costFormula")]
    """Optional cost formula expression"""


class PricingModelPricePeriodPrice(TypedDict, total=False):
    """The price amount and currency"""

    amount: Required[float]
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


class PricingModelPricePeriodTierFlatPrice(TypedDict, total=False):
    """Flat price for this tier"""

    amount: Required[float]
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


class PricingModelPricePeriodTierUnitPrice(TypedDict, total=False):
    """Per-unit price in this tier"""

    amount: Required[float]
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


class PricingModelPricePeriodTier(TypedDict, total=False):
    """A tier in tiered pricing."""

    flat_price: Annotated[PricingModelPricePeriodTierFlatPrice, PropertyInfo(alias="flatPrice")]
    """Flat price for this tier"""

    unit_price: Annotated[PricingModelPricePeriodTierUnitPrice, PropertyInfo(alias="unitPrice")]
    """Per-unit price in this tier"""

    up_to: Annotated[float, PropertyInfo(alias="upTo")]
    """Upper bound of this tier (null for unlimited)"""


class PricingModelPricePeriod(TypedDict, total=False):
    """Price configuration for a specific billing period."""

    billing_period: Required[Annotated[Literal["MONTHLY", "ANNUALLY"], PropertyInfo(alias="billingPeriod")]]
    """The billing period (MONTHLY or ANNUALLY)"""

    billing_country_code: Annotated[str, PropertyInfo(alias="billingCountryCode")]
    """ISO country code for localized pricing"""

    block_size: Annotated[float, PropertyInfo(alias="blockSize")]
    """Block size for usage-based pricing"""

    credit_grant_cadence: Annotated[
        Literal["BEGINNING_OF_BILLING_PERIOD", "MONTHLY"], PropertyInfo(alias="creditGrantCadence")
    ]
    """When credits are granted"""

    credit_rate: Annotated[PricingModelPricePeriodCreditRate, PropertyInfo(alias="creditRate")]
    """Credit rate configuration for credit-based pricing"""

    price: PricingModelPricePeriodPrice
    """The price amount and currency"""

    tiers: Iterable[PricingModelPricePeriodTier]
    """Tiered pricing configuration"""


class PricingModelMonthlyResetPeriodConfiguration(TypedDict, total=False):
    """Monthly reset period configuration"""

    according_to: Required[
        Annotated[Literal["SubscriptionStart", "StartOfTheMonth"], PropertyInfo(alias="accordingTo")]
    ]
    """Reset anchor (SubscriptionStart or StartOfTheMonth)"""


class PricingModelWeeklyResetPeriodConfiguration(TypedDict, total=False):
    """Weekly reset period configuration"""

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


class PricingModelYearlyResetPeriodConfiguration(TypedDict, total=False):
    """Yearly reset period configuration"""

    according_to: Required[Annotated[Literal["SubscriptionStart"], PropertyInfo(alias="accordingTo")]]
    """Reset anchor (SubscriptionStart)"""


class PricingModel(TypedDict, total=False):
    """A pricing model configuration with billing details and price periods."""

    billing_model: Required[
        Annotated[
            Literal["FLAT_FEE", "MINIMUM_SPEND", "PER_UNIT", "USAGE_BASED", "CREDIT_BASED"],
            PropertyInfo(alias="billingModel"),
        ]
    ]
    """The billing model (FLAT_FEE, PER_UNIT, USAGE_BASED, CREDIT_BASED)"""

    price_periods: Required[Annotated[Iterable[PricingModelPricePeriod], PropertyInfo(alias="pricePeriods")]]
    """Array of price period configurations (at least one required)"""

    billing_cadence: Annotated[Literal["RECURRING", "ONE_OFF"], PropertyInfo(alias="billingCadence")]
    """The billing cadence (RECURRING or ONE_OFF)"""

    feature_id: Annotated[str, PropertyInfo(alias="featureId")]
    """The feature ID this pricing model is associated with"""

    max_unit_quantity: Annotated[int, PropertyInfo(alias="maxUnitQuantity")]
    """Maximum number of units (max 999999)"""

    min_unit_quantity: Annotated[int, PropertyInfo(alias="minUnitQuantity")]
    """Minimum number of units"""

    monthly_reset_period_configuration: Annotated[
        PricingModelMonthlyResetPeriodConfiguration, PropertyInfo(alias="monthlyResetPeriodConfiguration")
    ]
    """Monthly reset period configuration"""

    reset_period: Annotated[Literal["YEAR", "MONTH", "WEEK", "DAY", "HOUR"], PropertyInfo(alias="resetPeriod")]
    """The usage reset period"""

    tiers_mode: Annotated[Literal["VOLUME", "GRADUATED"], PropertyInfo(alias="tiersMode")]
    """The tiered pricing mode (VOLUME or GRADUATED)"""

    top_up_custom_currency_id: Annotated[str, PropertyInfo(alias="topUpCustomCurrencyId")]
    """The custom currency ID for top-up pricing"""

    weekly_reset_period_configuration: Annotated[
        PricingModelWeeklyResetPeriodConfiguration, PropertyInfo(alias="weeklyResetPeriodConfiguration")
    ]
    """Weekly reset period configuration"""

    yearly_reset_period_configuration: Annotated[
        PricingModelYearlyResetPeriodConfiguration, PropertyInfo(alias="yearlyResetPeriodConfiguration")
    ]
    """Yearly reset period configuration"""
