# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "ContractCreateResponse",
    "Data",
    "DataLatestInvoice",
    "DataNextInvoice",
    "DataNextInvoiceAmount",
    "DataSubscription",
]


class DataLatestInvoice(BaseModel):
    """
    The most recent non-draft invoice for this contract (open, paid, or canceled), or null when none exists
    """

    billing_id: str = FieldInfo(alias="billingId")
    """Invoice billing ID"""

    created_at: datetime = FieldInfo(alias="createdAt")
    """Invoice creation date"""

    requires_action: bool = FieldInfo(alias="requiresAction")
    """Whether payment requires action"""

    status: Literal["OPEN", "CANCELED", "PAID"]
    """Invoice status"""

    amount_due: Optional[float] = FieldInfo(alias="amountDue", default=None)
    """Amount due"""

    billing_reason: Optional[
        Literal[
            "BILLING_CYCLE",
            "SUBSCRIPTION_CREATION",
            "SUBSCRIPTION_UPDATE",
            "MANUAL",
            "MINIMUM_INVOICE_AMOUNT_EXCEEDED",
            "OTHER",
        ]
    ] = FieldInfo(alias="billingReason", default=None)
    """Billing reason"""

    currency: Optional[str] = None
    """Invoice currency"""

    pdf_url: Optional[str] = FieldInfo(alias="pdfUrl", default=None)
    """Invoice PDF URL"""

    total: Optional[float] = None
    """Total amount"""


class DataNextInvoiceAmount(BaseModel):
    """The total amount of the upcoming invoice"""

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
    """ISO 4217 currency code"""


class DataNextInvoice(BaseModel):
    """A preview of the contract's upcoming invoice, or null when none is available"""

    amount: DataNextInvoiceAmount
    """The total amount of the upcoming invoice"""

    due_date: Optional[datetime] = FieldInfo(alias="dueDate", default=None)
    """The date the upcoming invoice is due"""

    period_end: Optional[datetime] = FieldInfo(alias="periodEnd", default=None)
    """The end of the billing period the upcoming invoice covers"""

    period_start: Optional[datetime] = FieldInfo(alias="periodStart", default=None)
    """The start of the billing period the upcoming invoice covers"""


class DataSubscription(BaseModel):
    """A custom subscription attached to a contract."""

    plan_display_name: Optional[str] = FieldInfo(alias="planDisplayName", default=None)
    """Display name of the subscription plan"""

    product_display_name: Optional[str] = FieldInfo(alias="productDisplayName", default=None)
    """Display name of the product the subscription plan belongs to"""

    subscription_id: str = FieldInfo(alias="subscriptionId")
    """The subscription ref ID (use it to deep-link to the subscription)"""


class Data(BaseModel):
    """A billing contract as reported by the connected billing provider."""

    id: Optional[str] = None
    """
    The persisted Stigg contract id (matches a subscription’s contractId; present
    for Stigg-managed contracts)
    """

    activation_end_date: Optional[datetime] = FieldInfo(alias="activationEndDate", default=None)
    """The date the contract activation ends"""

    activation_start_date: Optional[datetime] = FieldInfo(alias="activationStartDate", default=None)
    """The date the contract becomes active"""

    billing_id: Optional[str] = FieldInfo(alias="billingId", default=None)
    """
    The billing provider (Received) contract ID; null until the contract has synced
    to the billing provider
    """

    contract_id: str = FieldInfo(alias="contractId")
    """The Stigg contract ref ID (the key used to fetch/update/delete this contract)"""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """The date the contract was created"""

    customer_external_id: Optional[str] = FieldInfo(alias="customerExternalId", default=None)
    """The external identifier of the customer the contract belongs to"""

    external_id: str = FieldInfo(alias="externalId")
    """The external identifier of the contract"""

    latest_invoice: Optional[DataLatestInvoice] = FieldInfo(alias="latestInvoice", default=None)
    """
    The most recent non-draft invoice for this contract (open, paid, or canceled),
    or null when none exists
    """

    name: Optional[str] = None
    """
    The contract name (the purchase-order number when set, otherwise the
    contract/customer name)
    """

    next_invoice: Optional[DataNextInvoice] = FieldInfo(alias="nextInvoice", default=None)
    """A preview of the contract's upcoming invoice, or null when none is available"""

    po_number: Optional[str] = FieldInfo(alias="poNumber", default=None)
    """Purchase-order number, when set on the contract"""

    ref_id: Optional[str] = FieldInfo(alias="refId", default=None)
    """
    The Stigg contract ref ID (present for Stigg-managed contracts; the key used to
    update/delete)
    """

    state: Literal["DRAFT", "ACTIVE", "CANCELED", "END_BILLING"]
    """The current state of the contract"""

    subscriptions: List[DataSubscription]
    """The custom subscriptions attached to this contract (empty when none)"""


class ContractCreateResponse(BaseModel):
    """Response object"""

    data: Data
    """A billing contract as reported by the connected billing provider."""
