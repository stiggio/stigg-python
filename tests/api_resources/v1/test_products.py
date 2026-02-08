# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from stigg import Stigg, AsyncStigg
from tests.utils import assert_matches_type
from stigg.types.v1 import ProductListProductsResponse
from stigg.pagination import SyncMyCursorIDPage, AsyncMyCursorIDPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProducts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_products(self, client: Stigg) -> None:
        product = client.v1.products.list_products()
        assert_matches_type(SyncMyCursorIDPage[ProductListProductsResponse], product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_products_with_all_params(self, client: Stigg) -> None:
        product = client.v1.products.list_products(
            after="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            before="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=1,
        )
        assert_matches_type(SyncMyCursorIDPage[ProductListProductsResponse], product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_products(self, client: Stigg) -> None:
        response = client.v1.products.with_raw_response.list_products()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = response.parse()
        assert_matches_type(SyncMyCursorIDPage[ProductListProductsResponse], product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_products(self, client: Stigg) -> None:
        with client.v1.products.with_streaming_response.list_products() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = response.parse()
            assert_matches_type(SyncMyCursorIDPage[ProductListProductsResponse], product, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncProducts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_products(self, async_client: AsyncStigg) -> None:
        product = await async_client.v1.products.list_products()
        assert_matches_type(AsyncMyCursorIDPage[ProductListProductsResponse], product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_products_with_all_params(self, async_client: AsyncStigg) -> None:
        product = await async_client.v1.products.list_products(
            after="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            before="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=1,
        )
        assert_matches_type(AsyncMyCursorIDPage[ProductListProductsResponse], product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_products(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.products.with_raw_response.list_products()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = await response.parse()
        assert_matches_type(AsyncMyCursorIDPage[ProductListProductsResponse], product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_products(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.products.with_streaming_response.list_products() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = await response.parse()
            assert_matches_type(AsyncMyCursorIDPage[ProductListProductsResponse], product, path=["response"])

        assert cast(Any, response.is_closed) is True
