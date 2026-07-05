# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["EntityUpsertParams", "Entity"]


class EntityUpsertParams(TypedDict, total=False):
    entities: Required[Iterable[Entity]]
    """List of entities to create or update (1-100 entries)"""

    x_account_id: Annotated[str, PropertyInfo(alias="X-ACCOUNT-ID")]

    x_environment_id: Annotated[str, PropertyInfo(alias="X-ENVIRONMENT-ID")]


class Entity(TypedDict, total=False):
    """A single entity to create or update."""

    id: Required[str]
    """The unique identifier for the entity"""

    entity_type_id: Annotated[str, PropertyInfo(alias="entityTypeId")]
    """The entity type ID this entity instantiates.

    Required when creating a new entity; on a re-upsert may be omitted to preserve
    the existing type. Governance returns 400 if missing on create.
    """

    metadata: Dict[str, str]
    """Free-form key/value metadata.

    Patch semantics: empty-string value removes a key, omitted keys are preserved.
    """
