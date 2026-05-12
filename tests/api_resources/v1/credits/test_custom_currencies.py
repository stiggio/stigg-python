# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from stigg import Stigg, AsyncStigg
from tests.utils import assert_matches_type
from stigg.pagination import SyncMyCursorIDPage, AsyncMyCursorIDPage
from stigg.types.v1.credits import (
    CustomCurrency,
    CustomCurrencyListResponse,
    CustomCurrencyListAssociatedEntitiesResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCustomCurrencies:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Stigg) -> None:
        custom_currency = client.v1.credits.custom_currencies.create(
            id="id",
            display_name="displayName",
        )
        assert_matches_type(CustomCurrency, custom_currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Stigg) -> None:
        custom_currency = client.v1.credits.custom_currencies.create(
            id="id",
            display_name="displayName",
            description="description",
            metadata={"foo": "string"},
            symbol="symbol",
            units={
                "plural": "plural",
                "singular": "singular",
            },
        )
        assert_matches_type(CustomCurrency, custom_currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Stigg) -> None:
        response = client.v1.credits.custom_currencies.with_raw_response.create(
            id="id",
            display_name="displayName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_currency = response.parse()
        assert_matches_type(CustomCurrency, custom_currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Stigg) -> None:
        with client.v1.credits.custom_currencies.with_streaming_response.create(
            id="id",
            display_name="displayName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_currency = response.parse()
            assert_matches_type(CustomCurrency, custom_currency, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Stigg) -> None:
        custom_currency = client.v1.credits.custom_currencies.update(
            currency_id="currencyId",
        )
        assert_matches_type(CustomCurrency, custom_currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Stigg) -> None:
        custom_currency = client.v1.credits.custom_currencies.update(
            currency_id="currencyId",
            description="description",
            display_name="displayName",
            metadata={"foo": "string"},
            symbol="symbol",
            units={
                "plural": "plural",
                "singular": "singular",
            },
        )
        assert_matches_type(CustomCurrency, custom_currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Stigg) -> None:
        response = client.v1.credits.custom_currencies.with_raw_response.update(
            currency_id="currencyId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_currency = response.parse()
        assert_matches_type(CustomCurrency, custom_currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Stigg) -> None:
        with client.v1.credits.custom_currencies.with_streaming_response.update(
            currency_id="currencyId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_currency = response.parse()
            assert_matches_type(CustomCurrency, custom_currency, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Stigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `currency_id` but received ''"):
            client.v1.credits.custom_currencies.with_raw_response.update(
                currency_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Stigg) -> None:
        custom_currency = client.v1.credits.custom_currencies.list()
        assert_matches_type(SyncMyCursorIDPage[CustomCurrencyListResponse], custom_currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Stigg) -> None:
        custom_currency = client.v1.credits.custom_currencies.list(
            after="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            before="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=1,
            status=["ACTIVE"],
        )
        assert_matches_type(SyncMyCursorIDPage[CustomCurrencyListResponse], custom_currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Stigg) -> None:
        response = client.v1.credits.custom_currencies.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_currency = response.parse()
        assert_matches_type(SyncMyCursorIDPage[CustomCurrencyListResponse], custom_currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Stigg) -> None:
        with client.v1.credits.custom_currencies.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_currency = response.parse()
            assert_matches_type(SyncMyCursorIDPage[CustomCurrencyListResponse], custom_currency, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_archive(self, client: Stigg) -> None:
        custom_currency = client.v1.credits.custom_currencies.archive(
            "currencyId",
        )
        assert_matches_type(CustomCurrency, custom_currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_archive(self, client: Stigg) -> None:
        response = client.v1.credits.custom_currencies.with_raw_response.archive(
            "currencyId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_currency = response.parse()
        assert_matches_type(CustomCurrency, custom_currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_archive(self, client: Stigg) -> None:
        with client.v1.credits.custom_currencies.with_streaming_response.archive(
            "currencyId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_currency = response.parse()
            assert_matches_type(CustomCurrency, custom_currency, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_archive(self, client: Stigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `currency_id` but received ''"):
            client.v1.credits.custom_currencies.with_raw_response.archive(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_associated_entities(self, client: Stigg) -> None:
        custom_currency = client.v1.credits.custom_currencies.list_associated_entities(
            "currencyId",
        )
        assert_matches_type(CustomCurrencyListAssociatedEntitiesResponse, custom_currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_associated_entities(self, client: Stigg) -> None:
        response = client.v1.credits.custom_currencies.with_raw_response.list_associated_entities(
            "currencyId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_currency = response.parse()
        assert_matches_type(CustomCurrencyListAssociatedEntitiesResponse, custom_currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_associated_entities(self, client: Stigg) -> None:
        with client.v1.credits.custom_currencies.with_streaming_response.list_associated_entities(
            "currencyId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_currency = response.parse()
            assert_matches_type(CustomCurrencyListAssociatedEntitiesResponse, custom_currency, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_associated_entities(self, client: Stigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `currency_id` but received ''"):
            client.v1.credits.custom_currencies.with_raw_response.list_associated_entities(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_unarchive(self, client: Stigg) -> None:
        custom_currency = client.v1.credits.custom_currencies.unarchive(
            "currencyId",
        )
        assert_matches_type(CustomCurrency, custom_currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_unarchive(self, client: Stigg) -> None:
        response = client.v1.credits.custom_currencies.with_raw_response.unarchive(
            "currencyId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_currency = response.parse()
        assert_matches_type(CustomCurrency, custom_currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_unarchive(self, client: Stigg) -> None:
        with client.v1.credits.custom_currencies.with_streaming_response.unarchive(
            "currencyId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_currency = response.parse()
            assert_matches_type(CustomCurrency, custom_currency, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_unarchive(self, client: Stigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `currency_id` but received ''"):
            client.v1.credits.custom_currencies.with_raw_response.unarchive(
                "",
            )


class TestAsyncCustomCurrencies:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncStigg) -> None:
        custom_currency = await async_client.v1.credits.custom_currencies.create(
            id="id",
            display_name="displayName",
        )
        assert_matches_type(CustomCurrency, custom_currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncStigg) -> None:
        custom_currency = await async_client.v1.credits.custom_currencies.create(
            id="id",
            display_name="displayName",
            description="description",
            metadata={"foo": "string"},
            symbol="symbol",
            units={
                "plural": "plural",
                "singular": "singular",
            },
        )
        assert_matches_type(CustomCurrency, custom_currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.credits.custom_currencies.with_raw_response.create(
            id="id",
            display_name="displayName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_currency = await response.parse()
        assert_matches_type(CustomCurrency, custom_currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.credits.custom_currencies.with_streaming_response.create(
            id="id",
            display_name="displayName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_currency = await response.parse()
            assert_matches_type(CustomCurrency, custom_currency, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncStigg) -> None:
        custom_currency = await async_client.v1.credits.custom_currencies.update(
            currency_id="currencyId",
        )
        assert_matches_type(CustomCurrency, custom_currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncStigg) -> None:
        custom_currency = await async_client.v1.credits.custom_currencies.update(
            currency_id="currencyId",
            description="description",
            display_name="displayName",
            metadata={"foo": "string"},
            symbol="symbol",
            units={
                "plural": "plural",
                "singular": "singular",
            },
        )
        assert_matches_type(CustomCurrency, custom_currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.credits.custom_currencies.with_raw_response.update(
            currency_id="currencyId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_currency = await response.parse()
        assert_matches_type(CustomCurrency, custom_currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.credits.custom_currencies.with_streaming_response.update(
            currency_id="currencyId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_currency = await response.parse()
            assert_matches_type(CustomCurrency, custom_currency, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncStigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `currency_id` but received ''"):
            await async_client.v1.credits.custom_currencies.with_raw_response.update(
                currency_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncStigg) -> None:
        custom_currency = await async_client.v1.credits.custom_currencies.list()
        assert_matches_type(AsyncMyCursorIDPage[CustomCurrencyListResponse], custom_currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncStigg) -> None:
        custom_currency = await async_client.v1.credits.custom_currencies.list(
            after="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            before="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=1,
            status=["ACTIVE"],
        )
        assert_matches_type(AsyncMyCursorIDPage[CustomCurrencyListResponse], custom_currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.credits.custom_currencies.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_currency = await response.parse()
        assert_matches_type(AsyncMyCursorIDPage[CustomCurrencyListResponse], custom_currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.credits.custom_currencies.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_currency = await response.parse()
            assert_matches_type(AsyncMyCursorIDPage[CustomCurrencyListResponse], custom_currency, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_archive(self, async_client: AsyncStigg) -> None:
        custom_currency = await async_client.v1.credits.custom_currencies.archive(
            "currencyId",
        )
        assert_matches_type(CustomCurrency, custom_currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_archive(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.credits.custom_currencies.with_raw_response.archive(
            "currencyId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_currency = await response.parse()
        assert_matches_type(CustomCurrency, custom_currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_archive(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.credits.custom_currencies.with_streaming_response.archive(
            "currencyId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_currency = await response.parse()
            assert_matches_type(CustomCurrency, custom_currency, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_archive(self, async_client: AsyncStigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `currency_id` but received ''"):
            await async_client.v1.credits.custom_currencies.with_raw_response.archive(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_associated_entities(self, async_client: AsyncStigg) -> None:
        custom_currency = await async_client.v1.credits.custom_currencies.list_associated_entities(
            "currencyId",
        )
        assert_matches_type(CustomCurrencyListAssociatedEntitiesResponse, custom_currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_associated_entities(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.credits.custom_currencies.with_raw_response.list_associated_entities(
            "currencyId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_currency = await response.parse()
        assert_matches_type(CustomCurrencyListAssociatedEntitiesResponse, custom_currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_associated_entities(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.credits.custom_currencies.with_streaming_response.list_associated_entities(
            "currencyId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_currency = await response.parse()
            assert_matches_type(CustomCurrencyListAssociatedEntitiesResponse, custom_currency, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_associated_entities(self, async_client: AsyncStigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `currency_id` but received ''"):
            await async_client.v1.credits.custom_currencies.with_raw_response.list_associated_entities(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_unarchive(self, async_client: AsyncStigg) -> None:
        custom_currency = await async_client.v1.credits.custom_currencies.unarchive(
            "currencyId",
        )
        assert_matches_type(CustomCurrency, custom_currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_unarchive(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.credits.custom_currencies.with_raw_response.unarchive(
            "currencyId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_currency = await response.parse()
        assert_matches_type(CustomCurrency, custom_currency, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_unarchive(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.credits.custom_currencies.with_streaming_response.unarchive(
            "currencyId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_currency = await response.parse()
            assert_matches_type(CustomCurrency, custom_currency, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_unarchive(self, async_client: AsyncStigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `currency_id` but received ''"):
            await async_client.v1.credits.custom_currencies.with_raw_response.unarchive(
                "",
            )
