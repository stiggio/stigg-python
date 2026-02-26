# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ...types.v1 import (
    product_list_products_params,
    product_create_product_params,
    product_update_product_params,
    product_duplicate_product_params,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncMyCursorIDPage, AsyncMyCursorIDPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.v1.product import Product
from ...types.v1.product_list_products_response import ProductListProductsResponse

__all__ = ["ProductsResource", "AsyncProductsResource"]


class ProductsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ProductsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stiggio/stigg-python#accessing-raw-response-data-eg-headers
        """
        return ProductsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProductsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stiggio/stigg-python#with_streaming_response
        """
        return ProductsResourceWithStreamingResponse(self)

    def archive_product(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Product:
        """Archives a product, preventing new subscriptions.

        All plans and addons are
        archived.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/api/v1/products/{id}/archive",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Product,
        )

    def create_product(
        self,
        *,
        id: str,
        description: Optional[str] | Omit = omit,
        display_name: str | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        multiple_subscriptions: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Product:
        """
        Creates a new product.

        Args:
          id: The unique identifier for the entity

          description: Description of the product

          display_name: Display name of the product

          metadata: Additional metadata for the product

          multiple_subscriptions: Indicates if multiple subscriptions to this product are allowed

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/products",
            body=maybe_transform(
                {
                    "id": id,
                    "description": description,
                    "display_name": display_name,
                    "metadata": metadata,
                    "multiple_subscriptions": multiple_subscriptions,
                },
                product_create_product_params.ProductCreateProductParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Product,
        )

    def duplicate_product(
        self,
        path_id: str,
        *,
        body_id: str,
        description: Optional[str] | Omit = omit,
        display_name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Product:
        """
        Duplicates an existing product, including its plans, addons, and configuration.

        Args:
          body_id: The unique identifier for the entity

          description: Description of the product

          display_name: Display name of the product

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        return self._post(
            f"/api/v1/products/{path_id}/duplicate",
            body=maybe_transform(
                {
                    "body_id": body_id,
                    "description": description,
                    "display_name": display_name,
                },
                product_duplicate_product_params.ProductDuplicateProductParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Product,
        )

    def list_products(
        self,
        *,
        id: str | Omit = omit,
        after: str | Omit = omit,
        before: str | Omit = omit,
        created_at: product_list_products_params.CreatedAt | Omit = omit,
        limit: int | Omit = omit,
        status: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncMyCursorIDPage[ProductListProductsResponse]:
        """
        Retrieves a paginated list of products in the environment.

        Args:
          id: Filter by entity ID

          after: Return items that come after this cursor

          before: Return items that come before this cursor

          created_at: Filter by creation date using range operators: gt, gte, lt, lte

          limit: Maximum number of items to return

          status: Filter by product status. Supports comma-separated values for multiple statuses

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/v1/products",
            page=SyncMyCursorIDPage[ProductListProductsResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "after": after,
                        "before": before,
                        "created_at": created_at,
                        "limit": limit,
                        "status": status,
                    },
                    product_list_products_params.ProductListProductsParams,
                ),
            ),
            model=ProductListProductsResponse,
        )

    def unarchive_product(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Product:
        """
        Restores an archived product, allowing new subscriptions to be created.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/api/v1/products/{id}/unarchive",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Product,
        )

    def update_product(
        self,
        id: str,
        *,
        description: Optional[str] | Omit = omit,
        display_name: str | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        multiple_subscriptions: bool | Omit = omit,
        product_settings: product_update_product_params.ProductSettings | Omit = omit,
        usage_reset_cutoff_rule: product_update_product_params.UsageResetCutoffRule | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Product:
        """
        Updates an existing product's properties such as display name, description, and
        metadata.

        Args:
          description: Description of the product

          display_name: Display name of the product

          metadata: Additional metadata for the product

          multiple_subscriptions: Indicates if multiple subscriptions to this product are allowed

          usage_reset_cutoff_rule: Rule defining when usage resets upon subscription update.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/api/v1/products/{id}",
            body=maybe_transform(
                {
                    "description": description,
                    "display_name": display_name,
                    "metadata": metadata,
                    "multiple_subscriptions": multiple_subscriptions,
                    "product_settings": product_settings,
                    "usage_reset_cutoff_rule": usage_reset_cutoff_rule,
                },
                product_update_product_params.ProductUpdateProductParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Product,
        )


class AsyncProductsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncProductsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stiggio/stigg-python#accessing-raw-response-data-eg-headers
        """
        return AsyncProductsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProductsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stiggio/stigg-python#with_streaming_response
        """
        return AsyncProductsResourceWithStreamingResponse(self)

    async def archive_product(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Product:
        """Archives a product, preventing new subscriptions.

        All plans and addons are
        archived.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/api/v1/products/{id}/archive",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Product,
        )

    async def create_product(
        self,
        *,
        id: str,
        description: Optional[str] | Omit = omit,
        display_name: str | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        multiple_subscriptions: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Product:
        """
        Creates a new product.

        Args:
          id: The unique identifier for the entity

          description: Description of the product

          display_name: Display name of the product

          metadata: Additional metadata for the product

          multiple_subscriptions: Indicates if multiple subscriptions to this product are allowed

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/products",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "description": description,
                    "display_name": display_name,
                    "metadata": metadata,
                    "multiple_subscriptions": multiple_subscriptions,
                },
                product_create_product_params.ProductCreateProductParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Product,
        )

    async def duplicate_product(
        self,
        path_id: str,
        *,
        body_id: str,
        description: Optional[str] | Omit = omit,
        display_name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Product:
        """
        Duplicates an existing product, including its plans, addons, and configuration.

        Args:
          body_id: The unique identifier for the entity

          description: Description of the product

          display_name: Display name of the product

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        return await self._post(
            f"/api/v1/products/{path_id}/duplicate",
            body=await async_maybe_transform(
                {
                    "body_id": body_id,
                    "description": description,
                    "display_name": display_name,
                },
                product_duplicate_product_params.ProductDuplicateProductParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Product,
        )

    def list_products(
        self,
        *,
        id: str | Omit = omit,
        after: str | Omit = omit,
        before: str | Omit = omit,
        created_at: product_list_products_params.CreatedAt | Omit = omit,
        limit: int | Omit = omit,
        status: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ProductListProductsResponse, AsyncMyCursorIDPage[ProductListProductsResponse]]:
        """
        Retrieves a paginated list of products in the environment.

        Args:
          id: Filter by entity ID

          after: Return items that come after this cursor

          before: Return items that come before this cursor

          created_at: Filter by creation date using range operators: gt, gte, lt, lte

          limit: Maximum number of items to return

          status: Filter by product status. Supports comma-separated values for multiple statuses

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/v1/products",
            page=AsyncMyCursorIDPage[ProductListProductsResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "after": after,
                        "before": before,
                        "created_at": created_at,
                        "limit": limit,
                        "status": status,
                    },
                    product_list_products_params.ProductListProductsParams,
                ),
            ),
            model=ProductListProductsResponse,
        )

    async def unarchive_product(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Product:
        """
        Restores an archived product, allowing new subscriptions to be created.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/api/v1/products/{id}/unarchive",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Product,
        )

    async def update_product(
        self,
        id: str,
        *,
        description: Optional[str] | Omit = omit,
        display_name: str | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        multiple_subscriptions: bool | Omit = omit,
        product_settings: product_update_product_params.ProductSettings | Omit = omit,
        usage_reset_cutoff_rule: product_update_product_params.UsageResetCutoffRule | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Product:
        """
        Updates an existing product's properties such as display name, description, and
        metadata.

        Args:
          description: Description of the product

          display_name: Display name of the product

          metadata: Additional metadata for the product

          multiple_subscriptions: Indicates if multiple subscriptions to this product are allowed

          usage_reset_cutoff_rule: Rule defining when usage resets upon subscription update.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/api/v1/products/{id}",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "display_name": display_name,
                    "metadata": metadata,
                    "multiple_subscriptions": multiple_subscriptions,
                    "product_settings": product_settings,
                    "usage_reset_cutoff_rule": usage_reset_cutoff_rule,
                },
                product_update_product_params.ProductUpdateProductParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Product,
        )


class ProductsResourceWithRawResponse:
    def __init__(self, products: ProductsResource) -> None:
        self._products = products

        self.archive_product = to_raw_response_wrapper(
            products.archive_product,
        )
        self.create_product = to_raw_response_wrapper(
            products.create_product,
        )
        self.duplicate_product = to_raw_response_wrapper(
            products.duplicate_product,
        )
        self.list_products = to_raw_response_wrapper(
            products.list_products,
        )
        self.unarchive_product = to_raw_response_wrapper(
            products.unarchive_product,
        )
        self.update_product = to_raw_response_wrapper(
            products.update_product,
        )


class AsyncProductsResourceWithRawResponse:
    def __init__(self, products: AsyncProductsResource) -> None:
        self._products = products

        self.archive_product = async_to_raw_response_wrapper(
            products.archive_product,
        )
        self.create_product = async_to_raw_response_wrapper(
            products.create_product,
        )
        self.duplicate_product = async_to_raw_response_wrapper(
            products.duplicate_product,
        )
        self.list_products = async_to_raw_response_wrapper(
            products.list_products,
        )
        self.unarchive_product = async_to_raw_response_wrapper(
            products.unarchive_product,
        )
        self.update_product = async_to_raw_response_wrapper(
            products.update_product,
        )


class ProductsResourceWithStreamingResponse:
    def __init__(self, products: ProductsResource) -> None:
        self._products = products

        self.archive_product = to_streamed_response_wrapper(
            products.archive_product,
        )
        self.create_product = to_streamed_response_wrapper(
            products.create_product,
        )
        self.duplicate_product = to_streamed_response_wrapper(
            products.duplicate_product,
        )
        self.list_products = to_streamed_response_wrapper(
            products.list_products,
        )
        self.unarchive_product = to_streamed_response_wrapper(
            products.unarchive_product,
        )
        self.update_product = to_streamed_response_wrapper(
            products.update_product,
        )


class AsyncProductsResourceWithStreamingResponse:
    def __init__(self, products: AsyncProductsResource) -> None:
        self._products = products

        self.archive_product = async_to_streamed_response_wrapper(
            products.archive_product,
        )
        self.create_product = async_to_streamed_response_wrapper(
            products.create_product,
        )
        self.duplicate_product = async_to_streamed_response_wrapper(
            products.duplicate_product,
        )
        self.list_products = async_to_streamed_response_wrapper(
            products.list_products,
        )
        self.unarchive_product = async_to_streamed_response_wrapper(
            products.unarchive_product,
        )
        self.update_product = async_to_streamed_response_wrapper(
            products.update_product,
        )
