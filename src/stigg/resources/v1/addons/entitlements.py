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
from ...._base_client import make_request_options
from ....types.v1.addons import entitlement_create_params, entitlement_update_params
from ....types.v1.addons.addon_package_entitlement import AddonPackageEntitlement
from ....types.v1.addons.entitlement_list_response import EntitlementListResponse
from ....types.v1.addons.entitlement_create_response import EntitlementCreateResponse

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

    def create(
        self,
        addon_id: str,
        *,
        entitlements: Iterable[entitlement_create_params.Entitlement],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EntitlementCreateResponse:
        """
        Creates one or more entitlements (feature or credit) on a draft addon.

        Args:
          entitlements: Entitlements to create

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not addon_id:
            raise ValueError(f"Expected a non-empty value for `addon_id` but received {addon_id!r}")
        return self._post(
            f"/api/v1/addons/{addon_id}/entitlements",
            body=maybe_transform({"entitlements": entitlements}, entitlement_create_params.EntitlementCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EntitlementCreateResponse,
        )

    def update(
        self,
        id: str,
        *,
        addon_id: str,
        credit: entitlement_update_params.Credit | Omit = omit,
        feature: entitlement_update_params.Feature | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AddonPackageEntitlement:
        """
        Updates an existing entitlement on a draft addon.

        Args:
          credit: Credit entitlement fields to update

          feature: Feature entitlement fields to update

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not addon_id:
            raise ValueError(f"Expected a non-empty value for `addon_id` but received {addon_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/api/v1/addons/{addon_id}/entitlements/{id}",
            body=maybe_transform(
                {
                    "credit": credit,
                    "feature": feature,
                },
                entitlement_update_params.EntitlementUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AddonPackageEntitlement,
        )

    def list(
        self,
        addon_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EntitlementListResponse:
        """
        Retrieves a list of entitlements for an addon.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not addon_id:
            raise ValueError(f"Expected a non-empty value for `addon_id` but received {addon_id!r}")
        return self._get(
            f"/api/v1/addons/{addon_id}/entitlements",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EntitlementListResponse,
        )

    def delete(
        self,
        id: str,
        *,
        addon_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AddonPackageEntitlement:
        """
        Deletes an entitlement from a draft addon.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not addon_id:
            raise ValueError(f"Expected a non-empty value for `addon_id` but received {addon_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/api/v1/addons/{addon_id}/entitlements/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AddonPackageEntitlement,
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

    async def create(
        self,
        addon_id: str,
        *,
        entitlements: Iterable[entitlement_create_params.Entitlement],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EntitlementCreateResponse:
        """
        Creates one or more entitlements (feature or credit) on a draft addon.

        Args:
          entitlements: Entitlements to create

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not addon_id:
            raise ValueError(f"Expected a non-empty value for `addon_id` but received {addon_id!r}")
        return await self._post(
            f"/api/v1/addons/{addon_id}/entitlements",
            body=await async_maybe_transform(
                {"entitlements": entitlements}, entitlement_create_params.EntitlementCreateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EntitlementCreateResponse,
        )

    async def update(
        self,
        id: str,
        *,
        addon_id: str,
        credit: entitlement_update_params.Credit | Omit = omit,
        feature: entitlement_update_params.Feature | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AddonPackageEntitlement:
        """
        Updates an existing entitlement on a draft addon.

        Args:
          credit: Credit entitlement fields to update

          feature: Feature entitlement fields to update

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not addon_id:
            raise ValueError(f"Expected a non-empty value for `addon_id` but received {addon_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/api/v1/addons/{addon_id}/entitlements/{id}",
            body=await async_maybe_transform(
                {
                    "credit": credit,
                    "feature": feature,
                },
                entitlement_update_params.EntitlementUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AddonPackageEntitlement,
        )

    async def list(
        self,
        addon_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EntitlementListResponse:
        """
        Retrieves a list of entitlements for an addon.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not addon_id:
            raise ValueError(f"Expected a non-empty value for `addon_id` but received {addon_id!r}")
        return await self._get(
            f"/api/v1/addons/{addon_id}/entitlements",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EntitlementListResponse,
        )

    async def delete(
        self,
        id: str,
        *,
        addon_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AddonPackageEntitlement:
        """
        Deletes an entitlement from a draft addon.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not addon_id:
            raise ValueError(f"Expected a non-empty value for `addon_id` but received {addon_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/api/v1/addons/{addon_id}/entitlements/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AddonPackageEntitlement,
        )


class EntitlementsResourceWithRawResponse:
    def __init__(self, entitlements: EntitlementsResource) -> None:
        self._entitlements = entitlements

        self.create = to_raw_response_wrapper(
            entitlements.create,
        )
        self.update = to_raw_response_wrapper(
            entitlements.update,
        )
        self.list = to_raw_response_wrapper(
            entitlements.list,
        )
        self.delete = to_raw_response_wrapper(
            entitlements.delete,
        )


class AsyncEntitlementsResourceWithRawResponse:
    def __init__(self, entitlements: AsyncEntitlementsResource) -> None:
        self._entitlements = entitlements

        self.create = async_to_raw_response_wrapper(
            entitlements.create,
        )
        self.update = async_to_raw_response_wrapper(
            entitlements.update,
        )
        self.list = async_to_raw_response_wrapper(
            entitlements.list,
        )
        self.delete = async_to_raw_response_wrapper(
            entitlements.delete,
        )


class EntitlementsResourceWithStreamingResponse:
    def __init__(self, entitlements: EntitlementsResource) -> None:
        self._entitlements = entitlements

        self.create = to_streamed_response_wrapper(
            entitlements.create,
        )
        self.update = to_streamed_response_wrapper(
            entitlements.update,
        )
        self.list = to_streamed_response_wrapper(
            entitlements.list,
        )
        self.delete = to_streamed_response_wrapper(
            entitlements.delete,
        )


class AsyncEntitlementsResourceWithStreamingResponse:
    def __init__(self, entitlements: AsyncEntitlementsResource) -> None:
        self._entitlements = entitlements

        self.create = async_to_streamed_response_wrapper(
            entitlements.create,
        )
        self.update = async_to_streamed_response_wrapper(
            entitlements.update,
        )
        self.list = async_to_streamed_response_wrapper(
            entitlements.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            entitlements.delete,
        )
