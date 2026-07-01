# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["ConsumptionConsumeAsyncResponse"]


class ConsumptionConsumeAsyncResponse(BaseModel):
    """Response object"""

    data: object
    """Confirmation that the credit consumptions were accepted for processing"""
