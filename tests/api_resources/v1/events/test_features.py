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
    Feature,
    FeatureListFeaturesResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFeatures:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_archive_feature(self, client: Stigg) -> None:
        feature = client.v1.events.features.archive_feature(
            "x",
        )
        assert_matches_type(Feature, feature, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_archive_feature(self, client: Stigg) -> None:
        response = client.v1.events.features.with_raw_response.archive_feature(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feature = response.parse()
        assert_matches_type(Feature, feature, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_archive_feature(self, client: Stigg) -> None:
        with client.v1.events.features.with_streaming_response.archive_feature(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feature = response.parse()
            assert_matches_type(Feature, feature, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_archive_feature(self, client: Stigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v1.events.features.with_raw_response.archive_feature(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_feature(self, client: Stigg) -> None:
        feature = client.v1.events.features.create_feature(
            id="id",
            display_name="displayName",
            feature_type="BOOLEAN",
        )
        assert_matches_type(Feature, feature, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_feature_with_all_params(self, client: Stigg) -> None:
        feature = client.v1.events.features.create_feature(
            id="id",
            display_name="displayName",
            feature_type="BOOLEAN",
            description="description",
            enum_configuration=[
                {
                    "display_name": "displayName",
                    "value": "value",
                }
            ],
            feature_status="NEW",
            feature_units="featureUnits",
            feature_units_plural="featureUnitsPlural",
            metadata={"foo": "string"},
            meter_type="None",
            unit_transformation={
                "divide": 0,
                "feature_units": "featureUnits",
                "feature_units_plural": "featureUnitsPlural",
                "round": "UP",
            },
        )
        assert_matches_type(Feature, feature, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_feature(self, client: Stigg) -> None:
        response = client.v1.events.features.with_raw_response.create_feature(
            id="id",
            display_name="displayName",
            feature_type="BOOLEAN",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feature = response.parse()
        assert_matches_type(Feature, feature, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_feature(self, client: Stigg) -> None:
        with client.v1.events.features.with_streaming_response.create_feature(
            id="id",
            display_name="displayName",
            feature_type="BOOLEAN",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feature = response.parse()
            assert_matches_type(Feature, feature, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_features(self, client: Stigg) -> None:
        feature = client.v1.events.features.list_features()
        assert_matches_type(SyncMyCursorIDPage[FeatureListFeaturesResponse], feature, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_features_with_all_params(self, client: Stigg) -> None:
        feature = client.v1.events.features.list_features(
            id="id",
            after="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            before="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            created_at={
                "gt": parse_datetime("2019-12-27T18:11:19.117Z"),
                "gte": parse_datetime("2019-12-27T18:11:19.117Z"),
                "lt": parse_datetime("2019-12-27T18:11:19.117Z"),
                "lte": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            feature_type="featureType",
            limit=1,
            meter_type="meterType",
            status="status",
        )
        assert_matches_type(SyncMyCursorIDPage[FeatureListFeaturesResponse], feature, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_features(self, client: Stigg) -> None:
        response = client.v1.events.features.with_raw_response.list_features()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feature = response.parse()
        assert_matches_type(SyncMyCursorIDPage[FeatureListFeaturesResponse], feature, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_features(self, client: Stigg) -> None:
        with client.v1.events.features.with_streaming_response.list_features() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feature = response.parse()
            assert_matches_type(SyncMyCursorIDPage[FeatureListFeaturesResponse], feature, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_feature(self, client: Stigg) -> None:
        feature = client.v1.events.features.retrieve_feature(
            "x",
        )
        assert_matches_type(Feature, feature, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_feature(self, client: Stigg) -> None:
        response = client.v1.events.features.with_raw_response.retrieve_feature(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feature = response.parse()
        assert_matches_type(Feature, feature, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_feature(self, client: Stigg) -> None:
        with client.v1.events.features.with_streaming_response.retrieve_feature(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feature = response.parse()
            assert_matches_type(Feature, feature, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_feature(self, client: Stigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v1.events.features.with_raw_response.retrieve_feature(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_unarchive_feature(self, client: Stigg) -> None:
        feature = client.v1.events.features.unarchive_feature(
            "x",
        )
        assert_matches_type(Feature, feature, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_unarchive_feature(self, client: Stigg) -> None:
        response = client.v1.events.features.with_raw_response.unarchive_feature(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feature = response.parse()
        assert_matches_type(Feature, feature, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_unarchive_feature(self, client: Stigg) -> None:
        with client.v1.events.features.with_streaming_response.unarchive_feature(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feature = response.parse()
            assert_matches_type(Feature, feature, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_unarchive_feature(self, client: Stigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v1.events.features.with_raw_response.unarchive_feature(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_feature(self, client: Stigg) -> None:
        feature = client.v1.events.features.update_feature(
            id="x",
        )
        assert_matches_type(Feature, feature, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_feature_with_all_params(self, client: Stigg) -> None:
        feature = client.v1.events.features.update_feature(
            id="x",
            description="description",
            display_name="displayName",
            enum_configuration=[
                {
                    "display_name": "displayName",
                    "value": "value",
                }
            ],
            feature_units="featureUnits",
            feature_units_plural="featureUnitsPlural",
            metadata={"foo": "string"},
            meter={
                "aggregation": {
                    "function": "SUM",
                    "field": "field",
                },
                "filters": [
                    {
                        "conditions": [
                            {
                                "field": "field",
                                "operation": "EQUALS",
                                "value": "value",
                                "values": ["string"],
                            }
                        ]
                    }
                ],
            },
            unit_transformation={
                "divide": 0,
                "feature_units": "featureUnits",
                "feature_units_plural": "featureUnitsPlural",
                "round": "UP",
            },
        )
        assert_matches_type(Feature, feature, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_feature(self, client: Stigg) -> None:
        response = client.v1.events.features.with_raw_response.update_feature(
            id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feature = response.parse()
        assert_matches_type(Feature, feature, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_feature(self, client: Stigg) -> None:
        with client.v1.events.features.with_streaming_response.update_feature(
            id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feature = response.parse()
            assert_matches_type(Feature, feature, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_feature(self, client: Stigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v1.events.features.with_raw_response.update_feature(
                id="",
            )


class TestAsyncFeatures:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_archive_feature(self, async_client: AsyncStigg) -> None:
        feature = await async_client.v1.events.features.archive_feature(
            "x",
        )
        assert_matches_type(Feature, feature, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_archive_feature(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.events.features.with_raw_response.archive_feature(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feature = await response.parse()
        assert_matches_type(Feature, feature, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_archive_feature(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.events.features.with_streaming_response.archive_feature(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feature = await response.parse()
            assert_matches_type(Feature, feature, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_archive_feature(self, async_client: AsyncStigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v1.events.features.with_raw_response.archive_feature(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_feature(self, async_client: AsyncStigg) -> None:
        feature = await async_client.v1.events.features.create_feature(
            id="id",
            display_name="displayName",
            feature_type="BOOLEAN",
        )
        assert_matches_type(Feature, feature, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_feature_with_all_params(self, async_client: AsyncStigg) -> None:
        feature = await async_client.v1.events.features.create_feature(
            id="id",
            display_name="displayName",
            feature_type="BOOLEAN",
            description="description",
            enum_configuration=[
                {
                    "display_name": "displayName",
                    "value": "value",
                }
            ],
            feature_status="NEW",
            feature_units="featureUnits",
            feature_units_plural="featureUnitsPlural",
            metadata={"foo": "string"},
            meter_type="None",
            unit_transformation={
                "divide": 0,
                "feature_units": "featureUnits",
                "feature_units_plural": "featureUnitsPlural",
                "round": "UP",
            },
        )
        assert_matches_type(Feature, feature, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_feature(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.events.features.with_raw_response.create_feature(
            id="id",
            display_name="displayName",
            feature_type="BOOLEAN",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feature = await response.parse()
        assert_matches_type(Feature, feature, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_feature(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.events.features.with_streaming_response.create_feature(
            id="id",
            display_name="displayName",
            feature_type="BOOLEAN",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feature = await response.parse()
            assert_matches_type(Feature, feature, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_features(self, async_client: AsyncStigg) -> None:
        feature = await async_client.v1.events.features.list_features()
        assert_matches_type(AsyncMyCursorIDPage[FeatureListFeaturesResponse], feature, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_features_with_all_params(self, async_client: AsyncStigg) -> None:
        feature = await async_client.v1.events.features.list_features(
            id="id",
            after="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            before="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            created_at={
                "gt": parse_datetime("2019-12-27T18:11:19.117Z"),
                "gte": parse_datetime("2019-12-27T18:11:19.117Z"),
                "lt": parse_datetime("2019-12-27T18:11:19.117Z"),
                "lte": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            feature_type="featureType",
            limit=1,
            meter_type="meterType",
            status="status",
        )
        assert_matches_type(AsyncMyCursorIDPage[FeatureListFeaturesResponse], feature, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_features(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.events.features.with_raw_response.list_features()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feature = await response.parse()
        assert_matches_type(AsyncMyCursorIDPage[FeatureListFeaturesResponse], feature, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_features(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.events.features.with_streaming_response.list_features() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feature = await response.parse()
            assert_matches_type(AsyncMyCursorIDPage[FeatureListFeaturesResponse], feature, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_feature(self, async_client: AsyncStigg) -> None:
        feature = await async_client.v1.events.features.retrieve_feature(
            "x",
        )
        assert_matches_type(Feature, feature, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_feature(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.events.features.with_raw_response.retrieve_feature(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feature = await response.parse()
        assert_matches_type(Feature, feature, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_feature(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.events.features.with_streaming_response.retrieve_feature(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feature = await response.parse()
            assert_matches_type(Feature, feature, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_feature(self, async_client: AsyncStigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v1.events.features.with_raw_response.retrieve_feature(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_unarchive_feature(self, async_client: AsyncStigg) -> None:
        feature = await async_client.v1.events.features.unarchive_feature(
            "x",
        )
        assert_matches_type(Feature, feature, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_unarchive_feature(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.events.features.with_raw_response.unarchive_feature(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feature = await response.parse()
        assert_matches_type(Feature, feature, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_unarchive_feature(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.events.features.with_streaming_response.unarchive_feature(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feature = await response.parse()
            assert_matches_type(Feature, feature, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_unarchive_feature(self, async_client: AsyncStigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v1.events.features.with_raw_response.unarchive_feature(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_feature(self, async_client: AsyncStigg) -> None:
        feature = await async_client.v1.events.features.update_feature(
            id="x",
        )
        assert_matches_type(Feature, feature, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_feature_with_all_params(self, async_client: AsyncStigg) -> None:
        feature = await async_client.v1.events.features.update_feature(
            id="x",
            description="description",
            display_name="displayName",
            enum_configuration=[
                {
                    "display_name": "displayName",
                    "value": "value",
                }
            ],
            feature_units="featureUnits",
            feature_units_plural="featureUnitsPlural",
            metadata={"foo": "string"},
            meter={
                "aggregation": {
                    "function": "SUM",
                    "field": "field",
                },
                "filters": [
                    {
                        "conditions": [
                            {
                                "field": "field",
                                "operation": "EQUALS",
                                "value": "value",
                                "values": ["string"],
                            }
                        ]
                    }
                ],
            },
            unit_transformation={
                "divide": 0,
                "feature_units": "featureUnits",
                "feature_units_plural": "featureUnitsPlural",
                "round": "UP",
            },
        )
        assert_matches_type(Feature, feature, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_feature(self, async_client: AsyncStigg) -> None:
        response = await async_client.v1.events.features.with_raw_response.update_feature(
            id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feature = await response.parse()
        assert_matches_type(Feature, feature, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_feature(self, async_client: AsyncStigg) -> None:
        async with async_client.v1.events.features.with_streaming_response.update_feature(
            id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feature = await response.parse()
            assert_matches_type(Feature, feature, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_feature(self, async_client: AsyncStigg) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v1.events.features.with_raw_response.update_feature(
                id="",
            )
