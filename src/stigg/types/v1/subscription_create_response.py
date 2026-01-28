# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "SubscriptionCreateResponse",
    "Data",
    "DataEntitlement",
    "DataEntitlementFeature",
    "DataSubscription",
    "DataSubscriptionPrice",
    "DataSubscriptionPricePrice",
    "DataSubscriptionPriceTier",
    "DataSubscriptionPriceTierFlatPrice",
    "DataSubscriptionPriceTierUnitPrice",
]


class DataEntitlementFeature(BaseModel):
    ref_id: str = FieldInfo(alias="refId")


class DataEntitlement(BaseModel):
    access_denied_reason: Optional[str] = FieldInfo(alias="accessDeniedReason", default=None)

    current_usage: Optional[float] = FieldInfo(alias="currentUsage", default=None)

    entitlement_updated_at: Optional[datetime] = FieldInfo(alias="entitlementUpdatedAt", default=None)
    """entitlement updated at"""

    feature: Optional[DataEntitlementFeature] = None

    has_unlimited_usage: Optional[bool] = FieldInfo(alias="hasUnlimitedUsage", default=None)

    is_granted: Optional[bool] = FieldInfo(alias="isGranted", default=None)

    reset_period: Optional[Literal["YEAR", "MONTH", "WEEK", "DAY", "HOUR"]] = FieldInfo(
        alias="resetPeriod", default=None
    )

    usage_limit: Optional[float] = FieldInfo(alias="usageLimit", default=None)

    usage_period_anchor: Optional[datetime] = FieldInfo(alias="usagePeriodAnchor", default=None)
    """usage period anchor"""

    usage_period_end: Optional[datetime] = FieldInfo(alias="usagePeriodEnd", default=None)
    """usage period end"""

    usage_period_start: Optional[datetime] = FieldInfo(alias="usagePeriodStart", default=None)
    """usage period start"""


class DataSubscriptionPricePrice(BaseModel):
    """Override price amount"""

    amount: Optional[float] = None
    """The price amount"""

    billing_country_code: Optional[str] = FieldInfo(alias="billingCountryCode", default=None)
    """The billing country code of the price"""

    currency: Optional[
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
    ] = None
    """The price currency"""


class DataSubscriptionPriceTierFlatPrice(BaseModel):
    """The flat fee price of the price tier"""

    amount: Optional[float] = None
    """The price amount"""

    billing_country_code: Optional[str] = FieldInfo(alias="billingCountryCode", default=None)
    """The billing country code of the price"""

    currency: Optional[
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
    ] = None
    """The price currency"""


class DataSubscriptionPriceTierUnitPrice(BaseModel):
    """The unit price of the price tier"""

    amount: Optional[float] = None
    """The price amount"""

    billing_country_code: Optional[str] = FieldInfo(alias="billingCountryCode", default=None)
    """The billing country code of the price"""

    currency: Optional[
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
    ] = None
    """The price currency"""


class DataSubscriptionPriceTier(BaseModel):
    flat_price: Optional[DataSubscriptionPriceTierFlatPrice] = FieldInfo(alias="flatPrice", default=None)
    """The flat fee price of the price tier"""

    unit_price: Optional[DataSubscriptionPriceTierUnitPrice] = FieldInfo(alias="unitPrice", default=None)
    """The unit price of the price tier"""

    up_to: Optional[float] = FieldInfo(alias="upTo", default=None)
    """The up to quantity of the price tier"""


class DataSubscriptionPrice(BaseModel):
    addon_id: Optional[str] = FieldInfo(alias="addonId", default=None)
    """Addon identifier for the price override"""

    base_charge: Optional[bool] = FieldInfo(alias="baseCharge", default=None)
    """Whether this is a base charge override"""

    block_size: Optional[float] = FieldInfo(alias="blockSize", default=None)
    """Block size for pricing"""

    feature_id: Optional[str] = FieldInfo(alias="featureId", default=None)
    """Feature identifier for the price override"""

    price: Optional[DataSubscriptionPricePrice] = None
    """Override price amount"""

    tiers: Optional[List[DataSubscriptionPriceTier]] = None
    """Pricing tiers configuration"""


class DataSubscription(BaseModel):
    id: str
    """Subscription ID"""

    billing_id: Optional[str] = FieldInfo(alias="billingId", default=None)
    """Billing ID"""

    created_at: datetime = FieldInfo(alias="createdAt")
    """Created at"""

    customer_id: str = FieldInfo(alias="customerId")
    """Customer ID"""

    payment_collection: Literal["NOT_REQUIRED", "PROCESSING", "FAILED", "ACTION_REQUIRED"] = FieldInfo(
        alias="paymentCollection"
    )
    """Payment collection"""

    plan_id: str = FieldInfo(alias="planId")
    """Plan ID"""

    pricing_type: Literal["FREE", "PAID", "CUSTOM"] = FieldInfo(alias="pricingType")
    """Pricing type"""

    start_date: datetime = FieldInfo(alias="startDate")
    """Subscription start date"""

    status: Literal["PAYMENT_PENDING", "ACTIVE", "EXPIRED", "IN_TRIAL", "CANCELED", "NOT_STARTED"]
    """Subscription status"""

    cancellation_date: Optional[datetime] = FieldInfo(alias="cancellationDate", default=None)
    """Subscription cancellation date"""

    cancel_reason: Optional[
        Literal[
            "UPGRADE_OR_DOWNGRADE",
            "CANCELLED_BY_BILLING",
            "EXPIRED",
            "DETACH_BILLING",
            "TRIAL_ENDED",
            "Immediate",
            "TRIAL_CONVERTED",
            "PENDING_PAYMENT_EXPIRED",
            "ScheduledCancellation",
            "CustomerArchived",
            "AutoCancellationRule",
        ]
    ] = FieldInfo(alias="cancelReason", default=None)
    """Subscription cancel reason"""

    current_billing_period_end: Optional[datetime] = FieldInfo(alias="currentBillingPeriodEnd", default=None)
    """End of the current billing period"""

    current_billing_period_start: Optional[datetime] = FieldInfo(alias="currentBillingPeriodStart", default=None)
    """Start of the current billing period"""

    effective_end_date: Optional[datetime] = FieldInfo(alias="effectiveEndDate", default=None)
    """Subscription effective end date"""

    end_date: Optional[datetime] = FieldInfo(alias="endDate", default=None)
    """Subscription end date"""

    metadata: Optional[Dict[str, str]] = None
    """Additional metadata for the subscription"""

    paying_customer_id: Optional[str] = FieldInfo(alias="payingCustomerId", default=None)
    """Paying customer ID for delegated billing"""

    payment_collection_method: Optional[Literal["CHARGE", "INVOICE", "NONE"]] = FieldInfo(
        alias="paymentCollectionMethod", default=None
    )
    """The method used to collect payments for a subscription"""

    prices: Optional[List[DataSubscriptionPrice]] = None

    resource_id: Optional[str] = FieldInfo(alias="resourceId", default=None)
    """Resource ID"""

    trial_end_date: Optional[datetime] = FieldInfo(alias="trialEndDate", default=None)
    """Subscription trial end date"""

    unit_quantity: Optional[float] = FieldInfo(alias="unitQuantity", default=None)


class Data(BaseModel):
    id: str
    """Unique identifier for the provisioned subscription"""

    entitlements: List[DataEntitlement]

    status: Literal["SUCCESS", "PAYMENT_REQUIRED"]
    """Provision status: SUCCESS or PAYMENT_REQUIRED"""

    checkout_billing_id: Optional[str] = FieldInfo(alias="checkoutBillingId", default=None)
    """Checkout billing ID when payment is required"""

    checkout_url: Optional[str] = FieldInfo(alias="checkoutUrl", default=None)
    """URL to complete payment when PAYMENT_REQUIRED"""

    is_scheduled: Optional[bool] = FieldInfo(alias="isScheduled", default=None)
    """Whether the subscription is scheduled for future activation"""

    subscription: Optional[DataSubscription] = None


class SubscriptionCreateResponse(BaseModel):
    data: Data
