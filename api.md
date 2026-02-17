# V1

## Customers

Types:

```python
from stigg.types.v1 import (
    CustomerResponse,
    CustomerListResponse,
    CustomerImportResponse,
    CustomerListResourcesResponse,
)
```

Methods:

- <code title="get /api/v1/customers/{id}">client.v1.customers.<a href="./src/stigg/resources/v1/customers/customers.py">retrieve</a>(id) -> <a href="./src/stigg/types/v1/customer_response.py">CustomerResponse</a></code>
- <code title="patch /api/v1/customers/{id}">client.v1.customers.<a href="./src/stigg/resources/v1/customers/customers.py">update</a>(id, \*\*<a href="src/stigg/types/v1/customer_update_params.py">params</a>) -> <a href="./src/stigg/types/v1/customer_response.py">CustomerResponse</a></code>
- <code title="get /api/v1/customers">client.v1.customers.<a href="./src/stigg/resources/v1/customers/customers.py">list</a>(\*\*<a href="src/stigg/types/v1/customer_list_params.py">params</a>) -> <a href="./src/stigg/types/v1/customer_list_response.py">SyncMyCursorIDPage[CustomerListResponse]</a></code>
- <code title="post /api/v1/customers/{id}/archive">client.v1.customers.<a href="./src/stigg/resources/v1/customers/customers.py">archive</a>(id) -> <a href="./src/stigg/types/v1/customer_response.py">CustomerResponse</a></code>
- <code title="post /api/v1/customers/import">client.v1.customers.<a href="./src/stigg/resources/v1/customers/customers.py">import\_</a>(\*\*<a href="src/stigg/types/v1/customer_import_params.py">params</a>) -> <a href="./src/stigg/types/v1/customer_import_response.py">CustomerImportResponse</a></code>
- <code title="get /api/v1/customers/{id}/resources">client.v1.customers.<a href="./src/stigg/resources/v1/customers/customers.py">list_resources</a>(id, \*\*<a href="src/stigg/types/v1/customer_list_resources_params.py">params</a>) -> <a href="./src/stigg/types/v1/customer_list_resources_response.py">SyncMyCursorIDPage[CustomerListResourcesResponse]</a></code>
- <code title="post /api/v1/customers">client.v1.customers.<a href="./src/stigg/resources/v1/customers/customers.py">provision</a>(\*\*<a href="src/stigg/types/v1/customer_provision_params.py">params</a>) -> <a href="./src/stigg/types/v1/customer_response.py">CustomerResponse</a></code>
- <code title="post /api/v1/customers/{id}/unarchive">client.v1.customers.<a href="./src/stigg/resources/v1/customers/customers.py">unarchive</a>(id) -> <a href="./src/stigg/types/v1/customer_response.py">CustomerResponse</a></code>

### PaymentMethod

Methods:

- <code title="post /api/v1/customers/{id}/payment-method">client.v1.customers.payment_method.<a href="./src/stigg/resources/v1/customers/payment_method.py">attach</a>(id, \*\*<a href="src/stigg/types/v1/customers/payment_method_attach_params.py">params</a>) -> <a href="./src/stigg/types/v1/customer_response.py">CustomerResponse</a></code>
- <code title="delete /api/v1/customers/{id}/payment-method">client.v1.customers.payment_method.<a href="./src/stigg/resources/v1/customers/payment_method.py">detach</a>(id) -> <a href="./src/stigg/types/v1/customer_response.py">CustomerResponse</a></code>

## Subscriptions

Types:

```python
from stigg.types.v1 import (
    Subscription,
    SubscriptionListResponse,
    SubscriptionImportResponse,
    SubscriptionPreviewResponse,
    SubscriptionProvisionResponse,
)
```

Methods:

- <code title="get /api/v1/subscriptions/{id}">client.v1.subscriptions.<a href="./src/stigg/resources/v1/subscriptions/subscriptions.py">retrieve</a>(id) -> <a href="./src/stigg/types/v1/subscription.py">Subscription</a></code>
- <code title="patch /api/v1/subscriptions/{id}">client.v1.subscriptions.<a href="./src/stigg/resources/v1/subscriptions/subscriptions.py">update</a>(id, \*\*<a href="src/stigg/types/v1/subscription_update_params.py">params</a>) -> <a href="./src/stigg/types/v1/subscription.py">Subscription</a></code>
- <code title="get /api/v1/subscriptions">client.v1.subscriptions.<a href="./src/stigg/resources/v1/subscriptions/subscriptions.py">list</a>(\*\*<a href="src/stigg/types/v1/subscription_list_params.py">params</a>) -> <a href="./src/stigg/types/v1/subscription_list_response.py">SyncMyCursorIDPage[SubscriptionListResponse]</a></code>
- <code title="post /api/v1/subscriptions/{id}/cancel">client.v1.subscriptions.<a href="./src/stigg/resources/v1/subscriptions/subscriptions.py">cancel</a>(id, \*\*<a href="src/stigg/types/v1/subscription_cancel_params.py">params</a>) -> <a href="./src/stigg/types/v1/subscription.py">Subscription</a></code>
- <code title="post /api/v1/subscriptions/{id}/delegate">client.v1.subscriptions.<a href="./src/stigg/resources/v1/subscriptions/subscriptions.py">delegate</a>(id, \*\*<a href="src/stigg/types/v1/subscription_delegate_params.py">params</a>) -> <a href="./src/stigg/types/v1/subscription.py">Subscription</a></code>
- <code title="post /api/v1/subscriptions/import">client.v1.subscriptions.<a href="./src/stigg/resources/v1/subscriptions/subscriptions.py">import\_</a>(\*\*<a href="src/stigg/types/v1/subscription_import_params.py">params</a>) -> <a href="./src/stigg/types/v1/subscription_import_response.py">SubscriptionImportResponse</a></code>
- <code title="post /api/v1/subscriptions/{id}/migrate">client.v1.subscriptions.<a href="./src/stigg/resources/v1/subscriptions/subscriptions.py">migrate</a>(id, \*\*<a href="src/stigg/types/v1/subscription_migrate_params.py">params</a>) -> <a href="./src/stigg/types/v1/subscription.py">Subscription</a></code>
- <code title="post /api/v1/subscriptions/preview">client.v1.subscriptions.<a href="./src/stigg/resources/v1/subscriptions/subscriptions.py">preview</a>(\*\*<a href="src/stigg/types/v1/subscription_preview_params.py">params</a>) -> <a href="./src/stigg/types/v1/subscription_preview_response.py">SubscriptionPreviewResponse</a></code>
- <code title="post /api/v1/subscriptions">client.v1.subscriptions.<a href="./src/stigg/resources/v1/subscriptions/subscriptions.py">provision</a>(\*\*<a href="src/stigg/types/v1/subscription_provision_params.py">params</a>) -> <a href="./src/stigg/types/v1/subscription_provision_response.py">SubscriptionProvisionResponse</a></code>
- <code title="post /api/v1/subscriptions/{id}/transfer">client.v1.subscriptions.<a href="./src/stigg/resources/v1/subscriptions/subscriptions.py">transfer</a>(id, \*\*<a href="src/stigg/types/v1/subscription_transfer_params.py">params</a>) -> <a href="./src/stigg/types/v1/subscription.py">Subscription</a></code>

### FutureUpdate

Types:

```python
from stigg.types.v1.subscriptions import CancelSubscription
```

Methods:

- <code title="delete /api/v1/subscriptions/{id}/future-update/pending-payment">client.v1.subscriptions.future_update.<a href="./src/stigg/resources/v1/subscriptions/future_update.py">cancel_pending_payment</a>(id) -> <a href="./src/stigg/types/v1/subscriptions/cancel_subscription.py">CancelSubscription</a></code>
- <code title="delete /api/v1/subscriptions/{id}/future-update/schedule">client.v1.subscriptions.future_update.<a href="./src/stigg/resources/v1/subscriptions/future_update.py">cancel_schedule</a>(id) -> <a href="./src/stigg/types/v1/subscriptions/cancel_subscription.py">CancelSubscription</a></code>

### Usage

Types:

```python
from stigg.types.v1.subscriptions import UsageChargeUsageResponse, UsageSyncUsageResponse
```

Methods:

- <code title="post /api/v1/subscriptions/{id}/usage/charge">client.v1.subscriptions.usage.<a href="./src/stigg/resources/v1/subscriptions/usage.py">charge_usage</a>(id, \*\*<a href="src/stigg/types/v1/subscriptions/usage_charge_usage_params.py">params</a>) -> <a href="./src/stigg/types/v1/subscriptions/usage_charge_usage_response.py">UsageChargeUsageResponse</a></code>
- <code title="post /api/v1/subscriptions/{id}/usage/sync">client.v1.subscriptions.usage.<a href="./src/stigg/resources/v1/subscriptions/usage.py">sync_usage</a>(id) -> <a href="./src/stigg/types/v1/subscriptions/usage_sync_usage_response.py">UsageSyncUsageResponse</a></code>

### Invoice

Types:

```python
from stigg.types.v1.subscriptions import InvoiceMarkAsPaidResponse
```

Methods:

- <code title="post /api/v1/subscriptions/{id}/invoice/paid">client.v1.subscriptions.invoice.<a href="./src/stigg/resources/v1/subscriptions/invoice.py">mark_as_paid</a>(id) -> <a href="./src/stigg/types/v1/subscriptions/invoice_mark_as_paid_response.py">InvoiceMarkAsPaidResponse</a></code>

## Coupons

Types:

```python
from stigg.types.v1 import Coupon, CouponListResponse
```

Methods:

- <code title="post /api/v1/coupons">client.v1.coupons.<a href="./src/stigg/resources/v1/coupons.py">create</a>(\*\*<a href="src/stigg/types/v1/coupon_create_params.py">params</a>) -> <a href="./src/stigg/types/v1/coupon.py">Coupon</a></code>
- <code title="get /api/v1/coupons/{id}">client.v1.coupons.<a href="./src/stigg/resources/v1/coupons.py">retrieve</a>(id) -> <a href="./src/stigg/types/v1/coupon.py">Coupon</a></code>
- <code title="get /api/v1/coupons">client.v1.coupons.<a href="./src/stigg/resources/v1/coupons.py">list</a>(\*\*<a href="src/stigg/types/v1/coupon_list_params.py">params</a>) -> <a href="./src/stigg/types/v1/coupon_list_response.py">SyncMyCursorIDPage[CouponListResponse]</a></code>
- <code title="post /api/v1/coupons/{id}/archive">client.v1.coupons.<a href="./src/stigg/resources/v1/coupons.py">archive_coupon</a>(id) -> <a href="./src/stigg/types/v1/coupon.py">Coupon</a></code>
- <code title="patch /api/v1/coupons/{id}">client.v1.coupons.<a href="./src/stigg/resources/v1/coupons.py">update_coupon</a>(id, \*\*<a href="src/stigg/types/v1/coupon_update_coupon_params.py">params</a>) -> <a href="./src/stigg/types/v1/coupon.py">Coupon</a></code>

## Events

Types:

```python
from stigg.types.v1 import EventReportResponse
```

Methods:

- <code title="post /api/v1/events">client.v1.events.<a href="./src/stigg/resources/v1/events/events.py">report</a>(\*\*<a href="src/stigg/types/v1/event_report_params.py">params</a>) -> <a href="./src/stigg/types/v1/event_report_response.py">EventReportResponse</a></code>

### Features

Types:

```python
from stigg.types.v1.events import (
    FeatureArchiveFeatureResponse,
    FeatureCreateFeatureResponse,
    FeatureListFeaturesResponse,
    FeatureRetrieveFeatureResponse,
    FeatureUnarchiveFeatureResponse,
    FeatureUpdateFeatureResponse,
)
```

Methods:

- <code title="post /api/v1/features/{id}/archive">client.v1.events.features.<a href="./src/stigg/resources/v1/events/features.py">archive_feature</a>(id) -> <a href="./src/stigg/types/v1/events/feature_archive_feature_response.py">FeatureArchiveFeatureResponse</a></code>
- <code title="post /api/v1/features">client.v1.events.features.<a href="./src/stigg/resources/v1/events/features.py">create_feature</a>(\*\*<a href="src/stigg/types/v1/events/feature_create_feature_params.py">params</a>) -> <a href="./src/stigg/types/v1/events/feature_create_feature_response.py">FeatureCreateFeatureResponse</a></code>
- <code title="get /api/v1/features">client.v1.events.features.<a href="./src/stigg/resources/v1/events/features.py">list_features</a>(\*\*<a href="src/stigg/types/v1/events/feature_list_features_params.py">params</a>) -> <a href="./src/stigg/types/v1/events/feature_list_features_response.py">SyncMyCursorIDPage[FeatureListFeaturesResponse]</a></code>
- <code title="get /api/v1/features/{id}">client.v1.events.features.<a href="./src/stigg/resources/v1/events/features.py">retrieve_feature</a>(id) -> <a href="./src/stigg/types/v1/events/feature_retrieve_feature_response.py">FeatureRetrieveFeatureResponse</a></code>
- <code title="post /api/v1/features/{id}/unarchive">client.v1.events.features.<a href="./src/stigg/resources/v1/events/features.py">unarchive_feature</a>(id) -> <a href="./src/stigg/types/v1/events/feature_unarchive_feature_response.py">FeatureUnarchiveFeatureResponse</a></code>
- <code title="patch /api/v1/features/{id}">client.v1.events.features.<a href="./src/stigg/resources/v1/events/features.py">update_feature</a>(id, \*\*<a href="src/stigg/types/v1/events/feature_update_feature_params.py">params</a>) -> <a href="./src/stigg/types/v1/events/feature_update_feature_response.py">FeatureUpdateFeatureResponse</a></code>

### Addons

Types:

```python
from stigg.types.v1.events import (
    AddonArchiveAddonResponse,
    AddonCreateAddonResponse,
    AddonListAddonsResponse,
    AddonPublishAddonResponse,
    AddonRetrieveAddonResponse,
    AddonUpdateAddonResponse,
)
```

Methods:

- <code title="post /api/v1/addons/{id}/archive">client.v1.events.addons.<a href="./src/stigg/resources/v1/events/addons/addons.py">archive_addon</a>(id) -> <a href="./src/stigg/types/v1/events/addon_archive_addon_response.py">AddonArchiveAddonResponse</a></code>
- <code title="post /api/v1/addons">client.v1.events.addons.<a href="./src/stigg/resources/v1/events/addons/addons.py">create_addon</a>(\*\*<a href="src/stigg/types/v1/events/addon_create_addon_params.py">params</a>) -> <a href="./src/stigg/types/v1/events/addon_create_addon_response.py">AddonCreateAddonResponse</a></code>
- <code title="get /api/v1/addons">client.v1.events.addons.<a href="./src/stigg/resources/v1/events/addons/addons.py">list_addons</a>(\*\*<a href="src/stigg/types/v1/events/addon_list_addons_params.py">params</a>) -> <a href="./src/stigg/types/v1/events/addon_list_addons_response.py">SyncMyCursorIDPage[AddonListAddonsResponse]</a></code>
- <code title="post /api/v1/addons/{id}/publish">client.v1.events.addons.<a href="./src/stigg/resources/v1/events/addons/addons.py">publish_addon</a>(id, \*\*<a href="src/stigg/types/v1/events/addon_publish_addon_params.py">params</a>) -> <a href="./src/stigg/types/v1/events/addon_publish_addon_response.py">AddonPublishAddonResponse</a></code>
- <code title="get /api/v1/addons/{id}">client.v1.events.addons.<a href="./src/stigg/resources/v1/events/addons/addons.py">retrieve_addon</a>(id) -> <a href="./src/stigg/types/v1/events/addon_retrieve_addon_response.py">AddonRetrieveAddonResponse</a></code>
- <code title="patch /api/v1/addons/{id}">client.v1.events.addons.<a href="./src/stigg/resources/v1/events/addons/addons.py">update_addon</a>(id, \*\*<a href="src/stigg/types/v1/events/addon_update_addon_params.py">params</a>) -> <a href="./src/stigg/types/v1/events/addon_update_addon_response.py">AddonUpdateAddonResponse</a></code>

#### Draft

Types:

```python
from stigg.types.v1.events.addons import (
    DraftCreateAddonDraftResponse,
    DraftRemoveAddonDraftResponse,
)
```

Methods:

- <code title="post /api/v1/addons/{id}/draft">client.v1.events.addons.draft.<a href="./src/stigg/resources/v1/events/addons/draft.py">create_addon_draft</a>(id) -> <a href="./src/stigg/types/v1/events/addons/draft_create_addon_draft_response.py">DraftCreateAddonDraftResponse</a></code>
- <code title="delete /api/v1/addons/{id}/draft">client.v1.events.addons.draft.<a href="./src/stigg/resources/v1/events/addons/draft.py">remove_addon_draft</a>(id) -> <a href="./src/stigg/types/v1/events/addons/draft_remove_addon_draft_response.py">DraftRemoveAddonDraftResponse</a></code>

## Usage

Types:

```python
from stigg.types.v1 import UsageHistoryResponse, UsageReportResponse
```

Methods:

- <code title="get /api/v1/usage/{customerId}/history/{featureId}">client.v1.usage.<a href="./src/stigg/resources/v1/usage.py">history</a>(feature_id, \*, customer_id, \*\*<a href="src/stigg/types/v1/usage_history_params.py">params</a>) -> <a href="./src/stigg/types/v1/usage_history_response.py">UsageHistoryResponse</a></code>
- <code title="post /api/v1/usage">client.v1.usage.<a href="./src/stigg/resources/v1/usage.py">report</a>(\*\*<a href="src/stigg/types/v1/usage_report_params.py">params</a>) -> <a href="./src/stigg/types/v1/usage_report_response.py">UsageReportResponse</a></code>

## Products

Types:

```python
from stigg.types.v1 import (
    ProductArchiveProductResponse,
    ProductCreateProductResponse,
    ProductDuplicateProductResponse,
    ProductListProductsResponse,
    ProductUnarchiveProductResponse,
    ProductUpdateProductResponse,
)
```

Methods:

- <code title="post /api/v1/products/{id}/archive">client.v1.products.<a href="./src/stigg/resources/v1/products.py">archive_product</a>(id) -> <a href="./src/stigg/types/v1/product_archive_product_response.py">ProductArchiveProductResponse</a></code>
- <code title="post /api/v1/products">client.v1.products.<a href="./src/stigg/resources/v1/products.py">create_product</a>(\*\*<a href="src/stigg/types/v1/product_create_product_params.py">params</a>) -> <a href="./src/stigg/types/v1/product_create_product_response.py">ProductCreateProductResponse</a></code>
- <code title="post /api/v1/products/{id}/duplicate">client.v1.products.<a href="./src/stigg/resources/v1/products.py">duplicate_product</a>(path_id, \*\*<a href="src/stigg/types/v1/product_duplicate_product_params.py">params</a>) -> <a href="./src/stigg/types/v1/product_duplicate_product_response.py">ProductDuplicateProductResponse</a></code>
- <code title="get /api/v1/products">client.v1.products.<a href="./src/stigg/resources/v1/products.py">list_products</a>(\*\*<a href="src/stigg/types/v1/product_list_products_params.py">params</a>) -> <a href="./src/stigg/types/v1/product_list_products_response.py">SyncMyCursorIDPage[ProductListProductsResponse]</a></code>
- <code title="post /api/v1/products/{id}/unarchive">client.v1.products.<a href="./src/stigg/resources/v1/products.py">unarchive_product</a>(id) -> <a href="./src/stigg/types/v1/product_unarchive_product_response.py">ProductUnarchiveProductResponse</a></code>
- <code title="patch /api/v1/products/{id}">client.v1.products.<a href="./src/stigg/resources/v1/products.py">update_product</a>(id, \*\*<a href="src/stigg/types/v1/product_update_product_params.py">params</a>) -> <a href="./src/stigg/types/v1/product_update_product_response.py">ProductUpdateProductResponse</a></code>
