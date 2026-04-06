# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.internal.beta import event_queue_update_params, event_queue_provision_params
from ....types.internal.beta.event_queue_list_response import EventQueueListResponse
from ....types.internal.beta.event_queue_delete_response import EventQueueDeleteResponse
from ....types.internal.beta.event_queue_update_response import EventQueueUpdateResponse
from ....types.internal.beta.event_queue_retrieve_response import EventQueueRetrieveResponse
from ....types.internal.beta.event_queue_provision_response import EventQueueProvisionResponse

__all__ = ["EventQueuesResource", "AsyncEventQueuesResource"]


class EventQueuesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EventQueuesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stiggio/stigg-python#accessing-raw-response-data-eg-headers
        """
        return EventQueuesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EventQueuesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stiggio/stigg-python#with_streaming_response
        """
        return EventQueuesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        queue_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EventQueueRetrieveResponse:
        """
        Get event queue by queue name

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not queue_name:
            raise ValueError(f"Expected a non-empty value for `queue_name` but received {queue_name!r}")
        return self._get(
            path_template("/internal/beta/event-queues/{queue_name}", queue_name=queue_name),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EventQueueRetrieveResponse,
        )

    def update(
        self,
        queue_name: str,
        *,
        allowed_assume_role_arns: SequenceNotStr[str] | Omit = omit,
        create_low_priority_queues: bool | Omit = omit,
        event_types: List[
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
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EventQueueUpdateResponse:
        """
        Update event queue configuration

        Args:
          create_low_priority_queues: Whether to create separate low-priority queues for standard topic events

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not queue_name:
            raise ValueError(f"Expected a non-empty value for `queue_name` but received {queue_name!r}")
        return self._patch(
            path_template("/internal/beta/event-queues/{queue_name}", queue_name=queue_name),
            body=maybe_transform(
                {
                    "allowed_assume_role_arns": allowed_assume_role_arns,
                    "create_low_priority_queues": create_low_priority_queues,
                    "event_types": event_types,
                },
                event_queue_update_params.EventQueueUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EventQueueUpdateResponse,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EventQueueListResponse:
        """List all event queues for the current environment"""
        return self._get(
            "/internal/beta/event-queues",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EventQueueListResponse,
        )

    def delete(
        self,
        queue_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EventQueueDeleteResponse:
        """
        Delete an event queue and tear down its infrastructure

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not queue_name:
            raise ValueError(f"Expected a non-empty value for `queue_name` but received {queue_name!r}")
        return self._delete(
            path_template("/internal/beta/event-queues/{queue_name}", queue_name=queue_name),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EventQueueDeleteResponse,
        )

    def provision(
        self,
        *,
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
        ],
        allowed_assume_role_arns: SequenceNotStr[str] | Omit = omit,
        create_low_priority_queues: bool | Omit = omit,
        event_types: List[
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
        ]
        | Omit = omit,
        suffix: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EventQueueProvisionResponse:
        """
        Provision SQS queue, SNS subscriptions, and IAM role for the current environment

        Args:
          region: AWS region for the SQS queue (e.g., us-east-1, eu-west-1)

          allowed_assume_role_arns: Additional IAM role ARNs allowed to assume the external role for queue access

          create_low_priority_queues: Whether to create separate low-priority queues for standard topic events

          event_types: Event types to subscribe to. Defaults to entitlements, measurements, and
              migrations.

          suffix: Optional suffix to allow multiple queues for the same environment and region

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/internal/beta/event-queues/provision",
            body=maybe_transform(
                {
                    "region": region,
                    "allowed_assume_role_arns": allowed_assume_role_arns,
                    "create_low_priority_queues": create_low_priority_queues,
                    "event_types": event_types,
                    "suffix": suffix,
                },
                event_queue_provision_params.EventQueueProvisionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EventQueueProvisionResponse,
        )


class AsyncEventQueuesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEventQueuesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stiggio/stigg-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEventQueuesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEventQueuesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stiggio/stigg-python#with_streaming_response
        """
        return AsyncEventQueuesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        queue_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EventQueueRetrieveResponse:
        """
        Get event queue by queue name

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not queue_name:
            raise ValueError(f"Expected a non-empty value for `queue_name` but received {queue_name!r}")
        return await self._get(
            path_template("/internal/beta/event-queues/{queue_name}", queue_name=queue_name),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EventQueueRetrieveResponse,
        )

    async def update(
        self,
        queue_name: str,
        *,
        allowed_assume_role_arns: SequenceNotStr[str] | Omit = omit,
        create_low_priority_queues: bool | Omit = omit,
        event_types: List[
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
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EventQueueUpdateResponse:
        """
        Update event queue configuration

        Args:
          create_low_priority_queues: Whether to create separate low-priority queues for standard topic events

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not queue_name:
            raise ValueError(f"Expected a non-empty value for `queue_name` but received {queue_name!r}")
        return await self._patch(
            path_template("/internal/beta/event-queues/{queue_name}", queue_name=queue_name),
            body=await async_maybe_transform(
                {
                    "allowed_assume_role_arns": allowed_assume_role_arns,
                    "create_low_priority_queues": create_low_priority_queues,
                    "event_types": event_types,
                },
                event_queue_update_params.EventQueueUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EventQueueUpdateResponse,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EventQueueListResponse:
        """List all event queues for the current environment"""
        return await self._get(
            "/internal/beta/event-queues",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EventQueueListResponse,
        )

    async def delete(
        self,
        queue_name: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EventQueueDeleteResponse:
        """
        Delete an event queue and tear down its infrastructure

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not queue_name:
            raise ValueError(f"Expected a non-empty value for `queue_name` but received {queue_name!r}")
        return await self._delete(
            path_template("/internal/beta/event-queues/{queue_name}", queue_name=queue_name),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EventQueueDeleteResponse,
        )

    async def provision(
        self,
        *,
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
        ],
        allowed_assume_role_arns: SequenceNotStr[str] | Omit = omit,
        create_low_priority_queues: bool | Omit = omit,
        event_types: List[
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
        ]
        | Omit = omit,
        suffix: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EventQueueProvisionResponse:
        """
        Provision SQS queue, SNS subscriptions, and IAM role for the current environment

        Args:
          region: AWS region for the SQS queue (e.g., us-east-1, eu-west-1)

          allowed_assume_role_arns: Additional IAM role ARNs allowed to assume the external role for queue access

          create_low_priority_queues: Whether to create separate low-priority queues for standard topic events

          event_types: Event types to subscribe to. Defaults to entitlements, measurements, and
              migrations.

          suffix: Optional suffix to allow multiple queues for the same environment and region

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/internal/beta/event-queues/provision",
            body=await async_maybe_transform(
                {
                    "region": region,
                    "allowed_assume_role_arns": allowed_assume_role_arns,
                    "create_low_priority_queues": create_low_priority_queues,
                    "event_types": event_types,
                    "suffix": suffix,
                },
                event_queue_provision_params.EventQueueProvisionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EventQueueProvisionResponse,
        )


class EventQueuesResourceWithRawResponse:
    def __init__(self, event_queues: EventQueuesResource) -> None:
        self._event_queues = event_queues

        self.retrieve = to_raw_response_wrapper(
            event_queues.retrieve,
        )
        self.update = to_raw_response_wrapper(
            event_queues.update,
        )
        self.list = to_raw_response_wrapper(
            event_queues.list,
        )
        self.delete = to_raw_response_wrapper(
            event_queues.delete,
        )
        self.provision = to_raw_response_wrapper(
            event_queues.provision,
        )


class AsyncEventQueuesResourceWithRawResponse:
    def __init__(self, event_queues: AsyncEventQueuesResource) -> None:
        self._event_queues = event_queues

        self.retrieve = async_to_raw_response_wrapper(
            event_queues.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            event_queues.update,
        )
        self.list = async_to_raw_response_wrapper(
            event_queues.list,
        )
        self.delete = async_to_raw_response_wrapper(
            event_queues.delete,
        )
        self.provision = async_to_raw_response_wrapper(
            event_queues.provision,
        )


class EventQueuesResourceWithStreamingResponse:
    def __init__(self, event_queues: EventQueuesResource) -> None:
        self._event_queues = event_queues

        self.retrieve = to_streamed_response_wrapper(
            event_queues.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            event_queues.update,
        )
        self.list = to_streamed_response_wrapper(
            event_queues.list,
        )
        self.delete = to_streamed_response_wrapper(
            event_queues.delete,
        )
        self.provision = to_streamed_response_wrapper(
            event_queues.provision,
        )


class AsyncEventQueuesResourceWithStreamingResponse:
    def __init__(self, event_queues: AsyncEventQueuesResource) -> None:
        self._event_queues = event_queues

        self.retrieve = async_to_streamed_response_wrapper(
            event_queues.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            event_queues.update,
        )
        self.list = async_to_streamed_response_wrapper(
            event_queues.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            event_queues.delete,
        )
        self.provision = async_to_streamed_response_wrapper(
            event_queues.provision,
        )
