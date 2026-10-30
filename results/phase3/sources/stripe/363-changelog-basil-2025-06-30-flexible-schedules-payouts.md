# Adds more flexible schedules for monthly and weekly payouts

## What’s new

The payout schedule for an [Account](https://docs.stripe.com/api/accounts/object.md?api-version=2025-06-30.basil) is defined in [settings.payouts.schedule](https://docs.stripe.com/api/accounts/object.md?api-version=2025-06-30.basil#account_object-settings-payouts-schedule).

- If the `interval` is `monthly`, you can now specify when a payout should happen using [monthly_payout_days](https://docs.stripe.com/api/accounts/object.md?api-version=2025-06-30.basil#account_object-settings-payouts-schedule-monthly_payout_days).
- If the `interval` is `weekly`, you can now specify when a payout should happen using [weekly_payout_days](https://docs.stripe.com/api/accounts/object.md?api-version=2025-06-30.basil#account_object-settings-payouts-schedule-monthly_payout_days).

## Impact

You can now customise your payout schedule by selecting multiple payout days in a week or month. This gives you fine-grained control over when you receive your payouts.

## Changes

#### REST API

| Parameters | Change | Resources or endpoints |
| --- | --- | --- |
| `monthly_payout_days`, `weekly_payout_days` | Added | [Account#create.settings.payouts.schedule](/api/accounts/object?api-version=2025-06-30.basil#account_object-settings-payouts-schedule), [Account#update.settings.payouts.schedule](/api/accounts/object?api-version=2025-06-30.basil#account_object-settings-payouts-schedule), [Account.settings.payouts.schedule](/api/accounts/object?api-version=2025-06-30.basil#account_object-settings-payouts-schedule) |

#### Ruby

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `monthly_payout_days`, `weekly_payout_days` | Added | [Account::CreateParams::Setting::Payout::Schedule](/api/accounts/object?api-version=2025-06-30.basil#account_object-settings-payouts-schedule), [Account::Setting::Payout::Schedule](/api/accounts/object?api-version=2025-06-30.basil#account_object-settings-payouts-schedule), [Account::UpdateParams::Setting::Payout::Schedule](/api/accounts/object?api-version=2025-06-30.basil#account_object-settings-payouts-schedule) |

#### Python

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `monthly_payout_days`, `weekly_payout_days` | Added | [Account.CreateParamsSettingPayoutSchedule](/api/accounts/object?api-version=2025-06-30.basil#account_object-settings-payouts-schedule), [Account.ModifyParamsSettingPayoutSchedule](/api/accounts/object?api-version=2025-06-30.basil#account_object-settings-payouts-schedule), [Account.Setting.Payout.Schedule](/api/accounts/object?api-version=2025-06-30.basil#account_object-settings-payouts-schedule) |

#### PHP

This change doesn’t affect the PHP SDK.

#### Java

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `monthlyPayoutDays`, `weeklyPayoutDays` | Added | [Account.settings.payouts.schedule](/api/accounts/object?api-version=2025-06-30.basil#account_object-settings-payouts-schedule), [AccountCreateParams.settings.payouts.schedule](/api/accounts/object?api-version=2025-06-30.basil#account_object-settings-payouts-schedule), [AccountUpdateParams.settings.payouts.schedule](/api/accounts/object?api-version=2025-06-30.basil#account_object-settings-payouts-schedule) |

#### Node.js

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `monthly_payout_days`, `weekly_payout_days` | Added | [Account.settings.payouts.schedule](/api/accounts/object?api-version=2025-06-30.basil#account_object-settings-payouts-schedule), [AccountCreateParams.settings.payouts.schedule](/api/accounts/object?api-version=2025-06-30.basil#account_object-settings-payouts-schedule), [AccountUpdateParams.settings.payouts.schedule](/api/accounts/object?api-version=2025-06-30.basil#account_object-settings-payouts-schedule) |

#### Go

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `MonthlyPayoutDays`, `WeeklyPayoutDays` | Added | [AccountSettingsPayoutsSchedule](/api/accounts/object?api-version=2025-06-30.basil#account_object-settings-payouts-schedule), [AccountSettingsPayoutsScheduleParams](/api/accounts/object?api-version=2025-06-30.basil#account_object-settings-payouts-schedule) |

#### .NET

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `MonthlyPayoutDays`, `WeeklyPayoutDays` | Added | [Account.Settings.Payouts.Schedule](/api/accounts/object?api-version=2025-06-30.basil#account_object-settings-payouts-schedule), [AccountSettingsPayoutsScheduleOptions](/api/accounts/object?api-version=2025-06-30.basil#account_object-settings-payouts-schedule) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2025-06-30.basil`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to [v15.3.0](https://github.com/stripe/stripe-ruby/releases/tag/v15.3.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to [v12.3.0](https://github.com/stripe/stripe-python/releases/tag/v12.3.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to [v17.4.0](https://github.com/stripe/stripe-php/releases/tag/v17.4.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to [v29.3.0](https://github.com/stripe/stripe-java/releases/tag/v29.3.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to [v18.3.0](https://github.com/stripe/stripe-node/releases/tag/v18.3.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to [v82.3.0](https://github.com/stripe/stripe-go/releases/tag/v82.3.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to [v48.3.0](https://github.com/stripe/stripe-dotnet/releases/tag/v48.3.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

## Related changes

- [Verification Sessions can now collect verification information for a related Person](https://docs.stripe.com/changelog/basil/2025-06-30/identity-related-person.md)
- [Adds the ability to provide proof-of-address documents for connected accounts](https://docs.stripe.com/changelog/basil/2025-06-30/accounts-proof-of-address.md)
