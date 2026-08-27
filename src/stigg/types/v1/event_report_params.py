# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["EventReportParams", "Event"]


class EventReportParams(TypedDict, total=False):
    events: Required[Iterable[Event]]
    """A list of usage events to report"""

    x_account_id: Annotated[str, PropertyInfo(alias="X-ACCOUNT-ID")]

    x_environment_id: Annotated[str, PropertyInfo(alias="X-ENVIRONMENT-ID")]


class Event(TypedDict, total=False):
    """Raw usage event"""

    customer_id: Required[Annotated[str, PropertyInfo(alias="customerId")]]
    """Customer id"""

    event_name: Required[Annotated[str, PropertyInfo(alias="eventName")]]
    """The name of the usage event"""

    idempotency_key: Required[Annotated[str, PropertyInfo(alias="idempotencyKey")]]
    """
    A key you provide to safely retry the same usage report without double-counting
    it. Reports with a previously-seen idempotency key are deduplicated for 7 days;
    after that window a retry is treated as new usage.
    """

    dimensions: Dict[str, Union[str, float, bool]]
    """Dimensions associated with the usage event"""

    resource_id: Annotated[Optional[str], PropertyInfo(alias="resourceId")]
    """The customer resource this usage applies to.

    Optional — only required if the customer has multiple resources (for example,
    one subscription per workspace or site) and usage needs to be tracked separately
    per resource; omit it to report usage at the customer level.
    """

    timestamp: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Timestamp"""
