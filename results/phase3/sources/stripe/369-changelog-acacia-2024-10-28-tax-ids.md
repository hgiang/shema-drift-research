# Adds support for tax ID types in several new countries

## What’s new

Adds support for new tax ID types for Belarus, Morocco, Moldova, Tanzania, and Uzbekistan across various Stripe API endpoints and objects.

## Impact

This change lets you to collect, store, and process these specific tax ID types for customers in Belarus, Morocco, Moldova, Tanzania, and Uzbekistan.

## Changes

#### REST API

| Values | Change | Enums |
| --- | --- | --- |
| `by_tin`, `ma_vat`, `md_vat`, `tz_vat`, `uz_tin`, `uz_vat` | Added | [Checkout.Session.customer_details.tax_ids[].type](/api/checkout/sessions/object?api-version=2024-10-28.acacia#checkout_session_object-customer_details-tax_ids-type), [Invoice.customer_tax_ids[].type](/api/invoices/object?api-version=2024-10-28.acacia#invoice_object-customer_tax_ids-type), [Tax.Calculation.customer_details.tax_ids[].type](/api/tax/calculations/object?api-version=2024-10-28.acacia#tax_calculation_object-customer_details-tax_ids-type), [Tax.Transaction.customer_details.tax_ids[].type](/api/tax/transactions/object?api-version=2024-10-28.acacia#tax_transaction_object-customer_details-tax_ids-type), [TaxId.type](/api/tax_ids/object?api-version=2024-10-28.acacia#tax_id_object-type), [Customer#create.tax_id_data[].type](/api/customers/create?api-version=2024-10-28.acacia#create_customer-tax_id_data-type), [Invoice#create_preview.customer_details.tax_ids[].type](/api/invoices/create_preview?api-version=2024-10-28.acacia#create_create_preview-customer_details-tax_ids-type), [Invoice#upcoming.customer_details.tax_ids[].type](/api/invoices/upcoming?api-version=2024-10-28.acacia#upcoming_invoice-customer_details-tax_ids-type), [Invoice#upcomingLines.customer_details.tax_ids[].type](/api/invoice-line-item/invoices/upcoming/lines/retrieve?api-version=2024-10-28.acacia#upcoming_invoice_lines-customer_details-tax_ids-type), [Tax.Calculation#create.customer_details.tax_ids[].type](/api/tax/calculations/create?api-version=2024-10-28.acacia#calculate_tax-customer_details-tax_ids-type), [TaxId#create.type](/api/tax_ids/create?api-version=2024-10-28.acacia#create_tax_id-type) |

#### Ruby

This change doesn’t affect the Ruby SDK.

#### Python

| Values | Change | Enums |
| --- | --- | --- |
| `by_tin`, `ma_vat`, `md_vat`, `tz_vat`, `uz_tin`, `uz_vat` | Added | [stripe.checkout.Session.CustomerDetails.TaxId.type](/api/checkout/sessions/object?api-version=2024-10-28.acacia#checkout_session_object-customer_details-tax_ids-type), [stripe.Customer.CreateParamsTaxIdDatum.type](/api/customers/create?api-version=2024-10-28.acacia#create_customer-tax_id_data-type), [stripe.Customer.CreateTaxIdParams.type](/api/tax_ids/customer_create?api-version=2024-10-28.acacia#create_customer_tax_id-type), [stripe.Invoice.CustomerTaxId.type](/api/invoices/object?api-version=2024-10-28.acacia#invoice_object-customer_tax_ids-type), [stripe.Invoice.CreatePreviewParamsCustomerDetailsTaxId.type](/api/invoices/create_preview?api-version=2024-10-28.acacia#create_create_preview-customer_details-tax_ids-type), [stripe.Invoice.UpcomingParamsCustomerDetailsTaxId.type](/api/invoices/upcoming?api-version=2024-10-28.acacia#upcoming_invoice-customer_details-tax_ids-type), [stripe.Invoice.UpcomingLinesParamsCustomerDetailsTaxId.type](/api/invoice-line-item/invoices/upcoming/lines/retrieve?api-version=2024-10-28.acacia#upcoming_invoice_lines-customer_details-tax_ids-type), [stripe.tax.Calculation.CustomerDetails.TaxId.type](/api/tax/calculations/object?api-version=2024-10-28.acacia#tax_calculation_object-customer_details-tax_ids-type), [stripe.tax.Calculation.CreateParamsCustomerDetailsTaxId.type](/api/tax/calculations/create?api-version=2024-10-28.acacia#calculate_tax-customer_details-tax_ids-type), [stripe.tax.Transaction.CustomerDetails.TaxId.type](/api/tax/transactions/object?api-version=2024-10-28.acacia#tax_transaction_object-customer_details-tax_ids-type), [stripe.TaxId.type](/api/tax_ids/object?api-version=2024-10-28.acacia#tax_id_object-type), [stripe.TaxId.CreateParams.type](/api/tax_ids/create?api-version=2024-10-28.acacia#create_tax_id-type) |

#### PHP

| Values | Change | Enum |
| --- | --- | --- |
| `by_tin`, `ma_vat`, `md_vat`, `tz_vat`, `uz_tin`, `uz_vat` | Added | [TaxId.type](/api/tax_ids/object?api-version=2024-10-28.acacia#tax_id_object-type) |

#### Java

| Values | Change | Enums |
| --- | --- | --- |
| `by_tin`, `ma_vat`, `md_vat`, `tz_vat`, `uz_tin`, `uz_vat` | Added | [CustomerCreateParams.tax_id_data[].type](/api/customers/create?api-version=2024-10-28.acacia#create_customer-tax_id_data-type), [InvoiceCreatePreviewParams.customer_details.tax_ids[].type](/api/invoices/create_preview?api-version=2024-10-28.acacia#create_create_preview-customer_details-tax_ids-type), [InvoiceUpcomingLinesParams.customer_details.tax_ids[].type](/api/invoice-line-item/invoices/upcoming/lines/retrieve?api-version=2024-10-28.acacia#upcoming_invoice_lines-customer_details-tax_ids-type), [InvoiceUpcomingParams.customer_details.tax_ids[].type](/api/invoices/upcoming?api-version=2024-10-28.acacia#upcoming_invoice-customer_details-tax_ids-type), [TaxIdCreateParams.type](/api/tax_ids/create?api-version=2024-10-28.acacia#create_tax_id-type), [tax.CalculationCreateParams.customer_details.tax_ids[].type](/api/tax/calculations/create?api-version=2024-10-28.acacia#calculate_tax-customer_details-tax_ids-type) |

#### Node.js

| Values | Change | Enums |
| --- | --- | --- |
| `by_tin`, `ma_vat`, `md_vat`, `tz_vat`, `uz_tin`, `uz_vat` | Added | [Checkout.Session.customer_details.tax_ids[].type](/api/checkout/sessions/object?api-version=2024-10-28.acacia#checkout_session_object-customer_details-tax_ids-type), [Invoice.customer_tax_ids[].type](/api/invoices/object?api-version=2024-10-28.acacia#invoice_object-customer_tax_ids-type), [Tax.Calculation.customer_details.tax_ids[].type](/api/tax/calculations/object?api-version=2024-10-28.acacia#tax_calculation_object-customer_details-tax_ids-type), [Tax.Transaction.customer_details.tax_ids[].type](/api/tax/transactions/object?api-version=2024-10-28.acacia#tax_transaction_object-customer_details-tax_ids-type), [TaxId.type](/api/tax_ids/object?api-version=2024-10-28.acacia#tax_id_object-type), [CustomerCreateParams.tax_id_data[].type](/api/customers/create?api-version=2024-10-28.acacia#create_customer-tax_id_data-type), [InvoiceCreatePreviewParams.customer_details.tax_ids[].type](/api/invoices/create_preview?api-version=2024-10-28.acacia#create_create_preview-customer_details-tax_ids-type), [InvoiceUpcomingLinesParams.customer_details.tax_ids[].type](/api/invoice-line-item/invoices/upcoming/lines/retrieve?api-version=2024-10-28.acacia#upcoming_invoice_lines-customer_details-tax_ids-type), [InvoiceUpcomingParams.customer_details.tax_ids[].type](/api/invoices/upcoming?api-version=2024-10-28.acacia#upcoming_invoice-customer_details-tax_ids-type), [Tax.CalculationCreateParams.customer_details.tax_ids[].type](/api/tax/calculations/create?api-version=2024-10-28.acacia#calculate_tax-customer_details-tax_ids-type), [TaxIdCreateParams.type](/api/tax_ids/create?api-version=2024-10-28.acacia#create_tax_id-type) |

#### Go

| Values | Change | Enums |
| --- | --- | --- |
| `by_tin`, `ma_vat`, `md_vat`, `tz_vat`, `uz_tin`, `uz_vat` | Added | [CheckoutSessionCustomerDetailsTaxIdsType](/api/checkout/sessions/object?api-version=2024-10-28.acacia#checkout_session_object-customer_details-tax_ids-type), [InvoiceCustomerTaxIdsType](/api/invoices/object?api-version=2024-10-28.acacia#invoice_object-customer_tax_ids-type), [TaxCalculationCustomerDetailsTaxIdsType](/api/tax/calculations/object?api-version=2024-10-28.acacia#tax_calculation_object-customer_details-tax_ids-type), [TaxIdType](/api/tax_ids/object?api-version=2024-10-28.acacia#tax_id_object-type), [TaxTransactionCustomerDetailsTaxIdsType](/api/tax/transactions/object?api-version=2024-10-28.acacia#tax_transaction_object-customer_details-tax_ids-type) |

#### .NET

This change doesn’t affect the .NET SDK.

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2024-10-28.acacia`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to [v13.1.0](https://github.com/stripe/stripe-ruby/releases/tag/v13.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to [v11.2.0](https://github.com/stripe/stripe-python/releases/tag/v11.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to [v16.2.0](https://github.com/stripe/stripe-php/releases/tag/v16.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to [v28.0.0](https://github.com/stripe/stripe-java/releases/tag/v28.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to [v17.3.0](https://github.com/stripe/stripe-node/releases/tag/v17.3.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to [v81.0.0](https://github.com/stripe/stripe-go/releases/tag/v81.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to [v47.0.0](https://github.com/stripe/stripe-dotnet/releases/tag/v47.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

## Related changes

- [Adds support for new countries to the Tax Registration API](https://docs.stripe.com/changelog/acacia/2024-10-28/tax-registration-new-countries.md)
- [Adds support for collecting retail delivery fees](https://docs.stripe.com/changelog/acacia/2024-10-28/tax-retail-delivery-fee.md)
- [Adds option to automatically validate customer tax location during an update](https://docs.stripe.com/changelog/acacia/2024-10-28/tax-validate-location-auto.md)
