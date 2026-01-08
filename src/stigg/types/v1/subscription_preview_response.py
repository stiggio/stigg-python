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
    end: datetime
    """Billing period end date"""

    start: datetime
    """Billing period start date"""


class DataImmediateInvoiceDiscountDetails(BaseModel):
    code: Optional[str] = None

    fixed_amount: Optional[float] = FieldInfo(alias="fixedAmount", default=None)

    percentage: Optional[float] = None


class DataImmediateInvoiceDiscount(BaseModel):
    amount: float

    currency: str

    description: str


class DataImmediateInvoiceLine(BaseModel):
    currency: str

    description: str

    sub_total: float = FieldInfo(alias="subTotal")

    unit_price: float = FieldInfo(alias="unitPrice")

    quantity: Optional[float] = None


class DataImmediateInvoice(BaseModel):
    sub_total: float = FieldInfo(alias="subTotal")

    total: float

    billing_period_range: Optional[DataImmediateInvoiceBillingPeriodRange] = FieldInfo(
        alias="billingPeriodRange", default=None
    )

    currency: Optional[str] = None

    discount: Optional[float] = None

    discount_details: Optional[DataImmediateInvoiceDiscountDetails] = FieldInfo(alias="discountDetails", default=None)

    discounts: Optional[List[DataImmediateInvoiceDiscount]] = None

    lines: Optional[List[DataImmediateInvoiceLine]] = None

    tax: Optional[float] = None


class DataBillingPeriodRange(BaseModel):
    end: Optional[datetime] = None
    """Billing period end date"""

    start: Optional[datetime] = None
    """Billing period start date"""


class DataFreeItem(BaseModel):
    addon_id: str = FieldInfo(alias="addonId")

    quantity: float


class DataRecurringInvoiceBillingPeriodRange(BaseModel):
    end: datetime
    """Billing period end date"""

    start: datetime
    """Billing period start date"""


class DataRecurringInvoiceDiscountDetails(BaseModel):
    code: Optional[str] = None

    fixed_amount: Optional[float] = FieldInfo(alias="fixedAmount", default=None)

    percentage: Optional[float] = None


class DataRecurringInvoiceDiscount(BaseModel):
    amount: float

    currency: str

    description: str


class DataRecurringInvoiceLine(BaseModel):
    currency: str

    description: str

    sub_total: float = FieldInfo(alias="subTotal")

    unit_price: float = FieldInfo(alias="unitPrice")

    quantity: Optional[float] = None


class DataRecurringInvoice(BaseModel):
    sub_total: float = FieldInfo(alias="subTotal")

    total: float

    billing_period_range: Optional[DataRecurringInvoiceBillingPeriodRange] = FieldInfo(
        alias="billingPeriodRange", default=None
    )

    currency: Optional[str] = None

    discount: Optional[float] = None

    discount_details: Optional[DataRecurringInvoiceDiscountDetails] = FieldInfo(alias="discountDetails", default=None)

    discounts: Optional[List[DataRecurringInvoiceDiscount]] = None

    lines: Optional[List[DataRecurringInvoiceLine]] = None

    tax: Optional[float] = None


class Data(BaseModel):
    immediate_invoice: DataImmediateInvoice = FieldInfo(alias="immediateInvoice")

    billing_period_range: Optional[DataBillingPeriodRange] = FieldInfo(alias="billingPeriodRange", default=None)

    free_items: Optional[List[DataFreeItem]] = FieldInfo(alias="freeItems", default=None)

    has_scheduled_updates: Optional[bool] = FieldInfo(alias="hasScheduledUpdates", default=None)

    is_plan_downgrade: Optional[bool] = FieldInfo(alias="isPlanDowngrade", default=None)

    recurring_invoice: Optional[DataRecurringInvoice] = FieldInfo(alias="recurringInvoice", default=None)


class SubscriptionPreviewResponse(BaseModel):
    data: Data
