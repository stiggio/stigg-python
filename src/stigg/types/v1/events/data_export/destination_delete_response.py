# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["DestinationDeleteResponse", "Data", "DataDestination"]


class DataDestination(BaseModel):
    """A single destination entry under the DATA_EXPORT integration."""

    connected_at: str = FieldInfo(alias="connectedAt")
    """ISO8601 timestamp of when the destination was connected"""

    destination_id: str = FieldInfo(alias="destinationId")
    """Provider destination ID"""

    type: str
    """Destination type (snowflake, bigquery, ...)"""


class Data(BaseModel):
    """Current destinations under the DATA_EXPORT integration."""

    destinations: List[DataDestination]
    """Current destinations under the DATA_EXPORT integration"""


class DestinationDeleteResponse(BaseModel):
    """Response object"""

    data: Data
    """Current destinations under the DATA_EXPORT integration."""
