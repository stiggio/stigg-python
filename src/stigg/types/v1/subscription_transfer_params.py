# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SubscriptionTransferParams"]


class SubscriptionTransferParams(TypedDict, total=False):
    destination_resource_id: Required[Annotated[str, PropertyInfo(alias="destinationResourceId")]]
    """Resource ID to transfer the subscription to"""
