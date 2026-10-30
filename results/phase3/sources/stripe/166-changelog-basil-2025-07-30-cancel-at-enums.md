# Adds helpers to cancel subscriptions for billing periods with mixed intervals

## What’s new

We introduced the following [cancel_at](https://docs.stripe.com/api/subscriptions/create.md?api-version=2025-07-30.basil#create_subscription-cancel_at) enum values to simplify cancelling a [mixed interval](https://docs.stripe.com/billing/subscriptions/mixed-interval.md) subscription at the end of a billing period:

- `min_period_end`: Schedules cancellation of the subscription at the earliest `items.data.current_period_end` across all subscription items.
- `max_period_end`: Schedules cancellation of the subscription at the latest `items.data.current_period_end` across all subscription items.

In requests that change both the `current_period_end` of a Subscription item and set one of these new values, the updated `current_period_end` is taken as the respective cancellation date. Unlike [cancel_at_period_end](https://docs.stripe.com/api/subscriptions/create.md?api-version=2025-07-30.basil#create_subscription-cancel_at_period_end), these values resolve to timestamps immediately and further changes to `items.data.current_period_end` don’t affect them.

> For mixed interval subscriptions the existing [cancel_at_period_end](https://docs.stripe.com/api/subscriptions/create.md?api-version=2025-07-30.basil#create_subscription-cancel_at_period_end) feature always resolves to the earliest item period end.

## Impact

The following API endpoints support the new enums:

- [Create a subscription](https://docs.stripe.com/api/subscriptions/create.md?api-version=2025-07-30.basil)
- [Update a subscription](https://docs.stripe.com/api/subscriptions/update.md?api-version=2025-07-30.basil)
- [Create an invoice preview](https://docs.stripe.com/api/invoices/create_preview.md?api-version=2025-07-30.basil)

If your flexible billing mode integration currently uses [cancel_at_period_end](https://docs.stripe.com/api/subscriptions/create.md?api-version=2025-07-30.basil#create_subscription-cancel_at_period_end) to cancel subscriptions, update your integration to either:

- Use the new `min_period_end` or `max_period_end` enum values to specify which interval triggers cancelation.
- Populate [cancel_at](https://docs.stripe.com/api/subscriptions/create.md?api-version=2025-07-30.basil#create_subscription-cancel_at) with an explicit integer timestamp.

The `cancel_at_period_end` parameter on a Subscription isn’t compatible with the new `cancel_at` helpers.

If you update the `current_period_end` value for items in a subscription, you can add `cancel_at: min_period_end` or `cancel_at: max_period_end` in the same request to reset the subscription’s existing [cancel_at](https://docs.stripe.com/api/subscriptions/object.md?api-version=2025-07-30.basil#subscription_object-cancel_at) timestamp.

> This change won’t be available in the .NET SDK until version `49.0.0` and the Java SDK until version `30.0.0`. Until those versions are available, follow the instructions to [send undocumented parameters](https://docs.stripe.com/sdks/server-side.md#undocumented-params-and-fields) to pass the new enum values to the `cancel_at` parameter.

## Changes

#### REST API

| Fields | Change | From → to |
| --- | --- | --- |
| `Invoice#create_preview.subscription_details.cancel_at`, `Subscription#create.cancel_at`, `Subscription#update.cancel_at` | Changed | `DateTime → DateTime | enum('max_period_end'|'min_period_end')` |

#### Ruby

| Fields | Change | From → to |
| --- | --- | --- |
| `Invoice::CreatePreviewParams::SubscriptionDetail.cancel_at`, `Subscription::CreateParams.cancel_at`, `Subscription::UpdateParams.cancel_at` | Changed | `DateTime → DateTime | enum('max_period_end'|'min_period_end')` |

#### Python

| Fields | Change | From → to |
| --- | --- | --- |
| `Invoice.CreatePreviewParamsSubscriptionDetail.cancel_at`, `Subscription.CreateParams.cancel_at`, `Subscription.ModifyParams.cancel_at` | Changed | `DateTime → DateTime | enum('max_period_end'|'min_period_end')` |

#### PHP

This change doesn’t affect the PHP SDK.

#### Java

| Fields | Change | From → to |
| --- | --- | --- |
| `InvoiceCreatePreviewParams.subscription_details.cancelAt`, `SubscriptionCreateParams.cancelAt`, `SubscriptionUpdateParams.cancelAt` | Changed | `DateTime → DateTime | enum('max_period_end'|'min_period_end')` |

#### Node.js

| Fields | Change | From → to |
| --- | --- | --- |
| `InvoiceCreatePreviewParams.subscription_details.cancel_at`, `SubscriptionCreateParams.cancel_at`, `SubscriptionUpdateParams.cancel_at` | Changed | `DateTime → DateTime | enum('max_period_end'|'min_period_end')` |

#### Go

| Fields | Change | From → to |
| --- | --- | --- |
| `InvoiceCreatePreviewSubscriptionDetailsParams.CancelAt`, `SubscriptionParams.CancelAt` | Changed | `DateTime → DateTime | enum('max_period_end'|'min_period_end')` |

#### .NET

| Fields | Change | From → to |
| --- | --- | --- |
| `InvoiceSubscriptionDetailsOptions.CancelAt`, `SubscriptionCreateOptions.CancelAt`, `SubscriptionUpdateOptions.CancelAt` | Changed | `DateTime → DateTime | enum('max_period_end'|'min_period_end')` |

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

- [Adds a duration parameter for schedule phases](https://docs.stripe.com/changelog/basil/2025-07-30/add-schedule-phase-duration.md)
- [Adds support for quantity adjustment to the Customer Portal Configuration API](https://docs.stripe.com/changelog/basil/2025-07-30/customer-portal-subscription-update-quantity-limits.md)
- [Adds support for billing thresholds on flexible billing mode Subscriptions](https://docs.stripe.com/changelog/basil/2025-07-30/billing-thresholds.md)
- [Adds support for mixed intervals on the same subscription](https://docs.stripe.com/changelog/basil/2025-07-30/support-mixed-intervals.md)
