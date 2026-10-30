# Adds Balance Transaction types for provisional credits for Issuing disputes

## What’s new

Adds two values to the [type](https://docs.stripe.com/api/balance_transactions/object.md?api-version=2026-09-30.endive#balance_transaction_object-type) property of [Balance Transactions](https://docs.stripe.com/api/balance_transactions/object.md?api-version=2026-09-30.endive) to represent money movement related to [provisional credits for Issuing disputes](https://docs.stripe.com/issuing/purchases/disputes/provisional-credits.md):

- `issuing_dispute_provisional_credit` represents a temporary credit granted to the Issuing balance when a dispute is submitted.
- `issuing_dispute_provisional_credit_reversal` represents the reversal of that provisional credit at dispute resolution.

Both values are available as filters when you [list Balance Transactions](https://docs.stripe.com/api/balance_transactions/list.md?api-version=2026-09-30.endive#balance_transaction_list-type). Each type has a corresponding [reporting_category](https://docs.stripe.com/api/balance_transactions/object.md?api-version=2026-09-30.endive#balance_transaction_object-reporting_category) for differentiation in Balance Reports. The existing `issuing_dispute` type continues to represent the final credit for a won dispute.

## Impact

If your integration filters or processes Balance Transactions by `type`, you may encounter the `issuing_dispute_provisional_credit` and `issuing_dispute_provisional_credit_reversal` values in API responses. These values also appear in SDK type definitions and OpenAPI specs. To adapt your integration:

- Update any code that depends on `type` to handle the two additional values, especially if your code raises errors on unrecognised types.
- If applicable, adjust reconciliation workflows to use these new types to distinguish provisional credit movements from final dispute credits.
- Review [Balance reports](https://docs.stripe.com/reports/balance.md) that rely on reporting categories, because each type has its own corresponding `reporting_category`.

## Changes

#### REST API

| Values | Change | Enum |
| --- | --- | --- |
| `issuing_dispute_provisional_credit`, `issuing_dispute_provisional_credit_reversal` | Added | [BalanceTransaction.type](/api/balance_transactions/object?api-version=2026-09-30.endive#balance_transaction_object-type) |

#### Ruby

This change doesn’t affect the Ruby SDK.

#### Python

| Values | Change | Enum |
| --- | --- | --- |
| `issuing_dispute_provisional_credit`, `issuing_dispute_provisional_credit_reversal` | Added | [BalanceTransaction.type](/api/balance_transactions/object?api-version=2026-09-30.endive#balance_transaction_object-type) |

#### PHP

| Values | Change | Enum |
| --- | --- | --- |
| `issuing_dispute_provisional_credit`, `issuing_dispute_provisional_credit_reversal` | Added | [BalanceTransaction.type](/api/balance_transactions/object?api-version=2026-09-30.endive#balance_transaction_object-type) |

#### Java

This change doesn’t affect the Java SDK.

#### Node.js

| Values | Change | Enum |
| --- | --- | --- |
| `issuing_dispute_provisional_credit`, `issuing_dispute_provisional_credit_reversal` | Added | [BalanceTransaction.type](/api/balance_transactions/object?api-version=2026-09-30.endive#balance_transaction_object-type) |

#### Go

| Values | Change | Enum |
| --- | --- | --- |
| `issuing_dispute_provisional_credit`, `issuing_dispute_provisional_credit_reversal` | Added | [BalanceTransaction.Type](/api/balance_transactions/object?api-version=2026-09-30.endive#balance_transaction_object-Type) |

#### .NET

This change doesn’t affect the .NET SDK.

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2026-09-30.endive`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to the latest version.
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to the latest version.
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to the latest version.
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to the latest version.
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to the latest version.
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to the latest version.
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to the latest version.
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).
