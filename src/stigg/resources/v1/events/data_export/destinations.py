# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ....._utils import path_template, maybe_transform, strip_not_given, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.v1.events.data_export import destination_create_params, destination_update_selection_params
from .....types.v1.events.data_export.destination_create_response import DestinationCreateResponse
from .....types.v1.events.data_export.destination_delete_response import DestinationDeleteResponse
from .....types.v1.events.data_export.destination_update_selection_response import DestinationUpdateSelectionResponse

__all__ = ["DestinationsResource", "AsyncDestinationsResource"]


class DestinationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DestinationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stiggio/stigg-python#accessing-raw-response-data-eg-headers
        """
        return DestinationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DestinationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stiggio/stigg-python#with_streaming_response
        """
        return DestinationsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        destination_id: str,
        destination_type: str,
        enabled_models: SequenceNotStr[str] | Omit = omit,
        x_account_id: str | Omit = omit,
        x_environment_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DestinationCreateResponse:
        """
        Register a destination on the environment's DATA_EXPORT integration.
        Lazy-creates the integration row + provider recipient on first call. Idempotent
        on destinationId.

        Args:
          destination_id: The provider destination ID returned by the embedded SDK on connect

          destination_type: The destination type (e.g. snowflake, bigquery)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "X-ACCOUNT-ID": x_account_id,
                    "X-ENVIRONMENT-ID": x_environment_id,
                }
            ),
            **(extra_headers or {}),
        }
        return self._post(
            "/api/v1/data-export/destinations",
            body=maybe_transform(
                {
                    "destination_id": destination_id,
                    "destination_type": destination_type,
                    "enabled_models": enabled_models,
                },
                destination_create_params.DestinationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DestinationCreateResponse,
        )

    def delete(
        self,
        destination_id: str,
        *,
        x_account_id: str | Omit = omit,
        x_environment_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DestinationDeleteResponse:
        """
        Disconnect a destination: stops the provider sync (deletes the provider
        destination) and removes it from the DATA_EXPORT integration. Non-destructive —
        the warehouse table is left intact. Idempotent.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not destination_id:
            raise ValueError(f"Expected a non-empty value for `destination_id` but received {destination_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "X-ACCOUNT-ID": x_account_id,
                    "X-ENVIRONMENT-ID": x_environment_id,
                }
            ),
            **(extra_headers or {}),
        }
        return self._delete(
            path_template("/api/v1/data-export/destinations/{destination_id}", destination_id=destination_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DestinationDeleteResponse,
        )

    def update_selection(
        self,
        destination_id: str,
        *,
        enabled_models: SequenceNotStr[str],
        integration_id: str,
        x_account_id: str | Omit = omit,
        x_environment_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DestinationUpdateSelectionResponse:
        """Update a destination's entity selection.

        Pushes the new enabled_models to the
        provider first, then persists the selection. Applies on the next scheduled
        transfer.

        Args:
          integration_id: Target integration row hosting the destination

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not destination_id:
            raise ValueError(f"Expected a non-empty value for `destination_id` but received {destination_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "X-ACCOUNT-ID": x_account_id,
                    "X-ENVIRONMENT-ID": x_environment_id,
                }
            ),
            **(extra_headers or {}),
        }
        return self._patch(
            path_template("/api/v1/data-export/destinations/{destination_id}", destination_id=destination_id),
            body=maybe_transform(
                {
                    "enabled_models": enabled_models,
                    "integration_id": integration_id,
                },
                destination_update_selection_params.DestinationUpdateSelectionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DestinationUpdateSelectionResponse,
        )


class AsyncDestinationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDestinationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stiggio/stigg-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDestinationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDestinationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stiggio/stigg-python#with_streaming_response
        """
        return AsyncDestinationsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        destination_id: str,
        destination_type: str,
        enabled_models: SequenceNotStr[str] | Omit = omit,
        x_account_id: str | Omit = omit,
        x_environment_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DestinationCreateResponse:
        """
        Register a destination on the environment's DATA_EXPORT integration.
        Lazy-creates the integration row + provider recipient on first call. Idempotent
        on destinationId.

        Args:
          destination_id: The provider destination ID returned by the embedded SDK on connect

          destination_type: The destination type (e.g. snowflake, bigquery)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "X-ACCOUNT-ID": x_account_id,
                    "X-ENVIRONMENT-ID": x_environment_id,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._post(
            "/api/v1/data-export/destinations",
            body=await async_maybe_transform(
                {
                    "destination_id": destination_id,
                    "destination_type": destination_type,
                    "enabled_models": enabled_models,
                },
                destination_create_params.DestinationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DestinationCreateResponse,
        )

    async def delete(
        self,
        destination_id: str,
        *,
        x_account_id: str | Omit = omit,
        x_environment_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DestinationDeleteResponse:
        """
        Disconnect a destination: stops the provider sync (deletes the provider
        destination) and removes it from the DATA_EXPORT integration. Non-destructive —
        the warehouse table is left intact. Idempotent.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not destination_id:
            raise ValueError(f"Expected a non-empty value for `destination_id` but received {destination_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "X-ACCOUNT-ID": x_account_id,
                    "X-ENVIRONMENT-ID": x_environment_id,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._delete(
            path_template("/api/v1/data-export/destinations/{destination_id}", destination_id=destination_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DestinationDeleteResponse,
        )

    async def update_selection(
        self,
        destination_id: str,
        *,
        enabled_models: SequenceNotStr[str],
        integration_id: str,
        x_account_id: str | Omit = omit,
        x_environment_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DestinationUpdateSelectionResponse:
        """Update a destination's entity selection.

        Pushes the new enabled_models to the
        provider first, then persists the selection. Applies on the next scheduled
        transfer.

        Args:
          integration_id: Target integration row hosting the destination

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not destination_id:
            raise ValueError(f"Expected a non-empty value for `destination_id` but received {destination_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "X-ACCOUNT-ID": x_account_id,
                    "X-ENVIRONMENT-ID": x_environment_id,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._patch(
            path_template("/api/v1/data-export/destinations/{destination_id}", destination_id=destination_id),
            body=await async_maybe_transform(
                {
                    "enabled_models": enabled_models,
                    "integration_id": integration_id,
                },
                destination_update_selection_params.DestinationUpdateSelectionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DestinationUpdateSelectionResponse,
        )


class DestinationsResourceWithRawResponse:
    def __init__(self, destinations: DestinationsResource) -> None:
        self._destinations = destinations

        self.create = to_raw_response_wrapper(
            destinations.create,
        )
        self.delete = to_raw_response_wrapper(
            destinations.delete,
        )
        self.update_selection = to_raw_response_wrapper(
            destinations.update_selection,
        )


class AsyncDestinationsResourceWithRawResponse:
    def __init__(self, destinations: AsyncDestinationsResource) -> None:
        self._destinations = destinations

        self.create = async_to_raw_response_wrapper(
            destinations.create,
        )
        self.delete = async_to_raw_response_wrapper(
            destinations.delete,
        )
        self.update_selection = async_to_raw_response_wrapper(
            destinations.update_selection,
        )


class DestinationsResourceWithStreamingResponse:
    def __init__(self, destinations: DestinationsResource) -> None:
        self._destinations = destinations

        self.create = to_streamed_response_wrapper(
            destinations.create,
        )
        self.delete = to_streamed_response_wrapper(
            destinations.delete,
        )
        self.update_selection = to_streamed_response_wrapper(
            destinations.update_selection,
        )


class AsyncDestinationsResourceWithStreamingResponse:
    def __init__(self, destinations: AsyncDestinationsResource) -> None:
        self._destinations = destinations

        self.create = async_to_streamed_response_wrapper(
            destinations.create,
        )
        self.delete = async_to_streamed_response_wrapper(
            destinations.delete,
        )
        self.update_selection = async_to_streamed_response_wrapper(
            destinations.update_selection,
        )
