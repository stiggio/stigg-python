# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["CustomCurrencyListResponse", "Units"]


class Units(BaseModel):
    """Singular and plural unit labels for a custom currency"""

    plural: Optional[str] = None
    """Plural form of the unit label"""

    singular: Optional[str] = None
    """Singular form of the unit label"""


class CustomCurrencyListResponse(BaseModel):
    """A custom currency used to denominate credit-based entitlements and pricing"""

    id: str
    """The unique identifier for the custom currency"""

    archived_at: Optional[datetime] = FieldInfo(alias="archivedAt", default=None)
    """Timestamp of when the record was deleted"""

    created_at: datetime = FieldInfo(alias="createdAt")
    """Timestamp of when the record was created"""

    description: Optional[str] = None
    """Description of the currency"""

    display_name: str = FieldInfo(alias="displayName")
    """The display name of the custom currency"""

    metadata: Dict[str, str]
    """Metadata associated with the entity"""

    symbol: Optional[str] = None
    """The symbol used to represent the custom currency"""

    units: Optional[Units] = None
    """Singular and plural unit labels for a custom currency"""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """Timestamp of when the record was last updated"""
