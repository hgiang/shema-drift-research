# Adds support for Japan and China as Global Payouts cross-border payout destinations

## What’s new

Adds support for [Global Payouts](https://docs.stripe.com/global-payouts.md) recipient bank accounts in Japan and China. It also adds the following values for those countries to the read-only [default_outbound_destination](https://docs.stripe.com/api/v2/core/accounts/object.md?api-version=2026-04-22.preview#v2_account_object-configuration-recipient-default_outbound_destination-type) enum on the [Account v2](https://docs.stripe.com/api/v2/core/accounts/object.md?api-version=2026-04-22.preview) object’s `recipient` configuration:

- `jp_bank_account`: Japan
- `cn_bank_account`: China

This release also adds two possible bank account type values `futsu` and `toza` that are specific to Japanese bank accounts.

## Why is this a breaking change?

Japanese bank accounts take on bank account types `futsu` or `toza`, while every other country bank account takes on `checking` or `savings`. Upgrading to this version would require accounting for the possibility of these two new values being returned through the [bank_account_type](https://docs.stripe.com/api/v2/money-management/payout-methods/object.md?api-version=2026-04-22.preview#v2_payout_method_object-bank_account-bank_account_type) field on the Payout Method.

## Impact

Your recipients in these two countries can now create bank accounts to prepare for receiving cross-border payouts using Global Payouts. You can use [OutboundSetupIntents](https://docs.stripe.com/api/v2/money-management/outbound-setup-intents.md?api-version=2026-04-22.preview) to create the bank accounts and [OutboundPayments](https://docs.stripe.com/api/v2/money-management/outbound-payments.md?api-version=2026-04-22.preview) to send the payouts. These bank accounts can also serve as the default outbound destination on the recipient accounts.

## Changes

#### REST API

| Values | Change | Enums |
| --- | --- | --- |
| `cn_bank_account`, `jp_bank_account` | Added | [V2.Core.Account.configuration.recipient.default_outbound_destination](/api/v2/core/accounts/object?api-version=2026-04-22.preview#v2_account_object-configuration-recipient-default_outbound_destination-type) |
| `futsu`, `toza` | Added | [V2.Core.Vault.GbBankAccount](/api/v2/core/vault/gb-bank-accounts/object?api-version=2026-04-22.preview#v2_gb_bank_account_object-bank_account_type), [V2.Core.Vault.GbBankAccount#create](/api/v2/core/vault/gb-bank-accounts/create?api-version=2026-04-22.preview#v2_create_gb_bank_accounts-bank_account_type), [V2.MoneyManagement.PayoutMethod.bank_account](/api/v2/money-management/payout-methods/object?api-version=2026-04-22.preview#v2_payout_method_object-bank_account-bank_account_type), [V2.MoneyManagement.OutboundSetupIntent#create.payout_method_data.bank_account](/api/v2/money-management/outbound-setup-intents/create?api-version=2026-04-22.preview#v2_create_outbound_setup_intents-payout_method_data-bank_account-bank_account_type), [V2.MoneyManagement.OutboundSetupIntent#update.payout_method_data.bank_account](/api/v2/money-management/outbound-setup-intents/update?api-version=2026-04-22.preview#v2_update_outbound_setup_intents-payout_method_data-bank_account-bank_account_type) |

#### Ruby

This change doesn’t affect the Ruby SDK.

#### Python

| Values | Change | Enums |
| --- | --- | --- |
| `cn_bank_account`, `jp_bank_account` | Added | [V2.Core.Account.Configuration.Recipient.DefaultOutboundDestination](/api/v2/core/accounts/object?api-version=2026-04-22.preview#v2_account_object-configuration-recipient-default_outbound_destination-type) |
| `futsu`, `toza` | Added | [V2.Core.Vault.GbBankAccount](/api/v2/core/vault/gb-bank-accounts/object?api-version=2026-04-22.preview#v2_gb_bank_account_object-bank_account_type), [v2.core.vault.GbBankAccountCreateParams](/api/v2/core/vault/gb-bank-accounts/create?api-version=2026-04-22.preview#v2_create_gb_bank_accounts-bank_account_type), [V2.MoneyManagement.PayoutMethod.BankAccount](/api/v2/money-management/payout-methods/object?api-version=2026-04-22.preview#v2_payout_method_object-bank_account-bank_account_type), [v2.money_management.OutboundSetupIntentCreateParamsPayoutMethodDatumBankAccount](/api/v2/money-management/outbound-setup-intents/create?api-version=2026-04-22.preview#v2_create_outbound_setup_intents-payout_method_data-bank_account-bank_account_type), [v2.money_management.OutboundSetupIntentModifyParamsPayoutMethodDatumBankAccount](/api/v2/money-management/outbound-setup-intents/update?api-version=2026-04-22.preview#v2_update_outbound_setup_intents-payout_method_data-bank_account-bank_account_type) |

#### PHP

| Values | Change | Enums |
| --- | --- | --- |
| `cn_bank_account`, `jp_bank_account` | Added | [V2.Core.Account.configuration.recipient.default_outbound_destination](/api/v2/core/accounts/object?api-version=2026-04-22.preview#v2_account_object-configuration-recipient-default_outbound_destination-type) |
| `futsu`, `toza` | Added | [V2.Core.Vault.GbBankAccount](/api/v2/core/vault/gb-bank-accounts/object?api-version=2026-04-22.preview#v2_gb_bank_account_object-bank_account_type), [V2.MoneyManagement.PayoutMethod.bank_account](/api/v2/money-management/payout-methods/object?api-version=2026-04-22.preview#v2_payout_method_object-bank_account-bank_account_type) |

#### Java

| Values | Change | Enums |
| --- | --- | --- |
| `futsu`, `toza` | Added | [v2.core.vault.GbBankAccountCreateParams](/api/v2/core/vault/gb-bank-accounts/create?api-version=2026-04-22.preview#v2_create_gb_bank_accounts-bankAccountType), [v2.moneymanagement.OutboundSetupIntentCreateParams.payout_method_data.bank_account](/api/v2/money-management/outbound-setup-intents/create?api-version=2026-04-22.preview#v2_create_outbound_setup_intents-payout_method_data-bank_account-bankAccountType), [v2.moneymanagement.OutboundSetupIntentUpdateParams.payout_method_data.bank_account](/api/v2/money-management/outbound-setup-intents/update?api-version=2026-04-22.preview#v2_update_outbound_setup_intents-payout_method_data-bank_account-bankAccountType) |

#### Node.js

| Values | Change | Enums |
| --- | --- | --- |
| `cn_bank_account`, `jp_bank_account` | Added | [V2.Core.Account.configuration.recipient.default_outbound_destination](/api/v2/core/accounts/object?api-version=2026-04-22.preview#v2_account_object-configuration-recipient-default_outbound_destination-type) |
| `futsu`, `toza` | Added | [V2.Core.Vault.GbBankAccount](/api/v2/core/vault/gb-bank-accounts/object?api-version=2026-04-22.preview#v2_gb_bank_account_object-bank_account_type), [V2.Core.Vault.GbBankAccountCreateParams](/api/v2/core/vault/gb-bank-accounts/create?api-version=2026-04-22.preview#v2_create_gb_bank_accounts-bank_account_type), [V2.MoneyManagement.PayoutMethod.bank_account](/api/v2/money-management/payout-methods/object?api-version=2026-04-22.preview#v2_payout_method_object-bank_account-bank_account_type), [V2.MoneyManagement.OutboundSetupIntentCreateParams.payout_method_data.bank_account](/api/v2/money-management/outbound-setup-intents/create?api-version=2026-04-22.preview#v2_create_outbound_setup_intents-payout_method_data-bank_account-bank_account_type), [V2.MoneyManagement.OutboundSetupIntentUpdateParams.payout_method_data.bank_account](/api/v2/money-management/outbound-setup-intents/update?api-version=2026-04-22.preview#v2_update_outbound_setup_intents-payout_method_data-bank_account-bank_account_type) |

#### Go

| Values | Change | Enums |
| --- | --- | --- |
| `cn_bank_account`, `jp_bank_account` | Added | [V2CoreAccountConfigurationRecipientDefaultOutboundDestination](/api/v2/core/accounts/object?api-version=2026-04-22.preview#v2_account_object-configuration-recipient-default_outbound_destination-Type) |
| `futsu`, `toza` | Added | [V2CoreVaultGbBankAccount](/api/v2/core/vault/gb-bank-accounts/object?api-version=2026-04-22.preview#v2_gb_bank_account_object-BankAccountType), [V2MoneyManagementPayoutMethodBankAccount](/api/v2/money-management/payout-methods/object?api-version=2026-04-22.preview#v2_payout_method_object-bank_account-BankAccountType) |

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

## Related changes

- [Adds credential reuse for Global Payouts with Accounts v2](https://docs.stripe.com/changelog/dahlia/2026-04-22/credential-reuse-with-accounts-v2.md)
