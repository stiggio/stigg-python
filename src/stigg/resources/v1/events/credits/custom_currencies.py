# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional
from typing_extensions import Literal

import httpx

from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ....._utils import path_template, maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .....pagination import SyncMyCursorIDPage, AsyncMyCursorIDPage
from ....._base_client import AsyncPaginator, make_request_options
from .....types.v1.events.credits import (
    custom_currency_list_params,
    custom_currency_create_params,
    custom_currency_update_params,
)
from .....types.v1.events.credits.custom_currency_list_response import CustomCurrencyListResponse
from .....types.v1.events.credits.custom_currency_create_response import CustomCurrencyCreateResponse
from .....types.v1.events.credits.custom_currency_update_response import CustomCurrencyUpdateResponse
from .....types.v1.events.credits.custom_currency_archive_response import CustomCurrencyArchiveResponse
from .....types.v1.events.credits.custom_currency_unarchive_response import CustomCurrencyUnarchiveResponse
from .....types.v1.events.credits.custom_currency_list_associated_entities_response import (
    CustomCurrencyListAssociatedEntitiesResponse,
)

__all__ = ["CustomCurrenciesResource", "AsyncCustomCurrenciesResource"]


class CustomCurrenciesResource(SyncAPIResource):
    """Operations related to custom currencies"""

    @cached_property
    def with_raw_response(self) -> CustomCurrenciesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stiggio/stigg-python#accessing-raw-response-data-eg-headers
        """
        return CustomCurrenciesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CustomCurrenciesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stiggio/stigg-python#with_streaming_response
        """
        return CustomCurrenciesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        id: str,
        display_name: str,
        description: str | Omit = omit,
        metadata: Dict[str, str] | Omit = omit,
        symbol: str | Omit = omit,
        units: custom_currency_create_params.Units | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomCurrencyCreateResponse:
        """
        Creates a new custom currency in the environment.

        Args:
          id: The unique identifier for the new custom currency

          display_name: The display name of the custom currency

          description: Description of the currency

          metadata: Additional metadata to attach to the custom currency

          symbol: The symbol used to represent the custom currency

          units: Singular and plural unit labels for a custom currency. Both fields are required
              when supplied.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/credits/custom-currencies",
            body=maybe_transform(
                {
                    "id": id,
                    "display_name": display_name,
                    "description": description,
                    "metadata": metadata,
                    "symbol": symbol,
                    "units": units,
                },
                custom_currency_create_params.CustomCurrencyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomCurrencyCreateResponse,
        )

    def update(
        self,
        currency_id: str,
        *,
        description: Optional[str] | Omit = omit,
        display_name: str | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        symbol: Optional[str] | Omit = omit,
        units: custom_currency_update_params.Units | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomCurrencyUpdateResponse:
        """Updates an existing custom currency.

        Only the supplied fields are modified.

        Args:
          description: A human-readable description of the custom currency. Send an empty string to
              clear.

          display_name: The display name of the custom currency

          metadata: Additional metadata to attach to the custom currency

          symbol: The symbol used to represent the custom currency. Send an empty string to clear.

          units: Singular and plural unit labels for a custom currency. Both fields are required
              when supplied.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not currency_id:
            raise ValueError(f"Expected a non-empty value for `currency_id` but received {currency_id!r}")
        return self._patch(
            path_template("/api/v1/credits/custom-currencies/{currency_id}", currency_id=currency_id),
            body=maybe_transform(
                {
                    "description": description,
                    "display_name": display_name,
                    "metadata": metadata,
                    "symbol": symbol,
                    "units": units,
                },
                custom_currency_update_params.CustomCurrencyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomCurrencyUpdateResponse,
        )

    def list(
        self,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        limit: int | Omit = omit,
        status: List[Literal["ACTIVE", "ARCHIVED"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncMyCursorIDPage[CustomCurrencyListResponse]:
        """Retrieves a paginated list of custom currencies in the environment.

        Archived
        currencies are excluded by default; pass `status=ARCHIVED` (or
        `status=ACTIVE,ARCHIVED`) to include them.

        Args:
          after: Return items that come after this cursor

          before: Return items that come before this cursor

          limit: Maximum number of items to return

          status: Filter by custom currency status. Supports comma-separated values (e.g.,
              `ACTIVE,ARCHIVED`). Defaults to `ACTIVE`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/v1/credits/custom-currencies",
            page=SyncMyCursorIDPage[CustomCurrencyListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "limit": limit,
                        "status": status,
                    },
                    custom_currency_list_params.CustomCurrencyListParams,
                ),
            ),
            model=CustomCurrencyListResponse,
        )

    def archive(
        self,
        currency_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomCurrencyArchiveResponse:
        """Archives a custom currency.

        Fails if the currency is still associated with any
        active plan or addon — use the associated-entities endpoint first to inspect
        dependencies.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not currency_id:
            raise ValueError(f"Expected a non-empty value for `currency_id` but received {currency_id!r}")
        return self._post(
            path_template("/api/v1/credits/custom-currencies/{currency_id}/archive", currency_id=currency_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomCurrencyArchiveResponse,
        )

    def list_associated_entities(
        self,
        currency_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomCurrencyListAssociatedEntitiesResponse:
        """Lists the active plans and addons that reference a custom currency.

        Useful
        before archiving to inspect dependencies.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not currency_id:
            raise ValueError(f"Expected a non-empty value for `currency_id` but received {currency_id!r}")
        return self._get(
            path_template(
                "/api/v1/credits/custom-currencies/{currency_id}/associated-entities", currency_id=currency_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomCurrencyListAssociatedEntitiesResponse,
        )

    def unarchive(
        self,
        currency_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomCurrencyUnarchiveResponse:
        """Restores a previously archived custom currency.

        Fails if another active currency
        with the same ID already exists.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not currency_id:
            raise ValueError(f"Expected a non-empty value for `currency_id` but received {currency_id!r}")
        return self._post(
            path_template("/api/v1/credits/custom-currencies/{currency_id}/unarchive", currency_id=currency_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomCurrencyUnarchiveResponse,
        )


class AsyncCustomCurrenciesResource(AsyncAPIResource):
    """Operations related to custom currencies"""

    @cached_property
    def with_raw_response(self) -> AsyncCustomCurrenciesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stiggio/stigg-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCustomCurrenciesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCustomCurrenciesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stiggio/stigg-python#with_streaming_response
        """
        return AsyncCustomCurrenciesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        id: str,
        display_name: str,
        description: str | Omit = omit,
        metadata: Dict[str, str] | Omit = omit,
        symbol: str | Omit = omit,
        units: custom_currency_create_params.Units | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomCurrencyCreateResponse:
        """
        Creates a new custom currency in the environment.

        Args:
          id: The unique identifier for the new custom currency

          display_name: The display name of the custom currency

          description: Description of the currency

          metadata: Additional metadata to attach to the custom currency

          symbol: The symbol used to represent the custom currency

          units: Singular and plural unit labels for a custom currency. Both fields are required
              when supplied.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/credits/custom-currencies",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "display_name": display_name,
                    "description": description,
                    "metadata": metadata,
                    "symbol": symbol,
                    "units": units,
                },
                custom_currency_create_params.CustomCurrencyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomCurrencyCreateResponse,
        )

    async def update(
        self,
        currency_id: str,
        *,
        description: Optional[str] | Omit = omit,
        display_name: str | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        symbol: Optional[str] | Omit = omit,
        units: custom_currency_update_params.Units | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomCurrencyUpdateResponse:
        """Updates an existing custom currency.

        Only the supplied fields are modified.

        Args:
          description: A human-readable description of the custom currency. Send an empty string to
              clear.

          display_name: The display name of the custom currency

          metadata: Additional metadata to attach to the custom currency

          symbol: The symbol used to represent the custom currency. Send an empty string to clear.

          units: Singular and plural unit labels for a custom currency. Both fields are required
              when supplied.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not currency_id:
            raise ValueError(f"Expected a non-empty value for `currency_id` but received {currency_id!r}")
        return await self._patch(
            path_template("/api/v1/credits/custom-currencies/{currency_id}", currency_id=currency_id),
            body=await async_maybe_transform(
                {
                    "description": description,
                    "display_name": display_name,
                    "metadata": metadata,
                    "symbol": symbol,
                    "units": units,
                },
                custom_currency_update_params.CustomCurrencyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomCurrencyUpdateResponse,
        )

    def list(
        self,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        limit: int | Omit = omit,
        status: List[Literal["ACTIVE", "ARCHIVED"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[CustomCurrencyListResponse, AsyncMyCursorIDPage[CustomCurrencyListResponse]]:
        """Retrieves a paginated list of custom currencies in the environment.

        Archived
        currencies are excluded by default; pass `status=ARCHIVED` (or
        `status=ACTIVE,ARCHIVED`) to include them.

        Args:
          after: Return items that come after this cursor

          before: Return items that come before this cursor

          limit: Maximum number of items to return

          status: Filter by custom currency status. Supports comma-separated values (e.g.,
              `ACTIVE,ARCHIVED`). Defaults to `ACTIVE`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/v1/credits/custom-currencies",
            page=AsyncMyCursorIDPage[CustomCurrencyListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "limit": limit,
                        "status": status,
                    },
                    custom_currency_list_params.CustomCurrencyListParams,
                ),
            ),
            model=CustomCurrencyListResponse,
        )

    async def archive(
        self,
        currency_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomCurrencyArchiveResponse:
        """Archives a custom currency.

        Fails if the currency is still associated with any
        active plan or addon — use the associated-entities endpoint first to inspect
        dependencies.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not currency_id:
            raise ValueError(f"Expected a non-empty value for `currency_id` but received {currency_id!r}")
        return await self._post(
            path_template("/api/v1/credits/custom-currencies/{currency_id}/archive", currency_id=currency_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomCurrencyArchiveResponse,
        )

    async def list_associated_entities(
        self,
        currency_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomCurrencyListAssociatedEntitiesResponse:
        """Lists the active plans and addons that reference a custom currency.

        Useful
        before archiving to inspect dependencies.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not currency_id:
            raise ValueError(f"Expected a non-empty value for `currency_id` but received {currency_id!r}")
        return await self._get(
            path_template(
                "/api/v1/credits/custom-currencies/{currency_id}/associated-entities", currency_id=currency_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomCurrencyListAssociatedEntitiesResponse,
        )

    async def unarchive(
        self,
        currency_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomCurrencyUnarchiveResponse:
        """Restores a previously archived custom currency.

        Fails if another active currency
        with the same ID already exists.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not currency_id:
            raise ValueError(f"Expected a non-empty value for `currency_id` but received {currency_id!r}")
        return await self._post(
            path_template("/api/v1/credits/custom-currencies/{currency_id}/unarchive", currency_id=currency_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomCurrencyUnarchiveResponse,
        )


class CustomCurrenciesResourceWithRawResponse:
    def __init__(self, custom_currencies: CustomCurrenciesResource) -> None:
        self._custom_currencies = custom_currencies

        self.create = to_raw_response_wrapper(
            custom_currencies.create,
        )
        self.update = to_raw_response_wrapper(
            custom_currencies.update,
        )
        self.list = to_raw_response_wrapper(
            custom_currencies.list,
        )
        self.archive = to_raw_response_wrapper(
            custom_currencies.archive,
        )
        self.list_associated_entities = to_raw_response_wrapper(
            custom_currencies.list_associated_entities,
        )
        self.unarchive = to_raw_response_wrapper(
            custom_currencies.unarchive,
        )


class AsyncCustomCurrenciesResourceWithRawResponse:
    def __init__(self, custom_currencies: AsyncCustomCurrenciesResource) -> None:
        self._custom_currencies = custom_currencies

        self.create = async_to_raw_response_wrapper(
            custom_currencies.create,
        )
        self.update = async_to_raw_response_wrapper(
            custom_currencies.update,
        )
        self.list = async_to_raw_response_wrapper(
            custom_currencies.list,
        )
        self.archive = async_to_raw_response_wrapper(
            custom_currencies.archive,
        )
        self.list_associated_entities = async_to_raw_response_wrapper(
            custom_currencies.list_associated_entities,
        )
        self.unarchive = async_to_raw_response_wrapper(
            custom_currencies.unarchive,
        )


class CustomCurrenciesResourceWithStreamingResponse:
    def __init__(self, custom_currencies: CustomCurrenciesResource) -> None:
        self._custom_currencies = custom_currencies

        self.create = to_streamed_response_wrapper(
            custom_currencies.create,
        )
        self.update = to_streamed_response_wrapper(
            custom_currencies.update,
        )
        self.list = to_streamed_response_wrapper(
            custom_currencies.list,
        )
        self.archive = to_streamed_response_wrapper(
            custom_currencies.archive,
        )
        self.list_associated_entities = to_streamed_response_wrapper(
            custom_currencies.list_associated_entities,
        )
        self.unarchive = to_streamed_response_wrapper(
            custom_currencies.unarchive,
        )


class AsyncCustomCurrenciesResourceWithStreamingResponse:
    def __init__(self, custom_currencies: AsyncCustomCurrenciesResource) -> None:
        self._custom_currencies = custom_currencies

        self.create = async_to_streamed_response_wrapper(
            custom_currencies.create,
        )
        self.update = async_to_streamed_response_wrapper(
            custom_currencies.update,
        )
        self.list = async_to_streamed_response_wrapper(
            custom_currencies.list,
        )
        self.archive = async_to_streamed_response_wrapper(
            custom_currencies.archive,
        )
        self.list_associated_entities = async_to_streamed_response_wrapper(
            custom_currencies.list_associated_entities,
        )
        self.unarchive = async_to_streamed_response_wrapper(
            custom_currencies.unarchive,
        )
