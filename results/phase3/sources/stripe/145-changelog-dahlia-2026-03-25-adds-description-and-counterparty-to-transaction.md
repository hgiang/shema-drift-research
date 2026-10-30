# Adds a description and counterparty to transactions

## What’s new

Adds two new optional fields to the [Transaction](https://docs.stripe.com/api/v2/money-management/transactions/object.md?api-version=2026-03-25.preview) resource:

- [description](https://docs.stripe.com/api/v2/money-management/transactions/object.md?api-version=2026-03-25.preview#transaction_object-description): A string describing the transaction. Typically, this will be the `description` associated with the `flow` referenced by the transaction.
- [counterparty](https://docs.stripe.com/api/v2/money-management/transactions/object.md?api-version=2026-03-25.preview#transaction_object-counterparty): An object containing a [name](https://docs.stripe.com/api/v2/money-management/transactions/object.md?api-version=2026-03-25.preview#transaction_object-counterparty-name) property that identifies the other party involved in the transaction. For example, for an Outbound Payment, this would be the name of the recipient.

## Impact

You can now access additional transaction context when working with the Transactions API. The new fields don’t affect existing integrations. No code changes are required unless you want to use the new functionality.

## Changes

#### REST API

| Parameters | Change | Resources or endpoints |
| --- | --- | --- |
| `counterparty`, `description` | Added | [V2.MoneyManagement.Transaction](/api/v2/money-management/transactions/object?api-version=2026-03-25.preview) |

#### Ruby

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `counterparty`, `description` | Added | [V2::MoneyManagement::Transaction](/api/v2/money-management/transactions/object?api-version=2026-03-25.preview) |

#### Python

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `counterparty`, `description` | Added | [V2.MoneyManagement.Transaction](/api/v2/money-management/transactions/object?api-version=2026-03-25.preview) |

#### PHP

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `counterparty`, `description` | Added | [V2.MoneyManagement.Transaction](/api/v2/money-management/transactions/object?api-version=2026-03-25.preview) |

#### Java

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `counterparty`, `description` | Added | [v2.moneymanagement.Transaction](/api/v2/money-management/transactions/object?api-version=2026-03-25.preview) |

#### Node.js

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `counterparty`, `description` | Added | [V2.MoneyManagement.Transaction](/api/v2/money-management/transactions/object?api-version=2026-03-25.preview) |

#### Go

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `Counterparty`, `Description` | Added | [V2MoneyManagementTransaction](/api/v2/money-management/transactions/object?api-version=2026-03-25.preview) |

#### .NET

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `Counterparty`, `Description` | Added | [V2.MoneyManagement.Transaction](/api/v2/money-management/transactions/object?api-version=2026-03-25.preview) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2026-03-25.preview`
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
