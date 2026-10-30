# Adds support for parking tax registration types in the US

## What’s new

Adds two new registration types for US tax registrations: [parking_tax](https://docs.stripe.com/api/tax/registrations/create.md?api-version=2026-07-29.dahlia#tax_registration_create-country_options-us-parking_tax) and [mass_transit_parking_tax](https://docs.stripe.com/api/tax/registrations/create.md?api-version=2026-07-29.dahlia#tax_registration_create-country_options-us-mass_transit_parking_tax). Specify these types using the [country_options.us.type](https://docs.stripe.com/api/tax/registrations/create.md?api-version=2026-07-29.dahlia#tax_registration_create-country_options-us-type) parameter when you [create a tax registration](https://docs.stripe.com/api/tax/registrations/create.md?api-version=2026-07-29.dahlia).

Each registration type accepts a [jurisdiction](https://docs.stripe.com/api/tax/registrations/create.md?api-version=2026-07-29.dahlia#tax_registration_create-country_options-us-parking_tax-jurisdiction) parameter that takes a FIPS code to identify the specific taxing jurisdiction.

## Impact

You can now register to collect and remit parking taxes and mass transit parking taxes in applicable US jurisdictions using [Stripe Tax](https://docs.stripe.com/tax.md). Use the `parking_tax` or `mass_transit_parking_tax` type along with the appropriate jurisdiction FIPS code when [creating a registration](https://docs.stripe.com/api/tax/registrations/create.md?api-version=2026-07-29.dahlia) for these tax types.

## Changes

#### REST API

| Parameters | Change | Resources or endpoints |
| --- | --- | --- |
| `mass_transit_parking_tax`, `parking_tax` | Added | [Tax.Registration#create.country_options.us](/api/tax/registrations/create?api-version=2026-07-29.dahlia#tax_registration_create-country_options-us), [Tax.Registration.country_options.us](/api/tax/registrations/object?api-version=2026-07-29.dahlia#tax_registration_object-country_options-us) |

| Values | Change | Enums |
| --- | --- | --- |
| `mass_transit_parking_tax`, `parking_tax` | Added | [Tax.CalculationLineItem.tax_breakdown[].tax_rate_details.tax_type](/api/tax/calculations/object?api-version=2026-07-29.dahlia#tax_calculation_object-line_items-data-tax_breakdown-tax_rate_details-tax_type), [Tax.Calculation.shipping_cost.tax_breakdown[].tax_rate_details.tax_type](/api/tax/calculations/object?api-version=2026-07-29.dahlia#tax_calculation_object-shipping_cost-tax_breakdown-tax_rate_details-tax_type), [Tax.Calculation.tax_breakdown[].tax_rate_details.tax_type](/api/tax/calculations/object?api-version=2026-07-29.dahlia#tax_calculation_object-tax_breakdown-tax_rate_details-tax_type), [Tax.Transaction.shipping_cost.tax_breakdown[].tax_rate_details.tax_type](/api/tax/transactions/object?api-version=2026-07-29.dahlia#tax_transaction_object-shipping_cost-tax_breakdown-tax_rate_details-tax_type), [TaxRate.tax_type](/api/tax_rates/object?api-version=2026-07-29.dahlia#tax_rate_object-tax_type), [Invoice#add_lines.lines[].tax_amounts[].tax_rate_data.tax_type](/api/invoice-line-item/bulk?api-version=2026-07-29.dahlia#bulk_add_lines-lines-tax_amounts-tax_rate_data-tax_type), [Invoice#update_lines.lines[].tax_amounts[].tax_rate_data.tax_type](/api/invoice-line-item/invoices/update-lines/bulk?api-version=2026-07-29.dahlia#bulk_update_lines-lines-tax_amounts-tax_rate_data-tax_type), [InvoiceLineItem#update.tax_amounts[].tax_rate_data.tax_type](/api/invoice-line-item/update?api-version=2026-07-29.dahlia#update_line-tax_amounts-tax_rate_data-tax_type), [TaxRate#create.tax_type](/api/tax_rates/create?api-version=2026-07-29.dahlia#create_tax_rate-tax_type), [TaxRate#update.tax_type](/api/tax_rates/update?api-version=2026-07-29.dahlia#update_tax_rate-tax_type), [Tax.Registration#create.country_options.us.type](/api/tax/registrations/create?api-version=2026-07-29.dahlia#tax_registration_create-country_options-us-type), [Tax.Registration.country_options.us.type](/api/tax/registrations/object?api-version=2026-07-29.dahlia#tax_registration_object-country_options-us-type) |

#### Ruby

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `mass_transit_parking_tax`, `parking_tax` | Added | [Tax::Registration::CountryOption::Us](/api/tax/registrations/object?api-version=2026-07-29.dahlia#tax_registration_object-country_options-us), [Tax::RegistrationCreateParams::CountryOption::Us](/api/tax/registrations/create?api-version=2026-07-29.dahlia#tax_registration_create-country_options-us) |

#### Python

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `mass_transit_parking_tax`, `parking_tax` | Added | [Tax.Registration.CountryOption.Us](/api/tax/registrations/object?api-version=2026-07-29.dahlia#tax_registration_object-country_options-us), [tax.RegistrationCreateParamsCountryOptionUs](/api/tax/registrations/create?api-version=2026-07-29.dahlia#tax_registration_create-country_options-us) |

| Values | Change | Enums |
| --- | --- | --- |
| `mass_transit_parking_tax`, `parking_tax` | Added | [Tax.CalculationLineItem.TaxBreakdown.TaxRateDetail.tax_type](/api/tax/calculations/object?api-version=2026-07-29.dahlia#tax_calculation_object-line_items-data-tax_breakdown-tax_rate_details-tax_type), [Tax.Calculation.ShippingCost.TaxBreakdown.TaxRateDetail.tax_type](/api/tax/calculations/object?api-version=2026-07-29.dahlia#tax_calculation_object-shipping_cost-tax_breakdown-tax_rate_details-tax_type), [Tax.Calculation.TaxBreakdown.TaxRateDetail.tax_type](/api/tax/calculations/object?api-version=2026-07-29.dahlia#tax_calculation_object-tax_breakdown-tax_rate_details-tax_type), [Tax.Transaction.ShippingCost.TaxBreakdown.TaxRateDetail.tax_type](/api/tax/transactions/object?api-version=2026-07-29.dahlia#tax_transaction_object-shipping_cost-tax_breakdown-tax_rate_details-tax_type), [TaxRate.tax_type](/api/tax_rates/object?api-version=2026-07-29.dahlia#tax_rate_object-tax_type), [InvoiceAddLinesParamsLineTaxAmountTaxRateDatum.tax_type](/api/invoice-line-item/bulk?api-version=2026-07-29.dahlia#bulk_add_lines-lines-tax_amounts-tax_rate_data-tax_type), [InvoiceUpdateLinesParamsLineTaxAmountTaxRateDatum.tax_type](/api/invoice-line-item/invoices/update-lines/bulk?api-version=2026-07-29.dahlia#bulk_update_lines-lines-tax_amounts-tax_rate_data-tax_type), [InvoiceLineItemModifyParamsTaxAmountTaxRateDatum.tax_type](/api/invoice-line-item/update?api-version=2026-07-29.dahlia#update_line-tax_amounts-tax_rate_data-tax_type), [TaxRateCreateParams.tax_type](/api/tax_rates/create?api-version=2026-07-29.dahlia#create_tax_rate-tax_type), [TaxRateModifyParams.tax_type](/api/tax_rates/update?api-version=2026-07-29.dahlia#update_tax_rate-tax_type), [tax.RegistrationCreateParamsCountryOptionUs.type](/api/tax/registrations/create?api-version=2026-07-29.dahlia#tax_registration_create-country_options-us-type), [Tax.Registration.CountryOption.Us.type](/api/tax/registrations/object?api-version=2026-07-29.dahlia#tax_registration_object-country_options-us-type) |

#### PHP

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `mass_transit_parking_tax`, `parking_tax` | Added | [Tax.Registration.country_options.us](/api/tax/registrations/object?api-version=2026-07-29.dahlia#tax_registration_object-country_options-us), [Tax\Registration.create().$params.country_options.us](/api/tax/registrations/create?api-version=2026-07-29.dahlia#tax_registration_create-country_options-us) |

| Values | Change | Enums |
| --- | --- | --- |
| `mass_transit_parking_tax`, `parking_tax` | Added | [Tax.CalculationLineItem.tax_breakdown[].tax_rate_details.tax_type](/api/tax/calculations/object?api-version=2026-07-29.dahlia#tax_calculation_object-line_items-data-tax_breakdown-tax_rate_details-tax_type), [Tax.Calculation.shipping_cost.tax_breakdown[].tax_rate_details.tax_type](/api/tax/calculations/object?api-version=2026-07-29.dahlia#tax_calculation_object-shipping_cost-tax_breakdown-tax_rate_details-tax_type), [Tax.Calculation.tax_breakdown[].tax_rate_details.tax_type](/api/tax/calculations/object?api-version=2026-07-29.dahlia#tax_calculation_object-tax_breakdown-tax_rate_details-tax_type), [Tax.Transaction.shipping_cost.tax_breakdown[].tax_rate_details.tax_type](/api/tax/transactions/object?api-version=2026-07-29.dahlia#tax_transaction_object-shipping_cost-tax_breakdown-tax_rate_details-tax_type), [TaxRate.tax_type](/api/tax_rates/object?api-version=2026-07-29.dahlia#tax_rate_object-tax_type), [Tax.Registration.country_options.us.type](/api/tax/registrations/object?api-version=2026-07-29.dahlia#tax_registration_object-country_options-us-type) |

#### Java

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `massTransitParkingTax`, `parkingTax` | Added | [tax.Registration.country_options.us](/api/tax/registrations/object?api-version=2026-07-29.dahlia#tax_registration_object-country_options-us), [tax.RegistrationCreateParams.country_options.us](/api/tax/registrations/create?api-version=2026-07-29.dahlia#tax_registration_create-country_options-us) |

| Values | Change | Enums |
| --- | --- | --- |
| `mass_transit_parking_tax`, `parking_tax` | Added | [InvoiceAddLinesParams.lines[].tax_amounts[].tax_rate_data.taxType](/api/invoice-line-item/bulk?api-version=2026-07-29.dahlia#bulk_add_lines-lines-tax_amounts-tax_rate_data-taxType), [InvoiceUpdateLinesParams.lines[].tax_amounts[].tax_rate_data.taxType](/api/invoice-line-item/invoices/update-lines/bulk?api-version=2026-07-29.dahlia#bulk_update_lines-lines-tax_amounts-tax_rate_data-taxType), [InvoiceLineItemUpdateParams.tax_amounts[].tax_rate_data.taxType](/api/invoice-line-item/update?api-version=2026-07-29.dahlia#update_line-tax_amounts-tax_rate_data-taxType), [TaxRateCreateParams.taxType](/api/tax_rates/create?api-version=2026-07-29.dahlia#create_tax_rate-taxType), [TaxRateUpdateParams.taxType](/api/tax_rates/update?api-version=2026-07-29.dahlia#update_tax_rate-taxType), [tax.RegistrationCreateParams.country_options.us.type](/api/tax/registrations/create?api-version=2026-07-29.dahlia#tax_registration_create-country_options-us-type) |

#### Node.js

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `mass_transit_parking_tax`, `parking_tax` | Added | [Tax.Registration.country_options.us](/api/tax/registrations/object?api-version=2026-07-29.dahlia#tax_registration_object-country_options-us), [Tax.RegistrationCreateParams.country_options.us](/api/tax/registrations/create?api-version=2026-07-29.dahlia#tax_registration_create-country_options-us) |

| Values | Change | Enums |
| --- | --- | --- |
| `mass_transit_parking_tax`, `parking_tax` | Added | [Tax.CalculationLineItem.tax_breakdown[].tax_rate_details.tax_type](/api/tax/calculations/object?api-version=2026-07-29.dahlia#tax_calculation_object-line_items-data-tax_breakdown-tax_rate_details-tax_type), [Tax.Calculation.shipping_cost.tax_breakdown[].tax_rate_details.tax_type](/api/tax/calculations/object?api-version=2026-07-29.dahlia#tax_calculation_object-shipping_cost-tax_breakdown-tax_rate_details-tax_type), [Tax.Calculation.tax_breakdown[].tax_rate_details.tax_type](/api/tax/calculations/object?api-version=2026-07-29.dahlia#tax_calculation_object-tax_breakdown-tax_rate_details-tax_type), [Tax.Transaction.shipping_cost.tax_breakdown[].tax_rate_details.tax_type](/api/tax/transactions/object?api-version=2026-07-29.dahlia#tax_transaction_object-shipping_cost-tax_breakdown-tax_rate_details-tax_type), [TaxRate.tax_type](/api/tax_rates/object?api-version=2026-07-29.dahlia#tax_rate_object-tax_type), [InvoiceAddLinesParams.lines[].tax_amounts[].tax_rate_data.tax_type](/api/invoice-line-item/bulk?api-version=2026-07-29.dahlia#bulk_add_lines-lines-tax_amounts-tax_rate_data-tax_type), [InvoiceUpdateLinesParams.lines[].tax_amounts[].tax_rate_data.tax_type](/api/invoice-line-item/invoices/update-lines/bulk?api-version=2026-07-29.dahlia#bulk_update_lines-lines-tax_amounts-tax_rate_data-tax_type), [InvoiceLineItemUpdateParams.tax_amounts[].tax_rate_data.tax_type](/api/invoice-line-item/update?api-version=2026-07-29.dahlia#update_line-tax_amounts-tax_rate_data-tax_type), [TaxRateCreateParams.tax_type](/api/tax_rates/create?api-version=2026-07-29.dahlia#create_tax_rate-tax_type), [TaxRateUpdateParams.tax_type](/api/tax_rates/update?api-version=2026-07-29.dahlia#update_tax_rate-tax_type), [Tax.RegistrationCreateParams.country_options.us.type](/api/tax/registrations/create?api-version=2026-07-29.dahlia#tax_registration_create-country_options-us-type), [Tax.Registration.country_options.us.type](/api/tax/registrations/object?api-version=2026-07-29.dahlia#tax_registration_object-country_options-us-type) |

#### Go

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `MassTransitParkingTax`, `ParkingTax` | Added | [TaxRegistrationCountryOptionsUs](/api/tax/registrations/object?api-version=2026-07-29.dahlia#tax_registration_object-country_options-us), [TaxRegistrationCountryOptionsUsParams](/api/tax/registrations/create?api-version=2026-07-29.dahlia#tax_registration_create-country_options-us) |

| Values | Change | Enums |
| --- | --- | --- |
| `mass_transit_parking_tax`, `parking_tax` | Added | [TaxCalculationLineItemTaxBreakdownTaxRateDetails.TaxType](/api/tax/calculations/object?api-version=2026-07-29.dahlia#tax_calculation_object-line_items-data-tax_breakdown-tax_rate_details-tax_type), [TaxCalculationShippingCostTaxBreakdownTaxRateDetails.TaxType](/api/tax/calculations/object?api-version=2026-07-29.dahlia#tax_calculation_object-shipping_cost-tax_breakdown-tax_rate_details-TaxType), [TaxCalculationTaxBreakdownTaxRateDetails.TaxType](/api/tax/calculations/object?api-version=2026-07-29.dahlia#tax_calculation_object-tax_breakdown-tax_rate_details-TaxType), [TaxTransactionShippingCostTaxBreakdownTaxRateDetails.TaxType](/api/tax/transactions/object?api-version=2026-07-29.dahlia#tax_transaction_object-shipping_cost-tax_breakdown-tax_rate_details-TaxType), [TaxRate.TaxType](/api/tax_rates/object?api-version=2026-07-29.dahlia#tax_rate_object-TaxType), [TaxRegistrationCountryOptionsUs.Type](/api/tax/registrations/object?api-version=2026-07-29.dahlia#tax_registration_object-country_options-us-Type) |

#### .NET

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `MassTransitParkingTax`, `ParkingTax` | Added | [Tax.Registration.CountryOptions.Us](/api/tax/registrations/object?api-version=2026-07-29.dahlia#tax_registration_object-country_options-us), [TaxRegistrationCountryOptionsUsOptions](/api/tax/registrations/create?api-version=2026-07-29.dahlia#tax_registration_create-country_options-us) |

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

- [Adds support for Canary Islands tax ID type](https://docs.stripe.com/changelog/dahlia/2026-07-29/canary-islands-tax-id-type.md)
