# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["CustomerRetrieveResponse"]


class CustomerRetrieveResponse(BaseModel):
    id: str
    """Unique identifier for the entity"""

    email: Optional[str] = None
    """The email of the customer"""

    name: Optional[str] = None
    """The name of the customer"""
