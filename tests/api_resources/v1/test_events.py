# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from stigg import Stigg, AsyncStigg
from tests.utils import assert_matches_type
from stigg.types.v1 import EventReportResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEvents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_report(self, client: Stigg) -> None:
        event = client.v1.events.report(
            events=[
                {
                    "customer_id": "customerId",
                    "event_name": "x",
                    "idempotency_key": "x",
                }
            ],
        )
        assert_matches_type(EventReportResponse, event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_report(self, client: Stigg) -> None:
        response = client.v1.events.with_raw_response.report(
            events=[
                {
                    "customer_id": "customerId",
                    "event_name": "x",
                    "idempotency_key": "x",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = response.parse()
        assert_matches_type(EventReportResponse, event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_report(self, client: Stigg) -> None:
        with client.v1.events.with_streaming_response.report(
            events=[
                {
                    "customer_id": "customerId",
                    "event_name": "x",
                    "idempotency_key": "x",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = response.parse()
            assert_matches_type(EventReportResponse, event, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEvents:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_report(self, async_client: AsyncStigg) -> None:
        event = await async_client.v1.events.report(
            events=[
                {
                    "customer_id": "customerId",
                    "event_name": "x",
                    "idempotency_key": "x",
                }
            ],
        )
        assert_matches_type(EventReportResponse, event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_report(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.events.with_raw_response.report(
            events=[
                {
                    "customer_id": "customerId",
                    "event_name": "x",
                    "idempotency_key": "x",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = await response.parse()
        assert_matches_type(EventReportResponse, event, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_report(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.events.with_streaming_response.report(
            events=[
                {
                    "customer_id": "customerId",
                    "event_name": "x",
                    "idempotency_key": "x",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = await response.parse()
            assert_matches_type(EventReportResponse, event, path=["response"])

        assert cast(Any, response.is_closed) is True
