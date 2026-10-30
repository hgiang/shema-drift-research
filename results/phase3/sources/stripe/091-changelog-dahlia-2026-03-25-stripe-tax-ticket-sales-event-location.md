# Adds Stripe Tax support for ticket sales

## What’s new

Adds Stripe Tax support for [calculating tax on ticket sales and other event transactions](https://docs.stripe.com/tax/tax-for-tickets/integration-guide.md) based on event location rather than customer location.

Adds support for [tax on ticket sales](https://docs.stripe.com/tax/tax-for-tickets/integration-guide.md) to Stripe Tax using the following new elements:

- The [Tax Locations](https://docs.stripe.com/api/tax/location.md?api-version=2026-03-25.preview) API for managing venues and event spaces
- Performance location properties on existing Stripe Tax APIs and the [Products API](https://docs.stripe.com/api/products/create.md?api-version=2026-03-25.preview#create_product-tax_details-performance_location)
- A [requirements.performance_location property](https://docs.stripe.com/api/tax_codes/object.md?api-version=2026-03-25.preview#tax_code_object-requirements-performance_location) on the `TaxCode` object that indicates whether a particular tax code supports or requires a performance location
- The following tax registration enum values on the `TaxRegistration` object’s [country_options.us.type](https://docs.stripe.com/api/tax/registrations/object.md?api-version=2026-03-25.preview#tax_registration_object-country_options-us-type) property:
  - `admissions_tax`
  - `entertainment_tax`
  - `tourism_tax`

## Impact

If you sell tickets or other event-based goods and services and use Stripe Tax, you can now calculate tax based on the event’s location instead of the customer’s location. To do so, create a `Tax Location` object representing the event location and pass its ID as the `performance_location` when calculating tax.

You can also support event-related US tax registration types and access event-related tax breakdown values.

## Changes

#### REST API

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [Tax.Location](/api/tax/location/object?api-version=2026-03-25.preview) |

| Endpoints | Change | Resource |
| --- | --- | --- |
| `create`, `list`, `retrieve` | Added | [Tax.Location](/api/tax/location/object?api-version=2026-03-25.preview) |

| Parameters | Change | Resources or endpoints |
| --- | --- | --- |
| `performance_location` | Added | [Tax.Calculation#create.line_items[]](/api/tax/calculations/create?api-version=2026-03-25.preview#calculate_tax-line_items), `Tax.CalculationLineItem` |
| `tax_details` | Added | [Checkout.Session#create.line_items[].price_data.product_data](/api/checkout/sessions/create?api-version=2026-03-25.preview#create_checkout_session-line_items-price_data-product_data), [Checkout.Session#update.line_items[].price_data.product_data](/api/checkout/sessions/update?api-version=2026-03-25.preview#update_checkout_session-line_items-price_data-product_data), [Invoice#add_lines.lines[].price_data.product_data](/api/invoice-line-item/bulk?api-version=2026-03-25.preview#bulk_add_lines-lines-price_data-product_data), [Invoice#update_lines.lines[].price_data.product_data](/api/invoice-line-item/invoices/update-lines/bulk?api-version=2026-03-25.preview#bulk_update_lines-lines-price_data-product_data), [InvoiceLineItem#update.price_data.product_data](/api/invoice-line-item/update?api-version=2026-03-25.preview#update_line-price_data-product_data), [PaymentLink#create.line_items[].price_data.product_data](/api/payment-link/create?api-version=2026-03-25.preview#create_payment_link-line_items-price_data-product_data), [Plan#create.product[0]](/api/plans/create?api-version=2026-03-25.preview#create_plan-product-[0]), [Price#create.product_data](/api/prices/create?api-version=2026-03-25.preview#create_price-product_data), [Product#create](/api/products/create?api-version=2026-03-25.preview), [Product#update](/api/products/update?api-version=2026-03-25.preview) |
| `admissions_tax`, `attendance_tax`, `entertainment_tax`, `gross_receipts_tax`, `hospitality_tax`, `luxury_tax`, `resort_tax`, `tourism_tax` | Added | [Tax.Registration.country_options.us](/api/tax/registrations/object?api-version=2026-03-25.preview#tax_registration_object-country_options-us) |
| `requirements` | Added | [TaxCode](/api/tax_codes/object?api-version=2026-03-25.preview) |

| Values | Change | Enums |
| --- | --- | --- |
| `performance` | Added | `Tax.CalculationLineItem.tax_breakdown[]`, `Tax.Calculation.shipping_cost.tax_breakdown[]`, `Tax.Transaction.shipping_cost.tax_breakdown[]` |
| `admissions_tax`, `attendance_tax`, `entertainment_tax`, `gross_receipts_tax`, `hospitality_tax`, `luxury_tax`, `resort_tax`, `tourism_tax` | Added | `Tax.CalculationLineItem.tax_breakdown[].tax_rate_details`, `Tax.Calculation.shipping_cost.tax_breakdown[].tax_rate_details`, `Tax.Calculation.tax_breakdown[].tax_rate_details`, `Tax.Transaction.shipping_cost.tax_breakdown[].tax_rate_details`, [Tax.Registration#create.country_options.us](/api/tax/registrations/create?api-version=2026-03-25.preview#tax_registration_create-country_options-us-type), [Tax.Registration.country_options.us](/api/tax/registrations/create?api-version=2026-03-25.preview#tax_registration_create-country_options-us-type) |

#### Ruby

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [Tax::Location](/api/tax/location/object?api-version=2026-03-25.preview) |

| Methods | Change | Resource |
| --- | --- | --- |
| `create`, `list`, `retrieve` | Added | [Tax::Location](/api/tax/location/object?api-version=2026-03-25.preview) |

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `performance_location` | Added | [Tax::CalculationCreateParams::LineItem](/api/tax/calculations/create?api-version=2026-03-25.preview#calculate_tax-line_items), `Tax::CalculationLineItem` |
| `tax_details` | Added | [Checkout::SessionCreateParams::LineItem::PriceDatum::ProductDatum](/api/checkout/sessions/create?api-version=2026-03-25.preview#create_checkout_session-line_items-price_data-product_data), [Checkout::SessionUpdateParams::LineItem::PriceDatum::ProductDatum](/api/checkout/sessions/update?api-version=2026-03-25.preview#update_checkout_session-line_items-price_data-product_data), [InvoiceAddLinesParams::Line::PriceDatum::ProductDatum](/api/invoice-line-item/bulk?api-version=2026-03-25.preview#bulk_add_lines-lines-price_data-product_data), [InvoiceLineItemUpdateParams::PriceDatum::ProductDatum](/api/invoice-line-item/update?api-version=2026-03-25.preview#update_line-price_data-product_data), [InvoiceUpdateLinesParams::Line::PriceDatum::ProductDatum](/api/invoice-line-item/invoices/update-lines/bulk?api-version=2026-03-25.preview#bulk_update_lines-lines-price_data-product_data), [PaymentLinkCreateParams::LineItem::PriceDatum::ProductDatum](/api/payment-link/create?api-version=2026-03-25.preview#create_payment_link-line_items-price_data-product_data), [PlanCreateParams::Product](/api/plans/create?api-version=2026-03-25.preview#create_plan-product-[0]), [PriceCreateParams::ProductDatum](/api/prices/create?api-version=2026-03-25.preview#create_price-product_data), [ProductCreateParams](/api/products/create?api-version=2026-03-25.preview), [ProductUpdateParams](/api/products/update?api-version=2026-03-25.preview) |
| `admissions_tax`, `attendance_tax`, `entertainment_tax`, `gross_receipts_tax`, `hospitality_tax`, `luxury_tax`, `resort_tax`, `tourism_tax` | Added | [Tax::Registration::CountryOption::Me](/api/tax/registrations/object?api-version=2026-03-25.preview#tax_registration_object-country_options-us) |
| `requirements` | Added | [TaxCode](/api/tax_codes/object?api-version=2026-03-25.preview) |

#### Python

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [tax.Location](/api/tax/location/object?api-version=2026-03-25.preview) |

| Methods | Change | Resource |
| --- | --- | --- |
| `create`, `list`, `retrieve` | Added | [tax.Location](/api/tax/location/object?api-version=2026-03-25.preview) |

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `performance_location` | Added | `Tax.CalculationLineItem`, [tax.CalculationCreateParamsLineItem](/api/tax/calculations/create?api-version=2026-03-25.preview#calculate_tax-line_items) |
| `tax_details` | Added | [InvoiceAddLinesParamsLinePriceDatumProductDatum](/api/invoice-line-item/bulk?api-version=2026-03-25.preview#bulk_add_lines-lines-price_data-product_data), [InvoiceLineItemModifyParamsPriceDatumProductDatum](/api/invoice-line-item/update?api-version=2026-03-25.preview#update_line-price_data-product_data), [InvoiceUpdateLinesParamsLinePriceDatumProductDatum](/api/invoice-line-item/invoices/update-lines/bulk?api-version=2026-03-25.preview#bulk_update_lines-lines-price_data-product_data), [PaymentLinkCreateParamsLineItemPriceDatumProductDatum](/api/payment-link/create?api-version=2026-03-25.preview#create_payment_link-line_items-price_data-product_data), [PlanCreateParamsProduct](/api/plans/create?api-version=2026-03-25.preview#create_plan-product-[0]), [PriceCreateParamsProductDatum](/api/prices/create?api-version=2026-03-25.preview#create_price-product_data), [ProductCreateParams](/api/products/create?api-version=2026-03-25.preview), [ProductModifyParams](/api/products/update?api-version=2026-03-25.preview), [checkout.SessionCreateParamsLineItemPriceDatumProductDatum](/api/checkout/sessions/create?api-version=2026-03-25.preview#create_checkout_session-line_items-price_data-product_data), [checkout.SessionModifyParamsLineItemPriceDatumProductDatum](/api/checkout/sessions/update?api-version=2026-03-25.preview#update_checkout_session-line_items-price_data-product_data) |
| `admissions_tax`, `attendance_tax`, `entertainment_tax`, `gross_receipts_tax`, `hospitality_tax`, `luxury_tax`, `resort_tax`, `tourism_tax` | Added | [Tax.Registration.CountryOption.Me](/api/tax/registrations/object?api-version=2026-03-25.preview#tax_registration_object-country_options-us) |
| `requirements` | Added | [TaxCode](/api/tax_codes/object?api-version=2026-03-25.preview) |

| Values | Change | Enums |
| --- | --- | --- |
| `performance` | Added | `Tax.CalculationLineItem.TaxBreakdown`, `Tax.Calculation.ShippingCost.TaxBreakdown`, `Tax.Transaction.ShippingCost.TaxBreakdown` |
| `admissions_tax`, `attendance_tax`, `entertainment_tax`, `gross_receipts_tax`, `hospitality_tax`, `luxury_tax`, `resort_tax`, `tourism_tax` | Added | `Tax.CalculationLineItem.TaxBreakdown.TaxRateDetail`, `Tax.Calculation.ShippingCost.TaxBreakdown.TaxRateDetail`, `Tax.Calculation.TaxBreakdown.TaxRateDetail`, `Tax.Transaction.ShippingCost.TaxBreakdown.TaxRateDetail`, [tax.RegistrationCreateParamsCountryOptionMe](/api/tax/registrations/create?api-version=2026-03-25.preview#tax_registration_create-country_options-us-type), [Tax.Registration.CountryOption.Me](/api/tax/registrations/create?api-version=2026-03-25.preview#tax_registration_create-country_options-us-type) |

#### PHP

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [Tax.Location](/api/tax/location/object?api-version=2026-03-25.preview) |

| Methods | Change | Resource |
| --- | --- | --- |
| `all`, `create`, `retrieve` | Added | [Tax.Location](/api/tax/location/object?api-version=2026-03-25.preview) |

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `performance_location` | Added | `Tax.CalculationLineItem`, [Tax\Calculation.create().$params.line_item](/api/tax/calculations/create?api-version=2026-03-25.preview#calculate_tax-line_items) |
| `tax_details` | Added | [Checkout\Session.create().$params.line_item.price_datum.product_datum](/api/checkout/sessions/create?api-version=2026-03-25.preview#create_checkout_session-line_items-price_data-product_data), [Checkout\Session.update().$params.line_item.price_datum.product_datum](/api/checkout/sessions/update?api-version=2026-03-25.preview#update_checkout_session-line_items-price_data-product_data), [Invoice.add_lines().$params.line.price_datum.product_datum](/api/invoice-line-item/bulk?api-version=2026-03-25.preview#bulk_add_lines-lines-price_data-product_data), [Invoice.update_lines().$params.line.price_datum.product_datum](/api/invoice-line-item/invoices/update-lines/bulk?api-version=2026-03-25.preview#bulk_update_lines-lines-price_data-product_data), [InvoiceLineItem.update().$params.price_datum.product_datum](/api/invoice-line-item/update?api-version=2026-03-25.preview#update_line-price_data-product_data), [PaymentLink.create().$params.line_item.price_datum.product_datum](/api/payment-link/create?api-version=2026-03-25.preview#create_payment_link-line_items-price_data-product_data), [Plan.create().$params.product](/api/plans/create?api-version=2026-03-25.preview#create_plan-product-[0]), [Price.create().$params.product_datum](/api/prices/create?api-version=2026-03-25.preview#create_price-product_data), [Product.create().$params](/api/products/create?api-version=2026-03-25.preview), [Product.update().$params](/api/products/update?api-version=2026-03-25.preview) |
| `admissions_tax`, `attendance_tax`, `entertainment_tax`, `gross_receipts_tax`, `hospitality_tax`, `luxury_tax`, `resort_tax`, `tourism_tax` | Added | [Tax.Registration.country_options.us](/api/tax/registrations/object?api-version=2026-03-25.preview#tax_registration_object-country_options-us) |
| `requirements` | Added | [TaxCode](/api/tax_codes/object?api-version=2026-03-25.preview) |

| Values | Change | Enums |
| --- | --- | --- |
| `performance` | Added | `Tax.CalculationLineItem.tax_breakdown[]`, `Tax.Calculation.shipping_cost.tax_breakdown[]`, `Tax.Transaction.shipping_cost.tax_breakdown[]` |
| `admissions_tax`, `attendance_tax`, `entertainment_tax`, `gross_receipts_tax`, `hospitality_tax`, `luxury_tax`, `resort_tax`, `tourism_tax` | Added | `Tax.CalculationLineItem.tax_breakdown[].tax_rate_details`, `Tax.Calculation.shipping_cost.tax_breakdown[].tax_rate_details`, `Tax.Calculation.tax_breakdown[].tax_rate_details`, `Tax.Transaction.shipping_cost.tax_breakdown[].tax_rate_details`, [Tax.Registration.country_options.us](/api/tax/registrations/object?api-version=2026-03-25.preview#tax_registration_object-country_options-us-type) |

#### Java

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [tax.Location](/api/tax/location/object?api-version=2026-03-25.preview) |

| Methods | Change | Resource |
| --- | --- | --- |
| `create`, `list`, `retrieve` | Added | [tax.Location](/api/tax/location/object?api-version=2026-03-25.preview) |

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `performanceLocation` | Added | [tax.CalculationCreateParams.line_items[]](/api/tax/calculations/create?api-version=2026-03-25.preview#calculate_tax-line_items), `tax.CalculationLineItem` |
| `taxDetails` | Added | [InvoiceAddLinesParams.lines[].price_data.product_data](/api/invoice-line-item/bulk?api-version=2026-03-25.preview#bulk_add_lines-lines-price_data-product_data), [InvoiceLineItemUpdateParams.price_data.product_data](/api/invoice-line-item/update?api-version=2026-03-25.preview#update_line-price_data-product_data), [InvoiceUpdateLinesParams.lines[].price_data.product_data](/api/invoice-line-item/invoices/update-lines/bulk?api-version=2026-03-25.preview#bulk_update_lines-lines-price_data-product_data), [PaymentLinkCreateParams.line_items[].price_data.product_data](/api/payment-link/create?api-version=2026-03-25.preview#create_payment_link-line_items-price_data-product_data), [PlanCreateParams.product[0]](/api/plans/create?api-version=2026-03-25.preview#create_plan-product-[0]), [PriceCreateParams.product_data](/api/prices/create?api-version=2026-03-25.preview#create_price-product_data), [ProductCreateParams](/api/products/create?api-version=2026-03-25.preview), [ProductUpdateParams](/api/products/update?api-version=2026-03-25.preview), [checkout.SessionCreateParams.line_items[].price_data.product_data](/api/checkout/sessions/create?api-version=2026-03-25.preview#create_checkout_session-line_items-price_data-product_data), [checkout.SessionUpdateParams.line_items[].price_data.product_data](/api/checkout/sessions/update?api-version=2026-03-25.preview#update_checkout_session-line_items-price_data-product_data) |
| `admissionsTax`, `attendanceTax`, `entertainmentTax`, `grossReceiptsTax`, `hospitalityTax`, `luxuryTax`, `resortTax`, `tourismTax` | Added | [tax.Registration.country_options.us](/api/tax/registrations/object?api-version=2026-03-25.preview#tax_registration_object-country_options-us) |
| `requirements` | Added | [TaxCode](/api/tax_codes/object?api-version=2026-03-25.preview) |

| Values | Change | Enum |
| --- | --- | --- |
| `admissions_tax`, `attendance_tax`, `entertainment_tax`, `gross_receipts_tax`, `hospitality_tax`, `luxury_tax`, `resort_tax`, `tourism_tax` | Added | [tax.RegistrationCreateParams.country_options.us](/api/tax/registrations/create?api-version=2026-03-25.preview#tax_registration_create-country_options-us-type) |

#### Node.js

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [Tax.Location](/api/tax/location/object?api-version=2026-03-25.preview) |

| Methods | Change | Resource |
| --- | --- | --- |
| `create`, `list`, `retrieve` | Added | [Tax.Location](/api/tax/location/object?api-version=2026-03-25.preview) |

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `performance_location` | Added | [Tax.CalculationCreateParams.line_items[]](/api/tax/calculations/create?api-version=2026-03-25.preview#calculate_tax-line_items), `Tax.CalculationLineItem` |
| `tax_details` | Added | [Checkout.SessionCreateParams.line_items[].price_data.product_data](/api/checkout/sessions/create?api-version=2026-03-25.preview#create_checkout_session-line_items-price_data-product_data), [Checkout.SessionUpdateParams.line_items[].price_data.product_data](/api/checkout/sessions/update?api-version=2026-03-25.preview#update_checkout_session-line_items-price_data-product_data), [InvoiceAddLinesParams.lines[].price_data.product_data](/api/invoice-line-item/bulk?api-version=2026-03-25.preview#bulk_add_lines-lines-price_data-product_data), [InvoiceLineItemUpdateParams.price_data.product_data](/api/invoice-line-item/update?api-version=2026-03-25.preview#update_line-price_data-product_data), [InvoiceUpdateLinesParams.lines[].price_data.product_data](/api/invoice-line-item/invoices/update-lines/bulk?api-version=2026-03-25.preview#bulk_update_lines-lines-price_data-product_data), [PaymentLinkCreateParams.line_items[].price_data.product_data](/api/payment-link/create?api-version=2026-03-25.preview#create_payment_link-line_items-price_data-product_data), [PlanCreateParams.product[0]](/api/plans/create?api-version=2026-03-25.preview#create_plan-product-[0]), [PriceCreateParams.product_data](/api/prices/create?api-version=2026-03-25.preview#create_price-product_data), [ProductCreateParams](/api/products/create?api-version=2026-03-25.preview), [ProductUpdateParams](/api/products/update?api-version=2026-03-25.preview) |
| `admissions_tax`, `attendance_tax`, `entertainment_tax`, `gross_receipts_tax`, `hospitality_tax`, `luxury_tax`, `resort_tax`, `tourism_tax` | Added | [Tax.Registration.country_options.us](/api/tax/registrations/object?api-version=2026-03-25.preview#tax_registration_object-country_options-us) |
| `requirements` | Added | [TaxCode](/api/tax_codes/object?api-version=2026-03-25.preview) |

| Values | Change | Enums |
| --- | --- | --- |
| `performance` | Added | `Tax.CalculationLineItem.tax_breakdown[]`, `Tax.Calculation.shipping_cost.tax_breakdown[]`, `Tax.Transaction.shipping_cost.tax_breakdown[]` |
| `admissions_tax`, `attendance_tax`, `entertainment_tax`, `gross_receipts_tax`, `hospitality_tax`, `luxury_tax`, `resort_tax`, `tourism_tax` | Added | `Tax.CalculationLineItem.tax_breakdown[].tax_rate_details`, `Tax.Calculation.shipping_cost.tax_breakdown[].tax_rate_details`, `Tax.Calculation.tax_breakdown[].tax_rate_details`, `Tax.Transaction.shipping_cost.tax_breakdown[].tax_rate_details`, [Tax.RegistrationCreateParams.country_options.us](/api/tax/registrations/create?api-version=2026-03-25.preview#tax_registration_create-country_options-us-type), [Tax.Registration.country_options.us](/api/tax/registrations/create?api-version=2026-03-25.preview#tax_registration_create-country_options-us-type) |

#### Go

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [TaxLocation](/api/tax/location/object?api-version=2026-03-25.preview) |

| Methods | Change | Resource |
| --- | --- | --- |
| `Get`, `List`, `New` | Added | [TaxLocation](/api/tax/location/object?api-version=2026-03-25.preview) |

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `PerformanceLocation` | Added | `TaxCalculationLineItem`, [TaxCalculationLineItemParams](/api/tax/calculations/create?api-version=2026-03-25.preview#calculate_tax-line_items) |
| `TaxDetails` | Added | [CheckoutSessionLineItemPriceDataProductDataParams](/api/checkout/sessions/create?api-version=2026-03-25.preview#create_checkout_session-line_items-price_data-product_data), [InvoiceAddLinesLinePriceDataProductDataParams](/api/invoice-line-item/bulk?api-version=2026-03-25.preview#bulk_add_lines-lines-price_data-product_data), [InvoiceLineItemPriceDataProductDataParams](/api/invoice-line-item/update?api-version=2026-03-25.preview#update_line-price_data-product_data), [InvoiceUpdateLinesLinePriceDataProductDataParams](/api/invoice-line-item/invoices/update-lines/bulk?api-version=2026-03-25.preview#bulk_update_lines-lines-price_data-product_data), [PaymentLinkLineItemPriceDataProductDataParams](/api/payment-link/create?api-version=2026-03-25.preview#create_payment_link-line_items-price_data-product_data), [PlanProductParams](/api/plans/create?api-version=2026-03-25.preview#create_plan-product-[0]), [PriceProductDataParams](/api/prices/create?api-version=2026-03-25.preview#create_price-product_data), [ProductParams](/api/products/update?api-version=2026-03-25.preview) |
| `AdmissionsTax`, `AttendanceTax`, `EntertainmentTax`, `GrossReceiptsTax`, `HospitalityTax`, `LuxuryTax`, `ResortTax`, `TourismTax` | Added | [TaxRegistrationCountryOptionsUs](/api/tax/registrations/object?api-version=2026-03-25.preview#tax_registration_object-country_options-us) |
| `Requirements` | Added | [TaxCode](/api/tax_codes/object?api-version=2026-03-25.preview) |

| Values | Change | Enums |
| --- | --- | --- |
| `performance` | Added | `TaxCalculationLineItemTaxBreakdown`, `TaxCalculationShippingCostTaxBreakdown`, `TaxTransactionShippingCostTaxBreakdown` |
| `admissions_tax`, `attendance_tax`, `entertainment_tax`, `gross_receipts_tax`, `hospitality_tax`, `luxury_tax`, `resort_tax`, `tourism_tax` | Added | `TaxCalculationLineItemTaxBreakdownTaxRateDetails`, `TaxCalculationShippingCostTaxBreakdownTaxRateDetails`, `TaxCalculationTaxBreakdownTaxRateDetails`, `TaxTransactionShippingCostTaxBreakdownTaxRateDetails`, [TaxRegistrationCountryOptionsUs](/api/tax/registrations/object?api-version=2026-03-25.preview#tax_registration_object-country_options-us-Type) |

#### .NET

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [Tax.Location](/api/tax/location/object?api-version=2026-03-25.preview) |

| Methods | Change | Resource |
| --- | --- | --- |
| `Create`, `Get`, `List` | Added | [Tax.Location](/api/tax/location/object?api-version=2026-03-25.preview) |

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `PerformanceLocation` | Added | `Tax.CalculationLineItem`, [TaxCalculationLineItemOptions](/api/tax/calculations/create?api-version=2026-03-25.preview#calculate_tax-line_items) |
| `TaxDetails` | Added | [CheckoutSessionLineItemPriceDataProductDataOptions](/api/checkout/sessions/create?api-version=2026-03-25.preview#create_checkout_session-line_items-price_data-product_data), [InvoiceLineItemPriceDataProductDataOptions](/api/invoice-line-item/update?api-version=2026-03-25.preview#update_line-price_data-product_data), [InvoiceLinePriceDataProductDataOptions](/api/invoice-line-item/bulk?api-version=2026-03-25.preview#bulk_add_lines-lines-price_data-product_data), [PaymentLinkLineItemPriceDataProductDataOptions](/api/payment-link/create?api-version=2026-03-25.preview#create_payment_link-line_items-price_data-product_data), [PlanProductOptions](/api/plans/create?api-version=2026-03-25.preview#create_plan-product-[0]), [PriceProductDataOptions](/api/prices/create?api-version=2026-03-25.preview#create_price-product_data), [ProductCreateOptions](/api/products/create?api-version=2026-03-25.preview), [ProductUpdateOptions](/api/products/update?api-version=2026-03-25.preview) |
| `AdmissionsTax`, `AttendanceTax`, `EntertainmentTax`, `GrossReceiptsTax`, `HospitalityTax`, `LuxuryTax`, `ResortTax`, `TourismTax` | Added | [Tax.Registration.CountryOptions.Us](/api/tax/registrations/object?api-version=2026-03-25.preview#tax_registration_object-country_options-us) |
| `Requirements` | Added | [TaxCode](/api/tax_codes/object?api-version=2026-03-25.preview) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2026-03-25.preview`
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
