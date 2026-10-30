# Adds expandable tax rate property to tax rate details

## What’s new

You can now expand the [tax_rate](https://docs.stripe.com/api/tax_rates/object.md?api-version=2026-04-22.dahlia) property within [tax_rate_details](https://docs.stripe.com/api/invoices/object.md?api-version=2026-04-22.dahlia#invoice_object-total_taxes-tax_rate_details) on invoicing resources. Retrieve the full Tax Rate object inline instead of the tax rate ID, reducing API calls to display complete tax information.

The expandable [tax_rate](https://docs.stripe.com/api/tax_rates/object.md?api-version=2026-04-22.dahlia) property is now available on:

- [Invoice](https://docs.stripe.com/api/invoices/object.md?api-version=2026-04-22.dahlia): [total_taxes](https://docs.stripe.com/api/invoices/object.md?api-version=2026-04-22.dahlia#invoice_object-total_taxes)[].tax_rate_details.tax_rate and [lines](https://docs.stripe.com/api/invoices/object.md?api-version=2026-04-22.dahlia#invoice_object-lines).data[].taxes[].tax_rate_details.tax_rate
- [Invoice Line Item](https://docs.stripe.com/api/invoices/line_item.md?api-version=2026-04-22.dahlia): [taxes](https://docs.stripe.com/api/invoice-line-item/object.md?api-version=2026-04-22.dahlia#invoice_line_item_object-taxes)[].tax_rate_details.tax_rate
- [Credit Note](https://docs.stripe.com/api/credit_notes/object.md?api-version=2026-04-22.dahlia): [total_taxes](https://docs.stripe.com/api/credit_notes/object.md?api-version=2026-04-22.dahlia#credit_note_object-total_taxes)[].tax_rate_details.tax_rate
- [Credit Note Line Item](https://docs.stripe.com/api/credit_notes/line_item.md?api-version=2026-04-22.dahlia): [taxes](https://docs.stripe.com/api/credit_notes/line_item.md?api-version=2026-04-22.dahlia#credit_note_line_item_object-taxes)[].tax_rate_details.tax_rate

To expand the tax rate, include `tax_rate_details.tax_rate` in the [expand](https://docs.stripe.com/api/expanding_objects.md?api-version=2026-04-22.dahlia) parameter when retrieving these resources.

## Impact

Previously, the `tax_rate` property returned the Tax Rate ID as a string, requiring additional API calls to fetch the full Tax Rate object details.

Now you can access complete tax rate information, including the tax percentage and display name, without making separate API calls to retrieve Tax Rate objects. This can be useful when displaying tax breakdowns on invoices or receipts because you can show detailed tax information in a single request.

## Changes

#### REST API

| Fields | Change | From → to |
| --- | --- | --- |
| `CreditNote.total_taxes[].tax_rate_details.tax_rate`, `CreditNoteLineItem.taxes[].tax_rate_details.tax_rate`, `Invoice.total_taxes[].tax_rate_details.tax_rate`, `InvoiceLineItem.taxes[].tax_rate_details.tax_rate` | Changed | `string → expandable($TaxRate)` |

#### Ruby

| Fields | Change | From → to |
| --- | --- | --- |
| `CreditNote::TotalTax::TaxRateDetail.tax_rate`, `CreditNoteLineItem::Tax::TaxRateDetail.tax_rate`, `Invoice::TotalTax::TaxRateDetail.tax_rate`, `InvoiceLineItem::Tax::TaxRateDetail.tax_rate` | Changed | `string → expandable($TaxRate)` |

#### Python

| Fields | Change | From → to |
| --- | --- | --- |
| `CreditNote.TotalTax.TaxRateDetail.tax_rate`, `CreditNoteLineItem.Tax.TaxRateDetail.tax_rate`, `Invoice.TotalTax.TaxRateDetail.tax_rate`, `InvoiceLineItem.Tax.TaxRateDetail.tax_rate` | Changed | `string → expandable($TaxRate)` |

#### PHP

| Fields | Change | From → to |
| --- | --- | --- |
| `CreditNote.total_taxes[].tax_rate_details.tax_rate`, `CreditNoteLineItem.taxes[].tax_rate_details.tax_rate`, `Invoice.total_taxes[].tax_rate_details.tax_rate`, `InvoiceLineItem.taxes[].tax_rate_details.tax_rate` | Changed | `string → expandable($TaxRate)` |

#### Java

| Fields | Change | From → to |
| --- | --- | --- |
| `CreditNote.total_taxes[].tax_rate_details.taxRate`, `CreditNoteLineItem.taxes[].tax_rate_details.taxRate`, `Invoice.total_taxes[].tax_rate_details.taxRate`, `InvoiceLineItem.taxes[].tax_rate_details.taxRate` | Changed | `string → expandable($TaxRate)` |

#### Node.js

| Fields | Change | From → to |
| --- | --- | --- |
| `CreditNote.total_taxes[].tax_rate_details.tax_rate`, `CreditNoteLineItem.taxes[].tax_rate_details.tax_rate`, `Invoice.total_taxes[].tax_rate_details.tax_rate`, `InvoiceLineItem.taxes[].tax_rate_details.tax_rate` | Changed | `string → expandable(TaxRate)` |

#### Go

| Fields | Change | From → to |
| --- | --- | --- |
| `CreditNoteLineItemTaxesTaxRateDetails.TaxRate`, `CreditNoteTotalTaxesTaxRateDetails.TaxRate`, `InvoiceLineItemTaxesTaxRateDetails.TaxRate`, `InvoiceTotalTaxesTaxRateDetails.TaxRate` | Changed | `string → expandable($TaxRate)` |

#### .NET

| Fields | Change | From → to |
| --- | --- | --- |
| `CreditNote.TotalTaxes.TaxRateDetails.TaxRate`, `CreditNoteLineItem.Taxes.TaxRateDetails.TaxRate`, `Invoice.TotalTaxes.TaxRateDetails.TaxRate`, `InvoiceLineItem.Taxes.TaxRateDetails.TaxRate` | Changed | `string → expandable($TaxRate)` |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2026-04-22.dahlia`
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

- [Adds the ability to collect and store tax identification information for customers in the Faroe Islands, Gibraltar, Italy, and Paraguay](https://docs.stripe.com/changelog/dahlia/2026-04-22/new-tax-id-types-support.md)
