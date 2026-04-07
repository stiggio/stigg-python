# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
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
from ....types.v1.customers import integration_link_params, integration_list_params, integration_update_params
from ....types.v1.customer_integration_response import CustomerIntegrationResponse
from ....types.v1.customers.integration_list_response import IntegrationListResponse

__all__ = ["IntegrationsResource", "AsyncIntegrationsResource"]


class IntegrationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IntegrationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stiggio/stigg-python#accessing-raw-response-data-eg-headers
        """
        return IntegrationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IntegrationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stiggio/stigg-python#with_streaming_response
        """
        return IntegrationsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        integration_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomerIntegrationResponse:
        """
        Retrieves a specific integration for a customer by integration ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not integration_id:
            raise ValueError(f"Expected a non-empty value for `integration_id` but received {integration_id!r}")
        return self._get(
            path_template("/api/v1/customers/{id}/integrations/{integration_id}", id=id, integration_id=integration_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerIntegrationResponse,
        )

    def update(
        self,
        integration_id: str,
        *,
        id: str,
        synced_entity_id: Optional[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomerIntegrationResponse:
        """
        Updates a customer's integration link, such as changing the synced external
        entity ID.

        Args:
          synced_entity_id: Synced entity id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not integration_id:
            raise ValueError(f"Expected a non-empty value for `integration_id` but received {integration_id!r}")
        return self._patch(
            path_template("/api/v1/customers/{id}/integrations/{integration_id}", id=id, integration_id=integration_id),
            body=maybe_transform(
                {"synced_entity_id": synced_entity_id}, integration_update_params.IntegrationUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerIntegrationResponse,
        )

    def list(
        self,
        id: str,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        limit: int | Omit = omit,
        vendor_identifier: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncMyCursorIDPage[IntegrationListResponse]:
        """
        Retrieves a paginated list of a customer's external integrations (billing, CRM,
        etc.).

        Args:
          after: Return items that come after this cursor

          before: Return items that come before this cursor

          limit: Maximum number of items to return

          vendor_identifier: Filter by vendor identifier. Supports comma-separated values for multiple
              vendors (e.g., STRIPE,HUBSPOT)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get_api_list(
            path_template("/api/v1/customers/{id}/integrations", id=id),
            page=SyncMyCursorIDPage[IntegrationListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "limit": limit,
                        "vendor_identifier": vendor_identifier,
                    },
                    integration_list_params.IntegrationListParams,
                ),
            ),
            model=IntegrationListResponse,
        )

    def link(
        self,
        path_id: str,
        *,
        body_id: str,
        synced_entity_id: str,
        vendor_identifier: Literal[
            "AUTH0",
            "ZUORA",
            "STRIPE",
            "HUBSPOT",
            "AWS_MARKETPLACE",
            "SNOWFLAKE",
            "SALESFORCE",
            "BIG_QUERY",
            "OPEN_FGA",
            "APP_STORE",
        ],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomerIntegrationResponse:
        """
        Links a customer to an external integration by specifying the vendor and
        external entity ID.

        Args:
          body_id: Integration details

          synced_entity_id: Synced entity id

          vendor_identifier: The vendor identifier of integration

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        return self._post(
            path_template("/api/v1/customers/{path_id}/integrations", path_id=path_id),
            body=maybe_transform(
                {
                    "body_id": body_id,
                    "synced_entity_id": synced_entity_id,
                    "vendor_identifier": vendor_identifier,
                },
                integration_link_params.IntegrationLinkParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerIntegrationResponse,
        )

    def unlink(
        self,
        integration_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomerIntegrationResponse:
        """
        Removes the link between a customer and an external integration.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not integration_id:
            raise ValueError(f"Expected a non-empty value for `integration_id` but received {integration_id!r}")
        return self._delete(
            path_template("/api/v1/customers/{id}/integrations/{integration_id}", id=id, integration_id=integration_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerIntegrationResponse,
        )


class AsyncIntegrationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIntegrationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stiggio/stigg-python#accessing-raw-response-data-eg-headers
        """
        return AsyncIntegrationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIntegrationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stiggio/stigg-python#with_streaming_response
        """
        return AsyncIntegrationsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        integration_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomerIntegrationResponse:
        """
        Retrieves a specific integration for a customer by integration ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not integration_id:
            raise ValueError(f"Expected a non-empty value for `integration_id` but received {integration_id!r}")
        return await self._get(
            path_template("/api/v1/customers/{id}/integrations/{integration_id}", id=id, integration_id=integration_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerIntegrationResponse,
        )

    async def update(
        self,
        integration_id: str,
        *,
        id: str,
        synced_entity_id: Optional[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomerIntegrationResponse:
        """
        Updates a customer's integration link, such as changing the synced external
        entity ID.

        Args:
          synced_entity_id: Synced entity id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not integration_id:
            raise ValueError(f"Expected a non-empty value for `integration_id` but received {integration_id!r}")
        return await self._patch(
            path_template("/api/v1/customers/{id}/integrations/{integration_id}", id=id, integration_id=integration_id),
            body=await async_maybe_transform(
                {"synced_entity_id": synced_entity_id}, integration_update_params.IntegrationUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerIntegrationResponse,
        )

    def list(
        self,
        id: str,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        limit: int | Omit = omit,
        vendor_identifier: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[IntegrationListResponse, AsyncMyCursorIDPage[IntegrationListResponse]]:
        """
        Retrieves a paginated list of a customer's external integrations (billing, CRM,
        etc.).

        Args:
          after: Return items that come after this cursor

          before: Return items that come before this cursor

          limit: Maximum number of items to return

          vendor_identifier: Filter by vendor identifier. Supports comma-separated values for multiple
              vendors (e.g., STRIPE,HUBSPOT)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get_api_list(
            path_template("/api/v1/customers/{id}/integrations", id=id),
            page=AsyncMyCursorIDPage[IntegrationListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "limit": limit,
                        "vendor_identifier": vendor_identifier,
                    },
                    integration_list_params.IntegrationListParams,
                ),
            ),
            model=IntegrationListResponse,
        )

    async def link(
        self,
        path_id: str,
        *,
        body_id: str,
        synced_entity_id: str,
        vendor_identifier: Literal[
            "AUTH0",
            "ZUORA",
            "STRIPE",
            "HUBSPOT",
            "AWS_MARKETPLACE",
            "SNOWFLAKE",
            "SALESFORCE",
            "BIG_QUERY",
            "OPEN_FGA",
            "APP_STORE",
        ],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomerIntegrationResponse:
        """
        Links a customer to an external integration by specifying the vendor and
        external entity ID.

        Args:
          body_id: Integration details

          synced_entity_id: Synced entity id

          vendor_identifier: The vendor identifier of integration

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        return await self._post(
            path_template("/api/v1/customers/{path_id}/integrations", path_id=path_id),
            body=await async_maybe_transform(
                {
                    "body_id": body_id,
                    "synced_entity_id": synced_entity_id,
                    "vendor_identifier": vendor_identifier,
                },
                integration_link_params.IntegrationLinkParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerIntegrationResponse,
        )

    async def unlink(
        self,
        integration_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomerIntegrationResponse:
        """
        Removes the link between a customer and an external integration.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not integration_id:
            raise ValueError(f"Expected a non-empty value for `integration_id` but received {integration_id!r}")
        return await self._delete(
            path_template("/api/v1/customers/{id}/integrations/{integration_id}", id=id, integration_id=integration_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerIntegrationResponse,
        )


class IntegrationsResourceWithRawResponse:
    def __init__(self, integrations: IntegrationsResource) -> None:
        self._integrations = integrations

        self.retrieve = to_raw_response_wrapper(
            integrations.retrieve,
        )
        self.update = to_raw_response_wrapper(
            integrations.update,
        )
        self.list = to_raw_response_wrapper(
            integrations.list,
        )
        self.link = to_raw_response_wrapper(
            integrations.link,
        )
        self.unlink = to_raw_response_wrapper(
            integrations.unlink,
        )


class AsyncIntegrationsResourceWithRawResponse:
    def __init__(self, integrations: AsyncIntegrationsResource) -> None:
        self._integrations = integrations

        self.retrieve = async_to_raw_response_wrapper(
            integrations.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            integrations.update,
        )
        self.list = async_to_raw_response_wrapper(
            integrations.list,
        )
        self.link = async_to_raw_response_wrapper(
            integrations.link,
        )
        self.unlink = async_to_raw_response_wrapper(
            integrations.unlink,
        )


class IntegrationsResourceWithStreamingResponse:
    def __init__(self, integrations: IntegrationsResource) -> None:
        self._integrations = integrations

        self.retrieve = to_streamed_response_wrapper(
            integrations.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            integrations.update,
        )
        self.list = to_streamed_response_wrapper(
            integrations.list,
        )
        self.link = to_streamed_response_wrapper(
            integrations.link,
        )
        self.unlink = to_streamed_response_wrapper(
            integrations.unlink,
        )


class AsyncIntegrationsResourceWithStreamingResponse:
    def __init__(self, integrations: AsyncIntegrationsResource) -> None:
        self._integrations = integrations

        self.retrieve = async_to_streamed_response_wrapper(
            integrations.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            integrations.update,
        )
        self.list = async_to_streamed_response_wrapper(
            integrations.list,
        )
        self.link = async_to_streamed_response_wrapper(
            integrations.link,
        )
        self.unlink = async_to_streamed_response_wrapper(
            integrations.unlink,
        )
