# Adds a duration parameter for schedule phases

## What’s new

We introduced a new way to specify the length of a subscription schedule phase using the `duration` parameter to support mixed interval subscriptions. You can now define time-based durations for subscription schedule phases by length and interval type: `day`, `week`, `month`, `year`.

The `iterations` parameter is now marked as deprecated as `duration` replaces its functionality.

## Impact

You can now set the duration of a subscription schedule phase directly using the `duration` parameter in these following API endpoints:

- [Subscription Schedules Create](https://docs.stripe.com/api/subscription_schedules/create.md?api-version=2025-07-30.basil)
- [Subscription Schedules Update](https://docs.stripe.com/api/subscription_schedules/update.md?api-version=2025-07-30.basil)
- [Create an invoice preview](https://docs.stripe.com/api/invoices/create_preview.md?api-version=2025-07-30.basil)

Use `duration` instead of `iterations` to create or update mixed interval subscription schedules.

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `duration` | Added | [Invoice#create_preview.schedule_details.phases[]](/api/invoices/create_preview?api-version=2025-07-30.basil#create_create_preview-schedule_details-phases), [SubscriptionSchedule#create.phases[]](/api/subscription_schedules/create?api-version=2025-07-30.basil#create_subscription_schedule-phases), [SubscriptionSchedule#update.phases[]](/api/subscription_schedules/update?api-version=2025-07-30.basil#update_subscription_schedule-phases) |

#### Ruby

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `duration` | Added | [Invoice::CreatePreviewParams::ScheduleDetail::Phase](/api/invoices/create_preview?api-version=2025-07-30.basil#create_create_preview-schedule_details-phases), [SubscriptionSchedule::CreateParams::Phase](/api/subscription_schedules/create?api-version=2025-07-30.basil#create_subscription_schedule-phases), [SubscriptionSchedule::UpdateParams::Phase](/api/subscription_schedules/update?api-version=2025-07-30.basil#update_subscription_schedule-phases) |

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `duration` | Added | [Invoice.CreatePreviewParamsScheduleDetailPhase](/api/invoices/create_preview?api-version=2025-07-30.basil#create_create_preview-schedule_details-phases), [SubscriptionSchedule.CreateParamsPhase](/api/subscription_schedules/create?api-version=2025-07-30.basil#create_subscription_schedule-phases), [SubscriptionSchedule.ModifyParamsPhase](/api/subscription_schedules/update?api-version=2025-07-30.basil#update_subscription_schedule-phases) |

#### PHP

This change doesn’t affect the PHP SDK.

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `duration` | Added | [InvoiceCreatePreviewParams.schedule_details.phases[]](/api/invoices/create_preview?api-version=2025-07-30.basil#create_create_preview-schedule_details-phases), [SubscriptionScheduleCreateParams.phases[]](/api/subscription_schedules/create?api-version=2025-07-30.basil#create_subscription_schedule-phases), [SubscriptionScheduleUpdateParams.phases[]](/api/subscription_schedules/update?api-version=2025-07-30.basil#update_subscription_schedule-phases) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `duration` | Added | [InvoiceCreatePreviewParams.schedule_details.phases[]](/api/invoices/create_preview?api-version=2025-07-30.basil#create_create_preview-schedule_details-phases), [SubscriptionScheduleCreateParams.phases[]](/api/subscription_schedules/create?api-version=2025-07-30.basil#create_subscription_schedule-phases), [SubscriptionScheduleUpdateParams.phases[]](/api/subscription_schedules/update?api-version=2025-07-30.basil#update_subscription_schedule-phases) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `Duration` | Added | [InvoiceCreatePreviewScheduleDetailsPhaseParams](/api/invoices/create_preview?api-version=2025-07-30.basil#create_create_preview-schedule_details-phases), [SubscriptionSchedulePhaseParams](/api/subscription_schedules/create?api-version=2025-07-30.basil#create_subscription_schedule-phases) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `Duration` | Added | [InvoiceScheduleDetailsPhaseOptions](/api/invoices/create_preview?api-version=2025-07-30.basil#create_create_preview-schedule_details-phases), [SubscriptionSchedulePhaseOptions](/api/subscription_schedules/create?api-version=2025-07-30.basil#create_subscription_schedule-phases) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2025-07-30.basil`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to [v15.4.0](https://github.com/stripe/stripe-ruby/releases/tag/v15.4.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to [v12.4.0](https://github.com/stripe/stripe-python/releases/tag/v12.4.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to [v17.5.0](https://github.com/stripe/stripe-php/releases/tag/v17.5.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to [v29.4.0](https://github.com/stripe/stripe-java/releases/tag/v29.4.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to [v18.4.0](https://github.com/stripe/stripe-node/releases/tag/v18.4.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to [v82.4.0](https://github.com/stripe/stripe-go/releases/tag/v82.4.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to [v48.4.0](https://github.com/stripe/stripe-dotnet/releases/tag/v48.4.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

## Related changes

- [Adds support for quantity adjustment to the Customer Portal Configuration API](https://docs.stripe.com/changelog/basil/2025-07-30/customer-portal-subscription-update-quantity-limits.md)
- [Adds helpers to cancel subscriptions for billing periods with mixed intervals](https://docs.stripe.com/changelog/basil/2025-07-30/cancel-at-enums.md)
- [Adds support for billing thresholds on flexible billing mode Subscriptions](https://docs.stripe.com/changelog/basil/2025-07-30/billing-thresholds.md)
- [Adds support for mixed intervals on the same subscription](https://docs.stripe.com/changelog/basil/2025-07-30/support-mixed-intervals.md)
