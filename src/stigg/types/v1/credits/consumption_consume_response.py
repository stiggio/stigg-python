# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["ConsumptionConsumeResponse", "Data", "DataCredit"]


class DataCredit(BaseModel):
    """
    The optimistic credit balance after consumption (when sync credit consumption is enabled)
    """

    currency_id: str = FieldInfo(alias="currencyId")
    """The credit currency identifier"""

    current_usage: float = FieldInfo(alias="currentUsage")
    """
    The wallet's total consumed credits for this currency (optimistic — includes
    not-yet-reconciled usage), shared across every feature that draws on the
    currency. This is the running balance, not this call's deduction — see
    `consumed` for that.
    """

    timestamp: datetime
    """
    The grant-version timestamp of this balance, used by the SDK for last-write-wins
    reconciliation
    """

    usage_limit: float = FieldInfo(alias="usageLimit")
    """The total credits granted"""

    usage_period_end: Optional[datetime] = FieldInfo(alias="usagePeriodEnd", default=None)
    """
    End of the current credit grant period (when recurring credits reset), if
    applicable
    """


class Data(BaseModel):
    """Result of a synchronous direct credit consumption"""

    amount: float
    """The amount of credits consumed"""

    currency_id: str = FieldInfo(alias="currencyId")
    """The credit currency the credits were consumed from"""

    customer_id: str = FieldInfo(alias="customerId")
    """The customer the credits were consumed from"""

    timestamp: datetime
    """The timestamp the consumption was attributed to"""

    credit: Optional[DataCredit] = None
    """
    The optimistic credit balance after consumption (when sync credit consumption is
    enabled)
    """

    resource_id: Optional[str] = FieldInfo(alias="resourceId", default=None)
    """The resource the consumption was attributed to"""


class ConsumptionConsumeResponse(BaseModel):
    """Response object"""

    data: Data
    """Result of a synchronous direct credit consumption"""
