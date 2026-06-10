# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["EntityTypeUpsertParams", "Type"]


class EntityTypeUpsertParams(TypedDict, total=False):
    types: Required[Iterable[Type]]
    """Entity types to upsert (1–100 per request)"""

    x_account_id: Annotated[str, PropertyInfo(alias="X-ACCOUNT-ID")]

    x_environment_id: Annotated[str, PropertyInfo(alias="X-ENVIRONMENT-ID")]


class Type(TypedDict, total=False):
    """A single entity type definition."""

    id: Required[str]
    """The unique identifier for the entity"""

    attribution_keys: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="attributionKeys")]]
    """Dimension keys used to attribute usage events to instances of this type (e.g.

    ["orgId"]). Empty array means no attribution.
    """

    display_name: Required[Annotated[str, PropertyInfo(alias="displayName")]]
    """The display name for the entity type"""
