# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from stigg import Stigg, AsyncStigg
from tests.utils import assert_matches_type
from stigg.types.v1 import PermissionCheckResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPermissions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_check(self, client: Stigg) -> None:
        permission = client.v1.permissions.check(
            user_id="userId",
            resources_and_actions=[
                {
                    "action": "read",
                    "resource": "product",
                }
            ],
        )
        assert_matches_type(PermissionCheckResponse, permission, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_check(self, client: Stigg) -> None:
        response = client.v1.permissions.with_raw_response.check(
            user_id="userId",
            resources_and_actions=[
                {
                    "action": "read",
                    "resource": "product",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        permission = response.parse()
        assert_matches_type(PermissionCheckResponse, permission, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_check(self, client: Stigg) -> None:
        with client.v1.permissions.with_streaming_response.check(
            user_id="userId",
            resources_and_actions=[
                {
                    "action": "read",
                    "resource": "product",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            permission = response.parse()
            assert_matches_type(PermissionCheckResponse, permission, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPermissions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_check(self, async_client: AsyncStigg) -> None:
        permission = await async_client.v1.permissions.check(
            user_id="userId",
            resources_and_actions=[
                {
                    "action": "read",
                    "resource": "product",
                }
            ],
        )
        assert_matches_type(PermissionCheckResponse, permission, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_check(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.permissions.with_raw_response.check(
            user_id="userId",
            resources_and_actions=[
                {
                    "action": "read",
                    "resource": "product",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        permission = await response.parse()
        assert_matches_type(PermissionCheckResponse, permission, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_check(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.permissions.with_streaming_response.check(
            user_id="userId",
            resources_and_actions=[
                {
                    "action": "read",
                    "resource": "product",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            permission = await response.parse()
            assert_matches_type(PermissionCheckResponse, permission, path=["response"])

        assert cast(Any, response.is_closed) is True
