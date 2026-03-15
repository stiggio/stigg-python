# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["CustomerListResponse", "DefaultPaymentMethod", "Integration"]


class DefaultPaymentMethod(BaseModel):
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


class Integration(BaseModel):
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


class CustomerListResponse(BaseModel):
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

    coupon_id: Optional[str] = FieldInfo(alias="couponId", default=None)
    """Customer level coupon"""

    default_payment_method: Optional[DefaultPaymentMethod] = FieldInfo(alias="defaultPaymentMethod", default=None)
    """The default payment method details"""

    email: Optional[str] = None
    """The email of the customer"""

    integrations: Optional[List[Integration]] = None
    """List of integrations"""

    metadata: Optional[Dict[str, str]] = None
    """Additional metadata"""

    name: Optional[str] = None
    """The name of the customer"""
