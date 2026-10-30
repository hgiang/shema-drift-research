# Adds invoicing rules to Invoice Items

## What’s new

Adds the [invoicing_rules](https://docs.stripe.com/api/invoiceitems/object.md?api-version=2026-09-30.endive#invoiceitem_object-invoicing_rules) field to [Invoice Items](https://docs.stripe.com/api/invoiceitems/object.md?api-version=2026-09-30.endive). This array of rules controls when an invoice item is eligible to be included on an invoice. All rules must be satisfied before the item can be invoiced. Invoicing rules are used to [defer subscription credit prorations](https://docs.stripe.com/billing/subscriptions/credit-proration-deferral.md).

The currently supported rule is `defer_until_credited_items_resolved`, which prevents credit proration invoice items from being swept onto an invoice until the corresponding debit items are either paid or invoiced alongside the credit on the same invoice. The field value is `[]` when no rules are configured.

## Impact

[Invoice Items](https://docs.stripe.com/api/invoiceitems/object.md?api-version=2026-09-30.endive) now include the `invoicing_rules` field. No changes to your existing integration are required, but you can use this field to determine whether an invoice item has conditions that must be met before it can be invoiced.

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `invoicing_rules` | Added | [InvoiceItem](/api/invoiceitems/object?api-version=2026-09-30.endive#invoiceitem_object) |

#### Ruby

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `invoicing_rules` | Added | [InvoiceItem](/api/invoiceitems/object?api-version=2026-09-30.endive#invoiceitem_object) |

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `invoicing_rules` | Added | [InvoiceItem](/api/invoiceitems/object?api-version=2026-09-30.endive#invoiceitem_object) |

#### PHP

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `invoicing_rules` | Added | [InvoiceItem](/api/invoiceitems/object?api-version=2026-09-30.endive#invoiceitem_object) |

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `invoicingRules` | Added | [InvoiceItem](/api/invoiceitems/object?api-version=2026-09-30.endive#invoiceitem_object) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `invoicing_rules` | Added | [InvoiceItem](/api/invoiceitems/object?api-version=2026-09-30.endive#invoiceitem_object) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `InvoicingRules` | Added | [InvoiceItem](/api/invoiceitems/object?api-version=2026-09-30.endive#invoiceitem_object) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `InvoicingRules` | Added | [InvoiceItem](/api/invoiceitems/object?api-version=2026-09-30.endive#invoiceitem_object) |

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
- [Adds reference and company details parameters for Billie](https://docs.stripe.com/changelog/endive/2026-09-30/reference-and-company-details-billie.md)
- [Adds the ability to clear invoicing rules on Invoice Items](https://docs.stripe.com/changelog/endive/2026-09-30/clear-invoicing-rules-on-invoice-items.md)
- [Adds proration details for Invoice Items using classic billing mode](https://docs.stripe.com/changelog/endive/2026-09-30/invoice-items-proration-details.md)
- [Makes trial offers generally available](https://docs.stripe.com/changelog/endive/2026-09-30/trial-offer-ga.md)
- [Adds detailed status to explain why an invoice is uncollectible](https://docs.stripe.com/changelog/endive/2026-09-30/invoice-uncollectible-status-detail.md)
- [Adds support for scheduling Subscription cancellation as part of pending update](https://docs.stripe.com/changelog/endive/2026-09-30/scheduled-subscription-cancellation.md)
- [Adds the ability to pause and resume Subscriptions on demand](https://docs.stripe.com/changelog/endive/2026-09-30/pause-subscription.md)
- [Adds the Feedback Options API](https://docs.stripe.com/changelog/endive/2026-09-30/feedback-options-api.md)
