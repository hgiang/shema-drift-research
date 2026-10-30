# Adds the originating account holder name to Received Credit bank transfers

## What’s new

Adds the [account_holder_name](https://docs.stripe.com/api/v2/money-management/received-credits/object.md?api-version=2026-06-24.preview#v2_received_credit_object-bank_transfer-us_bank_account-account_holder_name) property to the [us_bank_account](https://docs.stripe.com/api/v2/money-management/received-credits/object.md?api-version=2026-06-24.preview#v2_received_credit_object-bank_transfer-us_bank_account) hash of the [Received Credit](https://docs.stripe.com/api/v2/money-management/received-credits/object.md?api-version=2026-06-24.preview) object. When a credit is received through a US bank transfer, this property returns the name of the account holder at the originating bank, if available.

## Impact

You can now read the `account_holder_name` property on a Received Credit to identify the sender of an inbound US bank transfer so you can track where the funds came from.

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `account_holder_name` | Added | [V2.MoneyManagement.ReceivedCredit.bank_transfer.us_bank_account](/api/v2/money-management/received-credits/object?api-version=2026-06-24.preview#v2_received_credit_object-bank_transfer-us_bank_account) |

#### Ruby

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `account_holder_name` | Added | [V2::MoneyManagement::ReceivedCredit::BankTransfer::UsBankAccount](/api/v2/money-management/received-credits/object?api-version=2026-06-24.preview#v2_received_credit_object-bank_transfer-us_bank_account) |

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `account_holder_name` | Added | [V2.MoneyManagement.ReceivedCredit.BankTransfer.UsBankAccount](/api/v2/money-management/received-credits/object?api-version=2026-06-24.preview#v2_received_credit_object-bank_transfer-us_bank_account) |

#### PHP

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `account_holder_name` | Added | [V2.MoneyManagement.ReceivedCredit.bank_transfer.us_bank_account](/api/v2/money-management/received-credits/object?api-version=2026-06-24.preview#v2_received_credit_object-bank_transfer-us_bank_account) |

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `accountHolderName` | Added | [v2.moneymanagement.ReceivedCredit.bank_transfer.us_bank_account](/api/v2/money-management/received-credits/object?api-version=2026-06-24.preview#v2_received_credit_object-bank_transfer-us_bank_account) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `account_holder_name` | Added | [V2.MoneyManagement.ReceivedCredit.bank_transfer.us_bank_account](/api/v2/money-management/received-credits/object?api-version=2026-06-24.preview#v2_received_credit_object-bank_transfer-us_bank_account) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `AccountHolderName` | Added | [V2MoneyManagementReceivedCreditBankTransferUsBankAccount](/api/v2/money-management/received-credits/object?api-version=2026-06-24.preview#v2_received_credit_object-bank_transfer-us_bank_account) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `AccountHolderName` | Added | [V2.MoneyManagement.ReceivedCredit.BankTransfer.UsBankAccount](/api/v2/money-management/received-credits/object?api-version=2026-06-24.preview#v2_received_credit_object-bank_transfer-us_bank_account) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2026-06-24.preview`
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

## Related changes

- [Replaces SWIFT code with BIC in Financial Addresses](https://docs.stripe.com/changelog/dahlia/2026-06-24/financial-addresses-replace-swift-with-bic.md)
- [Adds a failure reason for received debits when the debit capability is inactive](https://docs.stripe.com/changelog/dahlia/2026-06-24/received-debits-failure-reason-enum-capability-inactive.md)
- [Replaces the status filter with statuses on the List Financial Accounts endpoint](https://docs.stripe.com/changelog/dahlia/2026-06-24/v2-financial-accounts-statuses-filter.md)
