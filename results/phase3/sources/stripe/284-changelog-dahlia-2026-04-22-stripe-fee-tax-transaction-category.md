# Adds the Stripe fee tax transaction category

## What’s new

Adds the `stripe_fee_tax` category to the [category](https://docs.stripe.com/api/v2/money-management/transactions/object.md?api-version=2026-04-22.preview#v2_transaction_object-category) property of [Transaction v2](https://docs.stripe.com/api/v2/transactions/object.md?api-version=2026-04-22.preview) objects and the [transaction_details.category](https://docs.stripe.com/api/v2/money-management/transaction-entries/object.md?api-version=2026-04-22.preview#v2_transaction_entry_object-transaction_details-category) property of [Transaction Entry v2](https://docs.stripe.com/api/v2/money-management/transaction-entries/object.md?api-version=2026-04-22.preview) objects. The `stripe_fee_tax` category represents taxes applied to Stripe fees.

## Impact

You can now identify transactions specifically related to taxes on Stripe fees by checking for the `stripe_fee_tax` value in the `category` property.

If your integration filters or routes transactions by `category`, update your code to handle the new `stripe_fee_tax` value.

## Changes

#### REST API

| Value | Change | Enums |
| --- | --- | --- |
| `stripe_fee_tax` | Added | [V2.MoneyManagement.TransactionEntry.transaction_details](/api/v2/money-management/transaction-entries/object?api-version=2026-04-22.preview#v2_transaction_entry_object-transaction_details-category), [V2.MoneyManagement.Transaction](/api/v2/money-management/transaction-entries/object?api-version=2026-04-22.preview#v2_transaction_entry_object-category) |

#### Ruby

This change doesn’t affect the Ruby SDK.

#### Python

| Value | Change | Enums |
| --- | --- | --- |
| `stripe_fee_tax` | Added | [V2.MoneyManagement.TransactionEntry.TransactionDetail](/api/v2/money-management/transaction-entries/object?api-version=2026-04-22.preview#v2_transaction_entry_object-transaction_details-category), [V2.MoneyManagement.Transaction](/api/v2/money-management/transaction-entries/object?api-version=2026-04-22.preview#v2_transaction_entry_object-category) |

#### PHP

| Value | Change | Enums |
| --- | --- | --- |
| `stripe_fee_tax` | Added | [V2.MoneyManagement.TransactionEntry.transaction_details](/api/v2/money-management/transaction-entries/object?api-version=2026-04-22.preview#v2_transaction_entry_object-transaction_details-category), [V2.MoneyManagement.Transaction](/api/v2/money-management/transaction-entries/object?api-version=2026-04-22.preview#v2_transaction_entry_object-category) |

#### Java

This change doesn’t affect the Java SDK.

#### Node.js

| Value | Change | Enums |
| --- | --- | --- |
| `stripe_fee_tax` | Added | [V2.MoneyManagement.TransactionEntry.transaction_details](/api/v2/money-management/transaction-entries/object?api-version=2026-04-22.preview#v2_transaction_entry_object-transaction_details-category), [V2.MoneyManagement.Transaction](/api/v2/money-management/transaction-entries/object?api-version=2026-04-22.preview#v2_transaction_entry_object-category) |

#### Go

| Value | Change | Enums |
| --- | --- | --- |
| `stripe_fee_tax` | Added | [V2MoneyManagementTransactionEntryTransactionDetails](/api/v2/money-management/transaction-entries/object?api-version=2026-04-22.preview#v2_transaction_entry_object-transaction_details-Category), [V2MoneyManagementTransaction](/api/v2/money-management/transaction-entries/object?api-version=2026-04-22.preview#v2_transaction_entry_object-Category) |

#### .NET

This change doesn’t affect the .NET SDK.

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2026-04-22.preview`
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
