# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from stigg import Stigg, AsyncStigg
from tests.utils import assert_matches_type
from stigg.types.v1.events.addons import DraftCreateAddonDraftResponse, DraftRemoveAddonDraftResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDraft:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_addon_draft(self, client: Stigg) -> None:
        draft = client.v1.events.addons.draft.create_addon_draft(
            "x",
        )
        assert_matches_type(DraftCreateAddonDraftResponse, draft, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_addon_draft(self, client: Stigg) -> None:
        response = client.v1.events.addons.draft.with_raw_response.create_addon_draft(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        draft = response.parse()
        assert_matches_type(DraftCreateAddonDraftResponse, draft, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_addon_draft(self, client: Stigg) -> None:
        with client.v1.events.addons.draft.with_streaming_response.create_addon_draft(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            draft = response.parse()
            assert_matches_type(DraftCreateAddonDraftResponse, draft, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create_addon_draft(self, client: Stigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v1.events.addons.draft.with_raw_response.create_addon_draft(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_remove_addon_draft(self, client: Stigg) -> None:
        draft = client.v1.events.addons.draft.remove_addon_draft(
            "x",
        )
        assert_matches_type(DraftRemoveAddonDraftResponse, draft, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_remove_addon_draft(self, client: Stigg) -> None:
        response = client.v1.events.addons.draft.with_raw_response.remove_addon_draft(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        draft = response.parse()
        assert_matches_type(DraftRemoveAddonDraftResponse, draft, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_remove_addon_draft(self, client: Stigg) -> None:
        with client.v1.events.addons.draft.with_streaming_response.remove_addon_draft(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            draft = response.parse()
            assert_matches_type(DraftRemoveAddonDraftResponse, draft, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_remove_addon_draft(self, client: Stigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v1.events.addons.draft.with_raw_response.remove_addon_draft(
                "",
            )


class TestAsyncDraft:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_addon_draft(self, async_client: AsyncStigg) -> None:
        draft = await async_client.v1.events.addons.draft.create_addon_draft(
            "x",
        )
        assert_matches_type(DraftCreateAddonDraftResponse, draft, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_addon_draft(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.events.addons.draft.with_raw_response.create_addon_draft(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        draft = await response.parse()
        assert_matches_type(DraftCreateAddonDraftResponse, draft, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_addon_draft(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.events.addons.draft.with_streaming_response.create_addon_draft(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            draft = await response.parse()
            assert_matches_type(DraftCreateAddonDraftResponse, draft, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create_addon_draft(self, async_client: AsyncStigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v1.events.addons.draft.with_raw_response.create_addon_draft(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_remove_addon_draft(self, async_client: AsyncStigg) -> None:
        draft = await async_client.v1.events.addons.draft.remove_addon_draft(
            "x",
        )
        assert_matches_type(DraftRemoveAddonDraftResponse, draft, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_remove_addon_draft(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.events.addons.draft.with_raw_response.remove_addon_draft(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        draft = await response.parse()
        assert_matches_type(DraftRemoveAddonDraftResponse, draft, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_remove_addon_draft(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.events.addons.draft.with_streaming_response.remove_addon_draft(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            draft = await response.parse()
            assert_matches_type(DraftRemoveAddonDraftResponse, draft, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_remove_addon_draft(self, async_client: AsyncStigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v1.events.addons.draft.with_raw_response.remove_addon_draft(
                "",
            )
