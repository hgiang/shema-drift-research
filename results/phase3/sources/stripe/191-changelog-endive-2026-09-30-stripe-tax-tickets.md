# Adds support for ticket sales to Stripe Tax

## What’s new

[Stripe Tax](https://docs.stripe.com/tax.md) now supports ticket sales. Create a [performance_location](https://docs.stripe.com/api/tax/calculations/create.md?api-version=2026-09-30.endive#calculate_tax-line_items-performance_location) for an event venue and associate it with ticket line items or products. Stripe Tax uses the venue address to calculate tax and applies any supported event-specific taxes.

## Impact

If you sell tickets, you can now calculate tax based on where an event takes place.

For an overview, see [Tax location-based sales](https://docs.stripe.com/tax/location-sales.md). To set up your integration, read the guide to [taxing ticket sales based on event location](https://docs.stripe.com/tax/tax-for-tickets/integration-guide.md). You can also use performance locations to [tax in-person sales at a specific location](https://docs.stripe.com/tax/optional-tax-location/integration-guide.md).

## Changes

#### REST API

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [Tax.Location](/api/tax/location/object?api-version=2026-09-30.endive#tax_location_object) |

| Endpoints | Change | Resource |
| --- | --- | --- |
| `create`, `list`, `retrieve` | Added | [Tax.Location](/api/tax/location/object?api-version=2026-09-30.endive#tax_location_object) |

| Parameters | Change | Resources or endpoints |
| --- | --- | --- |
| `performance_location` | Added | [Tax.Calculation#create.line_items[]](/api/tax/calculations/create?api-version=2026-09-30.endive#calculate_tax-line_items), [Tax.CalculationLineItem](/api/tax/calculations/line_items/object?api-version=2026-09-30.endive) |
| `admissions_tax`, `attendance_tax`, `entertainment_tax`, `gross_receipts_tax`, `hospitality_tax`, `luxury_tax`, `resort_tax`, `tourism_tax` | Added | [Tax.Registration#create.country_options.us](/api/tax/registrations/create?api-version=2026-09-30.endive#tax_registration_create-country_options-us), [Tax.Registration.country_options.us](/api/tax/registrations/object?api-version=2026-09-30.endive#tax_registration_object-country_options-us) |
| `requirements` | Added | [TaxCode](/api/tax_codes/object?api-version=2026-09-30.endive#tax_code_object) |
| `tax_details` | Added | [Checkout.Session#create.line_items[].price_data.product_data](/api/checkout/sessions/create?api-version=2026-09-30.endive#create_checkout_session-line_items-price_data-product_data), [Checkout.Session#update.line_items[].price_data.product_data](/api/checkout/sessions/update?api-version=2026-09-30.endive#update_checkout_session-line_items-price_data-product_data), [Invoice#add_lines.lines[].price_data.product_data](/api/invoice-line-item/bulk?api-version=2026-09-30.endive#bulk_add_lines-lines-price_data-product_data), [Invoice#update_lines.lines[].price_data.product_data](/api/invoice-line-item/invoices/update-lines/bulk?api-version=2026-09-30.endive#bulk_update_lines-lines-price_data-product_data), [InvoiceLineItem#update.price_data.product_data](/api/invoice-line-item/update?api-version=2026-09-30.endive#update_line-price_data-product_data), [PaymentLink#create.line_items[].price_data.product_data](/api/payment-link/create?api-version=2026-09-30.endive#create_payment_link-line_items-price_data-product_data), [Plan#create.product[0]](/api/plans/create?api-version=2026-09-30.endive#create_plan-product-[0]), [Price#create.product_data](/api/prices/create?api-version=2026-09-30.endive#create_price-product_data), [Product](/api/products/object?api-version=2026-09-30.endive#product_object), [Product#create](/api/products/create?api-version=2026-09-30.endive#create_product), [Product#update](/api/products/update?api-version=2026-09-30.endive#update_product) |

| Values | Change | Enums |
| --- | --- | --- |
| `performance` | Added | [Tax.CalculationLineItem.tax_breakdown[].sourcing](/api/tax/calculations/line_items/object?api-version=2026-09-30.endive#tax_calculation_line_item_object-tax_breakdown-sourcing), [Tax.Calculation.shipping_cost.tax_breakdown[].sourcing](/api/tax/calculations/object?api-version=2026-09-30.endive#tax_calculation_object-shipping_cost-tax_breakdown-sourcing), [Tax.Transaction.shipping_cost.tax_breakdown[].sourcing](/api/tax/transactions/object?api-version=2026-09-30.endive#tax_transaction_object-shipping_cost-tax_breakdown-sourcing) |
| `admissions_tax`, `attendance_tax`, `entertainment_tax`, `gross_receipts_tax`, `hospitality_tax`, `luxury_tax`, `resort_tax`, `tourism_tax` | Added | [Tax.CalculationLineItem.tax_breakdown[].tax_rate_details.tax_type](/api/tax/calculations/line_items/object?api-version=2026-09-30.endive#tax_calculation_line_item_object-tax_breakdown-tax_rate_details-tax_type), [Tax.Calculation.shipping_cost.tax_breakdown[].tax_rate_details.tax_type](/api/tax/calculations/object?api-version=2026-09-30.endive#tax_calculation_object-shipping_cost-tax_breakdown-tax_rate_details-tax_type), [Tax.Calculation.tax_breakdown[].tax_rate_details.tax_type](/api/tax/calculations/object?api-version=2026-09-30.endive#tax_calculation_object-tax_breakdown-tax_rate_details-tax_type), [Tax.Transaction.shipping_cost.tax_breakdown[].tax_rate_details.tax_type](/api/tax/transactions/object?api-version=2026-09-30.endive#tax_transaction_object-shipping_cost-tax_breakdown-tax_rate_details-tax_type), [Tax.Registration#create.country_options.us.type](/api/tax/registrations/create?api-version=2026-09-30.endive#tax_registration_create-country_options-us-type), [Tax.Registration.country_options.us.type](/api/tax/registrations/object?api-version=2026-09-30.endive#tax_registration_object-country_options-us-type) |

#### Ruby

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [Tax::Location](/api/tax/location/object?api-version=2026-09-30.endive#tax_location_object) |

| Methods | Change | Resource |
| --- | --- | --- |
| `create`, `list`, `retrieve` | Added | [Tax::Location](/api/tax/location/object?api-version=2026-09-30.endive#tax_location_object) |

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `performance_location` | Added | [Tax::CalculationCreateParams::LineItem](/api/tax/calculations/create?api-version=2026-09-30.endive#calculate_tax-line_items), [Tax::CalculationLineItem](/api/tax/calculations/line_items/object?api-version=2026-09-30.endive) |
| `admissions_tax`, `attendance_tax`, `entertainment_tax`, `gross_receipts_tax`, `hospitality_tax`, `luxury_tax`, `resort_tax`, `tourism_tax` | Added | [Tax::Registration::CountryOption::Us](/api/tax/registrations/object?api-version=2026-09-30.endive#tax_registration_object-country_options-us), [Tax::RegistrationCreateParams::CountryOption::Us](/api/tax/registrations/create?api-version=2026-09-30.endive#tax_registration_create-country_options-us) |
| `requirements` | Added | [TaxCode](/api/tax_codes/object?api-version=2026-09-30.endive#tax_code_object) |
| `tax_details` | Added | [Checkout::SessionCreateParams::LineItem::PriceDatum::ProductDatum](/api/checkout/sessions/create?api-version=2026-09-30.endive#create_checkout_session-line_items-price_data-product_data), [Checkout::SessionUpdateParams::LineItem::PriceDatum::ProductDatum](/api/checkout/sessions/update?api-version=2026-09-30.endive#update_checkout_session-line_items-price_data-product_data), [InvoiceAddLinesParams::Line::PriceDatum::ProductDatum](/api/invoice-line-item/bulk?api-version=2026-09-30.endive#bulk_add_lines-lines-price_data-product_data), [InvoiceLineItemUpdateParams::PriceDatum::ProductDatum](/api/invoice-line-item/update?api-version=2026-09-30.endive#update_line-price_data-product_data), [InvoiceUpdateLinesParams::Line::PriceDatum::ProductDatum](/api/invoice-line-item/invoices/update-lines/bulk?api-version=2026-09-30.endive#bulk_update_lines-lines-price_data-product_data), [PaymentLinkCreateParams::LineItem::PriceDatum::ProductDatum](/api/payment-link/create?api-version=2026-09-30.endive#create_payment_link-line_items-price_data-product_data), [PlanCreateParams::Product](/api/plans/create?api-version=2026-09-30.endive#create_plan-product-[0]), [PriceCreateParams::ProductDatum](/api/prices/create?api-version=2026-09-30.endive#create_price-product_data), [Product](/api/products/object?api-version=2026-09-30.endive#product_object), [ProductCreateParams](/api/products/create?api-version=2026-09-30.endive#create_product), [ProductUpdateParams](/api/products/update?api-version=2026-09-30.endive#update_product) |

#### Python

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [tax.Location](/api/tax/location/object?api-version=2026-09-30.endive#tax_location_object) |

| Methods | Change | Resource |
| --- | --- | --- |
| `create`, `list`, `retrieve` | Added | [tax.Location](/api/tax/location/object?api-version=2026-09-30.endive#tax_location_object) |

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `performance_location` | Added | [Tax.CalculationLineItem](/api/tax/calculations/line_items/object?api-version=2026-09-30.endive), [tax.CalculationCreateParamsLineItem](/api/tax/calculations/create?api-version=2026-09-30.endive#calculate_tax-line_items) |
| `admissions_tax`, `attendance_tax`, `entertainment_tax`, `gross_receipts_tax`, `hospitality_tax`, `luxury_tax`, `resort_tax`, `tourism_tax` | Added | [Tax.Registration.CountryOption.Us](/api/tax/registrations/object?api-version=2026-09-30.endive#tax_registration_object-country_options-us), [tax.RegistrationCreateParamsCountryOptionUs](/api/tax/registrations/create?api-version=2026-09-30.endive#tax_registration_create-country_options-us) |
| `requirements` | Added | [TaxCode](/api/tax_codes/object?api-version=2026-09-30.endive#tax_code_object) |
| `tax_details` | Added | [InvoiceAddLinesParamsLinePriceDatumProductDatum](/api/invoice-line-item/bulk?api-version=2026-09-30.endive#bulk_add_lines-lines-price_data-product_data), [InvoiceLineItemModifyParamsPriceDatumProductDatum](/api/invoice-line-item/update?api-version=2026-09-30.endive#update_line-price_data-product_data), [InvoiceUpdateLinesParamsLinePriceDatumProductDatum](/api/invoice-line-item/invoices/update-lines/bulk?api-version=2026-09-30.endive#bulk_update_lines-lines-price_data-product_data), [PaymentLinkCreateParamsLineItemPriceDatumProductDatum](/api/payment-link/create?api-version=2026-09-30.endive#create_payment_link-line_items-price_data-product_data), [PlanCreateParamsProduct](/api/plans/create?api-version=2026-09-30.endive#create_plan-product-[0]), [PriceCreateParamsProductDatum](/api/prices/create?api-version=2026-09-30.endive#create_price-product_data), [Product](/api/products/object?api-version=2026-09-30.endive#product_object), [ProductCreateParams](/api/products/create?api-version=2026-09-30.endive#create_product), [ProductModifyParams](/api/products/update?api-version=2026-09-30.endive#update_product), [checkout.SessionCreateParamsLineItemPriceDatumProductDatum](/api/checkout/sessions/create?api-version=2026-09-30.endive#create_checkout_session-line_items-price_data-product_data), [checkout.SessionModifyParamsLineItemPriceDatumProductDatum](/api/checkout/sessions/update?api-version=2026-09-30.endive#update_checkout_session-line_items-price_data-product_data) |

| Values | Change | Enums |
| --- | --- | --- |
| `performance` | Added | [Tax.CalculationLineItem.TaxBreakdown.sourcing](/api/tax/calculations/line_items/object?api-version=2026-09-30.endive#tax_calculation_line_item_object-tax_breakdown-sourcing), [Tax.Calculation.ShippingCost.TaxBreakdown.sourcing](/api/tax/calculations/object?api-version=2026-09-30.endive#tax_calculation_object-shipping_cost-tax_breakdown-sourcing), [Tax.Transaction.ShippingCost.TaxBreakdown.sourcing](/api/tax/transactions/object?api-version=2026-09-30.endive#tax_transaction_object-shipping_cost-tax_breakdown-sourcing) |
| `admissions_tax`, `attendance_tax`, `entertainment_tax`, `gross_receipts_tax`, `hospitality_tax`, `luxury_tax`, `resort_tax`, `tourism_tax` | Added | [Tax.CalculationLineItem.TaxBreakdown.TaxRateDetail.tax_type](/api/tax/calculations/line_items/object?api-version=2026-09-30.endive#tax_calculation_line_item_object-tax_breakdown-tax_rate_details-tax_type), [Tax.Calculation.ShippingCost.TaxBreakdown.TaxRateDetail.tax_type](/api/tax/calculations/object?api-version=2026-09-30.endive#tax_calculation_object-shipping_cost-tax_breakdown-tax_rate_details-tax_type), [Tax.Calculation.TaxBreakdown.TaxRateDetail.tax_type](/api/tax/calculations/object?api-version=2026-09-30.endive#tax_calculation_object-tax_breakdown-tax_rate_details-tax_type), [Tax.Transaction.ShippingCost.TaxBreakdown.TaxRateDetail.tax_type](/api/tax/transactions/object?api-version=2026-09-30.endive#tax_transaction_object-shipping_cost-tax_breakdown-tax_rate_details-tax_type), [tax.RegistrationCreateParamsCountryOptionUs.type](/api/tax/registrations/create?api-version=2026-09-30.endive#tax_registration_create-country_options-us-type), [Tax.Registration.CountryOption.Us.type](/api/tax/registrations/object?api-version=2026-09-30.endive#tax_registration_object-country_options-us-type) |

#### PHP

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [Tax.Location](/api/tax/location/object?api-version=2026-09-30.endive#tax_location_object) |

| Methods | Change | Resource |
| --- | --- | --- |
| `all`, `create`, `retrieve` | Added | [Tax.Location](/api/tax/location/object?api-version=2026-09-30.endive#tax_location_object) |

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `performance_location` | Added | [Tax.CalculationLineItem](/api/tax/calculations/line_items/object?api-version=2026-09-30.endive), [Tax\Calculation.create().$params.line_item](/api/tax/calculations/create?api-version=2026-09-30.endive#calculate_tax-line_items) |
| `admissions_tax`, `attendance_tax`, `entertainment_tax`, `gross_receipts_tax`, `hospitality_tax`, `luxury_tax`, `resort_tax`, `tourism_tax` | Added | [Tax.Registration.country_options.us](/api/tax/registrations/object?api-version=2026-09-30.endive#tax_registration_object-country_options-us), [Tax\Registration.create().$params.country_option.us](/api/tax/registrations/create?api-version=2026-09-30.endive#tax_registration_create-country_options-us) |
| `requirements` | Added | [TaxCode](/api/tax_codes/object?api-version=2026-09-30.endive#tax_code_object) |
| `tax_details` | Added | [Checkout\Session.create().$params.line_item.price_datum.product_datum](/api/checkout/sessions/create?api-version=2026-09-30.endive#create_checkout_session-line_items-price_data-product_data), [Checkout\Session.update().$params.line_item.price_datum.product_datum](/api/checkout/sessions/update?api-version=2026-09-30.endive#update_checkout_session-line_items-price_data-product_data), [Invoice.add_lines().$params.line.price_datum.product_datum](/api/invoice-line-item/bulk?api-version=2026-09-30.endive#bulk_add_lines-lines-price_data-product_data), [Invoice.update_lines().$params.line.price_datum.product_datum](/api/invoice-line-item/invoices/update-lines/bulk?api-version=2026-09-30.endive#bulk_update_lines-lines-price_data-product_data), [InvoiceLineItem.update().$params.price_datum.product_datum](/api/invoice-line-item/update?api-version=2026-09-30.endive#update_line-price_data-product_data), [PaymentLink.create().$params.line_item.price_datum.product_datum](/api/payment-link/create?api-version=2026-09-30.endive#create_payment_link-line_items-price_data-product_data), [Plan.create().$params.product](/api/plans/create?api-version=2026-09-30.endive#create_plan-product-[0]), [Price.create().$params.product_datum](/api/prices/create?api-version=2026-09-30.endive#create_price-product_data), [Product](/api/products/object?api-version=2026-09-30.endive#product_object), [Product.create().$params](/api/products/create?api-version=2026-09-30.endive#create_product), [Product.update().$params](/api/products/update?api-version=2026-09-30.endive#update_product) |

| Values | Change | Enums |
| --- | --- | --- |
| `performance` | Added | [Tax.CalculationLineItem.tax_breakdown[].sourcing](/api/tax/calculations/line_items/object?api-version=2026-09-30.endive#tax_calculation_line_item_object-tax_breakdown-sourcing), [Tax.Calculation.shipping_cost.tax_breakdown[].sourcing](/api/tax/calculations/object?api-version=2026-09-30.endive#tax_calculation_object-shipping_cost-tax_breakdown-sourcing), [Tax.Transaction.shipping_cost.tax_breakdown[].sourcing](/api/tax/transactions/object?api-version=2026-09-30.endive#tax_transaction_object-shipping_cost-tax_breakdown-sourcing) |
| `admissions_tax`, `attendance_tax`, `entertainment_tax`, `gross_receipts_tax`, `hospitality_tax`, `luxury_tax`, `resort_tax`, `tourism_tax` | Added | [Tax.CalculationLineItem.tax_breakdown[].tax_rate_details.tax_type](/api/tax/calculations/line_items/object?api-version=2026-09-30.endive#tax_calculation_line_item_object-tax_breakdown-tax_rate_details-tax_type), [Tax.Calculation.shipping_cost.tax_breakdown[].tax_rate_details.tax_type](/api/tax/calculations/object?api-version=2026-09-30.endive#tax_calculation_object-shipping_cost-tax_breakdown-tax_rate_details-tax_type), [Tax.Calculation.tax_breakdown[].tax_rate_details.tax_type](/api/tax/calculations/object?api-version=2026-09-30.endive#tax_calculation_object-tax_breakdown-tax_rate_details-tax_type), [Tax.Transaction.shipping_cost.tax_breakdown[].tax_rate_details.tax_type](/api/tax/transactions/object?api-version=2026-09-30.endive#tax_transaction_object-shipping_cost-tax_breakdown-tax_rate_details-tax_type), [Tax.Registration.country_options.us.type](/api/tax/registrations/object?api-version=2026-09-30.endive#tax_registration_object-country_options-us-type) |

#### Java

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [tax.Location](/api/tax/location/object?api-version=2026-09-30.endive#tax_location_object) |

| Methods | Change | Resource |
| --- | --- | --- |
| `create`, `list`, `retrieve` | Added | [tax.Location](/api/tax/location/object?api-version=2026-09-30.endive#tax_location_object) |

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `performanceLocation` | Added | [tax.CalculationCreateParams.line_items[]](/api/tax/calculations/create?api-version=2026-09-30.endive#calculate_tax-line_items), [tax.CalculationLineItem](/api/tax/calculations/line_items/object?api-version=2026-09-30.endive) |
| `admissionsTax`, `attendanceTax`, `entertainmentTax`, `grossReceiptsTax`, `hospitalityTax`, `luxuryTax`, `resortTax`, `tourismTax` | Added | [tax.Registration.country_options.us](/api/tax/registrations/object?api-version=2026-09-30.endive#tax_registration_object-country_options-us), [tax.RegistrationCreateParams.country_options.us](/api/tax/registrations/create?api-version=2026-09-30.endive#tax_registration_create-country_options-us) |
| `requirements` | Added | [TaxCode](/api/tax_codes/object?api-version=2026-09-30.endive#tax_code_object) |
| `taxDetails` | Added | [InvoiceAddLinesParams.lines[].price_data.product_data](/api/invoice-line-item/bulk?api-version=2026-09-30.endive#bulk_add_lines-lines-price_data-product_data), [InvoiceLineItemUpdateParams.price_data.product_data](/api/invoice-line-item/update?api-version=2026-09-30.endive#update_line-price_data-product_data), [InvoiceUpdateLinesParams.lines[].price_data.product_data](/api/invoice-line-item/invoices/update-lines/bulk?api-version=2026-09-30.endive#bulk_update_lines-lines-price_data-product_data), [PaymentLinkCreateParams.line_items[].price_data.product_data](/api/payment-link/create?api-version=2026-09-30.endive#create_payment_link-line_items-price_data-product_data), [PlanCreateParams.product[0]](/api/plans/create?api-version=2026-09-30.endive#create_plan-product-[0]), [PriceCreateParams.product_data](/api/prices/create?api-version=2026-09-30.endive#create_price-product_data), [Product](/api/products/object?api-version=2026-09-30.endive#product_object), [ProductCreateParams](/api/products/create?api-version=2026-09-30.endive#create_product), [ProductUpdateParams](/api/products/update?api-version=2026-09-30.endive#update_product), [checkout.SessionCreateParams.line_items[].price_data.product_data](/api/checkout/sessions/create?api-version=2026-09-30.endive#create_checkout_session-line_items-price_data-product_data), [checkout.SessionUpdateParams.line_items[].price_data.product_data](/api/checkout/sessions/update?api-version=2026-09-30.endive#update_checkout_session-line_items-price_data-product_data) |

| Values | Change | Enum |
| --- | --- | --- |
| `admissions_tax`, `attendance_tax`, `entertainment_tax`, `gross_receipts_tax`, `hospitality_tax`, `luxury_tax`, `resort_tax`, `tourism_tax` | Added | [tax.RegistrationCreateParams.country_options.us.type](/api/tax/registrations/create?api-version=2026-09-30.endive#tax_registration_create-country_options-us-type) |

#### Node.js

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [Tax.Location](/api/tax/location/object?api-version=2026-09-30.endive#tax_location_object) |

| Methods | Change | Resource |
| --- | --- | --- |
| `create`, `list`, `retrieve` | Added | [Tax.Location](/api/tax/location/object?api-version=2026-09-30.endive#tax_location_object) |

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `performance_location` | Added | [Tax.CalculationCreateParams.line_items[]](/api/tax/calculations/create?api-version=2026-09-30.endive#calculate_tax-line_items), [Tax.CalculationLineItem](/api/tax/calculations/line_items/object?api-version=2026-09-30.endive) |
| `admissions_tax`, `attendance_tax`, `entertainment_tax`, `gross_receipts_tax`, `hospitality_tax`, `luxury_tax`, `resort_tax`, `tourism_tax` | Added | [Tax.Registration.country_options.us](/api/tax/registrations/object?api-version=2026-09-30.endive#tax_registration_object-country_options-us), [Tax.RegistrationCreateParams.country_options.us](/api/tax/registrations/create?api-version=2026-09-30.endive#tax_registration_create-country_options-us) |
| `requirements` | Added | [TaxCode](/api/tax_codes/object?api-version=2026-09-30.endive#tax_code_object) |
| `tax_details` | Added | [Checkout.SessionCreateParams.line_items[].price_data.product_data](/api/checkout/sessions/create?api-version=2026-09-30.endive#create_checkout_session-line_items-price_data-product_data), [Checkout.SessionUpdateParams.line_items[].price_data.product_data](/api/checkout/sessions/update?api-version=2026-09-30.endive#update_checkout_session-line_items-price_data-product_data), [InvoiceAddLinesParams.lines[].price_data.product_data](/api/invoice-line-item/bulk?api-version=2026-09-30.endive#bulk_add_lines-lines-price_data-product_data), [InvoiceLineItemUpdateParams.price_data.product_data](/api/invoice-line-item/update?api-version=2026-09-30.endive#update_line-price_data-product_data), [InvoiceUpdateLinesParams.lines[].price_data.product_data](/api/invoice-line-item/invoices/update-lines/bulk?api-version=2026-09-30.endive#bulk_update_lines-lines-price_data-product_data), [PaymentLinkCreateParams.line_items[].price_data.product_data](/api/payment-link/create?api-version=2026-09-30.endive#create_payment_link-line_items-price_data-product_data), [PlanCreateParams.product[0]](/api/plans/create?api-version=2026-09-30.endive#create_plan-product-[0]), [PriceCreateParams.product_data](/api/prices/create?api-version=2026-09-30.endive#create_price-product_data), [Product](/api/products/object?api-version=2026-09-30.endive#product_object), [ProductCreateParams](/api/products/create?api-version=2026-09-30.endive#create_product), [ProductUpdateParams](/api/products/update?api-version=2026-09-30.endive#update_product) |

| Values | Change | Enums |
| --- | --- | --- |
| `performance` | Added | [Tax.CalculationLineItem.tax_breakdown[].sourcing](/api/tax/calculations/line_items/object?api-version=2026-09-30.endive#tax_calculation_line_item_object-tax_breakdown-sourcing), [Tax.Calculation.shipping_cost.tax_breakdown[].sourcing](/api/tax/calculations/object?api-version=2026-09-30.endive#tax_calculation_object-shipping_cost-tax_breakdown-sourcing), [Tax.Transaction.shipping_cost.tax_breakdown[].sourcing](/api/tax/transactions/object?api-version=2026-09-30.endive#tax_transaction_object-shipping_cost-tax_breakdown-sourcing) |
| `admissions_tax`, `attendance_tax`, `entertainment_tax`, `gross_receipts_tax`, `hospitality_tax`, `luxury_tax`, `resort_tax`, `tourism_tax` | Added | [Tax.CalculationLineItem.tax_breakdown[].tax_rate_details.tax_type](/api/tax/calculations/line_items/object?api-version=2026-09-30.endive#tax_calculation_line_item_object-tax_breakdown-tax_rate_details-tax_type), [Tax.Calculation.shipping_cost.tax_breakdown[].tax_rate_details.tax_type](/api/tax/calculations/object?api-version=2026-09-30.endive#tax_calculation_object-shipping_cost-tax_breakdown-tax_rate_details-tax_type), [Tax.Calculation.tax_breakdown[].tax_rate_details.tax_type](/api/tax/calculations/object?api-version=2026-09-30.endive#tax_calculation_object-tax_breakdown-tax_rate_details-tax_type), [Tax.Transaction.shipping_cost.tax_breakdown[].tax_rate_details.tax_type](/api/tax/transactions/object?api-version=2026-09-30.endive#tax_transaction_object-shipping_cost-tax_breakdown-tax_rate_details-tax_type), [Tax.RegistrationCreateParams.country_options.us.type](/api/tax/registrations/create?api-version=2026-09-30.endive#tax_registration_create-country_options-us-type), [Tax.Registration.country_options.us.type](/api/tax/registrations/object?api-version=2026-09-30.endive#tax_registration_object-country_options-us-type) |

#### Go

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [TaxLocation](/api/tax/location/object?api-version=2026-09-30.endive#tax_location_object) |

| Methods | Change | Resource |
| --- | --- | --- |
| `Get`, `List`, `New` | Added | [TaxLocation](/api/tax/location/object?api-version=2026-09-30.endive#tax_location_object) |

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `PerformanceLocation` | Added | [TaxCalculationLineItem](/api/tax/calculations/line_items/object?api-version=2026-09-30.endive), [TaxCalculationLineItemParams](/api/tax/calculations/create?api-version=2026-09-30.endive#calculate_tax-line_items) |
| `AdmissionsTax`, `AttendanceTax`, `EntertainmentTax`, `GrossReceiptsTax`, `HospitalityTax`, `LuxuryTax`, `ResortTax`, `TourismTax` | Added | [TaxRegistrationCountryOptionsUs](/api/tax/registrations/object?api-version=2026-09-30.endive#tax_registration_object-country_options-us), [TaxRegistrationCountryOptionsUsParams](/api/tax/registrations/create?api-version=2026-09-30.endive#tax_registration_create-country_options-us) |
| `Requirements` | Added | [TaxCode](/api/tax_codes/object?api-version=2026-09-30.endive#tax_code_object) |
| `TaxDetails` | Added | [CheckoutSessionLineItemPriceDataProductDataParams](/api/checkout/sessions/create?api-version=2026-09-30.endive#create_checkout_session-line_items-price_data-product_data), [InvoiceAddLinesLinePriceDataProductDataParams](/api/invoice-line-item/bulk?api-version=2026-09-30.endive#bulk_add_lines-lines-price_data-product_data), [InvoiceLineItemPriceDataProductDataParams](/api/invoice-line-item/update?api-version=2026-09-30.endive#update_line-price_data-product_data), [InvoiceUpdateLinesLinePriceDataProductDataParams](/api/invoice-line-item/invoices/update-lines/bulk?api-version=2026-09-30.endive#bulk_update_lines-lines-price_data-product_data), [PaymentLinkLineItemPriceDataProductDataParams](/api/payment-link/create?api-version=2026-09-30.endive#create_payment_link-line_items-price_data-product_data), [PlanProductParams](/api/plans/create?api-version=2026-09-30.endive#create_plan-product-[0]), [PriceProductDataParams](/api/prices/create?api-version=2026-09-30.endive#create_price-product_data), [Product](/api/products/object?api-version=2026-09-30.endive#product_object), [ProductParams](/api/products/update?api-version=2026-09-30.endive#update_product) |

| Values | Change | Enums |
| --- | --- | --- |
| `performance` | Added | [TaxCalculationLineItemTaxBreakdown.Sourcing](/api/tax/calculations/line_items/object?api-version=2026-09-30.endive#tax_calculation_line_item_object-tax_breakdown-sourcing), [TaxCalculationShippingCostTaxBreakdown.Sourcing](/api/tax/calculations/object?api-version=2026-09-30.endive#tax_calculation_object-shipping_cost-tax_breakdown-Sourcing), [TaxTransactionShippingCostTaxBreakdown.Sourcing](/api/tax/transactions/object?api-version=2026-09-30.endive#tax_transaction_object-shipping_cost-tax_breakdown-Sourcing) |
| `admissions_tax`, `attendance_tax`, `entertainment_tax`, `gross_receipts_tax`, `hospitality_tax`, `luxury_tax`, `resort_tax`, `tourism_tax` | Added | [TaxCalculationLineItemTaxBreakdownTaxRateDetails.TaxType](/api/tax/calculations/line_items/object?api-version=2026-09-30.endive#tax_calculation_line_item_object-tax_breakdown-tax_rate_details-tax_type), [TaxCalculationShippingCostTaxBreakdownTaxRateDetails.TaxType](/api/tax/calculations/object?api-version=2026-09-30.endive#tax_calculation_object-shipping_cost-tax_breakdown-tax_rate_details-TaxType), [TaxCalculationTaxBreakdownTaxRateDetails.TaxType](/api/tax/calculations/object?api-version=2026-09-30.endive#tax_calculation_object-tax_breakdown-tax_rate_details-TaxType), [TaxTransactionShippingCostTaxBreakdownTaxRateDetails.TaxType](/api/tax/transactions/object?api-version=2026-09-30.endive#tax_transaction_object-shipping_cost-tax_breakdown-tax_rate_details-TaxType), [TaxRegistrationCountryOptionsUs.Type](/api/tax/registrations/object?api-version=2026-09-30.endive#tax_registration_object-country_options-us-Type) |

#### .NET

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [Tax.Location](/api/tax/location/object?api-version=2026-09-30.endive#tax_location_object) |

| Methods | Change | Resource |
| --- | --- | --- |
| `Create`, `Get`, `List` | Added | [Tax.Location](/api/tax/location/object?api-version=2026-09-30.endive#tax_location_object) |

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `PerformanceLocation` | Added | [Tax.CalculationLineItem](/api/tax/calculations/line_items/object?api-version=2026-09-30.endive), [TaxCalculationLineItemOptions](/api/tax/calculations/create?api-version=2026-09-30.endive#calculate_tax-line_items) |
| `AdmissionsTax`, `AttendanceTax`, `EntertainmentTax`, `GrossReceiptsTax`, `HospitalityTax`, `LuxuryTax`, `ResortTax`, `TourismTax` | Added | [Tax.Registration.CountryOptions.Us](/api/tax/registrations/object?api-version=2026-09-30.endive#tax_registration_object-country_options-us), [TaxRegistrationCountryOptionsUsOptions](/api/tax/registrations/create?api-version=2026-09-30.endive#tax_registration_create-country_options-us) |
| `Requirements` | Added | [TaxCode](/api/tax_codes/object?api-version=2026-09-30.endive#tax_code_object) |
| `TaxDetails` | Added | [CheckoutSessionLineItemPriceDataProductDataOptions](/api/checkout/sessions/create?api-version=2026-09-30.endive#create_checkout_session-line_items-price_data-product_data), [InvoiceLineItemPriceDataProductDataOptions](/api/invoice-line-item/update?api-version=2026-09-30.endive#update_line-price_data-product_data), [InvoiceLinePriceDataProductDataOptions](/api/invoice-line-item/bulk?api-version=2026-09-30.endive#bulk_add_lines-lines-price_data-product_data), [PaymentLinkLineItemPriceDataProductDataOptions](/api/payment-link/create?api-version=2026-09-30.endive#create_payment_link-line_items-price_data-product_data), [PlanProductOptions](/api/plans/create?api-version=2026-09-30.endive#create_plan-product-[0]), [PriceProductDataOptions](/api/prices/create?api-version=2026-09-30.endive#create_price-product_data), [Product](/api/products/object?api-version=2026-09-30.endive#product_object), [ProductCreateOptions](/api/products/create?api-version=2026-09-30.endive#create_product), [ProductUpdateOptions](/api/products/update?api-version=2026-09-30.endive#update_product) |

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
- [Adds support for new tax types](https://docs.stripe.com/changelog/endive/2026-09-30/stripe-tax-new-tax-types.md)
