# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from stigg import Stigg, AsyncStigg
from tests.utils import assert_matches_type
from stigg.types.v2 import CustomerGetCustomerResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCustomers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_customer(self, client: Stigg) -> None:
        customer = client.v2.customers.get_customer(
            ref_id="refId",
            x_api_key="X-API-KEY",
            x_environment_id="X-ENVIRONMENT-ID",
        )
        assert_matches_type(CustomerGetCustomerResponse, customer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_customer(self, client: Stigg) -> None:
        response = client.v2.customers.with_raw_response.get_customer(
            ref_id="refId",
            x_api_key="X-API-KEY",
            x_environment_id="X-ENVIRONMENT-ID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert_matches_type(CustomerGetCustomerResponse, customer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_customer(self, client: Stigg) -> None:
        with client.v2.customers.with_streaming_response.get_customer(
            ref_id="refId",
            x_api_key="X-API-KEY",
            x_environment_id="X-ENVIRONMENT-ID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = response.parse()
            assert_matches_type(CustomerGetCustomerResponse, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get_customer(self, client: Stigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ref_id` but received ''"):
            client.v2.customers.with_raw_response.get_customer(
                ref_id="",
                x_api_key="X-API-KEY",
                x_environment_id="X-ENVIRONMENT-ID",
            )


class TestAsyncCustomers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_customer(self, async_client: AsyncStigg) -> None:
        customer = await async_client.v2.customers.get_customer(
            ref_id="refId",
            x_api_key="X-API-KEY",
            x_environment_id="X-ENVIRONMENT-ID",
        )
        assert_matches_type(CustomerGetCustomerResponse, customer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_customer(self, async_client: AsyncStigg) -> None:
        response = await async_client.v2.customers.with_raw_response.get_customer(
            ref_id="refId",
            x_api_key="X-API-KEY",
            x_environment_id="X-ENVIRONMENT-ID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = await response.parse()
        assert_matches_type(CustomerGetCustomerResponse, customer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_customer(self, async_client: AsyncStigg) -> None:
        async with async_client.v2.customers.with_streaming_response.get_customer(
            ref_id="refId",
            x_api_key="X-API-KEY",
            x_environment_id="X-ENVIRONMENT-ID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = await response.parse()
            assert_matches_type(CustomerGetCustomerResponse, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get_customer(self, async_client: AsyncStigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ref_id` but received ''"):
            await async_client.v2.customers.with_raw_response.get_customer(
                ref_id="",
                x_api_key="X-API-KEY",
                x_environment_id="X-ENVIRONMENT-ID",
            )
