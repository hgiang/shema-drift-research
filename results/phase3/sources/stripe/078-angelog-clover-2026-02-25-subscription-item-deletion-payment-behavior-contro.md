# Adds payment behaviour control for subscription item deletion

## What’s new

You can specify the [payment_behavior](https://docs.stripe.com/api/subscription_items/delete.md?api-version=2026-02-25.clover#delete_subscription_item-payment_behavior) parameter when you [delete a subscription item](https://docs.stripe.com/api/subscription_items/delete.md?api-version=2026-02-25.clover). Setting `payment_behavior=pending_if_incomplete` stages the deletion as a pending update when the change would generate an invoice that requires payment, rather than deleting the item immediately.

## Impact

This new approach maintains consistency in your subscription management workflow and prevents items from being removed before payment is confirmed. Further, this change aligns subscription item deletion with the existing pending update behaviour available when [adding](https://docs.stripe.com/api/subscription_items/create.md?api-version=2026-02-25.clover#create_subscription_item-payment_behavior) and [modifying](https://docs.stripe.com/api/subscription_items/update.md?api-version=2026-02-25.clover#update_subscription_item-payment_behavior) subscription items. Previously, you could only delete subscription items immediately, which could create inconsistencies in how subscription changes are handled across different operations.

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `payment_behavior` | Added | [SubscriptionItem#delete](/api/subscription_items/delete?api-version=2026-02-25.clover) |

#### Ruby

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `payment_behavior` | Added | [SubscriptionItemDeleteParams](/api/subscription_items/delete?api-version=2026-02-25.clover) |

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `payment_behavior` | Added | [SubscriptionItemDeleteParams](/api/subscription_items/delete?api-version=2026-02-25.clover) |

#### PHP

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `payment_behavior` | Added | [SubscriptionItem.delete().$params](/api/subscription_items/delete?api-version=2026-02-25.clover) |

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `paymentBehavior` | Added | [SubscriptionItemDeleteParams](/api/subscription_items/delete?api-version=2026-02-25.clover) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `payment_behavior` | Added | [SubscriptionItemDeleteParams](/api/subscription_items/delete?api-version=2026-02-25.clover) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `PaymentBehavior` | Added | [SubscriptionItemParams](/api/subscription_items/delete?api-version=2026-02-25.clover) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `PaymentBehavior` | Added | [SubscriptionItemDeleteOptions](/api/subscription_items/delete?api-version=2026-02-25.clover) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2026-02-25.clover`
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

- [Adds Pay by Bank to the Billing API](https://docs.stripe.com/changelog/clover/2026-02-25/billing-api-pay-by-bank.md)
