# Adds alternative reference field to bank account and payout method resources

## What’s new

You can now view and cross-reference [Payout Methods](https://docs.stripe.com/api/v2/money-management/payout-methods.md?api-version=2026-01-28.preview) coming from [External Accounts](https://docs.stripe.com/api/external_accounts.md?api-version=2026-01-28.preview) using the new [alternative_reference](https://docs.stripe.com/api/v2/money-management/payout-methods/object.md?api-version=2026-01-28.preview#v2_payout_method_object-alternative_reference) property. This property is available for the following resources:

- [GbBankAccount](https://docs.stripe.com/api/v2/core/vault/gb-bank-accounts.md?api-version=2026-01-28.preview#v2_gb_bank_account_object-alternative_reference)
- [UsBankAccount](https://docs.stripe.com/api/v2/core/vault/us-bank-accounts.md?api-version=2026-01-28.preview#v2_us_bank_account_object-alternative_reference)
- [PayoutMethod](https://docs.stripe.com/api/v2/money-management/payout-methods/object.md?api-version=2026-01-28.preview#v2_payout_method_object-alternative_reference)

The new `alternative_reference` property follows the format `{type: "external_account", id: "ba_123"}`, where the ID corresponds to the External Account identifier.

## Impact

You can use the `alternative_reference` property to trace a Payout Method back to its External Account and update the credential information as needed, without any changes to your existing integration code. This new property is read-only and automatically populates when credentials originate from External Accounts.

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `alternative_reference` | Added | [V2.Core.Vault.GbBankAccount](/api/v2/core/vault/gb-bank-accounts/object?api-version=2026-01-28.preview), [V2.Core.Vault.UsBankAccount](/api/v2/core/vault/us-bank-accounts/object?api-version=2026-01-28.preview), [V2.MoneyManagement.PayoutMethod](/api/v2/money-management/payout-methods/object?api-version=2026-01-28.preview) |

#### Ruby

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `alternative_reference` | Added | [V2::Core::Vault::GbBankAccount](/api/v2/core/vault/gb-bank-accounts/object?api-version=2026-01-28.preview), [V2::Core::Vault::UsBankAccount](/api/v2/core/vault/us-bank-accounts/object?api-version=2026-01-28.preview), [V2::MoneyManagement::PayoutMethod](/api/v2/money-management/payout-methods/object?api-version=2026-01-28.preview) |

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `alternative_reference` | Added | [V2.Core.Vault.GbBankAccount](/api/v2/core/vault/gb-bank-accounts/object?api-version=2026-01-28.preview), [V2.Core.Vault.UsBankAccount](/api/v2/core/vault/us-bank-accounts/object?api-version=2026-01-28.preview), [V2.MoneyManagement.PayoutMethod](/api/v2/money-management/payout-methods/object?api-version=2026-01-28.preview) |

#### PHP

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `alternative_reference` | Added | [V2.Core.Vault.GbBankAccount](/api/v2/core/vault/gb-bank-accounts/object?api-version=2026-01-28.preview), [V2.Core.Vault.UsBankAccount](/api/v2/core/vault/us-bank-accounts/object?api-version=2026-01-28.preview), [V2.MoneyManagement.PayoutMethod](/api/v2/money-management/payout-methods/object?api-version=2026-01-28.preview) |

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `alternativeReference` | Added | [v2.core.vault.GbBankAccount](/api/v2/core/vault/gb-bank-accounts/object?api-version=2026-01-28.preview), [v2.core.vault.UsBankAccount](/api/v2/core/vault/us-bank-accounts/object?api-version=2026-01-28.preview), [v2.moneymanagement.PayoutMethod](/api/v2/money-management/payout-methods/object?api-version=2026-01-28.preview) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `alternative_reference` | Added | [V2.Core.Vault.GbBankAccount](/api/v2/core/vault/gb-bank-accounts/object?api-version=2026-01-28.preview), [V2.Core.Vault.UsBankAccount](/api/v2/core/vault/us-bank-accounts/object?api-version=2026-01-28.preview), [V2.MoneyManagement.PayoutMethod](/api/v2/money-management/payout-methods/object?api-version=2026-01-28.preview) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `AlternativeReference` | Added | [V2CoreVaultGbBankAccount](/api/v2/core/vault/gb-bank-accounts/object?api-version=2026-01-28.preview), [V2CoreVaultUsBankAccount](/api/v2/core/vault/us-bank-accounts/object?api-version=2026-01-28.preview), [V2MoneyManagementPayoutMethod](/api/v2/money-management/payout-methods/object?api-version=2026-01-28.preview) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `AlternativeReference` | Added | [V2.Core.Vault.GbBankAccount](/api/v2/core/vault/gb-bank-accounts/object?api-version=2026-01-28.preview), [V2.Core.Vault.UsBankAccount](/api/v2/core/vault/us-bank-accounts/object?api-version=2026-01-28.preview), [V2.MoneyManagement.PayoutMethod](/api/v2/money-management/payout-methods/object?api-version=2026-01-28.preview) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2026-01-28.preview`
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

- [Updates error codes for the Outbound Setup Intents API](https://docs.stripe.com/changelog/clover/2026-01-28/outbound-setup-intents-error-codes.md)
- [Adds fingerprint property to card payout methods](https://docs.stripe.com/changelog/clover/2026-01-28/card-payout-methods-fingerprint-property.md)
- [Global Payouts adds support for 15 new countries for cross-border payouts](https://docs.stripe.com/changelog/clover/2026-01-28/cross-border-payouts-new-countries.md)
