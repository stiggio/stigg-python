# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["CustomerListResourcesResponse"]


class CustomerListResourcesResponse(BaseModel):
    """
    Resource object that belongs to a customer, used to scope subscriptions and entitlements to a specific instance within the customer's account (e.g. a website, project, or workspace) for multi-resource pricing. A resource is identified only by its resourceId — there's no separate display name or metadata field on the resource itself; if you need to attach descriptive data, keep it in your own system keyed by resourceId.
    """

    id: str
    """Resource slug"""

    created_at: datetime = FieldInfo(alias="createdAt")
    """Timestamp of when the record was created"""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """Timestamp of when the record was last updated"""
