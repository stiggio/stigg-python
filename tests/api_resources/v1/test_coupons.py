# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from stigg import Stigg, AsyncStigg
from tests.utils import assert_matches_type
from stigg._utils import parse_datetime
from stigg.types.v1 import (
    Coupon,
    CouponListResponse,
)
from stigg.pagination import SyncMyCursorIDPage, AsyncMyCursorIDPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCoupons:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Stigg) -> None:
        coupon = client.v1.coupons.create(
            id="id",
            amounts_off=[
                {
                    "amount": 0,
                    "currency": "usd",
                }
            ],
            description="description",
            duration_in_months=1,
            metadata={"foo": "string"},
            name="name",
            percent_off=1,
        )
        assert_matches_type(Coupon, coupon, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Stigg) -> None:
        response = client.v1.coupons.with_raw_response.create(
            id="id",
            amounts_off=[
                {
                    "amount": 0,
                    "currency": "usd",
                }
            ],
            description="description",
            duration_in_months=1,
            metadata={"foo": "string"},
            name="name",
            percent_off=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        coupon = response.parse()
        assert_matches_type(Coupon, coupon, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Stigg) -> None:
        with client.v1.coupons.with_streaming_response.create(
            id="id",
            amounts_off=[
                {
                    "amount": 0,
                    "currency": "usd",
                }
            ],
            description="description",
            duration_in_months=1,
            metadata={"foo": "string"},
            name="name",
            percent_off=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            coupon = response.parse()
            assert_matches_type(Coupon, coupon, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Stigg) -> None:
        coupon = client.v1.coupons.retrieve(
            "x",
        )
        assert_matches_type(Coupon, coupon, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Stigg) -> None:
        response = client.v1.coupons.with_raw_response.retrieve(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        coupon = response.parse()
        assert_matches_type(Coupon, coupon, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Stigg) -> None:
        with client.v1.coupons.with_streaming_response.retrieve(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            coupon = response.parse()
            assert_matches_type(Coupon, coupon, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Stigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v1.coupons.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Stigg) -> None:
        coupon = client.v1.coupons.list()
        assert_matches_type(SyncMyCursorIDPage[CouponListResponse], coupon, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Stigg) -> None:
        coupon = client.v1.coupons.list(
            id="id",
            after="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            before="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            created_at={
                "gt": parse_datetime("2019-12-27T18:11:19.117Z"),
                "gte": parse_datetime("2019-12-27T18:11:19.117Z"),
                "lt": parse_datetime("2019-12-27T18:11:19.117Z"),
                "lte": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            limit=1,
            status="status",
            type="FIXED",
        )
        assert_matches_type(SyncMyCursorIDPage[CouponListResponse], coupon, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Stigg) -> None:
        response = client.v1.coupons.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        coupon = response.parse()
        assert_matches_type(SyncMyCursorIDPage[CouponListResponse], coupon, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Stigg) -> None:
        with client.v1.coupons.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            coupon = response.parse()
            assert_matches_type(SyncMyCursorIDPage[CouponListResponse], coupon, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_archive_coupon(self, client: Stigg) -> None:
        coupon = client.v1.coupons.archive_coupon(
            "x",
        )
        assert_matches_type(Coupon, coupon, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_archive_coupon(self, client: Stigg) -> None:
        response = client.v1.coupons.with_raw_response.archive_coupon(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        coupon = response.parse()
        assert_matches_type(Coupon, coupon, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_archive_coupon(self, client: Stigg) -> None:
        with client.v1.coupons.with_streaming_response.archive_coupon(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            coupon = response.parse()
            assert_matches_type(Coupon, coupon, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_archive_coupon(self, client: Stigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v1.coupons.with_raw_response.archive_coupon(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_coupon(self, client: Stigg) -> None:
        coupon = client.v1.coupons.update_coupon(
            id="x",
        )
        assert_matches_type(Coupon, coupon, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_coupon_with_all_params(self, client: Stigg) -> None:
        coupon = client.v1.coupons.update_coupon(
            id="x",
            description="description",
            metadata={"foo": "string"},
            name="name",
        )
        assert_matches_type(Coupon, coupon, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_coupon(self, client: Stigg) -> None:
        response = client.v1.coupons.with_raw_response.update_coupon(
            id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        coupon = response.parse()
        assert_matches_type(Coupon, coupon, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_coupon(self, client: Stigg) -> None:
        with client.v1.coupons.with_streaming_response.update_coupon(
            id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            coupon = response.parse()
            assert_matches_type(Coupon, coupon, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_coupon(self, client: Stigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v1.coupons.with_raw_response.update_coupon(
                id="",
            )


class TestAsyncCoupons:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncStigg) -> None:
        coupon = await async_client.v1.coupons.create(
            id="id",
            amounts_off=[
                {
                    "amount": 0,
                    "currency": "usd",
                }
            ],
            description="description",
            duration_in_months=1,
            metadata={"foo": "string"},
            name="name",
            percent_off=1,
        )
        assert_matches_type(Coupon, coupon, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.coupons.with_raw_response.create(
            id="id",
            amounts_off=[
                {
                    "amount": 0,
                    "currency": "usd",
                }
            ],
            description="description",
            duration_in_months=1,
            metadata={"foo": "string"},
            name="name",
            percent_off=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        coupon = await response.parse()
        assert_matches_type(Coupon, coupon, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.coupons.with_streaming_response.create(
            id="id",
            amounts_off=[
                {
                    "amount": 0,
                    "currency": "usd",
                }
            ],
            description="description",
            duration_in_months=1,
            metadata={"foo": "string"},
            name="name",
            percent_off=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            coupon = await response.parse()
            assert_matches_type(Coupon, coupon, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncStigg) -> None:
        coupon = await async_client.v1.coupons.retrieve(
            "x",
        )
        assert_matches_type(Coupon, coupon, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.coupons.with_raw_response.retrieve(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        coupon = await response.parse()
        assert_matches_type(Coupon, coupon, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.coupons.with_streaming_response.retrieve(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            coupon = await response.parse()
            assert_matches_type(Coupon, coupon, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncStigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v1.coupons.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncStigg) -> None:
        coupon = await async_client.v1.coupons.list()
        assert_matches_type(AsyncMyCursorIDPage[CouponListResponse], coupon, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncStigg) -> None:
        coupon = await async_client.v1.coupons.list(
            id="id",
            after="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            before="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            created_at={
                "gt": parse_datetime("2019-12-27T18:11:19.117Z"),
                "gte": parse_datetime("2019-12-27T18:11:19.117Z"),
                "lt": parse_datetime("2019-12-27T18:11:19.117Z"),
                "lte": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            limit=1,
            status="status",
            type="FIXED",
        )
        assert_matches_type(AsyncMyCursorIDPage[CouponListResponse], coupon, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.coupons.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        coupon = await response.parse()
        assert_matches_type(AsyncMyCursorIDPage[CouponListResponse], coupon, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.coupons.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            coupon = await response.parse()
            assert_matches_type(AsyncMyCursorIDPage[CouponListResponse], coupon, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_archive_coupon(self, async_client: AsyncStigg) -> None:
        coupon = await async_client.v1.coupons.archive_coupon(
            "x",
        )
        assert_matches_type(Coupon, coupon, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_archive_coupon(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.coupons.with_raw_response.archive_coupon(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        coupon = await response.parse()
        assert_matches_type(Coupon, coupon, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_archive_coupon(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.coupons.with_streaming_response.archive_coupon(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            coupon = await response.parse()
            assert_matches_type(Coupon, coupon, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_archive_coupon(self, async_client: AsyncStigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v1.coupons.with_raw_response.archive_coupon(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_coupon(self, async_client: AsyncStigg) -> None:
        coupon = await async_client.v1.coupons.update_coupon(
            id="x",
        )
        assert_matches_type(Coupon, coupon, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_coupon_with_all_params(self, async_client: AsyncStigg) -> None:
        coupon = await async_client.v1.coupons.update_coupon(
            id="x",
            description="description",
            metadata={"foo": "string"},
            name="name",
        )
        assert_matches_type(Coupon, coupon, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_coupon(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.coupons.with_raw_response.update_coupon(
            id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        coupon = await response.parse()
        assert_matches_type(Coupon, coupon, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_coupon(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.coupons.with_streaming_response.update_coupon(
            id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            coupon = await response.parse()
            assert_matches_type(Coupon, coupon, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_coupon(self, async_client: AsyncStigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v1.coupons.with_raw_response.update_coupon(
                id="",
            )
