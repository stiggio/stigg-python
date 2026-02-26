# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ....types.v1 import (
    addon_list_params,
    addon_create_params,
    addon_update_params,
    addon_publish_params,
    addon_set_pricing_params,
)
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
from ....types.v1.addon import Addon
from ....types.v1.addon_list_response import AddonListResponse
from ....types.v1.addon_publish_response import AddonPublishResponse
from ....types.v1.addon_remove_draft_response import AddonRemoveDraftResponse
from ....types.v1.set_package_pricing_response import SetPackagePricingResponse

__all__ = ["AddonsResource", "AsyncAddonsResource"]


class AddonsResource(SyncAPIResource):
    @cached_property
    def entitlements(self) -> EntitlementsResource:
        return EntitlementsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AddonsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stiggio/stigg-python#accessing-raw-response-data-eg-headers
        """
        return AddonsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AddonsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stiggio/stigg-python#with_streaming_response
        """
        return AddonsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        id: str,
        display_name: str,
        product_id: str,
        billing_id: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        max_quantity: Optional[int] | Omit = omit,
        metadata: Dict[str, str] | Omit = omit,
        pricing_type: Optional[Literal["FREE", "PAID", "CUSTOM"]] | Omit = omit,
        status: Literal["DRAFT", "PUBLISHED", "ARCHIVED"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Addon:
        """
        Creates a new addon in draft status, associated with a specific product.

        Args:
          id: The unique identifier for the entity

          display_name: The display name of the package

          product_id: The product id of the package

          billing_id: The unique identifier for the entity in the billing provider

          description: The description of the package

          max_quantity: The maximum quantity of this addon that can be added to a subscription

          metadata: Metadata associated with the entity

          pricing_type: The pricing type of the package

          status: The status of the package

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/addons",
            body=maybe_transform(
                {
                    "id": id,
                    "display_name": display_name,
                    "product_id": product_id,
                    "billing_id": billing_id,
                    "description": description,
                    "max_quantity": max_quantity,
                    "metadata": metadata,
                    "pricing_type": pricing_type,
                    "status": status,
                },
                addon_create_params.AddonCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Addon,
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
    ) -> Addon:
        """
        Retrieves an addon by its unique identifier, including entitlements and pricing
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
            f"/api/v1/addons/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Addon,
        )

    def update(
        self,
        id: str,
        *,
        billing_id: Optional[str] | Omit = omit,
        dependencies: Optional[SequenceNotStr[str]] | Omit = omit,
        description: Optional[str] | Omit = omit,
        display_name: str | Omit = omit,
        max_quantity: Optional[int] | Omit = omit,
        metadata: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Addon:
        """
        Updates an existing addon's properties such as display name, description, and
        metadata.

        Args:
          billing_id: The unique identifier for the entity in the billing provider

          dependencies: List of addons the addon is dependant on

          description: The description of the package

          display_name: The display name of the package

          max_quantity: The maximum quantity of this addon that can be added to a subscription

          metadata: Metadata associated with the entity

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/api/v1/addons/{id}",
            body=maybe_transform(
                {
                    "billing_id": billing_id,
                    "dependencies": dependencies,
                    "description": description,
                    "display_name": display_name,
                    "max_quantity": max_quantity,
                    "metadata": metadata,
                },
                addon_update_params.AddonUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Addon,
        )

    def list(
        self,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        created_at: addon_list_params.CreatedAt | Omit = omit,
        limit: int | Omit = omit,
        product_id: str | Omit = omit,
        status: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncMyCursorIDPage[AddonListResponse]:
        """
        Retrieves a paginated list of addons in the environment.

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
            "/api/v1/addons",
            page=SyncMyCursorIDPage[AddonListResponse],
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
                    addon_list_params.AddonListParams,
                ),
            ),
            model=AddonListResponse,
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
    ) -> Addon:
        """
        Archives an addon, preventing it from being used in new subscriptions.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/api/v1/addons/{id}/archive",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Addon,
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
    ) -> Addon:
        """
        Creates a draft version of an existing addon for modification before publishing.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/api/v1/addons/{id}/draft",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Addon,
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
    ) -> AddonPublishResponse:
        """
        Publishes a draft addon, making it available for use in subscriptions.

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
            f"/api/v1/addons/{id}/publish",
            body=maybe_transform({"migration_type": migration_type}, addon_publish_params.AddonPublishParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AddonPublishResponse,
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
    ) -> AddonRemoveDraftResponse:
        """
        Removes a draft version of an addon.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/api/v1/addons/{id}/draft",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AddonRemoveDraftResponse,
        )

    def set_pricing(
        self,
        id: str,
        *,
        pricing_type: Literal["FREE", "PAID", "CUSTOM"],
        billing_id: str | Omit = omit,
        minimum_spend: Optional[Iterable[addon_set_pricing_params.MinimumSpend]] | Omit = omit,
        overage_billing_period: Literal["ON_SUBSCRIPTION_RENEWAL", "MONTHLY"] | Omit = omit,
        overage_pricing_models: Iterable[addon_set_pricing_params.OveragePricingModel] | Omit = omit,
        pricing_models: Iterable[addon_set_pricing_params.PricingModel] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SetPackagePricingResponse:
        """
        Sets the pricing configuration for an addon.

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
            f"/api/v1/addons/{id}/charges",
            body=maybe_transform(
                {
                    "pricing_type": pricing_type,
                    "billing_id": billing_id,
                    "minimum_spend": minimum_spend,
                    "overage_billing_period": overage_billing_period,
                    "overage_pricing_models": overage_pricing_models,
                    "pricing_models": pricing_models,
                },
                addon_set_pricing_params.AddonSetPricingParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SetPackagePricingResponse,
        )


class AsyncAddonsResource(AsyncAPIResource):
    @cached_property
    def entitlements(self) -> AsyncEntitlementsResource:
        return AsyncEntitlementsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAddonsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stiggio/stigg-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAddonsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAddonsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stiggio/stigg-python#with_streaming_response
        """
        return AsyncAddonsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        id: str,
        display_name: str,
        product_id: str,
        billing_id: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        max_quantity: Optional[int] | Omit = omit,
        metadata: Dict[str, str] | Omit = omit,
        pricing_type: Optional[Literal["FREE", "PAID", "CUSTOM"]] | Omit = omit,
        status: Literal["DRAFT", "PUBLISHED", "ARCHIVED"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Addon:
        """
        Creates a new addon in draft status, associated with a specific product.

        Args:
          id: The unique identifier for the entity

          display_name: The display name of the package

          product_id: The product id of the package

          billing_id: The unique identifier for the entity in the billing provider

          description: The description of the package

          max_quantity: The maximum quantity of this addon that can be added to a subscription

          metadata: Metadata associated with the entity

          pricing_type: The pricing type of the package

          status: The status of the package

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/addons",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "display_name": display_name,
                    "product_id": product_id,
                    "billing_id": billing_id,
                    "description": description,
                    "max_quantity": max_quantity,
                    "metadata": metadata,
                    "pricing_type": pricing_type,
                    "status": status,
                },
                addon_create_params.AddonCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Addon,
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
    ) -> Addon:
        """
        Retrieves an addon by its unique identifier, including entitlements and pricing
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
            f"/api/v1/addons/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Addon,
        )

    async def update(
        self,
        id: str,
        *,
        billing_id: Optional[str] | Omit = omit,
        dependencies: Optional[SequenceNotStr[str]] | Omit = omit,
        description: Optional[str] | Omit = omit,
        display_name: str | Omit = omit,
        max_quantity: Optional[int] | Omit = omit,
        metadata: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Addon:
        """
        Updates an existing addon's properties such as display name, description, and
        metadata.

        Args:
          billing_id: The unique identifier for the entity in the billing provider

          dependencies: List of addons the addon is dependant on

          description: The description of the package

          display_name: The display name of the package

          max_quantity: The maximum quantity of this addon that can be added to a subscription

          metadata: Metadata associated with the entity

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/api/v1/addons/{id}",
            body=await async_maybe_transform(
                {
                    "billing_id": billing_id,
                    "dependencies": dependencies,
                    "description": description,
                    "display_name": display_name,
                    "max_quantity": max_quantity,
                    "metadata": metadata,
                },
                addon_update_params.AddonUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Addon,
        )

    def list(
        self,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        created_at: addon_list_params.CreatedAt | Omit = omit,
        limit: int | Omit = omit,
        product_id: str | Omit = omit,
        status: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[AddonListResponse, AsyncMyCursorIDPage[AddonListResponse]]:
        """
        Retrieves a paginated list of addons in the environment.

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
            "/api/v1/addons",
            page=AsyncMyCursorIDPage[AddonListResponse],
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
                    addon_list_params.AddonListParams,
                ),
            ),
            model=AddonListResponse,
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
    ) -> Addon:
        """
        Archives an addon, preventing it from being used in new subscriptions.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/api/v1/addons/{id}/archive",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Addon,
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
    ) -> Addon:
        """
        Creates a draft version of an existing addon for modification before publishing.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/api/v1/addons/{id}/draft",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Addon,
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
    ) -> AddonPublishResponse:
        """
        Publishes a draft addon, making it available for use in subscriptions.

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
            f"/api/v1/addons/{id}/publish",
            body=await async_maybe_transform(
                {"migration_type": migration_type}, addon_publish_params.AddonPublishParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AddonPublishResponse,
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
    ) -> AddonRemoveDraftResponse:
        """
        Removes a draft version of an addon.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/api/v1/addons/{id}/draft",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AddonRemoveDraftResponse,
        )

    async def set_pricing(
        self,
        id: str,
        *,
        pricing_type: Literal["FREE", "PAID", "CUSTOM"],
        billing_id: str | Omit = omit,
        minimum_spend: Optional[Iterable[addon_set_pricing_params.MinimumSpend]] | Omit = omit,
        overage_billing_period: Literal["ON_SUBSCRIPTION_RENEWAL", "MONTHLY"] | Omit = omit,
        overage_pricing_models: Iterable[addon_set_pricing_params.OveragePricingModel] | Omit = omit,
        pricing_models: Iterable[addon_set_pricing_params.PricingModel] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SetPackagePricingResponse:
        """
        Sets the pricing configuration for an addon.

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
            f"/api/v1/addons/{id}/charges",
            body=await async_maybe_transform(
                {
                    "pricing_type": pricing_type,
                    "billing_id": billing_id,
                    "minimum_spend": minimum_spend,
                    "overage_billing_period": overage_billing_period,
                    "overage_pricing_models": overage_pricing_models,
                    "pricing_models": pricing_models,
                },
                addon_set_pricing_params.AddonSetPricingParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SetPackagePricingResponse,
        )


class AddonsResourceWithRawResponse:
    def __init__(self, addons: AddonsResource) -> None:
        self._addons = addons

        self.create = to_raw_response_wrapper(
            addons.create,
        )
        self.retrieve = to_raw_response_wrapper(
            addons.retrieve,
        )
        self.update = to_raw_response_wrapper(
            addons.update,
        )
        self.list = to_raw_response_wrapper(
            addons.list,
        )
        self.archive = to_raw_response_wrapper(
            addons.archive,
        )
        self.create_draft = to_raw_response_wrapper(
            addons.create_draft,
        )
        self.publish = to_raw_response_wrapper(
            addons.publish,
        )
        self.remove_draft = to_raw_response_wrapper(
            addons.remove_draft,
        )
        self.set_pricing = to_raw_response_wrapper(
            addons.set_pricing,
        )

    @cached_property
    def entitlements(self) -> EntitlementsResourceWithRawResponse:
        return EntitlementsResourceWithRawResponse(self._addons.entitlements)


class AsyncAddonsResourceWithRawResponse:
    def __init__(self, addons: AsyncAddonsResource) -> None:
        self._addons = addons

        self.create = async_to_raw_response_wrapper(
            addons.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            addons.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            addons.update,
        )
        self.list = async_to_raw_response_wrapper(
            addons.list,
        )
        self.archive = async_to_raw_response_wrapper(
            addons.archive,
        )
        self.create_draft = async_to_raw_response_wrapper(
            addons.create_draft,
        )
        self.publish = async_to_raw_response_wrapper(
            addons.publish,
        )
        self.remove_draft = async_to_raw_response_wrapper(
            addons.remove_draft,
        )
        self.set_pricing = async_to_raw_response_wrapper(
            addons.set_pricing,
        )

    @cached_property
    def entitlements(self) -> AsyncEntitlementsResourceWithRawResponse:
        return AsyncEntitlementsResourceWithRawResponse(self._addons.entitlements)


class AddonsResourceWithStreamingResponse:
    def __init__(self, addons: AddonsResource) -> None:
        self._addons = addons

        self.create = to_streamed_response_wrapper(
            addons.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            addons.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            addons.update,
        )
        self.list = to_streamed_response_wrapper(
            addons.list,
        )
        self.archive = to_streamed_response_wrapper(
            addons.archive,
        )
        self.create_draft = to_streamed_response_wrapper(
            addons.create_draft,
        )
        self.publish = to_streamed_response_wrapper(
            addons.publish,
        )
        self.remove_draft = to_streamed_response_wrapper(
            addons.remove_draft,
        )
        self.set_pricing = to_streamed_response_wrapper(
            addons.set_pricing,
        )

    @cached_property
    def entitlements(self) -> EntitlementsResourceWithStreamingResponse:
        return EntitlementsResourceWithStreamingResponse(self._addons.entitlements)


class AsyncAddonsResourceWithStreamingResponse:
    def __init__(self, addons: AsyncAddonsResource) -> None:
        self._addons = addons

        self.create = async_to_streamed_response_wrapper(
            addons.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            addons.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            addons.update,
        )
        self.list = async_to_streamed_response_wrapper(
            addons.list,
        )
        self.archive = async_to_streamed_response_wrapper(
            addons.archive,
        )
        self.create_draft = async_to_streamed_response_wrapper(
            addons.create_draft,
        )
        self.publish = async_to_streamed_response_wrapper(
            addons.publish,
        )
        self.remove_draft = async_to_streamed_response_wrapper(
            addons.remove_draft,
        )
        self.set_pricing = async_to_streamed_response_wrapper(
            addons.set_pricing,
        )

    @cached_property
    def entitlements(self) -> AsyncEntitlementsResourceWithStreamingResponse:
        return AsyncEntitlementsResourceWithStreamingResponse(self._addons.entitlements)
