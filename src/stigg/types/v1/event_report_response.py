# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["EventReportResponse"]


class EventReportResponse(BaseModel):
    """Response object"""

    data: object
    """
    Empty success response confirming that events were successfully ingested and
    queued for processing by Stigg's metering system.
    """
