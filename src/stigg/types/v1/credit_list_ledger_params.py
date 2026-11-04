# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["CreditListLedgerParams"]


class CreditListLedgerParams(TypedDict, total=False):
    customer_id: Required[Annotated[str, PropertyInfo(alias="customerId")]]
    """Filter by customer ID (required)"""

    after: str
    """Return items that come after this cursor"""

    before: str
    """Return items that come before this cursor"""

    currency_id: Annotated[str, PropertyInfo(alias="currencyId")]
    """Filter by currency ID"""

    end_date: Annotated[Union[str, datetime], PropertyInfo(alias="endDate", format="iso8601")]
    """Filter to events with a timestamp on or before this date, inclusive (ISO 8601)"""

    event_type: Annotated[str, PropertyInfo(alias="eventType")]
    """Filter by event type(s), comma-separated"""

    limit: int
    """Maximum number of items to return"""

    reservation_id: Annotated[str, PropertyInfo(alias="reservationId")]
    """Filter by credit reservation ID"""

    resource_id: Annotated[str, PropertyInfo(alias="resourceId")]
    """Filter by resource ID"""

    start_date: Annotated[Union[str, datetime], PropertyInfo(alias="startDate", format="iso8601")]
    """Filter to events with a timestamp on or after this date, inclusive (ISO 8601)"""

    x_account_id: Annotated[str, PropertyInfo(alias="X-ACCOUNT-ID")]

    x_environment_id: Annotated[str, PropertyInfo(alias="X-ENVIRONMENT-ID")]
