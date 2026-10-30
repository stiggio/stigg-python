# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel

__all__ = ["EntityTypeArchiveResponse", "Data"]


class Data(BaseModel):
    """List of entity type identifiers that were acted on"""

    ids: List[str]
    """Entity type identifiers to act on"""


class EntityTypeArchiveResponse(BaseModel):
    """
    Wrapped response echoing the entity type ids that were acted on by an archive call
    """

    data: Data
    """List of entity type identifiers that were acted on"""
