# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from stigg import Stigg, AsyncStigg
from stigg.types import V1RetrieveCustomerResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestV1:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_customer(self, client: Stigg) -> None:
        v1 = client.v1.retrieve_customer(
            ref_id="refId",
            x_api_key="X-API-KEY",
            x_environment_id="X-ENVIRONMENT-ID",
        )
        assert_matches_type(V1RetrieveCustomerResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve_customer(self, client: Stigg) -> None:
        response = client.v1.with_raw_response.retrieve_customer(
            ref_id="refId",
            x_api_key="X-API-KEY",
            x_environment_id="X-ENVIRONMENT-ID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1RetrieveCustomerResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve_customer(self, client: Stigg) -> None:
        with client.v1.with_streaming_response.retrieve_customer(
            ref_id="refId",
            x_api_key="X-API-KEY",
            x_environment_id="X-ENVIRONMENT-ID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1RetrieveCustomerResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve_customer(self, client: Stigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ref_id` but received ''"):
            client.v1.with_raw_response.retrieve_customer(
                ref_id="",
                x_api_key="X-API-KEY",
                x_environment_id="X-ENVIRONMENT-ID",
            )


class TestAsyncV1:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_customer(self, async_client: AsyncStigg) -> None:
        v1 = await async_client.v1.retrieve_customer(
            ref_id="refId",
            x_api_key="X-API-KEY",
            x_environment_id="X-ENVIRONMENT-ID",
        )
        assert_matches_type(V1RetrieveCustomerResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve_customer(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.with_raw_response.retrieve_customer(
            ref_id="refId",
            x_api_key="X-API-KEY",
            x_environment_id="X-ENVIRONMENT-ID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1RetrieveCustomerResponse, v1, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve_customer(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.with_streaming_response.retrieve_customer(
            ref_id="refId",
            x_api_key="X-API-KEY",
            x_environment_id="X-ENVIRONMENT-ID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1RetrieveCustomerResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve_customer(self, async_client: AsyncStigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ref_id` but received ''"):
            await async_client.v1.with_raw_response.retrieve_customer(
                ref_id="",
                x_api_key="X-API-KEY",
                x_environment_id="X-ENVIRONMENT-ID",
            )
