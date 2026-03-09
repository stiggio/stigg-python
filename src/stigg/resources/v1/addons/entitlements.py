# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Literal, overload

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import required_args, maybe_transform, async_maybe_transform
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

    @overload
    def update(
        self,
        id: str,
        *,
        addon_id: str,
        type: Literal["FEATURE"],
        behavior: Literal["Increment", "Override"] | Omit = omit,
        description: str | Omit = omit,
        display_name_override: str | Omit = omit,
        enum_values: SequenceNotStr[str] | Omit = omit,
        has_soft_limit: bool | Omit = omit,
        has_unlimited_usage: bool | Omit = omit,
        hidden_from_widgets: List[Literal["PAYWALL", "CUSTOMER_PORTAL", "CHECKOUT"]] | Omit = omit,
        is_custom: bool | Omit = omit,
        is_granted: bool | Omit = omit,
        monthly_reset_period_configuration: Optional[
            entitlement_update_params.UpdateFeatureEntitlementRequestMonthlyResetPeriodConfiguration
        ]
        | Omit = omit,
        order: float | Omit = omit,
        reset_period: Literal["YEAR", "MONTH", "WEEK", "DAY", "HOUR"] | Omit = omit,
        usage_limit: Optional[int] | Omit = omit,
        weekly_reset_period_configuration: Optional[
            entitlement_update_params.UpdateFeatureEntitlementRequestWeeklyResetPeriodConfiguration
        ]
        | Omit = omit,
        yearly_reset_period_configuration: Optional[
            entitlement_update_params.UpdateFeatureEntitlementRequestYearlyResetPeriodConfiguration
        ]
        | Omit = omit,
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
          type: UpdateFeatureEntitlementRequest

          behavior: Entitlement behavior (Increment or Override)

          description: Description of the entitlement

          display_name_override: Override display name for the entitlement

          enum_values: Allowed enum values for the feature entitlement

          has_soft_limit: Whether the usage limit is a soft limit

          has_unlimited_usage: Whether usage is unlimited

          hidden_from_widgets: Widget types where this entitlement is hidden

          is_custom: Whether this is a custom entitlement

          is_granted: Whether the entitlement is granted

          monthly_reset_period_configuration: Configuration for monthly reset period

          order: Display order of the entitlement

          reset_period: Period at which usage resets

          usage_limit: Maximum allowed usage for the feature

          weekly_reset_period_configuration: Configuration for weekly reset period

          yearly_reset_period_configuration: Configuration for yearly reset period

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        id: str,
        *,
        addon_id: str,
        type: Literal["CREDIT"],
        amount: float | Omit = omit,
        behavior: Literal["Increment", "Override"] | Omit = omit,
        cadence: Literal["MONTH", "YEAR"] | Omit = omit,
        description: str | Omit = omit,
        display_name_override: str | Omit = omit,
        hidden_from_widgets: List[Literal["PAYWALL", "CUSTOMER_PORTAL", "CHECKOUT"]] | Omit = omit,
        is_custom: bool | Omit = omit,
        is_granted: bool | Omit = omit,
        order: float | Omit = omit,
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
          type: UpdateCreditEntitlementRequest

          amount: Credit grant amount

          behavior: Entitlement behavior (Increment or Override)

          cadence: Credit grant cadence (MONTH or YEAR)

          description: Description of the entitlement

          display_name_override: Override display name for the entitlement

          hidden_from_widgets: Widget types where this entitlement is hidden

          is_custom: Whether this is a custom entitlement

          is_granted: Whether the entitlement is granted

          order: Display order of the entitlement

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["addon_id", "type"])
    def update(
        self,
        id: str,
        *,
        addon_id: str,
        type: Literal["FEATURE"] | Literal["CREDIT"],
        behavior: Literal["Increment", "Override"] | Omit = omit,
        description: str | Omit = omit,
        display_name_override: str | Omit = omit,
        enum_values: SequenceNotStr[str] | Omit = omit,
        has_soft_limit: bool | Omit = omit,
        has_unlimited_usage: bool | Omit = omit,
        hidden_from_widgets: List[Literal["PAYWALL", "CUSTOMER_PORTAL", "CHECKOUT"]] | Omit = omit,
        is_custom: bool | Omit = omit,
        is_granted: bool | Omit = omit,
        monthly_reset_period_configuration: Optional[
            entitlement_update_params.UpdateFeatureEntitlementRequestMonthlyResetPeriodConfiguration
        ]
        | Omit = omit,
        order: float | Omit = omit,
        reset_period: Literal["YEAR", "MONTH", "WEEK", "DAY", "HOUR"] | Omit = omit,
        usage_limit: Optional[int] | Omit = omit,
        weekly_reset_period_configuration: Optional[
            entitlement_update_params.UpdateFeatureEntitlementRequestWeeklyResetPeriodConfiguration
        ]
        | Omit = omit,
        yearly_reset_period_configuration: Optional[
            entitlement_update_params.UpdateFeatureEntitlementRequestYearlyResetPeriodConfiguration
        ]
        | Omit = omit,
        amount: float | Omit = omit,
        cadence: Literal["MONTH", "YEAR"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AddonPackageEntitlement:
        if not addon_id:
            raise ValueError(f"Expected a non-empty value for `addon_id` but received {addon_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/api/v1/addons/{addon_id}/entitlements/{id}",
            body=maybe_transform(
                {
                    "type": type,
                    "behavior": behavior,
                    "description": description,
                    "display_name_override": display_name_override,
                    "enum_values": enum_values,
                    "has_soft_limit": has_soft_limit,
                    "has_unlimited_usage": has_unlimited_usage,
                    "hidden_from_widgets": hidden_from_widgets,
                    "is_custom": is_custom,
                    "is_granted": is_granted,
                    "monthly_reset_period_configuration": monthly_reset_period_configuration,
                    "order": order,
                    "reset_period": reset_period,
                    "usage_limit": usage_limit,
                    "weekly_reset_period_configuration": weekly_reset_period_configuration,
                    "yearly_reset_period_configuration": yearly_reset_period_configuration,
                    "amount": amount,
                    "cadence": cadence,
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

    @overload
    async def update(
        self,
        id: str,
        *,
        addon_id: str,
        type: Literal["FEATURE"],
        behavior: Literal["Increment", "Override"] | Omit = omit,
        description: str | Omit = omit,
        display_name_override: str | Omit = omit,
        enum_values: SequenceNotStr[str] | Omit = omit,
        has_soft_limit: bool | Omit = omit,
        has_unlimited_usage: bool | Omit = omit,
        hidden_from_widgets: List[Literal["PAYWALL", "CUSTOMER_PORTAL", "CHECKOUT"]] | Omit = omit,
        is_custom: bool | Omit = omit,
        is_granted: bool | Omit = omit,
        monthly_reset_period_configuration: Optional[
            entitlement_update_params.UpdateFeatureEntitlementRequestMonthlyResetPeriodConfiguration
        ]
        | Omit = omit,
        order: float | Omit = omit,
        reset_period: Literal["YEAR", "MONTH", "WEEK", "DAY", "HOUR"] | Omit = omit,
        usage_limit: Optional[int] | Omit = omit,
        weekly_reset_period_configuration: Optional[
            entitlement_update_params.UpdateFeatureEntitlementRequestWeeklyResetPeriodConfiguration
        ]
        | Omit = omit,
        yearly_reset_period_configuration: Optional[
            entitlement_update_params.UpdateFeatureEntitlementRequestYearlyResetPeriodConfiguration
        ]
        | Omit = omit,
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
          type: UpdateFeatureEntitlementRequest

          behavior: Entitlement behavior (Increment or Override)

          description: Description of the entitlement

          display_name_override: Override display name for the entitlement

          enum_values: Allowed enum values for the feature entitlement

          has_soft_limit: Whether the usage limit is a soft limit

          has_unlimited_usage: Whether usage is unlimited

          hidden_from_widgets: Widget types where this entitlement is hidden

          is_custom: Whether this is a custom entitlement

          is_granted: Whether the entitlement is granted

          monthly_reset_period_configuration: Configuration for monthly reset period

          order: Display order of the entitlement

          reset_period: Period at which usage resets

          usage_limit: Maximum allowed usage for the feature

          weekly_reset_period_configuration: Configuration for weekly reset period

          yearly_reset_period_configuration: Configuration for yearly reset period

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        id: str,
        *,
        addon_id: str,
        type: Literal["CREDIT"],
        amount: float | Omit = omit,
        behavior: Literal["Increment", "Override"] | Omit = omit,
        cadence: Literal["MONTH", "YEAR"] | Omit = omit,
        description: str | Omit = omit,
        display_name_override: str | Omit = omit,
        hidden_from_widgets: List[Literal["PAYWALL", "CUSTOMER_PORTAL", "CHECKOUT"]] | Omit = omit,
        is_custom: bool | Omit = omit,
        is_granted: bool | Omit = omit,
        order: float | Omit = omit,
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
          type: UpdateCreditEntitlementRequest

          amount: Credit grant amount

          behavior: Entitlement behavior (Increment or Override)

          cadence: Credit grant cadence (MONTH or YEAR)

          description: Description of the entitlement

          display_name_override: Override display name for the entitlement

          hidden_from_widgets: Widget types where this entitlement is hidden

          is_custom: Whether this is a custom entitlement

          is_granted: Whether the entitlement is granted

          order: Display order of the entitlement

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["addon_id", "type"])
    async def update(
        self,
        id: str,
        *,
        addon_id: str,
        type: Literal["FEATURE"] | Literal["CREDIT"],
        behavior: Literal["Increment", "Override"] | Omit = omit,
        description: str | Omit = omit,
        display_name_override: str | Omit = omit,
        enum_values: SequenceNotStr[str] | Omit = omit,
        has_soft_limit: bool | Omit = omit,
        has_unlimited_usage: bool | Omit = omit,
        hidden_from_widgets: List[Literal["PAYWALL", "CUSTOMER_PORTAL", "CHECKOUT"]] | Omit = omit,
        is_custom: bool | Omit = omit,
        is_granted: bool | Omit = omit,
        monthly_reset_period_configuration: Optional[
            entitlement_update_params.UpdateFeatureEntitlementRequestMonthlyResetPeriodConfiguration
        ]
        | Omit = omit,
        order: float | Omit = omit,
        reset_period: Literal["YEAR", "MONTH", "WEEK", "DAY", "HOUR"] | Omit = omit,
        usage_limit: Optional[int] | Omit = omit,
        weekly_reset_period_configuration: Optional[
            entitlement_update_params.UpdateFeatureEntitlementRequestWeeklyResetPeriodConfiguration
        ]
        | Omit = omit,
        yearly_reset_period_configuration: Optional[
            entitlement_update_params.UpdateFeatureEntitlementRequestYearlyResetPeriodConfiguration
        ]
        | Omit = omit,
        amount: float | Omit = omit,
        cadence: Literal["MONTH", "YEAR"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AddonPackageEntitlement:
        if not addon_id:
            raise ValueError(f"Expected a non-empty value for `addon_id` but received {addon_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/api/v1/addons/{addon_id}/entitlements/{id}",
            body=await async_maybe_transform(
                {
                    "type": type,
                    "behavior": behavior,
                    "description": description,
                    "display_name_override": display_name_override,
                    "enum_values": enum_values,
                    "has_soft_limit": has_soft_limit,
                    "has_unlimited_usage": has_unlimited_usage,
                    "hidden_from_widgets": hidden_from_widgets,
                    "is_custom": is_custom,
                    "is_granted": is_granted,
                    "monthly_reset_period_configuration": monthly_reset_period_configuration,
                    "order": order,
                    "reset_period": reset_period,
                    "usage_limit": usage_limit,
                    "weekly_reset_period_configuration": weekly_reset_period_configuration,
                    "yearly_reset_period_configuration": yearly_reset_period_configuration,
                    "amount": amount,
                    "cadence": cadence,
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
