# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["CustomCurrencyListAssociatedEntitiesResponse", "Data"]


class Data(BaseModel):
    """An entity (plan or addon) that references a custom currency"""

    id: str
    """The reference ID of the associated entity"""

    display_name: str = FieldInfo(alias="displayName")
    """The display name of the associated entity"""

    type: str
    """The kind of entity referencing the currency (e.g., Plan)"""


class CustomCurrencyListAssociatedEntitiesResponse(BaseModel):
    """List of entities (plans or addons) that reference a custom currency"""

    data: List[Data]
