# V1

## Customers

Types:

```python
from stigg.types.v1 import CustomerResponse, CustomerListResponse
```

Methods:

- <code title="post /api/v1/customers">client.v1.customers.<a href="./src/stigg/resources/v1/customers/customers.py">create</a>(\*\*<a href="src/stigg/types/v1/customer_create_params.py">params</a>) -> <a href="./src/stigg/types/v1/customer_response.py">CustomerResponse</a></code>
- <code title="get /api/v1/customers/{id}">client.v1.customers.<a href="./src/stigg/resources/v1/customers/customers.py">retrieve</a>(id) -> <a href="./src/stigg/types/v1/customer_response.py">CustomerResponse</a></code>
- <code title="patch /api/v1/customers/{id}">client.v1.customers.<a href="./src/stigg/resources/v1/customers/customers.py">update</a>(id, \*\*<a href="src/stigg/types/v1/customer_update_params.py">params</a>) -> <a href="./src/stigg/types/v1/customer_response.py">CustomerResponse</a></code>
- <code title="get /api/v1/customers">client.v1.customers.<a href="./src/stigg/resources/v1/customers/customers.py">list</a>(\*\*<a href="src/stigg/types/v1/customer_list_params.py">params</a>) -> <a href="./src/stigg/types/v1/customer_list_response.py">CustomerListResponse</a></code>
- <code title="post /api/v1/customers/{id}/archive">client.v1.customers.<a href="./src/stigg/resources/v1/customers/customers.py">archive</a>(id) -> <a href="./src/stigg/types/v1/customer_response.py">CustomerResponse</a></code>
- <code title="post /api/v1/customers/{id}/unarchive">client.v1.customers.<a href="./src/stigg/resources/v1/customers/customers.py">unarchive</a>(id) -> <a href="./src/stigg/types/v1/customer_response.py">CustomerResponse</a></code>

### PaymentMethod

Methods:

- <code title="post /api/v1/customers/{id}/payment-method">client.v1.customers.payment_method.<a href="./src/stigg/resources/v1/customers/payment_method.py">attach</a>(id, \*\*<a href="src/stigg/types/v1/customers/payment_method_attach_params.py">params</a>) -> <a href="./src/stigg/types/v1/customer_response.py">CustomerResponse</a></code>
- <code title="delete /api/v1/customers/{id}/payment-method">client.v1.customers.payment_method.<a href="./src/stigg/resources/v1/customers/payment_method.py">detach</a>(id) -> <a href="./src/stigg/types/v1/customer_response.py">CustomerResponse</a></code>
