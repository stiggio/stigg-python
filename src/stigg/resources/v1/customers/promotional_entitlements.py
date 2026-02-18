# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
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
from ....types.v1.customers import promotional_entitlement_list_params, promotional_entitlement_create_params
from ....types.v1.customers.promotional_entitlement_list_response import PromotionalEntitlementListResponse
from ....types.v1.customers.promotional_entitlement_create_response import PromotionalEntitlementCreateResponse
from ....types.v1.customers.promotional_entitlement_revoke_response import PromotionalEntitlementRevokeResponse

__all__ = ["PromotionalEntitlementsResource", "AsyncPromotionalEntitlementsResource"]


class PromotionalEntitlementsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PromotionalEntitlementsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stiggio/stigg-python#accessing-raw-response-data-eg-headers
        """
        return PromotionalEntitlementsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PromotionalEntitlementsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stiggio/stigg-python#with_streaming_response
        """
        return PromotionalEntitlementsResourceWithStreamingResponse(self)

    def create(
        self,
        id: str,
        *,
        promotional_entitlements: Iterable[promotional_entitlement_create_params.PromotionalEntitlement],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PromotionalEntitlementCreateResponse:
        """
        Grants promotional entitlements to a customer, providing feature access outside
        their subscription. Entitlements can be time-limited or permanent.

        Args:
          promotional_entitlements: Promotional entitlements to grant

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/api/v1/customers/{id}/promotional-entitlements",
            body=maybe_transform(
                {"promotional_entitlements": promotional_entitlements},
                promotional_entitlement_create_params.PromotionalEntitlementCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PromotionalEntitlementCreateResponse,
        )

    def list(
        self,
        id: str,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        created_at: promotional_entitlement_list_params.CreatedAt | Omit = omit,
        limit: int | Omit = omit,
        status: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncMyCursorIDPage[PromotionalEntitlementListResponse]:
        """
        Retrieves a paginated list of a customer's promotional entitlements.

        Args:
          after: Return items that come after this cursor

          before: Return items that come before this cursor

          created_at: Filter by creation date using range operators: gt, gte, lt, lte

          limit: Maximum number of items to return

          status: Filter by promotional entitlement status. Supports comma-separated values for
              multiple statuses

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get_api_list(
            f"/api/v1/customers/{id}/promotional-entitlements",
            page=SyncMyCursorIDPage[PromotionalEntitlementListResponse],
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
                        "status": status,
                    },
                    promotional_entitlement_list_params.PromotionalEntitlementListParams,
                ),
            ),
            model=PromotionalEntitlementListResponse,
        )

    def revoke(
        self,
        feature_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PromotionalEntitlementRevokeResponse:
        """
        Revokes a previously granted promotional entitlement from a customer for a
        specific feature.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not feature_id:
            raise ValueError(f"Expected a non-empty value for `feature_id` but received {feature_id!r}")
        return self._delete(
            f"/api/v1/customers/{id}/promotional-entitlements/{feature_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PromotionalEntitlementRevokeResponse,
        )


class AsyncPromotionalEntitlementsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPromotionalEntitlementsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stiggio/stigg-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPromotionalEntitlementsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPromotionalEntitlementsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stiggio/stigg-python#with_streaming_response
        """
        return AsyncPromotionalEntitlementsResourceWithStreamingResponse(self)

    async def create(
        self,
        id: str,
        *,
        promotional_entitlements: Iterable[promotional_entitlement_create_params.PromotionalEntitlement],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PromotionalEntitlementCreateResponse:
        """
        Grants promotional entitlements to a customer, providing feature access outside
        their subscription. Entitlements can be time-limited or permanent.

        Args:
          promotional_entitlements: Promotional entitlements to grant

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/api/v1/customers/{id}/promotional-entitlements",
            body=await async_maybe_transform(
                {"promotional_entitlements": promotional_entitlements},
                promotional_entitlement_create_params.PromotionalEntitlementCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PromotionalEntitlementCreateResponse,
        )

    def list(
        self,
        id: str,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        created_at: promotional_entitlement_list_params.CreatedAt | Omit = omit,
        limit: int | Omit = omit,
        status: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[PromotionalEntitlementListResponse, AsyncMyCursorIDPage[PromotionalEntitlementListResponse]]:
        """
        Retrieves a paginated list of a customer's promotional entitlements.

        Args:
          after: Return items that come after this cursor

          before: Return items that come before this cursor

          created_at: Filter by creation date using range operators: gt, gte, lt, lte

          limit: Maximum number of items to return

          status: Filter by promotional entitlement status. Supports comma-separated values for
              multiple statuses

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get_api_list(
            f"/api/v1/customers/{id}/promotional-entitlements",
            page=AsyncMyCursorIDPage[PromotionalEntitlementListResponse],
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
                        "status": status,
                    },
                    promotional_entitlement_list_params.PromotionalEntitlementListParams,
                ),
            ),
            model=PromotionalEntitlementListResponse,
        )

    async def revoke(
        self,
        feature_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PromotionalEntitlementRevokeResponse:
        """
        Revokes a previously granted promotional entitlement from a customer for a
        specific feature.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not feature_id:
            raise ValueError(f"Expected a non-empty value for `feature_id` but received {feature_id!r}")
        return await self._delete(
            f"/api/v1/customers/{id}/promotional-entitlements/{feature_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PromotionalEntitlementRevokeResponse,
        )


class PromotionalEntitlementsResourceWithRawResponse:
    def __init__(self, promotional_entitlements: PromotionalEntitlementsResource) -> None:
        self._promotional_entitlements = promotional_entitlements

        self.create = to_raw_response_wrapper(
            promotional_entitlements.create,
        )
        self.list = to_raw_response_wrapper(
            promotional_entitlements.list,
        )
        self.revoke = to_raw_response_wrapper(
            promotional_entitlements.revoke,
        )


class AsyncPromotionalEntitlementsResourceWithRawResponse:
    def __init__(self, promotional_entitlements: AsyncPromotionalEntitlementsResource) -> None:
        self._promotional_entitlements = promotional_entitlements

        self.create = async_to_raw_response_wrapper(
            promotional_entitlements.create,
        )
        self.list = async_to_raw_response_wrapper(
            promotional_entitlements.list,
        )
        self.revoke = async_to_raw_response_wrapper(
            promotional_entitlements.revoke,
        )


class PromotionalEntitlementsResourceWithStreamingResponse:
    def __init__(self, promotional_entitlements: PromotionalEntitlementsResource) -> None:
        self._promotional_entitlements = promotional_entitlements

        self.create = to_streamed_response_wrapper(
            promotional_entitlements.create,
        )
        self.list = to_streamed_response_wrapper(
            promotional_entitlements.list,
        )
        self.revoke = to_streamed_response_wrapper(
            promotional_entitlements.revoke,
        )


class AsyncPromotionalEntitlementsResourceWithStreamingResponse:
    def __init__(self, promotional_entitlements: AsyncPromotionalEntitlementsResource) -> None:
        self._promotional_entitlements = promotional_entitlements

        self.create = async_to_streamed_response_wrapper(
            promotional_entitlements.create,
        )
        self.list = async_to_streamed_response_wrapper(
            promotional_entitlements.list,
        )
        self.revoke = async_to_streamed_response_wrapper(
            promotional_entitlements.revoke,
        )
