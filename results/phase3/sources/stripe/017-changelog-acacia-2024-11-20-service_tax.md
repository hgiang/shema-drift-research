# Adds support for Service Tax type

## What’s new

Adds `service_tax` to the list of possible enum values for [tax_type](https://docs.stripe.com/api/tax_rates/update.md?api-version=2024-11-20.acacia#update_tax_rate-tax_type) in the [Tax Rate](https://docs.stripe.com/api/tax_rates.md?api-version=2024-11-20.acacia) resource.

## Impact

This change lets you accurately collect Service Tax in [Malaysia](https://docs.stripe.com/tax/supported-countries/asia-pacific.md?tax-jurisdiction-asia-pacific=malaysia) on digital products.

## Changes

#### REST API

| Value | Change | Enums |
| --- | --- | --- |
| `service_tax` | Added | [Invoice#add_lines.lines[].tax_amounts[].tax_rate_data.tax_type](/api/invoice-line-item/bulk?api-version=2024-11-20.acacia#bulk_add_lines-lines-tax_amounts-tax_rate_data-tax_type), [Invoice#update_lines.lines[].tax_amounts[].tax_rate_data.tax_type](/api/invoice-line-item/invoices/update-lines/bulk?api-version=2024-11-20.acacia#bulk_update_lines-lines-tax_amounts-tax_rate_data-tax_type), [Tax.Calculation.shipping_cost.tax_breakdown[].tax_rate_details.tax_type](/api/tax/calculations/object?api-version=2024-11-20.acacia#tax_calculation_object-shipping_cost-tax_breakdown-tax_rate_details-tax_type), [Tax.Calculation.tax_breakdown[].tax_rate_details.tax_type](/api/tax/calculations/object?api-version=2024-11-20.acacia#tax_calculation_object-tax_breakdown-tax_rate_details-tax_type), [Tax.CalculationLineItem.tax_breakdown[].tax_rate_details.tax_type](/api/tax/calculations/object?api-version=2024-11-20.acacia#tax_calculation_object-line_items-data-tax_breakdown-tax_rate_details-tax_type), [Tax.Transaction.shipping_cost.tax_breakdown[].tax_rate_details.tax_type](/api/tax/calculations/object?api-version=2024-11-20.acacia#tax_calculation_object-tax_breakdown-tax_rate_details-tax_type), [TaxRate#create.tax_type](/api/tax_rates/create?api-version=2024-11-20.acacia#create_tax_rate-tax_type), [TaxRate#update.tax_type](/api/tax_rates/update?api-version=2024-11-20.acacia#update_tax_rate-tax_type), [TaxRate.tax_type](/api/tax_rates/object?api-version=2024-11-20.acacia#tax_rate_object-tax_type) |

#### Ruby

This change doesn’t affect the Ruby SDK.

#### Python

| Value | Change | Enums |
| --- | --- | --- |
| `service_tax` | Added | [stripe.Invoice.AddLinesParamsLineTaxAmountTaxRateData.tax_type](/api/invoice-line-item/bulk?api-version=2024-11-20.acacia#bulk_add_lines-lines-tax_amounts-tax_rate_data-tax_type), [stripe.Invoice.UpdateLinesParamsLineTaxAmountTaxRateData.tax_type](/api/invoice-line-item/invoices/update-lines/bulk?api-version=2024-11-20.acacia#bulk_update_lines-lines-tax_amounts-tax_rate_data-tax_type), [stripe.InvoiceLineItem.ModifyParamsTaxAmountTaxRateData.tax_type](/api/invoice-line-item/update?api-version=2024-11-20.acacia#update_line-tax_amounts-tax_rate_data-tax_type), [stripe.tax.Calculation.ShippingCost.TaxBreakdown.TaxRateDetails.tax_type](/api/tax/calculations/object?api-version=2024-11-20.acacia#tax_calculation_object-shipping_cost-tax_breakdown-tax_rate_details-tax_type), [stripe.tax.Calculation.TaxBreakdown.TaxRateDetails.tax_type](/api/tax/calculations/object?api-version=2024-11-20.acacia#tax_calculation_object-tax_breakdown-tax_rate_details-tax_type), [stripe.tax.CalculationLineItem.TaxBreakdown.TaxRateDetails.tax_type](/api/tax/calculations/object?api-version=2024-11-20.acacia#tax_calculation_object-line_items-data-tax_breakdown-tax_rate_details-tax_type), [stripe.tax.Transaction.ShippingCost.TaxBreakdown.TaxRateDetails.tax_type](/api/tax/calculations/object?api-version=2024-11-20.acacia#tax_calculation_object-tax_breakdown-tax_rate_details-tax_type), [stripe.TaxRate.tax_type](/api/tax_rates/object?api-version=2024-11-20.acacia#tax_rate_object-tax_type), [stripe.TaxRate.CreateParams.tax_type](/api/tax_rates/create?api-version=2024-11-20.acacia#create_tax_rate-tax_type), [stripe.TaxRate.ModifyParams.tax_type](/api/tax_rates/update?api-version=2024-11-20.acacia#update_tax_rate-tax_type) |

#### PHP

| Value | Change | Enum |
| --- | --- | --- |
| `service_tax` | Added | [TaxRate.tax_type](/api/tax_rates/object?api-version=2024-11-20.acacia#tax_rate_object-tax_type) |

#### Java

| Value | Change | Enums |
| --- | --- | --- |
| `service_tax` | Added | [InvoiceAddLinesParams.lines[].tax_amounts[].tax_rate_data.tax_type](/api/invoice-line-item/bulk?api-version=2024-11-20.acacia#bulk_add_lines-lines-tax_amounts-tax_rate_data-tax_type), [InvoiceUpdateLinesParams.lines[].tax_amounts[].tax_rate_data.tax_type](/api/invoice-line-item/invoices/update-lines/bulk?api-version=2024-11-20.acacia#bulk_update_lines-lines-tax_amounts-tax_rate_data-tax_type), [TaxRateCreateParams.tax_type](/api/tax_rates/create?api-version=2024-11-20.acacia#create_tax_rate-tax_type), [TaxRateUpdateParams.tax_type](/api/tax_rates/update?api-version=2024-11-20.acacia#update_tax_rate-tax_type) |

#### Node.js

| Value | Change | Enums |
| --- | --- | --- |
| `service_tax` | Added | [InvoiceAddLinesParams.lines[].tax_amounts[].tax_rate_data.tax_type](/api/invoice-line-item/bulk?api-version=2024-11-20.acacia#bulk_add_lines-lines-tax_amounts-tax_rate_data-tax_type), [InvoiceUpdateLinesParams.lines[].tax_amounts[].tax_rate_data.tax_type](/api/invoice-line-item/invoices/update-lines/bulk?api-version=2024-11-20.acacia#bulk_update_lines-lines-tax_amounts-tax_rate_data-tax_type), [Tax.Calculation.shipping_cost.tax_breakdown[].tax_rate_details.tax_type](/api/tax/calculations/object?api-version=2024-11-20.acacia#tax_calculation_object-shipping_cost-tax_breakdown-tax_rate_details-tax_type), [Tax.Calculation.tax_breakdown[].tax_rate_details.tax_type](/api/tax/calculations/object?api-version=2024-11-20.acacia#tax_calculation_object-tax_breakdown-tax_rate_details-tax_type), [Tax.CalculationLineItem.tax_breakdown[].tax_rate_details.tax_type](/api/tax/calculations/object?api-version=2024-11-20.acacia#tax_calculation_object-line_items-data-tax_breakdown-tax_rate_details-tax_type), [Tax.Transaction.shipping_cost.tax_breakdown[].tax_rate_details.tax_type](/api/tax/calculations/object?api-version=2024-11-20.acacia#tax_calculation_object-tax_breakdown-tax_rate_details-tax_type), [TaxRate.tax_type](/api/tax_rates/object?api-version=2024-11-20.acacia#tax_rate_object-tax_type), [TaxRateCreateParams.tax_type](/api/tax_rates/create?api-version=2024-11-20.acacia#create_tax_rate-tax_type), [TaxRateUpdateParams.tax_type](/api/tax_rates/update?api-version=2024-11-20.acacia#update_tax_rate-tax_type) |

#### Go

| Value | Change | Enums |
| --- | --- | --- |
| `service_tax` | Added | [TaxCalculationLineItemTaxBreakdownTaxRateDetailsTaxType](/api/tax/calculations/object?api-version=2024-11-20.acacia#tax_calculation_object-line_items-data-tax_breakdown-tax_rate_details-tax_type), [TaxCalculationShippingCostTaxBreakdownTaxRateDetailsTaxType](/api/tax/calculations/object?api-version=2024-11-20.acacia#tax_calculation_object-shipping_cost-tax_breakdown-tax_rate_details-tax_type), [TaxCalculationTaxBreakdownTaxRateDetailsTaxType](/api/tax/calculations/object?api-version=2024-11-20.acacia#tax_calculation_object-tax_breakdown-tax_rate_details-tax_type), [TaxRateTaxType](/api/tax_rates/object?api-version=2024-11-20.acacia#tax_rate_object-tax_type), [TaxTransactionShippingCostTaxBreakdownTaxRateDetailsTaxType](/api/tax/calculations/object?api-version=2024-11-20.acacia#tax_calculation_object-tax_breakdown-tax_rate_details-tax_type) |

#### .NET

This change doesn’t affect the .NET SDK.

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2024-11-20.acacia`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to [v13.2.0](https://github.com/stripe/stripe-ruby/releases/tag/v13.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to [v11.3.0](https://github.com/stripe/stripe-python/releases/tag/v11.3.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to [v16.3.0](https://github.com/stripe/stripe-php/releases/tag/v16.3.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to [v28.1.0](https://github.com/stripe/stripe-java/releases/tag/v28.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to [v17.4.0](https://github.com/stripe/stripe-node/releases/tag/v17.4.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to [v81.1.0](https://github.com/stripe/stripe-go/releases/tag/v81.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to [v47.1.0](https://github.com/stripe/stripe-dotnet/releases/tag/v47.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

## Related changes

- [Adds tax ID support for Liechtenstein VAT](https://docs.stripe.com/changelog/acacia/2024-11-20/li_vat.md)
