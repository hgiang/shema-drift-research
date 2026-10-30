# Adds account balance and payout settings with the Balance Settings API

## What’s new

You can now customise how a connected account’s balance and payout are managed by your platform with the [Balance Settings API](https://docs.stripe.com/api/balance-settings.md?api-version=2025-09-30.clover). These options are included:

- [payments.debit_negative_balances](https://docs.stripe.com/api/balance-settings/object.md?api-version=2025-09-30.clover#balance_settings_object-payments-debit_negative_balances): determines whether Stripe should try to reclaim negative balances from an attached bank account.
- [payments.payouts.minimum_balance_by_currency](https://docs.stripe.com/api/balance-settings/object.md?api-version=2025-09-30.clover#balance_settings_object-payments-payouts-minimum_balance_by_currency): defines the minimum balance amount to retain per currency after automatic payouts – only funds in excess of that currency are paid out.
- [payments.payouts.schedule](https://docs.stripe.com/api/balance-settings/object.md?api-version=2025-09-30.clover#balance_settings_object-payments-payouts-schedule): specifies the precise schedule for payouts, including the frequency interval and days of the month or week.
- [payments.payouts.statement_descriptor](https://docs.stripe.com/api/balance-settings/object.md?api-version=2025-09-30.clover#balance_settings_object-payments-payouts-statement_descriptor): specifies the text that appears on the bank account statement for payouts.
- [payments.settlement_timing](https://docs.stripe.com/api/balance-settings/object.md?api-version=2025-09-30.clover&rds=1&lang=curl#balance_settings_object-payments-settlement_timing): defines settlement timing for pending funds to become available.

If you used the Balance Settings API on [preview API versions earlier than 2025-09-30.clover](https://docs.stripe.com/api/balance-settings.md?api-version=2025-08-27.preview), you’ll notice the following changes:

- The ability to set the Balance Settings [delay_days](https://docs.stripe.com/api/balance-settings/object.md?api-version=2025-09-30.preview#balance_settings_object-payments-settlement_timing-delay_days) to default by posting an empty `delay_days_override` value. The default value is the lowest available for your account.

- The [delay_days_override](https://docs.stripe.com/api/balance-settings/object.md?api-version=2025-09-30.clover#balance_settings_object-payments-settlement_timing-delay_days_override) field added to the [Balance Settings object](https://docs.stripe.com/api/balance-settings.md?api-version=2025-09-30.clover), which you can set when you [update Balance Settings](https://docs.stripe.com/api/balance-settings/update.md?api-version=2025-09-30.clover).

#### REST API

| Field | Change | From → to |
| --- | --- | --- |
| `BalanceSettings#update.payments.settlement_timing.delay_days_override` | Changed | `longInteger → emptyable(longInteger)` |

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `delay_days_override` | Added | [BalanceSettings.payments.settlement_timing](/api/balance-settings/object?api-version=2025-09-30.preview#balance_settings_object-payments-settlement_timing) |

#### Ruby

| Field | Change | From → to |
| --- | --- | --- |
| `BalanceSettings::UpdateParams::Payment::SettlementTiming.delay_days_override` | Changed | `longInteger → emptyable(longInteger)` |

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `delay_days_override` | Added | [BalanceSettings::Payment::SettlementTiming](/api/balance-settings/object?api-version=2025-09-30.preview#balance_settings_object-payments-settlement_timing) |

#### Python

| Field | Change | From → to |
| --- | --- | --- |
| `BalanceSettings.ModifyParamsPaymentSettlementTiming.delay_days_override` | Changed | `longInteger → emptyable(longInteger)` |

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `delay_days_override` | Added | [BalanceSettings.Payment.SettlementTiming](/api/balance-settings/object?api-version=2025-09-30.preview#balance_settings_object-payments-settlement_timing) |

#### PHP

| Field | Change | From → to |
| --- | --- | --- |
| `BalanceSettings.update().$params.payment.settlement_timing.delay_days_override` | Changed | `longInteger → emptyable(longInteger)` |

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `delay_days_override` | Added | [BalanceSettings.payments.settlement_timing](/api/balance-settings/object?api-version=2025-09-30.preview#balance_settings_object-payments-settlement_timing) |

#### Java

| Field | Change | From → to |
| --- | --- | --- |
| `BalanceSettingsUpdateParams.payments.settlement_timing.delayDaysOverride` | Changed | `longInteger → emptyable(longInteger)` |

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `delayDaysOverride` | Added | [BalanceSettings.payments.settlement_timing](/api/balance-settings/object?api-version=2025-09-30.preview#balance_settings_object-payments-settlement_timing) |

#### Node.js

| Field | Change | From → to |
| --- | --- | --- |
| `BalanceSettingUpdateParams.payments.settlement_timing.delay_days_override` | Changed | `longInteger → emptyable(longInteger)` |

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `delay_days_override` | Added | [BalanceSettings.payments.settlement_timing](/api/balance-settings/object?api-version=2025-09-30.preview#balance_settings_object-payments-settlement_timing) |

#### Go

| Field | Change | From → to |
| --- | --- | --- |
| `BalanceSettingsPaymentsSettlementTimingParams.DelayDaysOverride` | Changed | `longInteger → emptyable(longInteger)` |

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `DelayDaysOverride` | Added | [BalanceSettingsPaymentsSettlementTiming](/api/balance-settings/object?api-version=2025-09-30.preview#balance_settings_object-payments-settlement_timing) |

#### .NET

| Field | Change | From → to |
| --- | --- | --- |
| `BalanceSettingsPaymentsSettlementTimingOptions.DelayDaysOverride` | Changed | `longInteger → emptyable(longInteger)` |

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `DelayDaysOverride` | Added | [BalanceSettings.Payments.SettlementTiming](/api/balance-settings/object?api-version=2025-09-30.preview#balance_settings_object-payments-settlement_timing) |

## Impact

All Stripe platforms can now use the [Balance Settings API](https://docs.stripe.com/api/balance-settings.md?api-version=2025-09-30.clover) to customise account balances, configure [minimum balances for automatic payouts](https://docs.stripe.com/payouts/minimum-balances-for-automatic-payouts.md) and [manage payout settings](https://docs.stripe.com/connect/manage-payout-schedule.md).

We recommend using the [Balance Settings API](https://docs.stripe.com/api/balance-settings.md?api-version=2025-09-30.clover) for both Accounts v1 and Accounts v2 over the legacy [settings.payouts](https://docs.stripe.com/api/accounts/object.md?api-version=2025-09-30.clover#account_object-settings-payouts) hash in the [Accounts v1 API](https://docs.stripe.com/api/accounts.md?api-version=2025-09-30.clover) However, if you’re a platform on Accounts v1 and currently using `settings.payouts`, you don’t need to migrate. If you’re a platform on [Accounts v2](https://docs.stripe.com/connect/accounts-v2.md), see [Build a SaaS platform](https://docs.stripe.com/connect/saas.md) to learn more.

## Changes

#### REST API

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [BalanceSettings](/api/balance-settings/object?api-version=2025-09-30.clover) |

| Endpoints | Change | Resource |
| --- | --- | --- |
| `retrieve`, `update` | Added | [BalanceSettings](/api/balance-settings/object?api-version=2025-09-30.clover) |

#### Ruby

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [BalanceSettings](/api/balance-settings/object?api-version=2025-09-30.clover) |

| Methods | Change | Resource |
| --- | --- | --- |
| `retrieve`, `update` | Added | [BalanceSettings](/api/balance-settings/object?api-version=2025-09-30.clover) |

#### Python

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [BalanceSettings](/api/balance-settings/object?api-version=2025-09-30.clover) |

| Methods | Change | Resource |
| --- | --- | --- |
| `modify`, `retrieve` | Added | [BalanceSettings](/api/balance-settings/object?api-version=2025-09-30.clover) |

#### PHP

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [BalanceSettings](/api/balance-settings/object?api-version=2025-09-30.clover) |

| Methods | Change | Resource |
| --- | --- | --- |
| `retrieve`, `update` | Added | [BalanceSettings](/api/balance-settings/object?api-version=2025-09-30.clover) |

#### Java

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [BalanceSettings](/api/balance-settings/object?api-version=2025-09-30.clover) |

| Methods | Change | Resource |
| --- | --- | --- |
| `retrieve`, `update` | Added | [BalanceSettings](/api/balance-settings/object?api-version=2025-09-30.clover) |

#### Node.js

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [BalanceSettings](/api/balance-settings/object?api-version=2025-09-30.clover) |

| Methods | Change | Resource |
| --- | --- | --- |
| `retrieve`, `update` | Added | [BalanceSettings](/api/balance-settings/object?api-version=2025-09-30.clover) |

#### Go

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [BalanceSettings](/api/balance-settings/object?api-version=2025-09-30.clover) |

| Methods | Change | Resource |
| --- | --- | --- |
| `Get`, `Update` | Added | [BalanceSettings](/api/balance-settings/object?api-version=2025-09-30.clover) |

#### .NET

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [BalanceSettings](/api/balance-settings/object?api-version=2025-09-30.clover) |

| Methods | Change | Resource |
| --- | --- | --- |
| `Get`, `Update` | Added | [BalanceSettings](/api/balance-settings/object?api-version=2025-09-30.clover) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2025-09-30.clover`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to [v16.0.0](https://github.com/stripe/stripe-ruby/releases/tag/v16.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to [v13.0.1](https://github.com/stripe/stripe-python/releases/tag/v13.0.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to [v18.0.0](https://github.com/stripe/stripe-php/releases/tag/v18.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to [v30.0.0](https://github.com/stripe/stripe-java/releases/tag/v30.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to [v19.1.0](https://github.com/stripe/stripe-node/releases/tag/v19.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to [v83.0.0](https://github.com/stripe/stripe-go/releases/tag/v83.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to [v49.0.0](https://github.com/stripe/stripe-dotnet/releases/tag/v49.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

## Related changes

- [Adds specific descriptions for risk requirements during legal, PEP and sanctions review](https://docs.stripe.com/changelog/clover/2025-09-30/expanded-risk-requirement-descriptions.md)
- [Adds a new error code for business type validations](https://docs.stripe.com/changelog/clover/2025-09-30/business-type-error-code.md)
