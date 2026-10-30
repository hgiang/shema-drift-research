# Adds filtering by creation date to Customer Balance Transactions lists

## What’s new

You can now filter [Customer Balance Transactions](https://docs.stripe.com/api/customer_balance_transactions.md?api-version=2025-11-17.clover) by their creation date using the new [created](https://docs.stripe.com/api/customer_balance_transactions/list.md?api-version=2025-11-17.clover#list_customer_balance_transactions-created) parameter when you [list transactions](https://docs.stripe.com/api/customer_balance_transactions/list.md?api-version=2025-11-17.clover).

The parameter supports date range queries using the following operators to specify a date interval: [gt](https://docs.stripe.com/api/customer_balance_transactions/list.md?api-version=2025-11-17.clover&lang=curl#list_customer_balance_transactions-created-gt) (greater than), [gte](https://docs.stripe.com/api/customer_balance_transactions/list.md?api-version=2025-11-17.clover&lang=curl#list_customer_balance_transactions-created-gte) (greater than or equal to), [lt](https://docs.stripe.com/api/customer_balance_transactions/list.md?api-version=2025-11-17.clover&lang=curl#list_customer_balance_transactions-created-lt) (less than), and [lte](https://docs.stripe.com/api/customer_balance_transactions/list.md?api-version=2025-11-17.clover&lang=curl#list_customer_balance_transactions-created-lte) (less than or equal to).

## Impact

You can now filter customer balance transactions by their creation date when calling the list endpoint. This provides more granular control over which transactions you retrieve, allowing you to:

- Retrieve invoice payments created on a specific date by passing a timestamp to the `created` parameter. For example, specifying `?created=1609459200` filters for transactions created at that exact timestamp.
- Retrieve invoice payments created before or after a certain date using comparison operators. For example, specifying `created[gte]=1609459200` filters for transactions created after 1 January 2021.
- Retrieve invoice payments within a date range by combining operators. For example, specifying `created[gte]=1609459200&created[lt]=1612137600` filters for transactions created in January 2021.

These new filter operators reduce the need to retrieve all transactions and then filter them client-side, improving performance and reducing data transfer volume for date-specific queries.

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `created` | Added | [Customer#balance_transactions](/api/customer_balance_transactions/list?api-version=2025-11-17.clover) |

#### Ruby

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `created` | Added | [CustomerCustomerBalanceTransactionListParams](/api/customer_balance_transactions/list?api-version=2025-11-17.clover) |

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `created` | Added | [CustomerListCustomerBalanceTransactionParams](/api/customer_balance_transactions/list?api-version=2025-11-17.clover) |

#### PHP

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `created` | Added | [CustomerBalanceTransaction.all().$params](/api/customer_balance_transactions/list?api-version=2025-11-17.clover) |

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `created` | Added | [CustomerBalanceTransactionListParams](/api/customer_balance_transactions/list?api-version=2025-11-17.clover) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `created` | Added | [CustomerListCustomerBalanceTransactionsParams](/api/customer_balance_transactions/list?api-version=2025-11-17.clover) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `Created` | Added | [CustomerCustomerBalanceTransactionListParams](/api/customer_balance_transactions/list?api-version=2025-11-17.clover) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `Created` | Added | [CustomerCustomerBalanceTransactionListOptions](/api/customer_balance_transactions/list?api-version=2025-11-17.clover) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2025-11-17.clover`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to [v17.2.0](https://github.com/stripe/stripe-ruby/releases/tag/v17.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to [v13.2.0](https://github.com/stripe/stripe-python/releases/tag/v13.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to [v18.2.0](https://github.com/stripe/stripe-php/releases/tag/v18.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to [v30.2.0](https://github.com/stripe/stripe-java/releases/tag/v30.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to [v19.3.0](https://github.com/stripe/stripe-node/releases/tag/v19.3.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to [v83.2.0](https://github.com/stripe/stripe-go/releases/tag/v83.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to [v49.2.0](https://github.com/stripe/stripe-dotnet/releases/tag/v49.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

## Related changes

- [Adds filtering by creation date to Invoice Payment lists](https://docs.stripe.com/changelog/clover/2025-11-17/invoice-payments-list-created.md)
- [Adds the ability to specify a payment method configuration in the customer portal](https://docs.stripe.com/changelog/clover/2025-11-17/portal-payment-method-configuration.md)
