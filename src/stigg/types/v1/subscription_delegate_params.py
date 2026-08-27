# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SubscriptionDelegateParams"]


class SubscriptionDelegateParams(TypedDict, total=False):
    target_customer_id: Required[Annotated[str, PropertyInfo(alias="targetCustomerId")]]
    """
    The unique identifier of the customer who will manage this subscription going
    forward. This customer must already exist in your Stigg account. The paying
    customer for the subscription does not change as a result of this request.
    """

    x_account_id: Annotated[str, PropertyInfo(alias="X-ACCOUNT-ID")]

    x_environment_id: Annotated[str, PropertyInfo(alias="X-ENVIRONMENT-ID")]
