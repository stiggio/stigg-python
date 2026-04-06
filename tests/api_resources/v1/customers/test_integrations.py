# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from stigg import Stigg, AsyncStigg
from tests.utils import assert_matches_type
from stigg.pagination import SyncMyCursorIDPage, AsyncMyCursorIDPage
from stigg.types.v1.customers import (
    IntegrationLinkResponse,
    IntegrationListResponse,
    IntegrationUnlinkResponse,
    IntegrationUpdateResponse,
    IntegrationRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIntegrations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Stigg) -> None:
        integration = client.v1.customers.integrations.retrieve(
            integration_id="integrationId",
            id="id",
        )
        assert_matches_type(IntegrationRetrieveResponse, integration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Stigg) -> None:
        response = client.v1.customers.integrations.with_raw_response.retrieve(
            integration_id="integrationId",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = response.parse()
        assert_matches_type(IntegrationRetrieveResponse, integration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Stigg) -> None:
        with client.v1.customers.integrations.with_streaming_response.retrieve(
            integration_id="integrationId",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration = response.parse()
            assert_matches_type(IntegrationRetrieveResponse, integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Stigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v1.customers.integrations.with_raw_response.retrieve(
                integration_id="integrationId",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `integration_id` but received ''"):
            client.v1.customers.integrations.with_raw_response.retrieve(
                integration_id="",
                id="id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Stigg) -> None:
        integration = client.v1.customers.integrations.update(
            integration_id="integrationId",
            id="id",
            synced_entity_id="syncedEntityId",
        )
        assert_matches_type(IntegrationUpdateResponse, integration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Stigg) -> None:
        response = client.v1.customers.integrations.with_raw_response.update(
            integration_id="integrationId",
            id="id",
            synced_entity_id="syncedEntityId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = response.parse()
        assert_matches_type(IntegrationUpdateResponse, integration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Stigg) -> None:
        with client.v1.customers.integrations.with_streaming_response.update(
            integration_id="integrationId",
            id="id",
            synced_entity_id="syncedEntityId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration = response.parse()
            assert_matches_type(IntegrationUpdateResponse, integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Stigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v1.customers.integrations.with_raw_response.update(
                integration_id="integrationId",
                id="",
                synced_entity_id="syncedEntityId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `integration_id` but received ''"):
            client.v1.customers.integrations.with_raw_response.update(
                integration_id="",
                id="id",
                synced_entity_id="syncedEntityId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Stigg) -> None:
        integration = client.v1.customers.integrations.list(
            id="x",
        )
        assert_matches_type(SyncMyCursorIDPage[IntegrationListResponse], integration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Stigg) -> None:
        integration = client.v1.customers.integrations.list(
            id="x",
            after="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            before="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=1,
            vendor_identifier="vendorIdentifier",
        )
        assert_matches_type(SyncMyCursorIDPage[IntegrationListResponse], integration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Stigg) -> None:
        response = client.v1.customers.integrations.with_raw_response.list(
            id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = response.parse()
        assert_matches_type(SyncMyCursorIDPage[IntegrationListResponse], integration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Stigg) -> None:
        with client.v1.customers.integrations.with_streaming_response.list(
            id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration = response.parse()
            assert_matches_type(SyncMyCursorIDPage[IntegrationListResponse], integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Stigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v1.customers.integrations.with_raw_response.list(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_link(self, client: Stigg) -> None:
        integration = client.v1.customers.integrations.link(
            path_id="x",
            body_id="id",
            synced_entity_id="syncedEntityId",
            vendor_identifier="AUTH0",
        )
        assert_matches_type(IntegrationLinkResponse, integration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_link(self, client: Stigg) -> None:
        response = client.v1.customers.integrations.with_raw_response.link(
            path_id="x",
            body_id="id",
            synced_entity_id="syncedEntityId",
            vendor_identifier="AUTH0",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = response.parse()
        assert_matches_type(IntegrationLinkResponse, integration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_link(self, client: Stigg) -> None:
        with client.v1.customers.integrations.with_streaming_response.link(
            path_id="x",
            body_id="id",
            synced_entity_id="syncedEntityId",
            vendor_identifier="AUTH0",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration = response.parse()
            assert_matches_type(IntegrationLinkResponse, integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_link(self, client: Stigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.v1.customers.integrations.with_raw_response.link(
                path_id="",
                body_id="id",
                synced_entity_id="syncedEntityId",
                vendor_identifier="AUTH0",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_unlink(self, client: Stigg) -> None:
        integration = client.v1.customers.integrations.unlink(
            integration_id="integrationId",
            id="id",
        )
        assert_matches_type(IntegrationUnlinkResponse, integration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_unlink(self, client: Stigg) -> None:
        response = client.v1.customers.integrations.with_raw_response.unlink(
            integration_id="integrationId",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = response.parse()
        assert_matches_type(IntegrationUnlinkResponse, integration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_unlink(self, client: Stigg) -> None:
        with client.v1.customers.integrations.with_streaming_response.unlink(
            integration_id="integrationId",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration = response.parse()
            assert_matches_type(IntegrationUnlinkResponse, integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_unlink(self, client: Stigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v1.customers.integrations.with_raw_response.unlink(
                integration_id="integrationId",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `integration_id` but received ''"):
            client.v1.customers.integrations.with_raw_response.unlink(
                integration_id="",
                id="id",
            )


class TestAsyncIntegrations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncStigg) -> None:
        integration = await async_client.v1.customers.integrations.retrieve(
            integration_id="integrationId",
            id="id",
        )
        assert_matches_type(IntegrationRetrieveResponse, integration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.customers.integrations.with_raw_response.retrieve(
            integration_id="integrationId",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = await response.parse()
        assert_matches_type(IntegrationRetrieveResponse, integration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.customers.integrations.with_streaming_response.retrieve(
            integration_id="integrationId",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration = await response.parse()
            assert_matches_type(IntegrationRetrieveResponse, integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncStigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v1.customers.integrations.with_raw_response.retrieve(
                integration_id="integrationId",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `integration_id` but received ''"):
            await async_client.v1.customers.integrations.with_raw_response.retrieve(
                integration_id="",
                id="id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncStigg) -> None:
        integration = await async_client.v1.customers.integrations.update(
            integration_id="integrationId",
            id="id",
            synced_entity_id="syncedEntityId",
        )
        assert_matches_type(IntegrationUpdateResponse, integration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.customers.integrations.with_raw_response.update(
            integration_id="integrationId",
            id="id",
            synced_entity_id="syncedEntityId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = await response.parse()
        assert_matches_type(IntegrationUpdateResponse, integration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.customers.integrations.with_streaming_response.update(
            integration_id="integrationId",
            id="id",
            synced_entity_id="syncedEntityId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration = await response.parse()
            assert_matches_type(IntegrationUpdateResponse, integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncStigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v1.customers.integrations.with_raw_response.update(
                integration_id="integrationId",
                id="",
                synced_entity_id="syncedEntityId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `integration_id` but received ''"):
            await async_client.v1.customers.integrations.with_raw_response.update(
                integration_id="",
                id="id",
                synced_entity_id="syncedEntityId",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncStigg) -> None:
        integration = await async_client.v1.customers.integrations.list(
            id="x",
        )
        assert_matches_type(AsyncMyCursorIDPage[IntegrationListResponse], integration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncStigg) -> None:
        integration = await async_client.v1.customers.integrations.list(
            id="x",
            after="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            before="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=1,
            vendor_identifier="vendorIdentifier",
        )
        assert_matches_type(AsyncMyCursorIDPage[IntegrationListResponse], integration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.customers.integrations.with_raw_response.list(
            id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = await response.parse()
        assert_matches_type(AsyncMyCursorIDPage[IntegrationListResponse], integration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.customers.integrations.with_streaming_response.list(
            id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration = await response.parse()
            assert_matches_type(AsyncMyCursorIDPage[IntegrationListResponse], integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncStigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v1.customers.integrations.with_raw_response.list(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_link(self, async_client: AsyncStigg) -> None:
        integration = await async_client.v1.customers.integrations.link(
            path_id="x",
            body_id="id",
            synced_entity_id="syncedEntityId",
            vendor_identifier="AUTH0",
        )
        assert_matches_type(IntegrationLinkResponse, integration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_link(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.customers.integrations.with_raw_response.link(
            path_id="x",
            body_id="id",
            synced_entity_id="syncedEntityId",
            vendor_identifier="AUTH0",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = await response.parse()
        assert_matches_type(IntegrationLinkResponse, integration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_link(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.customers.integrations.with_streaming_response.link(
            path_id="x",
            body_id="id",
            synced_entity_id="syncedEntityId",
            vendor_identifier="AUTH0",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration = await response.parse()
            assert_matches_type(IntegrationLinkResponse, integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_link(self, async_client: AsyncStigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.v1.customers.integrations.with_raw_response.link(
                path_id="",
                body_id="id",
                synced_entity_id="syncedEntityId",
                vendor_identifier="AUTH0",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_unlink(self, async_client: AsyncStigg) -> None:
        integration = await async_client.v1.customers.integrations.unlink(
            integration_id="integrationId",
            id="id",
        )
        assert_matches_type(IntegrationUnlinkResponse, integration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_unlink(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.customers.integrations.with_raw_response.unlink(
            integration_id="integrationId",
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        integration = await response.parse()
        assert_matches_type(IntegrationUnlinkResponse, integration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_unlink(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.customers.integrations.with_streaming_response.unlink(
            integration_id="integrationId",
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            integration = await response.parse()
            assert_matches_type(IntegrationUnlinkResponse, integration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_unlink(self, async_client: AsyncStigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v1.customers.integrations.with_raw_response.unlink(
                integration_id="integrationId",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `integration_id` but received ''"):
            await async_client.v1.customers.integrations.with_raw_response.unlink(
                integration_id="",
                id="id",
            )
