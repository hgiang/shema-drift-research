# Adds new balance transaction types to support minimum balance

## What’s new

This update introduces two new [balance transaction types](https://docs.stripe.com/reports/balance-transaction-types.md#balance_related) to support payout reconciliation for Stripe accounts that limit automatic payouts by setting a minimum balance.

## Impact

The `payout_minimum_balance_hold` transaction type is a negative value representing the amount withheld from a payout to maintain an account’s minimum balance. The `payout_minimum_balance_release` transaction type is a positive value representing the amount added back to the account balance, and always corresponds to the hold value from the same payout. For example, if an account with a minimum balance of 100 USD contains 1000 USD to pay out, a `payout_minimum_balance_hold` of -100 USD is applied to the payout, resulting in a payout of 900 USD. Then, a matching `payout_minimum_balance_release` of 100 USD is added to the account balance.

## Changes

#### REST API

| Values | Change | Enum |
| --- | --- | --- |
| `payout_minimum_balance_hold`, `payout_minimum_balance_release` | Added | [BalanceTransaction.type](/api/balance_transactions/object?api-version=2024-12-18.acacia#balance_transaction_object-type) |

#### Ruby

This change doesn’t affect the Ruby SDK.

#### Python

| Values | Change | Enums |
| --- | --- | --- |
| `payout_minimum_balance_hold` | Added | [stripe.BalanceTransaction.type](/api/balance_transactions/object?api-version=2024-12-18.acacia#balance_transaction_object-type) |
| `payout_minimum_balance_release` | Added | [stripe.BalanceTransaction.type](/api/balance_transactions/object?api-version=2024-12-18.acacia#balance_transaction_object-type) |

#### PHP

| Values | Change | Enum |
| --- | --- | --- |
| `payout_minimum_balance_hold`, `payout_minimum_balance_release` | Added | [BalanceTransaction.type](/api/balance_transactions/object?api-version=2024-12-18.acacia#balance_transaction_object-type) |

#### Java

This change doesn’t affect the Java SDK.

#### Node.js

| Values | Change | Enum |
| --- | --- | --- |
| `payout_minimum_balance_hold`, `payout_minimum_balance_release` | Added | [BalanceTransaction.type](/api/balance_transactions/object?api-version=2024-12-18.acacia#balance_transaction_object-type) |

#### Go

| Values | Change | Enum |
| --- | --- | --- |
| `payout_minimum_balance_hold`, `payout_minimum_balance_release` | Added | [BalanceTransactionType](/api/balance_transactions/object?api-version=2024-12-18.acacia#balance_transaction_object-type) |

#### .NET

This change doesn’t affect the .NET SDK.

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2024-12-18.acacia`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to [v13.3.0](https://github.com/stripe/stripe-ruby/releases/tag/v13.3.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to [v11.4.0](https://github.com/stripe/stripe-python/releases/tag/v11.4.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to [v16.4.0](https://github.com/stripe/stripe-php/releases/tag/v16.4.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to [v28.2.0](https://github.com/stripe/stripe-java/releases/tag/v28.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to [v17.5.0](https://github.com/stripe/stripe-node/releases/tag/v17.5.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to [v81.2.0](https://github.com/stripe/stripe-go/releases/tag/v81.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to [v47.2.0](https://github.com/stripe/stripe-dotnet/releases/tag/v47.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

## Related changes

- [Adds SDK support for trace IDs](https://docs.stripe.com/changelog/acacia/2024-12-18/trace-id-sdk.md)
