# Adds disabled reason to invoices, subscriptions, and schedules

## What’s new

Adds a `disabled_reason` field under `invoice.automatic_tax` on the [Invoice object](https://docs.stripe.com/api/invoices/object.md?api-version=2024-12-18.acacia#invoice_object-automatic_tax-disabled_reason), `subscription.automatic_tax` on the [Subscription object](https://docs.stripe.com/api/subscriptions/object.md?api-version=2024-12-18.acacia#subscription_object-automatic_tax-disabled_reason), and `subscription_schedule.default_settings.automatic_tax` along with `subscription_schedule.phases.automatic_tax` on the [Subscription Schedule object](https://docs.stripe.com/api/subscription_schedules/object.md?api-version=2024-12-18.acacia).

## Impact

This field allows you to identify when Stripe disabled automatic tax during invoice finalisation because of a missing or incomplete location for your customer.

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `disabled_reason` | Added | [Invoice.automatic_tax](/api/invoices/object?api-version=2024-12-18.acacia#invoice_object-automatic_tax), [Subscription.automatic_tax](/api/subscriptions/object?api-version=2024-12-18.acacia#subscription_object-automatic_tax), [SubscriptionSchedule.default_settings.automatic_tax](/api/subscription_schedules/object?api-version=2024-12-18.acacia#subscription_schedule_object-default_settings-automatic_tax), [SubscriptionSchedule.phases[].automatic_tax](/api/subscription_schedules/object?api-version=2024-12-18.acacia#subscription_schedule_object-phases-automatic_tax) |

#### Ruby

This change doesn’t affect the Ruby SDK.

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `disabled_reason` | Added | [stripe.Invoice.AutomaticTax](/api/invoices/object?api-version=2024-12-18.acacia#invoice_object-automatic_tax), [stripe.Subscription.AutomaticTax](/api/subscriptions/object?api-version=2024-12-18.acacia#subscription_object-automatic_tax), [stripe.SubscriptionSchedule.DefaultSettings.AutomaticTax](/api/subscription_schedules/object?api-version=2024-12-18.acacia#subscription_schedule_object-default_settings-automatic_tax), [stripe.SubscriptionSchedule.Phase.AutomaticTax](/api/subscription_schedules/object?api-version=2024-12-18.acacia#subscription_schedule_object-phases-automatic_tax) |

#### PHP

This change doesn’t affect the PHP SDK.

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `disabled_reason` | Added | [Invoice.automatic_tax](/api/invoices/object?api-version=2024-12-18.acacia#invoice_object-automatic_tax), [Subscription.automatic_tax](/api/subscriptions/object?api-version=2024-12-18.acacia#subscription_object-automatic_tax), [SubscriptionSchedule.default_settings.automatic_tax](/api/subscription_schedules/object?api-version=2024-12-18.acacia#subscription_schedule_object-default_settings-automatic_tax), [SubscriptionSchedule.phases[].automatic_tax](/api/subscription_schedules/object?api-version=2024-12-18.acacia#subscription_schedule_object-phases-automatic_tax) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `disabled_reason` | Added | [Invoice.automatic_tax](/api/invoices/object?api-version=2024-12-18.acacia#invoice_object-automatic_tax), [Subscription.automatic_tax](/api/subscriptions/object?api-version=2024-12-18.acacia#subscription_object-automatic_tax), [SubscriptionSchedule.default_settings.automatic_tax](/api/subscription_schedules/object?api-version=2024-12-18.acacia#subscription_schedule_object-default_settings-automatic_tax), [SubscriptionSchedule.phases[].automatic_tax](/api/subscription_schedules/object?api-version=2024-12-18.acacia#subscription_schedule_object-phases-automatic_tax) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `DisabledReason` | Added | [InvoiceAutomaticTax](/api/invoices/object?api-version=2024-12-18.acacia#invoice_object-automatic_tax), [SubscriptionAutomaticTax](/api/subscriptions/object?api-version=2024-12-18.acacia#subscription_object-automatic_tax), [SubscriptionScheduleDefaultSettingsAutomaticTax](/api/subscription_schedules/object?api-version=2024-12-18.acacia#subscription_schedule_object-default_settings-automatic_tax), [SubscriptionSchedulePhasesAutomaticTax](/api/subscription_schedules/object?api-version=2024-12-18.acacia#subscription_schedule_object-phases-automatic_tax) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `DisabledReason` | Added | [InvoiceAutomaticTax](/api/invoices/object?api-version=2024-12-18.acacia#invoice_object-automatic_tax), [SubscriptionAutomaticTax](/api/subscriptions/object?api-version=2024-12-18.acacia#subscription_object-automatic_tax), [SubscriptionScheduleDefaultSettingsAutomaticTax](/api/subscription_schedules/object?api-version=2024-12-18.acacia#subscription_schedule_object-default_settings-automatic_tax), [SubscriptionSchedulePhasesAutomaticTax](/api/subscription_schedules/object?api-version=2024-12-18.acacia#subscription_schedule_object-phases-automatic_tax) |

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

- [Adds support for tax ID types in 19 new countries](https://docs.stripe.com/changelog/acacia/2024-12-18/tax-ids-19-new-countries.md)
- [Adds support for 21 new countries to the Tax Registration API](https://docs.stripe.com/changelog/acacia/2024-12-18/tax-registration-21-new-countries.md)
