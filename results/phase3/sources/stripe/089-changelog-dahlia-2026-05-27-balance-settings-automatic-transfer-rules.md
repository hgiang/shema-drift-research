# Adds automatic transfer rules to balance settings

## What’s new

You can now configure per-currency rules for automatically transferring funds from your payments balance to a [Financial Account](https://docs.stripe.com/api/treasury/financial_accounts.md?api-version=2026-05-27.dahlia) using the new [automatic_transfer_rules_by_currency](https://docs.stripe.com/api/balance-settings/object.md?api-version=2026-05-27.dahlia#balance_settings_object-payments-payouts-automatic_transfer_rules_by_currency) parameter on the [Balance Settings](https://docs.stripe.com/api/balance-settings/object.md?api-version=2026-05-27.dahlia) object.

The automatic transfer rules support two types:

- `transfer_all`: Transfers all available funds to the specified Financial Account
- `transfer_up_to_amount`: Transfers up to a specified maximum amount to the Financial Account

You can configure different rules for USD, GBP and EUR currencies. Each rule specifies a [payout_method](https://docs.stripe.com/api/balance-settings/object.md?api-version=2026-05-27.dahlia#balance_settings_object-payments-payouts-automatic_transfer_rules_by_currency-%3Ccurrency%3E.payout_method) that identifies the Financial Account where funds are transferred.

## Impact

You can now programmatically configure automatic transfers from your payments balance to a Financial Account through the API instead of using the Dashboard. This enables you to automate fund distribution as part of your platform’s account setup and management flows.

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `automatic_transfer_rules_by_currency` | Added | [BalanceSettings#update.payments.payouts](/api/balance-settings/update?api-version=2026-05-27.dahlia#update_balance_settings-payments-payouts), [BalanceSettings.payments.payouts](/api/balance-settings/object?api-version=2026-05-27.dahlia#balance_settings_object-payments-payouts) |

#### Ruby

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `automatic_transfer_rules_by_currency` | Added | [BalanceSettings::Payment::Payout](/api/balance-settings/object?api-version=2026-05-27.dahlia#balance_settings_object-payments-payouts), [BalanceSettingsUpdateParams::Payment::Payout](/api/balance-settings/update?api-version=2026-05-27.dahlia#update_balance_settings-payments-payouts) |

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `automatic_transfer_rules_by_currency` | Added | [BalanceSettings.Payment.Payout](/api/balance-settings/object?api-version=2026-05-27.dahlia#balance_settings_object-payments-payouts), [BalanceSettingsModifyParamsPaymentPayout](/api/balance-settings/update?api-version=2026-05-27.dahlia#update_balance_settings-payments-payouts) |

#### PHP

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `automatic_transfer_rules_by_currency` | Added | [BalanceSettings.payments.payouts](/api/balance-settings/object?api-version=2026-05-27.dahlia#balance_settings_object-payments-payouts), [BalanceSettings.update().$params.payment.payout](/api/balance-settings/update?api-version=2026-05-27.dahlia#update_balance_settings-payments-payouts) |

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `automaticTransferRulesByCurrency` | Added | [BalanceSettings.payments.payouts](/api/balance-settings/object?api-version=2026-05-27.dahlia#balance_settings_object-payments-payouts), [BalanceSettingsUpdateParams.payments.payouts](/api/balance-settings/update?api-version=2026-05-27.dahlia#update_balance_settings-payments-payouts) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `automatic_transfer_rules_by_currency` | Added | [BalanceSettingUpdateParams.payments.payouts](/api/balance-settings/update?api-version=2026-05-27.dahlia#update_balance_settings-payments-payouts), [BalanceSettings.payments.payouts](/api/balance-settings/object?api-version=2026-05-27.dahlia#balance_settings_object-payments-payouts) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `AutomaticTransferRulesByCurrency` | Added | [BalanceSettingsPaymentsPayouts](/api/balance-settings/object?api-version=2026-05-27.dahlia#balance_settings_object-payments-payouts), [BalanceSettingsPaymentsPayoutsParams](/api/balance-settings/update?api-version=2026-05-27.dahlia#update_balance_settings-payments-payouts) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `AutomaticTransferRulesByCurrency` | Added | [BalanceSettings.Payments.Payouts](/api/balance-settings/object?api-version=2026-05-27.dahlia#balance_settings_object-payments-payouts), [BalanceSettingsPaymentsPayoutsOptions](/api/balance-settings/update?api-version=2026-05-27.dahlia#update_balance_settings-payments-payouts) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2026-05-27.dahlia`
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

- [Adds digital attestation support to Accounts v2 for proof of registration and beneficial ownership verification](https://docs.stripe.com/changelog/dahlia/2026-05-27/digital-attestation-accounts-v2.md)
- [Adds the ability to configure custom start of day per connected account](https://docs.stripe.com/changelog/dahlia/2026-05-27/custom-start-of-day.md)
