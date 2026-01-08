# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from stigg import Stigg, AsyncStigg
from tests.utils import assert_matches_type
from stigg.types.v1.subscriptions import FutureUpdateCancelScheduleResponse, FutureUpdateCancelPendingPaymentResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFutureUpdate:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_cancel_pending_payment(self, client: Stigg) -> None:
        future_update = client.v1.subscriptions.future_update.cancel_pending_payment(
            "x",
        )
        assert_matches_type(FutureUpdateCancelPendingPaymentResponse, future_update, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_cancel_pending_payment(self, client: Stigg) -> None:
        response = client.v1.subscriptions.future_update.with_raw_response.cancel_pending_payment(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        future_update = response.parse()
        assert_matches_type(FutureUpdateCancelPendingPaymentResponse, future_update, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_cancel_pending_payment(self, client: Stigg) -> None:
        with client.v1.subscriptions.future_update.with_streaming_response.cancel_pending_payment(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            future_update = response.parse()
            assert_matches_type(FutureUpdateCancelPendingPaymentResponse, future_update, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_cancel_pending_payment(self, client: Stigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v1.subscriptions.future_update.with_raw_response.cancel_pending_payment(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_cancel_schedule(self, client: Stigg) -> None:
        future_update = client.v1.subscriptions.future_update.cancel_schedule(
            "x",
        )
        assert_matches_type(FutureUpdateCancelScheduleResponse, future_update, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_cancel_schedule(self, client: Stigg) -> None:
        response = client.v1.subscriptions.future_update.with_raw_response.cancel_schedule(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        future_update = response.parse()
        assert_matches_type(FutureUpdateCancelScheduleResponse, future_update, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_cancel_schedule(self, client: Stigg) -> None:
        with client.v1.subscriptions.future_update.with_streaming_response.cancel_schedule(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            future_update = response.parse()
            assert_matches_type(FutureUpdateCancelScheduleResponse, future_update, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_cancel_schedule(self, client: Stigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v1.subscriptions.future_update.with_raw_response.cancel_schedule(
                "",
            )


class TestAsyncFutureUpdate:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_cancel_pending_payment(self, async_client: AsyncStigg) -> None:
        future_update = await async_client.v1.subscriptions.future_update.cancel_pending_payment(
            "x",
        )
        assert_matches_type(FutureUpdateCancelPendingPaymentResponse, future_update, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_cancel_pending_payment(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.subscriptions.future_update.with_raw_response.cancel_pending_payment(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        future_update = await response.parse()
        assert_matches_type(FutureUpdateCancelPendingPaymentResponse, future_update, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_cancel_pending_payment(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.subscriptions.future_update.with_streaming_response.cancel_pending_payment(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            future_update = await response.parse()
            assert_matches_type(FutureUpdateCancelPendingPaymentResponse, future_update, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_cancel_pending_payment(self, async_client: AsyncStigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v1.subscriptions.future_update.with_raw_response.cancel_pending_payment(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_cancel_schedule(self, async_client: AsyncStigg) -> None:
        future_update = await async_client.v1.subscriptions.future_update.cancel_schedule(
            "x",
        )
        assert_matches_type(FutureUpdateCancelScheduleResponse, future_update, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_cancel_schedule(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.subscriptions.future_update.with_raw_response.cancel_schedule(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        future_update = await response.parse()
        assert_matches_type(FutureUpdateCancelScheduleResponse, future_update, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_cancel_schedule(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.subscriptions.future_update.with_streaming_response.cancel_schedule(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            future_update = await response.parse()
            assert_matches_type(FutureUpdateCancelScheduleResponse, future_update, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_cancel_schedule(self, async_client: AsyncStigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v1.subscriptions.future_update.with_raw_response.cancel_schedule(
                "",
            )
