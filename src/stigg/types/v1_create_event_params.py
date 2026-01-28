# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["V1CreateEventParams", "Event"]


class V1CreateEventParams(TypedDict, total=False):
    events: Required[Iterable[Event]]
    """A list of usage events to report"""


class Event(TypedDict, total=False):
    """Raw usage event"""

    customer_id: Required[Annotated[str, PropertyInfo(alias="customerId")]]
    """Customer id"""

    event_name: Required[Annotated[str, PropertyInfo(alias="eventName")]]
    """The name of the usage event"""

    idempotency_key: Required[Annotated[str, PropertyInfo(alias="idempotencyKey")]]
    """Idempotency key"""

    dimensions: Dict[str, Union[str, float, bool]]
    """Dimensions associated with the usage event"""

    resource_id: Annotated[Optional[str], PropertyInfo(alias="resourceId")]
    """Resource id"""

    timestamp: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Timestamp"""
