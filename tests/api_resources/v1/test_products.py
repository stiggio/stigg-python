# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from stigg import Stigg, AsyncStigg
from tests.utils import assert_matches_type
from stigg._utils import parse_datetime
from stigg.types.v1 import (
    ProductListProductsResponse,
    ProductCreateProductResponse,
    ProductUpdateProductResponse,
    ProductArchiveProductResponse,
    ProductDuplicateProductResponse,
    ProductUnarchiveProductResponse,
)
from stigg.pagination import SyncMyCursorIDPage, AsyncMyCursorIDPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProducts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_archive_product(self, client: Stigg) -> None:
        product = client.v1.products.archive_product(
            "x",
        )
        assert_matches_type(ProductArchiveProductResponse, product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_archive_product(self, client: Stigg) -> None:
        response = client.v1.products.with_raw_response.archive_product(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = response.parse()
        assert_matches_type(ProductArchiveProductResponse, product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_archive_product(self, client: Stigg) -> None:
        with client.v1.products.with_streaming_response.archive_product(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = response.parse()
            assert_matches_type(ProductArchiveProductResponse, product, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_archive_product(self, client: Stigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v1.products.with_raw_response.archive_product(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_product(self, client: Stigg) -> None:
        product = client.v1.products.create_product(
            id="id",
        )
        assert_matches_type(ProductCreateProductResponse, product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_product_with_all_params(self, client: Stigg) -> None:
        product = client.v1.products.create_product(
            id="id",
            description="description",
            display_name="displayName",
            metadata={"foo": "string"},
            multiple_subscriptions=True,
        )
        assert_matches_type(ProductCreateProductResponse, product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_product(self, client: Stigg) -> None:
        response = client.v1.products.with_raw_response.create_product(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = response.parse()
        assert_matches_type(ProductCreateProductResponse, product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_product(self, client: Stigg) -> None:
        with client.v1.products.with_streaming_response.create_product(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = response.parse()
            assert_matches_type(ProductCreateProductResponse, product, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_duplicate_product(self, client: Stigg) -> None:
        product = client.v1.products.duplicate_product(
            id="x",
        )
        assert_matches_type(ProductDuplicateProductResponse, product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_duplicate_product_with_all_params(self, client: Stigg) -> None:
        product = client.v1.products.duplicate_product(
            id="x",
            description="description",
            display_name="displayName",
        )
        assert_matches_type(ProductDuplicateProductResponse, product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_duplicate_product(self, client: Stigg) -> None:
        response = client.v1.products.with_raw_response.duplicate_product(
            id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = response.parse()
        assert_matches_type(ProductDuplicateProductResponse, product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_duplicate_product(self, client: Stigg) -> None:
        with client.v1.products.with_streaming_response.duplicate_product(
            id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = response.parse()
            assert_matches_type(ProductDuplicateProductResponse, product, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_duplicate_product(self, client: Stigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v1.products.with_raw_response.duplicate_product(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_products(self, client: Stigg) -> None:
        product = client.v1.products.list_products()
        assert_matches_type(SyncMyCursorIDPage[ProductListProductsResponse], product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_products_with_all_params(self, client: Stigg) -> None:
        product = client.v1.products.list_products(
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

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_unarchive_product(self, client: Stigg) -> None:
        product = client.v1.products.unarchive_product(
            "x",
        )
        assert_matches_type(ProductUnarchiveProductResponse, product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_unarchive_product(self, client: Stigg) -> None:
        response = client.v1.products.with_raw_response.unarchive_product(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = response.parse()
        assert_matches_type(ProductUnarchiveProductResponse, product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_unarchive_product(self, client: Stigg) -> None:
        with client.v1.products.with_streaming_response.unarchive_product(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = response.parse()
            assert_matches_type(ProductUnarchiveProductResponse, product, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_unarchive_product(self, client: Stigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v1.products.with_raw_response.unarchive_product(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_product(self, client: Stigg) -> None:
        product = client.v1.products.update_product(
            id="x",
        )
        assert_matches_type(ProductUpdateProductResponse, product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_product_with_all_params(self, client: Stigg) -> None:
        product = client.v1.products.update_product(
            id="x",
            description="description",
            display_name="displayName",
            metadata={"foo": "string"},
            multiple_subscriptions=True,
            product_settings={
                "subscription_cancellation_time": "END_OF_BILLING_PERIOD",
                "subscription_end_setup": "DOWNGRADE_TO_FREE",
                "subscription_start_setup": "PLAN_SELECTION",
                "downgrade_plan_id": "downgradePlanId",
                "prorate_at_end_of_billing_period": True,
                "subscription_start_plan_id": "subscriptionStartPlanId",
            },
            usage_reset_cutoff_rule={"behavior": "NEVER_RESET"},
        )
        assert_matches_type(ProductUpdateProductResponse, product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_product(self, client: Stigg) -> None:
        response = client.v1.products.with_raw_response.update_product(
            id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = response.parse()
        assert_matches_type(ProductUpdateProductResponse, product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_product(self, client: Stigg) -> None:
        with client.v1.products.with_streaming_response.update_product(
            id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = response.parse()
            assert_matches_type(ProductUpdateProductResponse, product, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_product(self, client: Stigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v1.products.with_raw_response.update_product(
                id="",
            )


class TestAsyncProducts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_archive_product(self, async_client: AsyncStigg) -> None:
        product = await async_client.v1.products.archive_product(
            "x",
        )
        assert_matches_type(ProductArchiveProductResponse, product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_archive_product(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.products.with_raw_response.archive_product(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = await response.parse()
        assert_matches_type(ProductArchiveProductResponse, product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_archive_product(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.products.with_streaming_response.archive_product(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = await response.parse()
            assert_matches_type(ProductArchiveProductResponse, product, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_archive_product(self, async_client: AsyncStigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v1.products.with_raw_response.archive_product(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_product(self, async_client: AsyncStigg) -> None:
        product = await async_client.v1.products.create_product(
            id="id",
        )
        assert_matches_type(ProductCreateProductResponse, product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_product_with_all_params(self, async_client: AsyncStigg) -> None:
        product = await async_client.v1.products.create_product(
            id="id",
            description="description",
            display_name="displayName",
            metadata={"foo": "string"},
            multiple_subscriptions=True,
        )
        assert_matches_type(ProductCreateProductResponse, product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_product(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.products.with_raw_response.create_product(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = await response.parse()
        assert_matches_type(ProductCreateProductResponse, product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_product(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.products.with_streaming_response.create_product(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = await response.parse()
            assert_matches_type(ProductCreateProductResponse, product, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_duplicate_product(self, async_client: AsyncStigg) -> None:
        product = await async_client.v1.products.duplicate_product(
            id="x",
        )
        assert_matches_type(ProductDuplicateProductResponse, product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_duplicate_product_with_all_params(self, async_client: AsyncStigg) -> None:
        product = await async_client.v1.products.duplicate_product(
            id="x",
            description="description",
            display_name="displayName",
        )
        assert_matches_type(ProductDuplicateProductResponse, product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_duplicate_product(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.products.with_raw_response.duplicate_product(
            id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = await response.parse()
        assert_matches_type(ProductDuplicateProductResponse, product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_duplicate_product(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.products.with_streaming_response.duplicate_product(
            id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = await response.parse()
            assert_matches_type(ProductDuplicateProductResponse, product, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_duplicate_product(self, async_client: AsyncStigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v1.products.with_raw_response.duplicate_product(
                id="",
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

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_unarchive_product(self, async_client: AsyncStigg) -> None:
        product = await async_client.v1.products.unarchive_product(
            "x",
        )
        assert_matches_type(ProductUnarchiveProductResponse, product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_unarchive_product(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.products.with_raw_response.unarchive_product(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = await response.parse()
        assert_matches_type(ProductUnarchiveProductResponse, product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_unarchive_product(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.products.with_streaming_response.unarchive_product(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = await response.parse()
            assert_matches_type(ProductUnarchiveProductResponse, product, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_unarchive_product(self, async_client: AsyncStigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v1.products.with_raw_response.unarchive_product(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_product(self, async_client: AsyncStigg) -> None:
        product = await async_client.v1.products.update_product(
            id="x",
        )
        assert_matches_type(ProductUpdateProductResponse, product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_product_with_all_params(self, async_client: AsyncStigg) -> None:
        product = await async_client.v1.products.update_product(
            id="x",
            description="description",
            display_name="displayName",
            metadata={"foo": "string"},
            multiple_subscriptions=True,
            product_settings={
                "subscription_cancellation_time": "END_OF_BILLING_PERIOD",
                "subscription_end_setup": "DOWNGRADE_TO_FREE",
                "subscription_start_setup": "PLAN_SELECTION",
                "downgrade_plan_id": "downgradePlanId",
                "prorate_at_end_of_billing_period": True,
                "subscription_start_plan_id": "subscriptionStartPlanId",
            },
            usage_reset_cutoff_rule={"behavior": "NEVER_RESET"},
        )
        assert_matches_type(ProductUpdateProductResponse, product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_product(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.products.with_raw_response.update_product(
            id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = await response.parse()
        assert_matches_type(ProductUpdateProductResponse, product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_product(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.products.with_streaming_response.update_product(
            id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = await response.parse()
            assert_matches_type(ProductUpdateProductResponse, product, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_product(self, async_client: AsyncStigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v1.products.with_raw_response.update_product(
                id="",
            )
