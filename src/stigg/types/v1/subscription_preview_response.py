# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "SubscriptionPreviewResponse",
    "Data",
    "DataImmediateInvoice",
    "DataImmediateInvoiceBillingPeriodRange",
    "DataImmediateInvoiceDiscountDetails",
    "DataImmediateInvoiceDiscount",
    "DataImmediateInvoiceLine",
    "DataBillingPeriodRange",
    "DataFreeItem",
    "DataRecurringInvoice",
    "DataRecurringInvoiceBillingPeriodRange",
    "DataRecurringInvoiceDiscountDetails",
    "DataRecurringInvoiceDiscount",
    "DataRecurringInvoiceLine",
]


class DataImmediateInvoiceBillingPeriodRange(BaseModel):
    """Billing period covered"""

    end: datetime
    """Billing period end date"""

    start: datetime
    """Billing period start date"""


class DataImmediateInvoiceDiscountDetails(BaseModel):
    """Discount breakdown"""

    code: Optional[str] = None
    """Promo code used"""

    fixed_amount: Optional[float] = FieldInfo(alias="fixedAmount", default=None)
    """Fixed discount amount"""

    percentage: Optional[float] = None
    """Percentage discount"""


class DataImmediateInvoiceDiscount(BaseModel):
    """Applied discount amount"""

    amount: float
    """Discount amount"""

    currency: str
    """Currency code"""

    description: str
    """Discount description"""


class DataImmediateInvoiceLine(BaseModel):
    """Invoice line item"""

    currency: str
    """Currency code"""

    description: str
    """Line item description"""

    sub_total: float = FieldInfo(alias="subTotal")
    """Line subtotal"""

    unit_price: float = FieldInfo(alias="unitPrice")
    """Price per unit"""

    quantity: Optional[float] = None
    """Quantity"""


class DataImmediateInvoice(BaseModel):
    """Invoice due immediately"""

    sub_total: float = FieldInfo(alias="subTotal")
    """Subtotal before discounts"""

    total: float
    """Invoice total"""

    billing_period_range: Optional[DataImmediateInvoiceBillingPeriodRange] = FieldInfo(
        alias="billingPeriodRange", default=None
    )
    """Billing period covered"""

    currency: Optional[str] = None
    """Currency code"""

    discount: Optional[float] = None
    """Total discount amount"""

    discount_details: Optional[DataImmediateInvoiceDiscountDetails] = FieldInfo(alias="discountDetails", default=None)
    """Discount breakdown"""

    discounts: Optional[List[DataImmediateInvoiceDiscount]] = None
    """Applied discounts"""

    lines: Optional[List[DataImmediateInvoiceLine]] = None
    """Line items"""

    tax: Optional[float] = None
    """Tax amount"""


class DataBillingPeriodRange(BaseModel):
    """Billing period range"""

    end: Optional[datetime] = None
    """Billing period end date"""

    start: Optional[datetime] = None
    """Billing period start date"""


class DataFreeItem(BaseModel):
    """Free item in subscription"""

    addon_id: str = FieldInfo(alias="addonId")
    """Addon ID"""

    quantity: float
    """Quantity"""


class DataRecurringInvoiceBillingPeriodRange(BaseModel):
    """Billing period covered"""

    end: datetime
    """Billing period end date"""

    start: datetime
    """Billing period start date"""


class DataRecurringInvoiceDiscountDetails(BaseModel):
    """Discount breakdown"""

    code: Optional[str] = None
    """Promo code used"""

    fixed_amount: Optional[float] = FieldInfo(alias="fixedAmount", default=None)
    """Fixed discount amount"""

    percentage: Optional[float] = None
    """Percentage discount"""


class DataRecurringInvoiceDiscount(BaseModel):
    """Applied discount amount"""

    amount: float
    """Discount amount"""

    currency: str
    """Currency code"""

    description: str
    """Discount description"""


class DataRecurringInvoiceLine(BaseModel):
    """Invoice line item"""

    currency: str
    """Currency code"""

    description: str
    """Line item description"""

    sub_total: float = FieldInfo(alias="subTotal")
    """Line subtotal"""

    unit_price: float = FieldInfo(alias="unitPrice")
    """Price per unit"""

    quantity: Optional[float] = None
    """Quantity"""


class DataRecurringInvoice(BaseModel):
    """Recurring invoice preview"""

    sub_total: float = FieldInfo(alias="subTotal")
    """Subtotal before discounts"""

    total: float
    """Invoice total"""

    billing_period_range: Optional[DataRecurringInvoiceBillingPeriodRange] = FieldInfo(
        alias="billingPeriodRange", default=None
    )
    """Billing period covered"""

    currency: Optional[str] = None
    """Currency code"""

    discount: Optional[float] = None
    """Total discount amount"""

    discount_details: Optional[DataRecurringInvoiceDiscountDetails] = FieldInfo(alias="discountDetails", default=None)
    """Discount breakdown"""

    discounts: Optional[List[DataRecurringInvoiceDiscount]] = None
    """Applied discounts"""

    lines: Optional[List[DataRecurringInvoiceLine]] = None
    """Line items"""

    tax: Optional[float] = None
    """Tax amount"""


class Data(BaseModel):
    """Pricing preview with invoices"""

    immediate_invoice: DataImmediateInvoice = FieldInfo(alias="immediateInvoice")
    """Invoice due immediately"""

    billing_period_range: Optional[DataBillingPeriodRange] = FieldInfo(alias="billingPeriodRange", default=None)
    """Billing period range"""

    free_items: Optional[List[DataFreeItem]] = FieldInfo(alias="freeItems", default=None)
    """Free items included"""

    has_scheduled_updates: Optional[bool] = FieldInfo(alias="hasScheduledUpdates", default=None)
    """Whether updates are scheduled"""

    is_plan_downgrade: Optional[bool] = FieldInfo(alias="isPlanDowngrade", default=None)
    """Whether this is a downgrade"""

    recurring_invoice: Optional[DataRecurringInvoice] = FieldInfo(alias="recurringInvoice", default=None)
    """Recurring invoice preview"""


class SubscriptionPreviewResponse(BaseModel):
    """Response object"""

    data: Data
    """Pricing preview with invoices"""
