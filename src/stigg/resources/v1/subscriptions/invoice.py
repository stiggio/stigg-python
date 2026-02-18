# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Query, Headers, NotGiven, not_given
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.v1.subscriptions.invoice_mark_as_paid_response import InvoiceMarkAsPaidResponse

__all__ = ["InvoiceResource", "AsyncInvoiceResource"]


class InvoiceResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InvoiceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stiggio/stigg-python#accessing-raw-response-data-eg-headers
        """
        return InvoiceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InvoiceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stiggio/stigg-python#with_streaming_response
        """
        return InvoiceResourceWithStreamingResponse(self)

    def mark_as_paid(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InvoiceMarkAsPaidResponse:
        """Marks the latest invoice of a subscription as paid in the billing provider.

        The
        invoice must exist and have an OPEN status.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/api/v1/subscriptions/{id}/invoice/paid",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InvoiceMarkAsPaidResponse,
        )


class AsyncInvoiceResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInvoiceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stiggio/stigg-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInvoiceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInvoiceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stiggio/stigg-python#with_streaming_response
        """
        return AsyncInvoiceResourceWithStreamingResponse(self)

    async def mark_as_paid(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InvoiceMarkAsPaidResponse:
        """Marks the latest invoice of a subscription as paid in the billing provider.

        The
        invoice must exist and have an OPEN status.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/api/v1/subscriptions/{id}/invoice/paid",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InvoiceMarkAsPaidResponse,
        )


class InvoiceResourceWithRawResponse:
    def __init__(self, invoice: InvoiceResource) -> None:
        self._invoice = invoice

        self.mark_as_paid = to_raw_response_wrapper(
            invoice.mark_as_paid,
        )


class AsyncInvoiceResourceWithRawResponse:
    def __init__(self, invoice: AsyncInvoiceResource) -> None:
        self._invoice = invoice

        self.mark_as_paid = async_to_raw_response_wrapper(
            invoice.mark_as_paid,
        )


class InvoiceResourceWithStreamingResponse:
    def __init__(self, invoice: InvoiceResource) -> None:
        self._invoice = invoice

        self.mark_as_paid = to_streamed_response_wrapper(
            invoice.mark_as_paid,
        )


class AsyncInvoiceResourceWithStreamingResponse:
    def __init__(self, invoice: AsyncInvoiceResource) -> None:
        self._invoice = invoice

        self.mark_as_paid = async_to_streamed_response_wrapper(
            invoice.mark_as_paid,
        )
