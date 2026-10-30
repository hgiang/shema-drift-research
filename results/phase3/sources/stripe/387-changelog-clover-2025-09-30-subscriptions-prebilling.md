# Enables pre-billing for subscriptions

## What’s new

You can now pre-bill subscriptions for a longer duration than their current billing period, and choose which subscription items you want to pre-bill.

Subscriptions must use [flexible billing mode](https://docs.stripe.com/billing/subscriptions/billing-mode.md) to use prebilling.

## Impact

You can now pre-bill subscriptions by setting the `billing_schedules` parameter in the following APIs:

- [Create a subscription](https://docs.stripe.com/api/subscriptions/create.md?api-version=2025-09-30.preview)
- [Update a subscription](https://docs.stripe.com/api/subscriptions/update.md?api-version=2025-09-30.preview)
- [Create a preview invoices](https://docs.stripe.com/api/invoices/create_preview.md?api-version=2025-09-30.preview)

You can configure how long you want to pre-bill for by using `billing_schedules.bill_until`, and which prices you want to pre-bill using `billing_schedules.applies_to`. You can also identify the date each subscription item has been billed until using `subscriptions.items.data.billed_until` the field.

## Changes

#### REST API

| Parameters | Change | Resources or endpoints |
| --- | --- | --- |
| `billing_schedules` | Added | [Invoice#create_preview.subscription_details](/api/invoices/create_preview?api-version=2025-09-30.preview#create_invoice-subscription_details), [Subscription](/api/subscriptions/object?api-version=2025-09-30.preview), [Subscription#create](/api/subscriptions/create?api-version=2025-09-30.preview), [Subscription#update](/api/subscriptions/update?api-version=2025-09-30.preview) |
| `billed_until` | Added | [SubscriptionItem](/api/subscription_items/object?api-version=2025-09-30.preview) |

#### Ruby

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `billing_schedules` | Added | [Invoice::CreatePreviewParams::SubscriptionDetail](/api/invoices/create_preview?api-version=2025-09-30.preview#create_invoice-subscription_details), [Subscription](/api/subscriptions/object?api-version=2025-09-30.preview), [Subscription::CreateParams](/api/subscriptions/create?api-version=2025-09-30.preview), [Subscription::UpdateParams](/api/subscriptions/update?api-version=2025-09-30.preview) |
| `billed_until` | Added | [SubscriptionItem](/api/subscription_items/object?api-version=2025-09-30.preview) |

#### Python

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `billing_schedules` | Added | [Invoice.CreatePreviewParamsSubscriptionDetail](/api/invoices/create_preview?api-version=2025-09-30.preview#create_invoice-subscription_details), [Subscription](/api/subscriptions/object?api-version=2025-09-30.preview), [Subscription.CreateParams](/api/subscriptions/create?api-version=2025-09-30.preview), [Subscription.ModifyParams](/api/subscriptions/update?api-version=2025-09-30.preview) |
| `billed_until` | Added | [SubscriptionItem](/api/subscription_items/object?api-version=2025-09-30.preview) |

#### PHP

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `billing_schedules` | Added | [Invoice.create_preview().$params.subscription_detail](/api/invoices/create_preview?api-version=2025-09-30.preview#create_invoice-subscription_details), [Subscription](/api/subscriptions/object?api-version=2025-09-30.preview), [Subscription.create().$params](/api/subscriptions/create?api-version=2025-09-30.preview), [Subscription.update().$params](/api/subscriptions/update?api-version=2025-09-30.preview) |
| `billed_until` | Added | [SubscriptionItem](/api/subscription_items/object?api-version=2025-09-30.preview) |

#### Java

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `billingSchedules` | Added | [InvoiceCreatePreviewParams.subscription_details](/api/invoices/create_preview?api-version=2025-09-30.preview#create_invoice-subscription_details), [Subscription](/api/subscriptions/object?api-version=2025-09-30.preview), [SubscriptionCreateParams](/api/subscriptions/create?api-version=2025-09-30.preview), [SubscriptionUpdateParams](/api/subscriptions/update?api-version=2025-09-30.preview) |
| `billedUntil` | Added | [SubscriptionItem](/api/subscription_items/object?api-version=2025-09-30.preview) |

#### Node.js

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `billing_schedules` | Added | [InvoiceCreatePreviewParams.subscription_details](/api/invoices/create_preview?api-version=2025-09-30.preview#create_invoice-subscription_details), [Subscription](/api/subscriptions/object?api-version=2025-09-30.preview), [SubscriptionCreateParams](/api/subscriptions/create?api-version=2025-09-30.preview), [SubscriptionUpdateParams](/api/subscriptions/update?api-version=2025-09-30.preview) |
| `billed_until` | Added | [SubscriptionItem](/api/subscription_items/object?api-version=2025-09-30.preview) |

#### Go

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `BillingSchedules` | Added | [InvoiceCreatePreviewSubscriptionDetailsParams](/api/invoices/create_preview?api-version=2025-09-30.preview#create_invoice-subscription_details), [Subscription](/api/subscriptions/object?api-version=2025-09-30.preview), [SubscriptionParams](/api/subscriptions/update?api-version=2025-09-30.preview) |
| `BilledUntil` | Added | [SubscriptionItem](/api/subscription_items/object?api-version=2025-09-30.preview) |

#### .NET

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `BillingSchedules` | Added | [InvoiceSubscriptionDetailsOptions](/api/invoices/create_preview?api-version=2025-09-30.preview#create_invoice-subscription_details), [Subscription](/api/subscriptions/object?api-version=2025-09-30.preview), [SubscriptionCreateOptions](/api/subscriptions/create?api-version=2025-09-30.preview), [SubscriptionUpdateOptions](/api/subscriptions/update?api-version=2025-09-30.preview) |
| `BilledUntil` | Added | [SubscriptionItem](/api/subscription_items/object?api-version=2025-09-30.preview) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2025-09-30.preview`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to [v16.1.0-beta.1](https://github.com/stripe/stripe-ruby/releases/tag/v16.1.0-beta.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to [v13.1.2b1](https://github.com/stripe/stripe-python/releases/tag/v13.1.2b1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to [v18.1.0-beta.1](https://github.com/stripe/stripe-php/releases/tag/v18.1.0-beta.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to [v30.1.0-beta.1](https://github.com/stripe/stripe-java/releases/tag/v30.1.0-beta.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to [v19.2.0-beta.1](https://github.com/stripe/stripe-node/releases/tag/v19.2.0-beta.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to [v83.1.0-beta.1](https://github.com/stripe/stripe-go/releases/tag/v83.1.0-beta.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to [v49.1.0-beta.1](https://github.com/stripe/stripe-dotnet/releases/tag/v49.1.0-beta.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

## Related changes

- [Adds pagination and updates fields for aggregated Billing meter usage data](https://docs.stripe.com/changelog/clover/2025-09-30/update-meter-usage-fields.md)
- [Adds the ability to update automatic tax, invoice creation and invoice settings for Checkout Sessions](https://docs.stripe.com/changelog/clover/2025-09-30/checkout-sessions-tax-and-invoice-settings.md)
- [Adds the unit label parameter to the product data hash](https://docs.stripe.com/changelog/clover/2025-09-30/add-product-data-unit-label-preview.md)
