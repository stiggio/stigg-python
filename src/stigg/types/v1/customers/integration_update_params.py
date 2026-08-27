# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["IntegrationUpdateParams"]


class IntegrationUpdateParams(TypedDict, total=False):
    id: Required[str]

    synced_entity_id: Required[Annotated[Optional[str], PropertyInfo(alias="syncedEntityId")]]
    """The external entity ID this record is linked to in the vendor system (e.g.

    the Stripe customer ID). Null until the link has synced; required when creating
    the link.
    """

    x_account_id: Annotated[str, PropertyInfo(alias="X-ACCOUNT-ID")]

    x_environment_id: Annotated[str, PropertyInfo(alias="X-ENVIRONMENT-ID")]
