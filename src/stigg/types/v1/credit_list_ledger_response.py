# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["CreditListLedgerResponse", "Breakdown"]


class Breakdown(BaseModel):
    amount: float
    """The amount of the ledger event.

    Reservation events carry their net effect on the balance: a reserve is negative,
    and so is a release that consumed more than was held
    """

    credit_currency_id: str = FieldInfo(alias="creditCurrencyId")
    """The credit currency ID"""

    credit_grant_id: str = FieldInfo(alias="creditGrantId")
    """The credit grant ID associated with this event"""

    customer_id: str = FieldInfo(alias="customerId")
    """The customer ID this event belongs to"""

    event_id: Optional[str] = FieldInfo(alias="eventId", default=None)
    """The unique event identifier"""

    event_type: Literal[
        "CREDITS_GRANTED",
        "CREDITS_EXPIRED",
        "CREDITS_CONSUMED",
        "CREDITS_VOIDED",
        "CREDITS_UPDATED",
        "CREDITS_CONSUMPTION_TRANSFER_SOURCE",
        "CREDITS_CONSUMPTION_TRANSFER_TARGET",
        "CREDITS_RESERVED",
        "CREDITS_RESERVATION_RELEASED",
        "CREDITS_RESERVATION_EXPIRED",
    ] = FieldInfo(alias="eventType")
    """The type of credit event"""

    feature_id: Optional[str] = FieldInfo(alias="featureId", default=None)
    """The feature ID associated with this event"""

    reservation_id: Optional[str] = FieldInfo(alias="reservationId", default=None)
    """The credit reservation this event belongs to"""

    resource_id: Optional[str] = FieldInfo(alias="resourceId", default=None)
    """The resource ID this event is scoped to"""

    timestamp: datetime
    """The timestamp when the event occurred"""


class CreditListLedgerResponse(BaseModel):
    """A credit ledger event representing a change to credit balance"""

    amount: float
    """The amount of the ledger event.

    Reservation events carry their net effect on the balance: a reserve is negative,
    and so is a release that consumed more than was held
    """

    breakdown: Optional[List[Breakdown]] = None
    """On a released reservation, the credits consumed from each grant"""

    credit_currency_id: str = FieldInfo(alias="creditCurrencyId")
    """The credit currency ID"""

    credit_grant_id: str = FieldInfo(alias="creditGrantId")
    """The credit grant ID associated with this event"""

    customer_id: str = FieldInfo(alias="customerId")
    """The customer ID this event belongs to"""

    event_id: Optional[str] = FieldInfo(alias="eventId", default=None)
    """The unique event identifier"""

    event_type: Literal[
        "CREDITS_GRANTED",
        "CREDITS_EXPIRED",
        "CREDITS_CONSUMED",
        "CREDITS_VOIDED",
        "CREDITS_UPDATED",
        "CREDITS_CONSUMPTION_TRANSFER_SOURCE",
        "CREDITS_CONSUMPTION_TRANSFER_TARGET",
        "CREDITS_RESERVED",
        "CREDITS_RESERVATION_RELEASED",
        "CREDITS_RESERVATION_EXPIRED",
    ] = FieldInfo(alias="eventType")
    """The type of credit event"""

    feature_id: Optional[str] = FieldInfo(alias="featureId", default=None)
    """The feature ID associated with this event"""

    hold_returned_amount: Optional[float] = FieldInfo(alias="holdReturnedAmount", default=None)
    """
    On a released reservation, the held amount returned to the balance before
    consumed credits are deducted
    """

    metadata: Optional[Dict[str, str]] = None
    """The metadata sent with the credit reservation"""

    reservation_id: Optional[str] = FieldInfo(alias="reservationId", default=None)
    """The credit reservation this event belongs to"""

    resource_id: Optional[str] = FieldInfo(alias="resourceId", default=None)
    """The resource ID this event is scoped to"""

    timestamp: datetime
    """The timestamp when the event occurred"""
