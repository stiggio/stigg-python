# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["GrantCreateParams", "BillingInformation", "BillingInformationBillingAddress", "Cost"]


class GrantCreateParams(TypedDict, total=False):
    amount: Required[float]
    """The credit amount to grant"""

    currency_id: Required[Annotated[str, PropertyInfo(alias="currencyId")]]
    """The credit currency ID (required)"""

    customer_id: Required[Annotated[str, PropertyInfo(alias="customerId")]]
    """The customer ID to grant credits to (required)"""

    display_name: Required[Annotated[str, PropertyInfo(alias="displayName")]]
    """The display name for the credit grant"""

    grant_type: Required[Annotated[Literal["PAID", "PROMOTIONAL", "RECURRING"], PropertyInfo(alias="grantType")]]
    """The type of credit grant (PAID, PROMOTIONAL, RECURRING)"""

    await_payment_confirmation: Annotated[bool, PropertyInfo(alias="awaitPaymentConfirmation")]
    """Whether to wait for payment confirmation before returning (default: true)"""

    billing_information: Annotated[BillingInformation, PropertyInfo(alias="billingInformation")]
    """Billing information for the credit grant"""

    comment: str
    """An optional comment on the credit grant"""

    cost: Cost
    """The monetary cost of the credit grant"""

    effective_at: Annotated[Union[str, datetime], PropertyInfo(alias="effectiveAt", format="iso8601")]
    """The date when the credit grant becomes effective"""

    expire_at: Annotated[Union[str, datetime], PropertyInfo(alias="expireAt", format="iso8601")]
    """The date when the credit grant expires"""

    metadata: Dict[str, str]
    """Additional metadata for the credit grant"""

    payment_collection_method: Annotated[
        Literal["CHARGE", "INVOICE", "NONE"], PropertyInfo(alias="paymentCollectionMethod")
    ]
    """The payment collection method (CHARGE, INVOICE, NONE)"""

    priority: int
    """The priority of the credit grant (lower number = higher priority)"""

    resource_id: Annotated[str, PropertyInfo(alias="resourceId")]
    """The resource ID to scope the grant to"""


class BillingInformationBillingAddress(TypedDict, total=False):
    """The billing address"""

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


class BillingInformation(TypedDict, total=False):
    """Billing information for the credit grant"""

    billing_address: Annotated[BillingInformationBillingAddress, PropertyInfo(alias="billingAddress")]
    """The billing address"""

    invoice_days_until_due: Annotated[float, PropertyInfo(alias="invoiceDaysUntilDue")]
    """Days until the invoice is due"""

    is_invoice_paid: Annotated[bool, PropertyInfo(alias="isInvoicePaid")]
    """Whether the invoice is already paid"""


class Cost(TypedDict, total=False):
    """The monetary cost of the credit grant"""

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
