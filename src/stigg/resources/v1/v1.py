# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .permissions import (
    PermissionsResource,
    AsyncPermissionsResource,
    PermissionsResourceWithRawResponse,
    AsyncPermissionsResourceWithRawResponse,
    PermissionsResourceWithStreamingResponse,
    AsyncPermissionsResourceWithStreamingResponse,
)
from ..._base_client import make_request_options
from ...types.v1_retrieve_customer_response import V1RetrieveCustomerResponse

__all__ = ["V1Resource", "AsyncV1Resource"]


class V1Resource(SyncAPIResource):
    @cached_property
    def permissions(self) -> PermissionsResource:
        return PermissionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> V1ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/stigg-python#accessing-raw-response-data-eg-headers
        """
        return V1ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V1ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/stigg-python#with_streaming_response
        """
        return V1ResourceWithStreamingResponse(self)

    def retrieve_customer(
        self,
        ref_id: str,
        *,
        x_api_key: str,
        x_environment_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1RetrieveCustomerResponse:
        """
        Get a single customer by id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ref_id:
            raise ValueError(f"Expected a non-empty value for `ref_id` but received {ref_id!r}")
        extra_headers = {"X-API-KEY": x_api_key, "X-ENVIRONMENT-ID": x_environment_id, **(extra_headers or {})}
        return self._get(
            f"/api/v1/customers/{ref_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1RetrieveCustomerResponse,
        )


class AsyncV1Resource(AsyncAPIResource):
    @cached_property
    def permissions(self) -> AsyncPermissionsResource:
        return AsyncPermissionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncV1ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/stigg-python#accessing-raw-response-data-eg-headers
        """
        return AsyncV1ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV1ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/stigg-python#with_streaming_response
        """
        return AsyncV1ResourceWithStreamingResponse(self)

    async def retrieve_customer(
        self,
        ref_id: str,
        *,
        x_api_key: str,
        x_environment_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V1RetrieveCustomerResponse:
        """
        Get a single customer by id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not ref_id:
            raise ValueError(f"Expected a non-empty value for `ref_id` but received {ref_id!r}")
        extra_headers = {"X-API-KEY": x_api_key, "X-ENVIRONMENT-ID": x_environment_id, **(extra_headers or {})}
        return await self._get(
            f"/api/v1/customers/{ref_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1RetrieveCustomerResponse,
        )


class V1ResourceWithRawResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

        self.retrieve_customer = to_raw_response_wrapper(
            v1.retrieve_customer,
        )

    @cached_property
    def permissions(self) -> PermissionsResourceWithRawResponse:
        return PermissionsResourceWithRawResponse(self._v1.permissions)


class AsyncV1ResourceWithRawResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

        self.retrieve_customer = async_to_raw_response_wrapper(
            v1.retrieve_customer,
        )

    @cached_property
    def permissions(self) -> AsyncPermissionsResourceWithRawResponse:
        return AsyncPermissionsResourceWithRawResponse(self._v1.permissions)


class V1ResourceWithStreamingResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

        self.retrieve_customer = to_streamed_response_wrapper(
            v1.retrieve_customer,
        )

    @cached_property
    def permissions(self) -> PermissionsResourceWithStreamingResponse:
        return PermissionsResourceWithStreamingResponse(self._v1.permissions)


class AsyncV1ResourceWithStreamingResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

        self.retrieve_customer = async_to_streamed_response_wrapper(
            v1.retrieve_customer,
        )

    @cached_property
    def permissions(self) -> AsyncPermissionsResourceWithStreamingResponse:
        return AsyncPermissionsResourceWithStreamingResponse(self._v1.permissions)
