# Updates bank account and payout method resources for Global Payouts

## What’s new

- Renames the `enabled_delivery_options` property to [enabled_delivery_schemes](https://docs.stripe.com/api/v2/money-management/payout-methods/object.md?api-version=2026-08-26.preview#v2_payout_method_object-bank_account-enabled_delivery_schemes) on the [bank_account](https://docs.stripe.com/api/v2/money-management/payout-methods/object.md?api-version=2026-08-26.preview#v2_payout_method_object-bank_account) hash of the [v2 Payout Method](https://docs.stripe.com/api/v2/money-management/payout-methods.md?api-version=2026-08-26.preview) object. The new name better reflects that the property represents delivery schemes rather than generic options.
- Adds the [restricted](https://docs.stripe.com/api/v2/core/vault/us-bank-accounts/object.md?api-version=2026-08-26.preview#v2_us_bank_account_object-restricted) property to [US Bank Account](https://docs.stripe.com/api/v2/core/vault/us-bank-accounts/object.md?api-version=2026-08-26.preview) and [GB Bank Account](https://docs.stripe.com/api/v2/core/vault/gb-bank-accounts/object.md?api-version=2026-08-26.preview) vault resources. This Boolean property indicates whether a user can use a correctly configured bank account for money movement. Without this field, users might infer blocked transactions as invalid configuration.

## Why is this a breaking change?

Integrations that reference the `enabled_delivery_options` property of the v2 Payout Methods object’s `bank_account` hash won’t receive expected data and might receive errors if they don’t handle the renamed property in their integration.

## Impact

If your integration reads the `enabled_delivery_options` property from v2 Payout Method Bank Account objects, you must update your code to use `enabled_delivery_schemes` instead.

You can also now inspect the `restricted` property on vault bank accounts to determine whether a bank account can receive payouts on Stripe. This new functionality isn’t breaking and requires no change if you choose not to use it.

## Changes

#### REST API

| Parameters | Change | Resources or endpoints |
| --- | --- | --- |
| `restricted` | Added | [V2.Core.Vault.GbBankAccount](/api/v2/core/vault/gb-bank-accounts/object?api-version=2026-08-26.preview#v2_gb_bank_account_object), [V2.Core.Vault.UsBankAccount](/api/v2/core/vault/us-bank-accounts/object?api-version=2026-08-26.preview#v2_us_bank_account_object) |
| `enabled_delivery_schemes` | Added | [V2.MoneyManagement.PayoutMethod.bank_account](/api/v2/money-management/payout-methods/object?api-version=2026-08-26.preview#v2_payout_method_object-bank_account) |
| `enabled_delivery_options` | Removed | [V2.MoneyManagement.PayoutMethod.bank_account](/api/v2/money-management/payout-methods/object?api-version=2026-08-26.preview#v2_payout_method_object-bank_account) |

#### Ruby

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `restricted` | Added | [V2::Core::Vault::GbBankAccount](/api/v2/core/vault/gb-bank-accounts/object?api-version=2026-08-26.preview#v2_gb_bank_account_object), [V2::Core::Vault::UsBankAccount](/api/v2/core/vault/us-bank-accounts/object?api-version=2026-08-26.preview#v2_us_bank_account_object) |
| `enabled_delivery_schemes` | Added | [V2::MoneyManagement::PayoutMethod::BankAccount](/api/v2/money-management/payout-methods/object?api-version=2026-08-26.preview#v2_payout_method_object-bank_account) |
| `enabled_delivery_options` | Removed | [V2::MoneyManagement::PayoutMethod::BankAccount](/api/v2/money-management/payout-methods/object?api-version=2026-08-26.preview#v2_payout_method_object-bank_account) |

#### Python

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `restricted` | Added | [V2.Core.Vault.GbBankAccount](/api/v2/core/vault/gb-bank-accounts/object?api-version=2026-08-26.preview#v2_gb_bank_account_object), [V2.Core.Vault.UsBankAccount](/api/v2/core/vault/us-bank-accounts/object?api-version=2026-08-26.preview#v2_us_bank_account_object) |
| `enabled_delivery_schemes` | Added | [V2.MoneyManagement.PayoutMethod.BankAccount](/api/v2/money-management/payout-methods/object?api-version=2026-08-26.preview#v2_payout_method_object-bank_account) |
| `enabled_delivery_options` | Removed | [V2.MoneyManagement.PayoutMethod.BankAccount](/api/v2/money-management/payout-methods/object?api-version=2026-08-26.preview#v2_payout_method_object-bank_account) |

#### PHP

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `restricted` | Added | [V2.Core.Vault.GbBankAccount](/api/v2/core/vault/gb-bank-accounts/object?api-version=2026-08-26.preview#v2_gb_bank_account_object), [V2.Core.Vault.UsBankAccount](/api/v2/core/vault/us-bank-accounts/object?api-version=2026-08-26.preview#v2_us_bank_account_object) |
| `enabled_delivery_schemes` | Added | [V2.MoneyManagement.PayoutMethod.bank_account](/api/v2/money-management/payout-methods/object?api-version=2026-08-26.preview#v2_payout_method_object-bank_account) |
| `enabled_delivery_options` | Removed | [V2.MoneyManagement.PayoutMethod.bank_account](/api/v2/money-management/payout-methods/object?api-version=2026-08-26.preview#v2_payout_method_object-bank_account) |

#### Java

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `restricted` | Added | [v2.core.vault.GbBankAccount](/api/v2/core/vault/gb-bank-accounts/object?api-version=2026-08-26.preview#v2_gb_bank_account_object), [v2.core.vault.UsBankAccount](/api/v2/core/vault/us-bank-accounts/object?api-version=2026-08-26.preview#v2_us_bank_account_object) |
| `enabledDeliverySchemes` | Added | [v2.moneymanagement.PayoutMethod.bank_account](/api/v2/money-management/payout-methods/object?api-version=2026-08-26.preview#v2_payout_method_object-bank_account) |
| `enabledDeliveryOptions` | Removed | [v2.moneymanagement.PayoutMethod.bank_account](/api/v2/money-management/payout-methods/object?api-version=2026-08-26.preview#v2_payout_method_object-bank_account) |

#### Node.js

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `restricted` | Added | [V2.Core.Vault.GbBankAccount](/api/v2/core/vault/gb-bank-accounts/object?api-version=2026-08-26.preview#v2_gb_bank_account_object), [V2.Core.Vault.UsBankAccount](/api/v2/core/vault/us-bank-accounts/object?api-version=2026-08-26.preview#v2_us_bank_account_object) |
| `enabled_delivery_schemes` | Added | [V2.MoneyManagement.PayoutMethod.bank_account](/api/v2/money-management/payout-methods/object?api-version=2026-08-26.preview#v2_payout_method_object-bank_account) |
| `enabled_delivery_options` | Removed | [V2.MoneyManagement.PayoutMethod.bank_account](/api/v2/money-management/payout-methods/object?api-version=2026-08-26.preview#v2_payout_method_object-bank_account) |

#### Go

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `Restricted` | Added | [V2CoreVaultGbBankAccount](/api/v2/core/vault/gb-bank-accounts/object?api-version=2026-08-26.preview#v2_gb_bank_account_object), [V2CoreVaultUsBankAccount](/api/v2/core/vault/us-bank-accounts/object?api-version=2026-08-26.preview#v2_us_bank_account_object) |
| `EnabledDeliverySchemes` | Added | [V2MoneyManagementPayoutMethodBankAccount](/api/v2/money-management/payout-methods/object?api-version=2026-08-26.preview#v2_payout_method_object-bank_account) |
| `EnabledDeliveryOptions` | Removed | [V2MoneyManagementPayoutMethodBankAccount](/api/v2/money-management/payout-methods/object?api-version=2026-08-26.preview#v2_payout_method_object-bank_account) |

#### .NET

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `Restricted` | Added | [V2.Core.Vault.GbBankAccount](/api/v2/core/vault/gb-bank-accounts/object?api-version=2026-08-26.preview#v2_gb_bank_account_object), [V2.Core.Vault.UsBankAccount](/api/v2/core/vault/us-bank-accounts/object?api-version=2026-08-26.preview#v2_us_bank_account_object) |
| `EnabledDeliverySchemes` | Added | [V2.MoneyManagement.PayoutMethod.BankAccount](/api/v2/money-management/payout-methods/object?api-version=2026-08-26.preview#v2_payout_method_object-bank_account) |
| `EnabledDeliveryOptions` | Removed | [V2.MoneyManagement.PayoutMethod.BankAccount](/api/v2/money-management/payout-methods/object?api-version=2026-08-26.preview#v2_payout_method_object-bank_account) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2026-08-26.preview`
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

- [Removes support for specifying payment method types in Payment Intents and Setup Intents](https://docs.stripe.com/changelog/dahlia/2026-08-26/removes-payment-method-types-parameter-from-payment-intents-setup-intents.md)
