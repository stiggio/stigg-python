# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["EntityListParams"]


class EntityListParams(TypedDict, total=False):
    after: str
    """Return items that come after this cursor"""

    before: str
    """Return items that come before this cursor"""

    include_archived: Annotated[Literal["true", "false"], PropertyInfo(alias="includeArchived")]
    """Whether to include archived entities. One of: true, false"""

    limit: int
    """Maximum number of items to return"""

    type_ref_id: Annotated[str, PropertyInfo(alias="typeRefId")]
    """Filter results to entities of a specific entity type, by the type's refId"""

    x_account_id: Annotated[str, PropertyInfo(alias="X-ACCOUNT-ID")]

    x_environment_id: Annotated[str, PropertyInfo(alias="X-ENVIRONMENT-ID")]
