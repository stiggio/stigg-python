# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncMyCursorIDPage, AsyncMyCursorIDPage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.v1.events import plan_list_params, plan_create_params
from ....types.v1.events.plan_list_response import PlanListResponse
from ....types.v1.events.plan_create_response import PlanCreateResponse
from ....types.v1.events.plan_retrieve_response import PlanRetrieveResponse

__all__ = ["PlansResource", "AsyncPlansResource"]


class PlansResource(SyncAPIResource):
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
    ) -> PlanCreateResponse:
        """
        Creates a new plan in draft status.

        Args:
          id: The unique identifier for the entity

          display_name: The display name of the package

          product_id: The product ID to associate the plan with

          billing_id: The unique identifier for the entity in the billing provider

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
            cast_to=PlanCreateResponse,
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
    ) -> PlanRetrieveResponse:
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
            cast_to=PlanRetrieveResponse,
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


class AsyncPlansResource(AsyncAPIResource):
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
    ) -> PlanCreateResponse:
        """
        Creates a new plan in draft status.

        Args:
          id: The unique identifier for the entity

          display_name: The display name of the package

          product_id: The product ID to associate the plan with

          billing_id: The unique identifier for the entity in the billing provider

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
            cast_to=PlanCreateResponse,
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
    ) -> PlanRetrieveResponse:
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
            cast_to=PlanRetrieveResponse,
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


class PlansResourceWithRawResponse:
    def __init__(self, plans: PlansResource) -> None:
        self._plans = plans

        self.create = to_raw_response_wrapper(
            plans.create,
        )
        self.retrieve = to_raw_response_wrapper(
            plans.retrieve,
        )
        self.list = to_raw_response_wrapper(
            plans.list,
        )


class AsyncPlansResourceWithRawResponse:
    def __init__(self, plans: AsyncPlansResource) -> None:
        self._plans = plans

        self.create = async_to_raw_response_wrapper(
            plans.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            plans.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            plans.list,
        )


class PlansResourceWithStreamingResponse:
    def __init__(self, plans: PlansResource) -> None:
        self._plans = plans

        self.create = to_streamed_response_wrapper(
            plans.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            plans.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            plans.list,
        )


class AsyncPlansResourceWithStreamingResponse:
    def __init__(self, plans: AsyncPlansResource) -> None:
        self._plans = plans

        self.create = async_to_streamed_response_wrapper(
            plans.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            plans.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            plans.list,
        )
