# Adds credited items information to invoice item proration details

## What’s new

Adds the [credited_items](https://docs.stripe.com/api/invoiceitems/object.md?api-version=2026-05-27.dahlia#invoiceitem_object-proration_details-credited_items) property to the [proration_details](https://docs.stripe.com/api/invoiceitems/object.md?api-version=2026-05-27.dahlia#invoiceitem_object-proration_details) hash on the [Invoice Item](https://docs.stripe.com/api/invoiceitems/object.md?api-version=2026-05-27.dahlia) object. For credit invoice items that are prorations, this property provides links to the corresponding debit invoice line items or invoice items that the credit applies to.

The `credited_items` property contains:

- A `type` field indicating whether the credit references a pending invoice item (`invoice_item`) or invoice line items on an existing invoice (`invoice_line_items`)
- When `type` is `invoice_item`, an `invoice_item` field with the ID of the debited invoice item
- When `type` is `invoice_line_items`, an `invoice_line_item_details` object containing information about the credited line items

## Impact

You can now access detailed information about which debits a credit proration applies to, making it easier to reconcile prorations and understand the relationship between credit and debit items in your billing workflows. For more information on credit prorations with `credited_items`, see [Relating credit prorations to debited items](https://docs.stripe.com/billing/subscriptions/prorations.md#credit-proration-debit-links).

The `credited_items` property is read-only. Stripe automatically populates it when credit invoice items are created through the proration process.

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `credited_items` | Added | [InvoiceItem.proration_details](/api/invoiceitems/object?api-version=2026-05-27.dahlia#invoiceitem_object-proration_details) |

#### Ruby

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `credited_items` | Added | [InvoiceItem::ProrationDetail](/api/invoiceitems/object?api-version=2026-05-27.dahlia#invoiceitem_object-proration_details) |

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `credited_items` | Added | [InvoiceItem.ProrationDetail](/api/invoiceitems/object?api-version=2026-05-27.dahlia#invoiceitem_object-proration_details) |

#### PHP

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `credited_items` | Added | [InvoiceItem.proration_details](/api/invoiceitems/object?api-version=2026-05-27.dahlia#invoiceitem_object-proration_details) |

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `creditedItems` | Added | [InvoiceItem.proration_details](/api/invoiceitems/object?api-version=2026-05-27.dahlia#invoiceitem_object-proration_details) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `credited_items` | Added | [InvoiceItem.proration_details](/api/invoiceitems/object?api-version=2026-05-27.dahlia#invoiceitem_object-proration_details) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `CreditedItems` | Added | [InvoiceItemProrationDetails](/api/invoiceitems/object?api-version=2026-05-27.dahlia#invoiceitem_object-proration_details) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `CreditedItems` | Added | [InvoiceItem.ProrationDetails](/api/invoiceitems/object?api-version=2026-05-27.dahlia#invoiceitem_object-proration_details) |

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
- [Adds billing schedules to enable prebilling on subscriptions](https://docs.stripe.com/changelog/dahlia/2026-05-27/subscriptions-billing-schedules.md)
- [Adds discount and discounts properties to pending subscription updates](https://docs.stripe.com/changelog/dahlia/2026-05-27/pending-subscription-updates-discount-and-discounts-properties.md)
- [Adds metadata support to pending subscription updates](https://docs.stripe.com/changelog/dahlia/2026-05-27/pending-subscription-update-metadata.md)
- [Adds customer parameter to test clock creation](https://docs.stripe.com/changelog/dahlia/2026-05-27/test-clock-creation-customer-parameter.md)
