# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ....types.v1 import plan_list_params, plan_create_params, plan_update_params, plan_publish_params
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .entitlements import (
    EntitlementsResource,
    AsyncEntitlementsResource,
    EntitlementsResourceWithRawResponse,
    AsyncEntitlementsResourceWithRawResponse,
    EntitlementsResourceWithStreamingResponse,
    AsyncEntitlementsResourceWithStreamingResponse,
)
from ....pagination import SyncMyCursorIDPage, AsyncMyCursorIDPage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.v1.plan import Plan
from ....types.v1.plan_list_response import PlanListResponse
from ....types.v1.plan_publish_response import PlanPublishResponse
from ....types.v1.plan_remove_draft_response import PlanRemoveDraftResponse

__all__ = ["PlansResource", "AsyncPlansResource"]


class PlansResource(SyncAPIResource):
    """Operations related to plans"""

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
            path_template("/api/v1/plans/{id}", id=id),
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
        charges: plan_update_params.Charges | Omit = omit,
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

          charges: Pricing configuration to set on the plan draft

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
            path_template("/api/v1/plans/{id}", id=id),
            body=maybe_transform(
                {
                    "billing_id": billing_id,
                    "charges": charges,
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
            path_template("/api/v1/plans/{id}/archive", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Plan,
        )

    def create_draft(
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
        Creates a draft version of an existing plan for modification before publishing.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/api/v1/plans/{id}/draft", id=id),
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
            path_template("/api/v1/plans/{id}/publish", id=id),
            body=maybe_transform({"migration_type": migration_type}, plan_publish_params.PlanPublishParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlanPublishResponse,
        )

    def remove_draft(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PlanRemoveDraftResponse:
        """
        Removes a draft version of a plan.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            path_template("/api/v1/plans/{id}/draft", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlanRemoveDraftResponse,
        )


class AsyncPlansResource(AsyncAPIResource):
    """Operations related to plans"""

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
            path_template("/api/v1/plans/{id}", id=id),
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
        charges: plan_update_params.Charges | Omit = omit,
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

          charges: Pricing configuration to set on the plan draft

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
            path_template("/api/v1/plans/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "billing_id": billing_id,
                    "charges": charges,
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
            path_template("/api/v1/plans/{id}/archive", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Plan,
        )

    async def create_draft(
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
        Creates a draft version of an existing plan for modification before publishing.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/api/v1/plans/{id}/draft", id=id),
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
            path_template("/api/v1/plans/{id}/publish", id=id),
            body=await async_maybe_transform({"migration_type": migration_type}, plan_publish_params.PlanPublishParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlanPublishResponse,
        )

    async def remove_draft(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PlanRemoveDraftResponse:
        """
        Removes a draft version of a plan.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            path_template("/api/v1/plans/{id}/draft", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlanRemoveDraftResponse,
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
        self.create_draft = to_raw_response_wrapper(
            plans.create_draft,
        )
        self.publish = to_raw_response_wrapper(
            plans.publish,
        )
        self.remove_draft = to_raw_response_wrapper(
            plans.remove_draft,
        )

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
        self.create_draft = async_to_raw_response_wrapper(
            plans.create_draft,
        )
        self.publish = async_to_raw_response_wrapper(
            plans.publish,
        )
        self.remove_draft = async_to_raw_response_wrapper(
            plans.remove_draft,
        )

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
        self.create_draft = to_streamed_response_wrapper(
            plans.create_draft,
        )
        self.publish = to_streamed_response_wrapper(
            plans.publish,
        )
        self.remove_draft = to_streamed_response_wrapper(
            plans.remove_draft,
        )

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
        self.create_draft = async_to_streamed_response_wrapper(
            plans.create_draft,
        )
        self.publish = async_to_streamed_response_wrapper(
            plans.publish,
        )
        self.remove_draft = async_to_streamed_response_wrapper(
            plans.remove_draft,
        )

    @cached_property
    def entitlements(self) -> AsyncEntitlementsResourceWithStreamingResponse:
        return AsyncEntitlementsResourceWithStreamingResponse(self._plans.entitlements)
