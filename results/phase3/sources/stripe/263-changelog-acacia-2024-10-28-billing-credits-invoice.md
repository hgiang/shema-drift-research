# Adds support for pre-tax credit amount information to invoices

## What’s new

Adds the [pretax_credit_amounts](https://docs.stripe.com/api/invoice-line-item/object.md?api-version=2024-10-28.acacia#invoice_line_item_object-pretax_credit_amounts) attribute to the [Invoice Line Item](https://docs.stripe.com/api/invoice-line-item.md?api-version=2024-10-28.acacia) resource and the [total_pretax_credit_amounts](https://docs.stripe.com/api/invoices/object.md?api-version=2024-10-28.acacia#invoice_object-total_pretax_credit_amounts) attribute to the [Invoice](https://docs.stripe.com/api/invoices.md?api-version=2024-10-28.acacia) resource. These fields contains information about [billing credits](https://docs.stripe.com/billing/subscriptions/usage-based/billing-credits.md), along with other pre-tax credits like discounts, that were applied to the invoice.

## Impact

You can now see a breakdown of credits applied to an invoice before tax calculations, including discounts. This information shows which credit notes were issued and how they relate to the invoice.

## Changes

#### REST API

| Parameters | Change | Resources or endpoints |
| --- | --- | --- |
| `pretax_credit_amounts` | Added | [InvoiceLineitem](/api/invoice-line-item/object?api-version=2024-10-28.acacia) |
| `total_pretax_credit_amounts` | Added | [Invoice](/api/invoices/object?api-version=2024-10-28.acacia) |

#### Ruby

This change doesn’t affect the Ruby SDK.

#### Python

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `pretax_credit_amounts` | Added | [stripe.InvoiceLineitem](/api/invoice-line-item/object?api-version=2024-10-28.acacia) |
| `total_pretax_credit_amounts` | Added | [stripe.Invoice](/api/invoices/object?api-version=2024-10-28.acacia) |

#### PHP

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `pretax_credit_amounts` | Added | [InvoiceLineitem](/api/invoice-line-item/object?api-version=2024-10-28.acacia) |
| `total_pretax_credit_amounts` | Added | [Invoice](/api/invoices/object?api-version=2024-10-28.acacia) |

#### Java

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `pretax_credit_amounts` | Added | [InvoiceLineitem](/api/invoice-line-item/object?api-version=2024-10-28.acacia) |
| `total_pretax_credit_amounts` | Added | [Invoice](/api/invoices/object?api-version=2024-10-28.acacia) |

#### Node.js

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `pretax_credit_amounts` | Added | [InvoiceLineitem](/api/invoice-line-item/object?api-version=2024-10-28.acacia) |
| `total_pretax_credit_amounts` | Added | [Invoice](/api/invoices/object?api-version=2024-10-28.acacia) |

#### Go

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `PretaxCreditAmounts` | Added | [InvoiceLineitem](/api/invoice-line-item/object?api-version=2024-10-28.acacia) |
| `TotalPretaxCreditAmounts` | Added | [Invoice](/api/invoices/object?api-version=2024-10-28.acacia) |

#### .NET

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `PretaxCreditAmounts` | Added | [InvoiceLineitem](/api/invoice-line-item/object?api-version=2024-10-28.acacia) |
| `TotalPretaxCreditAmounts` | Added | [Invoice](/api/invoices/object?api-version=2024-10-28.acacia) |

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

- [Adds Credit Grant APIs and resources](https://docs.stripe.com/changelog/acacia/2024-10-28/billing-credits-apis.md)
- [Adds support for pre-tax credit amount information to credit notes](https://docs.stripe.com/changelog/acacia/2024-10-28/billing-credits-credit-note.md)
