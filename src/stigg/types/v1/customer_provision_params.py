# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "CustomerProvisionParams",
    "DefaultPaymentMethod",
    "Integration",
    "Passthrough",
    "PassthroughStripe",
    "PassthroughStripeBillingAddress",
    "PassthroughStripeShippingAddress",
    "PassthroughStripeTaxID",
    "PassthroughZuora",
    "PassthroughZuoraBillingAddress",
]


class CustomerProvisionParams(TypedDict, total=False):
    id: Required[str]
    """Customer slug"""

    billing_currency: Annotated[
        Optional[
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
        ],
        PropertyInfo(alias="billingCurrency"),
    ]
    """The billing currency of the customer"""

    billing_id: Annotated[Optional[str], PropertyInfo(alias="billingId")]
    """The unique identifier for the entity in the billing provider"""

    coupon_id: Annotated[Union[str, Literal[""], None], PropertyInfo(alias="couponId")]
    """Customer level coupon"""

    default_payment_method: Annotated[Optional[DefaultPaymentMethod], PropertyInfo(alias="defaultPaymentMethod")]
    """The default payment method details"""

    email: Optional[str]
    """The email of the customer"""

    integrations: Iterable[Integration]
    """List of integrations"""

    language: Optional[str]
    """Language to use for this customer"""

    metadata: Dict[str, str]
    """Additional metadata"""

    name: Optional[str]
    """The name of the customer"""

    passthrough: Passthrough
    """Vendor-specific billing passthrough fields."""

    timezone: Optional[str]
    """Timezone to use for this customer"""


class DefaultPaymentMethod(TypedDict, total=False):
    """The default payment method details"""

    billing_id: Required[Annotated[Optional[str], PropertyInfo(alias="billingId")]]
    """The default payment method id"""

    card_expiry_month: Required[Annotated[Optional[float], PropertyInfo(alias="cardExpiryMonth")]]
    """The expiration month of the default payment method"""

    card_expiry_year: Required[Annotated[Optional[float], PropertyInfo(alias="cardExpiryYear")]]
    """The expiration year of the default payment method"""

    card_last4_digits: Required[Annotated[Optional[str], PropertyInfo(alias="cardLast4Digits")]]
    """The last 4 digits of the default payment method"""

    type: Required[Literal["CARD", "BANK", "CASH_APP"]]
    """The default payment method type"""


class Integration(TypedDict, total=False):
    """External billing or CRM integration link"""

    id: Required[str]
    """Integration details"""

    synced_entity_id: Required[Annotated[Optional[str], PropertyInfo(alias="syncedEntityId")]]
    """Synced entity id"""

    vendor_identifier: Required[
        Annotated[
            Literal[
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
            ],
            PropertyInfo(alias="vendorIdentifier"),
        ]
    ]
    """The vendor identifier of integration"""


class PassthroughStripeBillingAddress(TypedDict, total=False):
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


class PassthroughStripeShippingAddress(TypedDict, total=False):
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


class PassthroughStripeTaxID(TypedDict, total=False):
    """Tax identifier with type and value for customer tax exemptions."""

    type: Required[str]
    """The type of tax exemption identifier, such as VAT."""

    value: Required[str]
    """The actual tax identifier value"""


class PassthroughStripe(TypedDict, total=False):
    """Stripe-specific billing fields for the customer."""

    billing_address: Annotated[PassthroughStripeBillingAddress, PropertyInfo(alias="billingAddress")]
    """Physical address"""

    customer_name: Annotated[str, PropertyInfo(alias="customerName")]
    """Customer name"""

    invoice_custom_fields: Annotated[Dict[str, str], PropertyInfo(alias="invoiceCustomFields")]
    """Invoice custom fields"""

    metadata: Dict[str, str]
    """Additional metadata"""

    payment_method_id: Annotated[str, PropertyInfo(alias="paymentMethodId")]
    """Billing provider payment method id, attached to this customer"""

    shipping_address: Annotated[PassthroughStripeShippingAddress, PropertyInfo(alias="shippingAddress")]
    """Physical address"""

    tax_ids: Annotated[Iterable[PassthroughStripeTaxID], PropertyInfo(alias="taxIds")]
    """Tax IDs"""


class PassthroughZuoraBillingAddress(TypedDict, total=False):
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


class PassthroughZuora(TypedDict, total=False):
    """Zuora-specific billing fields for the customer."""

    billing_address: Annotated[PassthroughZuoraBillingAddress, PropertyInfo(alias="billingAddress")]
    """Physical address"""

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
    """Customers selected currency"""

    metadata: Dict[str, str]
    """Additional metadata"""

    payment_method_id: Annotated[str, PropertyInfo(alias="paymentMethodId")]
    """Billing provider payment method id, attached to this customer"""


class Passthrough(TypedDict, total=False):
    """Vendor-specific billing passthrough fields."""

    stripe: PassthroughStripe
    """Stripe-specific billing fields for the customer."""

    zuora: PassthroughZuora
    """Zuora-specific billing fields for the customer."""
