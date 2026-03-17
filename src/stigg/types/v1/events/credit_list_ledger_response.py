# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["CreditListLedgerResponse"]


class CreditListLedgerResponse(BaseModel):
    """A credit ledger event representing a change to credit balance"""

    amount: float
    """The credit amount for this event"""

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
    ] = FieldInfo(alias="eventType")
    """The type of credit event"""

    feature_id: Optional[str] = FieldInfo(alias="featureId", default=None)
    """The feature ID associated with this event"""

    resource_id: Optional[str] = FieldInfo(alias="resourceId", default=None)
    """The resource ID this event is scoped to"""

    timestamp: datetime
    """The timestamp when the event occurred"""
