# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ...types.v1 import coupon_list_params, coupon_create_params, coupon_update_coupon_params
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncMyCursorIDPage, AsyncMyCursorIDPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.v1.coupon import Coupon
from ...types.v1.coupon_list_response import CouponListResponse

__all__ = ["CouponsResource", "AsyncCouponsResource"]


class CouponsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CouponsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stiggio/stigg-python#accessing-raw-response-data-eg-headers
        """
        return CouponsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CouponsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stiggio/stigg-python#with_streaming_response
        """
        return CouponsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        id: str,
        amounts_off: Optional[Iterable[coupon_create_params.AmountsOff]],
        description: Optional[str],
        duration_in_months: Optional[int],
        metadata: Optional[Dict[str, str]],
        name: str,
        percent_off: Optional[float],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Coupon:
        """
        Creates a new discount coupon with percentage or fixed amount off, applicable to
        customer subscriptions.

        Args:
          id: The unique identifier for the entity

          amounts_off: Fixed amount discounts in different currencies

          description: Description of the coupon

          duration_in_months: Duration of the coupon validity in months

          metadata: Metadata associated with the entity

          name: Name of the coupon

          percent_off: Percentage discount off the original price

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
                    "metadata": metadata,
                    "name": name,
                    "percent_off": percent_off,
                },
                coupon_create_params.CouponCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Coupon,
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
    ) -> Coupon:
        """
        Retrieves a coupon by its unique identifier.

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
            cast_to=Coupon,
        )

    def list(
        self,
        *,
        id: str | Omit = omit,
        after: str | Omit = omit,
        before: str | Omit = omit,
        created_at: coupon_list_params.CreatedAt | Omit = omit,
        limit: int | Omit = omit,
        status: str | Omit = omit,
        type: Literal["FIXED", "PERCENTAGE"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncMyCursorIDPage[CouponListResponse]:
        """
        Retrieves a paginated list of coupons in the environment.

        Args:
          id: Filter by entity ID

          after: Return items that come after this cursor

          before: Return items that come before this cursor

          created_at: Filter by creation date using range operators: gt, gte, lt, lte

          limit: Maximum number of items to return

          status: Filter by coupon status. Supports comma-separated values for multiple statuses

          type: Filter by coupon type (FIXED or PERCENTAGE)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/v1/coupons",
            page=SyncMyCursorIDPage[CouponListResponse],
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
                        "type": type,
                    },
                    coupon_list_params.CouponListParams,
                ),
            ),
            model=CouponListResponse,
        )

    def archive_coupon(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Coupon:
        """
        Archives a coupon, preventing it from being applied to new subscriptions.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/api/v1/coupons/{id}/archive",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Coupon,
        )

    def update_coupon(
        self,
        id: str,
        *,
        description: Optional[str] | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Coupon:
        """
        Updates an existing coupon's properties such as name, description, and metadata.

        Args:
          description: Description of the coupon

          metadata: Metadata associated with the entity

          name: Name of the coupon

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/api/v1/coupons/{id}",
            body=maybe_transform(
                {
                    "description": description,
                    "metadata": metadata,
                    "name": name,
                },
                coupon_update_coupon_params.CouponUpdateCouponParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Coupon,
        )


class AsyncCouponsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCouponsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stiggio/stigg-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCouponsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCouponsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stiggio/stigg-python#with_streaming_response
        """
        return AsyncCouponsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        id: str,
        amounts_off: Optional[Iterable[coupon_create_params.AmountsOff]],
        description: Optional[str],
        duration_in_months: Optional[int],
        metadata: Optional[Dict[str, str]],
        name: str,
        percent_off: Optional[float],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Coupon:
        """
        Creates a new discount coupon with percentage or fixed amount off, applicable to
        customer subscriptions.

        Args:
          id: The unique identifier for the entity

          amounts_off: Fixed amount discounts in different currencies

          description: Description of the coupon

          duration_in_months: Duration of the coupon validity in months

          metadata: Metadata associated with the entity

          name: Name of the coupon

          percent_off: Percentage discount off the original price

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
                    "metadata": metadata,
                    "name": name,
                    "percent_off": percent_off,
                },
                coupon_create_params.CouponCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Coupon,
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
    ) -> Coupon:
        """
        Retrieves a coupon by its unique identifier.

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
            cast_to=Coupon,
        )

    def list(
        self,
        *,
        id: str | Omit = omit,
        after: str | Omit = omit,
        before: str | Omit = omit,
        created_at: coupon_list_params.CreatedAt | Omit = omit,
        limit: int | Omit = omit,
        status: str | Omit = omit,
        type: Literal["FIXED", "PERCENTAGE"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[CouponListResponse, AsyncMyCursorIDPage[CouponListResponse]]:
        """
        Retrieves a paginated list of coupons in the environment.

        Args:
          id: Filter by entity ID

          after: Return items that come after this cursor

          before: Return items that come before this cursor

          created_at: Filter by creation date using range operators: gt, gte, lt, lte

          limit: Maximum number of items to return

          status: Filter by coupon status. Supports comma-separated values for multiple statuses

          type: Filter by coupon type (FIXED or PERCENTAGE)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/v1/coupons",
            page=AsyncMyCursorIDPage[CouponListResponse],
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
                        "type": type,
                    },
                    coupon_list_params.CouponListParams,
                ),
            ),
            model=CouponListResponse,
        )

    async def archive_coupon(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Coupon:
        """
        Archives a coupon, preventing it from being applied to new subscriptions.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/api/v1/coupons/{id}/archive",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Coupon,
        )

    async def update_coupon(
        self,
        id: str,
        *,
        description: Optional[str] | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Coupon:
        """
        Updates an existing coupon's properties such as name, description, and metadata.

        Args:
          description: Description of the coupon

          metadata: Metadata associated with the entity

          name: Name of the coupon

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/api/v1/coupons/{id}",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "metadata": metadata,
                    "name": name,
                },
                coupon_update_coupon_params.CouponUpdateCouponParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Coupon,
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
        self.archive_coupon = to_raw_response_wrapper(
            coupons.archive_coupon,
        )
        self.update_coupon = to_raw_response_wrapper(
            coupons.update_coupon,
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
        self.archive_coupon = async_to_raw_response_wrapper(
            coupons.archive_coupon,
        )
        self.update_coupon = async_to_raw_response_wrapper(
            coupons.update_coupon,
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
        self.archive_coupon = to_streamed_response_wrapper(
            coupons.archive_coupon,
        )
        self.update_coupon = to_streamed_response_wrapper(
            coupons.update_coupon,
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
        self.archive_coupon = async_to_streamed_response_wrapper(
            coupons.archive_coupon,
        )
        self.update_coupon = async_to_streamed_response_wrapper(
            coupons.update_coupon,
        )
