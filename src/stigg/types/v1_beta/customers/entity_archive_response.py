# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel

__all__ = ["EntityArchiveResponse", "Data"]


class Data(BaseModel):
    """List of entity identifiers that were acted on"""

    ids: List[str]
    """Entity identifiers to act on"""


class EntityArchiveResponse(BaseModel):
    """
    Wrapped response echoing the ids that were acted on by an archive/unarchive call
    """

    data: Data
    """List of entity identifiers that were acted on"""
