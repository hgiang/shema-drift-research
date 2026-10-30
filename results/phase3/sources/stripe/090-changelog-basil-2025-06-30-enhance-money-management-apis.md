# Adds new status and consolidates error codes for money management APIs

## What’s new

This release introduces several enhancements for [money management](https://docs.stripe.com/money-management.md):

- Adds a new `pending` status to the [Financial Account](https://docs.stripe.com/api/v2/money-management/financial-accounts.md?api-version=preview) resource to indicate when a Financial Account has been created and is in the process of opening.
- Replaces the `description` property with `metadata` in the [Financial Account](https://docs.stripe.com/api/v2/money-management/financial-accounts.md?api-version=preview) resource.
- Adds additional types to the `balance_transfer` object in the [Received Credit](https://docs.stripe.com/api/v2/money-management/received-credits.md?api-version=preview) resource.
- Consolidates and aligns error codes for the methods to [create an outbound transfer](https://docs.stripe.com/api/v2/money-management/outbound-transfers/create.md?api-version=preview) and [create an outbound payment](https://docs.stripe.com/api/v2/money-management/outbound-payments/create.md?api-version=preview).

| Old error code | New error code |
| --- | --- |
| `outbound_transfer_insufficient_funds` | `insufficient_funds` |
| `outbound_payment_insufficient_funds` | `insufficient_funds` |
| `outbound_payment_recipient_amount_limit_exceeded` | `recipient_amount_limit_exceeded` |
| `outbound_payment_recipient_count_limit_exceeded` | `recipient_count_limit_exceeded` |
| `outbound_payment_recipient_email_does_not_exist` | `recipient_email_does_not_exist` |
| `outbound_payment_recipient_feature_not_active` | `recipient_feature_not_active` |

## Impact

- The new `pending` status provides greater visibility into [Financial Account](https://docs.stripe.com/api/v2/money-management/financial-accounts.md?api-version=preview) states when you’re creating accounts.
- Replacing `description` with `metadata` allows you to associate more powerful, structured data with Financial Accounts.
- Consolidating error codes across the methods to [create an outbound transfer](https://docs.stripe.com/api/v2/money-management/outbound-transfers/create.md?api-version=preview) and [create an outbound payment](https://docs.stripe.com/api/v2/money-management/outbound-payments/create.md?api-version=preview) simplifies error management for your integration.

## Changes

#### REST API

| Parameters | Change | Resources or endpoints |
| --- | --- | --- |
| `metadata` | Added | [V2.MoneyManagement.FinancialAccount](/api/v2/money-management/financial-accounts/object?api-version=2025-06-30.preview) |
| `description` | Removed | [V2.MoneyManagement.FinancialAccount](/api/v2/money-management/financial-accounts/object?api-version=2025-06-30.preview) |
| `from_account`, `outbound_payment`, `outbound_transfer` | Added | [V2.MoneyManagement.ReceivedCredit.balance_transfer](/api/v2/money-management/received-credits/object?api-version=2025-06-30.preview#v2_received_credit_object-balance_transfer) |

| Value | Change | Enum |
| --- | --- | --- |
| `pending` | Added | [V2.MoneyManagement.FinancialAccount.status](/api/v2/money-management/financial-accounts/object?api-version=2025-06-30.preview#v2_financial_account_object-status) |

| Fields | Change | From → to |
| --- | --- | --- |
| `V2.MoneyManagement.ReceivedCredit.balance_transfer.type` | Changed | [literal('payout_v1') → enum('outbound_payment'|'outbound_transfer'|'payout_v1')](/api/v2/money-management/received-credits/object?api-version=2025-06-30.preview#v2_received_credit_object-balance_transfer-type) |
| `V2.MoneyManagement.ReceivedCredit.balance_transfer.payout_v1` | Changed | [string → nullable(string)](/api/v2/money-management/received-credits/object?api-version=2025-06-30.preview#v2_received_credit_object-balance_transfer-payout_v1) |

| Codes | Change |  |
| --- | --- | --- |
| `storer_capability_missing`, `storer_capability_not_active` | Added | [Error.code](/api/errors?api-version=2025-06-30.preview#errors-code) |
| `insufficient_funds` | Added | [Error.code](/api/errors?api-version=2025-06-30.preview#errors-code) |
| `outbound_payment_insufficient_funds`, `outbound_transfer_insufficient_funds` | Removed | [Error.code](/api/errors?api-version=2025-06-30.preview#errors-code) |
| `recipient_amount_limit_exceeded`, `recipient_count_limit_exceeded` | Added | [Error.code](/api/errors?api-version=2025-06-30.preview#errors-code) |
| `outbound_payment_recipient_amount_limit_exceeded`, `outbound_payment_recipient_count_limit_exceeded` | Removed | [Error.code](/api/errors?api-version=2025-06-30.preview#errors-code) |
| `recipient_email_does_not_exist` | Added | [Error.code](/api/errors?api-version=2025-06-30.preview#errors-code) |
| `outbound_payment_recipient_email_does_not_exist` | Removed | [Error.code](/api/errors?api-version=2025-06-30.preview#errors-code) |
| `recipient_feature_not_active` | Added | [Error.code](/api/errors?api-version=2025-06-30.preview#errors-code) |
| `outbound_payment_recipient_feature_not_active` | Removed | [Error.code](/api/errors?api-version=2025-06-30.preview#errors-code) |

#### Ruby

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `metadata` | Added | [V2::MoneyManagement::FinancialAccount](/api/v2/money-management/financial-accounts/object?api-version=2025-06-30.preview) |
| `description` | Removed | [V2::MoneyManagement::FinancialAccount](/api/v2/money-management/financial-accounts/object?api-version=2025-06-30.preview) |
| `from_account`, `outbound_payment`, `outbound_transfer` | Added | [V2::MoneyManagement::ReceivedCredit::BalanceTransfer](/api/v2/money-management/received-credits/object?api-version=2025-06-30.preview#v2_received_credit_object-balance_transfer) |

| Fields | Change | From → to |
| --- | --- | --- |
| `V2::MoneyManagement::ReceivedCredit::BalanceTransfer.type` | Changed | [literal('payout_v1') → enum('outbound_payment'|'outbound_transfer'|'payout_v1')](/api/v2/money-management/received-credits/object?api-version=2025-06-30.preview#v2_received_credit_object-balance_transfer-type) |
| `V2::MoneyManagement::ReceivedCredit::BalanceTransfer.payout_v1` | Changed | [string → nullable(string)](/api/v2/money-management/received-credits/object?api-version=2025-06-30.preview#v2_received_credit_object-balance_transfer-payout_v1) |

| Codes | Change |  |
| --- | --- | --- |
| `StorerCapabilityMissingError`, `StorerCapabilityNotActiveError` | Added | [Error.code](/api/errors?api-version=2025-06-30.preview#errors-code) |
| `InsufficientFundsError` | Added | [Error.code](/api/errors?api-version=2025-06-30.preview#errors-code) |
| `OutboundPaymentInsufficientFundsError`, `OutboundTransferInsufficientFundsError` | Removed | [Error.code](/api/errors?api-version=2025-06-30.preview#errors-code) |
| `RecipientAmountLimitExceededError`, `RecipientCountLimitExceededError` | Added | [Error.code](/api/errors?api-version=2025-06-30.preview#errors-code) |
| `OutboundPaymentRecipientAmountLimitExceededError`, `OutboundPaymentRecipientCountLimitExceededError` | Removed | [Error.code](/api/errors?api-version=2025-06-30.preview#errors-code) |
| `RecipientEmailDoesNotExistError` | Added | [Error.code](/api/errors?api-version=2025-06-30.preview#errors-code) |
| `OutboundPaymentRecipientEmailDoesNotExistError` | Removed | [Error.code](/api/errors?api-version=2025-06-30.preview#errors-code) |
| `RecipientFeatureNotActiveError` | Added | [Error.code](/api/errors?api-version=2025-06-30.preview#errors-code) |
| `OutboundPaymentRecipientFeatureNotActiveError` | Removed | [Error.code](/api/errors?api-version=2025-06-30.preview#errors-code) |

#### Python

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `metadata` | Added | [V2.MoneyManagement.FinancialAccount](/api/v2/money-management/financial-accounts/object?api-version=2025-06-30.preview) |
| `description` | Removed | [V2.MoneyManagement.FinancialAccount](/api/v2/money-management/financial-accounts/object?api-version=2025-06-30.preview) |
| `from_account`, `outbound_payment`, `outbound_transfer` | Added | [V2.MoneyManagement.ReceivedCredit.BalanceTransfer](/api/v2/money-management/received-credits/object?api-version=2025-06-30.preview#v2_received_credit_object-balance_transfer) |

| Value | Change | Enum |
| --- | --- | --- |
| `pending` | Added | [V2.MoneyManagement.FinancialAccount.status](/api/v2/money-management/financial-accounts/object?api-version=2025-06-30.preview#v2_financial_account_object-status) |

| Fields | Change | From → to |
| --- | --- | --- |
| `V2.MoneyManagement.ReceivedCredit.BalanceTransfer.type` | Changed | [literal('payout_v1') → enum('outbound_payment'|'outbound_transfer'|'payout_v1')](/api/v2/money-management/received-credits/object?api-version=2025-06-30.preview#v2_received_credit_object-balance_transfer-type) |
| `V2.MoneyManagement.ReceivedCredit.BalanceTransfer.payout_v1` | Changed | [string → nullable(string)](/api/v2/money-management/received-credits/object?api-version=2025-06-30.preview#v2_received_credit_object-balance_transfer-payout_v1) |

| Codes | Change |  |
| --- | --- | --- |
| `StorerCapabilityMissingException`, `StorerCapabilityNotActiveException` | Added | [Error.code](/api/errors?api-version=2025-06-30.preview#errors-code) |
| `InsufficientFundsException` | Added | [Error.code](/api/errors?api-version=2025-06-30.preview#errors-code) |
| `OutboundPaymentInsufficientFundsException`, `OutboundTransferInsufficientFundsException` | Removed | [Error.code](/api/errors?api-version=2025-06-30.preview#errors-code) |
| `RecipientAmountLimitExceededException`, `RecipientCountLimitExceededException` | Added | [Error.code](/api/errors?api-version=2025-06-30.preview#errors-code) |
| `OutboundPaymentRecipientAmountLimitExceededException`, `OutboundPaymentRecipientCountLimitExceededException` | Removed | [Error.code](/api/errors?api-version=2025-06-30.preview#errors-code) |
| `RecipientEmailDoesNotExistException` | Added | [Error.code](/api/errors?api-version=2025-06-30.preview#errors-code) |
| `OutboundPaymentRecipientEmailDoesNotExistException` | Removed | [Error.code](/api/errors?api-version=2025-06-30.preview#errors-code) |
| `RecipientFeatureNotActiveException` | Added | [Error.code](/api/errors?api-version=2025-06-30.preview#errors-code) |
| `OutboundPaymentRecipientFeatureNotActiveException` | Removed | [Error.code](/api/errors?api-version=2025-06-30.preview#errors-code) |

#### PHP

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `metadata` | Added | [V2.MoneyManagement.FinancialAccount](/api/v2/money-management/financial-accounts/object?api-version=2025-06-30.preview) |
| `description` | Removed | [V2.MoneyManagement.FinancialAccount](/api/v2/money-management/financial-accounts/object?api-version=2025-06-30.preview) |

| Value | Change | Enum |
| --- | --- | --- |
| `pending` | Added | [V2.MoneyManagement.FinancialAccount.status](/api/v2/money-management/financial-accounts/object?api-version=2025-06-30.preview#v2_financial_account_object-status) |

| Fields | Change | From → to |
| --- | --- | --- |
| `V2.MoneyManagement.ReceivedCredit.balance_transfer.type` | Changed | [literal('payout_v1') → enum('outbound_payment'|'outbound_transfer'|'payout_v1')](/api/v2/money-management/received-credits/object?api-version=2025-06-30.preview#v2_received_credit_object-balance_transfer-type) |
| `V2.MoneyManagement.ReceivedCredit.balance_transfer.payout_v1` | Changed | [string → nullable(string)](/api/v2/money-management/received-credits/object?api-version=2025-06-30.preview#v2_received_credit_object-balance_transfer-payout_v1) |

| Codes | Change |  |
| --- | --- | --- |
| `StorerCapabilityMissingException`, `StorerCapabilityNotActiveException` | Added | [Error.code](/api/errors?api-version=2025-06-30.preview#errors-code) |
| `InsufficientFundsException` | Added | [Error.code](/api/errors?api-version=2025-06-30.preview#errors-code) |
| `OutboundPaymentInsufficientFundsException`, `OutboundTransferInsufficientFundsException` | Removed | [Error.code](/api/errors?api-version=2025-06-30.preview#errors-code) |
| `RecipientAmountLimitExceededException`, `RecipientCountLimitExceededException` | Added | [Error.code](/api/errors?api-version=2025-06-30.preview#errors-code) |
| `OutboundPaymentRecipientAmountLimitExceededException`, `OutboundPaymentRecipientCountLimitExceededException` | Removed | [Error.code](/api/errors?api-version=2025-06-30.preview#errors-code) |
| `RecipientEmailDoesNotExistException` | Added | [Error.code](/api/errors?api-version=2025-06-30.preview#errors-code) |
| `OutboundPaymentRecipientEmailDoesNotExistException` | Removed | [Error.code](/api/errors?api-version=2025-06-30.preview#errors-code) |
| `RecipientFeatureNotActiveException` | Added | [Error.code](/api/errors?api-version=2025-06-30.preview#errors-code) |
| `OutboundPaymentRecipientFeatureNotActiveException` | Removed | [Error.code](/api/errors?api-version=2025-06-30.preview#errors-code) |

#### Java

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `metadata` | Added | [v2.moneymanagement.FinancialAccount](/api/v2/money-management/financial-accounts/object?api-version=2025-06-30.preview) |
| `description` | Removed | [v2.moneymanagement.FinancialAccount](/api/v2/money-management/financial-accounts/object?api-version=2025-06-30.preview) |
| `fromAccount`, `outboundPayment`, `outboundTransfer` | Added | [v2.moneymanagement.ReceivedCredit.balance_transfer](/api/v2/money-management/received-credits/object?api-version=2025-06-30.preview#v2_received_credit_object-balance_transfer) |

| Field | Change | From → to |
| --- | --- | --- |
| `v2.moneymanagement.ReceivedCredit.balance_transfer.type` | Changed | [literal('payout_v1') → enum('outbound_payment'|'outbound_transfer'|'payout_v1')](/api/v2/money-management/received-credits/object?api-version=2025-06-30.preview#v2_received_credit_object-balance_transfer-type) |

| Codes | Change |  |
| --- | --- | --- |
| `StorerCapabilityMissingException`, `StorerCapabilityNotActiveException` | Added | [Error.code](/api/errors?api-version=2025-06-30.preview#errors-code) |
| `InsufficientFundsException` | Added | [Error.code](/api/errors?api-version=2025-06-30.preview#errors-code) |
| `OutboundPaymentInsufficientFundsException`, `OutboundTransferInsufficientFundsException` | Removed | [Error.code](/api/errors?api-version=2025-06-30.preview#errors-code) |
| `RecipientAmountLimitExceededException`, `RecipientCountLimitExceededException` | Added | [Error.code](/api/errors?api-version=2025-06-30.preview#errors-code) |
| `OutboundPaymentRecipientAmountLimitExceededException`, `OutboundPaymentRecipientCountLimitExceededException` | Removed | [Error.code](/api/errors?api-version=2025-06-30.preview#errors-code) |
| `RecipientEmailDoesNotExistException` | Added | [Error.code](/api/errors?api-version=2025-06-30.preview#errors-code) |
| `OutboundPaymentRecipientEmailDoesNotExistException` | Removed | [Error.code](/api/errors?api-version=2025-06-30.preview#errors-code) |
| `RecipientFeatureNotActiveException` | Added | [Error.code](/api/errors?api-version=2025-06-30.preview#errors-code) |
| `OutboundPaymentRecipientFeatureNotActiveException` | Removed | [Error.code](/api/errors?api-version=2025-06-30.preview#errors-code) |

#### Node.js

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `metadata` | Added | [V2.MoneyManagement.FinancialAccount](/api/v2/money-management/financial-accounts/object?api-version=2025-06-30.preview) |
| `description` | Removed | [V2.MoneyManagement.FinancialAccount](/api/v2/money-management/financial-accounts/object?api-version=2025-06-30.preview) |
| `from_account`, `outbound_payment`, `outbound_transfer` | Added | [V2.MoneyManagement.ReceivedCredit.balance_transfer](/api/v2/money-management/received-credits/object?api-version=2025-06-30.preview#v2_received_credit_object-balance_transfer) |

| Value | Change | Enum |
| --- | --- | --- |
| `pending` | Added | [V2.MoneyManagement.FinancialAccount.status](/api/v2/money-management/financial-accounts/object?api-version=2025-06-30.preview#v2_financial_account_object-status) |

| Fields | Change | From → to |
| --- | --- | --- |
| `V2.MoneyManagement.ReceivedCredit.balance_transfer.type` | Changed | [literal('payout_v1') → enum('outbound_payment'|'outbound_transfer'|'payout_v1')](/api/v2/money-management/received-credits/object?api-version=2025-06-30.preview#v2_received_credit_object-balance_transfer-type) |
| `V2.MoneyManagement.ReceivedCredit.balance_transfer.payout_v1` | Changed | [string → string | null](/api/v2/money-management/received-credits/object?api-version=2025-06-30.preview#v2_received_credit_object-balance_transfer-payout_v1) |

| Codes | Change |  |
| --- | --- | --- |
| `StorerCapabilityMissingError`, `StorerCapabilityNotActiveError` | Added | [Error.code](/api/errors?api-version=2025-06-30.preview#errors-code) |
| `InsufficientFundsError` | Added | [Error.code](/api/errors?api-version=2025-06-30.preview#errors-code) |
| `OutboundPaymentInsufficientFundsError`, `OutboundTransferInsufficientFundsError` | Removed | [Error.code](/api/errors?api-version=2025-06-30.preview#errors-code) |
| `RecipientAmountLimitExceededError`, `RecipientCountLimitExceededError` | Added | [Error.code](/api/errors?api-version=2025-06-30.preview#errors-code) |
| `OutboundPaymentRecipientAmountLimitExceededError`, `OutboundPaymentRecipientCountLimitExceededError` | Removed | [Error.code](/api/errors?api-version=2025-06-30.preview#errors-code) |
| `RecipientEmailDoesNotExistError` | Added | [Error.code](/api/errors?api-version=2025-06-30.preview#errors-code) |
| `OutboundPaymentRecipientEmailDoesNotExistError` | Removed | [Error.code](/api/errors?api-version=2025-06-30.preview#errors-code) |
| `RecipientFeatureNotActiveError` | Added | [Error.code](/api/errors?api-version=2025-06-30.preview#errors-code) |
| `OutboundPaymentRecipientFeatureNotActiveError` | Removed | [Error.code](/api/errors?api-version=2025-06-30.preview#errors-code) |

#### Go

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `Metadata` | Added | [V2MoneyManagementFinancialAccount](/api/v2/money-management/financial-accounts/object?api-version=2025-06-30.preview) |
| `Description` | Removed | [V2MoneyManagementFinancialAccount](/api/v2/money-management/financial-accounts/object?api-version=2025-06-30.preview) |
| `FromAccount`, `OutboundPayment`, `OutboundTransfer` | Added | [V2MoneyManagementReceivedCreditBalanceTransfer](/api/v2/money-management/received-credits/object?api-version=2025-06-30.preview#v2_received_credit_object-balance_transfer) |

| Value | Change | Enum |
| --- | --- | --- |
| `pending` | Added | [V2MoneyManagementFinancialAccount.Status](/api/v2/money-management/financial-accounts/object?api-version=2025-06-30.preview#v2_financial_account_object-status) |

| Field | Change | From → to |
| --- | --- | --- |
| `V2MoneyManagementReceivedCreditBalanceTransfer.Type` | Changed | [literal('payout_v1') → enum('outbound_payment'|'outbound_transfer'|'payout_v1')](/api/v2/money-management/received-credits/object?api-version=2025-06-30.preview#v2_received_credit_object-balance_transfer-type) |

| Codes | Change |  |
| --- | --- | --- |
| `StorerCapabilityMissingError`, `StorerCapabilityNotActiveError` | Added | [Error.code](/api/errors?api-version=2025-06-30.preview#errors-code) |
| `InsufficientFundsError` | Added | [Error.code](/api/errors?api-version=2025-06-30.preview#errors-code) |
| `OutboundPaymentInsufficientFundsError`, `OutboundTransferInsufficientFundsError` | Removed | [Error.code](/api/errors?api-version=2025-06-30.preview#errors-code) |
| `RecipientAmountLimitExceededError`, `RecipientCountLimitExceededError` | Added | [Error.code](/api/errors?api-version=2025-06-30.preview#errors-code) |
| `OutboundPaymentRecipientAmountLimitExceededError`, `OutboundPaymentRecipientCountLimitExceededError` | Removed | [Error.code](/api/errors?api-version=2025-06-30.preview#errors-code) |
| `RecipientEmailDoesNotExistError` | Added | [Error.code](/api/errors?api-version=2025-06-30.preview#errors-code) |
| `OutboundPaymentRecipientEmailDoesNotExistError` | Removed | [Error.code](/api/errors?api-version=2025-06-30.preview#errors-code) |
| `RecipientFeatureNotActiveError` | Added | [Error.code](/api/errors?api-version=2025-06-30.preview#errors-code) |
| `OutboundPaymentRecipientFeatureNotActiveError` | Removed | [Error.code](/api/errors?api-version=2025-06-30.preview#errors-code) |

#### .NET

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `Metadata` | Added | [V2.MoneyManagement.FinancialAccount](/api/v2/money-management/financial-accounts/object?api-version=2025-06-30.preview) |
| `Description` | Removed | [V2.MoneyManagement.FinancialAccount](/api/v2/money-management/financial-accounts/object?api-version=2025-06-30.preview) |
| `FromAccount`, `OutboundPayment`, `OutboundTransfer` | Added | [V2.MoneyManagement.ReceivedCredit.BalanceTransfer](/api/v2/money-management/received-credits/object?api-version=2025-06-30.preview#v2_received_credit_object-balance_transfer) |

| Field | Change | From → to |
| --- | --- | --- |
| `V2.MoneyManagement.ReceivedCredit.BalanceTransfer.Type` | Changed | [literal('payout_v1') → enum('outbound_payment'|'outbound_transfer'|'payout_v1')](/api/v2/money-management/received-credits/object?api-version=2025-06-30.preview#v2_received_credit_object-balance_transfer-type) |

| Codes | Change |  |
| --- | --- | --- |
| `StorerCapabilityMissingException`, `StorerCapabilityNotActiveException` | Added | [Error.code](/api/errors?api-version=2025-06-30.preview#errors-code) |
| `InsufficientFundsException` | Added | [Error.code](/api/errors?api-version=2025-06-30.preview#errors-code) |
| `OutboundPaymentInsufficientFundsException`, `OutboundTransferInsufficientFundsException` | Removed | [Error.code](/api/errors?api-version=2025-06-30.preview#errors-code) |
| `RecipientAmountLimitExceededException`, `RecipientCountLimitExceededException` | Added | [Error.code](/api/errors?api-version=2025-06-30.preview#errors-code) |
| `OutboundPaymentRecipientAmountLimitExceededException`, `OutboundPaymentRecipientCountLimitExceededException` | Removed | [Error.code](/api/errors?api-version=2025-06-30.preview#errors-code) |
| `RecipientEmailDoesNotExistException` | Added | [Error.code](/api/errors?api-version=2025-06-30.preview#errors-code) |
| `OutboundPaymentRecipientEmailDoesNotExistException` | Removed | [Error.code](/api/errors?api-version=2025-06-30.preview#errors-code) |
| `RecipientFeatureNotActiveException` | Added | [Error.code](/api/errors?api-version=2025-06-30.preview#errors-code) |
| `OutboundPaymentRecipientFeatureNotActiveException` | Removed | [Error.code](/api/errors?api-version=2025-06-30.preview#errors-code) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2025-06-30.preview`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to [v15.4.0-beta.2](https://github.com/stripe/stripe-ruby/releases/tag/v15.4.0-beta.2)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to [v12.4.0b2](https://github.com/stripe/stripe-python/releases/tag/v12.4.0b2)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to [v17.5.0-beta.2](https://github.com/stripe/stripe-php/releases/tag/v17.5.0-beta.2)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to [v29.4.0-beta.2](https://github.com/stripe/stripe-java/releases/tag/v29.4.0-beta.2)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to [v18.4.0-beta.2](https://github.com/stripe/stripe-node/releases/tag/v18.4.0-beta.2)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to [v82.4.0-beta.2](https://github.com/stripe/stripe-go/releases/tag/v82.4.0-beta.2)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to [v48.4.0-beta.2](https://github.com/stripe/stripe-dotnet/releases/tag/v48.4.0-beta.2)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).
