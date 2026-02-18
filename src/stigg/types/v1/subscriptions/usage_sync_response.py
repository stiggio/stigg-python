# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["UsageSyncResponse", "Data"]


class Data(BaseModel):
    """Result of triggering a subscription usage sync."""

    triggered: bool
    """Whether usage was synced to the billing provider"""


class UsageSyncResponse(BaseModel):
    """Response object"""

    data: Data
    """Result of triggering a subscription usage sync."""
