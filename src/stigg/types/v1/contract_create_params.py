# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = [
    "ContractCreateParams",
    "Subscription",
    "SubscriptionNewSubscription",
    "SubscriptionNewSubscriptionAddon",
    "SubscriptionNewSubscriptionAppliedCoupon",
    "SubscriptionNewSubscriptionAppliedCouponConfiguration",
    "SubscriptionNewSubscriptionAppliedCouponDiscount",
    "SubscriptionNewSubscriptionAppliedCouponDiscountAmountsOff",
    "SubscriptionNewSubscriptionBillingInformation",
    "SubscriptionNewSubscriptionBillingInformationBillingAddress",
    "SubscriptionNewSubscriptionBillingInformationTaxID",
    "SubscriptionNewSubscriptionBudget",
    "SubscriptionNewSubscriptionCharge",
    "SubscriptionNewSubscriptionCheckoutOptions",
    "SubscriptionNewSubscriptionEntitlement",
    "SubscriptionNewSubscriptionEntitlementFeature",
    "SubscriptionNewSubscriptionEntitlementFeatureMonthlyResetPeriodConfiguration",
    "SubscriptionNewSubscriptionEntitlementFeatureWeeklyResetPeriodConfiguration",
    "SubscriptionNewSubscriptionEntitlementFeatureYearlyResetPeriodConfiguration",
    "SubscriptionNewSubscriptionEntitlementCredit",
    "SubscriptionNewSubscriptionMinimumSpend",
    "SubscriptionNewSubscriptionPriceOverride",
    "SubscriptionNewSubscriptionPriceOverrideCreditRate",
    "SubscriptionNewSubscriptionPriceOverrideTier",
    "SubscriptionNewSubscriptionPriceOverrideTierFlatPrice",
    "SubscriptionNewSubscriptionPriceOverrideTierUnitPrice",
    "SubscriptionNewSubscriptionTrialOverrideConfiguration",
]


class ContractCreateParams(TypedDict, total=False):
    customer_id: Required[Annotated[str, PropertyInfo(alias="customerId")]]
    """The customer ref ID the contract belongs to"""

    subscriptions: Required[Iterable[Subscription]]
    """The subscriptions to attach to the contract (must be non-empty).

    Each entry is either a new subscription to create or a reference to an existing
    custom subscription.
    """

    activation_end_date: Annotated[Union[str, datetime], PropertyInfo(alias="activationEndDate", format="iso8601")]
    """Optional contract activation end date"""

    activation_start_date: Annotated[Union[str, datetime], PropertyInfo(alias="activationStartDate", format="iso8601")]
    """Optional contract activation start date"""

    name: Optional[str]
    """Optional contract name"""

    po_number: Annotated[Optional[str], PropertyInfo(alias="poNumber")]
    """Optional purchase-order number"""

    setup_billing: Annotated[bool, PropertyInfo(alias="setupBilling")]
    """
    Whether to set up billing for the contract by creating a billing contract in the
    connected billing provider. When false, the contract only provisions access
    (grants entitlements) and no billing contract is created. Defaults to true.
    """

    x_account_id: Annotated[str, PropertyInfo(alias="X-ACCOUNT-ID")]

    x_environment_id: Annotated[str, PropertyInfo(alias="X-ENVIRONMENT-ID")]


class SubscriptionNewSubscriptionAddon(TypedDict, total=False):
    """Addon configuration"""

    id: Required[str]
    """Addon ID"""

    quantity: Required[int]
    """Number of addon instances"""


class SubscriptionNewSubscriptionAppliedCouponConfiguration(TypedDict, total=False):
    """Coupon timing configuration"""

    start_date: Annotated[Union[str, datetime], PropertyInfo(alias="startDate", format="iso8601")]
    """Coupon start date"""


class SubscriptionNewSubscriptionAppliedCouponDiscountAmountsOff(TypedDict, total=False):
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


class SubscriptionNewSubscriptionAppliedCouponDiscount(TypedDict, total=False):
    """Ad-hoc discount configuration"""

    amounts_off: Annotated[
        Optional[Iterable[SubscriptionNewSubscriptionAppliedCouponDiscountAmountsOff]], PropertyInfo(alias="amountsOff")
    ]
    """Fixed amounts off by currency"""

    description: str
    """Ad-hoc discount"""

    duration_in_months: Annotated[float, PropertyInfo(alias="durationInMonths")]
    """Duration in months"""

    name: str
    """Discount name"""

    percent_off: Annotated[float, PropertyInfo(alias="percentOff")]
    """Percentage discount"""


class SubscriptionNewSubscriptionAppliedCoupon(TypedDict, total=False):
    """Coupon configuration"""

    billing_coupon_id: Annotated[str, PropertyInfo(alias="billingCouponId")]
    """Billing provider coupon ID"""

    configuration: SubscriptionNewSubscriptionAppliedCouponConfiguration
    """Coupon timing configuration"""

    coupon_id: Annotated[str, PropertyInfo(alias="couponId")]
    """Stigg coupon ID"""

    discount: SubscriptionNewSubscriptionAppliedCouponDiscount
    """Ad-hoc discount configuration"""

    promotion_code: Annotated[str, PropertyInfo(alias="promotionCode")]
    """Promotion code to apply"""


class SubscriptionNewSubscriptionBillingInformationBillingAddress(TypedDict, total=False):
    """Billing address for the subscription"""

    city: str

    country: str

    line1: str

    line2: str

    postal_code: Annotated[str, PropertyInfo(alias="postalCode")]

    state: str


class SubscriptionNewSubscriptionBillingInformationTaxID(TypedDict, total=False):
    """Tax identifier with type and value for customer tax exemptions."""

    type: Required[str]
    """The type of tax exemption identifier, such as VAT."""

    value: Required[str]
    """The actual tax identifier value"""


class SubscriptionNewSubscriptionBillingInformation(TypedDict, total=False):
    billing_address: Annotated[
        SubscriptionNewSubscriptionBillingInformationBillingAddress, PropertyInfo(alias="billingAddress")
    ]
    """Billing address for the subscription"""

    charge_on_behalf_of_account: Annotated[Optional[str], PropertyInfo(alias="chargeOnBehalfOfAccount")]
    """Stripe Connect account to charge on behalf of"""

    integration_id: Annotated[Optional[str], PropertyInfo(alias="integrationId")]
    """Billing integration identifier"""

    invoice_days_until_due: Annotated[float, PropertyInfo(alias="invoiceDaysUntilDue")]
    """Number of days until invoice is due"""

    is_backdated: Annotated[bool, PropertyInfo(alias="isBackdated")]
    """Whether the subscription is backdated"""

    is_invoice_paid: Annotated[bool, PropertyInfo(alias="isInvoicePaid")]
    """Whether the invoice is marked as paid"""

    metadata: Dict[str, str]
    """
    Additional metadata for the subscription, stored as an arbitrary flat key-value
    object.
    """

    proration_behavior: Annotated[
        Literal["INVOICE_IMMEDIATELY", "CREATE_PRORATIONS", "NONE"], PropertyInfo(alias="prorationBehavior")
    ]
    """How to handle proration for billing changes"""

    tax_ids: Annotated[Iterable[SubscriptionNewSubscriptionBillingInformationTaxID], PropertyInfo(alias="taxIds")]
    """Customer tax identification numbers"""

    tax_percentage: Annotated[float, PropertyInfo(alias="taxPercentage")]
    """Tax percentage (0-100)"""

    tax_rate_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="taxRateIds")]
    """Tax rate identifiers to apply"""


class SubscriptionNewSubscriptionBudget(TypedDict, total=False):
    has_soft_limit: Required[Annotated[bool, PropertyInfo(alias="hasSoftLimit")]]
    """Whether the budget is a soft limit"""

    limit: Required[float]
    """Maximum spending limit"""


class SubscriptionNewSubscriptionCharge(TypedDict, total=False):
    """
    A charge selection for a subscription (references a catalog charge with a quantity).
    """

    id: Required[str]
    """Charge ID"""

    quantity: Required[float]
    """Charge quantity. Minimum is 0 (zero is allowed)."""

    type: Required[Literal["FEATURE", "CREDIT"]]
    """Charge type"""


class SubscriptionNewSubscriptionCheckoutOptions(TypedDict, total=False):
    """Checkout page configuration for payment collection"""

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


class SubscriptionNewSubscriptionEntitlementFeatureMonthlyResetPeriodConfiguration(TypedDict, total=False):
    """Configuration for monthly reset period"""

    according_to: Required[
        Annotated[Literal["SubscriptionStart", "StartOfTheMonth"], PropertyInfo(alias="accordingTo")]
    ]
    """Reset anchor (SubscriptionStart or StartOfTheMonth)"""


class SubscriptionNewSubscriptionEntitlementFeatureWeeklyResetPeriodConfiguration(TypedDict, total=False):
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


class SubscriptionNewSubscriptionEntitlementFeatureYearlyResetPeriodConfiguration(TypedDict, total=False):
    """Configuration for yearly reset period"""

    according_to: Required[Annotated[Literal["SubscriptionStart"], PropertyInfo(alias="accordingTo")]]
    """Reset anchor (SubscriptionStart)"""


class SubscriptionNewSubscriptionEntitlementFeature(TypedDict, total=False):
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
        Optional[SubscriptionNewSubscriptionEntitlementFeatureMonthlyResetPeriodConfiguration],
        PropertyInfo(alias="monthlyResetPeriodConfiguration"),
    ]
    """Configuration for monthly reset period"""

    reset_period: Annotated[Literal["YEAR", "MONTH", "WEEK", "DAY", "HOUR"], PropertyInfo(alias="resetPeriod")]
    """Period at which usage resets"""

    usage_limit: Annotated[int, PropertyInfo(alias="usageLimit")]
    """Maximum allowed usage for the feature"""

    weekly_reset_period_configuration: Annotated[
        Optional[SubscriptionNewSubscriptionEntitlementFeatureWeeklyResetPeriodConfiguration],
        PropertyInfo(alias="weeklyResetPeriodConfiguration"),
    ]
    """Configuration for weekly reset period"""

    yearly_reset_period_configuration: Annotated[
        Optional[SubscriptionNewSubscriptionEntitlementFeatureYearlyResetPeriodConfiguration],
        PropertyInfo(alias="yearlyResetPeriodConfiguration"),
    ]
    """Configuration for yearly reset period"""


class SubscriptionNewSubscriptionEntitlementCredit(TypedDict, total=False):
    """Credit entitlement configuration for a subscription"""

    id: Required[str]
    """The custom currency ID for the credit entitlement"""

    amount: Required[float]
    """Credit grant amount"""

    cadence: Required[Literal["MONTH", "YEAR"]]
    """Credit grant cadence (MONTH or YEAR)"""

    type: Required[Literal["CREDIT"]]
    """SubscriptionCreditEntitlementRequest"""

    has_soft_limit: Annotated[bool, PropertyInfo(alias="hasSoftLimit")]
    """Whether the credit balance is a soft limit"""


SubscriptionNewSubscriptionEntitlement: TypeAlias = Union[
    SubscriptionNewSubscriptionEntitlementFeature, SubscriptionNewSubscriptionEntitlementCredit
]


class SubscriptionNewSubscriptionMinimumSpend(TypedDict, total=False):
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


class SubscriptionNewSubscriptionPriceOverrideCreditRate(TypedDict, total=False):
    amount: Required[float]
    """The credit rate amount"""

    currency_id: Required[Annotated[str, PropertyInfo(alias="currencyId")]]
    """The custom currency refId for the credit rate"""

    cost_formula: Annotated[Optional[str], PropertyInfo(alias="costFormula")]
    """A custom formula for calculating cost based on single event dimensions"""


class SubscriptionNewSubscriptionPriceOverrideTierFlatPrice(TypedDict, total=False):
    """The flat fee price of the price tier"""

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


class SubscriptionNewSubscriptionPriceOverrideTierUnitPrice(TypedDict, total=False):
    """The unit price of the price tier"""

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


class SubscriptionNewSubscriptionPriceOverrideTier(TypedDict, total=False):
    flat_price: Annotated[SubscriptionNewSubscriptionPriceOverrideTierFlatPrice, PropertyInfo(alias="flatPrice")]
    """The flat fee price of the price tier"""

    unit_price: Annotated[SubscriptionNewSubscriptionPriceOverrideTierUnitPrice, PropertyInfo(alias="unitPrice")]
    """The unit price of the price tier"""

    up_to: Annotated[float, PropertyInfo(alias="upTo")]
    """The up to quantity of the price tier"""


class SubscriptionNewSubscriptionPriceOverride(TypedDict, total=False):
    addon_id: Annotated[Optional[str], PropertyInfo(alias="addonId")]
    """Addon identifier for the price override"""

    amount: float
    """The price amount"""

    base_charge: Annotated[bool, PropertyInfo(alias="baseCharge")]
    """Whether this is a base charge override"""

    billing_country_code: Annotated[str, PropertyInfo(alias="billingCountryCode")]
    """ISO 3166-1 alpha-2 country code this price applies to.

    Omit for the default price shown to all countries; set one or more
    country-specific price periods on the same currency to localize the amount by
    billing country.
    """

    block_size: Annotated[float, PropertyInfo(alias="blockSize")]
    """Block size for pricing"""

    credit_grant_cadence: Annotated[
        Literal["BEGINNING_OF_BILLING_PERIOD", "MONTHLY"], PropertyInfo(alias="creditGrantCadence")
    ]

    credit_rate: Annotated[SubscriptionNewSubscriptionPriceOverrideCreditRate, PropertyInfo(alias="creditRate")]

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

    feature_id: Annotated[Optional[str], PropertyInfo(alias="featureId")]
    """Feature identifier for the price override"""

    tiers: Iterable[SubscriptionNewSubscriptionPriceOverrideTier]
    """Pricing tiers configuration"""


class SubscriptionNewSubscriptionTrialOverrideConfiguration(TypedDict, total=False):
    """Trial period override settings"""

    is_trial: Required[Annotated[bool, PropertyInfo(alias="isTrial")]]
    """Whether the subscription should start with a trial period"""

    trial_end_behavior: Annotated[
        Literal["CONVERT_TO_PAID", "CANCEL_SUBSCRIPTION"], PropertyInfo(alias="trialEndBehavior")
    ]
    """Behavior when trial ends: CONVERT_TO_PAID or CANCEL_SUBSCRIPTION"""

    trial_end_date: Annotated[Union[str, datetime], PropertyInfo(alias="trialEndDate", format="iso8601")]
    """Custom trial end date"""


class SubscriptionNewSubscription(TypedDict, total=False):
    """
    A new subscription to create, using the same body the provision-subscription endpoint accepts
    """

    customer_id: Required[Annotated[str, PropertyInfo(alias="customerId")]]
    """Customer ID to provision the subscription for"""

    plan_id: Required[Annotated[str, PropertyInfo(alias="planId")]]
    """Plan ID to provision"""

    id: str
    """Unique identifier for the subscription"""

    addons: Iterable[SubscriptionNewSubscriptionAddon]

    applied_coupon: Annotated[SubscriptionNewSubscriptionAppliedCoupon, PropertyInfo(alias="appliedCoupon")]
    """Coupon configuration"""

    await_payment_confirmation: Annotated[bool, PropertyInfo(alias="awaitPaymentConfirmation")]
    """Whether to wait for payment confirmation before returning the subscription"""

    billing_country_code: Annotated[Optional[str], PropertyInfo(alias="billingCountryCode")]
    """The ISO 3166-1 alpha-2 country code for billing"""

    billing_cycle_anchor: Annotated[Literal["UNCHANGED", "NOW"], PropertyInfo(alias="billingCycleAnchor")]
    """Billing cycle anchor behavior for the subscription"""

    billing_id: Annotated[Optional[str], PropertyInfo(alias="billingId")]
    """External billing system identifier"""

    billing_information: Annotated[
        SubscriptionNewSubscriptionBillingInformation, PropertyInfo(alias="billingInformation")
    ]

    billing_period: Annotated[Literal["MONTHLY", "ANNUALLY"], PropertyInfo(alias="billingPeriod")]
    """Billing period (MONTHLY or ANNUALLY)"""

    budget: Optional[SubscriptionNewSubscriptionBudget]

    cancellation_date: Annotated[Union[str, datetime], PropertyInfo(alias="cancellationDate", format="iso8601")]
    """Subscription cancellation date"""

    charges: Iterable[SubscriptionNewSubscriptionCharge]

    checkout_options: Annotated[SubscriptionNewSubscriptionCheckoutOptions, PropertyInfo(alias="checkoutOptions")]
    """Checkout page configuration for payment collection"""

    entitlements: Iterable[SubscriptionNewSubscriptionEntitlement]

    metadata: Dict[str, str]
    """
    Additional metadata for the subscription, stored as an arbitrary flat key-value
    object.
    """

    minimum_spend: Annotated[Optional[SubscriptionNewSubscriptionMinimumSpend], PropertyInfo(alias="minimumSpend")]
    """Minimum spend amount"""

    paying_customer_id: Annotated[Optional[str], PropertyInfo(alias="payingCustomerId")]
    """Optional paying customer ID for split billing scenarios"""

    payment_collection_method: Annotated[
        Literal["CHARGE", "INVOICE", "NONE"], PropertyInfo(alias="paymentCollectionMethod")
    ]
    """How payments should be collected for this subscription"""

    price_overrides: Annotated[Iterable[SubscriptionNewSubscriptionPriceOverride], PropertyInfo(alias="priceOverrides")]

    resource_id: Annotated[Optional[str], PropertyInfo(alias="resourceId")]
    """Optional resource ID for multi-instance subscriptions"""

    salesforce_id: Annotated[Optional[str], PropertyInfo(alias="salesforceId")]
    """Salesforce ID"""

    schedule_strategy: Annotated[
        Literal["END_OF_BILLING_PERIOD", "END_OF_BILLING_MONTH", "IMMEDIATE"], PropertyInfo(alias="scheduleStrategy")
    ]
    """Strategy for scheduling subscription changes"""

    start_date: Annotated[Union[str, datetime], PropertyInfo(alias="startDate", format="iso8601")]
    """Subscription start date"""

    trial_override_configuration: Annotated[
        SubscriptionNewSubscriptionTrialOverrideConfiguration, PropertyInfo(alias="trialOverrideConfiguration")
    ]
    """Trial period override settings"""

    unit_quantity: Annotated[int, PropertyInfo(alias="unitQuantity")]
    """Unit quantity for per-unit pricing. Minimum is 0 (zero is allowed)."""


class Subscription(TypedDict, total=False):
    """
    A single subscription on a contract: exactly one of newSubscription or existingSubscriptionId must be set.
    """

    existing_subscription_id: Annotated[str, PropertyInfo(alias="existingSubscriptionId")]
    """The subscription ref ID of an already-created custom subscription to link"""

    new_subscription: Annotated[SubscriptionNewSubscription, PropertyInfo(alias="newSubscription")]
    """
    A new subscription to create, using the same body the provision-subscription
    endpoint accepts
    """
