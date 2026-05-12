# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from stigg import Stigg, AsyncStigg
from tests.utils import assert_matches_type
from stigg.types.v1.credits import AutoRechargeGetAutoRechargeResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAutoRecharge:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_auto_recharge(self, client: Stigg) -> None:
        auto_recharge = client.v1.credits.auto_recharge.get_auto_recharge(
            currency_id="currencyId",
            customer_id="customerId",
        )
        assert_matches_type(AutoRechargeGetAutoRechargeResponse, auto_recharge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_auto_recharge(self, client: Stigg) -> None:
        response = client.v1.credits.auto_recharge.with_raw_response.get_auto_recharge(
            currency_id="currencyId",
            customer_id="customerId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auto_recharge = response.parse()
        assert_matches_type(AutoRechargeGetAutoRechargeResponse, auto_recharge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_auto_recharge(self, client: Stigg) -> None:
        with client.v1.credits.auto_recharge.with_streaming_response.get_auto_recharge(
            currency_id="currencyId",
            customer_id="customerId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auto_recharge = response.parse()
            assert_matches_type(AutoRechargeGetAutoRechargeResponse, auto_recharge, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAutoRecharge:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_auto_recharge(self, async_client: AsyncStigg) -> None:
        auto_recharge = await async_client.v1.credits.auto_recharge.get_auto_recharge(
            currency_id="currencyId",
            customer_id="customerId",
        )
        assert_matches_type(AutoRechargeGetAutoRechargeResponse, auto_recharge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_auto_recharge(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.credits.auto_recharge.with_raw_response.get_auto_recharge(
            currency_id="currencyId",
            customer_id="customerId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auto_recharge = await response.parse()
        assert_matches_type(AutoRechargeGetAutoRechargeResponse, auto_recharge, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_auto_recharge(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.credits.auto_recharge.with_streaming_response.get_auto_recharge(
            currency_id="currencyId",
            customer_id="customerId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auto_recharge = await response.parse()
            assert_matches_type(AutoRechargeGetAutoRechargeResponse, auto_recharge, path=["response"])

        assert cast(Any, response.is_closed) is True
