# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SubscriptionCancelParams"]


class SubscriptionCancelParams(TypedDict, total=False):
    cancellation_action: Annotated[Literal["DEFAULT", "REVOKE_ENTITLEMENTS"], PropertyInfo(alias="cancellationAction")]
    """Action on cancellation (downgrade or revoke)"""

    cancellation_time: Annotated[
        Literal["END_OF_BILLING_PERIOD", "IMMEDIATE", "SPECIFIC_DATE"], PropertyInfo(alias="cancellationTime")
    ]
    """When to cancel (immediate, period end, or date)"""

    end_date: Annotated[Union[str, datetime], PropertyInfo(alias="endDate", format="iso8601")]
    """Subscription end date"""

    prorate: bool
    """If set, enables or disables prorating of credits on subscription cancellation."""
