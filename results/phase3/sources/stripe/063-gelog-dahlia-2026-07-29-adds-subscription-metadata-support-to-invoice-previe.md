# Adds subscription metadata support to invoice previews

## What’s new

Adds the ability to pass [subscription_details.metadata](https://docs.stripe.com/api/invoices/create_preview.md?api-version=2026-07-29.dahlia#create_invoice-subscription_details-metadata) when creating [invoice previews](https://docs.stripe.com/api/invoices/create_preview.md?api-version=2026-07-29.dahlia). This lets you include subscription metadata as part of a preview request, whether you’re previewing a new subscription creation or an update to an existing subscription that sets or changes `metadata` on the subscription.

## Impact

If your integration previews invoices before creating or updating subscriptions that include [metadata](https://docs.stripe.com/api/metadata.md?api-version=2026-07-29.dahlia), you can now pass that `metadata` in the preview request to get an accurate preview of the resulting invoice.

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `metadata` | Added | [Invoice#create_preview.subscription_details](/api/invoices/create_preview?api-version=2026-07-29.dahlia#create_invoice-subscription_details) |

#### Ruby

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `metadata` | Added | [InvoiceCreatePreviewParams::SubscriptionDetail](/api/invoices/create_preview?api-version=2026-07-29.dahlia#create_invoice-subscription_details) |

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `metadata` | Added | [InvoiceCreatePreviewParamsSubscriptionDetail](/api/invoices/create_preview?api-version=2026-07-29.dahlia#create_invoice-subscription_details) |

#### PHP

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `metadata` | Added | [Invoice.create_preview().$params.subscription_detail](/api/invoices/create_preview?api-version=2026-07-29.dahlia#create_invoice-subscription_details) |

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `metadata` | Added | [InvoiceCreatePreviewParams.subscription_details](/api/invoices/create_preview?api-version=2026-07-29.dahlia#create_invoice-subscription_details) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `metadata` | Added | [InvoiceCreatePreviewParams.subscription_details](/api/invoices/create_preview?api-version=2026-07-29.dahlia#create_invoice-subscription_details) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `Metadata` | Added | [InvoiceCreatePreviewSubscriptionDetailsParams](/api/invoices/create_preview?api-version=2026-07-29.dahlia#create_invoice-subscription_details) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `Metadata` | Added | [InvoiceSubscriptionDetailsOptions](/api/invoices/create_preview?api-version=2026-07-29.dahlia#create_invoice-subscription_details) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2026-07-29.dahlia`
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

- [Adds invoice description, footer and custom parameters to the Subscription Schedules and Quotes APIs](https://docs.stripe.com/changelog/dahlia/2026-07-29/invoice-description-footer-and-custom-fields.md)
- [Adds the trial property to subscription schedule phases](https://docs.stripe.com/changelog/dahlia/2026-07-29/subscription-schedule-phases-trial-property.md)
- [Adds item-level discount support for pending updates](https://docs.stripe.com/changelog/dahlia/2026-07-29/item-level-discounts-for-pending-updates.md)
