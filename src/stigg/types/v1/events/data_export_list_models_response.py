# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["DataExportListModelsResponse", "Data", "DataGroup", "DataGroupModel"]


class DataGroupModel(BaseModel):
    """A single data-export model the customer can opt into."""

    id: str
    """
    Wire identifier — what gets persisted on the destination and registered with the
    provider
    """

    display_name: str = FieldInfo(alias="displayName")
    """Customer-facing label for the model"""


class DataGroup(BaseModel):
    """A group of related data-export models, mirroring the public docs taxonomy."""

    id: str
    """Stable group identifier"""

    display_name: str = FieldInfo(alias="displayName")
    """Customer-facing group label"""

    models: List[DataGroupModel]
    """Models in this group"""


class Data(BaseModel):
    """Grouped catalog of every data-export model a destination can opt into."""

    groups: List[DataGroup]
    """Groups of data-export models, in display order"""


class DataExportListModelsResponse(BaseModel):
    """Response object"""

    data: Data
    """Grouped catalog of every data-export model a destination can opt into."""
