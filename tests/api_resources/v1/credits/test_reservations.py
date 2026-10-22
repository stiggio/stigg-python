# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from stigg import Stigg, AsyncStigg
from tests.utils import assert_matches_type
from stigg.types.v1.credits import ReservationReleaseResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestReservations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_release(self, client: Stigg) -> None:
        reservation = client.v1.credits.reservations.release(
            reservation_id="x",
            consumed_amount=0,
            currency_id="currencyId",
            customer_id="customerId",
        )
        assert_matches_type(ReservationReleaseResponse, reservation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_release_with_all_params(self, client: Stigg) -> None:
        reservation = client.v1.credits.reservations.release(
            reservation_id="x",
            consumed_amount=0,
            currency_id="currencyId",
            customer_id="customerId",
            resource_id="resourceId",
            x_account_id="X-ACCOUNT-ID",
            x_environment_id="X-ENVIRONMENT-ID",
        )
        assert_matches_type(ReservationReleaseResponse, reservation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_release(self, client: Stigg) -> None:
        response = client.v1.credits.reservations.with_raw_response.release(
            reservation_id="x",
            consumed_amount=0,
            currency_id="currencyId",
            customer_id="customerId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reservation = response.parse()
        assert_matches_type(ReservationReleaseResponse, reservation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_release(self, client: Stigg) -> None:
        with client.v1.credits.reservations.with_streaming_response.release(
            reservation_id="x",
            consumed_amount=0,
            currency_id="currencyId",
            customer_id="customerId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reservation = response.parse()
            assert_matches_type(ReservationReleaseResponse, reservation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_release(self, client: Stigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `reservation_id` but received ''"):
            client.v1.credits.reservations.with_raw_response.release(
                reservation_id="",
                consumed_amount=0,
                currency_id="currencyId",
                customer_id="customerId",
            )


class TestAsyncReservations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_release(self, async_client: AsyncStigg) -> None:
        reservation = await async_client.v1.credits.reservations.release(
            reservation_id="x",
            consumed_amount=0,
            currency_id="currencyId",
            customer_id="customerId",
        )
        assert_matches_type(ReservationReleaseResponse, reservation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_release_with_all_params(self, async_client: AsyncStigg) -> None:
        reservation = await async_client.v1.credits.reservations.release(
            reservation_id="x",
            consumed_amount=0,
            currency_id="currencyId",
            customer_id="customerId",
            resource_id="resourceId",
            x_account_id="X-ACCOUNT-ID",
            x_environment_id="X-ENVIRONMENT-ID",
        )
        assert_matches_type(ReservationReleaseResponse, reservation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_release(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.credits.reservations.with_raw_response.release(
            reservation_id="x",
            consumed_amount=0,
            currency_id="currencyId",
            customer_id="customerId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reservation = await response.parse()
        assert_matches_type(ReservationReleaseResponse, reservation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_release(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.credits.reservations.with_streaming_response.release(
            reservation_id="x",
            consumed_amount=0,
            currency_id="currencyId",
            customer_id="customerId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reservation = await response.parse()
            assert_matches_type(ReservationReleaseResponse, reservation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_release(self, async_client: AsyncStigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `reservation_id` but received ''"):
            await async_client.v1.credits.reservations.with_raw_response.release(
                reservation_id="",
                consumed_amount=0,
                currency_id="currencyId",
                customer_id="customerId",
            )
