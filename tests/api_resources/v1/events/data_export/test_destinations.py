# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from stigg import Stigg, AsyncStigg
from tests.utils import assert_matches_type
from stigg.types.v1.events.data_export import (
    DestinationCreateResponse,
    DestinationDeleteResponse,
    DestinationUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDestinations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Stigg) -> None:
        destination = client.v1.events.data_export.destinations.create(
            destination_id="x",
            destination_type="x",
        )
        assert_matches_type(DestinationCreateResponse, destination, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Stigg) -> None:
        destination = client.v1.events.data_export.destinations.create(
            destination_id="x",
            destination_type="x",
            enabled_models=["x"],
            x_account_id="X-ACCOUNT-ID",
            x_environment_id="X-ENVIRONMENT-ID",
        )
        assert_matches_type(DestinationCreateResponse, destination, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Stigg) -> None:
        response = client.v1.events.data_export.destinations.with_raw_response.create(
            destination_id="x",
            destination_type="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        destination = response.parse()
        assert_matches_type(DestinationCreateResponse, destination, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Stigg) -> None:
        with client.v1.events.data_export.destinations.with_streaming_response.create(
            destination_id="x",
            destination_type="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            destination = response.parse()
            assert_matches_type(DestinationCreateResponse, destination, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Stigg) -> None:
        destination = client.v1.events.data_export.destinations.update(
            destination_id="x",
            enabled_models=["x"],
            integration_id="x",
        )
        assert_matches_type(DestinationUpdateResponse, destination, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Stigg) -> None:
        destination = client.v1.events.data_export.destinations.update(
            destination_id="x",
            enabled_models=["x"],
            integration_id="x",
            x_account_id="X-ACCOUNT-ID",
            x_environment_id="X-ENVIRONMENT-ID",
        )
        assert_matches_type(DestinationUpdateResponse, destination, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Stigg) -> None:
        response = client.v1.events.data_export.destinations.with_raw_response.update(
            destination_id="x",
            enabled_models=["x"],
            integration_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        destination = response.parse()
        assert_matches_type(DestinationUpdateResponse, destination, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Stigg) -> None:
        with client.v1.events.data_export.destinations.with_streaming_response.update(
            destination_id="x",
            enabled_models=["x"],
            integration_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            destination = response.parse()
            assert_matches_type(DestinationUpdateResponse, destination, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Stigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `destination_id` but received ''"):
            client.v1.events.data_export.destinations.with_raw_response.update(
                destination_id="",
                enabled_models=["x"],
                integration_id="x",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Stigg) -> None:
        destination = client.v1.events.data_export.destinations.delete(
            destination_id="x",
        )
        assert_matches_type(DestinationDeleteResponse, destination, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: Stigg) -> None:
        destination = client.v1.events.data_export.destinations.delete(
            destination_id="x",
            x_account_id="X-ACCOUNT-ID",
            x_environment_id="X-ENVIRONMENT-ID",
        )
        assert_matches_type(DestinationDeleteResponse, destination, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Stigg) -> None:
        response = client.v1.events.data_export.destinations.with_raw_response.delete(
            destination_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        destination = response.parse()
        assert_matches_type(DestinationDeleteResponse, destination, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Stigg) -> None:
        with client.v1.events.data_export.destinations.with_streaming_response.delete(
            destination_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            destination = response.parse()
            assert_matches_type(DestinationDeleteResponse, destination, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Stigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `destination_id` but received ''"):
            client.v1.events.data_export.destinations.with_raw_response.delete(
                destination_id="",
            )


class TestAsyncDestinations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncStigg) -> None:
        destination = await async_client.v1.events.data_export.destinations.create(
            destination_id="x",
            destination_type="x",
        )
        assert_matches_type(DestinationCreateResponse, destination, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncStigg) -> None:
        destination = await async_client.v1.events.data_export.destinations.create(
            destination_id="x",
            destination_type="x",
            enabled_models=["x"],
            x_account_id="X-ACCOUNT-ID",
            x_environment_id="X-ENVIRONMENT-ID",
        )
        assert_matches_type(DestinationCreateResponse, destination, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.events.data_export.destinations.with_raw_response.create(
            destination_id="x",
            destination_type="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        destination = await response.parse()
        assert_matches_type(DestinationCreateResponse, destination, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.events.data_export.destinations.with_streaming_response.create(
            destination_id="x",
            destination_type="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            destination = await response.parse()
            assert_matches_type(DestinationCreateResponse, destination, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncStigg) -> None:
        destination = await async_client.v1.events.data_export.destinations.update(
            destination_id="x",
            enabled_models=["x"],
            integration_id="x",
        )
        assert_matches_type(DestinationUpdateResponse, destination, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncStigg) -> None:
        destination = await async_client.v1.events.data_export.destinations.update(
            destination_id="x",
            enabled_models=["x"],
            integration_id="x",
            x_account_id="X-ACCOUNT-ID",
            x_environment_id="X-ENVIRONMENT-ID",
        )
        assert_matches_type(DestinationUpdateResponse, destination, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.events.data_export.destinations.with_raw_response.update(
            destination_id="x",
            enabled_models=["x"],
            integration_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        destination = await response.parse()
        assert_matches_type(DestinationUpdateResponse, destination, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.events.data_export.destinations.with_streaming_response.update(
            destination_id="x",
            enabled_models=["x"],
            integration_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            destination = await response.parse()
            assert_matches_type(DestinationUpdateResponse, destination, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncStigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `destination_id` but received ''"):
            await async_client.v1.events.data_export.destinations.with_raw_response.update(
                destination_id="",
                enabled_models=["x"],
                integration_id="x",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncStigg) -> None:
        destination = await async_client.v1.events.data_export.destinations.delete(
            destination_id="x",
        )
        assert_matches_type(DestinationDeleteResponse, destination, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncStigg) -> None:
        destination = await async_client.v1.events.data_export.destinations.delete(
            destination_id="x",
            x_account_id="X-ACCOUNT-ID",
            x_environment_id="X-ENVIRONMENT-ID",
        )
        assert_matches_type(DestinationDeleteResponse, destination, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.events.data_export.destinations.with_raw_response.delete(
            destination_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        destination = await response.parse()
        assert_matches_type(DestinationDeleteResponse, destination, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.events.data_export.destinations.with_streaming_response.delete(
            destination_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            destination = await response.parse()
            assert_matches_type(DestinationDeleteResponse, destination, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncStigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `destination_id` but received ''"):
            await async_client.v1.events.data_export.destinations.with_raw_response.delete(
                destination_id="",
            )
