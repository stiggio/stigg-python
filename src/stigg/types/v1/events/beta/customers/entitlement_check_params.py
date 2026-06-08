# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Annotated, TypedDict

from ......_types import SequenceNotStr
from ......_utils import PropertyInfo

__all__ = ["EntitlementCheckParams"]


class EntitlementCheckParams(TypedDict, total=False):
    currency_id: Annotated[str, PropertyInfo(alias="currencyId")]
    """Currency ID (refId) to check for credit entitlements.

    Mutually exclusive with `featureId`.
    """

    dimensions: Dict[str, str]
    """Optional attribution map (e.g.

    `dimensions[userId]=u1`). When provided, the response includes a `chains` array
    with per-entity governance limits.
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

    x_account_id: Annotated[str, PropertyInfo(alias="X-ACCOUNT-ID")]

    x_environment_id: Annotated[str, PropertyInfo(alias="X-ENVIRONMENT-ID")]
