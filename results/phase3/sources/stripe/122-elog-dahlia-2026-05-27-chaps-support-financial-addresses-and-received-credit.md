# Adds CHAPS support to Financial Addresses and Received Credits

## What’s new

Stripe now supports CHAPS payments for UK bank accounts in both [Financial Addresses](https://docs.stripe.com/api/v2/money-management/financial-addresses.md?api-version=2026-05-27.preview) and [Received Credits](https://docs.stripe.com/api/v2/money-management/received-credits.md?api-version=2026-05-27.preview).

You can now specify `chaps` as a [network](https://docs.stripe.com/api/v2/money-management/financial-addresses/credit.md?api-version=2026-05-27.preview#v2_credit_financial_addresses-network) value when creating Financial Addresses with GB bank account credentials. The [network](https://docs.stripe.com/api/v2/money-management/received-credits/retrieve.md?api-version=2026-05-27.preview#v2_retrieve_received_credits-response-bank_transfer-gb_bank_account-network) property on Received Credit bank transfers also accepts `chaps` alongside the existing `fps` value.

## Impact

You can now configure your Financial Addresses to accept CHAPS transactions to receive payments through both major UK payment networks. This allows customers to send larger value payments or payments outside standard FPS operating hours. This change builds on existing FPS support to provide coverage of UK domestic payment rails.

If you process UK bank transfers, update your integration to handle the new `chaps` network value in webhook events and API responses for Received Credits. Existing FPS functionality remains unchanged.

## Changes

#### REST API

| Value | Change | Enum |
| --- | --- | --- |
| `chaps` | Added | [V2.FinancialAddressCreditSimulation#credit.network](/api/v2/money-management/financial-addresses/credit?api-version=2026-05-27.preview#v2_credit_financial_addresses-network) |

| Field | Change | From → to |
| --- | --- | --- |
| `V2.MoneyManagement.ReceivedCredit.bank_transfer.gb_bank_account.network` | Changed | `literal('fps') → enum('chaps'|'fps')` |

#### Ruby

| Field | Change | From → to |
| --- | --- | --- |
| `V2::MoneyManagement::ReceivedCredit::BankTransfer::GbBankAccount.network` | Changed | `literal('fps') → enum('chaps'|'fps')` |

#### Python

| Value | Change | Enum |
| --- | --- | --- |
| `chaps` | Added | [v2.FinancialAddressCreditSimulationCreditParams.network](/api/v2/money-management/financial-addresses/credit?api-version=2026-05-27.preview#v2_credit_financial_addresses-network) |

| Field | Change | From → to |
| --- | --- | --- |
| `V2.MoneyManagement.ReceivedCredit.BankTransfer.GbBankAccount.network` | Changed | `literal('fps') → enum('chaps'|'fps')` |

#### PHP

| Field | Change | From → to |
| --- | --- | --- |
| `V2.MoneyManagement.ReceivedCredit.bank_transfer.gb_bank_account.network` | Changed | `literal('fps') → enum('chaps'|'fps')` |

#### Java

| Value | Change | Enum |
| --- | --- | --- |
| `chaps` | Added | [v2.FinancialAddressCreditSimulationCreditParams.network](/api/v2/money-management/financial-addresses/credit?api-version=2026-05-27.preview#v2_credit_financial_addresses-network) |

| Field | Change | From → to |
| --- | --- | --- |
| `v2.moneymanagement.ReceivedCredit.bank_transfer.gb_bank_account.network` | Changed | `literal('fps') → enum('chaps'|'fps')` |

#### Node.js

| Value | Change | Enum |
| --- | --- | --- |
| `chaps` | Added | [V2.FinancialAddressCreditSimulationCreditParams.network](/api/v2/money-management/financial-addresses/credit?api-version=2026-05-27.preview#v2_credit_financial_addresses-network) |

| Field | Change | From → to |
| --- | --- | --- |
| `V2.MoneyManagement.ReceivedCredit.bank_transfer.gb_bank_account.network` | Changed | `literal('fps') → enum('chaps'|'fps')` |

#### Go

| Field | Change | From → to |
| --- | --- | --- |
| `V2MoneyManagementReceivedCreditBankTransferGbBankAccount.Network` | Changed | `literal('fps') → enum('chaps'|'fps')` |

#### .NET

| Field | Change | From → to |
| --- | --- | --- |
| `V2.MoneyManagement.ReceivedCredit.BankTransfer.GbBankAccount.Network` | Changed | `literal('fps') → enum('chaps'|'fps')` |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2026-05-27.preview`
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
