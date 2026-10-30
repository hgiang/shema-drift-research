# Deprecates legacy payout type for balance transfers in the ReceivedCredit API

## What’s new

The [balance_transfer](https://docs.stripe.com/api/v2/money-management/received-credits/object.md?api-version=2026-07-29.preview#v2_received_credit_object-balance_transfer) hash on the [ReceivedCredit](https://docs.stripe.com/api/v2/money-management/received-credits/object.md?api-version=2026-07-29.preview) object now uses `payout` as the type value for payout-initiated balance transfers. This change adds the `payout` enum value to [balance_transfer.type](https://docs.stripe.com/api/v2/money-management/received-credits/object.md?api-version=2026-07-29.preview#v2_received_credit_object-balance_transfer-type) and a corresponding [payout](https://docs.stripe.com/api/v2/money-management/received-credits/object.md?api-version=2026-07-29.preview#v2_received_credit_object-balance_transfer-payout) property to the `balance_transfer` hash. The legacy `payout_v1` property and enum value are deprecated.

## Impact

If you previously read `balance_transfer.type` as `payout_v1`, update your code to use `payout` instead. Integrations on earlier API versions aren’t affected.

## Changes

#### REST API

| Parameters | Change | Resources or endpoints |
| --- | --- | --- |
| `payout` | Added | [V2.MoneyManagement.ReceivedCredit.balance_transfer](/api/v2/money-management/received-credits/object?api-version=2026-07-29.preview#v2_received_credit_object-balance_transfer) |
| `payout_v1` | Removed | [V2.MoneyManagement.ReceivedCredit.balance_transfer](/api/v2/money-management/received-credits/object?api-version=2026-07-29.preview#v2_received_credit_object-balance_transfer) |

| Value | Change | Enum |
| --- | --- | --- |
| `payout` | Added | [V2.MoneyManagement.ReceivedCredit.balance_transfer.type](/api/v2/money-management/received-credits/object?api-version=2026-07-29.preview#v2_received_credit_object-balance_transfer-type) |

#### Ruby

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `payout` | Added | [V2::MoneyManagement::ReceivedCredit::BalanceTransfer](/api/v2/money-management/received-credits/object?api-version=2026-07-29.preview#v2_received_credit_object-balance_transfer) |
| `payout_v1` | Removed | [V2::MoneyManagement::ReceivedCredit::BalanceTransfer](/api/v2/money-management/received-credits/object?api-version=2026-07-29.preview#v2_received_credit_object-balance_transfer) |

#### Python

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `payout` | Added | [V2.MoneyManagement.ReceivedCredit.BalanceTransfer](/api/v2/money-management/received-credits/object?api-version=2026-07-29.preview#v2_received_credit_object-balance_transfer) |
| `payout_v1` | Removed | [V2.MoneyManagement.ReceivedCredit.BalanceTransfer](/api/v2/money-management/received-credits/object?api-version=2026-07-29.preview#v2_received_credit_object-balance_transfer) |

| Value | Change | Enum |
| --- | --- | --- |
| `payout` | Added | [V2.MoneyManagement.ReceivedCredit.BalanceTransfer.type](/api/v2/money-management/received-credits/object?api-version=2026-07-29.preview#v2_received_credit_object-balance_transfer-type) |

#### PHP

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `payout` | Added | [V2.MoneyManagement.ReceivedCredit.balance_transfer](/api/v2/money-management/received-credits/object?api-version=2026-07-29.preview#v2_received_credit_object-balance_transfer) |
| `payout_v1` | Removed | [V2.MoneyManagement.ReceivedCredit.balance_transfer](/api/v2/money-management/received-credits/object?api-version=2026-07-29.preview#v2_received_credit_object-balance_transfer) |

| Value | Change | Enum |
| --- | --- | --- |
| `payout` | Added | [V2.MoneyManagement.ReceivedCredit.balance_transfer.type](/api/v2/money-management/received-credits/object?api-version=2026-07-29.preview#v2_received_credit_object-balance_transfer-type) |

#### Java

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `payout` | Added | [v2.moneymanagement.ReceivedCredit.balance_transfer](/api/v2/money-management/received-credits/object?api-version=2026-07-29.preview#v2_received_credit_object-balance_transfer) |
| `payoutV1` | Removed | [v2.moneymanagement.ReceivedCredit.balance_transfer](/api/v2/money-management/received-credits/object?api-version=2026-07-29.preview#v2_received_credit_object-balance_transfer) |

#### Node.js

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `payout` | Added | [V2.MoneyManagement.ReceivedCredit.balance_transfer](/api/v2/money-management/received-credits/object?api-version=2026-07-29.preview#v2_received_credit_object-balance_transfer) |
| `payout_v1` | Removed | [V2.MoneyManagement.ReceivedCredit.balance_transfer](/api/v2/money-management/received-credits/object?api-version=2026-07-29.preview#v2_received_credit_object-balance_transfer) |

| Value | Change | Enum |
| --- | --- | --- |
| `payout` | Added | [V2.MoneyManagement.ReceivedCredit.balance_transfer.type](/api/v2/money-management/received-credits/object?api-version=2026-07-29.preview#v2_received_credit_object-balance_transfer-type) |

#### Go

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `Payout` | Added | [V2MoneyManagementReceivedCreditBalanceTransfer](/api/v2/money-management/received-credits/object?api-version=2026-07-29.preview#v2_received_credit_object-balance_transfer) |
| `PayoutV1` | Removed | [V2MoneyManagementReceivedCreditBalanceTransfer](/api/v2/money-management/received-credits/object?api-version=2026-07-29.preview#v2_received_credit_object-balance_transfer) |

| Value | Change | Enum |
| --- | --- | --- |
| `payout` | Added | [V2MoneyManagementReceivedCreditBalanceTransfer.Type](/api/v2/money-management/received-credits/object?api-version=2026-07-29.preview#v2_received_credit_object-balance_transfer-Type) |

#### .NET

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `Payout` | Added | [V2.MoneyManagement.ReceivedCredit.BalanceTransfer](/api/v2/money-management/received-credits/object?api-version=2026-07-29.preview#v2_received_credit_object-balance_transfer) |
| `PayoutV1` | Removed | [V2.MoneyManagement.ReceivedCredit.BalanceTransfer](/api/v2/money-management/received-credits/object?api-version=2026-07-29.preview#v2_received_credit_object-balance_transfer) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2026-07-29.preview`
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
