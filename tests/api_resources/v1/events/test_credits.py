# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from stigg import Stigg, AsyncStigg
from tests.utils import assert_matches_type
from stigg._utils import parse_datetime
from stigg.pagination import SyncMyCursorIDPage, AsyncMyCursorIDPage
from stigg.types.v1.events import (
    CreditGetUsageResponse,
    CreditListLedgerResponse,
    CreditGetAutoRechargeResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCredits:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_auto_recharge(self, client: Stigg) -> None:
        credit = client.v1.events.credits.get_auto_recharge(
            currency_id="currencyId",
            customer_id="customerId",
        )
        assert_matches_type(CreditGetAutoRechargeResponse, credit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_auto_recharge(self, client: Stigg) -> None:
        response = client.v1.events.credits.with_raw_response.get_auto_recharge(
            currency_id="currencyId",
            customer_id="customerId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit = response.parse()
        assert_matches_type(CreditGetAutoRechargeResponse, credit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_auto_recharge(self, client: Stigg) -> None:
        with client.v1.events.credits.with_streaming_response.get_auto_recharge(
            currency_id="currencyId",
            customer_id="customerId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit = response.parse()
            assert_matches_type(CreditGetAutoRechargeResponse, credit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_usage(self, client: Stigg) -> None:
        credit = client.v1.events.credits.get_usage(
            customer_id="customerId",
        )
        assert_matches_type(CreditGetUsageResponse, credit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_usage_with_all_params(self, client: Stigg) -> None:
        credit = client.v1.events.credits.get_usage(
            customer_id="customerId",
            currency_id="currencyId",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            resource_id="resourceId",
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            time_range="LAST_DAY",
        )
        assert_matches_type(CreditGetUsageResponse, credit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_usage(self, client: Stigg) -> None:
        response = client.v1.events.credits.with_raw_response.get_usage(
            customer_id="customerId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit = response.parse()
        assert_matches_type(CreditGetUsageResponse, credit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_usage(self, client: Stigg) -> None:
        with client.v1.events.credits.with_streaming_response.get_usage(
            customer_id="customerId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit = response.parse()
            assert_matches_type(CreditGetUsageResponse, credit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_ledger(self, client: Stigg) -> None:
        credit = client.v1.events.credits.list_ledger(
            customer_id="customerId",
        )
        assert_matches_type(SyncMyCursorIDPage[CreditListLedgerResponse], credit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_ledger_with_all_params(self, client: Stigg) -> None:
        credit = client.v1.events.credits.list_ledger(
            customer_id="customerId",
            after="after",
            before="before",
            currency_id="currencyId",
            limit=1,
            resource_id="resourceId",
        )
        assert_matches_type(SyncMyCursorIDPage[CreditListLedgerResponse], credit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_ledger(self, client: Stigg) -> None:
        response = client.v1.events.credits.with_raw_response.list_ledger(
            customer_id="customerId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit = response.parse()
        assert_matches_type(SyncMyCursorIDPage[CreditListLedgerResponse], credit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_ledger(self, client: Stigg) -> None:
        with client.v1.events.credits.with_streaming_response.list_ledger(
            customer_id="customerId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit = response.parse()
            assert_matches_type(SyncMyCursorIDPage[CreditListLedgerResponse], credit, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCredits:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_auto_recharge(self, async_client: AsyncStigg) -> None:
        credit = await async_client.v1.events.credits.get_auto_recharge(
            currency_id="currencyId",
            customer_id="customerId",
        )
        assert_matches_type(CreditGetAutoRechargeResponse, credit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_auto_recharge(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.events.credits.with_raw_response.get_auto_recharge(
            currency_id="currencyId",
            customer_id="customerId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit = await response.parse()
        assert_matches_type(CreditGetAutoRechargeResponse, credit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_auto_recharge(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.events.credits.with_streaming_response.get_auto_recharge(
            currency_id="currencyId",
            customer_id="customerId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit = await response.parse()
            assert_matches_type(CreditGetAutoRechargeResponse, credit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_usage(self, async_client: AsyncStigg) -> None:
        credit = await async_client.v1.events.credits.get_usage(
            customer_id="customerId",
        )
        assert_matches_type(CreditGetUsageResponse, credit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_usage_with_all_params(self, async_client: AsyncStigg) -> None:
        credit = await async_client.v1.events.credits.get_usage(
            customer_id="customerId",
            currency_id="currencyId",
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            resource_id="resourceId",
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            time_range="LAST_DAY",
        )
        assert_matches_type(CreditGetUsageResponse, credit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_usage(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.events.credits.with_raw_response.get_usage(
            customer_id="customerId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit = await response.parse()
        assert_matches_type(CreditGetUsageResponse, credit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_usage(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.events.credits.with_streaming_response.get_usage(
            customer_id="customerId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit = await response.parse()
            assert_matches_type(CreditGetUsageResponse, credit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_ledger(self, async_client: AsyncStigg) -> None:
        credit = await async_client.v1.events.credits.list_ledger(
            customer_id="customerId",
        )
        assert_matches_type(AsyncMyCursorIDPage[CreditListLedgerResponse], credit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_ledger_with_all_params(self, async_client: AsyncStigg) -> None:
        credit = await async_client.v1.events.credits.list_ledger(
            customer_id="customerId",
            after="after",
            before="before",
            currency_id="currencyId",
            limit=1,
            resource_id="resourceId",
        )
        assert_matches_type(AsyncMyCursorIDPage[CreditListLedgerResponse], credit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_ledger(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.events.credits.with_raw_response.list_ledger(
            customer_id="customerId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit = await response.parse()
        assert_matches_type(AsyncMyCursorIDPage[CreditListLedgerResponse], credit, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_ledger(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.events.credits.with_streaming_response.list_ledger(
            customer_id="customerId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit = await response.parse()
            assert_matches_type(AsyncMyCursorIDPage[CreditListLedgerResponse], credit, path=["response"])

        assert cast(Any, response.is_closed) is True
