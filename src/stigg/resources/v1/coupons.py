# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ...types.v1 import coupon_list_params, coupon_create_params
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.v1.coupon_list_response import CouponListResponse
from ...types.v1.coupon_create_response import CouponCreateResponse
from ...types.v1.coupon_retrieve_response import CouponRetrieveResponse

__all__ = ["CouponsResource", "AsyncCouponsResource"]


class CouponsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CouponsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/stigg-python#accessing-raw-response-data-eg-headers
        """
        return CouponsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CouponsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/stigg-python#with_streaming_response
        """
        return CouponsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        id: str,
        amounts_off: Optional[Iterable[coupon_create_params.AmountsOff]],
        description: Optional[str],
        duration_in_months: Optional[int],
        name: str,
        percent_off: Optional[float],
        additional_meta_data: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CouponCreateResponse:
        """
        Create a new Coupon

        Args:
          id: The unique identifier for the entity

          amounts_off: Fixed amount discounts in different currencies

          description: Description of the coupon

          duration_in_months: Duration of the coupon validity in months

          name: Name of the coupon

          percent_off: Percentage discount off the original price

          additional_meta_data: Metadata associated with the entity

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/coupons",
            body=maybe_transform(
                {
                    "id": id,
                    "amounts_off": amounts_off,
                    "description": description,
                    "duration_in_months": duration_in_months,
                    "name": name,
                    "percent_off": percent_off,
                    "additional_meta_data": additional_meta_data,
                },
                coupon_create_params.CouponCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CouponCreateResponse,
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
    ) -> CouponRetrieveResponse:
        """
        Get a single Coupon by id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/api/v1/coupons/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CouponRetrieveResponse,
        )

    def list(
        self,
        *,
        ending_before: str | Omit = omit,
        limit: int | Omit = omit,
        starting_after: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CouponListResponse:
        """
        Get a list of Coupons

        Args:
          ending_before: Ending before this UUID for pagination

          limit: Items per page

          starting_after: Starting after this UUID for pagination

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/coupons",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ending_before": ending_before,
                        "limit": limit,
                        "starting_after": starting_after,
                    },
                    coupon_list_params.CouponListParams,
                ),
            ),
            cast_to=CouponListResponse,
        )


class AsyncCouponsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCouponsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/stigg-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCouponsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCouponsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/stigg-python#with_streaming_response
        """
        return AsyncCouponsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        id: str,
        amounts_off: Optional[Iterable[coupon_create_params.AmountsOff]],
        description: Optional[str],
        duration_in_months: Optional[int],
        name: str,
        percent_off: Optional[float],
        additional_meta_data: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CouponCreateResponse:
        """
        Create a new Coupon

        Args:
          id: The unique identifier for the entity

          amounts_off: Fixed amount discounts in different currencies

          description: Description of the coupon

          duration_in_months: Duration of the coupon validity in months

          name: Name of the coupon

          percent_off: Percentage discount off the original price

          additional_meta_data: Metadata associated with the entity

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/coupons",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "amounts_off": amounts_off,
                    "description": description,
                    "duration_in_months": duration_in_months,
                    "name": name,
                    "percent_off": percent_off,
                    "additional_meta_data": additional_meta_data,
                },
                coupon_create_params.CouponCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CouponCreateResponse,
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
    ) -> CouponRetrieveResponse:
        """
        Get a single Coupon by id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/api/v1/coupons/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CouponRetrieveResponse,
        )

    async def list(
        self,
        *,
        ending_before: str | Omit = omit,
        limit: int | Omit = omit,
        starting_after: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CouponListResponse:
        """
        Get a list of Coupons

        Args:
          ending_before: Ending before this UUID for pagination

          limit: Items per page

          starting_after: Starting after this UUID for pagination

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/coupons",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "ending_before": ending_before,
                        "limit": limit,
                        "starting_after": starting_after,
                    },
                    coupon_list_params.CouponListParams,
                ),
            ),
            cast_to=CouponListResponse,
        )


class CouponsResourceWithRawResponse:
    def __init__(self, coupons: CouponsResource) -> None:
        self._coupons = coupons

        self.create = to_raw_response_wrapper(
            coupons.create,
        )
        self.retrieve = to_raw_response_wrapper(
            coupons.retrieve,
        )
        self.list = to_raw_response_wrapper(
            coupons.list,
        )


class AsyncCouponsResourceWithRawResponse:
    def __init__(self, coupons: AsyncCouponsResource) -> None:
        self._coupons = coupons

        self.create = async_to_raw_response_wrapper(
            coupons.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            coupons.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            coupons.list,
        )


class CouponsResourceWithStreamingResponse:
    def __init__(self, coupons: CouponsResource) -> None:
        self._coupons = coupons

        self.create = to_streamed_response_wrapper(
            coupons.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            coupons.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            coupons.list,
        )


class AsyncCouponsResourceWithStreamingResponse:
    def __init__(self, coupons: AsyncCouponsResource) -> None:
        self._coupons = coupons

        self.create = async_to_streamed_response_wrapper(
            coupons.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            coupons.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            coupons.list,
        )
