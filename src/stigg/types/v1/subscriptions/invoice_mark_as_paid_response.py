# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["InvoiceMarkAsPaidResponse", "Data"]


class Data(BaseModel):
    """Result of marking a subscription invoice as paid."""

    id: str
    """The subscription ID whose invoice was marked as paid"""


class InvoiceMarkAsPaidResponse(BaseModel):
    """Response object"""

    data: Data
    """Result of marking a subscription invoice as paid."""
