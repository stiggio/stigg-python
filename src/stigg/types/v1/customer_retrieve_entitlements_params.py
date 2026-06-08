# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["CustomerRetrieveEntitlementsParams"]


class CustomerRetrieveEntitlementsParams(TypedDict, total=False):
    resource_id: Annotated[str, PropertyInfo(alias="resourceId")]
    """Resource ID to scope entitlements to a specific resource"""

    x_account_id: Annotated[str, PropertyInfo(alias="X-ACCOUNT-ID")]

    x_environment_id: Annotated[str, PropertyInfo(alias="X-ENVIRONMENT-ID")]
