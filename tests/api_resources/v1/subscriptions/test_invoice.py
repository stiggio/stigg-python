# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from stigg import Stigg, AsyncStigg
from tests.utils import assert_matches_type
from stigg.types.v1.subscriptions import InvoiceMarkAsPaidResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInvoice:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_mark_as_paid(self, client: Stigg) -> None:
        invoice = client.v1.subscriptions.invoice.mark_as_paid(
            "x",
        )
        assert_matches_type(InvoiceMarkAsPaidResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_mark_as_paid(self, client: Stigg) -> None:
        response = client.v1.subscriptions.invoice.with_raw_response.mark_as_paid(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = response.parse()
        assert_matches_type(InvoiceMarkAsPaidResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_mark_as_paid(self, client: Stigg) -> None:
        with client.v1.subscriptions.invoice.with_streaming_response.mark_as_paid(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = response.parse()
            assert_matches_type(InvoiceMarkAsPaidResponse, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_mark_as_paid(self, client: Stigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v1.subscriptions.invoice.with_raw_response.mark_as_paid(
                "",
            )


class TestAsyncInvoice:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_mark_as_paid(self, async_client: AsyncStigg) -> None:
        invoice = await async_client.v1.subscriptions.invoice.mark_as_paid(
            "x",
        )
        assert_matches_type(InvoiceMarkAsPaidResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_mark_as_paid(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.subscriptions.invoice.with_raw_response.mark_as_paid(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invoice = await response.parse()
        assert_matches_type(InvoiceMarkAsPaidResponse, invoice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_mark_as_paid(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.subscriptions.invoice.with_streaming_response.mark_as_paid(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invoice = await response.parse()
            assert_matches_type(InvoiceMarkAsPaidResponse, invoice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_mark_as_paid(self, async_client: AsyncStigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v1.subscriptions.invoice.with_raw_response.mark_as_paid(
                "",
            )
