# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["CustomerCheckEntitlementParams"]


class CustomerCheckEntitlementParams(TypedDict, total=False):
    currency_id: Annotated[str, PropertyInfo(alias="currencyId")]
    """Currency ID (refId) to check for credit entitlements.

    Mutually exclusive with `featureId`.
    """

    feature_id: Annotated[str, PropertyInfo(alias="featureId")]
    """Feature ID (refId) to check. Mutually exclusive with `currencyId`."""

    requested_usage: Annotated[int, PropertyInfo(alias="requestedUsage")]
    """
    Requested usage amount to evaluate against the entitlement limit (numeric
    features only)
    """

    requested_values: Annotated[SequenceNotStr[str], PropertyInfo(alias="requestedValues")]
    """Requested values to evaluate against allowed values (enum features only)"""

    reservation_expires_at: Annotated[
        Union[str, datetime], PropertyInfo(alias="reservationExpiresAt", format="iso8601")
    ]
    """When the reservation expires (ISO 8601, at most 24 hours ahead).

    Mutually exclusive with `reservationTtlSeconds`.
    """

    reservation_id: Annotated[str, PropertyInfo(alias="reservationId")]
    """Client-provided reservation ID, required with `reserveAmount`.

    Retry with the same ID to get the same result; reuse with different parameters
    is a conflict.
    """

    reservation_metadata: Annotated[str, PropertyInfo(alias="reservationMetadata")]
    """JSON-encoded object of string values to attach to the reservation."""

    reservation_ttl_seconds: Annotated[int, PropertyInfo(alias="reservationTtlSeconds")]
    """How long the reservation holds the credits, in seconds (1–86400, default 3600).

    Mutually exclusive with `reservationExpiresAt`.
    """

    reserve_amount: Annotated[float, PropertyInfo(alias="reserveAmount")]
    """Credits to reserve (credit entitlements only).

    The check is decided and the credits held atomically; `requestedUsage` is
    ignored.
    """

    resource_id: Annotated[str, PropertyInfo(alias="resourceId")]
    """Resource ID to scope the entitlement check to a specific resource"""

    x_account_id: Annotated[str, PropertyInfo(alias="X-ACCOUNT-ID")]

    x_environment_id: Annotated[str, PropertyInfo(alias="X-ENVIRONMENT-ID")]
