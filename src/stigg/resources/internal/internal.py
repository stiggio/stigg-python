# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from .beta.beta import (
    BetaResource,
    AsyncBetaResource,
    BetaResourceWithRawResponse,
    AsyncBetaResourceWithRawResponse,
    BetaResourceWithStreamingResponse,
    AsyncBetaResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["InternalResource", "AsyncInternalResource"]


class InternalResource(SyncAPIResource):
    @cached_property
    def beta(self) -> BetaResource:
        return BetaResource(self._client)

    @cached_property
    def with_raw_response(self) -> InternalResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stiggio/stigg-python#accessing-raw-response-data-eg-headers
        """
        return InternalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InternalResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stiggio/stigg-python#with_streaming_response
        """
        return InternalResourceWithStreamingResponse(self)


class AsyncInternalResource(AsyncAPIResource):
    @cached_property
    def beta(self) -> AsyncBetaResource:
        return AsyncBetaResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncInternalResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stiggio/stigg-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInternalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInternalResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stiggio/stigg-python#with_streaming_response
        """
        return AsyncInternalResourceWithStreamingResponse(self)


class InternalResourceWithRawResponse:
    def __init__(self, internal: InternalResource) -> None:
        self._internal = internal

    @cached_property
    def beta(self) -> BetaResourceWithRawResponse:
        return BetaResourceWithRawResponse(self._internal.beta)


class AsyncInternalResourceWithRawResponse:
    def __init__(self, internal: AsyncInternalResource) -> None:
        self._internal = internal

    @cached_property
    def beta(self) -> AsyncBetaResourceWithRawResponse:
        return AsyncBetaResourceWithRawResponse(self._internal.beta)


class InternalResourceWithStreamingResponse:
    def __init__(self, internal: InternalResource) -> None:
        self._internal = internal

    @cached_property
    def beta(self) -> BetaResourceWithStreamingResponse:
        return BetaResourceWithStreamingResponse(self._internal.beta)


class AsyncInternalResourceWithStreamingResponse:
    def __init__(self, internal: AsyncInternalResource) -> None:
        self._internal = internal

    @cached_property
    def beta(self) -> AsyncBetaResourceWithStreamingResponse:
        return AsyncBetaResourceWithStreamingResponse(self._internal.beta)
