# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SubscriptionDelegateParams"]


class SubscriptionDelegateParams(TypedDict, total=False):
    target_customer_id: Required[Annotated[str, PropertyInfo(alias="targetCustomerId")]]
    """The customer ID to delegate the subscription to"""
