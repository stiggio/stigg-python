# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["AddonRemoveDraftResponse", "Data"]


class Data(BaseModel):
    id: str
    """The unique identifier for the entity"""


class AddonRemoveDraftResponse(BaseModel):
    """Response confirming the addon draft was removed."""

    data: Data
