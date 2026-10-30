# Adds Croatian Personal Identification Number to supported Tax IDs

## What’s new

Lets you include the Croatian Personal Identification Number (`hr_oib`) as a Tax ID type across various API endpoints, which improves support for Croatian customers and ensures accurate tax reporting and compliance.

## Changes

#### REST API

| Value | Change | Enums |
| --- | --- | --- |
| `hr_oib` | Added | [Checkout.Session.customer_details.tax_ids[].type](/api/checkout/sessions/object?api-version=2024-09-30.acacia#checkout_session_object-customer_details-tax_ids-type), [Customer#create.tax_id_data[].type](/api/customers/create?api-version=2024-09-30.acacia#create_customer-tax_id_data-type), [Invoice.customer_tax_ids[].type](/api/invoices/object?api-version=2024-09-30.acacia#invoice_object-customer_tax_ids-type), [Invoice#create_preview.customer_details.tax_ids[].type](/api/invoices/create_preview?api-version=2024-09-30.acacia#create_create_preview-customer_details-tax_ids-type), [Invoice#upcoming.customer_details.tax_ids[].type](/api/invoices/upcoming?api-version=2024-09-30.acacia#upcoming_invoice-customer_details-tax_ids-type), [Invoice#upcomingLines.customer_details.tax_ids[].type](/api/invoice-line-item/invoices/upcoming/lines/retrieve?api-version=2024-09-30.acacia#upcoming_invoice_lines-customer_details-tax_ids-type), [Tax.Calculation#create.customer_details.tax_ids[].type](/api/tax/calculations/create?api-version=2024-09-30.acacia#calculate_tax-customer_details-tax_ids-type), [Tax.Calculation.customer_details.tax_ids[].type](/api/tax/calculations/object?api-version=2024-09-30.acacia#tax_calculation_object-customer_details-tax_ids-type), [Tax.Transaction.customer_details.tax_ids[].type](/api/tax/transactions/object?api-version=2024-09-30.acacia#tax_transaction_object-customer_details-tax_ids-type), [TaxId#create.type](/api/tax_ids/create?api-version=2024-09-30.acacia#create_tax_id-type), [TaxId.type](/api/tax_ids/object?api-version=2024-09-30.acacia#tax_id_object-type) |

#### Ruby

This change doesn’t affect the Ruby SDK.

#### Python

This change doesn’t affect the Python SDK.

#### PHP

| Value | Change | Enum |
| --- | --- | --- |
| `hr_oib` | Added | [TaxId.type](/api/tax_ids/object?api-version=2024-09-30.acacia#tax_id_object-type) |

#### Java

| Value | Change | Enums |
| --- | --- | --- |
| `hr_oib` | Added | [CustomerCreateParams.tax_id_data[].type](/api/customers/create?api-version=2024-09-30.acacia#create_customer-tax_id_data-type), [InvoiceCreatePreviewParams.customer_details.tax_ids[].type](/api/invoices/create_preview?api-version=2024-09-30.acacia#create_create_preview-customer_details-tax_ids-type), [InvoiceUpcomingLinesParams.customer_details.tax_ids[].type](/api/invoice-line-item/invoices/upcoming/lines/retrieve?api-version=2024-09-30.acacia#upcoming_invoice_lines-customer_details-tax_ids-type), [InvoiceUpcomingParams.customer_details.tax_ids[].type](/api/invoices/upcoming?api-version=2024-09-30.acacia#upcoming_invoice-customer_details-tax_ids-type), [TaxIdCreateParams.type](/api/tax_ids/create?api-version=2024-09-30.acacia#create_tax_id-type), [tax.CalculationCreateParams.customer_details.tax_ids[].type](/api/tax/calculations/create?api-version=2024-09-30.acacia#calculate_tax-customer_details-tax_ids-type) |

#### Node.js

| Value | Change | Enums |
| --- | --- | --- |
| `hr_oib` | Added | [Checkout.Session.customer_details.tax_ids[].type](/api/checkout/sessions/object?api-version=2024-09-30.acacia#checkout_session_object-customer_details-tax_ids-type), [CustomerCreateParams.tax_id_data[].type](/api/customers/create?api-version=2024-09-30.acacia#create_customer-tax_id_data-type), [InvoiceCreatePreviewParams.customer_details.tax_ids[].type](/api/invoices/create_preview?api-version=2024-09-30.acacia#create_create_preview-customer_details-tax_ids-type), [InvoiceUpcomingLinesParams.customer_details.tax_ids[].type](/api/invoice-line-item/invoices/upcoming/lines/retrieve?api-version=2024-09-30.acacia#upcoming_invoice_lines-customer_details-tax_ids-type), [InvoiceUpcomingParams.customer_details.tax_ids[].type](/api/invoices/upcoming?api-version=2024-09-30.acacia#upcoming_invoice-customer_details-tax_ids-type), [Invoice.customer_tax_ids[].type](/api/invoices/object?api-version=2024-09-30.acacia#invoice_object-customer_tax_ids-type), [Tax.Calculation.customer_details.tax_ids[].type](/api/tax/calculations/object?api-version=2024-09-30.acacia#tax_calculation_object-customer_details-tax_ids-type), [Tax.CalculationCreateParams.customer_details.tax_ids[].type](/api/tax/calculations/create?api-version=2024-09-30.acacia#calculate_tax-customer_details-tax_ids-type), [TaxIdCreateParams.type](/api/tax_ids/create?api-version=2024-09-30.acacia#create_tax_id-type), [Tax.Transaction.customer_details.tax_ids[].type](/api/tax/transactions/object?api-version=2024-09-30.acacia#tax_transaction_object-customer_details-tax_ids-type), [TaxId.type](/api/tax_ids/object?api-version=2024-09-30.acacia#tax_id_object-type) |

#### Go

| Value | Change | Enums |
| --- | --- | --- |
| `hr_oib` | Added | [CheckoutSessionCustomerDetailsTaxIdsType](/api/checkout/sessions/object?api-version=2024-09-30.acacia#checkout_session_object-customer_details-tax_ids-type), [InvoiceCustomerTaxIdsType](/api/invoices/object?api-version=2024-09-30.acacia#invoice_object-customer_tax_ids-type), [TaxCalculationCustomerDetailsTaxIdsType](/api/tax/calculations/object?api-version=2024-09-30.acacia#tax_calculation_object-customer_details-tax_ids-type), [TaxIdType](/api/tax_ids/object?api-version=2024-09-30.acacia#tax_id_object-type), [TaxTransactionCustomerDetailsTaxIdsType](/api/tax/transactions/object?api-version=2024-09-30.acacia#tax_transaction_object-customer_details-tax_ids-type) |

#### .NET

This change doesn’t affect the .NET SDK.

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2024-09-30.acacia`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to [v13.0.0](https://github.com/stripe/stripe-ruby/releases/tag/v13.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to [v11.0.0](https://github.com/stripe/stripe-python/releases/tag/v11.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to [v16.0.0](https://github.com/stripe/stripe-php/releases/tag/v16.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to [v27.0.0](https://github.com/stripe/stripe-java/releases/tag/v27.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to [v17.0.0](https://github.com/stripe/stripe-node/releases/tag/v17.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to [v80.0.0](https://github.com/stripe/stripe-go/releases/tag/v80.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to [v46.0.0](https://github.com/stripe/stripe-dotnet/releases/tag/v46.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

## Related changes

- [Adds Switzerland UID as a supported customer tax ID](https://docs.stripe.com/changelog/acacia/2024-09-30/switzerland-tax-uid.md)
- [Adds support for requiring a customer tax ID on Checkout and Payment Links](https://docs.stripe.com/changelog/acacia/2024-09-30/requiring-customer-tax-id-checkout-session-paymentlink.md)
