# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = [
    "AddonUpdateParams",
    "Charges",
    "ChargesMinimumSpend",
    "ChargesMinimumSpendMinimum",
    "ChargesOveragePricingModel",
    "ChargesOveragePricingModelPricePeriod",
    "ChargesOveragePricingModelPricePeriodCreditRate",
    "ChargesOveragePricingModelPricePeriodPrice",
    "ChargesOveragePricingModelPricePeriodTier",
    "ChargesOveragePricingModelPricePeriodTierFlatPrice",
    "ChargesOveragePricingModelPricePeriodTierUnitPrice",
    "ChargesOveragePricingModelEntitlement",
    "ChargesOveragePricingModelEntitlementMonthlyResetPeriodConfiguration",
    "ChargesOveragePricingModelEntitlementWeeklyResetPeriodConfiguration",
    "ChargesOveragePricingModelEntitlementYearlyResetPeriodConfiguration",
    "ChargesPricingModel",
    "ChargesPricingModelPricePeriod",
    "ChargesPricingModelPricePeriodCreditRate",
    "ChargesPricingModelPricePeriodPrice",
    "ChargesPricingModelPricePeriodTier",
    "ChargesPricingModelPricePeriodTierFlatPrice",
    "ChargesPricingModelPricePeriodTierUnitPrice",
    "ChargesPricingModelMonthlyResetPeriodConfiguration",
    "ChargesPricingModelWeeklyResetPeriodConfiguration",
    "ChargesPricingModelYearlyResetPeriodConfiguration",
]


class AddonUpdateParams(TypedDict, total=False):
    billing_id: Annotated[Optional[str], PropertyInfo(alias="billingId")]
    """The unique identifier for the entity in the billing provider"""

    charges: Charges
    """Pricing configuration to set on the addon draft"""

    dependencies: Optional[SequenceNotStr[str]]
    """List of addons the addon is dependant on"""

    description: Optional[str]
    """The description of the package"""

    display_name: Annotated[str, PropertyInfo(alias="displayName")]
    """The display name of the package"""

    max_quantity: Annotated[Optional[int], PropertyInfo(alias="maxQuantity")]
    """The maximum quantity of this addon that can be added to a subscription"""

    metadata: Dict[str, str]
    """Metadata associated with the entity"""

    status: Literal["DRAFT", "PUBLISHED", "ARCHIVED"]
    """The status of the package"""


class ChargesMinimumSpendMinimum(TypedDict, total=False):
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


class ChargesMinimumSpend(TypedDict, total=False):
    """Minimum spend configuration for a billing period."""

    billing_period: Required[Annotated[Literal["MONTHLY", "ANNUALLY"], PropertyInfo(alias="billingPeriod")]]
    """The billing period"""

    minimum: Required[ChargesMinimumSpendMinimum]
    """The minimum spend amount"""


class ChargesOveragePricingModelPricePeriodCreditRate(TypedDict, total=False):
    """Credit rate configuration for credit-based pricing"""

    amount: Required[float]
    """The credit rate amount"""

    currency_id: Required[Annotated[str, PropertyInfo(alias="currencyId")]]
    """The custom currency ID"""

    cost_formula: Annotated[str, PropertyInfo(alias="costFormula")]
    """Optional cost formula expression"""


class ChargesOveragePricingModelPricePeriodPrice(TypedDict, total=False):
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


class ChargesOveragePricingModelPricePeriodTierFlatPrice(TypedDict, total=False):
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


class ChargesOveragePricingModelPricePeriodTierUnitPrice(TypedDict, total=False):
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


class ChargesOveragePricingModelPricePeriodTier(TypedDict, total=False):
    """A tier in tiered pricing."""

    flat_price: Annotated[ChargesOveragePricingModelPricePeriodTierFlatPrice, PropertyInfo(alias="flatPrice")]
    """Flat price for this tier"""

    unit_price: Annotated[ChargesOveragePricingModelPricePeriodTierUnitPrice, PropertyInfo(alias="unitPrice")]
    """Per-unit price in this tier"""

    up_to: Annotated[float, PropertyInfo(alias="upTo")]
    """Upper bound of this tier (null for unlimited)"""


class ChargesOveragePricingModelPricePeriod(TypedDict, total=False):
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

    credit_rate: Annotated[ChargesOveragePricingModelPricePeriodCreditRate, PropertyInfo(alias="creditRate")]
    """Credit rate configuration for credit-based pricing"""

    price: ChargesOveragePricingModelPricePeriodPrice
    """The price amount and currency"""

    tiers: Iterable[ChargesOveragePricingModelPricePeriodTier]
    """Tiered pricing configuration"""


class ChargesOveragePricingModelEntitlementMonthlyResetPeriodConfiguration(TypedDict, total=False):
    """Monthly reset configuration"""

    according_to: Required[
        Annotated[Literal["SubscriptionStart", "StartOfTheMonth"], PropertyInfo(alias="accordingTo")]
    ]
    """Reset anchor (SubscriptionStart or StartOfTheMonth)"""


class ChargesOveragePricingModelEntitlementWeeklyResetPeriodConfiguration(TypedDict, total=False):
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


class ChargesOveragePricingModelEntitlementYearlyResetPeriodConfiguration(TypedDict, total=False):
    """Yearly reset configuration"""

    according_to: Required[Annotated[Literal["SubscriptionStart"], PropertyInfo(alias="accordingTo")]]
    """Reset anchor (SubscriptionStart)"""


class ChargesOveragePricingModelEntitlement(TypedDict, total=False):
    """Entitlement configuration for the overage feature"""

    feature_id: Required[Annotated[str, PropertyInfo(alias="featureId")]]
    """The feature ID for the entitlement"""

    has_soft_limit: Annotated[bool, PropertyInfo(alias="hasSoftLimit")]
    """Whether the limit is soft (allows overage)"""

    has_unlimited_usage: Annotated[bool, PropertyInfo(alias="hasUnlimitedUsage")]
    """Whether usage is unlimited"""

    monthly_reset_period_configuration: Annotated[
        ChargesOveragePricingModelEntitlementMonthlyResetPeriodConfiguration,
        PropertyInfo(alias="monthlyResetPeriodConfiguration"),
    ]
    """Monthly reset configuration"""

    reset_period: Annotated[Literal["YEAR", "MONTH", "WEEK", "DAY", "HOUR"], PropertyInfo(alias="resetPeriod")]
    """The usage reset period"""

    usage_limit: Annotated[float, PropertyInfo(alias="usageLimit")]
    """The usage limit before overage kicks in"""

    weekly_reset_period_configuration: Annotated[
        ChargesOveragePricingModelEntitlementWeeklyResetPeriodConfiguration,
        PropertyInfo(alias="weeklyResetPeriodConfiguration"),
    ]
    """Weekly reset configuration"""

    yearly_reset_period_configuration: Annotated[
        ChargesOveragePricingModelEntitlementYearlyResetPeriodConfiguration,
        PropertyInfo(alias="yearlyResetPeriodConfiguration"),
    ]
    """Yearly reset configuration"""


class ChargesOveragePricingModel(TypedDict, total=False):
    """Overage pricing model configuration."""

    billing_model: Required[
        Annotated[
            Literal["FLAT_FEE", "MINIMUM_SPEND", "PER_UNIT", "USAGE_BASED", "CREDIT_BASED"],
            PropertyInfo(alias="billingModel"),
        ]
    ]
    """The billing model for overages"""

    price_periods: Required[
        Annotated[Iterable[ChargesOveragePricingModelPricePeriod], PropertyInfo(alias="pricePeriods")]
    ]
    """Price periods for overage pricing"""

    billing_cadence: Annotated[Literal["RECURRING", "ONE_OFF"], PropertyInfo(alias="billingCadence")]
    """The billing cadence for overages"""

    entitlement: ChargesOveragePricingModelEntitlement
    """Entitlement configuration for the overage feature"""

    feature_id: Annotated[str, PropertyInfo(alias="featureId")]
    """The feature ID for overage pricing"""

    top_up_custom_currency_id: Annotated[str, PropertyInfo(alias="topUpCustomCurrencyId")]
    """Custom currency ID for overage top-up"""


class ChargesPricingModelPricePeriodCreditRate(TypedDict, total=False):
    """Credit rate configuration for credit-based pricing"""

    amount: Required[float]
    """The credit rate amount"""

    currency_id: Required[Annotated[str, PropertyInfo(alias="currencyId")]]
    """The custom currency ID"""

    cost_formula: Annotated[str, PropertyInfo(alias="costFormula")]
    """Optional cost formula expression"""


class ChargesPricingModelPricePeriodPrice(TypedDict, total=False):
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


class ChargesPricingModelPricePeriodTierFlatPrice(TypedDict, total=False):
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


class ChargesPricingModelPricePeriodTierUnitPrice(TypedDict, total=False):
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


class ChargesPricingModelPricePeriodTier(TypedDict, total=False):
    """A tier in tiered pricing."""

    flat_price: Annotated[ChargesPricingModelPricePeriodTierFlatPrice, PropertyInfo(alias="flatPrice")]
    """Flat price for this tier"""

    unit_price: Annotated[ChargesPricingModelPricePeriodTierUnitPrice, PropertyInfo(alias="unitPrice")]
    """Per-unit price in this tier"""

    up_to: Annotated[float, PropertyInfo(alias="upTo")]
    """Upper bound of this tier (null for unlimited)"""


class ChargesPricingModelPricePeriod(TypedDict, total=False):
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

    credit_rate: Annotated[ChargesPricingModelPricePeriodCreditRate, PropertyInfo(alias="creditRate")]
    """Credit rate configuration for credit-based pricing"""

    price: ChargesPricingModelPricePeriodPrice
    """The price amount and currency"""

    tiers: Iterable[ChargesPricingModelPricePeriodTier]
    """Tiered pricing configuration"""


class ChargesPricingModelMonthlyResetPeriodConfiguration(TypedDict, total=False):
    """Monthly reset period configuration"""

    according_to: Required[
        Annotated[Literal["SubscriptionStart", "StartOfTheMonth"], PropertyInfo(alias="accordingTo")]
    ]
    """Reset anchor (SubscriptionStart or StartOfTheMonth)"""


class ChargesPricingModelWeeklyResetPeriodConfiguration(TypedDict, total=False):
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


class ChargesPricingModelYearlyResetPeriodConfiguration(TypedDict, total=False):
    """Yearly reset period configuration"""

    according_to: Required[Annotated[Literal["SubscriptionStart"], PropertyInfo(alias="accordingTo")]]
    """Reset anchor (SubscriptionStart)"""


class ChargesPricingModel(TypedDict, total=False):
    """A pricing model configuration with billing details and price periods."""

    billing_model: Required[
        Annotated[
            Literal["FLAT_FEE", "MINIMUM_SPEND", "PER_UNIT", "USAGE_BASED", "CREDIT_BASED"],
            PropertyInfo(alias="billingModel"),
        ]
    ]
    """The billing model (FLAT_FEE, PER_UNIT, USAGE_BASED, CREDIT_BASED)"""

    price_periods: Required[Annotated[Iterable[ChargesPricingModelPricePeriod], PropertyInfo(alias="pricePeriods")]]
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
        ChargesPricingModelMonthlyResetPeriodConfiguration, PropertyInfo(alias="monthlyResetPeriodConfiguration")
    ]
    """Monthly reset period configuration"""

    reset_period: Annotated[Literal["YEAR", "MONTH", "WEEK", "DAY", "HOUR"], PropertyInfo(alias="resetPeriod")]
    """The usage reset period"""

    tiers_mode: Annotated[Literal["VOLUME", "GRADUATED"], PropertyInfo(alias="tiersMode")]
    """The tiered pricing mode (VOLUME or GRADUATED)"""

    top_up_custom_currency_id: Annotated[str, PropertyInfo(alias="topUpCustomCurrencyId")]
    """The custom currency ID for top-up pricing"""

    weekly_reset_period_configuration: Annotated[
        ChargesPricingModelWeeklyResetPeriodConfiguration, PropertyInfo(alias="weeklyResetPeriodConfiguration")
    ]
    """Weekly reset period configuration"""

    yearly_reset_period_configuration: Annotated[
        ChargesPricingModelYearlyResetPeriodConfiguration, PropertyInfo(alias="yearlyResetPeriodConfiguration")
    ]
    """Yearly reset period configuration"""


class Charges(TypedDict, total=False):
    """Pricing configuration to set on the addon draft"""

    pricing_type: Required[Annotated[Literal["FREE", "PAID", "CUSTOM"], PropertyInfo(alias="pricingType")]]
    """The pricing type (FREE, PAID, or CUSTOM)"""

    billing_id: Annotated[str, PropertyInfo(alias="billingId")]
    """Deprecated: billing integration ID"""

    minimum_spend: Annotated[Optional[Iterable[ChargesMinimumSpend]], PropertyInfo(alias="minimumSpend")]
    """Minimum spend configuration per billing period"""

    overage_billing_period: Annotated[
        Literal["ON_SUBSCRIPTION_RENEWAL", "MONTHLY"], PropertyInfo(alias="overageBillingPeriod")
    ]
    """When overage charges are billed"""

    overage_pricing_models: Annotated[Iterable[ChargesOveragePricingModel], PropertyInfo(alias="overagePricingModels")]
    """Array of overage pricing model configurations"""

    pricing_models: Annotated[Iterable[ChargesPricingModel], PropertyInfo(alias="pricingModels")]
    """Array of pricing model configurations"""
