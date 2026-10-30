# Updates schedule customisation for weekly and monthly payouts

## What’s new

You can now configure more precise weekly or monthly payout schedules through the [Balance Settings API](https://docs.stripe.com/api/balance-settings/object.md?api-version=2025-06-30.preview). Previously, you could only choose one day of the week or month for a payout.

- We’ve renamed `monthly_anchor` to [monthly_payouts_days](https://docs.stripe.com/api/balance-settings/object.md?api-version=2025-07-30.preview#balance_settings_object-payouts-schedule-monthly_payout_days), which can now configure multiple days of the month for payouts.

- We’ve renamed `weekly_anchor` to [weekly_payouts_days](https://docs.stripe.com/api/balance-settings/object.md?api-version=2025-07-30.preview#balance_settings_object-payouts-schedule-weekly_payout_days), which can now configure multiple days of the week for payouts.

## Why is this a breaking change?

The `weekly_anchor` and `monthly_anchor` fields have been replaced with `weekly_payouts_days` and `monthly_payout_days`, respectively.

## Impact

If you participate in the [Accounts v2 API](https://docs.stripe.com/connect/accounts-v2.md) public preview and want to use API version `2025-07-30.preview` or later, update your balance settings integration to use the `weekly_payout_days` or `monthly_payout_days` fields.

## Changes

#### REST API

| Parameters | Change | Resources or endpoints |
| --- | --- | --- |
| `monthly_payout_days`, `weekly_payout_days` | Added | [BalanceSettings#update.payouts.schedule](/api/balance-settings/update?api-version=2025-07-30.preview#update_balance_settings-payouts-schedule), [BalanceSettings.payouts.schedule](/api/balance-settings/object?api-version=2025-07-30.preview#balance_settings_object-payouts-schedule) |
| `monthly_anchor`, `weekly_anchor` | Removed | [BalanceSettings#update.payouts.schedule](/api/balance-settings/update?api-version=2025-07-30.preview#update_balance_settings-payouts-schedule), [BalanceSettings.payouts.schedule](/api/balance-settings/object?api-version=2025-07-30.preview#balance_settings_object-payouts-schedule) |

#### Ruby

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `monthly_payout_days`, `weekly_payout_days` | Added | [BalanceSettings::Payout::Schedule](/api/balance-settings/object?api-version=2025-07-30.preview#balance_settings_object-payouts-schedule), [BalanceSettings::UpdateParams::Payout::Schedule](/api/balance-settings/update?api-version=2025-07-30.preview#update_balance_settings-payouts-schedule) |
| `monthly_anchor`, `weekly_anchor` | Removed | [BalanceSettings::Payout::Schedule](/api/balance-settings/object?api-version=2025-07-30.preview#balance_settings_object-payouts-schedule), [BalanceSettings::UpdateParams::Payout::Schedule](/api/balance-settings/update?api-version=2025-07-30.preview#update_balance_settings-payouts-schedule) |

#### Python

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `monthly_payout_days`, `weekly_payout_days` | Added | [BalanceSettings.ModifyParamsPayoutSchedule](/api/balance-settings/update?api-version=2025-07-30.preview#update_balance_settings-payouts-schedule), [BalanceSettings.Payout.Schedule](/api/balance-settings/object?api-version=2025-07-30.preview#balance_settings_object-payouts-schedule) |
| `monthly_anchor`, `weekly_anchor` | Removed | [BalanceSettings.ModifyParamsPayoutSchedule](/api/balance-settings/update?api-version=2025-07-30.preview#update_balance_settings-payouts-schedule), [BalanceSettings.Payout.Schedule](/api/balance-settings/object?api-version=2025-07-30.preview#balance_settings_object-payouts-schedule) |

#### PHP

This change doesn’t affect the PHP SDK.

#### Java

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `monthlyPayoutDays`, `weeklyPayoutDays` | Added | [BalanceSettings.payouts.schedule](/api/balance-settings/object?api-version=2025-07-30.preview#balance_settings_object-payouts-schedule), [BalanceSettingsUpdateParams.payouts.schedule](/api/balance-settings/update?api-version=2025-07-30.preview#update_balance_settings-payouts-schedule) |
| `monthlyAnchor`, `weeklyAnchor` | Removed | [BalanceSettings.payouts.schedule](/api/balance-settings/object?api-version=2025-07-30.preview#balance_settings_object-payouts-schedule), [BalanceSettingsUpdateParams.payouts.schedule](/api/balance-settings/update?api-version=2025-07-30.preview#update_balance_settings-payouts-schedule) |

#### Node.js

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `monthly_payout_days`, `weekly_payout_days` | Added | [BalanceSettingUpdateParams.payouts.schedule](/api/balance-settings/update?api-version=2025-07-30.preview#update_balance_settings-payouts-schedule), [BalanceSettings.payouts.schedule](/api/balance-settings/object?api-version=2025-07-30.preview#balance_settings_object-payouts-schedule) |
| `monthly_anchor`, `weekly_anchor` | Removed | [BalanceSettingUpdateParams.payouts.schedule](/api/balance-settings/update?api-version=2025-07-30.preview#update_balance_settings-payouts-schedule), [BalanceSettings.payouts.schedule](/api/balance-settings/object?api-version=2025-07-30.preview#balance_settings_object-payouts-schedule) |

#### Go

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `MonthlyPayoutDays`, `WeeklyPayoutDays` | Added | [BalanceSettingsPayoutsSchedule](/api/balance-settings/object?api-version=2025-07-30.preview#balance_settings_object-payouts-schedule), [BalanceSettingsPayoutsScheduleParams](/api/balance-settings/update?api-version=2025-07-30.preview#update_balance_settings-payouts-schedule) |
| `MonthlyAnchor`, `WeeklyAnchor` | Removed | [BalanceSettingsPayoutsSchedule](/api/balance-settings/object?api-version=2025-07-30.preview#balance_settings_object-payouts-schedule), [BalanceSettingsPayoutsScheduleParams](/api/balance-settings/update?api-version=2025-07-30.preview#update_balance_settings-payouts-schedule) |

#### .NET

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `MonthlyPayoutDays`, `WeeklyPayoutDays` | Added | [BalanceSettings.Payouts.Schedule](/api/balance-settings/object?api-version=2025-07-30.preview#balance_settings_object-payouts-schedule), [BalanceSettingsPayoutsScheduleOptions](/api/balance-settings/update?api-version=2025-07-30.preview#update_balance_settings-payouts-schedule) |
| `MonthlyAnchor`, `WeeklyAnchor` | Removed | [BalanceSettings.Payouts.Schedule](/api/balance-settings/object?api-version=2025-07-30.preview#balance_settings_object-payouts-schedule), [BalanceSettingsPayoutsScheduleOptions](/api/balance-settings/update?api-version=2025-07-30.preview#update_balance_settings-payouts-schedule) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2025-07-30.preview`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to [v15.5.0-beta.1](https://github.com/stripe/stripe-ruby/releases/tag/v15.5.0-beta.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to [v12.5.0b1](https://github.com/stripe/stripe-python/releases/tag/v12.5.0b1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to [v17.6.0-beta.1](https://github.com/stripe/stripe-php/releases/tag/v17.6.0-beta.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to [v29.5.0-beta.1](https://github.com/stripe/stripe-java/releases/tag/v29.5.0-beta.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to [v18.5.0-beta.1](https://github.com/stripe/stripe-node/releases/tag/v18.5.0-beta.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to [v82.5.0-beta.1](https://github.com/stripe/stripe-go/releases/tag/v82.5.0-beta.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to [v48.5.0-beta.1](https://github.com/stripe/stripe-dotnet/releases/tag/v48.5.0-beta.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

## Related changes

- [Adds Account Links v2 API support for connected accounts created using the Accounts v2 API](https://docs.stripe.com/changelog/basil/2025-07-30/enable-v2-account-links-api-for-connect.md)
- [Renames the parameter for custom settlement timing on the Balance Settings API](https://docs.stripe.com/changelog/basil/2025-07-30/balance-settings-delay-days-rename.md)
- [Adds Connect embedded component for Instant Payouts promotion](https://docs.stripe.com/changelog/basil/2025-07-30/instant-payouts-promotion-embedded-component.md)
