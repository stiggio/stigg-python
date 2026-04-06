# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["EventQueueUpdateResponse", "Data"]


class Data(BaseModel):
    """Event queue provisioning status and details"""

    created_at: datetime = FieldInfo(alias="createdAt")
    """Timestamp of when the record was created"""

    queue_name: str = FieldInfo(alias="queueName")
    """Unique queue identifier"""

    region: Literal[
        "us-east-1",
        "us-east-2",
        "us-west-1",
        "us-west-2",
        "ca-central-1",
        "eu-west-1",
        "eu-west-2",
        "eu-west-3",
        "eu-central-1",
        "eu-central-2",
        "eu-north-1",
        "eu-south-1",
        "eu-south-2",
        "ap-southeast-1",
        "ap-southeast-2",
        "ap-southeast-3",
        "ap-northeast-1",
        "ap-northeast-2",
        "ap-northeast-3",
        "ap-south-1",
        "ap-south-2",
        "ap-east-1",
        "sa-east-1",
        "af-south-1",
        "me-south-1",
        "me-central-1",
        "il-central-1",
    ]
    """AWS region where the queue is deployed"""

    status: Literal["PROVISIONING", "ACTIVE", "FAILED", "DEPROVISIONING"]
    """Current provisioning status"""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """Timestamp of when the record was last updated"""

    queue_url: Optional[str] = FieldInfo(alias="queueUrl", default=None)
    """SQS queue URL"""

    role_arn: Optional[str] = FieldInfo(alias="roleArn", default=None)
    """IAM role ARN for queue access"""

    suffix: Optional[str] = None
    """Queue suffix for disambiguation"""


class EventQueueUpdateResponse(BaseModel):
    """Response object"""

    data: Data
    """Event queue provisioning status and details"""
