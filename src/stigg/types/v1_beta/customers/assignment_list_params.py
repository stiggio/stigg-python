# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["AssignmentListParams"]


class AssignmentListParams(TypedDict, total=False):
    after: str
    """Return items that come after this cursor"""

    before: str
    """Return items that come before this cursor"""

    currency_id: Annotated[str, PropertyInfo(alias="currencyId")]
    """Filter assignments to a specific currency, by its ID.

    Mutually exclusive with `featureId`.
    """

    entity_id: Annotated[str, PropertyInfo(alias="entityId")]
    """Filter assignments to a specific entity ID"""

    feature_id: Annotated[str, PropertyInfo(alias="featureId")]
    """Filter assignments to a specific feature, by its ID.

    Mutually exclusive with `currencyId`.
    """

    limit: int
    """Maximum number of items to return"""

    x_account_id: Annotated[str, PropertyInfo(alias="X-ACCOUNT-ID")]

    x_environment_id: Annotated[str, PropertyInfo(alias="X-ENVIRONMENT-ID")]
