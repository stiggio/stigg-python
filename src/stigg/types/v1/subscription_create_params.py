# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = [
    "SubscriptionCreateParams",
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
    "CheckoutOptions",
    "MinimumSpend",
    "MinimumSpendMinimum",
    "PriceOverride",
    "PriceOverrideCreditRate",
    "PriceOverridePrice",
    "PriceOverrideTier",
    "PriceOverrideTierFlatPrice",
    "PriceOverrideTierUnitPrice",
    "SubscriptionEntitlement",
    "TrialOverrideConfiguration",
]


class SubscriptionCreateParams(TypedDict, total=False):
    customer_id: Required[Annotated[str, PropertyInfo(alias="customerId")]]
    """Customer ID to provision the subscription for"""

    plan_id: Required[Annotated[str, PropertyInfo(alias="planId")]]
    """Plan ID to provision"""

    id: str
    """Unique identifier for the subscription"""

    addons: Iterable[Addon]

    applied_coupon: Annotated[AppliedCoupon, PropertyInfo(alias="appliedCoupon")]
    """Coupon configuration"""

    await_payment_confirmation: Annotated[bool, PropertyInfo(alias="awaitPaymentConfirmation")]
    """Whether to wait for payment confirmation before returning the subscription"""

    billing_country_code: Annotated[Optional[str], PropertyInfo(alias="billingCountryCode")]
    """The ISO 3166-1 alpha-2 country code for billing"""

    billing_id: Annotated[Optional[str], PropertyInfo(alias="billingId")]
    """External billing system identifier"""

    billing_information: Annotated[BillingInformation, PropertyInfo(alias="billingInformation")]

    billing_period: Annotated[Literal["MONTHLY", "ANNUALLY"], PropertyInfo(alias="billingPeriod")]
    """Billing period (MONTHLY or ANNUALLY)"""

    budget: Optional[Budget]

    charges: Iterable[Charge]

    checkout_options: Annotated[CheckoutOptions, PropertyInfo(alias="checkoutOptions")]
    """Checkout page configuration for payment collection"""

    metadata: Dict[str, str]
    """Additional metadata for the subscription"""

    minimum_spend: Annotated[Optional[MinimumSpend], PropertyInfo(alias="minimumSpend")]

    paying_customer_id: Annotated[Optional[str], PropertyInfo(alias="payingCustomerId")]
    """Optional paying customer ID for split billing scenarios"""

    payment_collection_method: Annotated[
        Literal["CHARGE", "INVOICE", "NONE"], PropertyInfo(alias="paymentCollectionMethod")
    ]
    """How payments should be collected for this subscription"""

    price_overrides: Annotated[Iterable[PriceOverride], PropertyInfo(alias="priceOverrides")]

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

    subscription_entitlements: Annotated[
        Iterable[SubscriptionEntitlement], PropertyInfo(alias="subscriptionEntitlements")
    ]

    trial_override_configuration: Annotated[
        TrialOverrideConfiguration, PropertyInfo(alias="trialOverrideConfiguration")
    ]
    """Trial period override settings"""

    unit_quantity: Annotated[float, PropertyInfo(alias="unitQuantity")]


class Addon(TypedDict, total=False):
    addon_id: Required[Annotated[str, PropertyInfo(alias="addonId")]]
    """Addon identifier"""

    quantity: int
    """Number of addon units"""


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
    """Coupon configuration"""

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


class BillingInformationBillingAddress(TypedDict, total=False):
    """Billing address for the subscription"""

    city: str

    country: str

    line1: str

    line2: str

    postal_code: Annotated[str, PropertyInfo(alias="postalCode")]

    state: str


class BillingInformationTaxID(TypedDict, total=False):
    type: Required[str]
    """The type of tax exemption identifier, such as VAT."""

    value: Required[str]
    """The actual tax identifier value"""


class BillingInformation(TypedDict, total=False):
    billing_address: Annotated[BillingInformationBillingAddress, PropertyInfo(alias="billingAddress")]
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
    """Additional metadata for the subscription"""

    proration_behavior: Annotated[
        Literal["INVOICE_IMMEDIATELY", "CREATE_PRORATIONS", "NONE"], PropertyInfo(alias="prorationBehavior")
    ]
    """How to handle proration for billing changes"""

    tax_ids: Annotated[Iterable[BillingInformationTaxID], PropertyInfo(alias="taxIds")]
    """Customer tax identification numbers"""

    tax_percentage: Annotated[float, PropertyInfo(alias="taxPercentage")]
    """Tax percentage (0-100)"""

    tax_rate_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="taxRateIds")]
    """Tax rate identifiers to apply"""


class Budget(TypedDict, total=False):
    has_soft_limit: Required[Annotated[bool, PropertyInfo(alias="hasSoftLimit")]]
    """Whether the budget is a soft limit"""

    limit: Required[float]
    """Maximum spending limit"""


class Charge(TypedDict, total=False):
    """Charge item"""

    id: Required[str]
    """Charge ID"""

    quantity: Required[float]
    """Charge quantity"""

    type: Required[Literal["FEATURE", "CREDIT"]]
    """Charge type"""


class CheckoutOptions(TypedDict, total=False):
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


class MinimumSpendMinimum(TypedDict, total=False):
    """Minimum spend amount"""

    amount: float
    """The price amount"""

    billing_country_code: Annotated[Optional[str], PropertyInfo(alias="billingCountryCode")]
    """The billing country code of the price"""

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
    minimum: Optional[MinimumSpendMinimum]
    """Minimum spend amount"""


class PriceOverrideCreditRate(TypedDict, total=False):
    amount: Required[float]
    """The credit rate amount"""

    currency_id: Required[Annotated[str, PropertyInfo(alias="currencyId")]]
    """The custom currency refId for the credit rate"""

    cost_formula: Annotated[Optional[str], PropertyInfo(alias="costFormula")]
    """A custom formula for calculating cost based on single event dimensions"""


class PriceOverridePrice(TypedDict, total=False):
    """Override price amount"""

    amount: float
    """The price amount"""

    billing_country_code: Annotated[Optional[str], PropertyInfo(alias="billingCountryCode")]
    """The billing country code of the price"""

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


class PriceOverrideTierFlatPrice(TypedDict, total=False):
    """The flat fee price of the price tier"""

    amount: float
    """The price amount"""

    billing_country_code: Annotated[Optional[str], PropertyInfo(alias="billingCountryCode")]
    """The billing country code of the price"""

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


class PriceOverrideTierUnitPrice(TypedDict, total=False):
    """The unit price of the price tier"""

    amount: float
    """The price amount"""

    billing_country_code: Annotated[Optional[str], PropertyInfo(alias="billingCountryCode")]
    """The billing country code of the price"""

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


class PriceOverrideTier(TypedDict, total=False):
    flat_price: Annotated[PriceOverrideTierFlatPrice, PropertyInfo(alias="flatPrice")]
    """The flat fee price of the price tier"""

    unit_price: Annotated[PriceOverrideTierUnitPrice, PropertyInfo(alias="unitPrice")]
    """The unit price of the price tier"""

    up_to: Annotated[float, PropertyInfo(alias="upTo")]
    """The up to quantity of the price tier"""


class PriceOverride(TypedDict, total=False):
    addon_id: Annotated[Optional[str], PropertyInfo(alias="addonId")]
    """Addon identifier for the price override"""

    base_charge: Annotated[bool, PropertyInfo(alias="baseCharge")]
    """Whether this is a base charge override"""

    block_size: Annotated[float, PropertyInfo(alias="blockSize")]
    """Block size for pricing"""

    credit_grant_cadence: Annotated[
        Literal["BEGINNING_OF_BILLING_PERIOD", "MONTHLY"], PropertyInfo(alias="creditGrantCadence")
    ]

    credit_rate: Annotated[PriceOverrideCreditRate, PropertyInfo(alias="creditRate")]

    feature_id: Annotated[Optional[str], PropertyInfo(alias="featureId")]
    """Feature identifier for the price override"""

    price: PriceOverridePrice
    """Override price amount"""

    tiers: Iterable[PriceOverrideTier]
    """Pricing tiers configuration"""


class SubscriptionEntitlement(TypedDict, total=False):
    feature_id: Required[Annotated[str, PropertyInfo(alias="featureId")]]
    """Feature ID"""

    usage_limit: Required[Annotated[float, PropertyInfo(alias="usageLimit")]]

    is_granted: Annotated[bool, PropertyInfo(alias="isGranted")]


class TrialOverrideConfiguration(TypedDict, total=False):
    """Trial period override settings"""

    is_trial: Required[Annotated[bool, PropertyInfo(alias="isTrial")]]
    """Whether the subscription should start with a trial period"""

    trial_end_behavior: Annotated[
        Literal["CONVERT_TO_PAID", "CANCEL_SUBSCRIPTION"], PropertyInfo(alias="trialEndBehavior")
    ]
    """Behavior when trial ends: CONVERT_TO_PAID or CANCEL_SUBSCRIPTION"""

    trial_end_date: Annotated[Union[str, datetime], PropertyInfo(alias="trialEndDate", format="iso8601")]
    """Custom trial end date"""
