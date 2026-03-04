# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .usage import (
    UsageResource,
    AsyncUsageResource,
    UsageResourceWithRawResponse,
    AsyncUsageResourceWithRawResponse,
    UsageResourceWithStreamingResponse,
    AsyncUsageResourceWithStreamingResponse,
)
from .events import (
    EventsResource,
    AsyncEventsResource,
    EventsResourceWithRawResponse,
    AsyncEventsResourceWithRawResponse,
    EventsResourceWithStreamingResponse,
    AsyncEventsResourceWithStreamingResponse,
)
from .coupons import (
    CouponsResource,
    AsyncCouponsResource,
    CouponsResourceWithRawResponse,
    AsyncCouponsResourceWithRawResponse,
    CouponsResourceWithStreamingResponse,
    AsyncCouponsResourceWithStreamingResponse,
)
from .features import (
    FeaturesResource,
    AsyncFeaturesResource,
    FeaturesResourceWithRawResponse,
    AsyncFeaturesResourceWithRawResponse,
    FeaturesResourceWithStreamingResponse,
    AsyncFeaturesResourceWithStreamingResponse,
)
from .products import (
    ProductsResource,
    AsyncProductsResource,
    ProductsResourceWithRawResponse,
    AsyncProductsResourceWithRawResponse,
    ProductsResourceWithStreamingResponse,
    AsyncProductsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .plans.plans import (
    PlansResource,
    AsyncPlansResource,
    PlansResourceWithRawResponse,
    AsyncPlansResourceWithRawResponse,
    PlansResourceWithStreamingResponse,
    AsyncPlansResourceWithStreamingResponse,
)
from .addons.addons import (
    AddonsResource,
    AsyncAddonsResource,
    AddonsResourceWithRawResponse,
    AsyncAddonsResourceWithRawResponse,
    AddonsResourceWithStreamingResponse,
    AsyncAddonsResourceWithStreamingResponse,
)
from .customers.customers import (
    CustomersResource,
    AsyncCustomersResource,
    CustomersResourceWithRawResponse,
    AsyncCustomersResourceWithRawResponse,
    CustomersResourceWithStreamingResponse,
    AsyncCustomersResourceWithStreamingResponse,
)
from .subscriptions.subscriptions import (
    SubscriptionsResource,
    AsyncSubscriptionsResource,
    SubscriptionsResourceWithRawResponse,
    AsyncSubscriptionsResourceWithRawResponse,
    SubscriptionsResourceWithStreamingResponse,
    AsyncSubscriptionsResourceWithStreamingResponse,
)

__all__ = ["V1Resource", "AsyncV1Resource"]


class V1Resource(SyncAPIResource):
    @cached_property
    def customers(self) -> CustomersResource:
        return CustomersResource(self._client)

    @cached_property
    def subscriptions(self) -> SubscriptionsResource:
        return SubscriptionsResource(self._client)

    @cached_property
    def coupons(self) -> CouponsResource:
        """Operations related to coupons"""
        return CouponsResource(self._client)

    @cached_property
    def events(self) -> EventsResource:
        """Operations related to usage & metering"""
        return EventsResource(self._client)

    @cached_property
    def features(self) -> FeaturesResource:
        """Operations related to features"""
        return FeaturesResource(self._client)

    @cached_property
    def addons(self) -> AddonsResource:
        """Operations related to addons"""
        return AddonsResource(self._client)

    @cached_property
    def plans(self) -> PlansResource:
        """Operations related to plans"""
        return PlansResource(self._client)

    @cached_property
    def usage(self) -> UsageResource:
        """Operations related to usage & metering"""
        return UsageResource(self._client)

    @cached_property
    def products(self) -> ProductsResource:
        """Operations related to products"""
        return ProductsResource(self._client)

    @cached_property
    def with_raw_response(self) -> V1ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stiggio/stigg-python#accessing-raw-response-data-eg-headers
        """
        return V1ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V1ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stiggio/stigg-python#with_streaming_response
        """
        return V1ResourceWithStreamingResponse(self)


class AsyncV1Resource(AsyncAPIResource):
    @cached_property
    def customers(self) -> AsyncCustomersResource:
        return AsyncCustomersResource(self._client)

    @cached_property
    def subscriptions(self) -> AsyncSubscriptionsResource:
        return AsyncSubscriptionsResource(self._client)

    @cached_property
    def coupons(self) -> AsyncCouponsResource:
        """Operations related to coupons"""
        return AsyncCouponsResource(self._client)

    @cached_property
    def events(self) -> AsyncEventsResource:
        """Operations related to usage & metering"""
        return AsyncEventsResource(self._client)

    @cached_property
    def features(self) -> AsyncFeaturesResource:
        """Operations related to features"""
        return AsyncFeaturesResource(self._client)

    @cached_property
    def addons(self) -> AsyncAddonsResource:
        """Operations related to addons"""
        return AsyncAddonsResource(self._client)

    @cached_property
    def plans(self) -> AsyncPlansResource:
        """Operations related to plans"""
        return AsyncPlansResource(self._client)

    @cached_property
    def usage(self) -> AsyncUsageResource:
        """Operations related to usage & metering"""
        return AsyncUsageResource(self._client)

    @cached_property
    def products(self) -> AsyncProductsResource:
        """Operations related to products"""
        return AsyncProductsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncV1ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stiggio/stigg-python#accessing-raw-response-data-eg-headers
        """
        return AsyncV1ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV1ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stiggio/stigg-python#with_streaming_response
        """
        return AsyncV1ResourceWithStreamingResponse(self)


class V1ResourceWithRawResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

    @cached_property
    def customers(self) -> CustomersResourceWithRawResponse:
        return CustomersResourceWithRawResponse(self._v1.customers)

    @cached_property
    def subscriptions(self) -> SubscriptionsResourceWithRawResponse:
        return SubscriptionsResourceWithRawResponse(self._v1.subscriptions)

    @cached_property
    def coupons(self) -> CouponsResourceWithRawResponse:
        """Operations related to coupons"""
        return CouponsResourceWithRawResponse(self._v1.coupons)

    @cached_property
    def events(self) -> EventsResourceWithRawResponse:
        """Operations related to usage & metering"""
        return EventsResourceWithRawResponse(self._v1.events)

    @cached_property
    def features(self) -> FeaturesResourceWithRawResponse:
        """Operations related to features"""
        return FeaturesResourceWithRawResponse(self._v1.features)

    @cached_property
    def addons(self) -> AddonsResourceWithRawResponse:
        """Operations related to addons"""
        return AddonsResourceWithRawResponse(self._v1.addons)

    @cached_property
    def plans(self) -> PlansResourceWithRawResponse:
        """Operations related to plans"""
        return PlansResourceWithRawResponse(self._v1.plans)

    @cached_property
    def usage(self) -> UsageResourceWithRawResponse:
        """Operations related to usage & metering"""
        return UsageResourceWithRawResponse(self._v1.usage)

    @cached_property
    def products(self) -> ProductsResourceWithRawResponse:
        """Operations related to products"""
        return ProductsResourceWithRawResponse(self._v1.products)


class AsyncV1ResourceWithRawResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

    @cached_property
    def customers(self) -> AsyncCustomersResourceWithRawResponse:
        return AsyncCustomersResourceWithRawResponse(self._v1.customers)

    @cached_property
    def subscriptions(self) -> AsyncSubscriptionsResourceWithRawResponse:
        return AsyncSubscriptionsResourceWithRawResponse(self._v1.subscriptions)

    @cached_property
    def coupons(self) -> AsyncCouponsResourceWithRawResponse:
        """Operations related to coupons"""
        return AsyncCouponsResourceWithRawResponse(self._v1.coupons)

    @cached_property
    def events(self) -> AsyncEventsResourceWithRawResponse:
        """Operations related to usage & metering"""
        return AsyncEventsResourceWithRawResponse(self._v1.events)

    @cached_property
    def features(self) -> AsyncFeaturesResourceWithRawResponse:
        """Operations related to features"""
        return AsyncFeaturesResourceWithRawResponse(self._v1.features)

    @cached_property
    def addons(self) -> AsyncAddonsResourceWithRawResponse:
        """Operations related to addons"""
        return AsyncAddonsResourceWithRawResponse(self._v1.addons)

    @cached_property
    def plans(self) -> AsyncPlansResourceWithRawResponse:
        """Operations related to plans"""
        return AsyncPlansResourceWithRawResponse(self._v1.plans)

    @cached_property
    def usage(self) -> AsyncUsageResourceWithRawResponse:
        """Operations related to usage & metering"""
        return AsyncUsageResourceWithRawResponse(self._v1.usage)

    @cached_property
    def products(self) -> AsyncProductsResourceWithRawResponse:
        """Operations related to products"""
        return AsyncProductsResourceWithRawResponse(self._v1.products)


class V1ResourceWithStreamingResponse:
    def __init__(self, v1: V1Resource) -> None:
        self._v1 = v1

    @cached_property
    def customers(self) -> CustomersResourceWithStreamingResponse:
        return CustomersResourceWithStreamingResponse(self._v1.customers)

    @cached_property
    def subscriptions(self) -> SubscriptionsResourceWithStreamingResponse:
        return SubscriptionsResourceWithStreamingResponse(self._v1.subscriptions)

    @cached_property
    def coupons(self) -> CouponsResourceWithStreamingResponse:
        """Operations related to coupons"""
        return CouponsResourceWithStreamingResponse(self._v1.coupons)

    @cached_property
    def events(self) -> EventsResourceWithStreamingResponse:
        """Operations related to usage & metering"""
        return EventsResourceWithStreamingResponse(self._v1.events)

    @cached_property
    def features(self) -> FeaturesResourceWithStreamingResponse:
        """Operations related to features"""
        return FeaturesResourceWithStreamingResponse(self._v1.features)

    @cached_property
    def addons(self) -> AddonsResourceWithStreamingResponse:
        """Operations related to addons"""
        return AddonsResourceWithStreamingResponse(self._v1.addons)

    @cached_property
    def plans(self) -> PlansResourceWithStreamingResponse:
        """Operations related to plans"""
        return PlansResourceWithStreamingResponse(self._v1.plans)

    @cached_property
    def usage(self) -> UsageResourceWithStreamingResponse:
        """Operations related to usage & metering"""
        return UsageResourceWithStreamingResponse(self._v1.usage)

    @cached_property
    def products(self) -> ProductsResourceWithStreamingResponse:
        """Operations related to products"""
        return ProductsResourceWithStreamingResponse(self._v1.products)


class AsyncV1ResourceWithStreamingResponse:
    def __init__(self, v1: AsyncV1Resource) -> None:
        self._v1 = v1

    @cached_property
    def customers(self) -> AsyncCustomersResourceWithStreamingResponse:
        return AsyncCustomersResourceWithStreamingResponse(self._v1.customers)

    @cached_property
    def subscriptions(self) -> AsyncSubscriptionsResourceWithStreamingResponse:
        return AsyncSubscriptionsResourceWithStreamingResponse(self._v1.subscriptions)

    @cached_property
    def coupons(self) -> AsyncCouponsResourceWithStreamingResponse:
        """Operations related to coupons"""
        return AsyncCouponsResourceWithStreamingResponse(self._v1.coupons)

    @cached_property
    def events(self) -> AsyncEventsResourceWithStreamingResponse:
        """Operations related to usage & metering"""
        return AsyncEventsResourceWithStreamingResponse(self._v1.events)

    @cached_property
    def features(self) -> AsyncFeaturesResourceWithStreamingResponse:
        """Operations related to features"""
        return AsyncFeaturesResourceWithStreamingResponse(self._v1.features)

    @cached_property
    def addons(self) -> AsyncAddonsResourceWithStreamingResponse:
        """Operations related to addons"""
        return AsyncAddonsResourceWithStreamingResponse(self._v1.addons)

    @cached_property
    def plans(self) -> AsyncPlansResourceWithStreamingResponse:
        """Operations related to plans"""
        return AsyncPlansResourceWithStreamingResponse(self._v1.plans)

    @cached_property
    def usage(self) -> AsyncUsageResourceWithStreamingResponse:
        """Operations related to usage & metering"""
        return AsyncUsageResourceWithStreamingResponse(self._v1.usage)

    @cached_property
    def products(self) -> AsyncProductsResourceWithStreamingResponse:
        """Operations related to products"""
        return AsyncProductsResourceWithStreamingResponse(self._v1.products)
