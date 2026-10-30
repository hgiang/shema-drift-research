# Adds billing schedules to enable prebilling on subscriptions

## What’s new

You can now collect payment for future billing periods before they begin by specifying billing schedules when you [create](https://docs.stripe.com/api/subscriptions/create.md?api-version=2026-05-27.dahlia#create_subscription-billing_schedules), [update](https://docs.stripe.com/api/subscriptions/update.md?api-version=2026-05-27.dahlia#update_subscription-billing_schedules), or [preview](https://docs.stripe.com/api/invoices/create_preview.md?api-version=2026-05-27.dahlia#create_invoice-subscription_details-billing_schedules) subscriptions. Billing schedules determine the future period to bill for and can apply to some or all of the items in the subscription.

The new [billed_until](https://docs.stripe.com/api/subscription_items/object.md?api-version=2026-05-27.dahlia#subscription_item_object-billed_until) property on subscription items allows you to see when the prebilled period ends for each item.

## Impact

You can now prebill customers for future periods before they begin. Common use cases include:

| Use case | Description |
| --- | --- |
| **Prepay multiple months at signup** | Charge a monthly subscriber upfront for 3 months when they sign up, then resume normal monthly billing from that point. |
| **Early renewal billing** | When a renewal is 7 days away, generate and send the customer the renewal invoice now instead of waiting for the end of the billing cycle. |
| **Annual payment on a monthly price** | Let a customer pay for 12 months of a monthly plan in one upfront invoice, without changing the underlying price to an annual interval. |
| **Early cancellation fee** | Charge a customer for the remaining term of a committed contract when they cancel early by prebilling through the end of the commitment, then cancelling the subscription. |

Learn more about [configuring prebilling for subscriptions](https://docs.stripe.com/billing/subscriptions/prebilling.md).

## Changes

#### REST API

| Parameters | Change | Resources or endpoints |
| --- | --- | --- |
| `billing_schedules` | Added | [Invoice#create_preview.subscription_details](/api/invoices/create_preview?api-version=2026-05-27.dahlia#create_invoice-subscription_details), [Subscription](/api/subscriptions/object?api-version=2026-05-27.dahlia#subscription_object), [Subscription#create](/api/subscriptions/create?api-version=2026-05-27.dahlia#create_subscription), [Subscription#update](/api/subscriptions/update?api-version=2026-05-27.dahlia#update_subscription) |
| `billed_until` | Added | [SubscriptionItem](/api/subscription_items/object?api-version=2026-05-27.dahlia#subscription_item_object) |

#### Ruby

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `billing_schedules` | Added | [InvoiceCreatePreviewParams::SubscriptionDetail](/api/invoices/create_preview?api-version=2026-05-27.dahlia#create_invoice-subscription_details), [Subscription](/api/subscriptions/object?api-version=2026-05-27.dahlia#subscription_object), [SubscriptionCreateParams](/api/subscriptions/create?api-version=2026-05-27.dahlia#create_subscription), [SubscriptionUpdateParams](/api/subscriptions/update?api-version=2026-05-27.dahlia#update_subscription) |
| `billed_until` | Added | [SubscriptionItem](/api/subscription_items/object?api-version=2026-05-27.dahlia#subscription_item_object) |

#### Python

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `billing_schedules` | Added | [InvoiceCreatePreviewParamsSubscriptionDetail](/api/invoices/create_preview?api-version=2026-05-27.dahlia#create_invoice-subscription_details), [Subscription](/api/subscriptions/object?api-version=2026-05-27.dahlia#subscription_object), [SubscriptionCreateParams](/api/subscriptions/create?api-version=2026-05-27.dahlia#create_subscription), [SubscriptionModifyParams](/api/subscriptions/update?api-version=2026-05-27.dahlia#update_subscription) |
| `billed_until` | Added | [SubscriptionItem](/api/subscription_items/object?api-version=2026-05-27.dahlia#subscription_item_object) |

#### PHP

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `billing_schedules` | Added | [Invoice.create_preview().$params.subscription_detail](/api/invoices/create_preview?api-version=2026-05-27.dahlia#create_invoice-subscription_details), [Subscription](/api/subscriptions/object?api-version=2026-05-27.dahlia#subscription_object), [Subscription.create().$params](/api/subscriptions/create?api-version=2026-05-27.dahlia#create_subscription), [Subscription.update().$params](/api/subscriptions/update?api-version=2026-05-27.dahlia#update_subscription) |
| `billed_until` | Added | [SubscriptionItem](/api/subscription_items/object?api-version=2026-05-27.dahlia#subscription_item_object) |

#### Java

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `billingSchedules` | Added | [InvoiceCreatePreviewParams.subscription_details](/api/invoices/create_preview?api-version=2026-05-27.dahlia#create_invoice-subscription_details), [Subscription](/api/subscriptions/object?api-version=2026-05-27.dahlia#subscription_object), [SubscriptionCreateParams](/api/subscriptions/create?api-version=2026-05-27.dahlia#create_subscription), [SubscriptionUpdateParams](/api/subscriptions/update?api-version=2026-05-27.dahlia#update_subscription) |
| `billedUntil` | Added | [SubscriptionItem](/api/subscription_items/object?api-version=2026-05-27.dahlia#subscription_item_object) |

#### Node.js

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `billing_schedules` | Added | [InvoiceCreatePreviewParams.subscription_details](/api/invoices/create_preview?api-version=2026-05-27.dahlia#create_invoice-subscription_details), [Subscription](/api/subscriptions/object?api-version=2026-05-27.dahlia#subscription_object), [SubscriptionCreateParams](/api/subscriptions/create?api-version=2026-05-27.dahlia#create_subscription), [SubscriptionUpdateParams](/api/subscriptions/update?api-version=2026-05-27.dahlia#update_subscription) |
| `billed_until` | Added | [SubscriptionItem](/api/subscription_items/object?api-version=2026-05-27.dahlia#subscription_item_object) |

#### Go

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `BillingSchedules` | Added | [InvoiceCreatePreviewSubscriptionDetailsParams](/api/invoices/create_preview?api-version=2026-05-27.dahlia#create_invoice-subscription_details), [Subscription](/api/subscriptions/object?api-version=2026-05-27.dahlia#subscription_object), [SubscriptionParams](/api/subscriptions/update?api-version=2026-05-27.dahlia#update_subscription) |
| `BilledUntil` | Added | [SubscriptionItem](/api/subscription_items/object?api-version=2026-05-27.dahlia#subscription_item_object) |

#### .NET

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `BillingSchedules` | Added | [InvoiceSubscriptionDetailsOptions](/api/invoices/create_preview?api-version=2026-05-27.dahlia#create_invoice-subscription_details), [Subscription](/api/subscriptions/object?api-version=2026-05-27.dahlia#subscription_object), [SubscriptionCreateOptions](/api/subscriptions/create?api-version=2026-05-27.dahlia#create_subscription), [SubscriptionUpdateOptions](/api/subscriptions/update?api-version=2026-05-27.dahlia#update_subscription) |
| `BilledUntil` | Added | [SubscriptionItem](/api/subscription_items/object?api-version=2026-05-27.dahlia#subscription_item_object) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2026-05-27.dahlia`
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

- [Adds discount eligibility options for add-on invoice items on Subscriptions and Preview Invoice APIs](https://docs.stripe.com/changelog/dahlia/2026-05-27/invoice-items-discount-eligibility.md)
- [Adds amount paid off Stripe property to Invoice object](https://docs.stripe.com/changelog/dahlia/2026-05-27/invoice-object-amount-paid-off-stripe-property.md)
- [Adds discount and discounts properties to pending subscription updates](https://docs.stripe.com/changelog/dahlia/2026-05-27/pending-subscription-updates-discount-and-discounts-properties.md)
- [Adds metadata support to pending subscription updates](https://docs.stripe.com/changelog/dahlia/2026-05-27/pending-subscription-update-metadata.md)
- [Adds credited items information to invoice item proration details](https://docs.stripe.com/changelog/dahlia/2026-05-27/invoice-item-proration-credited-items.md)
- [Adds customer parameter to test clock creation](https://docs.stripe.com/changelog/dahlia/2026-05-27/test-clock-creation-customer-parameter.md)
