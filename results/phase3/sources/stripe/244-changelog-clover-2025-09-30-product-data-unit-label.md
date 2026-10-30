# Enables specifying units of measurement for Products

## What’s new

Adds the ability to specify a product’s unit of measurement using the [unit_label](https://docs.stripe.com/api/checkout/sessions/create.md?api-version=2025-09-30.clover#create_checkout_session-line_items-price_data-product_data-unit_label) parameter in the [product_data](https://docs.stripe.com/api/checkout/sessions/create.md?api-version=2025-09-30.clover#create_checkout_session-line_items-price_data-product_data) hash.

## Impact

You can now specify the `unit_label` when you create a [Product](https://docs.stripe.com/api/products.md?api-version=2025-09-30.clover) by adding a line item to a [Checkout Session](https://docs.stripe.com/api/checkout/sessions.md?api-version=2025-09-30.clover), [Payment Link](https://docs.stripe.com/api/payment-link.md?api-version=2025-09-30.clover), [Payment Intent](https://docs.stripe.com/api/payment_intents.md?api-version=2025-09-30.clover) or [Invoice](https://docs.stripe.com/api/invoices.md?api-version=2025-09-30.clover). You must include the product’s unit of measurement to meet the requirements of card network Level 2/Level 3 programmes.

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `unit_label` | Added | [Checkout.Session#create.line_items[].price_data.product_data](/api/checkout/sessions/create?api-version=2025-09-30.clover#create_checkout_session-line_items-price_data-product_data), [Invoice#add_lines.lines[].price_data.product_data](/api/invoice-line-item/bulk?api-version=2025-09-30.clover#bulk_invoice-lines-price_data-product_data), [Invoice#update_lines.lines[].price_data.product_data](/api/invoice-line-item/invoices/update-lines/bulk?api-version=2025-09-30.clover#bulk_invoice-lines-price_data-product_data), [InvoiceLineItem#update.price_data.product_data](/api/invoice-line-item/update?api-version=2025-09-30.clover#update_line_item-price_data-product_data), [PaymentLink#create.line_items[].price_data.product_data](/api/payment-link/create?api-version=2025-09-30.clover#create_payment_link-line_items-price_data-product_data) |

#### Ruby

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `unit_label` | Added | [Checkout::Session::CreateParams::LineItem::PriceDatum::ProductDatum](/api/checkout/sessions/create?api-version=2025-09-30.clover#create_checkout_session-line_items-price_data-product_data), [Invoice::AddLinesParams::Line::PriceDatum::ProductDatum](/api/invoice-line-item/bulk?api-version=2025-09-30.clover#bulk_invoice-lines-price_data-product_data), [Invoice::UpdateLinesParams::Line::PriceDatum::ProductDatum](/api/invoice-line-item/invoices/update-lines/bulk?api-version=2025-09-30.clover#bulk_invoice-lines-price_data-product_data), [InvoiceLineItem::UpdateParams::PriceDatum::ProductDatum](/api/invoice-line-item/update?api-version=2025-09-30.clover#update_line_item-price_data-product_data), [PaymentLink::CreateParams::LineItem::PriceDatum::ProductDatum](/api/payment-link/create?api-version=2025-09-30.clover#create_payment_link-line_items-price_data-product_data) |

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `unit_label` | Added | [Invoice.AddLinesParamsLinePriceDatumProductDatum](/api/invoice-line-item/bulk?api-version=2025-09-30.clover#bulk_invoice-lines-price_data-product_data), [Invoice.UpdateLinesParamsLinePriceDatumProductDatum](/api/invoice-line-item/invoices/update-lines/bulk?api-version=2025-09-30.clover#bulk_invoice-lines-price_data-product_data), [InvoiceLineItem.ModifyParamsPriceDatumProductDatum](/api/invoice-line-item/update?api-version=2025-09-30.clover#update_line_item-price_data-product_data), [PaymentLink.CreateParamsLineItemPriceDatumProductDatum](/api/payment-link/create?api-version=2025-09-30.clover#create_payment_link-line_items-price_data-product_data), [checkout.Session.CreateParamsLineItemPriceDatumProductDatum](/api/checkout/sessions/create?api-version=2025-09-30.clover#create_checkout_session-line_items-price_data-product_data) |

#### PHP

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `unit_label` | Added | [Checkout\Session.create().$params.line_item.price_datum.product_datum](/api/checkout/sessions/create?api-version=2025-09-30.clover#create_checkout_session-line_items-price_data-product_data), [Invoice.add_lines().$params.line.price_datum.product_datum](/api/invoice-line-item/bulk?api-version=2025-09-30.clover#bulk_invoice-lines-price_data-product_data), [Invoice.update_lines().$params.line.price_datum.product_datum](/api/invoice-line-item/invoices/update-lines/bulk?api-version=2025-09-30.clover#bulk_invoice-lines-price_data-product_data), [InvoiceLineItem.update().$params.price_datum.product_datum](/api/invoice-line-item/update?api-version=2025-09-30.clover#update_line_item-price_data-product_data), [PaymentLink.create().$params.line_item.price_datum.product_datum](/api/payment-link/create?api-version=2025-09-30.clover#create_payment_link-line_items-price_data-product_data) |

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `unitLabel` | Added | [InvoiceAddLinesParams.lines[].price_data.product_data](/api/invoice-line-item/bulk?api-version=2025-09-30.clover#bulk_invoice-lines-price_data-product_data), [InvoiceLineItemUpdateParams.price_data.product_data](/api/invoice-line-item/update?api-version=2025-09-30.clover#update_line_item-price_data-product_data), [InvoiceUpdateLinesParams.lines[].price_data.product_data](/api/invoice-line-item/invoices/update-lines/bulk?api-version=2025-09-30.clover#bulk_invoice-lines-price_data-product_data), [PaymentLinkCreateParams.line_items[].price_data.product_data](/api/payment-link/create?api-version=2025-09-30.clover#create_payment_link-line_items-price_data-product_data), [checkout.SessionCreateParams.line_items[].price_data.product_data](/api/checkout/sessions/create?api-version=2025-09-30.clover#create_checkout_session-line_items-price_data-product_data) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `unit_label` | Added | [Checkout.SessionCreateParams.line_items[].price_data.product_data](/api/checkout/sessions/create?api-version=2025-09-30.clover#create_checkout_session-line_items-price_data-product_data), [InvoiceAddLinesParams.lines[].price_data.product_data](/api/invoice-line-item/bulk?api-version=2025-09-30.clover#bulk_invoice-lines-price_data-product_data), [InvoiceLineItemUpdateParams.price_data.product_data](/api/invoice-line-item/update?api-version=2025-09-30.clover#update_line_item-price_data-product_data), [InvoiceUpdateLinesParams.lines[].price_data.product_data](/api/invoice-line-item/invoices/update-lines/bulk?api-version=2025-09-30.clover#bulk_invoice-lines-price_data-product_data), [PaymentLinkCreateParams.line_items[].price_data.product_data](/api/payment-link/create?api-version=2025-09-30.clover#create_payment_link-line_items-price_data-product_data) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `UnitLabel` | Added | [CheckoutSessionLineItemPriceDataProductDataParams](/api/checkout/sessions/create?api-version=2025-09-30.clover#create_checkout_session-line_items-price_data-product_data), [InvoiceAddLinesLinePriceDataProductDataParams](/api/invoice-line-item/bulk?api-version=2025-09-30.clover#bulk_invoice-lines-price_data-product_data), [InvoiceLineItemPriceDataProductDataParams](/api/invoice-line-item/update?api-version=2025-09-30.clover#update_line_item-price_data-product_data), [InvoiceUpdateLinesLinePriceDataProductDataParams](/api/invoice-line-item/invoices/update-lines/bulk?api-version=2025-09-30.clover#bulk_invoice-lines-price_data-product_data), [PaymentLinkLineItemPriceDataProductDataParams](/api/payment-link/create?api-version=2025-09-30.clover#create_payment_link-line_items-price_data-product_data) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `UnitLabel` | Added | [CheckoutSessionLineItemPriceDataProductDataOptions](/api/checkout/sessions/create?api-version=2025-09-30.clover#create_checkout_session-line_items-price_data-product_data), [InvoiceLineItemPriceDataProductDataOptions](/api/invoice-line-item/update?api-version=2025-09-30.clover#update_line_item-price_data-product_data), [InvoiceLinePriceDataProductDataOptions](/api/invoice-line-item/bulk?api-version=2025-09-30.clover#bulk_invoice-lines-price_data-product_data), [PaymentLinkLineItemPriceDataProductDataOptions](/api/payment-link/create?api-version=2025-09-30.clover#create_payment_link-line_items-price_data-product_data) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2025-09-30.clover`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to [v16.0.0](https://github.com/stripe/stripe-ruby/releases/tag/v16.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to [v13.0.1](https://github.com/stripe/stripe-python/releases/tag/v13.0.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to [v18.0.0](https://github.com/stripe/stripe-php/releases/tag/v18.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to [v30.0.0](https://github.com/stripe/stripe-java/releases/tag/v30.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to [v19.1.0](https://github.com/stripe/stripe-node/releases/tag/v19.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to [v83.0.0](https://github.com/stripe/stripe-go/releases/tag/v83.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to [v49.0.0](https://github.com/stripe/stripe-dotnet/releases/tag/v49.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

## Related changes

- [Removes postal code for card payments in certain regions on Checkout and Payment Element](https://docs.stripe.com/changelog/clover/2025-09-30/postal_code_in_card_form_for_non_us_countries.md)
- [Removes currency conversion field from Checkout Sessions](https://docs.stripe.com/changelog/clover/2025-09-30/remove-checkout-session-currency-conversion-field.md)
- [Removes support for the redirectToCheckout method](https://docs.stripe.com/changelog/clover/2025-09-30/remove-redirect-to-checkout.md)
- [Updates initCheckout to be synchronous](https://docs.stripe.com/changelog/clover/2025-09-30/update-init-checkout-synchronous.md)
- [Adds support for collecting business and individual names in Checkout Sessions](https://docs.stripe.com/changelog/clover/2025-09-30/checkout-name-collection.md)
- [Adds the ability to exclude payment methods from Checkout Sessions and Payment Intents](https://docs.stripe.com/changelog/clover/2025-09-30/exclude-payment-methods-checkout-sessions.md)
- [Adds support for setting the capture method for specific payment methods with the Checkout Sessions API](https://docs.stripe.com/changelog/clover/2025-09-30/checkout-capture-method-per-payment-method.md)
- [Adds support for configuring branding settings for Checkout Sessions](https://docs.stripe.com/changelog/clover/2025-09-30/checkout-sessions-branding-settings.md)
