# Adds support for new tax types

## What’s new

Adds three new US tax types to [Stripe Tax](https://docs.stripe.com/tax.md): [digital_excise_tax](https://docs.stripe.com/api/tax/calculations/object.md?api-version=2026-09-30.endive#tax_calculation_object-tax_breakdown-tax_rate_details-tax_type), [utility_users_tax](https://docs.stripe.com/api/tax/calculations/object.md?api-version=2026-09-30.endive#tax_calculation_object-tax_breakdown-tax_rate_details-tax_type) and [recycling_fee](https://docs.stripe.com/api/tax/calculations/object.md?api-version=2026-09-30.endive#tax_calculation_object-tax_breakdown-tax_rate_details-tax_type).

## Impact

You can now identify digital excise tax, utility users tax, and recycling fee in [Tax Calculations](https://docs.stripe.com/api/tax/calculations/object.md?api-version=2026-09-30.endive). Use the `digital_excise_tax` or `utility_users_tax` type when [creating a custom Tax Rate](https://docs.stripe.com/api/tax_rates/create.md?api-version=2026-09-30.endive) or specifying [tax rate data for an invoice line item](https://docs.stripe.com/api/invoice-line-item/update.md?api-version=2026-09-30.endive#update_line-tax_amounts-tax_rate_data-tax_type).

## Changes

#### REST API

| Values | Change | Enums |
| --- | --- | --- |
| `digital_excise_tax`, `recycling_fee`, `utility_users_tax` | Added | [Tax.CalculationLineItem.tax_breakdown[].tax_rate_details.tax_type](/api/tax/calculations/object?api-version=2026-09-30.endive#tax_calculation_object-line_items-data-tax_breakdown-tax_rate_details-tax_type), [Tax.Calculation.shipping_cost.tax_breakdown[].tax_rate_details.tax_type](/api/tax/calculations/object?api-version=2026-09-30.endive#tax_calculation_object-shipping_cost-tax_breakdown-tax_rate_details-tax_type), [Tax.Calculation.tax_breakdown[].tax_rate_details.tax_type](/api/tax/calculations/object?api-version=2026-09-30.endive#tax_calculation_object-tax_breakdown-tax_rate_details-tax_type), [Tax.Transaction.shipping_cost.tax_breakdown[].tax_rate_details.tax_type](/api/tax/transactions/object?api-version=2026-09-30.endive#tax_transaction_object-shipping_cost-tax_breakdown-tax_rate_details-tax_type) |
| `digital_excise_tax`, `utility_users_tax` | Added | [Invoice#add_lines.lines[].tax_amounts[].tax_rate_data.tax_type](/api/invoice-line-item/bulk?api-version=2026-09-30.endive#bulk_add_lines-lines-tax_amounts-tax_rate_data-tax_type), [Invoice#update_lines.lines[].tax_amounts[].tax_rate_data.tax_type](/api/invoice-line-item/invoices/update-lines/bulk?api-version=2026-09-30.endive#bulk_update_lines-lines-tax_amounts-tax_rate_data-tax_type), [InvoiceLineItem#update.tax_amounts[].tax_rate_data.tax_type](/api/invoice-line-item/update?api-version=2026-09-30.endive#update_line-tax_amounts-tax_rate_data-tax_type), [TaxRate#create.tax_type](/api/tax_rates/create?api-version=2026-09-30.endive#create_tax_rate-tax_type), [TaxRate#update.tax_type](/api/tax_rates/update?api-version=2026-09-30.endive#update_tax_rate-tax_type), [TaxRate.tax_type](/api/tax_rates/object?api-version=2026-09-30.endive#tax_rate_object-tax_type) |

#### Ruby

This change doesn’t affect the Ruby SDK.

#### Python

| Values | Change | Enums |
| --- | --- | --- |
| `digital_excise_tax`, `recycling_fee`, `utility_users_tax` | Added | [Tax.CalculationLineItem.TaxBreakdown.TaxRateDetail.tax_type](/api/tax/calculations/object?api-version=2026-09-30.endive#tax_calculation_object-line_items-data-tax_breakdown-tax_rate_details-tax_type), [Tax.Calculation.ShippingCost.TaxBreakdown.TaxRateDetail.tax_type](/api/tax/calculations/object?api-version=2026-09-30.endive#tax_calculation_object-shipping_cost-tax_breakdown-tax_rate_details-tax_type), [Tax.Calculation.TaxBreakdown.TaxRateDetail.tax_type](/api/tax/calculations/object?api-version=2026-09-30.endive#tax_calculation_object-tax_breakdown-tax_rate_details-tax_type), [Tax.Transaction.ShippingCost.TaxBreakdown.TaxRateDetail.tax_type](/api/tax/transactions/object?api-version=2026-09-30.endive#tax_transaction_object-shipping_cost-tax_breakdown-tax_rate_details-tax_type) |
| `digital_excise_tax`, `utility_users_tax` | Added | [InvoiceAddLinesParamsLineTaxAmountTaxRateDatum.tax_type](/api/invoice-line-item/bulk?api-version=2026-09-30.endive#bulk_add_lines-lines-tax_amounts-tax_rate_data-tax_type), [InvoiceUpdateLinesParamsLineTaxAmountTaxRateDatum.tax_type](/api/invoice-line-item/invoices/update-lines/bulk?api-version=2026-09-30.endive#bulk_update_lines-lines-tax_amounts-tax_rate_data-tax_type), [InvoiceLineItemModifyParamsTaxAmountTaxRateDatum.tax_type](/api/invoice-line-item/update?api-version=2026-09-30.endive#update_line-tax_amounts-tax_rate_data-tax_type), [TaxRateCreateParams.tax_type](/api/tax_rates/create?api-version=2026-09-30.endive#create_tax_rate-tax_type), [TaxRateModifyParams.tax_type](/api/tax_rates/update?api-version=2026-09-30.endive#update_tax_rate-tax_type), [TaxRate.tax_type](/api/tax_rates/object?api-version=2026-09-30.endive#tax_rate_object-tax_type) |

#### PHP

| Values | Change | Enums |
| --- | --- | --- |
| `digital_excise_tax`, `recycling_fee`, `utility_users_tax` | Added | [Tax.CalculationLineItem.tax_breakdown[].tax_rate_details.tax_type](/api/tax/calculations/object?api-version=2026-09-30.endive#tax_calculation_object-line_items-data-tax_breakdown-tax_rate_details-tax_type), [Tax.Calculation.shipping_cost.tax_breakdown[].tax_rate_details.tax_type](/api/tax/calculations/object?api-version=2026-09-30.endive#tax_calculation_object-shipping_cost-tax_breakdown-tax_rate_details-tax_type), [Tax.Calculation.tax_breakdown[].tax_rate_details.tax_type](/api/tax/calculations/object?api-version=2026-09-30.endive#tax_calculation_object-tax_breakdown-tax_rate_details-tax_type), [Tax.Transaction.shipping_cost.tax_breakdown[].tax_rate_details.tax_type](/api/tax/transactions/object?api-version=2026-09-30.endive#tax_transaction_object-shipping_cost-tax_breakdown-tax_rate_details-tax_type) |
| `digital_excise_tax`, `utility_users_tax` | Added | [TaxRate.tax_type](/api/tax_rates/object?api-version=2026-09-30.endive#tax_rate_object-tax_type) |

#### Java

| Values | Change | Enums |
| --- | --- | --- |
| `digital_excise_tax`, `utility_users_tax` | Added | [InvoiceAddLinesParams.lines[].tax_amounts[].tax_rate_data.taxType](/api/invoice-line-item/bulk?api-version=2026-09-30.endive#bulk_add_lines-lines-tax_amounts-tax_rate_data-taxType), [InvoiceUpdateLinesParams.lines[].tax_amounts[].tax_rate_data.taxType](/api/invoice-line-item/invoices/update-lines/bulk?api-version=2026-09-30.endive#bulk_update_lines-lines-tax_amounts-tax_rate_data-taxType), [InvoiceLineItemUpdateParams.tax_amounts[].tax_rate_data.taxType](/api/invoice-line-item/update?api-version=2026-09-30.endive#update_line-tax_amounts-tax_rate_data-taxType), [TaxRateCreateParams.taxType](/api/tax_rates/create?api-version=2026-09-30.endive#create_tax_rate-taxType), [TaxRateUpdateParams.taxType](/api/tax_rates/update?api-version=2026-09-30.endive#update_tax_rate-taxType) |

#### Node.js

| Values | Change | Enums |
| --- | --- | --- |
| `digital_excise_tax`, `recycling_fee`, `utility_users_tax` | Added | [Tax.CalculationLineItem.tax_breakdown[].tax_rate_details.tax_type](/api/tax/calculations/object?api-version=2026-09-30.endive#tax_calculation_object-line_items-data-tax_breakdown-tax_rate_details-tax_type), [Tax.Calculation.shipping_cost.tax_breakdown[].tax_rate_details.tax_type](/api/tax/calculations/object?api-version=2026-09-30.endive#tax_calculation_object-shipping_cost-tax_breakdown-tax_rate_details-tax_type), [Tax.Calculation.tax_breakdown[].tax_rate_details.tax_type](/api/tax/calculations/object?api-version=2026-09-30.endive#tax_calculation_object-tax_breakdown-tax_rate_details-tax_type), [Tax.Transaction.shipping_cost.tax_breakdown[].tax_rate_details.tax_type](/api/tax/transactions/object?api-version=2026-09-30.endive#tax_transaction_object-shipping_cost-tax_breakdown-tax_rate_details-tax_type) |
| `digital_excise_tax`, `utility_users_tax` | Added | [InvoiceAddLinesParams.lines[].tax_amounts[].tax_rate_data.tax_type](/api/invoice-line-item/bulk?api-version=2026-09-30.endive#bulk_add_lines-lines-tax_amounts-tax_rate_data-tax_type), [InvoiceUpdateLinesParams.lines[].tax_amounts[].tax_rate_data.tax_type](/api/invoice-line-item/invoices/update-lines/bulk?api-version=2026-09-30.endive#bulk_update_lines-lines-tax_amounts-tax_rate_data-tax_type), [InvoiceLineItemUpdateParams.tax_amounts[].tax_rate_data.tax_type](/api/invoice-line-item/update?api-version=2026-09-30.endive#update_line-tax_amounts-tax_rate_data-tax_type), [TaxRateCreateParams.tax_type](/api/tax_rates/create?api-version=2026-09-30.endive#create_tax_rate-tax_type), [TaxRateUpdateParams.tax_type](/api/tax_rates/update?api-version=2026-09-30.endive#update_tax_rate-tax_type), [TaxRate.tax_type](/api/tax_rates/object?api-version=2026-09-30.endive#tax_rate_object-tax_type) |

#### Go

| Values | Change | Enums |
| --- | --- | --- |
| `digital_excise_tax`, `recycling_fee`, `utility_users_tax` | Added | [TaxCalculationLineItemTaxBreakdownTaxRateDetails.TaxType](/api/tax/calculations/object?api-version=2026-09-30.endive#tax_calculation_object-line_items-data-tax_breakdown-tax_rate_details-tax_type), [TaxCalculationShippingCostTaxBreakdownTaxRateDetails.TaxType](/api/tax/calculations/object?api-version=2026-09-30.endive#tax_calculation_object-shipping_cost-tax_breakdown-tax_rate_details-tax_type), [TaxCalculationTaxBreakdownTaxRateDetails.TaxType](/api/tax/calculations/object?api-version=2026-09-30.endive#tax_calculation_object-tax_breakdown-tax_rate_details-tax_type), [TaxTransactionShippingCostTaxBreakdownTaxRateDetails.TaxType](/api/tax/transactions/object?api-version=2026-09-30.endive#tax_transaction_object-shipping_cost-tax_breakdown-tax_rate_details-tax_type) |
| `digital_excise_tax`, `utility_users_tax` | Added | [TaxRate.TaxType](/api/tax_rates/object?api-version=2026-09-30.endive#tax_rate_object-tax_type) |

#### .NET

This change doesn’t affect the .NET SDK.

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

- [Adds Failed Tax Calculation error](https://docs.stripe.com/changelog/endive/2026-09-30/failed-tax-calculation-error.md)
- [Adds support for ticket sales to Stripe Tax](https://docs.stripe.com/changelog/endive/2026-09-30/stripe-tax-tickets.md)
