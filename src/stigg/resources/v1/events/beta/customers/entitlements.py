# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict

import httpx

from ......_types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ......_utils import path_template, maybe_transform, async_maybe_transform
from ......_compat import cached_property
from ......_resource import SyncAPIResource, AsyncAPIResource
from ......_response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ......_base_client import make_request_options
from ......types.v1.events.beta.customers import entitlement_check_params
from ......types.v1.events.beta.customers.entitlement_check_response import EntitlementCheckResponse

__all__ = ["EntitlementsResource", "AsyncEntitlementsResource"]


class EntitlementsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EntitlementsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stiggio/stigg-python#accessing-raw-response-data-eg-headers
        """
        return EntitlementsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EntitlementsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stiggio/stigg-python#with_streaming_response
        """
        return EntitlementsResourceWithStreamingResponse(self)

    def check(
        self,
        id: str,
        *,
        currency_id: str | Omit = omit,
        dimensions: Dict[str, str] | Omit = omit,
        feature_id: str | Omit = omit,
        requested_usage: int | Omit = omit,
        requested_values: SequenceNotStr[str] | Omit = omit,
        resource_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EntitlementCheckResponse:
        """Experimental — request and response shapes may change without notice.

        Same
        semantics as `Check entitlement`, plus an optional `dimensions` query param that
        resolves to per-entity governance limits surfaced as `chains` on the response.

        Args:
          currency_id: Currency ID (refId) to check for credit entitlements. Mutually exclusive with
              `featureId`.

          dimensions: Optional attribution map (e.g. `dimensions[userId]=u1`). When provided, the
              response includes a `chains` array with per-entity governance limits.

          feature_id: Feature ID (refId) to check. Mutually exclusive with `currencyId`.

          requested_usage: Requested usage amount to evaluate against the entitlement limit (numeric
              features only)

          requested_values: Requested values to evaluate against allowed values (enum features only)

          resource_id: Resource ID to scope the entitlement check to a specific resource

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/api/v1-beta/customers/{id}/entitlements/check", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "currency_id": currency_id,
                        "dimensions": dimensions,
                        "feature_id": feature_id,
                        "requested_usage": requested_usage,
                        "requested_values": requested_values,
                        "resource_id": resource_id,
                    },
                    entitlement_check_params.EntitlementCheckParams,
                ),
            ),
            cast_to=EntitlementCheckResponse,
        )


class AsyncEntitlementsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEntitlementsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stiggio/stigg-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEntitlementsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEntitlementsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stiggio/stigg-python#with_streaming_response
        """
        return AsyncEntitlementsResourceWithStreamingResponse(self)

    async def check(
        self,
        id: str,
        *,
        currency_id: str | Omit = omit,
        dimensions: Dict[str, str] | Omit = omit,
        feature_id: str | Omit = omit,
        requested_usage: int | Omit = omit,
        requested_values: SequenceNotStr[str] | Omit = omit,
        resource_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EntitlementCheckResponse:
        """Experimental — request and response shapes may change without notice.

        Same
        semantics as `Check entitlement`, plus an optional `dimensions` query param that
        resolves to per-entity governance limits surfaced as `chains` on the response.

        Args:
          currency_id: Currency ID (refId) to check for credit entitlements. Mutually exclusive with
              `featureId`.

          dimensions: Optional attribution map (e.g. `dimensions[userId]=u1`). When provided, the
              response includes a `chains` array with per-entity governance limits.

          feature_id: Feature ID (refId) to check. Mutually exclusive with `currencyId`.

          requested_usage: Requested usage amount to evaluate against the entitlement limit (numeric
              features only)

          requested_values: Requested values to evaluate against allowed values (enum features only)

          resource_id: Resource ID to scope the entitlement check to a specific resource

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/api/v1-beta/customers/{id}/entitlements/check", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "currency_id": currency_id,
                        "dimensions": dimensions,
                        "feature_id": feature_id,
                        "requested_usage": requested_usage,
                        "requested_values": requested_values,
                        "resource_id": resource_id,
                    },
                    entitlement_check_params.EntitlementCheckParams,
                ),
            ),
            cast_to=EntitlementCheckResponse,
        )


class EntitlementsResourceWithRawResponse:
    def __init__(self, entitlements: EntitlementsResource) -> None:
        self._entitlements = entitlements

        self.check = to_raw_response_wrapper(
            entitlements.check,
        )


class AsyncEntitlementsResourceWithRawResponse:
    def __init__(self, entitlements: AsyncEntitlementsResource) -> None:
        self._entitlements = entitlements

        self.check = async_to_raw_response_wrapper(
            entitlements.check,
        )


class EntitlementsResourceWithStreamingResponse:
    def __init__(self, entitlements: EntitlementsResource) -> None:
        self._entitlements = entitlements

        self.check = to_streamed_response_wrapper(
            entitlements.check,
        )


class AsyncEntitlementsResourceWithStreamingResponse:
    def __init__(self, entitlements: AsyncEntitlementsResource) -> None:
        self._entitlements = entitlements

        self.check = async_to_streamed_response_wrapper(
            entitlements.check,
        )
