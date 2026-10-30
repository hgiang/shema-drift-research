# Adds additional beneficiary information for bank transfer payments

## What’s new

Adds additional information about the beneficiary (receiver) for customers making bank transfer payments.

## Impact

Stripe provides funding instructions for customers making [bank transfer payments](https://docs.stripe.com/payments/bank-transfers.md) to merchants using a Stripe-provided bank account, including details such as the destination account number and bank code. Some banks (and bank transfer interfaces) also ask customers to provide additional information about the receiver, such as their name, address, and the address of the bank. For convenience, Stripe now includes this information in the funding instructions presented for each bank transfer payment.

## Changes

#### REST API

| Parameters | Change | Resources or endpoints |
| --- | --- | --- |
| `account_holder_address`, `bank_address` | Added | [FundingInstructions.bank_transfer.financial_addresses[].iban](/api/issuing/funding_instructions/object?api-version=2024-12-18.acacia#issuing_funding_instructions_object-bank_transfer-financial_addresses-iban), [FundingInstructions.bank_transfer.financial_addresses[].sort_code](/api/issuing/funding_instructions/object?api-version=2024-12-18.acacia#issuing_funding_instructions_object-bank_transfer-financial_addresses-sort_code), `FundingInstructions.bank_transfer.financial_addresses[].spei`, `FundingInstructions.bank_transfer.financial_addresses[].zengin`, [PaymentIntent.next_action.display_bank_transfer_instructions.financial_addresses[].iban](/api/payment_intents/object?api-version=2024-12-18.acacia#payment_intent_object-next_action-display_bank_transfer_instructions-financial_addresses-iban), [PaymentIntent.next_action.display_bank_transfer_instructions.financial_addresses[].sort_code](/api/payment_intents/object?api-version=2024-12-18.acacia#payment_intent_object-next_action-display_bank_transfer_instructions-financial_addresses-sort_code), [PaymentIntent.next_action.display_bank_transfer_instructions.financial_addresses[].spei](/api/payment_intents/object?api-version=2024-12-18.acacia#payment_intent_object-next_action-display_bank_transfer_instructions-financial_addresses-spei), [PaymentIntent.next_action.display_bank_transfer_instructions.financial_addresses[].zengin](/api/payment_intents/object?api-version=2024-12-18.acacia#payment_intent_object-next_action-display_bank_transfer_instructions-financial_addresses-zengin) |

#### Ruby

This change doesn’t affect the Ruby SDK.

#### Python

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `account_holder_address` | Added | [stripe.FundingInstructions.BankTransfer.FinancialAddress.Iban](/api/issuing/funding_instructions/object?api-version=2024-12-18.acacia#issuing_funding_instructions_object-bank_transfer-financial_addresses-iban), [stripe.FundingInstructions.BankTransfer.FinancialAddress.SortCode](/api/issuing/funding_instructions/object?api-version=2024-12-18.acacia#issuing_funding_instructions_object-bank_transfer-financial_addresses-sort_code), `stripe.FundingInstructions.BankTransfer.FinancialAddress.Spei`, `stripe.FundingInstructions.BankTransfer.FinancialAddress.Zengin`, [stripe.PaymentIntent.NextAction.DisplayBankTransferInstructions.FinancialAddress.Iban](/api/payment_intents/object?api-version=2024-12-18.acacia#payment_intent_object-next_action-display_bank_transfer_instructions-financial_addresses-iban), [stripe.PaymentIntent.NextAction.DisplayBankTransferInstructions.FinancialAddress.SortCode](/api/payment_intents/object?api-version=2024-12-18.acacia#payment_intent_object-next_action-display_bank_transfer_instructions-financial_addresses-sort_code), [stripe.PaymentIntent.NextAction.DisplayBankTransferInstructions.FinancialAddress.Spei](/api/payment_intents/object?api-version=2024-12-18.acacia#payment_intent_object-next_action-display_bank_transfer_instructions-financial_addresses-spei), [stripe.PaymentIntent.NextAction.DisplayBankTransferInstructions.FinancialAddress.Zengin](/api/payment_intents/object?api-version=2024-12-18.acacia#payment_intent_object-next_action-display_bank_transfer_instructions-financial_addresses-zengin) |
| `bank_address` | Added | [stripe.FundingInstructions.BankTransfer.FinancialAddress.Iban](/api/issuing/funding_instructions/object?api-version=2024-12-18.acacia#issuing_funding_instructions_object-bank_transfer-financial_addresses-iban), [stripe.FundingInstructions.BankTransfer.FinancialAddress.SortCode](/api/issuing/funding_instructions/object?api-version=2024-12-18.acacia#issuing_funding_instructions_object-bank_transfer-financial_addresses-sort_code), `stripe.FundingInstructions.BankTransfer.FinancialAddress.Spei`, `stripe.FundingInstructions.BankTransfer.FinancialAddress.Zengin`, [stripe.PaymentIntent.NextAction.DisplayBankTransferInstructions.FinancialAddress.Iban](/api/payment_intents/object?api-version=2024-12-18.acacia#payment_intent_object-next_action-display_bank_transfer_instructions-financial_addresses-iban), [stripe.PaymentIntent.NextAction.DisplayBankTransferInstructions.FinancialAddress.SortCode](/api/payment_intents/object?api-version=2024-12-18.acacia#payment_intent_object-next_action-display_bank_transfer_instructions-financial_addresses-sort_code), [stripe.PaymentIntent.NextAction.DisplayBankTransferInstructions.FinancialAddress.Spei](/api/payment_intents/object?api-version=2024-12-18.acacia#payment_intent_object-next_action-display_bank_transfer_instructions-financial_addresses-spei), [stripe.PaymentIntent.NextAction.DisplayBankTransferInstructions.FinancialAddress.Zengin](/api/payment_intents/object?api-version=2024-12-18.acacia#payment_intent_object-next_action-display_bank_transfer_instructions-financial_addresses-zengin) |

#### PHP

This change doesn’t affect the PHP SDK.

#### Java

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `account_holder_address`, `bank_address` | Added | [FundingInstructions.bank_transfer.financial_addresses[].iban](/api/issuing/funding_instructions/object?api-version=2024-12-18.acacia#issuing_funding_instructions_object-bank_transfer-financial_addresses-iban), [FundingInstructions.bank_transfer.financial_addresses[].sort_code](/api/issuing/funding_instructions/object?api-version=2024-12-18.acacia#issuing_funding_instructions_object-bank_transfer-financial_addresses-sort_code), `FundingInstructions.bank_transfer.financial_addresses[].spei`, `FundingInstructions.bank_transfer.financial_addresses[].zengin`, [PaymentIntent.next_action.display_bank_transfer_instructions.financial_addresses[].iban](/api/payment_intents/object?api-version=2024-12-18.acacia#payment_intent_object-next_action-display_bank_transfer_instructions-financial_addresses-iban), [PaymentIntent.next_action.display_bank_transfer_instructions.financial_addresses[].sort_code](/api/payment_intents/object?api-version=2024-12-18.acacia#payment_intent_object-next_action-display_bank_transfer_instructions-financial_addresses-sort_code), [PaymentIntent.next_action.display_bank_transfer_instructions.financial_addresses[].spei](/api/payment_intents/object?api-version=2024-12-18.acacia#payment_intent_object-next_action-display_bank_transfer_instructions-financial_addresses-spei), [PaymentIntent.next_action.display_bank_transfer_instructions.financial_addresses[].zengin](/api/payment_intents/object?api-version=2024-12-18.acacia#payment_intent_object-next_action-display_bank_transfer_instructions-financial_addresses-zengin) |

#### Node.js

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `account_holder_address`, `bank_address` | Added | [FundingInstructions.bank_transfer.financial_addresses[].iban](/api/issuing/funding_instructions/object?api-version=2024-12-18.acacia#issuing_funding_instructions_object-bank_transfer-financial_addresses-iban), [FundingInstructions.bank_transfer.financial_addresses[].sort_code](/api/issuing/funding_instructions/object?api-version=2024-12-18.acacia#issuing_funding_instructions_object-bank_transfer-financial_addresses-sort_code), `FundingInstructions.bank_transfer.financial_addresses[].spei`, `FundingInstructions.bank_transfer.financial_addresses[].zengin`, [PaymentIntent.next_action.display_bank_transfer_instructions.financial_addresses[].iban](/api/payment_intents/object?api-version=2024-12-18.acacia#payment_intent_object-next_action-display_bank_transfer_instructions-financial_addresses-iban), [PaymentIntent.next_action.display_bank_transfer_instructions.financial_addresses[].sort_code](/api/payment_intents/object?api-version=2024-12-18.acacia#payment_intent_object-next_action-display_bank_transfer_instructions-financial_addresses-sort_code), [PaymentIntent.next_action.display_bank_transfer_instructions.financial_addresses[].spei](/api/payment_intents/object?api-version=2024-12-18.acacia#payment_intent_object-next_action-display_bank_transfer_instructions-financial_addresses-spei), [PaymentIntent.next_action.display_bank_transfer_instructions.financial_addresses[].zengin](/api/payment_intents/object?api-version=2024-12-18.acacia#payment_intent_object-next_action-display_bank_transfer_instructions-financial_addresses-zengin) |

#### Go

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `AccountHolderAddress`, `BankAddress` | Added | [FundingInstructionsBankTransferFinancialAddressesIban](/api/issuing/funding_instructions/object?api-version=2024-12-18.acacia#issuing_funding_instructions_object-bank_transfer-financial_addresses-iban), [FundingInstructionsBankTransferFinancialAddressesSortCode](/api/issuing/funding_instructions/object?api-version=2024-12-18.acacia#issuing_funding_instructions_object-bank_transfer-financial_addresses-sort_code), `FundingInstructionsBankTransferFinancialAddressesSpei`, `FundingInstructionsBankTransferFinancialAddressesZengin`, [PaymentIntentNextActionDisplayBankTransferInstructionsFinancialAddressesIban](/api/payment_intents/object?api-version=2024-12-18.acacia#payment_intent_object-next_action-display_bank_transfer_instructions-financial_addresses-iban), [PaymentIntentNextActionDisplayBankTransferInstructionsFinancialAddressesSortCode](/api/payment_intents/object?api-version=2024-12-18.acacia#payment_intent_object-next_action-display_bank_transfer_instructions-financial_addresses-sort_code), [PaymentIntentNextActionDisplayBankTransferInstructionsFinancialAddressesSpei](/api/payment_intents/object?api-version=2024-12-18.acacia#payment_intent_object-next_action-display_bank_transfer_instructions-financial_addresses-spei), [PaymentIntentNextActionDisplayBankTransferInstructionsFinancialAddressesZengin](/api/payment_intents/object?api-version=2024-12-18.acacia#payment_intent_object-next_action-display_bank_transfer_instructions-financial_addresses-zengin) |

#### .NET

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `AccountHolderAddress`, `BankAddress` | Added | [FundingInstructionsBankTransferFinancialAddressesIban](/api/issuing/funding_instructions/object?api-version=2024-12-18.acacia#issuing_funding_instructions_object-bank_transfer-financial_addresses-iban), [FundingInstructionsBankTransferFinancialAddressesSortCode](/api/issuing/funding_instructions/object?api-version=2024-12-18.acacia#issuing_funding_instructions_object-bank_transfer-financial_addresses-sort_code), `FundingInstructionsBankTransferFinancialAddressesSpei`, `FundingInstructionsBankTransferFinancialAddressesZengin`, [PaymentIntentNextActionDisplayBankTransferInstructionsFinancialAddressesIban](/api/payment_intents/object?api-version=2024-12-18.acacia#payment_intent_object-next_action-display_bank_transfer_instructions-financial_addresses-iban), [PaymentIntentNextActionDisplayBankTransferInstructionsFinancialAddressesSortCode](/api/payment_intents/object?api-version=2024-12-18.acacia#payment_intent_object-next_action-display_bank_transfer_instructions-financial_addresses-sort_code), [PaymentIntentNextActionDisplayBankTransferInstructionsFinancialAddressesSpei](/api/payment_intents/object?api-version=2024-12-18.acacia#payment_intent_object-next_action-display_bank_transfer_instructions-financial_addresses-spei), [PaymentIntentNextActionDisplayBankTransferInstructionsFinancialAddressesZengin](/api/payment_intents/object?api-version=2024-12-18.acacia#payment_intent_object-next_action-display_bank_transfer_instructions-financial_addresses-zengin) |

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

- [Adds funding details to Amazon Pay and Revolut Pay charges](https://docs.stripe.com/changelog/acacia/2024-12-18/charge-pm-details.md)
- [Adds support for SEPA Direct Debit and Bacs Direct Debit mandate reference prefix](https://docs.stripe.com/changelog/acacia/2024-12-18/mandate-reference-prefix.md)
