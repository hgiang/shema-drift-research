# Replaces top-level price fields with improved price modelling on Invoice Items and Invoice Line Items

## What’s new

We’re introducing a new polymorphic `pricing` concept on [Invoice Items](https://docs.stripe.com/api/invoiceitems/object.md?api-version=2025-03-31.basil#invoiceitem_object-pricing) and [Invoice Line Items](https://docs.stripe.com/api/invoice-line-item/object.md?api-version=2025-03-31.basil#invoice_line_item_object-pricing). It contains all price-related data and unifies the structure of pricing objects ([Price](https://docs.stripe.com/api/prices/object.md?api-version=2025-03-31.basil) and [Plan](https://docs.stripe.com/api/plans/object.md?api-version=2025-03-31.basil)) to prepare for adding new pricing object types. We’re also moving unit amount data into `pricing`.

## Why is this a breaking change?

- `price` and `plan` fields are no longer available on Invoice Items and Invoice Line Items.
- Move `unit_amount` and `unit_amount_decimal` to the new `pricing` concept on Invoice Items and Invoice Line Items.

## Impact

Replace all references to `price` or `plan` on Invoice Items or Invoice Line Items with the `pricing` field:

- Instead of `invoice_item.price.id`, use `invoice_item.pricing.price_details.price` after verifying that `invoice_item.pricing.type` is `price_details`
- When creating or updating Invoice Items, use the `pricing` parameter instead of `price` (for example, set `pricing.price` instead of passing the `price` parameter)
- For unit amounts, use `pricing.unit_amount_decimal` instead of `unit_amount` or `unit_amount_decimal`
- When creating or updating Invoice Items, use the `unit_amount_decimal` parameter instead of `unit_amount`

## Changes

#### REST API

| Parameters | Change | Resources or endpoints |
| --- | --- | --- |
| `plan`, `price`, `unit_amount_decimal`, `unit_amount` | Removed | [InvoiceItem](/api/invoiceitems/object?api-version=2025-03-31.basil) |
| `plan`, `price` | Removed | [InvoiceLineItem](/api/invoice-line-item?api-version=2025-03-31.basil) |
| `pricing` | Added | [Invoice#add_lines.lines[]](/api/invoice-line-item/update?api-version=2025-03-31.basil), [Invoice#update_lines.lines[]](/api/invoices/update?api-version=2025-03-31.basil), [InvoiceItem#create](/api/invoiceitems/create?api-version=2025-03-31.basil), [InvoiceItem#update](/api/invoiceitems/update?api-version=2025-03-31.basil), [InvoiceLineItem#update](/api/invoice-line-item/update?api-version=2025-03-31.basil), [InvoiceItem](/api/invoiceitems/object?api-version=2025-03-31.basil), [InvoiceLineItem](/api/invoice-line-item?api-version=2025-03-31.basil) |
| `price` | Removed | [Invoice#add_lines.lines[]](/api/invoice-line-item/update?api-version=2025-03-31.basil), [Invoice#update_lines.lines[]](/api/invoices/update?api-version=2025-03-31.basil), [InvoiceItem#create](/api/invoiceitems/create?api-version=2025-03-31.basil), [InvoiceItem#update](/api/invoiceitems/update?api-version=2025-03-31.basil), [InvoiceItem](/api/invoiceitems/object?api-version=2025-03-31.basil), [InvoiceLineItem#update](/api/invoice-line-item/update?api-version=2025-03-31.basil), [InvoiceLineItem](/api/invoice-line-item?api-version=2025-03-31.basil) |
| `unit_amount` | Removed | [InvoiceItem#create](/api/invoiceitems/create?api-version=2025-03-31.basil), [InvoiceItem#update](/api/invoiceitems/update?api-version=2025-03-31.basil), [InvoiceItem](/api/invoiceitems/object?api-version=2025-03-31.basil) |

#### Ruby

This change doesn’t affect the Ruby SDK.

#### Python

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `plan`, `price`, `unit_amount` | Removed | [stripe.InvoiceItem](/api/invoiceitems/object?api-version=2025-03-31.basil) |
| `pricing` | Added | [Invoice.AddLinesParamsLine](/api/invoice-line-item/bulk?api-version=2025-03-31.basil#bulk_add_lines-lines), [Invoice.UpdateLinesParamsLine](/api/invoices/update?api-version=2025-03-31.basil), [InvoiceItem.CreateParams](/api/invoiceitems/create?api-version=2025-03-31.basil), [InvoiceItem.UpdateParams](/api/invoiceitems/update?api-version=2025-03-31.basil), [InvoiceLineItem.UpdateParams](/api/invoice-line-item/update?api-version=2025-03-31.basil), [InvoiceItem](/api/invoiceitems/object?api-version=2025-03-31.basil), [InvoiceLineItem](/api/invoice-line-item?api-version=2025-03-31.basil) |
| `price` | Removed | [Invoice.AddLinesParamsLine](/api/invoice-line-item/bulk?api-version=2025-03-31.basil#bulk_add_lines-lines), [Invoice.UpdateLinesParamsLine](/api/invoices/update?api-version=2025-03-31.basil), [InvoiceItem.CreateParams](/api/invoiceitems/create?api-version=2025-03-31.basil), [InvoiceItem.UpdateParams](/api/invoiceitems/update?api-version=2025-03-31.basil), [InvoiceItem](/api/invoiceitems/object?api-version=2025-03-31.basil), [InvoiceLineItem.UpdateParams](/api/invoice-line-item/update?api-version=2025-03-31.basil), [InvoiceLineItem](/api/invoice-line-item?api-version=2025-03-31.basil) |
| `unit_amount` | Removed | [InvoiceItem.CreateParams](/api/invoiceitems/create?api-version=2025-03-31.basil), [InvoiceItem.UpdateParams](/api/invoiceitems/update?api-version=2025-03-31.basil), [InvoiceItem](/api/invoiceitems/object?api-version=2025-03-31.basil), [stripe.InvoiceItem](/api/invoiceitems/object?api-version=2025-03-31.basil) |

#### PHP

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `plan`, `price`, `unit_amount_decimal`, `unit_amount` | Removed | [InvoiceItem](/api/invoiceitems/object?api-version=2025-03-31.basil) |
| `plan`, `price` | Removed | [InvoiceLineItem](/api/invoice-line-item?api-version=2025-03-31.basil) |
| `pricing` | Added | [InvoiceItem](/api/invoiceitems/object?api-version=2025-03-31.basil), [InvoiceLineItem](/api/invoice-line-item?api-version=2025-03-31.basil) |

#### Java

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `plan`, `price`, `unit_amount_decimal`, `unit_amount` | Removed | [InvoiceItem](/api/invoiceitems/object?api-version=2025-03-31.basil) |
| `plan`, `price` | Removed | [InvoiceLineItem](/api/invoice-line-item?api-version=2025-03-31.basil) |
| `pricing` | Added | [InvoiceAddLinesParams.lines[]](/api/invoice-line-item/bulk?api-version=2025-03-31.basil#bulk_add_lines-lines), [InvoiceItemCreateParams](/api/invoiceitems/create?api-version=2025-03-31.basil), [InvoiceItemUpdateParams](/api/invoiceitems/update?api-version=2025-03-31.basil), [InvoiceLineItemUpdateParams](/api/invoice-line-item/update?api-version=2025-03-31.basil), [InvoiceUpdateLinesParams.lines[]](/api/invoices/update?api-version=2025-03-31.basil), [InvoiceItem](/api/invoiceitems/object?api-version=2025-03-31.basil), [InvoiceLineItem](/api/invoice-line-item?api-version=2025-03-31.basil) |
| `price` | Removed | [InvoiceAddLinesParams.lines[]](/api/invoice-line-item/bulk?api-version=2025-03-31.basil#bulk_add_lines-lines), [InvoiceItemCreateParams](/api/invoiceitems/create?api-version=2025-03-31.basil), [InvoiceItemUpdateParams](/api/invoiceitems/update?api-version=2025-03-31.basil), [InvoiceItem](/api/invoiceitems/object?api-version=2025-03-31.basil), [InvoiceLineItemUpdateParams](/api/invoice-line-item/update?api-version=2025-03-31.basil), [InvoiceLineItem](/api/invoice-line-item?api-version=2025-03-31.basil), [InvoiceUpdateLinesParams.lines[]](/api/invoices/update?api-version=2025-03-31.basil) |
| `unitAmount` | Removed | [InvoiceItemCreateParams](/api/invoiceitems/create?api-version=2025-03-31.basil), [InvoiceItemUpdateParams](/api/invoiceitems/update?api-version=2025-03-31.basil), [InvoiceItem](/api/invoiceitems/object?api-version=2025-03-31.basil) |

#### Node.js

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `plan`, `price`, `unit_amount_decimal`, `unit_amount` | Removed | [InvoiceItem](/api/invoiceitems/object?api-version=2025-03-31.basil) |
| `plan`, `price` | Removed | [InvoiceLineItem](/api/invoice-line-item?api-version=2025-03-31.basil) |
| `pricing` | Added | [InvoiceAddLinesParams.lines[]](/api/invoice-line-item/bulk?api-version=2025-03-31.basil#bulk_add_lines-lines), [InvoiceItemCreateParams](/api/invoiceitems/create?api-version=2025-03-31.basil), [InvoiceItemUpdateParams](/api/invoiceitems/update?api-version=2025-03-31.basil), [InvoiceLineItemUpdateParams](/api/invoice-line-item/update?api-version=2025-03-31.basil), [InvoiceUpdateLinesParams.lines[]](/api/invoices/update?api-version=2025-03-31.basil), [InvoiceItem](/api/invoiceitems/object?api-version=2025-03-31.basil), [InvoiceLineItem](/api/invoice-line-item?api-version=2025-03-31.basil) |
| `price` | Removed | [InvoiceAddLinesParams.lines[]](/api/invoice-line-item/bulk?api-version=2025-03-31.basil#bulk_add_lines-lines), [InvoiceItemCreateParams](/api/invoiceitems/create?api-version=2025-03-31.basil), [InvoiceItemUpdateParams](/api/invoiceitems/update?api-version=2025-03-31.basil), [InvoiceItem](/api/invoiceitems/object?api-version=2025-03-31.basil), [InvoiceLineItemUpdateParams](/api/invoice-line-item/update?api-version=2025-03-31.basil), [InvoiceLineItem](/api/invoice-line-item?api-version=2025-03-31.basil), [InvoiceUpdateLinesParams.lines[]](/api/invoices/update?api-version=2025-03-31.basil) |
| `unit_amount` | Removed | [InvoiceItemCreateParams](/api/invoiceitems/create?api-version=2025-03-31.basil), [InvoiceItemUpdateParams](/api/invoiceitems/update?api-version=2025-03-31.basil), [InvoiceItem](/api/invoiceitems/object?api-version=2025-03-31.basil) |

#### Go

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `Plan`, `Price`, `UnitAmountDecimal`, `UnitAmount` | Removed | [InvoiceItem](/api/invoiceitems/object?api-version=2025-03-31.basil) |
| `Plan`, `Price` | Removed | [InvoiceLineItem](/api/invoice-line-item?api-version=2025-03-31.basil) |
| `Pricing` | Added | [InvoiceAddLinesLinesParams](/api/invoice-line-item/bulk?api-version=2025-03-31.basil#bulk_add_lines-lines), [InvoiceItemParams](/api/invoiceitems?api-version=2025-03-31.basil), [InvoiceLineItemParams](/api/invoice-line-item?api-version=2025-03-31.basil), [InvoiceUpdateLinesLinesParams](/api/invoices/update?api-version=2025-03-31.basil), [InvoiceItem](/api/invoiceitems/object?api-version=2025-03-31.basil), [InvoiceLineItem](/api/invoice-line-item?api-version=2025-03-31.basil) |
| `Price` | Removed | [InvoiceAddLinesLinesParams](/api/invoice-line-item/bulk?api-version=2025-03-31.basil#bulk_add_lines-lines), [InvoiceItemParams](/api/invoiceitems?api-version=2025-03-31.basil), [InvoiceItem](/api/invoiceitems/object?api-version=2025-03-31.basil), [InvoiceLineItemParams](/api/invoice-line-item?api-version=2025-03-31.basil), [InvoiceLineItem](/api/invoice-line-item?api-version=2025-03-31.basil), [InvoiceUpdateLinesLinesParams](/api/invoices/update?api-version=2025-03-31.basil) |
| `UnitAmount` | Removed | [InvoiceItemParams](/api/invoiceitems?api-version=2025-03-31.basil), [InvoiceItem](/api/invoiceitems/object?api-version=2025-03-31.basil) |

#### .NET

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `Plan`, `Price`, `UnitAmountDecimal`, `UnitAmount` | Removed | [InvoiceItem](/api/invoiceitems/object?api-version=2025-03-31.basil) |
| `Plan`, `Price` | Removed | [InvoiceLineItem](/api/invoice-line-item?api-version=2025-03-31.basil) |
| `Pricing` | Added | [InvoiceItemCreateOptions](/api/invoiceitems/create?api-version=2025-03-31.basil), [InvoiceItemUpdateOptions](/api/invoiceitems/update?api-version=2025-03-31.basil), [InvoiceLineItemUpdateOptions](/api/invoice-line-item/update?api-version=2025-03-31.basil), [InvoiceLinesOptions](/api/invoice-line-item?api-version=2025-03-31.basil), [InvoiceItem](/api/invoiceitems/object?api-version=2025-03-31.basil), [InvoiceLineItem](/api/invoice-line-item?api-version=2025-03-31.basil) |
| `Price` | Removed | [InvoiceItemCreateOptions](/api/invoiceitems/create?api-version=2025-03-31.basil), [InvoiceItemUpdateOptions](/api/invoiceitems/update?api-version=2025-03-31.basil), [InvoiceItem](/api/invoiceitems/object?api-version=2025-03-31.basil), [InvoiceLineItemUpdateOptions](/api/invoice-line-item/update?api-version=2025-03-31.basil), [InvoiceLineItem](/api/invoice-line-item?api-version=2025-03-31.basil), [InvoiceLinesOptions](/api/invoice-line-item?api-version=2025-03-31.basil) |
| `UnitAmount` | Removed | [InvoiceItemCreateOptions](/api/invoiceitems/create?api-version=2025-03-31.basil), [InvoiceItemUpdateOptions](/api/invoiceitems/update?api-version=2025-03-31.basil), [InvoiceItem](/api/invoiceitems/object?api-version=2025-03-31.basil) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2025-03-31.basil`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to [v15.0.0](https://github.com/stripe/stripe-ruby/releases/tag/v15.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to [v12.0.0](https://github.com/stripe/stripe-python/releases/tag/v12.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to [v17.0.0](https://github.com/stripe/stripe-php/releases/tag/v17.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to [v29.0.0](https://github.com/stripe/stripe-java/releases/tag/v29.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to [v18.0.0](https://github.com/stripe/stripe-node/releases/tag/v18.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to [v82.0.0](https://github.com/stripe/stripe-go/releases/tag/v82.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to [v48.0.0](https://github.com/stripe/stripe-dotnet/releases/tag/v48.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

## Related changes

- [Replaces top-level tax-related properties with improved tax modelling on Invoices, Invoice Line Items, and Credit Note Line Items](https://docs.stripe.com/changelog/basil/2025-03-31/invoice-tax-configurations.md)
- [Adds support for multiple (partial) payments on invoices](https://docs.stripe.com/changelog/basil/2025-03-31/add-support-for-multiple-partial-payments-on-invoices.md)
- [Adds jurisdiction level and taxability reason to manual tax amounts on invoices](https://docs.stripe.com/changelog/basil/2025-03-31/invoice-manual-tax-amount-fields.md)
