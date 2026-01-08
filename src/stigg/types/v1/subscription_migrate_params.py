# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SubscriptionMigrateParams"]


class SubscriptionMigrateParams(TypedDict, total=False):
    subscription_migration_time: Annotated[
        Literal["END_OF_BILLING_PERIOD", "IMMEDIATE"], PropertyInfo(alias="subscriptionMigrationTime")
    ]
    """When to migrate the subscription: IMMEDIATE or END_OF_BILLING_PERIOD"""
