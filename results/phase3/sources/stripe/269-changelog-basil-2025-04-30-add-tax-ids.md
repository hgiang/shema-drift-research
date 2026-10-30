# Adds support for tax ID types in ten new countries

## What’s new

Adds support for new tax ID types for Aruba, Azerbaijan, Bangladesh, Benin, Burkina Faso, Cameroon, Cape Verde, Ethiopia, Kyrgyzstan, Laos and Philippines to [Checkout Sessions](https://docs.stripe.com/api/checkout/sessions.md?api-version=2025-04-30.basil), [Invoices](https://docs.stripe.com/api/invoices.md?api-version=2025-04-30.basil), [Tax Calculations](https://docs.stripe.com/api/tax/calculations.md?api-version=2025-04-30.basil), [Tax Transactions](https://docs.stripe.com/api/tax/transactions.md?api-version=2025-04-30.basil) and [Tax IDs](https://docs.stripe.com/api/tax_ids.md?api-version=2025-04-30.basil).

## Impact

This change lets you collect, store, and process tax ID types for customers in Aruba, Azerbaijan, Bangladesh, Benin, Burkina Faso, Cameroon, Cape Verde, Ethiopia, Kyrgyzstan, Laos, and Philippines.

## Changes

#### REST API

| Values | Change | Enums |
| --- | --- | --- |
| `aw_tin`, `az_tin`, `bd_bin`, `bf_ifu`, `bj_ifu`, `cm_niu`, `cv_nif`, `et_tin`, `kg_tin`, `la_tin` | Added | [Checkout.Session.customer_details.tax_ids[].type](/api/checkout/sessions/object?api-version=2025-04-30.basil#checkout_session_object-customer_details-tax_ids-type), [Invoice.customer_tax_ids[].type](/api/invoices/object?api-version=2025-04-30.basil#invoice_object-customer_tax_ids-type), [Tax.Calculation.customer_details.tax_ids[].type](/api/tax/calculations/object?api-version=2025-04-30.basil#tax_calculation_object-customer_details-tax_ids-type), [Tax.Transaction.customer_details.tax_ids[].type](/api/tax/transactions/object?api-version=2025-04-30.basil#tax_transaction_object-customer_details-tax_ids-type), [TaxId.type](/api/tax_ids/object?api-version=2025-04-30.basil#tax_id_object-type) |
| `aw_tin`, `az_tin`, `bd_bin`, `bf_ifu`, `bj_ifu`, `cm_niu`, `cv_nif`, `et_tin`, `kg_tin`, `la_tin` | Added | [Customer#create.tax_id_data[].type](/api/customers/create?api-version=2025-04-30.basil#create_customer-tax_id_data-type), [Invoice#create_preview.customer_details.tax_ids[].type](/api/invoices/create_preview?api-version=2025-04-30.basil#create_create_preview-customer_details-tax_ids-type), [Tax.Calculation#create.customer_details.tax_ids[].type](/api/tax/calculations/create?api-version=2025-04-30.basil#calculate_tax-customer_details-tax_ids-type), [TaxId#create.type](/api/tax_ids/create?api-version=2025-04-30.basil#create_tax_id-type) |

#### Ruby

This change doesn’t affect the Ruby SDK.

#### Python

| Values | Change | Enums |
| --- | --- | --- |
| `aw_tin`, `az_tin`, `bd_bin`, `bf_ifu`, `bj_ifu`, `cm_niu`, `cv_nif`, `et_tin`, `kg_tin`, `la_tin` | Added | `CheckoutSession.CustomerDetail.TaxId.type`, `CustomerTaxId.type`, `Invoice.CustomerTaxId.type`, `TaxCalculation.CustomerDetail.TaxId.type`, `TaxId.type`, `TaxTransaction.CustomerDetail.TaxId.type` |
| `aw_tin`, `az_tin`, `bd_bin`, `bf_ifu`, `bj_ifu`, `cm_niu`, `cv_nif`, `et_tin`, `kg_tin`, `la_tin` | Added | `Customer.CreateParamsTaxIdDatum.type`, `CustomerTaxId.CreateParams.type`, `Invoice.CreatePreviewParamsCustomerDetailTaxId.type`, `TaxId.CreateParams.type`, `tax.Calculation.CreateParamsCustomerDetailTaxId.type` |

#### PHP

| Values | Change | Enums |
| --- | --- | --- |
| `aw_tin`, `az_tin`, `bd_bin`, `bf_ifu`, `bj_ifu`, `cm_niu`, `cv_nif`, `et_tin`, `kg_tin`, `la_tin` | Added | `Invoice.customer_tax_ids[].type`, [TaxId.type](/api/tax_ids/object?api-version=2025-04-30.basil#tax_id_object-type) |

#### Java

| Values | Change | Enums |
| --- | --- | --- |
| `aw_tin`, `az_tin`, `bd_bin`, `bf_ifu`, `bj_ifu`, `cm_niu`, `cv_nif`, `et_tin`, `kg_tin`, `la_tin` | Added | [CustomerCreateParams.tax_id_data[].type](/api/customers/create?api-version=2025-04-30.basil#create_customer-tax_id_data-type), `CustomerTaxIdCreateParams.type`, [InvoiceCreatePreviewParams.customer_details.tax_ids[].type](/api/invoices/create_preview?api-version=2025-04-30.basil#create_create_preview-customer_details-tax_ids-type), [TaxIdCreateParams.type](/api/tax_ids/create?api-version=2025-04-30.basil#create_tax_id-type), [tax.CalculationCreateParams.customer_details.tax_ids[].type](/api/tax/calculations/create?api-version=2025-04-30.basil#calculate_tax-customer_details-tax_ids-type) |

#### Node.js

| Values | Change | Enums |
| --- | --- | --- |
| `aw_tin`, `az_tin`, `bd_bin`, `bf_ifu`, `bj_ifu`, `cm_niu`, `cv_nif`, `et_tin`, `kg_tin`, `la_tin` | Added | [Checkout.Session.customer_details.tax_ids[].type](/api/checkout/sessions/object?api-version=2025-04-30.basil#checkout_session_object-customer_details-tax_ids-type), `CustomerTaxId.type`, [Invoice.customer_tax_ids[].type](/api/invoices/object?api-version=2025-04-30.basil#invoice_object-customer_tax_ids-type), [Tax.Calculation.customer_details.tax_ids[].type](/api/tax/calculations/object?api-version=2025-04-30.basil#tax_calculation_object-customer_details-tax_ids-type), [Tax.Transaction.customer_details.tax_ids[].type](/api/tax/transactions/object?api-version=2025-04-30.basil#tax_transaction_object-customer_details-tax_ids-type), [TaxId.type](/api/tax_ids/object?api-version=2025-04-30.basil#tax_id_object-type) |
| `aw_tin`, `az_tin`, `bd_bin`, `bf_ifu`, `bj_ifu`, `cm_niu`, `cv_nif`, `et_tin`, `kg_tin`, `la_tin` | Added | [CustomerCreateParams.tax_id_data[].type](/api/customers/create?api-version=2025-04-30.basil#create_customer-tax_id_data-type), `CustomerTaxIdCreateParams.type`, [InvoiceCreatePreviewParams.customer_details.tax_ids[].type](/api/invoices/create_preview?api-version=2025-04-30.basil#create_create_preview-customer_details-tax_ids-type), [Tax.CalculationCreateParams.customer_details.tax_ids[].type](/api/tax/calculations/create?api-version=2025-04-30.basil#calculate_tax-customer_details-tax_ids-type), [TaxIdCreateParams.type](/api/tax_ids/create?api-version=2025-04-30.basil#create_tax_id-type) |

#### Go

| Values | Change | Enums |
| --- | --- | --- |
| `aw_tin`, `az_tin`, `bd_bin`, `bf_ifu`, `bj_ifu`, `cm_niu`, `cv_nif`, `et_tin`, `kg_tin`, `la_tin` | Added | `CheckoutSessionCustomerDetailsTaxIds.Type`, `TaxCalculationCustomerDetailsTaxIds.Type`, `TaxId.Type`, `TaxTransactionCustomerDetailsTaxIds.Type` |

#### .NET

This change doesn’t affect the .NET SDK.

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2025-04-30.basil`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to [v15.1.0](https://github.com/stripe/stripe-ruby/releases/tag/v15.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to [v12.1.0](https://github.com/stripe/stripe-python/releases/tag/v12.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to [v17.2.0](https://github.com/stripe/stripe-php/releases/tag/v17.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to [v29.1.0](https://github.com/stripe/stripe-java/releases/tag/v29.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to [v18.1.0](https://github.com/stripe/stripe-node/releases/tag/v18.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to [v82.1.0](https://github.com/stripe/stripe-go/releases/tag/v82.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to [v48.1.0](https://github.com/stripe/stripe-dotnet/releases/tag/v48.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

## Related changes

- [Tax Registration API now supports twelve new countries](https://docs.stripe.com/changelog/basil/2025-04-30/additional-tax-registration-countries.md)
