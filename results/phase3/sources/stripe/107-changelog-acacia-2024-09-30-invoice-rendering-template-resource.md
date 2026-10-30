# Adds Invoice Rendering Templates for Invoices

## What’s new

Use Invoice Rendering Templates to specify rules for how invoices group and display line items, default descriptions, footers and custom fields. [Create the templates](https://docs.stripe.com/invoicing/group-line-items.md#create-an-invoice-rendering-template) in the Dashboard and apply it to [Invoices](https://docs.stripe.com/api/invoices.md?api-version=2024-09-30.acacia) and [Customers](https://docs.stripe.com/api/customers.md?api-version=2024-09-30.acacia).

## Impact

This version lets you [configure templates](https://docs.stripe.com/invoicing/group-line-items.md#create-an-invoice-rendering-template) to apply to specific Invoices and Customers in the Dashboard or through the API. You can use the templates to group the lines of an invoice together or provide default descriptions, footers, and custom fields.

## Changes

#### REST API

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [InvoiceRenderingTemplate](/api/invoice-rendering-template/object?api-version=2024-09-30.acacia) |

#### Ruby

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [InvoiceRenderingTemplate](/api/invoice-rendering-template/object?api-version=2024-09-30.acacia) |

#### Python

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [stripe.InvoiceRenderingTemplate](/api/invoice-rendering-template/object?api-version=2024-09-30.acacia) |

#### PHP

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [InvoiceRenderingTemplate](/api/invoice-rendering-template/object?api-version=2024-09-30.acacia) |

#### Java

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [InvoiceRenderingTemplate](/api/invoice-rendering-template/object?api-version=2024-09-30.acacia) |

#### Node.js

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [InvoiceRenderingTemplate](/api/invoice-rendering-template/object?api-version=2024-09-30.acacia) |

#### Go

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [InvoiceRenderingTemplate](/api/invoice-rendering-template/object?api-version=2024-09-30.acacia) |

#### .NET

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [InvoiceRenderingTemplate](/api/invoice-rendering-template/object?api-version=2024-09-30.acacia) |

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

- [Adds retrieve and archive methods for Invoice Rendering Templates](https://docs.stripe.com/changelog/acacia/2024-09-30/invoice-rendering-template-methods.md)
- [Adds support for templates to Invoices and Customers](https://docs.stripe.com/changelog/acacia/2024-09-30/invoice-rendering-template-parameter.md)
- [Adds version support for Invoice Rendering Templates](https://docs.stripe.com/changelog/acacia/2024-09-30/invoice-rendering-template-version.md)
