# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["GrantListResponse", "Cost", "LatestInvoice"]


class Cost(BaseModel):
    """The monetary cost of the credit grant"""

    amount: float
    """The cost amount"""

    currency: str
    """The currency code"""


class LatestInvoice(BaseModel):
    """The latest invoice details for this grant"""

    billing_id: str = FieldInfo(alias="billingId")
    """The billing provider invoice ID"""

    billing_reason: Optional[Literal["MANUAL", "OTHER"]] = FieldInfo(alias="billingReason", default=None)
    """The billing reason for the invoice"""

    created_at: datetime = FieldInfo(alias="createdAt")
    """The invoice creation date"""

    currency: Optional[str] = None
    """The invoice currency"""

    due_date: Optional[datetime] = FieldInfo(alias="dueDate", default=None)
    """The invoice due date"""

    error_message: Optional[str] = FieldInfo(alias="errorMessage", default=None)
    """Error message if payment failed"""

    payment_url: Optional[str] = FieldInfo(alias="paymentUrl", default=None)
    """The payment URL for settling the invoice"""

    pdf_url: Optional[str] = FieldInfo(alias="pdfUrl", default=None)
    """The PDF URL of the invoice"""

    requires_action: bool = FieldInfo(alias="requiresAction")
    """Whether the invoice requires user action"""

    status: Literal["OPEN", "PAID", "CANCELED"]
    """The invoice status"""

    sub_total: Optional[float] = FieldInfo(alias="subTotal", default=None)
    """The subtotal amount before tax"""

    tax: Optional[float] = None
    """The tax amount"""

    total: Optional[float] = None
    """The total amount including tax"""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """The invoice last update date"""


class GrantListResponse(BaseModel):
    """Credit grant object representing allocated credits for a customer"""

    id: str
    """The unique readable identifier of the credit grant"""

    amount: float
    """The total credits granted"""

    comment: Optional[str] = None
    """An optional comment on the credit grant"""

    consumed_amount: float = FieldInfo(alias="consumedAmount")
    """The total credits consumed from this grant"""

    cost: Cost
    """The monetary cost of the credit grant"""

    created_at: datetime = FieldInfo(alias="createdAt")
    """Timestamp of when the record was created"""

    currency_id: str = FieldInfo(alias="currencyId")
    """The currency identifier for this grant"""

    customer_id: str = FieldInfo(alias="customerId")
    """The customer ID this grant belongs to"""

    display_name: str = FieldInfo(alias="displayName")
    """The display name of the credit grant"""

    effective_at: datetime = FieldInfo(alias="effectiveAt")
    """The date when the credit grant becomes effective"""

    expire_at: Optional[datetime] = FieldInfo(alias="expireAt", default=None)
    """The date when the credit grant expires"""

    grant_type: Literal["PAID", "PROMOTIONAL", "RECURRING"] = FieldInfo(alias="grantType")
    """The type of credit grant (PAID, PROMOTIONAL, RECURRING)"""

    invoice_id: Optional[str] = FieldInfo(alias="invoiceId", default=None)
    """The billing invoice ID associated with this grant"""

    latest_invoice: Optional[LatestInvoice] = FieldInfo(alias="latestInvoice", default=None)
    """The latest invoice details for this grant"""

    metadata: Dict[str, str]
    """Metadata associated with the entity"""

    payment_collection: Literal["NOT_REQUIRED", "PROCESSING", "FAILED", "ACTION_REQUIRED"] = FieldInfo(
        alias="paymentCollection"
    )
    """The payment collection status"""

    priority: float
    """The priority of the credit grant (lower number = higher priority)"""

    resource_id: Optional[str] = FieldInfo(alias="resourceId", default=None)
    """The resource ID this grant is scoped to"""

    source_type: Optional[Literal["PRICE", "PLAN_ENTITLEMENT", "ADDON_ENTITLEMENT"]] = FieldInfo(
        alias="sourceType", default=None
    )
    """The source type of the grant (PRICE, PLAN_ENTITLEMENT, ADDON_ENTITLEMENT)"""

    status: Literal["PAYMENT_PENDING", "ACTIVE", "EXPIRED", "VOIDED", "SCHEDULED"]
    """The effective status of the credit grant"""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """Timestamp of when the record was last updated"""

    voided_at: Optional[datetime] = FieldInfo(alias="voidedAt", default=None)
    """The date when the credit grant was voided"""
