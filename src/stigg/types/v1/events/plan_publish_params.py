# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["PlanPublishParams"]


class PlanPublishParams(TypedDict, total=False):
    migration_type: Required[Annotated[Literal["NEW_CUSTOMERS", "ALL_CUSTOMERS"], PropertyInfo(alias="migrationType")]]
    """The migration type of the package"""
