# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from stigg import Stigg, AsyncStigg
from tests.utils import assert_matches_type
from stigg._utils import parse_datetime
from stigg.types.v1.credits import (
    ConsumptionConsumeResponse,
    ConsumptionConsumeAsyncResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConsumption:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_consume(self, client: Stigg) -> None:
        consumption = client.v1.credits.consumption.consume(
            amount=1,
            currency_id="currencyId",
            customer_id="customerId",
            idempotency_key="x",
        )
        assert_matches_type(ConsumptionConsumeResponse, consumption, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_consume_with_all_params(self, client: Stigg) -> None:
        consumption = client.v1.credits.consumption.consume(
            amount=1,
            currency_id="currencyId",
            customer_id="customerId",
            idempotency_key="x",
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            dimensions={"foo": "string"},
            resource_id="resourceId",
            x_account_id="X-ACCOUNT-ID",
            x_environment_id="X-ENVIRONMENT-ID",
        )
        assert_matches_type(ConsumptionConsumeResponse, consumption, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_consume(self, client: Stigg) -> None:
        response = client.v1.credits.consumption.with_raw_response.consume(
            amount=1,
            currency_id="currencyId",
            customer_id="customerId",
            idempotency_key="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        consumption = response.parse()
        assert_matches_type(ConsumptionConsumeResponse, consumption, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_consume(self, client: Stigg) -> None:
        with client.v1.credits.consumption.with_streaming_response.consume(
            amount=1,
            currency_id="currencyId",
            customer_id="customerId",
            idempotency_key="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            consumption = response.parse()
            assert_matches_type(ConsumptionConsumeResponse, consumption, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_consume_async(self, client: Stigg) -> None:
        consumption = client.v1.credits.consumption.consume_async(
            consumptions=[
                {
                    "amount": 1,
                    "currency_id": "currencyId",
                    "customer_id": "customerId",
                    "idempotency_key": "x",
                }
            ],
        )
        assert_matches_type(ConsumptionConsumeAsyncResponse, consumption, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_consume_async_with_all_params(self, client: Stigg) -> None:
        consumption = client.v1.credits.consumption.consume_async(
            consumptions=[
                {
                    "amount": 1,
                    "currency_id": "currencyId",
                    "customer_id": "customerId",
                    "idempotency_key": "x",
                    "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "dimensions": {"foo": "string"},
                    "resource_id": "resourceId",
                }
            ],
            x_account_id="X-ACCOUNT-ID",
            x_environment_id="X-ENVIRONMENT-ID",
        )
        assert_matches_type(ConsumptionConsumeAsyncResponse, consumption, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_consume_async(self, client: Stigg) -> None:
        response = client.v1.credits.consumption.with_raw_response.consume_async(
            consumptions=[
                {
                    "amount": 1,
                    "currency_id": "currencyId",
                    "customer_id": "customerId",
                    "idempotency_key": "x",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        consumption = response.parse()
        assert_matches_type(ConsumptionConsumeAsyncResponse, consumption, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_consume_async(self, client: Stigg) -> None:
        with client.v1.credits.consumption.with_streaming_response.consume_async(
            consumptions=[
                {
                    "amount": 1,
                    "currency_id": "currencyId",
                    "customer_id": "customerId",
                    "idempotency_key": "x",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            consumption = response.parse()
            assert_matches_type(ConsumptionConsumeAsyncResponse, consumption, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncConsumption:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_consume(self, async_client: AsyncStigg) -> None:
        consumption = await async_client.v1.credits.consumption.consume(
            amount=1,
            currency_id="currencyId",
            customer_id="customerId",
            idempotency_key="x",
        )
        assert_matches_type(ConsumptionConsumeResponse, consumption, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_consume_with_all_params(self, async_client: AsyncStigg) -> None:
        consumption = await async_client.v1.credits.consumption.consume(
            amount=1,
            currency_id="currencyId",
            customer_id="customerId",
            idempotency_key="x",
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            dimensions={"foo": "string"},
            resource_id="resourceId",
            x_account_id="X-ACCOUNT-ID",
            x_environment_id="X-ENVIRONMENT-ID",
        )
        assert_matches_type(ConsumptionConsumeResponse, consumption, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_consume(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.credits.consumption.with_raw_response.consume(
            amount=1,
            currency_id="currencyId",
            customer_id="customerId",
            idempotency_key="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        consumption = await response.parse()
        assert_matches_type(ConsumptionConsumeResponse, consumption, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_consume(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.credits.consumption.with_streaming_response.consume(
            amount=1,
            currency_id="currencyId",
            customer_id="customerId",
            idempotency_key="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            consumption = await response.parse()
            assert_matches_type(ConsumptionConsumeResponse, consumption, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_consume_async(self, async_client: AsyncStigg) -> None:
        consumption = await async_client.v1.credits.consumption.consume_async(
            consumptions=[
                {
                    "amount": 1,
                    "currency_id": "currencyId",
                    "customer_id": "customerId",
                    "idempotency_key": "x",
                }
            ],
        )
        assert_matches_type(ConsumptionConsumeAsyncResponse, consumption, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_consume_async_with_all_params(self, async_client: AsyncStigg) -> None:
        consumption = await async_client.v1.credits.consumption.consume_async(
            consumptions=[
                {
                    "amount": 1,
                    "currency_id": "currencyId",
                    "customer_id": "customerId",
                    "idempotency_key": "x",
                    "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                    "dimensions": {"foo": "string"},
                    "resource_id": "resourceId",
                }
            ],
            x_account_id="X-ACCOUNT-ID",
            x_environment_id="X-ENVIRONMENT-ID",
        )
        assert_matches_type(ConsumptionConsumeAsyncResponse, consumption, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_consume_async(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.credits.consumption.with_raw_response.consume_async(
            consumptions=[
                {
                    "amount": 1,
                    "currency_id": "currencyId",
                    "customer_id": "customerId",
                    "idempotency_key": "x",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        consumption = await response.parse()
        assert_matches_type(ConsumptionConsumeAsyncResponse, consumption, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_consume_async(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.credits.consumption.with_streaming_response.consume_async(
            consumptions=[
                {
                    "amount": 1,
                    "currency_id": "currencyId",
                    "customer_id": "customerId",
                    "idempotency_key": "x",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            consumption = await response.parse()
            assert_matches_type(ConsumptionConsumeAsyncResponse, consumption, path=["response"])

        assert cast(Any, response.is_closed) is True
