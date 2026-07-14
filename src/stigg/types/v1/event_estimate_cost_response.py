# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["EventEstimateCostResponse", "Data", "DataEstimate", "DataEstimateBreakdown"]


class DataEstimateBreakdown(BaseModel):
    cost: float
    """The estimated credit cost contributed by this feature"""

    feature_id: str = FieldInfo(alias="featureId")
    """The feature whose meter contributed this cost"""

    warning_code: Optional[Literal["UNSUPPORTED_AGGREGATION"]] = FieldInfo(alias="warningCode", default=None)
    """Warning explaining why this cost may be inaccurate, if any"""


class DataEstimate(BaseModel):
    balance_after_estimate: float = FieldInfo(alias="balanceAfterEstimate")
    """The credit balance after subtracting the estimated cost"""

    breakdown: List[DataEstimateBreakdown]
    """Estimated cost contribution per feature"""

    currency_id: str = FieldInfo(alias="currencyId")
    """The credit currency identifier"""

    current_balance: float = FieldInfo(alias="currentBalance")
    """The current credit balance, including not-yet-reconciled consumption"""

    estimated_cost: float = FieldInfo(alias="estimatedCost")
    """The estimated credit cost of the reported event or usage"""

    would_overdraft: bool = FieldInfo(alias="wouldOverdraft")
    """Whether the estimated consumption would bring the balance below zero"""


class Data(BaseModel):
    """Estimated credit cost, current balance and balance after"""

    estimates: List[DataEstimate]
    """Per-currency cost estimates"""

    warnings: List[Literal["RESOURCE_SCOPED_SUBSCRIPTION_EXISTS", "FEATURE_NOT_FOUND", "FEATURE_NOT_CREDIT_BASED"]]
    """Request-level warnings about the estimation context"""


class EventEstimateCostResponse(BaseModel):
    """Response object"""

    data: Data
    """Estimated credit cost, current balance and balance after"""
