# Upgrades fields and refines error contracts for Payout Methods

## What’s new

Introduces several upgrades to the [Payout Methods](https://docs.stripe.com/api/v2/money-management/payout-methods.md?api-version=2026-09-30.preview) API.

Adds `ineligible` as a new value for the [usage_status](https://docs.stripe.com/api/v2/money-management/payout-methods/object.md?api-version=2026-09-30.preview#v2_payout_method_object-usage_status) property on Payout Methods. The `ineligible` value indicates that a payout method can’t currently be used for money movement. This value can appear in both `usage_status.payments` and `usage_status.transfers`, and you can also filter by `ineligible` when [listing payout methods](https://docs.stripe.com/api/v2/money-management/payout-methods/list.md?api-version=2026-09-30.preview). A payout method is `ineligible` if it is `archived` or `restricted`.

Moves the [archived](https://docs.stripe.com/api/v2/money-management/payout-methods/object.md?api-version=2026-09-30.preview#v2_payout_method_object-archived) property to the top level of the Payout Method resource such that it is read as `payout_method.archived`. Previously, `archived` was nested under each payout method sub-type (such as `payout_method.bank_account.archived` and `payout_method.card.archived`).

Adds `blocked_by_stripe` error type to the `unsupported_us_bank` error code on the [v2 US bank accounts](https://docs.stripe.com/api/v2/core/vault/us-bank-accounts.md?api-version=2026-09-30.preview) API, plus `VerificationAttemptFailed`, `VerificationExpired`, `VerificationNotInitiated`, and `InvalidVaultedCredential` errors across SDKs.

Adds  `blocked_by_stripe` error type to the `unsupported_gb_bank` and `blocked_gb_bank_account` error codes on the [v2 GB bank accounts](https://docs.stripe.com/api/v2/core/vault/gb-bank-accounts.md?api-version=2026-09-30.preview). Also adds `controlled_by_alternate_resource` error type to the `gb_bank_account_cannot_be_archived` error code, and `quota_exceeded` error type to the `limit_gb_bank_account` error code.

Confirmation of Payee no longer affects payments eligibility for GB bank account payout methods. Starting with `2026-09-30.preview`, a GB bank account payout method reports `usage_status.payments` as `eligible` instead of `requires_action` and no longer returns a `confirmation_of_payee` next action, and its Outbound Setup Intent resolves to `succeeded` instead of `requires_action`. `usage_status.transfers` is unchanged.

## Why is this a breaking change?

The `archived` property moves from sub-type objects to the top level, which changes the response shape.

If your code depends on the previous response structure, you must update it to handle these changes.

On `2026-09-30.preview` and later, GB bank account payout methods return `usage_status.payments = eligible` (previously `requires_action` with a `confirmation_of_payee` next action) and their Outbound Setup Intents resolve to `succeeded`. If your integration waits for `requires_action` / `confirmation_of_payee` before treating a GB bank account as usable for payments, update it to treat these payout methods as `eligible`, but be aware that Confirmation of Payee may still be required before the payout method can be used to receive payouts.

## Impact

If your integration reads the `usage_status` property on Payout Methods, you can now receive `ineligible` as a value. Update any code that handles `usage_status` enum values to account for this new status.

If your integration reads the archived property from a sub-type object (such as `bank_account.archived`), you must update it to read `archived` from the top level of the Payout Method resource instead.

## Changes

#### REST API

| Parameters | Change | Resources or endpoints |
| --- | --- | --- |
| `archived` | Added | [V2.MoneyManagement.PayoutMethod](/api/v2/money-management/payout-methods/object?api-version=2026-09-30.preview#v2_payout_method_object) |
| `archived` | Removed | [V2.MoneyManagement.PayoutMethod.bank_account](/api/v2/money-management/payout-methods/object?api-version=2026-09-30.preview#v2_payout_method_object-bank_account), [V2.MoneyManagement.PayoutMethod.card](/api/v2/money-management/payout-methods/object?api-version=2026-09-30.preview#v2_payout_method_object-card) |

| Value | Change | Enums |
| --- | --- | --- |
| `ineligible` | Added | [V2.MoneyManagement.PayoutMethod.usage_status.payments](/api/v2/money-management/payout-methods/object?api-version=2026-09-30.preview#v2_payout_method_object-usage_status-payments), [V2.MoneyManagement.PayoutMethod.usage_status.transfers](/api/v2/money-management/payout-methods/object?api-version=2026-09-30.preview#v2_payout_method_object-usage_status-transfers), [V2.MoneyManagement.PayoutMethod#list.usage_status.payments](/api/v2/money-management/payout-methods/list?api-version=2026-09-30.preview#v2_list_payout_methods-usage_status-payments), [V2.MoneyManagement.PayoutMethod#list.usage_status.transfers](/api/v2/money-management/payout-methods/list?api-version=2026-09-30.preview#v2_list_payout_methods-usage_status-transfers) |

| Codes | Change |  |
| --- | --- | --- |
| `unsupported_us_bank` | Added | `blocked_by_stripe` |
|  | Added | `verification_attempt_failed`, `verification_expired`, `verification_not_initiated`, `invalid_vaulted_credential` |
| `blocked_gb_bank_account`, `unsupported_gb_bank` | Added | `blocked_by_stripe` |
| `gb_bank_account_cannot_be_archived` | Added | `controlled_by_alternate_resource` |
| `limit_gb_bank_account` | Added | `quota_exceeded` |

#### Ruby

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `archived` | Added | [V2::MoneyManagement::PayoutMethod](/api/v2/money-management/payout-methods/object?api-version=2026-09-30.preview#v2_payout_method_object) |
| `archived` | Removed | [V2::MoneyManagement::PayoutMethod::BankAccount](/api/v2/money-management/payout-methods/object?api-version=2026-09-30.preview#v2_payout_method_object-bank_account), [V2::MoneyManagement::PayoutMethod::Card](/api/v2/money-management/payout-methods/object?api-version=2026-09-30.preview#v2_payout_method_object-card) |

| Codes | Change |  |
| --- | --- | --- |
|  | Added | `VerificationAttemptFailedError`, `VerificationExpiredError`, `VerificationNotInitiatedError`, `InvalidVaultedCredentialError` |

#### Python

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `archived` | Added | [V2.MoneyManagement.PayoutMethod](/api/v2/money-management/payout-methods/object?api-version=2026-09-30.preview#v2_payout_method_object) |
| `archived` | Removed | [V2.MoneyManagement.PayoutMethod.BankAccount](/api/v2/money-management/payout-methods/object?api-version=2026-09-30.preview#v2_payout_method_object-bank_account), [V2.MoneyManagement.PayoutMethod.Card](/api/v2/money-management/payout-methods/object?api-version=2026-09-30.preview#v2_payout_method_object-card) |

| Value | Change | Enums |
| --- | --- | --- |
| `ineligible` | Added | [V2.MoneyManagement.PayoutMethod.UsageStatus.payments](/api/v2/money-management/payout-methods/object?api-version=2026-09-30.preview#v2_payout_method_object-usage_status-payments), [V2.MoneyManagement.PayoutMethod.UsageStatus.transfers](/api/v2/money-management/payout-methods/object?api-version=2026-09-30.preview#v2_payout_method_object-usage_status-transfers), [v2.money_management.PayoutMethodListParamsUsageStatus.payments](/api/v2/money-management/payout-methods/list?api-version=2026-09-30.preview#v2_list_payout_methods-usage_status-payments), [v2.money_management.PayoutMethodListParamsUsageStatus.transfers](/api/v2/money-management/payout-methods/list?api-version=2026-09-30.preview#v2_list_payout_methods-usage_status-transfers) |

| Codes | Change |  |
| --- | --- | --- |
| `unsupported_us_bank` | Added | `BlockedByStripeError` |
|  | Added | `VerificationAttemptFailedError`, `VerificationExpiredError`, `VerificationNotInitiatedError`, `InvalidVaultedCredentialError` |
| `blocked_gb_bank_account`, `unsupported_gb_bank` | Added | `BlockedByStripeError` |
| `gb_bank_account_cannot_be_archived` | Added | `ControlledByAlternateResourceError` |
| `limit_gb_bank_account` | Added | `QuotaExceededError` |

#### PHP

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `archived` | Added | [V2.MoneyManagement.PayoutMethod](/api/v2/money-management/payout-methods/object?api-version=2026-09-30.preview#v2_payout_method_object) |
| `archived` | Removed | [V2.MoneyManagement.PayoutMethod.bank_account](/api/v2/money-management/payout-methods/object?api-version=2026-09-30.preview#v2_payout_method_object-bank_account), [V2.MoneyManagement.PayoutMethod.card](/api/v2/money-management/payout-methods/object?api-version=2026-09-30.preview#v2_payout_method_object-card) |

| Value | Change | Enums |
| --- | --- | --- |
| `ineligible` | Added | [V2.MoneyManagement.PayoutMethod.usage_status.payments](/api/v2/money-management/payout-methods/object?api-version=2026-09-30.preview#v2_payout_method_object-usage_status-payments), [V2.MoneyManagement.PayoutMethod.usage_status.transfers](/api/v2/money-management/payout-methods/object?api-version=2026-09-30.preview#v2_payout_method_object-usage_status-transfers) |

| Codes | Change |  |
| --- | --- | --- |
|  | Added | `VerificationAttemptFailedException`, `VerificationExpiredException`, `VerificationNotInitiatedException`, `InvalidVaultedCredentialException` |

#### Java

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `archived` | Added | [v2.moneymanagement.PayoutMethod](/api/v2/money-management/payout-methods/object?api-version=2026-09-30.preview#v2_payout_method_object) |
| `archived` | Removed | [v2.moneymanagement.PayoutMethod.bank_account](/api/v2/money-management/payout-methods/object?api-version=2026-09-30.preview#v2_payout_method_object-bank_account), [v2.moneymanagement.PayoutMethod.card](/api/v2/money-management/payout-methods/object?api-version=2026-09-30.preview#v2_payout_method_object-card) |

| Value | Change | Enums |
| --- | --- | --- |
| `ineligible` | Added | [v2.moneymanagement.PayoutMethodListParams.usage_status.payments](/api/v2/money-management/payout-methods/list?api-version=2026-09-30.preview#v2_list_payout_methods-usage_status-payments), [v2.moneymanagement.PayoutMethodListParams.usage_status.transfers](/api/v2/money-management/payout-methods/list?api-version=2026-09-30.preview#v2_list_payout_methods-usage_status-transfers) |

| Codes | Change |  |
| --- | --- | --- |
|  | Added | `VerificationAttemptFailedException`, `VerificationExpiredException`, `VerificationNotInitiatedException`, `InvalidVaultedCredentialException` |

#### Node.js

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `archived` | Added | [V2.MoneyManagement.PayoutMethod](/api/v2/money-management/payout-methods/object?api-version=2026-09-30.preview#v2_payout_method_object) |
| `archived` | Removed | [V2.MoneyManagement.PayoutMethod.bank_account](/api/v2/money-management/payout-methods/object?api-version=2026-09-30.preview#v2_payout_method_object-bank_account), [V2.MoneyManagement.PayoutMethod.card](/api/v2/money-management/payout-methods/object?api-version=2026-09-30.preview#v2_payout_method_object-card) |

| Value | Change | Enums |
| --- | --- | --- |
| `ineligible` | Added | [V2.MoneyManagement.PayoutMethod.usage_status.payments](/api/v2/money-management/payout-methods/object?api-version=2026-09-30.preview#v2_payout_method_object-usage_status-payments), [V2.MoneyManagement.PayoutMethod.usage_status.transfers](/api/v2/money-management/payout-methods/object?api-version=2026-09-30.preview#v2_payout_method_object-usage_status-transfers), [V2.MoneyManagement.PayoutMethodListParams.usage_status.payments](/api/v2/money-management/payout-methods/list?api-version=2026-09-30.preview#v2_list_payout_methods-usage_status-payments), [V2.MoneyManagement.PayoutMethodListParams.usage_status.transfers](/api/v2/money-management/payout-methods/list?api-version=2026-09-30.preview#v2_list_payout_methods-usage_status-transfers) |

| Codes | Change |  |
| --- | --- | --- |
| `unsupported_us_bank` | Added | `BlockedByStripeError` |
|  | Added | `VerificationAttemptFailedError`, `VerificationExpiredError`, `VerificationNotInitiatedError`, `InvalidVaultedCredentialError` |
| `blocked_gb_bank_account`, `unsupported_gb_bank` | Added | `BlockedByStripeError` |
| `gb_bank_account_cannot_be_archived` | Added | `ControlledByAlternateResourceError` |
| `limit_gb_bank_account` | Added | `QuotaExceededError` |

#### Go

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `Archived` | Added | [V2MoneyManagementPayoutMethod](/api/v2/money-management/payout-methods/object?api-version=2026-09-30.preview#v2_payout_method_object) |
| `Archived` | Removed | [V2MoneyManagementPayoutMethodBankAccount](/api/v2/money-management/payout-methods/object?api-version=2026-09-30.preview#v2_payout_method_object-bank_account), [V2MoneyManagementPayoutMethodCard](/api/v2/money-management/payout-methods/object?api-version=2026-09-30.preview#v2_payout_method_object-card) |

| Value | Change | Enums |
| --- | --- | --- |
| `ineligible` | Added | [V2MoneyManagementPayoutMethodUsageStatus.Payments](/api/v2/money-management/payout-methods/object?api-version=2026-09-30.preview#v2_payout_method_object-usage_status-Payments), [V2MoneyManagementPayoutMethodUsageStatus.Transfers](/api/v2/money-management/payout-methods/object?api-version=2026-09-30.preview#v2_payout_method_object-usage_status-Transfers) |

| Codes | Change |  |
| --- | --- | --- |
| `unsupported_us_bank` | Added | `BlockedByStripeError` |
|  | Added | `VerificationAttemptFailedError`, `VerificationExpiredError`, `VerificationNotInitiatedError`, `InvalidVaultedCredentialError` |
| `blocked_gb_bank_account`, `unsupported_gb_bank` | Added | `BlockedByStripeError` |
| `gb_bank_account_cannot_be_archived` | Added | `ControlledByAlternateResourceError` |
| `limit_gb_bank_account` | Added | `QuotaExceededError` |

#### .NET

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `Archived` | Added | [V2.MoneyManagement.PayoutMethod](/api/v2/money-management/payout-methods/object?api-version=2026-09-30.preview#v2_payout_method_object) |
| `Archived` | Removed | [V2.MoneyManagement.PayoutMethod.BankAccount](/api/v2/money-management/payout-methods/object?api-version=2026-09-30.preview#v2_payout_method_object-bank_account), [V2.MoneyManagement.PayoutMethod.Card](/api/v2/money-management/payout-methods/object?api-version=2026-09-30.preview#v2_payout_method_object-card) |

| Codes | Change |  |
| --- | --- | --- |
|  | Added | `VerificationAttemptFailedException`, `VerificationExpiredException`, `VerificationNotInitiatedException`, `InvalidVaultedCredentialException` |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2026-09-30.preview`
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

- [Adds rejected status for Accounts v2 capabilities](https://docs.stripe.com/changelog/endive/2026-09-30/rejected-accounts-v2-capabilities-preview.md)
