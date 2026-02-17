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
    AddonListAddonsResponse,
    AddonCreateAddonResponse,
    AddonUpdateAddonResponse,
    AddonArchiveAddonResponse,
    AddonPublishAddonResponse,
    AddonRetrieveAddonResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAddons:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_archive_addon(self, client: Stigg) -> None:
        addon = client.v1.events.addons.archive_addon(
            "x",
        )
        assert_matches_type(AddonArchiveAddonResponse, addon, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_archive_addon(self, client: Stigg) -> None:
        response = client.v1.events.addons.with_raw_response.archive_addon(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        addon = response.parse()
        assert_matches_type(AddonArchiveAddonResponse, addon, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_archive_addon(self, client: Stigg) -> None:
        with client.v1.events.addons.with_streaming_response.archive_addon(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            addon = response.parse()
            assert_matches_type(AddonArchiveAddonResponse, addon, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_archive_addon(self, client: Stigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v1.events.addons.with_raw_response.archive_addon(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_addon(self, client: Stigg) -> None:
        addon = client.v1.events.addons.create_addon(
            id="id",
            display_name="displayName",
            product_id="productId",
        )
        assert_matches_type(AddonCreateAddonResponse, addon, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_addon_with_all_params(self, client: Stigg) -> None:
        addon = client.v1.events.addons.create_addon(
            id="id",
            display_name="displayName",
            product_id="productId",
            billing_id="billingId",
            description="description",
            max_quantity=1,
            metadata={"foo": "string"},
            pricing_type="FREE",
            status="DRAFT",
        )
        assert_matches_type(AddonCreateAddonResponse, addon, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_addon(self, client: Stigg) -> None:
        response = client.v1.events.addons.with_raw_response.create_addon(
            id="id",
            display_name="displayName",
            product_id="productId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        addon = response.parse()
        assert_matches_type(AddonCreateAddonResponse, addon, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_addon(self, client: Stigg) -> None:
        with client.v1.events.addons.with_streaming_response.create_addon(
            id="id",
            display_name="displayName",
            product_id="productId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            addon = response.parse()
            assert_matches_type(AddonCreateAddonResponse, addon, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_addons(self, client: Stigg) -> None:
        addon = client.v1.events.addons.list_addons()
        assert_matches_type(SyncMyCursorIDPage[AddonListAddonsResponse], addon, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_addons_with_all_params(self, client: Stigg) -> None:
        addon = client.v1.events.addons.list_addons(
            after="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            before="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            created_at={
                "gt": parse_datetime("2019-12-27T18:11:19.117Z"),
                "gte": parse_datetime("2019-12-27T18:11:19.117Z"),
                "lt": parse_datetime("2019-12-27T18:11:19.117Z"),
                "lte": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            limit=1,
            product_id="productId",
            status="DRAFT",
        )
        assert_matches_type(SyncMyCursorIDPage[AddonListAddonsResponse], addon, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_addons(self, client: Stigg) -> None:
        response = client.v1.events.addons.with_raw_response.list_addons()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        addon = response.parse()
        assert_matches_type(SyncMyCursorIDPage[AddonListAddonsResponse], addon, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_addons(self, client: Stigg) -> None:
        with client.v1.events.addons.with_streaming_response.list_addons() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            addon = response.parse()
            assert_matches_type(SyncMyCursorIDPage[AddonListAddonsResponse], addon, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_publish_addon(self, client: Stigg) -> None:
        addon = client.v1.events.addons.publish_addon(
            id="x",
            migration_type="NEW_CUSTOMERS",
        )
        assert_matches_type(AddonPublishAddonResponse, addon, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_publish_addon(self, client: Stigg) -> None:
        response = client.v1.events.addons.with_raw_response.publish_addon(
            id="x",
            migration_type="NEW_CUSTOMERS",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        addon = response.parse()
        assert_matches_type(AddonPublishAddonResponse, addon, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_publish_addon(self, client: Stigg) -> None:
        with client.v1.events.addons.with_streaming_response.publish_addon(
            id="x",
            migration_type="NEW_CUSTOMERS",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            addon = response.parse()
            assert_matches_type(AddonPublishAddonResponse, addon, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_publish_addon(self, client: Stigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v1.events.addons.with_raw_response.publish_addon(
                id="",
                migration_type="NEW_CUSTOMERS",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_addon(self, client: Stigg) -> None:
        addon = client.v1.events.addons.retrieve_addon(
            "x",
        )
        assert_matches_type(AddonRetrieveAddonResponse, addon, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_addon(self, client: Stigg) -> None:
        response = client.v1.events.addons.with_raw_response.retrieve_addon(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        addon = response.parse()
        assert_matches_type(AddonRetrieveAddonResponse, addon, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_addon(self, client: Stigg) -> None:
        with client.v1.events.addons.with_streaming_response.retrieve_addon(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            addon = response.parse()
            assert_matches_type(AddonRetrieveAddonResponse, addon, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve_addon(self, client: Stigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v1.events.addons.with_raw_response.retrieve_addon(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_addon(self, client: Stigg) -> None:
        addon = client.v1.events.addons.update_addon(
            id="x",
        )
        assert_matches_type(AddonUpdateAddonResponse, addon, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_addon_with_all_params(self, client: Stigg) -> None:
        addon = client.v1.events.addons.update_addon(
            id="x",
            billing_id="billingId",
            dependencies=["string"],
            description="description",
            display_name="displayName",
            max_quantity=0,
            metadata={"foo": "string"},
        )
        assert_matches_type(AddonUpdateAddonResponse, addon, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_addon(self, client: Stigg) -> None:
        response = client.v1.events.addons.with_raw_response.update_addon(
            id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        addon = response.parse()
        assert_matches_type(AddonUpdateAddonResponse, addon, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_addon(self, client: Stigg) -> None:
        with client.v1.events.addons.with_streaming_response.update_addon(
            id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            addon = response.parse()
            assert_matches_type(AddonUpdateAddonResponse, addon, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_addon(self, client: Stigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v1.events.addons.with_raw_response.update_addon(
                id="",
            )


class TestAsyncAddons:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_archive_addon(self, async_client: AsyncStigg) -> None:
        addon = await async_client.v1.events.addons.archive_addon(
            "x",
        )
        assert_matches_type(AddonArchiveAddonResponse, addon, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_archive_addon(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.events.addons.with_raw_response.archive_addon(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        addon = await response.parse()
        assert_matches_type(AddonArchiveAddonResponse, addon, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_archive_addon(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.events.addons.with_streaming_response.archive_addon(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            addon = await response.parse()
            assert_matches_type(AddonArchiveAddonResponse, addon, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_archive_addon(self, async_client: AsyncStigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v1.events.addons.with_raw_response.archive_addon(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_addon(self, async_client: AsyncStigg) -> None:
        addon = await async_client.v1.events.addons.create_addon(
            id="id",
            display_name="displayName",
            product_id="productId",
        )
        assert_matches_type(AddonCreateAddonResponse, addon, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_addon_with_all_params(self, async_client: AsyncStigg) -> None:
        addon = await async_client.v1.events.addons.create_addon(
            id="id",
            display_name="displayName",
            product_id="productId",
            billing_id="billingId",
            description="description",
            max_quantity=1,
            metadata={"foo": "string"},
            pricing_type="FREE",
            status="DRAFT",
        )
        assert_matches_type(AddonCreateAddonResponse, addon, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_addon(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.events.addons.with_raw_response.create_addon(
            id="id",
            display_name="displayName",
            product_id="productId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        addon = await response.parse()
        assert_matches_type(AddonCreateAddonResponse, addon, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_addon(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.events.addons.with_streaming_response.create_addon(
            id="id",
            display_name="displayName",
            product_id="productId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            addon = await response.parse()
            assert_matches_type(AddonCreateAddonResponse, addon, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_addons(self, async_client: AsyncStigg) -> None:
        addon = await async_client.v1.events.addons.list_addons()
        assert_matches_type(AsyncMyCursorIDPage[AddonListAddonsResponse], addon, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_addons_with_all_params(self, async_client: AsyncStigg) -> None:
        addon = await async_client.v1.events.addons.list_addons(
            after="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            before="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            created_at={
                "gt": parse_datetime("2019-12-27T18:11:19.117Z"),
                "gte": parse_datetime("2019-12-27T18:11:19.117Z"),
                "lt": parse_datetime("2019-12-27T18:11:19.117Z"),
                "lte": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            limit=1,
            product_id="productId",
            status="DRAFT",
        )
        assert_matches_type(AsyncMyCursorIDPage[AddonListAddonsResponse], addon, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_addons(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.events.addons.with_raw_response.list_addons()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        addon = await response.parse()
        assert_matches_type(AsyncMyCursorIDPage[AddonListAddonsResponse], addon, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_addons(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.events.addons.with_streaming_response.list_addons() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            addon = await response.parse()
            assert_matches_type(AsyncMyCursorIDPage[AddonListAddonsResponse], addon, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_publish_addon(self, async_client: AsyncStigg) -> None:
        addon = await async_client.v1.events.addons.publish_addon(
            id="x",
            migration_type="NEW_CUSTOMERS",
        )
        assert_matches_type(AddonPublishAddonResponse, addon, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_publish_addon(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.events.addons.with_raw_response.publish_addon(
            id="x",
            migration_type="NEW_CUSTOMERS",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        addon = await response.parse()
        assert_matches_type(AddonPublishAddonResponse, addon, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_publish_addon(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.events.addons.with_streaming_response.publish_addon(
            id="x",
            migration_type="NEW_CUSTOMERS",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            addon = await response.parse()
            assert_matches_type(AddonPublishAddonResponse, addon, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_publish_addon(self, async_client: AsyncStigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v1.events.addons.with_raw_response.publish_addon(
                id="",
                migration_type="NEW_CUSTOMERS",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_addon(self, async_client: AsyncStigg) -> None:
        addon = await async_client.v1.events.addons.retrieve_addon(
            "x",
        )
        assert_matches_type(AddonRetrieveAddonResponse, addon, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_addon(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.events.addons.with_raw_response.retrieve_addon(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        addon = await response.parse()
        assert_matches_type(AddonRetrieveAddonResponse, addon, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_addon(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.events.addons.with_streaming_response.retrieve_addon(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            addon = await response.parse()
            assert_matches_type(AddonRetrieveAddonResponse, addon, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve_addon(self, async_client: AsyncStigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v1.events.addons.with_raw_response.retrieve_addon(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_addon(self, async_client: AsyncStigg) -> None:
        addon = await async_client.v1.events.addons.update_addon(
            id="x",
        )
        assert_matches_type(AddonUpdateAddonResponse, addon, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_addon_with_all_params(self, async_client: AsyncStigg) -> None:
        addon = await async_client.v1.events.addons.update_addon(
            id="x",
            billing_id="billingId",
            dependencies=["string"],
            description="description",
            display_name="displayName",
            max_quantity=0,
            metadata={"foo": "string"},
        )
        assert_matches_type(AddonUpdateAddonResponse, addon, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_addon(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.events.addons.with_raw_response.update_addon(
            id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        addon = await response.parse()
        assert_matches_type(AddonUpdateAddonResponse, addon, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_addon(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.events.addons.with_streaming_response.update_addon(
            id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            addon = await response.parse()
            assert_matches_type(AddonUpdateAddonResponse, addon, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_addon(self, async_client: AsyncStigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v1.events.addons.with_raw_response.update_addon(
                id="",
            )
