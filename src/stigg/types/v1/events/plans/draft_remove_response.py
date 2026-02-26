# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ....._models import BaseModel

__all__ = ["DraftRemoveResponse", "Data"]


class Data(BaseModel):
    id: str
    """The unique identifier for the entity"""


class DraftRemoveResponse(BaseModel):
    """Response confirming the plan draft was removed."""

    data: Data
