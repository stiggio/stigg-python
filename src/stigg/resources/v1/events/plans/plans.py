# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Literal

import httpx

from .draft import (
    DraftResource,
    AsyncDraftResource,
    DraftResourceWithRawResponse,
    AsyncDraftResourceWithRawResponse,
    DraftResourceWithStreamingResponse,
    AsyncDraftResourceWithStreamingResponse,
)
from ....._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ....._utils import maybe_transform, async_maybe_transform
from ....._compat import cached_property
from .entitlements import (
    EntitlementsResource,
    AsyncEntitlementsResource,
    EntitlementsResourceWithRawResponse,
    AsyncEntitlementsResourceWithRawResponse,
    EntitlementsResourceWithStreamingResponse,
    AsyncEntitlementsResourceWithStreamingResponse,
)
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .....pagination import SyncMyCursorIDPage, AsyncMyCursorIDPage
from ....._base_client import AsyncPaginator, make_request_options
from .....types.v1.events import (
    plan_list_params,
    plan_create_params,
    plan_update_params,
    plan_publish_params,
    plan_set_pricing_params,
)
from .....types.v1.events.plan import Plan
from .....types.v1.events.plan_list_response import PlanListResponse
from .....types.v1.events.plan_publish_response import PlanPublishResponse
from .....types.v1.events.set_package_pricing_response import SetPackagePricingResponse

__all__ = ["PlansResource", "AsyncPlansResource"]


class PlansResource(SyncAPIResource):
    @cached_property
    def draft(self) -> DraftResource:
        return DraftResource(self._client)

    @cached_property
    def entitlements(self) -> EntitlementsResource:
        return EntitlementsResource(self._client)

    @cached_property
    def with_raw_response(self) -> PlansResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stiggio/stigg-python#accessing-raw-response-data-eg-headers
        """
        return PlansResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PlansResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stiggio/stigg-python#with_streaming_response
        """
        return PlansResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        id: str,
        display_name: str,
        product_id: str,
        billing_id: Optional[str] | Omit = omit,
        default_trial_config: Optional[plan_create_params.DefaultTrialConfig] | Omit = omit,
        description: Optional[str] | Omit = omit,
        metadata: Dict[str, str] | Omit = omit,
        parent_plan_id: Optional[str] | Omit = omit,
        pricing_type: Optional[Literal["FREE", "PAID", "CUSTOM"]] | Omit = omit,
        status: Literal["DRAFT", "PUBLISHED", "ARCHIVED"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Plan:
        """
        Creates a new plan in draft status.

        Args:
          id: The unique identifier for the entity

          display_name: The display name of the package

          product_id: The product ID to associate the plan with

          billing_id: The unique identifier for the entity in the billing provider

          default_trial_config: Default trial configuration for the plan

          description: The description of the package

          metadata: Metadata associated with the entity

          parent_plan_id: The ID of the parent plan, if applicable

          pricing_type: The pricing type of the package

          status: The status of the package

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/plans",
            body=maybe_transform(
                {
                    "id": id,
                    "display_name": display_name,
                    "product_id": product_id,
                    "billing_id": billing_id,
                    "default_trial_config": default_trial_config,
                    "description": description,
                    "metadata": metadata,
                    "parent_plan_id": parent_plan_id,
                    "pricing_type": pricing_type,
                    "status": status,
                },
                plan_create_params.PlanCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Plan,
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
    ) -> Plan:
        """
        Retrieves a plan by its unique identifier, including entitlements and pricing
        details.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/api/v1/plans/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Plan,
        )

    def update(
        self,
        id: str,
        *,
        billing_id: Optional[str] | Omit = omit,
        compatible_addon_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        default_trial_config: Optional[plan_update_params.DefaultTrialConfig] | Omit = omit,
        description: Optional[str] | Omit = omit,
        display_name: str | Omit = omit,
        metadata: Dict[str, str] | Omit = omit,
        parent_plan_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Plan:
        """
        Updates an existing plan's properties such as display name, description, and
        metadata.

        Args:
          billing_id: The unique identifier for the entity in the billing provider

          default_trial_config: Default trial configuration for the plan

          description: The description of the package

          display_name: The display name of the package

          metadata: Metadata associated with the entity

          parent_plan_id: The ID of the parent plan, if applicable

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/api/v1/plans/{id}",
            body=maybe_transform(
                {
                    "billing_id": billing_id,
                    "compatible_addon_ids": compatible_addon_ids,
                    "default_trial_config": default_trial_config,
                    "description": description,
                    "display_name": display_name,
                    "metadata": metadata,
                    "parent_plan_id": parent_plan_id,
                },
                plan_update_params.PlanUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Plan,
        )

    def list(
        self,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        created_at: plan_list_params.CreatedAt | Omit = omit,
        limit: int | Omit = omit,
        product_id: str | Omit = omit,
        status: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncMyCursorIDPage[PlanListResponse]:
        """
        Retrieves a paginated list of plans in the environment.

        Args:
          after: Return items that come after this cursor

          before: Return items that come before this cursor

          created_at: Filter by creation date using range operators: gt, gte, lt, lte

          limit: Maximum number of items to return

          product_id: Filter by product ID

          status: Filter by status. Supports comma-separated values for multiple statuses

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/v1/plans",
            page=SyncMyCursorIDPage[PlanListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "created_at": created_at,
                        "limit": limit,
                        "product_id": product_id,
                        "status": status,
                    },
                    plan_list_params.PlanListParams,
                ),
            ),
            model=PlanListResponse,
        )

    def archive(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Plan:
        """
        Archives a plan, preventing it from being used in new subscriptions.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/api/v1/plans/{id}/archive",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Plan,
        )

    def publish(
        self,
        id: str,
        *,
        migration_type: Literal["NEW_CUSTOMERS", "ALL_CUSTOMERS"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PlanPublishResponse:
        """
        Publishes a draft plan, making it available for use in subscriptions.

        Args:
          migration_type: The migration type of the package

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/api/v1/plans/{id}/publish",
            body=maybe_transform({"migration_type": migration_type}, plan_publish_params.PlanPublishParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlanPublishResponse,
        )

    def set_pricing(
        self,
        id: str,
        *,
        pricing_type: Literal["FREE", "PAID", "CUSTOM"],
        billing_id: str | Omit = omit,
        minimum_spend: Optional[Iterable[plan_set_pricing_params.MinimumSpend]] | Omit = omit,
        overage_billing_period: Literal["ON_SUBSCRIPTION_RENEWAL", "MONTHLY"] | Omit = omit,
        overage_pricing_models: Iterable[plan_set_pricing_params.OveragePricingModel] | Omit = omit,
        pricing_models: Iterable[plan_set_pricing_params.PricingModel] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SetPackagePricingResponse:
        """
        Sets the pricing configuration for a plan, including pricing models, overage
        pricing, and minimum spend.

        Args:
          pricing_type: The pricing type (FREE, PAID, or CUSTOM)

          billing_id: Deprecated: billing integration ID

          minimum_spend: Minimum spend configuration per billing period

          overage_billing_period: When overage charges are billed

          overage_pricing_models: Array of overage pricing model configurations

          pricing_models: Array of pricing model configurations

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._put(
            f"/api/v1/plans/{id}/charges",
            body=maybe_transform(
                {
                    "pricing_type": pricing_type,
                    "billing_id": billing_id,
                    "minimum_spend": minimum_spend,
                    "overage_billing_period": overage_billing_period,
                    "overage_pricing_models": overage_pricing_models,
                    "pricing_models": pricing_models,
                },
                plan_set_pricing_params.PlanSetPricingParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SetPackagePricingResponse,
        )


class AsyncPlansResource(AsyncAPIResource):
    @cached_property
    def draft(self) -> AsyncDraftResource:
        return AsyncDraftResource(self._client)

    @cached_property
    def entitlements(self) -> AsyncEntitlementsResource:
        return AsyncEntitlementsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPlansResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stiggio/stigg-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPlansResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPlansResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stiggio/stigg-python#with_streaming_response
        """
        return AsyncPlansResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        id: str,
        display_name: str,
        product_id: str,
        billing_id: Optional[str] | Omit = omit,
        default_trial_config: Optional[plan_create_params.DefaultTrialConfig] | Omit = omit,
        description: Optional[str] | Omit = omit,
        metadata: Dict[str, str] | Omit = omit,
        parent_plan_id: Optional[str] | Omit = omit,
        pricing_type: Optional[Literal["FREE", "PAID", "CUSTOM"]] | Omit = omit,
        status: Literal["DRAFT", "PUBLISHED", "ARCHIVED"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Plan:
        """
        Creates a new plan in draft status.

        Args:
          id: The unique identifier for the entity

          display_name: The display name of the package

          product_id: The product ID to associate the plan with

          billing_id: The unique identifier for the entity in the billing provider

          default_trial_config: Default trial configuration for the plan

          description: The description of the package

          metadata: Metadata associated with the entity

          parent_plan_id: The ID of the parent plan, if applicable

          pricing_type: The pricing type of the package

          status: The status of the package

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/plans",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "display_name": display_name,
                    "product_id": product_id,
                    "billing_id": billing_id,
                    "default_trial_config": default_trial_config,
                    "description": description,
                    "metadata": metadata,
                    "parent_plan_id": parent_plan_id,
                    "pricing_type": pricing_type,
                    "status": status,
                },
                plan_create_params.PlanCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Plan,
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
    ) -> Plan:
        """
        Retrieves a plan by its unique identifier, including entitlements and pricing
        details.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/api/v1/plans/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Plan,
        )

    async def update(
        self,
        id: str,
        *,
        billing_id: Optional[str] | Omit = omit,
        compatible_addon_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        default_trial_config: Optional[plan_update_params.DefaultTrialConfig] | Omit = omit,
        description: Optional[str] | Omit = omit,
        display_name: str | Omit = omit,
        metadata: Dict[str, str] | Omit = omit,
        parent_plan_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Plan:
        """
        Updates an existing plan's properties such as display name, description, and
        metadata.

        Args:
          billing_id: The unique identifier for the entity in the billing provider

          default_trial_config: Default trial configuration for the plan

          description: The description of the package

          display_name: The display name of the package

          metadata: Metadata associated with the entity

          parent_plan_id: The ID of the parent plan, if applicable

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/api/v1/plans/{id}",
            body=await async_maybe_transform(
                {
                    "billing_id": billing_id,
                    "compatible_addon_ids": compatible_addon_ids,
                    "default_trial_config": default_trial_config,
                    "description": description,
                    "display_name": display_name,
                    "metadata": metadata,
                    "parent_plan_id": parent_plan_id,
                },
                plan_update_params.PlanUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Plan,
        )

    def list(
        self,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        created_at: plan_list_params.CreatedAt | Omit = omit,
        limit: int | Omit = omit,
        product_id: str | Omit = omit,
        status: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[PlanListResponse, AsyncMyCursorIDPage[PlanListResponse]]:
        """
        Retrieves a paginated list of plans in the environment.

        Args:
          after: Return items that come after this cursor

          before: Return items that come before this cursor

          created_at: Filter by creation date using range operators: gt, gte, lt, lte

          limit: Maximum number of items to return

          product_id: Filter by product ID

          status: Filter by status. Supports comma-separated values for multiple statuses

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/v1/plans",
            page=AsyncMyCursorIDPage[PlanListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "created_at": created_at,
                        "limit": limit,
                        "product_id": product_id,
                        "status": status,
                    },
                    plan_list_params.PlanListParams,
                ),
            ),
            model=PlanListResponse,
        )

    async def archive(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Plan:
        """
        Archives a plan, preventing it from being used in new subscriptions.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/api/v1/plans/{id}/archive",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Plan,
        )

    async def publish(
        self,
        id: str,
        *,
        migration_type: Literal["NEW_CUSTOMERS", "ALL_CUSTOMERS"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PlanPublishResponse:
        """
        Publishes a draft plan, making it available for use in subscriptions.

        Args:
          migration_type: The migration type of the package

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/api/v1/plans/{id}/publish",
            body=await async_maybe_transform({"migration_type": migration_type}, plan_publish_params.PlanPublishParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlanPublishResponse,
        )

    async def set_pricing(
        self,
        id: str,
        *,
        pricing_type: Literal["FREE", "PAID", "CUSTOM"],
        billing_id: str | Omit = omit,
        minimum_spend: Optional[Iterable[plan_set_pricing_params.MinimumSpend]] | Omit = omit,
        overage_billing_period: Literal["ON_SUBSCRIPTION_RENEWAL", "MONTHLY"] | Omit = omit,
        overage_pricing_models: Iterable[plan_set_pricing_params.OveragePricingModel] | Omit = omit,
        pricing_models: Iterable[plan_set_pricing_params.PricingModel] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SetPackagePricingResponse:
        """
        Sets the pricing configuration for a plan, including pricing models, overage
        pricing, and minimum spend.

        Args:
          pricing_type: The pricing type (FREE, PAID, or CUSTOM)

          billing_id: Deprecated: billing integration ID

          minimum_spend: Minimum spend configuration per billing period

          overage_billing_period: When overage charges are billed

          overage_pricing_models: Array of overage pricing model configurations

          pricing_models: Array of pricing model configurations

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._put(
            f"/api/v1/plans/{id}/charges",
            body=await async_maybe_transform(
                {
                    "pricing_type": pricing_type,
                    "billing_id": billing_id,
                    "minimum_spend": minimum_spend,
                    "overage_billing_period": overage_billing_period,
                    "overage_pricing_models": overage_pricing_models,
                    "pricing_models": pricing_models,
                },
                plan_set_pricing_params.PlanSetPricingParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SetPackagePricingResponse,
        )


class PlansResourceWithRawResponse:
    def __init__(self, plans: PlansResource) -> None:
        self._plans = plans

        self.create = to_raw_response_wrapper(
            plans.create,
        )
        self.retrieve = to_raw_response_wrapper(
            plans.retrieve,
        )
        self.update = to_raw_response_wrapper(
            plans.update,
        )
        self.list = to_raw_response_wrapper(
            plans.list,
        )
        self.archive = to_raw_response_wrapper(
            plans.archive,
        )
        self.publish = to_raw_response_wrapper(
            plans.publish,
        )
        self.set_pricing = to_raw_response_wrapper(
            plans.set_pricing,
        )

    @cached_property
    def draft(self) -> DraftResourceWithRawResponse:
        return DraftResourceWithRawResponse(self._plans.draft)

    @cached_property
    def entitlements(self) -> EntitlementsResourceWithRawResponse:
        return EntitlementsResourceWithRawResponse(self._plans.entitlements)


class AsyncPlansResourceWithRawResponse:
    def __init__(self, plans: AsyncPlansResource) -> None:
        self._plans = plans

        self.create = async_to_raw_response_wrapper(
            plans.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            plans.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            plans.update,
        )
        self.list = async_to_raw_response_wrapper(
            plans.list,
        )
        self.archive = async_to_raw_response_wrapper(
            plans.archive,
        )
        self.publish = async_to_raw_response_wrapper(
            plans.publish,
        )
        self.set_pricing = async_to_raw_response_wrapper(
            plans.set_pricing,
        )

    @cached_property
    def draft(self) -> AsyncDraftResourceWithRawResponse:
        return AsyncDraftResourceWithRawResponse(self._plans.draft)

    @cached_property
    def entitlements(self) -> AsyncEntitlementsResourceWithRawResponse:
        return AsyncEntitlementsResourceWithRawResponse(self._plans.entitlements)


class PlansResourceWithStreamingResponse:
    def __init__(self, plans: PlansResource) -> None:
        self._plans = plans

        self.create = to_streamed_response_wrapper(
            plans.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            plans.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            plans.update,
        )
        self.list = to_streamed_response_wrapper(
            plans.list,
        )
        self.archive = to_streamed_response_wrapper(
            plans.archive,
        )
        self.publish = to_streamed_response_wrapper(
            plans.publish,
        )
        self.set_pricing = to_streamed_response_wrapper(
            plans.set_pricing,
        )

    @cached_property
    def draft(self) -> DraftResourceWithStreamingResponse:
        return DraftResourceWithStreamingResponse(self._plans.draft)

    @cached_property
    def entitlements(self) -> EntitlementsResourceWithStreamingResponse:
        return EntitlementsResourceWithStreamingResponse(self._plans.entitlements)


class AsyncPlansResourceWithStreamingResponse:
    def __init__(self, plans: AsyncPlansResource) -> None:
        self._plans = plans

        self.create = async_to_streamed_response_wrapper(
            plans.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            plans.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            plans.update,
        )
        self.list = async_to_streamed_response_wrapper(
            plans.list,
        )
        self.archive = async_to_streamed_response_wrapper(
            plans.archive,
        )
        self.publish = async_to_streamed_response_wrapper(
            plans.publish,
        )
        self.set_pricing = async_to_streamed_response_wrapper(
            plans.set_pricing,
        )

    @cached_property
    def draft(self) -> AsyncDraftResourceWithStreamingResponse:
        return AsyncDraftResourceWithStreamingResponse(self._plans.draft)

    @cached_property
    def entitlements(self) -> AsyncEntitlementsResourceWithStreamingResponse:
        return AsyncEntitlementsResourceWithStreamingResponse(self._plans.entitlements)
