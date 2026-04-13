# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["EventQueueProvisionParams"]


class EventQueueProvisionParams(TypedDict, total=False):
    region: Required[
        Literal[
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
    ]
    """AWS region for the SQS queue (e.g., us-east-1, eu-west-1)"""

    allowed_assume_role_arns: Annotated[SequenceNotStr[str], PropertyInfo(alias="allowedAssumeRoleArns")]
    """Additional IAM role ARNs allowed to assume the external role for queue access"""

    create_low_priority_queues: Annotated[bool, PropertyInfo(alias="createLowPriorityQueues")]
    """Whether to create separate low-priority queues for standard topic events"""

    event_types: Annotated[
        List[
            Literal[
                "MEMBER_INVITED",
                "SYNC_SUBSCRIPTION",
                "SYNC_CREDIT_GRANT",
                "CUSTOMER_CREATED",
                "CUSTOMER_UPDATED",
                "CUSTOMER_DELETED",
                "SYNC_CUSTOMER",
                "SUBSCRIPTION_CREATED",
                "SUBSCRIPTION_CANCELED",
                "SUBSCRIPTION_EXPIRED",
                "SUBSCRIPTION_UPDATED",
                "SUBSCRIPTION_TRIAL_STARTED",
                "SUBSCRIPTION_TRIAL_EXPIRED",
                "SUBSCRIPTION_TRIAL_CONVERTED",
                "SUBSCRIPTION_TRIAL_ENDS_SOON",
                "SYNC_SUBSCRIPTION_USAGE",
                "SUBSCRIPTION_USAGE_UPDATED",
                "SUBSCRIPTION_SPENT_LIMIT_EXCEEDED",
                "CREATE_SUBSCRIPTION_FAILED",
                "PLAN_CREATED",
                "PLAN_UPDATED",
                "PLAN_DELETED",
                "ADDON_CREATED",
                "ADDON_UPDATED",
                "ADDON_DELETED",
                "SYNC_PACKAGE",
                "FEATURE_CREATED",
                "FEATURE_UPDATED",
                "FEATURE_DELETED",
                "FEATURE_ARCHIVED",
                "API_KEY_CREATED",
                "API_KEY_UPDATED",
                "API_KEY_ROTATED",
                "API_KEY_REVOKED",
                "ENTITLEMENT_REQUESTED",
                "ENTITLEMENT_GRANTED",
                "ENTITLEMENT_DENIED",
                "MEASUREMENT_REPORTED",
                "USAGE_THRESHOLD_EXCEEDED",
                "PROMOTIONAL_ENTITLEMENT_GRANTED",
                "PROMOTIONAL_ENTITLEMENT_REVOKED",
                "PROMOTIONAL_ENTITLEMENT_UPDATED",
                "PROMOTIONAL_ENTITLEMENT_EXPIRED",
                "PROMOTIONAL_ENTITLEMENT_ENDS_SOON",
                "PACKAGE_PUBLISHED",
                "MIGRATE_SUBSCRIPTIONS",
                "RECALCULATE_MIGRATED_ENTITLEMENTS_BATCH",
                "MIGRATE_SUBSCRIPTIONS_SCHEDULED_UPDATES",
                "ENTITLEMENTS_UPDATED",
                "RESYNC_INTEGRATION_TRIGGERED",
                "COUPON_CREATED",
                "COUPON_UPDATED",
                "IMPORT_INTEGRATION_CATALOG_TRIGGERED",
                "IMPORT_INTEGRATION_CUSTOMERS_TRIGGERED",
                "INCOMING_STRIPE_WEBHOOK",
                "INCOMING_AWS_MARKETPLACE_WEBHOOK",
                "INCOMING_ZUORA_WEBHOOK",
                "INCOMING_DOGGO_WEBHOOK",
                "INCOMING_APP_STORE_WEBHOOK",
                "RESYNC_INTEGRATION",
                "SYNC_COUPON",
                "IMPORT_INTEGRATION_CATALOG",
                "IMPORT_INTEGRATION_CUSTOMERS",
                "SYNC_FAILED",
                "CUSTOMER_PAYMENT_FAILED",
                "PRODUCT_CREATED",
                "PRODUCT_UPDATED",
                "PRODUCT_DELETED",
                "PRODUCT_UNARCHIVED",
                "PACKAGE_GROUP_CREATED",
                "PACKAGE_GROUP_UPDATED",
                "ENVIRONMENT_DELETED",
                "WIDGET_CONFIGURATION_UPDATED",
                "EDGE_API_DATA_RESYNC",
                "EDGE_API_DOGGO_RESYNC",
                "EDGE_API_CLIENT_CONFIGURATION_DATA_RESYNC",
                "PURGE_CUSTOMER_PERSISTENT_CACHE_REQUESTED",
                "CUSTOMER_RESOURCE_ENTITLEMENT_CALCULATION_TRIGGERED",
                "RECALCULATE_RESOURCE_ENTITLEMENTS",
                "CUSTOMER_ENTITLEMENT_CALCULATION_TRIGGERED[",
                "RECALCULATE_ENTITLEMENTS_TRIGGERED",
                "IMPORT_SUBSCRIPTIONS_BULK_TRIGGERED",
                "EDGE_API_CUSTOMER_DATA_RESYNC",
                "EDGE_API_SUBSCRIPTIONS_DATA_RESYNC",
                "EDGE_API_PACKAGE_ENTITLEMENTS_DATA_RESYNC",
                "EDGE_API_PRODUCT_CACHE_DATA_RESYNC",
                "EDGE_API_PLAN_CACHE_DATA_RESYNC",
                "EDGE_API_CUSTOM_CURRENCY_CACHE_DATA_RESYNC",
                "REPLAY_WEBHOOK_EVENT",
                "SUBSCRIPTIONS_MIGRATED",
                "SUBSCRIPTIONS_MIGRATION_TRIGGERED",
                "SUBSCRIPTION_BILLING_MONTH_ENDS_SOON",
                "SUBSCRIPTION_USAGE_CHARGE_TRIGGERED",
                "SCHEDULER_BATCH",
                "EVENT_LOG_CREATED",
                "CREDIT_GRANT_CREATED",
                "CREDIT_GRANT_EXPIRED",
                "CREDIT_GRANT_VOIDED",
                "CREDIT_GRANT_UPDATED",
                "CREDIT_GRANT_DEPLETED",
                "CREDIT_GRANT_BALANCE_LOW",
                "CREDIT_BALANCE_UPDATED",
                "CREDIT_BALANCE_DEPLETED",
                "CREDIT_BALANCE_LOW",
                "CREDIT_GRANT_PROCESS_COMPLETED",
                "AUTOMATIC_RECHARGE_THRESHOLD_BREACH",
                "AUTOMATIC_RECHARGE_OPERATION_ATTEMPTED",
                "CREDITS_AUTOMATIC_RECHARGE_LIMIT_EXCEEDED",
                "AUTOMATIC_RECHARGE_CONFIGURATION_CHANGED",
                "FEATURE_GROUP_CREATED",
                "FEATURE_GROUP_UPDATED",
                "FEATURE_GROUP_ARCHIVED",
                "FEATURE_GROUP_UN_ARCHIVED",
                "STRIPE_APP_DRAWER_VIEWED",
                "EVENT_QUEUE_PROVISIONING_REQUESTED",
                "EVENT_QUEUE_DEPROVISIONING_REQUESTED",
            ]
        ],
        PropertyInfo(alias="eventTypes"),
    ]
    """Event types to subscribe to.

    Defaults to entitlements, measurements, and migrations.
    """

    suffix: str
    """Optional suffix to allow multiple queues for the same environment and region"""
