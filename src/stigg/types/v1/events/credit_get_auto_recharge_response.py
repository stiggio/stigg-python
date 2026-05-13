# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["CreditGetAutoRechargeResponse", "Data"]


class Data(BaseModel):
    """Automatic recharge configuration for a customer and currency"""

    id: Optional[str] = None
    """The unique configuration ID"""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """Timestamp of when the record was created"""

    currency_id: str = FieldInfo(alias="currencyId")
    """The currency ID for this configuration"""

    customer_id: str = FieldInfo(alias="customerId")
    """The customer ID this configuration belongs to"""

    grant_expiration_period: Literal["1_MONTH", "1_YEAR"] = FieldInfo(alias="grantExpirationPeriod")
    """Expiration period for auto-recharge grants (1_MONTH or 1_YEAR)"""

    is_enabled: bool = FieldInfo(alias="isEnabled")
    """Whether automatic recharge is enabled"""

    max_spend_limit: Optional[float] = FieldInfo(alias="maxSpendLimit", default=None)
    """Maximum monthly spend limit for automatic recharges"""

    target_balance: float = FieldInfo(alias="targetBalance")
    """The target credit balance to recharge to"""

    threshold_type: Literal["CREDIT_AMOUNT", "DOLLAR_AMOUNT"] = FieldInfo(alias="thresholdType")
    """The threshold type (CREDIT_AMOUNT or DOLLAR_AMOUNT)"""

    threshold_value: float = FieldInfo(alias="thresholdValue")
    """The threshold value that triggers a recharge"""

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """Timestamp of when the record was last updated"""


class CreditGetAutoRechargeResponse(BaseModel):
    """Response object"""

    data: Data
    """Automatic recharge configuration for a customer and currency"""
