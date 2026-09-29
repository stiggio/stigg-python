# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["IntegrationLinkParams"]


class IntegrationLinkParams(TypedDict, total=False):
    body_id: Required[Annotated[str, PropertyInfo(alias="id")]]
    """The internal ID of the integration this record is linked to"""

    synced_entity_id: Required[Annotated[str, PropertyInfo(alias="syncedEntityId")]]
    """The external entity ID this record is linked to in the vendor system (e.g.

    the Stripe customer ID). Null until the link has synced; required when creating
    the link.
    """

    vendor_identifier: Required[
        Annotated[Literal["STRIPE", "ZUORA", "HUBSPOT", "AWS_MARKETPLACE"], PropertyInfo(alias="vendorIdentifier")]
    ]
    """The vendor whose system holds the customer record"""

    x_account_id: Annotated[str, PropertyInfo(alias="X-ACCOUNT-ID")]

    x_environment_id: Annotated[str, PropertyInfo(alias="X-ENVIRONMENT-ID")]
