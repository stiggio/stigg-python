# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ...._types import Body, Query, Headers, NotGiven, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.v1.customers import promotional_create_params
from ....types.v1.customers.promotional_create_response import PromotionalCreateResponse
from ....types.v1.customers.promotional_revoke_response import PromotionalRevokeResponse

__all__ = ["PromotionalResource", "AsyncPromotionalResource"]


class PromotionalResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PromotionalResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/stigg-python#accessing-raw-response-data-eg-headers
        """
        return PromotionalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PromotionalResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/stigg-python#with_streaming_response
        """
        return PromotionalResourceWithStreamingResponse(self)

    def create(
        self,
        customer_id: str,
        *,
        promotional_entitlements: Iterable[promotional_create_params.PromotionalEntitlement],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PromotionalCreateResponse:
        """
        Create a new Promotional Entitlements

        Args:
          promotional_entitlements: Promotional entitlements to grant

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        return self._post(
            f"/api/v1/customers/{customer_id}/promotional",
            body=maybe_transform(
                {"promotional_entitlements": promotional_entitlements},
                promotional_create_params.PromotionalCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PromotionalCreateResponse,
        )

    def revoke(
        self,
        feature_id: str,
        *,
        customer_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PromotionalRevokeResponse:
        """
        Perform revocation on a Promotional Entitlement

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        if not feature_id:
            raise ValueError(f"Expected a non-empty value for `feature_id` but received {feature_id!r}")
        return self._delete(
            f"/api/v1/customers/{customer_id}/promotional/featureId/{feature_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PromotionalRevokeResponse,
        )


class AsyncPromotionalResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPromotionalResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/stigg-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPromotionalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPromotionalResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/stigg-python#with_streaming_response
        """
        return AsyncPromotionalResourceWithStreamingResponse(self)

    async def create(
        self,
        customer_id: str,
        *,
        promotional_entitlements: Iterable[promotional_create_params.PromotionalEntitlement],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PromotionalCreateResponse:
        """
        Create a new Promotional Entitlements

        Args:
          promotional_entitlements: Promotional entitlements to grant

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        return await self._post(
            f"/api/v1/customers/{customer_id}/promotional",
            body=await async_maybe_transform(
                {"promotional_entitlements": promotional_entitlements},
                promotional_create_params.PromotionalCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PromotionalCreateResponse,
        )

    async def revoke(
        self,
        feature_id: str,
        *,
        customer_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PromotionalRevokeResponse:
        """
        Perform revocation on a Promotional Entitlement

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        if not feature_id:
            raise ValueError(f"Expected a non-empty value for `feature_id` but received {feature_id!r}")
        return await self._delete(
            f"/api/v1/customers/{customer_id}/promotional/featureId/{feature_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PromotionalRevokeResponse,
        )


class PromotionalResourceWithRawResponse:
    def __init__(self, promotional: PromotionalResource) -> None:
        self._promotional = promotional

        self.create = to_raw_response_wrapper(
            promotional.create,
        )
        self.revoke = to_raw_response_wrapper(
            promotional.revoke,
        )


class AsyncPromotionalResourceWithRawResponse:
    def __init__(self, promotional: AsyncPromotionalResource) -> None:
        self._promotional = promotional

        self.create = async_to_raw_response_wrapper(
            promotional.create,
        )
        self.revoke = async_to_raw_response_wrapper(
            promotional.revoke,
        )


class PromotionalResourceWithStreamingResponse:
    def __init__(self, promotional: PromotionalResource) -> None:
        self._promotional = promotional

        self.create = to_streamed_response_wrapper(
            promotional.create,
        )
        self.revoke = to_streamed_response_wrapper(
            promotional.revoke,
        )


class AsyncPromotionalResourceWithStreamingResponse:
    def __init__(self, promotional: AsyncPromotionalResource) -> None:
        self._promotional = promotional

        self.create = async_to_streamed_response_wrapper(
            promotional.create,
        )
        self.revoke = async_to_streamed_response_wrapper(
            promotional.revoke,
        )
