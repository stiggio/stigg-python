# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SubscriptionDelegateParams"]


class SubscriptionDelegateParams(TypedDict, total=False):
    target_customer_id: Required[Annotated[str, PropertyInfo(alias="targetCustomerId")]]
    """
    The unique identifier of the customer who will assume payment responsibility for
    this subscription. This customer must already exist in your Stigg account and
    have a valid payment method if the subscription requires payment.
    """
