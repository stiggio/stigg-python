# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ....._utils import maybe_transform, async_maybe_transform
from ....._compat import cached_property
from .destinations import (
    DestinationsResource,
    AsyncDestinationsResource,
    DestinationsResourceWithRawResponse,
    AsyncDestinationsResourceWithRawResponse,
    DestinationsResourceWithStreamingResponse,
    AsyncDestinationsResourceWithStreamingResponse,
)
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.v1.events import data_export_trigger_sync_params, data_export_mint_scoped_token_params
from .....types.v1.events.data_export_trigger_sync_response import DataExportTriggerSyncResponse
from .....types.v1.events.data_export_mint_scoped_token_response import DataExportMintScopedTokenResponse

__all__ = ["DataExportResource", "AsyncDataExportResource"]


class DataExportResource(SyncAPIResource):
    @cached_property
    def destinations(self) -> DestinationsResource:
        return DestinationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> DataExportResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stiggio/stigg-python#accessing-raw-response-data-eg-headers
        """
        return DataExportResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DataExportResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stiggio/stigg-python#with_streaming_response
        """
        return DataExportResourceWithStreamingResponse(self)

    def mint_scoped_token(
        self,
        *,
        application_origin: str,
        destination_type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DataExportMintScopedTokenResponse:
        """Mint a scoped JWT for the FE embedded SDK.

        Lazy-creates the DATA_EXPORT
        integration if needed.

        Args:
          application_origin: FE origin the resulting JWT is bound to (provider-side anti-fraud)

          destination_type: Pin the token to a specific warehouse connect flow

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/data-export/scoped-token",
            body=maybe_transform(
                {
                    "application_origin": application_origin,
                    "destination_type": destination_type,
                },
                data_export_mint_scoped_token_params.DataExportMintScopedTokenParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataExportMintScopedTokenResponse,
        )

    def trigger_sync(
        self,
        *,
        destination_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DataExportTriggerSyncResponse:
        """
        Trigger a sync for one destination or all destinations under the provider
        entity.

        Args:
          destination_id: Provider destination ID to sync. Omit to sync all destinations.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/data-export/sync",
            body=maybe_transform(
                {"destination_id": destination_id}, data_export_trigger_sync_params.DataExportTriggerSyncParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataExportTriggerSyncResponse,
        )


class AsyncDataExportResource(AsyncAPIResource):
    @cached_property
    def destinations(self) -> AsyncDestinationsResource:
        return AsyncDestinationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDataExportResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stiggio/stigg-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDataExportResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDataExportResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stiggio/stigg-python#with_streaming_response
        """
        return AsyncDataExportResourceWithStreamingResponse(self)

    async def mint_scoped_token(
        self,
        *,
        application_origin: str,
        destination_type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DataExportMintScopedTokenResponse:
        """Mint a scoped JWT for the FE embedded SDK.

        Lazy-creates the DATA_EXPORT
        integration if needed.

        Args:
          application_origin: FE origin the resulting JWT is bound to (provider-side anti-fraud)

          destination_type: Pin the token to a specific warehouse connect flow

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/data-export/scoped-token",
            body=await async_maybe_transform(
                {
                    "application_origin": application_origin,
                    "destination_type": destination_type,
                },
                data_export_mint_scoped_token_params.DataExportMintScopedTokenParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataExportMintScopedTokenResponse,
        )

    async def trigger_sync(
        self,
        *,
        destination_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DataExportTriggerSyncResponse:
        """
        Trigger a sync for one destination or all destinations under the provider
        entity.

        Args:
          destination_id: Provider destination ID to sync. Omit to sync all destinations.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/data-export/sync",
            body=await async_maybe_transform(
                {"destination_id": destination_id}, data_export_trigger_sync_params.DataExportTriggerSyncParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataExportTriggerSyncResponse,
        )


class DataExportResourceWithRawResponse:
    def __init__(self, data_export: DataExportResource) -> None:
        self._data_export = data_export

        self.mint_scoped_token = to_raw_response_wrapper(
            data_export.mint_scoped_token,
        )
        self.trigger_sync = to_raw_response_wrapper(
            data_export.trigger_sync,
        )

    @cached_property
    def destinations(self) -> DestinationsResourceWithRawResponse:
        return DestinationsResourceWithRawResponse(self._data_export.destinations)


class AsyncDataExportResourceWithRawResponse:
    def __init__(self, data_export: AsyncDataExportResource) -> None:
        self._data_export = data_export

        self.mint_scoped_token = async_to_raw_response_wrapper(
            data_export.mint_scoped_token,
        )
        self.trigger_sync = async_to_raw_response_wrapper(
            data_export.trigger_sync,
        )

    @cached_property
    def destinations(self) -> AsyncDestinationsResourceWithRawResponse:
        return AsyncDestinationsResourceWithRawResponse(self._data_export.destinations)


class DataExportResourceWithStreamingResponse:
    def __init__(self, data_export: DataExportResource) -> None:
        self._data_export = data_export

        self.mint_scoped_token = to_streamed_response_wrapper(
            data_export.mint_scoped_token,
        )
        self.trigger_sync = to_streamed_response_wrapper(
            data_export.trigger_sync,
        )

    @cached_property
    def destinations(self) -> DestinationsResourceWithStreamingResponse:
        return DestinationsResourceWithStreamingResponse(self._data_export.destinations)


class AsyncDataExportResourceWithStreamingResponse:
    def __init__(self, data_export: AsyncDataExportResource) -> None:
        self._data_export = data_export

        self.mint_scoped_token = async_to_streamed_response_wrapper(
            data_export.mint_scoped_token,
        )
        self.trigger_sync = async_to_streamed_response_wrapper(
            data_export.trigger_sync,
        )

    @cached_property
    def destinations(self) -> AsyncDestinationsResourceWithStreamingResponse:
        return AsyncDestinationsResourceWithStreamingResponse(self._data_export.destinations)
