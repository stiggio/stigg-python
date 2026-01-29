# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["CustomerImportResponse", "Data"]


class Data(BaseModel):
    """List of newly created customer IDs from the import operation."""

    new_customers: List[str] = FieldInfo(alias="newCustomers")
    """Customer IDs created during import"""


class CustomerImportResponse(BaseModel):
    """Response object"""

    data: Data
    """List of newly created customer IDs from the import operation."""
