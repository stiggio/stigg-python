# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["CustomerListInvoicesResponse", "LineItem"]


class LineItem(BaseModel):
    """A single line item on an invoice."""

    amount: Optional[float] = None
    """Total amount for this line (unit price × quantity)"""

    description: Optional[str] = None
    """Human-readable description of the line item"""

    product_external_id: Optional[str] = FieldInfo(alias="productExternalId", default=None)
    """External ID of the product this line item relates to, when one is mapped"""

    quantity: Optional[float] = None
    """Quantity billed on this line"""

    unit_price: Optional[float] = FieldInfo(alias="unitPrice", default=None)
    """Price per unit for this line"""


class CustomerListInvoicesResponse(BaseModel):
    """A customer invoice as reported by the connected billing provider."""

    contract_external_id: Optional[str] = FieldInfo(alias="contractExternalId", default=None)
    """
    External ID of the contract the invoice belongs to: your contract ref when
    mapped, otherwise the Received contract ID
    """

    currency: Optional[str] = None
    """The ISO-4217 currency code of the invoice"""

    customer_external_id: Optional[str] = FieldInfo(alias="customerExternalId", default=None)
    """
    External ID of the customer the invoice belongs to: your customer ref when
    mapped, otherwise the Received customer ID
    """

    discount: Optional[float] = None
    """The total discount amount"""

    due_date: Optional[datetime] = FieldInfo(alias="dueDate", default=None)
    """The date payment is due"""

    invoice_external_id: Optional[str] = FieldInfo(alias="invoiceExternalId", default=None)
    """
    External ID for the invoice: the mapped external ID when one exists, otherwise
    the invoice ID
    """

    invoice_id: str = FieldInfo(alias="invoiceId")
    """The billing provider (Received) invoice ID"""

    invoice_number: Optional[str] = FieldInfo(alias="invoiceNumber", default=None)
    """The invoice document number (or draft number while the invoice is unissued)"""

    issue_date: Optional[datetime] = FieldInfo(alias="issueDate", default=None)
    """The date the invoice was issued"""

    line_items: List[LineItem] = FieldInfo(alias="lineItems")
    """The invoice line items"""

    paid_date: Optional[datetime] = FieldInfo(alias="paidDate", default=None)
    """The date the invoice was reconciled as paid; present once reconciled"""

    state: Literal["OPEN", "CANCELED", "PAID"]
    """The invoice status (open, paid, or canceled)"""

    subtotal: Optional[float] = None
    """The pre-tax subtotal"""

    tax: Optional[float] = None
    """The total tax amount"""

    total: Optional[float] = None
    """The total amount due"""
