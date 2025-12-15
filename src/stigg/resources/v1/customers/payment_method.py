# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
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
from ...._base_client import make_request_options
from ....types.v1.customers import payment_method_attach_params
from ....types.v1.customer_response import CustomerResponse

__all__ = ["PaymentMethodResource", "AsyncPaymentMethodResource"]


class PaymentMethodResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PaymentMethodResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/stigg-python#accessing-raw-response-data-eg-headers
        """
        return PaymentMethodResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PaymentMethodResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/stigg-python#with_streaming_response
        """
        return PaymentMethodResourceWithStreamingResponse(self)

    def attach(
        self,
        id: str,
        *,
        integration_id: str,
        payment_method_id: str,
        vendor_identifier: Literal[
            "AUTH0",
            "ZUORA",
            "STRIPE",
            "HUBSPOT",
            "AWS_MARKETPLACE",
            "SNOWFLAKE",
            "SALESFORCE",
            "BIG_QUERY",
            "OPEN_FGA",
            "APP_STORE",
        ],
        billing_currency: Optional[
            Literal[
                "usd",
                "aed",
                "all",
                "amd",
                "ang",
                "aud",
                "awg",
                "azn",
                "bam",
                "bbd",
                "bdt",
                "bgn",
                "bif",
                "bmd",
                "bnd",
                "bsd",
                "bwp",
                "byn",
                "bzd",
                "brl",
                "cad",
                "cdf",
                "chf",
                "cny",
                "czk",
                "dkk",
                "dop",
                "dzd",
                "egp",
                "etb",
                "eur",
                "fjd",
                "gbp",
                "gel",
                "gip",
                "gmd",
                "gyd",
                "hkd",
                "hrk",
                "htg",
                "idr",
                "ils",
                "inr",
                "isk",
                "jmd",
                "jpy",
                "kes",
                "kgs",
                "khr",
                "kmf",
                "krw",
                "kyd",
                "kzt",
                "lbp",
                "lkr",
                "lrd",
                "lsl",
                "mad",
                "mdl",
                "mga",
                "mkd",
                "mmk",
                "mnt",
                "mop",
                "mro",
                "mvr",
                "mwk",
                "mxn",
                "myr",
                "mzn",
                "nad",
                "ngn",
                "nok",
                "npr",
                "nzd",
                "pgk",
                "php",
                "pkr",
                "pln",
                "qar",
                "ron",
                "rsd",
                "rub",
                "rwf",
                "sar",
                "sbd",
                "scr",
                "sek",
                "sgd",
                "sle",
                "sll",
                "sos",
                "szl",
                "thb",
                "tjs",
                "top",
                "try",
                "ttd",
                "tzs",
                "uah",
                "uzs",
                "vnd",
                "vuv",
                "wst",
                "xaf",
                "xcd",
                "yer",
                "zar",
                "zmw",
                "clp",
                "djf",
                "gnf",
                "ugx",
                "pyg",
                "xof",
                "xpf",
            ]
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomerResponse:
        """
        Perform payment-method attachment on a Customer

        Args:
          integration_id: Integration details

          payment_method_id: Billing provider payment method id

          vendor_identifier: The vendor identifier of integration

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/api/v1/customers/{id}/payment-method",
            body=maybe_transform(
                {
                    "integration_id": integration_id,
                    "payment_method_id": payment_method_id,
                    "vendor_identifier": vendor_identifier,
                    "billing_currency": billing_currency,
                },
                payment_method_attach_params.PaymentMethodAttachParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerResponse,
        )

    def detach(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomerResponse:
        """
        Perform payment-method detachment on a Customer

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/api/v1/customers/{id}/payment-method",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerResponse,
        )


class AsyncPaymentMethodResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPaymentMethodResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/stigg-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPaymentMethodResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPaymentMethodResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/stigg-python#with_streaming_response
        """
        return AsyncPaymentMethodResourceWithStreamingResponse(self)

    async def attach(
        self,
        id: str,
        *,
        integration_id: str,
        payment_method_id: str,
        vendor_identifier: Literal[
            "AUTH0",
            "ZUORA",
            "STRIPE",
            "HUBSPOT",
            "AWS_MARKETPLACE",
            "SNOWFLAKE",
            "SALESFORCE",
            "BIG_QUERY",
            "OPEN_FGA",
            "APP_STORE",
        ],
        billing_currency: Optional[
            Literal[
                "usd",
                "aed",
                "all",
                "amd",
                "ang",
                "aud",
                "awg",
                "azn",
                "bam",
                "bbd",
                "bdt",
                "bgn",
                "bif",
                "bmd",
                "bnd",
                "bsd",
                "bwp",
                "byn",
                "bzd",
                "brl",
                "cad",
                "cdf",
                "chf",
                "cny",
                "czk",
                "dkk",
                "dop",
                "dzd",
                "egp",
                "etb",
                "eur",
                "fjd",
                "gbp",
                "gel",
                "gip",
                "gmd",
                "gyd",
                "hkd",
                "hrk",
                "htg",
                "idr",
                "ils",
                "inr",
                "isk",
                "jmd",
                "jpy",
                "kes",
                "kgs",
                "khr",
                "kmf",
                "krw",
                "kyd",
                "kzt",
                "lbp",
                "lkr",
                "lrd",
                "lsl",
                "mad",
                "mdl",
                "mga",
                "mkd",
                "mmk",
                "mnt",
                "mop",
                "mro",
                "mvr",
                "mwk",
                "mxn",
                "myr",
                "mzn",
                "nad",
                "ngn",
                "nok",
                "npr",
                "nzd",
                "pgk",
                "php",
                "pkr",
                "pln",
                "qar",
                "ron",
                "rsd",
                "rub",
                "rwf",
                "sar",
                "sbd",
                "scr",
                "sek",
                "sgd",
                "sle",
                "sll",
                "sos",
                "szl",
                "thb",
                "tjs",
                "top",
                "try",
                "ttd",
                "tzs",
                "uah",
                "uzs",
                "vnd",
                "vuv",
                "wst",
                "xaf",
                "xcd",
                "yer",
                "zar",
                "zmw",
                "clp",
                "djf",
                "gnf",
                "ugx",
                "pyg",
                "xof",
                "xpf",
            ]
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomerResponse:
        """
        Perform payment-method attachment on a Customer

        Args:
          integration_id: Integration details

          payment_method_id: Billing provider payment method id

          vendor_identifier: The vendor identifier of integration

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/api/v1/customers/{id}/payment-method",
            body=await async_maybe_transform(
                {
                    "integration_id": integration_id,
                    "payment_method_id": payment_method_id,
                    "vendor_identifier": vendor_identifier,
                    "billing_currency": billing_currency,
                },
                payment_method_attach_params.PaymentMethodAttachParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerResponse,
        )

    async def detach(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomerResponse:
        """
        Perform payment-method detachment on a Customer

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/api/v1/customers/{id}/payment-method",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerResponse,
        )


class PaymentMethodResourceWithRawResponse:
    def __init__(self, payment_method: PaymentMethodResource) -> None:
        self._payment_method = payment_method

        self.attach = to_raw_response_wrapper(
            payment_method.attach,
        )
        self.detach = to_raw_response_wrapper(
            payment_method.detach,
        )


class AsyncPaymentMethodResourceWithRawResponse:
    def __init__(self, payment_method: AsyncPaymentMethodResource) -> None:
        self._payment_method = payment_method

        self.attach = async_to_raw_response_wrapper(
            payment_method.attach,
        )
        self.detach = async_to_raw_response_wrapper(
            payment_method.detach,
        )


class PaymentMethodResourceWithStreamingResponse:
    def __init__(self, payment_method: PaymentMethodResource) -> None:
        self._payment_method = payment_method

        self.attach = to_streamed_response_wrapper(
            payment_method.attach,
        )
        self.detach = to_streamed_response_wrapper(
            payment_method.detach,
        )


class AsyncPaymentMethodResourceWithStreamingResponse:
    def __init__(self, payment_method: AsyncPaymentMethodResource) -> None:
        self._payment_method = payment_method

        self.attach = async_to_streamed_response_wrapper(
            payment_method.attach,
        )
        self.detach = async_to_streamed_response_wrapper(
            payment_method.detach,
        )
