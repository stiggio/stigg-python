# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "CustomerResponse",
    "Data",
    "DataDefaultPaymentMethod",
    "DataIntegration",
    "DataPassthrough",
    "DataPassthroughStripe",
    "DataPassthroughStripeBillingAddress",
    "DataPassthroughStripeShippingAddress",
    "DataPassthroughStripeTaxID",
    "DataPassthroughZuora",
    "DataPassthroughZuoraBillingAddress",
]


class DataDefaultPaymentMethod(BaseModel):
    """The default payment method details"""

    billing_id: Optional[str] = FieldInfo(alias="billingId", default=None)
    """The default payment method id"""

    card_expiry_month: Optional[float] = FieldInfo(alias="cardExpiryMonth", default=None)
    """The expiration month of the default payment method"""

    card_expiry_year: Optional[float] = FieldInfo(alias="cardExpiryYear", default=None)
    """The expiration year of the default payment method"""

    card_last4_digits: Optional[str] = FieldInfo(alias="cardLast4Digits", default=None)
    """The last 4 digits of the default payment method"""

    type: Literal["CARD", "BANK", "CASH_APP"]
    """The default payment method type"""


class DataIntegration(BaseModel):
    """External billing or CRM integration link"""

    id: str
    """Integration details"""

    synced_entity_id: Optional[str] = FieldInfo(alias="syncedEntityId", default=None)
    """Synced entity id"""

    vendor_identifier: Literal[
        "AUTH0",
        "ZUORA",
        "STRIPE",
        "HUBSPOT",
        "AWS_MARKETPLACE",
        "SNOWFLAKE",
        "SALESFORCE",
        "BIG_QUERY",
        "OPEN_FGA",
        "APP_STORE",
    ] = FieldInfo(alias="vendorIdentifier")
    """The vendor identifier of integration"""


class DataPassthroughStripeBillingAddress(BaseModel):
    """Physical address"""

    city: Optional[str] = None
    """City name"""

    country: Optional[str] = None
    """Country code or name"""

    line1: Optional[str] = None
    """Street address line 1"""

    line2: Optional[str] = None
    """Street address line 2"""

    postal_code: Optional[str] = FieldInfo(alias="postalCode", default=None)
    """Postal or ZIP code"""

    state: Optional[str] = None
    """State or province"""


class DataPassthroughStripeShippingAddress(BaseModel):
    """Physical address"""

    city: Optional[str] = None
    """City name"""

    country: Optional[str] = None
    """Country code or name"""

    line1: Optional[str] = None
    """Street address line 1"""

    line2: Optional[str] = None
    """Street address line 2"""

    postal_code: Optional[str] = FieldInfo(alias="postalCode", default=None)
    """Postal or ZIP code"""

    state: Optional[str] = None
    """State or province"""


class DataPassthroughStripeTaxID(BaseModel):
    """Tax identifier with type and value for customer tax exemptions."""

    type: str
    """The type of tax exemption identifier, such as VAT."""

    value: str
    """The actual tax identifier value"""


class DataPassthroughStripe(BaseModel):
    """Stripe-specific billing fields for the customer."""

    billing_address: Optional[DataPassthroughStripeBillingAddress] = FieldInfo(alias="billingAddress", default=None)
    """Physical address"""

    customer_name: Optional[str] = FieldInfo(alias="customerName", default=None)
    """Customer name"""

    invoice_custom_fields: Optional[Dict[str, str]] = FieldInfo(alias="invoiceCustomFields", default=None)
    """Invoice custom fields"""

    metadata: Optional[Dict[str, str]] = None
    """Additional metadata"""

    payment_method_id: Optional[str] = FieldInfo(alias="paymentMethodId", default=None)
    """Billing provider payment method id, attached to this customer"""

    shipping_address: Optional[DataPassthroughStripeShippingAddress] = FieldInfo(alias="shippingAddress", default=None)
    """Physical address"""

    tax_ids: Optional[List[DataPassthroughStripeTaxID]] = FieldInfo(alias="taxIds", default=None)
    """Tax IDs"""


class DataPassthroughZuoraBillingAddress(BaseModel):
    """Physical address"""

    city: Optional[str] = None
    """City name"""

    country: Optional[str] = None
    """Country code or name"""

    line1: Optional[str] = None
    """Street address line 1"""

    line2: Optional[str] = None
    """Street address line 2"""

    postal_code: Optional[str] = FieldInfo(alias="postalCode", default=None)
    """Postal or ZIP code"""

    state: Optional[str] = None
    """State or province"""


class DataPassthroughZuora(BaseModel):
    """Zuora-specific billing fields for the customer."""

    billing_address: Optional[DataPassthroughZuoraBillingAddress] = FieldInfo(alias="billingAddress", default=None)
    """Physical address"""

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
    """Customers selected currency"""

    metadata: Optional[Dict[str, str]] = None
    """Additional metadata"""

    payment_method_id: Optional[str] = FieldInfo(alias="paymentMethodId", default=None)
    """Billing provider payment method id, attached to this customer"""


class DataPassthrough(BaseModel):
    """Vendor-specific billing passthrough fields."""

    stripe: Optional[DataPassthroughStripe] = None
    """Stripe-specific billing fields for the customer."""

    zuora: Optional[DataPassthroughZuora] = None
    """Zuora-specific billing fields for the customer."""


class Data(BaseModel):
    """A customer can be either an organization or an individual"""

    id: str
    """Customer slug"""

    archived_at: Optional[datetime] = FieldInfo(alias="archivedAt", default=None)
    """Timestamp of when the record was deleted"""

    created_at: datetime = FieldInfo(alias="createdAt")
    """Timestamp of when the record was created"""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """Timestamp of when the record was last updated"""

    billing_currency: Optional[
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
    ] = FieldInfo(alias="billingCurrency", default=None)
    """The billing currency of the customer"""

    billing_id: Optional[str] = FieldInfo(alias="billingId", default=None)
    """The unique identifier for the entity in the billing provider"""

    coupon_id: Union[str, Literal[""], None] = FieldInfo(alias="couponId", default=None)
    """Customer level coupon"""

    default_payment_method: Optional[DataDefaultPaymentMethod] = FieldInfo(alias="defaultPaymentMethod", default=None)
    """The default payment method details"""

    email: Optional[str] = None
    """The email of the customer"""

    integrations: Optional[List[DataIntegration]] = None
    """List of integrations"""

    language: Optional[str] = None
    """Language to use for this customer"""

    metadata: Optional[Dict[str, str]] = None
    """Additional metadata"""

    name: Optional[str] = None
    """The name of the customer"""

    passthrough: Optional[DataPassthrough] = None
    """Vendor-specific billing passthrough fields."""

    timezone: Optional[str] = None
    """Timezone to use for this customer"""


class CustomerResponse(BaseModel):
    """Response object"""

    data: Data
    """A customer can be either an organization or an individual"""
