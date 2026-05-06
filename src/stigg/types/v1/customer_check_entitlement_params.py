# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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

    resource_id: Annotated[str, PropertyInfo(alias="resourceId")]
    """Resource ID to scope the entitlement check to a specific resource"""
