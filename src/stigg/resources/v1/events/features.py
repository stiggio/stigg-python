# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Literal

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
from ....types.v1.events import (
    feature_list_features_params,
    feature_create_feature_params,
    feature_update_feature_params,
)
from ....types.v1.events.feature import Feature
from ....types.v1.events.feature_list_features_response import FeatureListFeaturesResponse

__all__ = ["FeaturesResource", "AsyncFeaturesResource"]


class FeaturesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FeaturesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stiggio/stigg-python#accessing-raw-response-data-eg-headers
        """
        return FeaturesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FeaturesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stiggio/stigg-python#with_streaming_response
        """
        return FeaturesResourceWithStreamingResponse(self)

    def archive_feature(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Feature:
        """
        Archives a feature, preventing it from being used in new entitlements.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/api/v1/features/{id}/archive",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Feature,
        )

    def create_feature(
        self,
        *,
        id: str,
        display_name: str,
        feature_type: Literal["BOOLEAN", "NUMBER", "ENUM"],
        description: str | Omit = omit,
        enum_configuration: Iterable[feature_create_feature_params.EnumConfiguration] | Omit = omit,
        feature_status: Literal["NEW", "SUSPENDED", "ACTIVE"] | Omit = omit,
        feature_units: str | Omit = omit,
        feature_units_plural: str | Omit = omit,
        metadata: Dict[str, str] | Omit = omit,
        meter_type: Literal["None", "FLUCTUATING", "INCREMENTAL"] | Omit = omit,
        unit_transformation: Optional[feature_create_feature_params.UnitTransformation] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Feature:
        """
        Creates a new feature with the specified type, metering, and configuration.

        Args:
          id: The unique identifier for the feature

          display_name: The display name for the feature

          feature_type: The type of the feature

          description: The description for the feature

          enum_configuration: The configuration data for the feature

          feature_status: The status of the feature

          feature_units: The units for the feature

          feature_units_plural: The plural units for the feature

          metadata: The additional metadata for the feature

          meter_type: The meter type for the feature

          unit_transformation: Unit transformation to be applied to the reported usage

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/features",
            body=maybe_transform(
                {
                    "id": id,
                    "display_name": display_name,
                    "feature_type": feature_type,
                    "description": description,
                    "enum_configuration": enum_configuration,
                    "feature_status": feature_status,
                    "feature_units": feature_units,
                    "feature_units_plural": feature_units_plural,
                    "metadata": metadata,
                    "meter_type": meter_type,
                    "unit_transformation": unit_transformation,
                },
                feature_create_feature_params.FeatureCreateFeatureParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Feature,
        )

    def list_features(
        self,
        *,
        id: str | Omit = omit,
        after: str | Omit = omit,
        before: str | Omit = omit,
        created_at: feature_list_features_params.CreatedAt | Omit = omit,
        feature_type: str | Omit = omit,
        limit: int | Omit = omit,
        meter_type: str | Omit = omit,
        status: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncMyCursorIDPage[FeatureListFeaturesResponse]:
        """
        Retrieves a paginated list of features in the environment.

        Args:
          id: Filter by entity ID

          after: Return items that come after this cursor

          before: Return items that come before this cursor

          created_at: Filter by creation date using range operators: gt, gte, lt, lte

          feature_type: Filter by feature type. Supports comma-separated values for multiple types

          limit: Maximum number of items to return

          meter_type: Filter by meter type. Supports comma-separated values for multiple types

          status: Filter by feature status. Supports comma-separated values for multiple statuses

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/v1/features",
            page=SyncMyCursorIDPage[FeatureListFeaturesResponse],
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
                        "feature_type": feature_type,
                        "limit": limit,
                        "meter_type": meter_type,
                        "status": status,
                    },
                    feature_list_features_params.FeatureListFeaturesParams,
                ),
            ),
            model=FeatureListFeaturesResponse,
        )

    def retrieve_feature(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Feature:
        """
        Retrieves a feature by its unique identifier.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/api/v1/features/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Feature,
        )

    def unarchive_feature(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Feature:
        """
        Restores an archived feature, allowing it to be used in entitlements again.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/api/v1/features/{id}/unarchive",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Feature,
        )

    def update_feature(
        self,
        id: str,
        *,
        description: str | Omit = omit,
        display_name: str | Omit = omit,
        enum_configuration: Iterable[feature_update_feature_params.EnumConfiguration] | Omit = omit,
        feature_units: str | Omit = omit,
        feature_units_plural: str | Omit = omit,
        metadata: Dict[str, str] | Omit = omit,
        meter: feature_update_feature_params.Meter | Omit = omit,
        unit_transformation: Optional[feature_update_feature_params.UnitTransformation] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Feature:
        """
        Updates an existing feature's properties such as display name, description, and
        configuration.

        Args:
          description: The description for the feature

          display_name: The display name for the feature

          enum_configuration: The configuration data for the feature

          feature_units: The units for the feature

          feature_units_plural: The plural units for the feature

          metadata: The additional metadata for the feature

          unit_transformation: Unit transformation to be applied to the reported usage

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/api/v1/features/{id}",
            body=maybe_transform(
                {
                    "description": description,
                    "display_name": display_name,
                    "enum_configuration": enum_configuration,
                    "feature_units": feature_units,
                    "feature_units_plural": feature_units_plural,
                    "metadata": metadata,
                    "meter": meter,
                    "unit_transformation": unit_transformation,
                },
                feature_update_feature_params.FeatureUpdateFeatureParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Feature,
        )


class AsyncFeaturesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFeaturesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stiggio/stigg-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFeaturesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFeaturesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stiggio/stigg-python#with_streaming_response
        """
        return AsyncFeaturesResourceWithStreamingResponse(self)

    async def archive_feature(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Feature:
        """
        Archives a feature, preventing it from being used in new entitlements.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/api/v1/features/{id}/archive",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Feature,
        )

    async def create_feature(
        self,
        *,
        id: str,
        display_name: str,
        feature_type: Literal["BOOLEAN", "NUMBER", "ENUM"],
        description: str | Omit = omit,
        enum_configuration: Iterable[feature_create_feature_params.EnumConfiguration] | Omit = omit,
        feature_status: Literal["NEW", "SUSPENDED", "ACTIVE"] | Omit = omit,
        feature_units: str | Omit = omit,
        feature_units_plural: str | Omit = omit,
        metadata: Dict[str, str] | Omit = omit,
        meter_type: Literal["None", "FLUCTUATING", "INCREMENTAL"] | Omit = omit,
        unit_transformation: Optional[feature_create_feature_params.UnitTransformation] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Feature:
        """
        Creates a new feature with the specified type, metering, and configuration.

        Args:
          id: The unique identifier for the feature

          display_name: The display name for the feature

          feature_type: The type of the feature

          description: The description for the feature

          enum_configuration: The configuration data for the feature

          feature_status: The status of the feature

          feature_units: The units for the feature

          feature_units_plural: The plural units for the feature

          metadata: The additional metadata for the feature

          meter_type: The meter type for the feature

          unit_transformation: Unit transformation to be applied to the reported usage

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/features",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "display_name": display_name,
                    "feature_type": feature_type,
                    "description": description,
                    "enum_configuration": enum_configuration,
                    "feature_status": feature_status,
                    "feature_units": feature_units,
                    "feature_units_plural": feature_units_plural,
                    "metadata": metadata,
                    "meter_type": meter_type,
                    "unit_transformation": unit_transformation,
                },
                feature_create_feature_params.FeatureCreateFeatureParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Feature,
        )

    def list_features(
        self,
        *,
        id: str | Omit = omit,
        after: str | Omit = omit,
        before: str | Omit = omit,
        created_at: feature_list_features_params.CreatedAt | Omit = omit,
        feature_type: str | Omit = omit,
        limit: int | Omit = omit,
        meter_type: str | Omit = omit,
        status: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[FeatureListFeaturesResponse, AsyncMyCursorIDPage[FeatureListFeaturesResponse]]:
        """
        Retrieves a paginated list of features in the environment.

        Args:
          id: Filter by entity ID

          after: Return items that come after this cursor

          before: Return items that come before this cursor

          created_at: Filter by creation date using range operators: gt, gte, lt, lte

          feature_type: Filter by feature type. Supports comma-separated values for multiple types

          limit: Maximum number of items to return

          meter_type: Filter by meter type. Supports comma-separated values for multiple types

          status: Filter by feature status. Supports comma-separated values for multiple statuses

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/v1/features",
            page=AsyncMyCursorIDPage[FeatureListFeaturesResponse],
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
                        "feature_type": feature_type,
                        "limit": limit,
                        "meter_type": meter_type,
                        "status": status,
                    },
                    feature_list_features_params.FeatureListFeaturesParams,
                ),
            ),
            model=FeatureListFeaturesResponse,
        )

    async def retrieve_feature(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Feature:
        """
        Retrieves a feature by its unique identifier.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/api/v1/features/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Feature,
        )

    async def unarchive_feature(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Feature:
        """
        Restores an archived feature, allowing it to be used in entitlements again.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/api/v1/features/{id}/unarchive",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Feature,
        )

    async def update_feature(
        self,
        id: str,
        *,
        description: str | Omit = omit,
        display_name: str | Omit = omit,
        enum_configuration: Iterable[feature_update_feature_params.EnumConfiguration] | Omit = omit,
        feature_units: str | Omit = omit,
        feature_units_plural: str | Omit = omit,
        metadata: Dict[str, str] | Omit = omit,
        meter: feature_update_feature_params.Meter | Omit = omit,
        unit_transformation: Optional[feature_update_feature_params.UnitTransformation] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Feature:
        """
        Updates an existing feature's properties such as display name, description, and
        configuration.

        Args:
          description: The description for the feature

          display_name: The display name for the feature

          enum_configuration: The configuration data for the feature

          feature_units: The units for the feature

          feature_units_plural: The plural units for the feature

          metadata: The additional metadata for the feature

          unit_transformation: Unit transformation to be applied to the reported usage

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/api/v1/features/{id}",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "display_name": display_name,
                    "enum_configuration": enum_configuration,
                    "feature_units": feature_units,
                    "feature_units_plural": feature_units_plural,
                    "metadata": metadata,
                    "meter": meter,
                    "unit_transformation": unit_transformation,
                },
                feature_update_feature_params.FeatureUpdateFeatureParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Feature,
        )


class FeaturesResourceWithRawResponse:
    def __init__(self, features: FeaturesResource) -> None:
        self._features = features

        self.archive_feature = to_raw_response_wrapper(
            features.archive_feature,
        )
        self.create_feature = to_raw_response_wrapper(
            features.create_feature,
        )
        self.list_features = to_raw_response_wrapper(
            features.list_features,
        )
        self.retrieve_feature = to_raw_response_wrapper(
            features.retrieve_feature,
        )
        self.unarchive_feature = to_raw_response_wrapper(
            features.unarchive_feature,
        )
        self.update_feature = to_raw_response_wrapper(
            features.update_feature,
        )


class AsyncFeaturesResourceWithRawResponse:
    def __init__(self, features: AsyncFeaturesResource) -> None:
        self._features = features

        self.archive_feature = async_to_raw_response_wrapper(
            features.archive_feature,
        )
        self.create_feature = async_to_raw_response_wrapper(
            features.create_feature,
        )
        self.list_features = async_to_raw_response_wrapper(
            features.list_features,
        )
        self.retrieve_feature = async_to_raw_response_wrapper(
            features.retrieve_feature,
        )
        self.unarchive_feature = async_to_raw_response_wrapper(
            features.unarchive_feature,
        )
        self.update_feature = async_to_raw_response_wrapper(
            features.update_feature,
        )


class FeaturesResourceWithStreamingResponse:
    def __init__(self, features: FeaturesResource) -> None:
        self._features = features

        self.archive_feature = to_streamed_response_wrapper(
            features.archive_feature,
        )
        self.create_feature = to_streamed_response_wrapper(
            features.create_feature,
        )
        self.list_features = to_streamed_response_wrapper(
            features.list_features,
        )
        self.retrieve_feature = to_streamed_response_wrapper(
            features.retrieve_feature,
        )
        self.unarchive_feature = to_streamed_response_wrapper(
            features.unarchive_feature,
        )
        self.update_feature = to_streamed_response_wrapper(
            features.update_feature,
        )


class AsyncFeaturesResourceWithStreamingResponse:
    def __init__(self, features: AsyncFeaturesResource) -> None:
        self._features = features

        self.archive_feature = async_to_streamed_response_wrapper(
            features.archive_feature,
        )
        self.create_feature = async_to_streamed_response_wrapper(
            features.create_feature,
        )
        self.list_features = async_to_streamed_response_wrapper(
            features.list_features,
        )
        self.retrieve_feature = async_to_streamed_response_wrapper(
            features.retrieve_feature,
        )
        self.unarchive_feature = async_to_streamed_response_wrapper(
            features.unarchive_feature,
        )
        self.update_feature = async_to_streamed_response_wrapper(
            features.update_feature,
        )
