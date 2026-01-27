# V1

Types:

```python
from stigg.types import V1CreateEventResponse, V1CreateUsageResponse
```

Methods:

- <code title="post /api/v1/events">client.v1.<a href="./src/stigg/resources/v1/v1.py">create_event</a>(\*\*<a href="src/stigg/types/v1_create_event_params.py">params</a>) -> <a href="./src/stigg/types/v1_create_event_response.py">V1CreateEventResponse</a></code>
- <code title="post /api/v1/usage">client.v1.<a href="./src/stigg/resources/v1/v1.py">create_usage</a>(\*\*<a href="src/stigg/types/v1_create_usage_params.py">params</a>) -> <a href="./src/stigg/types/v1_create_usage_response.py">V1CreateUsageResponse</a></code>

## Customers

Types:

```python
from stigg.types.v1 import CustomerResponse, CustomerListResponse
```

Methods:

- <code title="post /api/v1/customers">client.v1.customers.<a href="./src/stigg/resources/v1/customers/customers.py">create</a>(\*\*<a href="src/stigg/types/v1/customer_create_params.py">params</a>) -> <a href="./src/stigg/types/v1/customer_response.py">CustomerResponse</a></code>
- <code title="get /api/v1/customers/{id}">client.v1.customers.<a href="./src/stigg/resources/v1/customers/customers.py">retrieve</a>(id) -> <a href="./src/stigg/types/v1/customer_response.py">CustomerResponse</a></code>
- <code title="patch /api/v1/customers/{id}">client.v1.customers.<a href="./src/stigg/resources/v1/customers/customers.py">update</a>(id, \*\*<a href="src/stigg/types/v1/customer_update_params.py">params</a>) -> <a href="./src/stigg/types/v1/customer_response.py">CustomerResponse</a></code>
- <code title="get /api/v1/customers">client.v1.customers.<a href="./src/stigg/resources/v1/customers/customers.py">list</a>(\*\*<a href="src/stigg/types/v1/customer_list_params.py">params</a>) -> <a href="./src/stigg/types/v1/customer_list_response.py">SyncMyCursorIDPage[CustomerListResponse]</a></code>
- <code title="post /api/v1/customers/{id}/archive">client.v1.customers.<a href="./src/stigg/resources/v1/customers/customers.py">archive</a>(id) -> <a href="./src/stigg/types/v1/customer_response.py">CustomerResponse</a></code>
- <code title="post /api/v1/customers/{id}/unarchive">client.v1.customers.<a href="./src/stigg/resources/v1/customers/customers.py">unarchive</a>(id) -> <a href="./src/stigg/types/v1/customer_response.py">CustomerResponse</a></code>

### PaymentMethod

Methods:

- <code title="post /api/v1/customers/{id}/payment-method">client.v1.customers.payment_method.<a href="./src/stigg/resources/v1/customers/payment_method.py">attach</a>(id, \*\*<a href="src/stigg/types/v1/customers/payment_method_attach_params.py">params</a>) -> <a href="./src/stigg/types/v1/customer_response.py">CustomerResponse</a></code>
- <code title="delete /api/v1/customers/{id}/payment-method">client.v1.customers.payment_method.<a href="./src/stigg/resources/v1/customers/payment_method.py">detach</a>(id) -> <a href="./src/stigg/types/v1/customer_response.py">CustomerResponse</a></code>

### Usage

Types:

```python
from stigg.types.v1.customers import UsageRetrieveResponse
```

Methods:

- <code title="get /api/v1/customers/{customerId}/usage/features/{featureId}">client.v1.customers.usage.<a href="./src/stigg/resources/v1/customers/usage.py">retrieve</a>(feature_id, \*, customer_id, \*\*<a href="src/stigg/types/v1/customers/usage_retrieve_params.py">params</a>) -> <a href="./src/stigg/types/v1/customers/usage_retrieve_response.py">UsageRetrieveResponse</a></code>

## Subscriptions

Types:

```python
from stigg.types.v1 import (
    SubscriptionCreateResponse,
    SubscriptionRetrieveResponse,
    SubscriptionListResponse,
    SubscriptionDelegateResponse,
    SubscriptionMigrateResponse,
    SubscriptionPreviewResponse,
    SubscriptionTransferResponse,
)
```

Methods:

- <code title="post /api/v1/subscriptions">client.v1.subscriptions.<a href="./src/stigg/resources/v1/subscriptions/subscriptions.py">create</a>(\*\*<a href="src/stigg/types/v1/subscription_create_params.py">params</a>) -> <a href="./src/stigg/types/v1/subscription_create_response.py">SubscriptionCreateResponse</a></code>
- <code title="get /api/v1/subscriptions/{id}">client.v1.subscriptions.<a href="./src/stigg/resources/v1/subscriptions/subscriptions.py">retrieve</a>(id) -> <a href="./src/stigg/types/v1/subscription_retrieve_response.py">SubscriptionRetrieveResponse</a></code>
- <code title="get /api/v1/subscriptions">client.v1.subscriptions.<a href="./src/stigg/resources/v1/subscriptions/subscriptions.py">list</a>(\*\*<a href="src/stigg/types/v1/subscription_list_params.py">params</a>) -> <a href="./src/stigg/types/v1/subscription_list_response.py">SyncMyCursorIDPage[SubscriptionListResponse]</a></code>
- <code title="post /api/v1/subscriptions/{id}/delegate">client.v1.subscriptions.<a href="./src/stigg/resources/v1/subscriptions/subscriptions.py">delegate</a>(id, \*\*<a href="src/stigg/types/v1/subscription_delegate_params.py">params</a>) -> <a href="./src/stigg/types/v1/subscription_delegate_response.py">SubscriptionDelegateResponse</a></code>
- <code title="post /api/v1/subscriptions/{id}/migrate">client.v1.subscriptions.<a href="./src/stigg/resources/v1/subscriptions/subscriptions.py">migrate</a>(id, \*\*<a href="src/stigg/types/v1/subscription_migrate_params.py">params</a>) -> <a href="./src/stigg/types/v1/subscription_migrate_response.py">SubscriptionMigrateResponse</a></code>
- <code title="post /api/v1/subscriptions/preview">client.v1.subscriptions.<a href="./src/stigg/resources/v1/subscriptions/subscriptions.py">preview</a>(\*\*<a href="src/stigg/types/v1/subscription_preview_params.py">params</a>) -> <a href="./src/stigg/types/v1/subscription_preview_response.py">SubscriptionPreviewResponse</a></code>
- <code title="post /api/v1/subscriptions/{id}/transfer">client.v1.subscriptions.<a href="./src/stigg/resources/v1/subscriptions/subscriptions.py">transfer</a>(id, \*\*<a href="src/stigg/types/v1/subscription_transfer_params.py">params</a>) -> <a href="./src/stigg/types/v1/subscription_transfer_response.py">SubscriptionTransferResponse</a></code>

### FutureUpdate

Types:

```python
from stigg.types.v1.subscriptions import (
    FutureUpdateCancelPendingPaymentResponse,
    FutureUpdateCancelScheduleResponse,
)
```

Methods:

- <code title="delete /api/v1/subscriptions/{id}/future-update/pending-payment">client.v1.subscriptions.future_update.<a href="./src/stigg/resources/v1/subscriptions/future_update.py">cancel_pending_payment</a>(id) -> <a href="./src/stigg/types/v1/subscriptions/future_update_cancel_pending_payment_response.py">FutureUpdateCancelPendingPaymentResponse</a></code>
- <code title="delete /api/v1/subscriptions/{id}/future-update/schedule">client.v1.subscriptions.future_update.<a href="./src/stigg/resources/v1/subscriptions/future_update.py">cancel_schedule</a>(id) -> <a href="./src/stigg/types/v1/subscriptions/future_update_cancel_schedule_response.py">FutureUpdateCancelScheduleResponse</a></code>

## Coupons

Types:

```python
from stigg.types.v1 import CouponCreateResponse, CouponRetrieveResponse, CouponListResponse
```

Methods:

- <code title="post /api/v1/coupons">client.v1.coupons.<a href="./src/stigg/resources/v1/coupons.py">create</a>(\*\*<a href="src/stigg/types/v1/coupon_create_params.py">params</a>) -> <a href="./src/stigg/types/v1/coupon_create_response.py">CouponCreateResponse</a></code>
- <code title="get /api/v1/coupons/{id}">client.v1.coupons.<a href="./src/stigg/resources/v1/coupons.py">retrieve</a>(id) -> <a href="./src/stigg/types/v1/coupon_retrieve_response.py">CouponRetrieveResponse</a></code>
- <code title="get /api/v1/coupons">client.v1.coupons.<a href="./src/stigg/resources/v1/coupons.py">list</a>(\*\*<a href="src/stigg/types/v1/coupon_list_params.py">params</a>) -> <a href="./src/stigg/types/v1/coupon_list_response.py">SyncMyCursorIDPage[CouponListResponse]</a></code>
