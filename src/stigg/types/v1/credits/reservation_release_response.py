# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["ReservationReleaseResponse", "Data", "DataCredit", "DataReservation"]


class DataCredit(BaseModel):
    """The optimistic credit balance after the release"""

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


class DataReservation(BaseModel):
    """The released reservation"""

    id: str
    """The client-provided reservation ID."""

    amount: float
    """The amount of credits held."""

    consumed_amount: Optional[float] = FieldInfo(alias="consumedAmount", default=None)
    """The amount consumed at release"""

    expires_at: datetime = FieldInfo(alias="expiresAt")
    """When the reservation expires.

    Unreleased credits return to the balance at this time.
    """

    status: Literal["ACTIVE", "RELEASED"]
    """The status of the reservation."""


class Data(BaseModel):
    """Result of releasing a credit reservation"""

    credit: Optional[DataCredit] = None
    """The optimistic credit balance after the release"""

    reservation: DataReservation
    """The released reservation"""


class ReservationReleaseResponse(BaseModel):
    """Response object"""

    data: Data
    """Result of releasing a credit reservation"""
