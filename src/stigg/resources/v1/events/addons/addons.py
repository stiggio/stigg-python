# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
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
    addon_list_addons_params,
    addon_create_addon_params,
    addon_update_addon_params,
    addon_publish_addon_params,
)
from .....types.v1.events.addon_list_addons_response import AddonListAddonsResponse
from .....types.v1.events.addon_create_addon_response import AddonCreateAddonResponse
from .....types.v1.events.addon_update_addon_response import AddonUpdateAddonResponse
from .....types.v1.events.addon_archive_addon_response import AddonArchiveAddonResponse
from .....types.v1.events.addon_publish_addon_response import AddonPublishAddonResponse
from .....types.v1.events.addon_retrieve_addon_response import AddonRetrieveAddonResponse

__all__ = ["AddonsResource", "AsyncAddonsResource"]


class AddonsResource(SyncAPIResource):
    @cached_property
    def draft(self) -> DraftResource:
        return DraftResource(self._client)

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

    def archive_addon(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AddonArchiveAddonResponse:
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
            cast_to=AddonArchiveAddonResponse,
        )

    def create_addon(
        self,
        *,
        id: str,
        display_name: str,
        product_id: str,
        billing_id: str | Omit = omit,
        description: str | Omit = omit,
        max_quantity: int | Omit = omit,
        metadata: Dict[str, str] | Omit = omit,
        pricing_type: Literal["FREE", "PAID", "CUSTOM"] | Omit = omit,
        status: Literal["DRAFT", "PUBLISHED", "ARCHIVED"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AddonCreateAddonResponse:
        """
        Creates a new addon in draft status, associated with a specific product.

        Args:
          id: The unique identifier for the entity

          display_name: The display name of the package

          product_id: The product ID to associate the addon with

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
                addon_create_addon_params.AddonCreateAddonParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AddonCreateAddonResponse,
        )

    def list_addons(
        self,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        created_at: addon_list_addons_params.CreatedAt | Omit = omit,
        limit: int | Omit = omit,
        product_id: str | Omit = omit,
        status: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncMyCursorIDPage[AddonListAddonsResponse]:
        """
        Retrieves a paginated list of addons in the environment.

        Args:
          after: Return items that come after this cursor

          before: Return items that come before this cursor

          created_at: Filter by creation date using range operators: gt, gte, lt, lte

          limit: Maximum number of items to return

          product_id: Filter by product ID

          status: Filter by addon status. Supports comma-separated values for multiple statuses

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/v1/addons",
            page=SyncMyCursorIDPage[AddonListAddonsResponse],
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
                    addon_list_addons_params.AddonListAddonsParams,
                ),
            ),
            model=AddonListAddonsResponse,
        )

    def publish_addon(
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
    ) -> AddonPublishAddonResponse:
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
            body=maybe_transform(
                {"migration_type": migration_type}, addon_publish_addon_params.AddonPublishAddonParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AddonPublishAddonResponse,
        )

    def retrieve_addon(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AddonRetrieveAddonResponse:
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
            cast_to=AddonRetrieveAddonResponse,
        )

    def update_addon(
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
    ) -> AddonUpdateAddonResponse:
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
                addon_update_addon_params.AddonUpdateAddonParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AddonUpdateAddonResponse,
        )


class AsyncAddonsResource(AsyncAPIResource):
    @cached_property
    def draft(self) -> AsyncDraftResource:
        return AsyncDraftResource(self._client)

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

    async def archive_addon(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AddonArchiveAddonResponse:
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
            cast_to=AddonArchiveAddonResponse,
        )

    async def create_addon(
        self,
        *,
        id: str,
        display_name: str,
        product_id: str,
        billing_id: str | Omit = omit,
        description: str | Omit = omit,
        max_quantity: int | Omit = omit,
        metadata: Dict[str, str] | Omit = omit,
        pricing_type: Literal["FREE", "PAID", "CUSTOM"] | Omit = omit,
        status: Literal["DRAFT", "PUBLISHED", "ARCHIVED"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AddonCreateAddonResponse:
        """
        Creates a new addon in draft status, associated with a specific product.

        Args:
          id: The unique identifier for the entity

          display_name: The display name of the package

          product_id: The product ID to associate the addon with

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
                addon_create_addon_params.AddonCreateAddonParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AddonCreateAddonResponse,
        )

    def list_addons(
        self,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        created_at: addon_list_addons_params.CreatedAt | Omit = omit,
        limit: int | Omit = omit,
        product_id: str | Omit = omit,
        status: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[AddonListAddonsResponse, AsyncMyCursorIDPage[AddonListAddonsResponse]]:
        """
        Retrieves a paginated list of addons in the environment.

        Args:
          after: Return items that come after this cursor

          before: Return items that come before this cursor

          created_at: Filter by creation date using range operators: gt, gte, lt, lte

          limit: Maximum number of items to return

          product_id: Filter by product ID

          status: Filter by addon status. Supports comma-separated values for multiple statuses

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/v1/addons",
            page=AsyncMyCursorIDPage[AddonListAddonsResponse],
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
                    addon_list_addons_params.AddonListAddonsParams,
                ),
            ),
            model=AddonListAddonsResponse,
        )

    async def publish_addon(
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
    ) -> AddonPublishAddonResponse:
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
                {"migration_type": migration_type}, addon_publish_addon_params.AddonPublishAddonParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AddonPublishAddonResponse,
        )

    async def retrieve_addon(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AddonRetrieveAddonResponse:
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
            cast_to=AddonRetrieveAddonResponse,
        )

    async def update_addon(
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
    ) -> AddonUpdateAddonResponse:
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
                addon_update_addon_params.AddonUpdateAddonParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AddonUpdateAddonResponse,
        )


class AddonsResourceWithRawResponse:
    def __init__(self, addons: AddonsResource) -> None:
        self._addons = addons

        self.archive_addon = to_raw_response_wrapper(
            addons.archive_addon,
        )
        self.create_addon = to_raw_response_wrapper(
            addons.create_addon,
        )
        self.list_addons = to_raw_response_wrapper(
            addons.list_addons,
        )
        self.publish_addon = to_raw_response_wrapper(
            addons.publish_addon,
        )
        self.retrieve_addon = to_raw_response_wrapper(
            addons.retrieve_addon,
        )
        self.update_addon = to_raw_response_wrapper(
            addons.update_addon,
        )

    @cached_property
    def draft(self) -> DraftResourceWithRawResponse:
        return DraftResourceWithRawResponse(self._addons.draft)


class AsyncAddonsResourceWithRawResponse:
    def __init__(self, addons: AsyncAddonsResource) -> None:
        self._addons = addons

        self.archive_addon = async_to_raw_response_wrapper(
            addons.archive_addon,
        )
        self.create_addon = async_to_raw_response_wrapper(
            addons.create_addon,
        )
        self.list_addons = async_to_raw_response_wrapper(
            addons.list_addons,
        )
        self.publish_addon = async_to_raw_response_wrapper(
            addons.publish_addon,
        )
        self.retrieve_addon = async_to_raw_response_wrapper(
            addons.retrieve_addon,
        )
        self.update_addon = async_to_raw_response_wrapper(
            addons.update_addon,
        )

    @cached_property
    def draft(self) -> AsyncDraftResourceWithRawResponse:
        return AsyncDraftResourceWithRawResponse(self._addons.draft)


class AddonsResourceWithStreamingResponse:
    def __init__(self, addons: AddonsResource) -> None:
        self._addons = addons

        self.archive_addon = to_streamed_response_wrapper(
            addons.archive_addon,
        )
        self.create_addon = to_streamed_response_wrapper(
            addons.create_addon,
        )
        self.list_addons = to_streamed_response_wrapper(
            addons.list_addons,
        )
        self.publish_addon = to_streamed_response_wrapper(
            addons.publish_addon,
        )
        self.retrieve_addon = to_streamed_response_wrapper(
            addons.retrieve_addon,
        )
        self.update_addon = to_streamed_response_wrapper(
            addons.update_addon,
        )

    @cached_property
    def draft(self) -> DraftResourceWithStreamingResponse:
        return DraftResourceWithStreamingResponse(self._addons.draft)


class AsyncAddonsResourceWithStreamingResponse:
    def __init__(self, addons: AsyncAddonsResource) -> None:
        self._addons = addons

        self.archive_addon = async_to_streamed_response_wrapper(
            addons.archive_addon,
        )
        self.create_addon = async_to_streamed_response_wrapper(
            addons.create_addon,
        )
        self.list_addons = async_to_streamed_response_wrapper(
            addons.list_addons,
        )
        self.publish_addon = async_to_streamed_response_wrapper(
            addons.publish_addon,
        )
        self.retrieve_addon = async_to_streamed_response_wrapper(
            addons.retrieve_addon,
        )
        self.update_addon = async_to_streamed_response_wrapper(
            addons.update_addon,
        )

    @cached_property
    def draft(self) -> AsyncDraftResourceWithStreamingResponse:
        return AsyncDraftResourceWithStreamingResponse(self._addons.draft)
