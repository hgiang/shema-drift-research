# Enables expansion for invoice pricing details

## What’s new

You can now [expand](https://docs.stripe.com/api/expanding_objects.md?api-version=2025-12-15.clover) the [price_details.price](https://docs.stripe.com/api/invoice-line-item/object.md?api-version=2025-12-15.clover#invoice_line_item_object-pricing-price_details-price) hash on [Invoice Line Items](https://docs.stripe.com/api/invoice-line-item/object.md?api-version=2025-12-15.clover#invoice_line_item_object-pricing-price_details-price) and [Invoice Items](https://docs.stripe.com/api/invoiceitems/object.md?api-version=2025-12-15.clover#invoiceitem_object-pricing-price_details-price) so that the details of the [Price](https://docs.stripe.com/api/prices.md?api-version=2025-12-15.clover) object are included in the response.

Previously, the `pricing_details.price` field returned only the price ID. You had to make a separate API call to retrieve the object details of the related Price.

## Impact

You can now get detailed information about [Prices](https://docs.stripe.com/api/prices.md?api-version=2025-12-15.clover) associated with [Invoice Items](https://docs.stripe.com/api/invoiceitems.md?api-version=2025-12-15.clover) and [Invoice Line Items](https://docs.stripe.com/api/invoice-line-item.md?api-version=2025-12-15.clover) with a single API request. This reduces the number of API requests needed to get granular pricing information for invoices.

To use this feature, specify the `price` field (including parent attributes) in the expand parameter when retrieving these resources.

## Changes

#### REST API

| Fields | Change | From → to |
| --- | --- | --- |
| `InvoiceItem.pricing.price_details.price`, `InvoiceLineItem.pricing.price_details.price` | Changed | `string → expandable($Price)` |

#### Ruby

| Fields | Change | From → to |
| --- | --- | --- |
| `InvoiceItem::Pricing::PriceDetail.price`, `InvoiceLineItem::Pricing::PriceDetail.price` | Changed | `string → expandable($Price)` |

#### Python

| Fields | Change | From → to |
| --- | --- | --- |
| `InvoiceItem.Pricing.PriceDetail.price`, `InvoiceLineItem.Pricing.PriceDetail.price` | Changed | `string → expandable($Price)` |

#### PHP

| Fields | Change | From → to |
| --- | --- | --- |
| `InvoiceItem.pricing.price_details.price`, `InvoiceLineItem.pricing.price_details.price` | Changed | `string → expandable($Price)` |

#### Java

| Fields | Change | From → to |
| --- | --- | --- |
| `InvoiceItem.pricing.price_details.price`, `InvoiceLineItem.pricing.price_details.price` | Changed | `string → expandable($Price)` |

#### Node.js

| Fields | Change | From → to |
| --- | --- | --- |
| `InvoiceItem.pricing.price_details.price`, `InvoiceLineItem.pricing.price_details.price` | Changed | `string → expandable(Price)` |

#### Go

| Fields | Change | From → to |
| --- | --- | --- |
| `InvoiceItemPricingPriceDetails.Price`, `InvoiceLineItemPricingPriceDetails.Price` | Changed | `string → expandable($Price)` |

#### .NET

| Fields | Change | From → to |
| --- | --- | --- |
| `InvoiceItem.Pricing.PriceDetails.Price`, `InvoiceLineItem.Pricing.PriceDetails.Price` | Changed | `string → expandable($Price)` |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2025-12-15.clover`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to [v18.2.0](https://github.com/stripe/stripe-ruby/releases/tag/v18.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to [v14.2.0](https://github.com/stripe/stripe-python/releases/tag/v14.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to [v19.2.0](https://github.com/stripe/stripe-php/releases/tag/v19.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to [v31.2.0](https://github.com/stripe/stripe-java/releases/tag/v31.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to [v20.2.0](https://github.com/stripe/stripe-node/releases/tag/v20.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to [v84.2.0](https://github.com/stripe/stripe-go/releases/tag/v84.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to [v50.2.0](https://github.com/stripe/stripe-dotnet/releases/tag/v50.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

## Related changes

- [Subscriptions updated from the Customer Portal can now also modify their billing cycle anchor](https://docs.stripe.com/changelog/clover/2025-12-15/customer-portal-billing-cycle-anchor.md)
- [Adds the ability to filter customer balance transactions by invoice](https://docs.stripe.com/changelog/clover/2025-12-15/customer-balance-transations-list-invoice.md)
- [Adds subtotal property to Invoice Line Items](https://docs.stripe.com/changelog/clover/2025-12-15/invoice-line-item-subtotal.md)
