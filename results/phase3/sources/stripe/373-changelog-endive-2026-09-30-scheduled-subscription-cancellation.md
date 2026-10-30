# Adds support for scheduling Subscription cancellation as part of pending update

## What’s new

You can now cancel a Subscription at the end of a billing period as part of a [pending update](https://docs.stripe.com/billing/subscriptions/pending-updates.md) that applies when payment on an Invoice succeeds.

The [cancel_at_period_end](https://docs.stripe.com/api/subscriptions/object.md?api-version=2026-09-30.endive#subscription_object-pending_update) property is a nullable boolean added to [pending_update](https://docs.stripe.com/api/subscriptions/object.md?api-version=2026-09-30.endive#subscription_object-pending_update) for a [Subscription](https://docs.stripe.com/api/subscriptions/object.md?api-version=2026-09-30.endive). It indicates whether the subscription will cancel at the end of the current billing period when the pending update applies.

## Impact

You can now pass `cancel_at_period_end` when you [update a subscription](https://docs.stripe.com/api/subscriptions/update.md?api-version=2026-09-30.endive) with [payment_behavior](https://docs.stripe.com/api/subscriptions/update.md?api-version=2026-09-30.endive#update_subscription-payment_behavior) set to `pending_if_incomplete`. This combination previously returned an error. If a subsequent update includes a conflicting `cancel_at_period_end` value, Stripe expires the existing pending update.

If the payment fails or requires customer action, Stripe stores the setting in the `pending_update` hash. After successfully applying the update, Stripe cancels the subscription once the period ends.

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `cancel_at_period_end` | Added | [Subscription.pending_update](/api/subscriptions/object?api-version=2026-09-30.endive#subscription_object-pending_update) |

#### Ruby

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `cancel_at_period_end` | Added | [Subscription::PendingUpdate](/api/subscriptions/object?api-version=2026-09-30.endive#subscription_object-pending_update) |

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `cancel_at_period_end` | Added | [Subscription.PendingUpdate](/api/subscriptions/object?api-version=2026-09-30.endive#subscription_object-pending_update) |

#### PHP

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `cancel_at_period_end` | Added | [Subscription.pending_update](/api/subscriptions/object?api-version=2026-09-30.endive#subscription_object-pending_update) |

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `cancelAtPeriodEnd` | Added | [Subscription.pending_update](/api/subscriptions/object?api-version=2026-09-30.endive#subscription_object-pending_update) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `cancel_at_period_end` | Added | [Subscription.pending_update](/api/subscriptions/object?api-version=2026-09-30.endive#subscription_object-pending_update) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `CancelAtPeriodEnd` | Added | [SubscriptionPendingUpdate](/api/subscriptions/object?api-version=2026-09-30.endive#subscription_object-pending_update) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `CancelAtPeriodEnd` | Added | [Subscription.PendingUpdate](/api/subscriptions/object?api-version=2026-09-30.endive#subscription_object-pending_update) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2026-09-30.endive`
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

- [Unifies the billing cycle anchor format across Subscriptions and Invoices](https://docs.stripe.com/changelog/endive/2026-09-30/polymorphic-billing-cycle-anchor.md)
- [Adds invoicing rules to Invoice Items](https://docs.stripe.com/changelog/endive/2026-09-30/invoicing-rules-for-invoice-items.md)
- [Adds reference and company details parameters for Billie](https://docs.stripe.com/changelog/endive/2026-09-30/reference-and-company-details-billie.md)
- [Adds the ability to clear invoicing rules on Invoice Items](https://docs.stripe.com/changelog/endive/2026-09-30/clear-invoicing-rules-on-invoice-items.md)
- [Adds proration details for Invoice Items using classic billing mode](https://docs.stripe.com/changelog/endive/2026-09-30/invoice-items-proration-details.md)
- [Makes trial offers generally available](https://docs.stripe.com/changelog/endive/2026-09-30/trial-offer-ga.md)
- [Adds detailed status to explain why an invoice is uncollectible](https://docs.stripe.com/changelog/endive/2026-09-30/invoice-uncollectible-status-detail.md)
- [Adds the ability to pause and resume Subscriptions on demand](https://docs.stripe.com/changelog/endive/2026-09-30/pause-subscription.md)
- [Adds the Feedback Options API](https://docs.stripe.com/changelog/endive/2026-09-30/feedback-options-api.md)
