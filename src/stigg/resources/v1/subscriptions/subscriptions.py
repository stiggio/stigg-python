# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ....types.v1 import (
    subscription_list_params,
    subscription_create_params,
    subscription_migrate_params,
    subscription_preview_params,
    subscription_delegate_params,
    subscription_transfer_params,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncMyCursorIDPage, AsyncMyCursorIDPage
from .future_update import (
    FutureUpdateResource,
    AsyncFutureUpdateResource,
    FutureUpdateResourceWithRawResponse,
    AsyncFutureUpdateResourceWithRawResponse,
    FutureUpdateResourceWithStreamingResponse,
    AsyncFutureUpdateResourceWithStreamingResponse,
)
from ...._base_client import AsyncPaginator, make_request_options
from ....types.v1.subscription_list_response import SubscriptionListResponse
from ....types.v1.subscription_create_response import SubscriptionCreateResponse
from ....types.v1.subscription_migrate_response import SubscriptionMigrateResponse
from ....types.v1.subscription_preview_response import SubscriptionPreviewResponse
from ....types.v1.subscription_delegate_response import SubscriptionDelegateResponse
from ....types.v1.subscription_retrieve_response import SubscriptionRetrieveResponse
from ....types.v1.subscription_transfer_response import SubscriptionTransferResponse

__all__ = ["SubscriptionsResource", "AsyncSubscriptionsResource"]


class SubscriptionsResource(SyncAPIResource):
    @cached_property
    def future_update(self) -> FutureUpdateResource:
        return FutureUpdateResource(self._client)

    @cached_property
    def with_raw_response(self) -> SubscriptionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stiggio/stigg-python#accessing-raw-response-data-eg-headers
        """
        return SubscriptionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SubscriptionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stiggio/stigg-python#with_streaming_response
        """
        return SubscriptionsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        customer_id: str,
        plan_id: str,
        id: Optional[str] | Omit = omit,
        await_payment_confirmation: bool | Omit = omit,
        billing_period: Literal["MONTHLY", "ANNUALLY"] | Omit = omit,
        checkout_options: subscription_create_params.CheckoutOptions | Omit = omit,
        metadata: Dict[str, str] | Omit = omit,
        paying_customer_id: Optional[str] | Omit = omit,
        resource_id: Optional[str] | Omit = omit,
        trial_override_configuration: subscription_create_params.TrialOverrideConfiguration | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionCreateResponse:
        """
        Create a new Subscription

        Args:
          customer_id: Customer ID to provision the subscription for

          plan_id: Plan ID to provision

          id: Unique identifier for the subscription

          await_payment_confirmation: Whether to wait for payment confirmation before returning the subscription

          metadata: Additional metadata for the subscription

          paying_customer_id: Optional paying customer ID for split billing scenarios

          resource_id: Optional resource ID for multi-instance subscriptions

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/subscriptions",
            body=maybe_transform(
                {
                    "customer_id": customer_id,
                    "plan_id": plan_id,
                    "id": id,
                    "await_payment_confirmation": await_payment_confirmation,
                    "billing_period": billing_period,
                    "checkout_options": checkout_options,
                    "metadata": metadata,
                    "paying_customer_id": paying_customer_id,
                    "resource_id": resource_id,
                    "trial_override_configuration": trial_override_configuration,
                },
                subscription_create_params.SubscriptionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionCreateResponse,
        )

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionRetrieveResponse:
        """
        Get a single Subscription by id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/api/v1/subscriptions/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionRetrieveResponse,
        )

    def list(
        self,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        customer_id: str | Omit = omit,
        limit: int | Omit = omit,
        status: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncMyCursorIDPage[SubscriptionListResponse]:
        """
        Get a list of Subscriptions

        Args:
          after: Starting after this UUID for pagination

          before: Ending before this UUID for pagination

          customer_id: Filter by customer ID

          limit: Items per page

          status: Filter by subscription status (comma-separated for multiple statuses, e.g.,
              ACTIVE,IN_TRIAL)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/v1/subscriptions",
            page=SyncMyCursorIDPage[SubscriptionListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "customer_id": customer_id,
                        "limit": limit,
                        "status": status,
                    },
                    subscription_list_params.SubscriptionListParams,
                ),
            ),
            model=SubscriptionListResponse,
        )

    def delegate(
        self,
        id: str,
        *,
        target_customer_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionDelegateResponse:
        """
        Perform delegate on a Subscription

        Args:
          target_customer_id: The customer ID to delegate the subscription to

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/api/v1/subscriptions/{id}/delegate",
            body=maybe_transform(
                {"target_customer_id": target_customer_id}, subscription_delegate_params.SubscriptionDelegateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionDelegateResponse,
        )

    def migrate(
        self,
        id: str,
        *,
        subscription_migration_time: Literal["END_OF_BILLING_PERIOD", "IMMEDIATE"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionMigrateResponse:
        """
        Perform migrate to latest plan version on a Subscription

        Args:
          subscription_migration_time: When to migrate the subscription: IMMEDIATE or END_OF_BILLING_PERIOD

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/api/v1/subscriptions/{id}/migrate",
            body=maybe_transform(
                {"subscription_migration_time": subscription_migration_time},
                subscription_migrate_params.SubscriptionMigrateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionMigrateResponse,
        )

    def preview(
        self,
        *,
        customer_id: str,
        plan_id: str,
        addons: Iterable[subscription_preview_params.Addon] | Omit = omit,
        applied_coupon: subscription_preview_params.AppliedCoupon | Omit = omit,
        billable_features: Iterable[subscription_preview_params.BillableFeature] | Omit = omit,
        billing_country_code: str | Omit = omit,
        billing_information: subscription_preview_params.BillingInformation | Omit = omit,
        billing_period: Literal["MONTHLY", "ANNUALLY"] | Omit = omit,
        charges: Iterable[subscription_preview_params.Charge] | Omit = omit,
        paying_customer_id: str | Omit = omit,
        resource_id: str | Omit = omit,
        schedule_strategy: Literal["END_OF_BILLING_PERIOD", "END_OF_BILLING_MONTH", "IMMEDIATE"] | Omit = omit,
        start_date: Union[str, datetime] | Omit = omit,
        trial_override_configuration: subscription_preview_params.TrialOverrideConfiguration | Omit = omit,
        unit_quantity: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionPreviewResponse:
        """
        Create a new Subscription Preview

        Args:
          customer_id: Customer ID

          plan_id: Plan ID

          start_date: Subscription start date

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/subscriptions/preview",
            body=maybe_transform(
                {
                    "customer_id": customer_id,
                    "plan_id": plan_id,
                    "addons": addons,
                    "applied_coupon": applied_coupon,
                    "billable_features": billable_features,
                    "billing_country_code": billing_country_code,
                    "billing_information": billing_information,
                    "billing_period": billing_period,
                    "charges": charges,
                    "paying_customer_id": paying_customer_id,
                    "resource_id": resource_id,
                    "schedule_strategy": schedule_strategy,
                    "start_date": start_date,
                    "trial_override_configuration": trial_override_configuration,
                    "unit_quantity": unit_quantity,
                },
                subscription_preview_params.SubscriptionPreviewParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionPreviewResponse,
        )

    def transfer(
        self,
        id: str,
        *,
        destination_resource_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionTransferResponse:
        """
        Perform transfer to resource on a Subscription

        Args:
          destination_resource_id: The resource ID to transfer the subscription to. The destination resource must
              belong to the same customer.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/api/v1/subscriptions/{id}/transfer",
            body=maybe_transform(
                {"destination_resource_id": destination_resource_id},
                subscription_transfer_params.SubscriptionTransferParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionTransferResponse,
        )


class AsyncSubscriptionsResource(AsyncAPIResource):
    @cached_property
    def future_update(self) -> AsyncFutureUpdateResource:
        return AsyncFutureUpdateResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSubscriptionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stiggio/stigg-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSubscriptionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSubscriptionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stiggio/stigg-python#with_streaming_response
        """
        return AsyncSubscriptionsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        customer_id: str,
        plan_id: str,
        id: Optional[str] | Omit = omit,
        await_payment_confirmation: bool | Omit = omit,
        billing_period: Literal["MONTHLY", "ANNUALLY"] | Omit = omit,
        checkout_options: subscription_create_params.CheckoutOptions | Omit = omit,
        metadata: Dict[str, str] | Omit = omit,
        paying_customer_id: Optional[str] | Omit = omit,
        resource_id: Optional[str] | Omit = omit,
        trial_override_configuration: subscription_create_params.TrialOverrideConfiguration | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionCreateResponse:
        """
        Create a new Subscription

        Args:
          customer_id: Customer ID to provision the subscription for

          plan_id: Plan ID to provision

          id: Unique identifier for the subscription

          await_payment_confirmation: Whether to wait for payment confirmation before returning the subscription

          metadata: Additional metadata for the subscription

          paying_customer_id: Optional paying customer ID for split billing scenarios

          resource_id: Optional resource ID for multi-instance subscriptions

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/subscriptions",
            body=await async_maybe_transform(
                {
                    "customer_id": customer_id,
                    "plan_id": plan_id,
                    "id": id,
                    "await_payment_confirmation": await_payment_confirmation,
                    "billing_period": billing_period,
                    "checkout_options": checkout_options,
                    "metadata": metadata,
                    "paying_customer_id": paying_customer_id,
                    "resource_id": resource_id,
                    "trial_override_configuration": trial_override_configuration,
                },
                subscription_create_params.SubscriptionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionCreateResponse,
        )

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionRetrieveResponse:
        """
        Get a single Subscription by id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/api/v1/subscriptions/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionRetrieveResponse,
        )

    def list(
        self,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        customer_id: str | Omit = omit,
        limit: int | Omit = omit,
        status: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[SubscriptionListResponse, AsyncMyCursorIDPage[SubscriptionListResponse]]:
        """
        Get a list of Subscriptions

        Args:
          after: Starting after this UUID for pagination

          before: Ending before this UUID for pagination

          customer_id: Filter by customer ID

          limit: Items per page

          status: Filter by subscription status (comma-separated for multiple statuses, e.g.,
              ACTIVE,IN_TRIAL)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/v1/subscriptions",
            page=AsyncMyCursorIDPage[SubscriptionListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "customer_id": customer_id,
                        "limit": limit,
                        "status": status,
                    },
                    subscription_list_params.SubscriptionListParams,
                ),
            ),
            model=SubscriptionListResponse,
        )

    async def delegate(
        self,
        id: str,
        *,
        target_customer_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionDelegateResponse:
        """
        Perform delegate on a Subscription

        Args:
          target_customer_id: The customer ID to delegate the subscription to

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/api/v1/subscriptions/{id}/delegate",
            body=await async_maybe_transform(
                {"target_customer_id": target_customer_id}, subscription_delegate_params.SubscriptionDelegateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionDelegateResponse,
        )

    async def migrate(
        self,
        id: str,
        *,
        subscription_migration_time: Literal["END_OF_BILLING_PERIOD", "IMMEDIATE"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionMigrateResponse:
        """
        Perform migrate to latest plan version on a Subscription

        Args:
          subscription_migration_time: When to migrate the subscription: IMMEDIATE or END_OF_BILLING_PERIOD

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/api/v1/subscriptions/{id}/migrate",
            body=await async_maybe_transform(
                {"subscription_migration_time": subscription_migration_time},
                subscription_migrate_params.SubscriptionMigrateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionMigrateResponse,
        )

    async def preview(
        self,
        *,
        customer_id: str,
        plan_id: str,
        addons: Iterable[subscription_preview_params.Addon] | Omit = omit,
        applied_coupon: subscription_preview_params.AppliedCoupon | Omit = omit,
        billable_features: Iterable[subscription_preview_params.BillableFeature] | Omit = omit,
        billing_country_code: str | Omit = omit,
        billing_information: subscription_preview_params.BillingInformation | Omit = omit,
        billing_period: Literal["MONTHLY", "ANNUALLY"] | Omit = omit,
        charges: Iterable[subscription_preview_params.Charge] | Omit = omit,
        paying_customer_id: str | Omit = omit,
        resource_id: str | Omit = omit,
        schedule_strategy: Literal["END_OF_BILLING_PERIOD", "END_OF_BILLING_MONTH", "IMMEDIATE"] | Omit = omit,
        start_date: Union[str, datetime] | Omit = omit,
        trial_override_configuration: subscription_preview_params.TrialOverrideConfiguration | Omit = omit,
        unit_quantity: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionPreviewResponse:
        """
        Create a new Subscription Preview

        Args:
          customer_id: Customer ID

          plan_id: Plan ID

          start_date: Subscription start date

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/subscriptions/preview",
            body=await async_maybe_transform(
                {
                    "customer_id": customer_id,
                    "plan_id": plan_id,
                    "addons": addons,
                    "applied_coupon": applied_coupon,
                    "billable_features": billable_features,
                    "billing_country_code": billing_country_code,
                    "billing_information": billing_information,
                    "billing_period": billing_period,
                    "charges": charges,
                    "paying_customer_id": paying_customer_id,
                    "resource_id": resource_id,
                    "schedule_strategy": schedule_strategy,
                    "start_date": start_date,
                    "trial_override_configuration": trial_override_configuration,
                    "unit_quantity": unit_quantity,
                },
                subscription_preview_params.SubscriptionPreviewParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionPreviewResponse,
        )

    async def transfer(
        self,
        id: str,
        *,
        destination_resource_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriptionTransferResponse:
        """
        Perform transfer to resource on a Subscription

        Args:
          destination_resource_id: The resource ID to transfer the subscription to. The destination resource must
              belong to the same customer.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/api/v1/subscriptions/{id}/transfer",
            body=await async_maybe_transform(
                {"destination_resource_id": destination_resource_id},
                subscription_transfer_params.SubscriptionTransferParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscriptionTransferResponse,
        )


class SubscriptionsResourceWithRawResponse:
    def __init__(self, subscriptions: SubscriptionsResource) -> None:
        self._subscriptions = subscriptions

        self.create = to_raw_response_wrapper(
            subscriptions.create,
        )
        self.retrieve = to_raw_response_wrapper(
            subscriptions.retrieve,
        )
        self.list = to_raw_response_wrapper(
            subscriptions.list,
        )
        self.delegate = to_raw_response_wrapper(
            subscriptions.delegate,
        )
        self.migrate = to_raw_response_wrapper(
            subscriptions.migrate,
        )
        self.preview = to_raw_response_wrapper(
            subscriptions.preview,
        )
        self.transfer = to_raw_response_wrapper(
            subscriptions.transfer,
        )

    @cached_property
    def future_update(self) -> FutureUpdateResourceWithRawResponse:
        return FutureUpdateResourceWithRawResponse(self._subscriptions.future_update)


class AsyncSubscriptionsResourceWithRawResponse:
    def __init__(self, subscriptions: AsyncSubscriptionsResource) -> None:
        self._subscriptions = subscriptions

        self.create = async_to_raw_response_wrapper(
            subscriptions.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            subscriptions.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            subscriptions.list,
        )
        self.delegate = async_to_raw_response_wrapper(
            subscriptions.delegate,
        )
        self.migrate = async_to_raw_response_wrapper(
            subscriptions.migrate,
        )
        self.preview = async_to_raw_response_wrapper(
            subscriptions.preview,
        )
        self.transfer = async_to_raw_response_wrapper(
            subscriptions.transfer,
        )

    @cached_property
    def future_update(self) -> AsyncFutureUpdateResourceWithRawResponse:
        return AsyncFutureUpdateResourceWithRawResponse(self._subscriptions.future_update)


class SubscriptionsResourceWithStreamingResponse:
    def __init__(self, subscriptions: SubscriptionsResource) -> None:
        self._subscriptions = subscriptions

        self.create = to_streamed_response_wrapper(
            subscriptions.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            subscriptions.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            subscriptions.list,
        )
        self.delegate = to_streamed_response_wrapper(
            subscriptions.delegate,
        )
        self.migrate = to_streamed_response_wrapper(
            subscriptions.migrate,
        )
        self.preview = to_streamed_response_wrapper(
            subscriptions.preview,
        )
        self.transfer = to_streamed_response_wrapper(
            subscriptions.transfer,
        )

    @cached_property
    def future_update(self) -> FutureUpdateResourceWithStreamingResponse:
        return FutureUpdateResourceWithStreamingResponse(self._subscriptions.future_update)


class AsyncSubscriptionsResourceWithStreamingResponse:
    def __init__(self, subscriptions: AsyncSubscriptionsResource) -> None:
        self._subscriptions = subscriptions

        self.create = async_to_streamed_response_wrapper(
            subscriptions.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            subscriptions.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            subscriptions.list,
        )
        self.delegate = async_to_streamed_response_wrapper(
            subscriptions.delegate,
        )
        self.migrate = async_to_streamed_response_wrapper(
            subscriptions.migrate,
        )
        self.preview = async_to_streamed_response_wrapper(
            subscriptions.preview,
        )
        self.transfer = async_to_streamed_response_wrapper(
            subscriptions.transfer,
        )

    @cached_property
    def future_update(self) -> AsyncFutureUpdateResourceWithStreamingResponse:
        return AsyncFutureUpdateResourceWithStreamingResponse(self._subscriptions.future_update)
