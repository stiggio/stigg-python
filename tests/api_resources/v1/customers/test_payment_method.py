# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from stigg import Stigg, AsyncStigg
from tests.utils import assert_matches_type
from stigg.types.v1 import CustomerResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPaymentMethod:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_attach(self, client: Stigg) -> None:
        payment_method = client.v1.customers.payment_method.attach(
            id="x",
            integration_id="integrationId",
            payment_method_id="paymentMethodId",
            vendor_identifier="AUTH0",
        )
        assert_matches_type(CustomerResponse, payment_method, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_attach_with_all_params(self, client: Stigg) -> None:
        payment_method = client.v1.customers.payment_method.attach(
            id="x",
            integration_id="integrationId",
            payment_method_id="paymentMethodId",
            vendor_identifier="AUTH0",
            billing_currency="usd",
        )
        assert_matches_type(CustomerResponse, payment_method, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_attach(self, client: Stigg) -> None:
        response = client.v1.customers.payment_method.with_raw_response.attach(
            id="x",
            integration_id="integrationId",
            payment_method_id="paymentMethodId",
            vendor_identifier="AUTH0",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_method = response.parse()
        assert_matches_type(CustomerResponse, payment_method, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_attach(self, client: Stigg) -> None:
        with client.v1.customers.payment_method.with_streaming_response.attach(
            id="x",
            integration_id="integrationId",
            payment_method_id="paymentMethodId",
            vendor_identifier="AUTH0",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_method = response.parse()
            assert_matches_type(CustomerResponse, payment_method, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_attach(self, client: Stigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v1.customers.payment_method.with_raw_response.attach(
                id="",
                integration_id="integrationId",
                payment_method_id="paymentMethodId",
                vendor_identifier="AUTH0",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_detach(self, client: Stigg) -> None:
        payment_method = client.v1.customers.payment_method.detach(
            "x",
        )
        assert_matches_type(CustomerResponse, payment_method, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_detach(self, client: Stigg) -> None:
        response = client.v1.customers.payment_method.with_raw_response.detach(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_method = response.parse()
        assert_matches_type(CustomerResponse, payment_method, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_detach(self, client: Stigg) -> None:
        with client.v1.customers.payment_method.with_streaming_response.detach(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_method = response.parse()
            assert_matches_type(CustomerResponse, payment_method, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_detach(self, client: Stigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v1.customers.payment_method.with_raw_response.detach(
                "",
            )


class TestAsyncPaymentMethod:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_attach(self, async_client: AsyncStigg) -> None:
        payment_method = await async_client.v1.customers.payment_method.attach(
            id="x",
            integration_id="integrationId",
            payment_method_id="paymentMethodId",
            vendor_identifier="AUTH0",
        )
        assert_matches_type(CustomerResponse, payment_method, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_attach_with_all_params(self, async_client: AsyncStigg) -> None:
        payment_method = await async_client.v1.customers.payment_method.attach(
            id="x",
            integration_id="integrationId",
            payment_method_id="paymentMethodId",
            vendor_identifier="AUTH0",
            billing_currency="usd",
        )
        assert_matches_type(CustomerResponse, payment_method, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_attach(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.customers.payment_method.with_raw_response.attach(
            id="x",
            integration_id="integrationId",
            payment_method_id="paymentMethodId",
            vendor_identifier="AUTH0",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_method = await response.parse()
        assert_matches_type(CustomerResponse, payment_method, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_attach(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.customers.payment_method.with_streaming_response.attach(
            id="x",
            integration_id="integrationId",
            payment_method_id="paymentMethodId",
            vendor_identifier="AUTH0",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_method = await response.parse()
            assert_matches_type(CustomerResponse, payment_method, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_attach(self, async_client: AsyncStigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v1.customers.payment_method.with_raw_response.attach(
                id="",
                integration_id="integrationId",
                payment_method_id="paymentMethodId",
                vendor_identifier="AUTH0",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_detach(self, async_client: AsyncStigg) -> None:
        payment_method = await async_client.v1.customers.payment_method.detach(
            "x",
        )
        assert_matches_type(CustomerResponse, payment_method, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_detach(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.customers.payment_method.with_raw_response.detach(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_method = await response.parse()
        assert_matches_type(CustomerResponse, payment_method, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_detach(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.customers.payment_method.with_streaming_response.detach(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_method = await response.parse()
            assert_matches_type(CustomerResponse, payment_method, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_detach(self, async_client: AsyncStigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v1.customers.payment_method.with_raw_response.detach(
                "",
            )
