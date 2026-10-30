# Adds support for Invoice Rendering Templates on Checkout and Payment Links

## What’s new

Adds the new `template` parameter to the existing `invoice_creation[invoice_data][rendering_options]` parameter on the [Create a Checkout Session](https://docs.stripe.com/api/checkout/sessions/create.md?api-version=2025-07-30.basil), [Create a Payment Link](https://docs.stripe.com/api/payment-link/create.md?api-version=2025-07-30.basil) and [Update a Payment Link](https://docs.stripe.com/api/payment-link/update.md?api-version=2025-07-30.basil) endpoints.

## Impact

Checkout and Payment Link users can now use an [Invoice Rendering Template](https://docs.stripe.com/invoicing/invoice-rendering-template.md) when creating [post-payment invoices](https://docs.stripe.com/receipts.md#paid-invoice-receipts).

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `template` | Added | [Checkout.Session#create.invoice_creation.invoice_data.rendering_options](/api/checkout/sessions/create?api-version=2025-07-30.basil#create_checkout_session-invoice_creation-invoice_data-rendering_options-template), [Checkout.Session.invoice_creation.invoice_data.rendering_options](/api/checkout/sessions/object?api-version=2025-07-30.basil#checkout_session_object-invoice_creation-invoice_data-rendering_options-template), [PaymentLink#create.invoice_creation.invoice_data.rendering_options](/api/payment-link/create?api-version=2025-07-30.basil#create_payment_link-invoice_creation-invoice_data-rendering_options-template), [PaymentLink#update.invoice_creation.invoice_data.rendering_options](/api/payment-link/update?api-version=2025-07-30.basil#update_payment_link-invoice_creation-invoice_data-rendering_options-template), [PaymentLink.invoice_creation.invoice_data.rendering_options](/api/payment-link/object?api-version=2025-07-30.basil#payment_link_object-invoice_creation-invoice_data-rendering_options-template) |

#### Ruby

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `template` | Added | [Checkout::Session::CreateParams::InvoiceCreation::InvoiceDatum::RenderingOption](/api/checkout/sessions/create?api-version=2025-07-30.basil#create_checkout_session-invoice_creation-invoice_data-rendering_options-template), [Checkout::Session::InvoiceCreation::InvoiceDatum::RenderingOption](/api/checkout/sessions/object?api-version=2025-07-30.basil#checkout_session_object-invoice_creation-invoice_data-rendering_options-template), [PaymentLink::CreateParams::InvoiceCreation::InvoiceDatum::RenderingOption](/api/payment-link/create?api-version=2025-07-30.basil#create_payment_link-invoice_creation-invoice_data-rendering_options-template), [PaymentLink::InvoiceCreation::InvoiceDatum::RenderingOption](/api/payment-link/object?api-version=2025-07-30.basil#payment_link_object-invoice_creation-invoice_data-rendering_options-template), [PaymentLink::UpdateParams::InvoiceCreation::InvoiceDatum::RenderingOption](/api/payment-link/update?api-version=2025-07-30.basil#update_payment_link-invoice_creation-invoice_data-rendering_options-template) |

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `template` | Added | [Checkout.Session.InvoiceCreation.InvoiceDatum.RenderingOption](/api/checkout/sessions/object?api-version=2025-07-30.basil#checkout_session_object-invoice_creation-invoice_data-rendering_options-template), [PaymentLink.CreateParamsInvoiceCreationInvoiceDatumRenderingOption](/api/payment-link/create?api-version=2025-07-30.basil#create_payment_link-invoice_creation-invoice_data-rendering_options-template), [PaymentLink.InvoiceCreation.InvoiceDatum.RenderingOption](/api/payment-link/object?api-version=2025-07-30.basil#payment_link_object-invoice_creation-invoice_data-rendering_options-template), [PaymentLink.ModifyParamsInvoiceCreationInvoiceDatumRenderingOption](/api/payment-link/update?api-version=2025-07-30.basil#update_payment_link-invoice_creation-invoice_data-rendering_options-template), [checkout.Session.CreateParamsInvoiceCreationInvoiceDatumRenderingOption](/api/checkout/sessions/create?api-version=2025-07-30.basil#create_checkout_session-invoice_creation-invoice_data-rendering_options-template) |

#### PHP

This change doesn’t affect the PHP SDK.

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `template` | Added | [PaymentLink.invoice_creation.invoice_data.rendering_options](/api/payment-link/object?api-version=2025-07-30.basil#payment_link_object-invoice_creation-invoice_data-rendering_options-template), [PaymentLinkCreateParams.invoice_creation.invoice_data.rendering_options](/api/payment-link/create?api-version=2025-07-30.basil#create_payment_link-invoice_creation-invoice_data-rendering_options-template), [PaymentLinkUpdateParams.invoice_creation.invoice_data.rendering_options](/api/payment-link/update?api-version=2025-07-30.basil#update_payment_link-invoice_creation-invoice_data-rendering_options-template), [checkout.Session.invoice_creation.invoice_data.rendering_options](/api/checkout/sessions/object?api-version=2025-07-30.basil#checkout_session_object-invoice_creation-invoice_data-rendering_options-template), [checkout.SessionCreateParams.invoice_creation.invoice_data.rendering_options](/api/checkout/sessions/create?api-version=2025-07-30.basil#create_checkout_session-invoice_creation-invoice_data-rendering_options-template) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `template` | Added | [Checkout.Session.invoice_creation.invoice_data.rendering_options](/api/checkout/sessions/object?api-version=2025-07-30.basil#checkout_session_object-invoice_creation-invoice_data-rendering_options-template), [Checkout.SessionCreateParams.invoice_creation.invoice_data.rendering_options](/api/checkout/sessions/create?api-version=2025-07-30.basil#create_checkout_session-invoice_creation-invoice_data-rendering_options-template), [PaymentLink.invoice_creation.invoice_data.rendering_options](/api/payment-link/object?api-version=2025-07-30.basil#payment_link_object-invoice_creation-invoice_data-rendering_options-template), [PaymentLinkCreateParams.invoice_creation.invoice_data.rendering_options](/api/payment-link/create?api-version=2025-07-30.basil#create_payment_link-invoice_creation-invoice_data-rendering_options-template), [PaymentLinkUpdateParams.invoice_creation.invoice_data.rendering_options](/api/payment-link/update?api-version=2025-07-30.basil#update_payment_link-invoice_creation-invoice_data-rendering_options-template) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `Template` | Added | [CheckoutSessionInvoiceCreationInvoiceDataRenderingOptions](/api/checkout/sessions/object?api-version=2025-07-30.basil#checkout_session_object-invoice_creation-invoice_data-rendering_options-template), [CheckoutSessionInvoiceCreationInvoiceDataRenderingOptionsParams](/api/checkout/sessions/create?api-version=2025-07-30.basil#create_checkout_session-invoice_creation-invoice_data-rendering_options-template), [PaymentLinkInvoiceCreationInvoiceDataRenderingOptions](/api/payment-link/object?api-version=2025-07-30.basil#payment_link_object-invoice_creation-invoice_data-rendering_options-template), [PaymentLinkInvoiceCreationInvoiceDataRenderingOptionsParams](/api/payment-link/create?api-version=2025-07-30.basil#create_payment_link-invoice_creation-invoice_data-rendering_options-template) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `Template` | Added | [Checkout.Session.InvoiceCreation.InvoiceData.RenderingOptions](/api/checkout/sessions/object?api-version=2025-07-30.basil#checkout_session_object-invoice_creation-invoice_data-rendering_options-template), [CheckoutSessionInvoiceCreationInvoiceDataRenderingOptionsOptions](/api/checkout/sessions/create?api-version=2025-07-30.basil#create_checkout_session-invoice_creation-invoice_data-rendering_options-template), [PaymentLink.InvoiceCreation.InvoiceData.RenderingOptions](/api/payment-link/object?api-version=2025-07-30.basil#payment_link_object-invoice_creation-invoice_data-rendering_options-template), [PaymentLinkInvoiceCreationInvoiceDataRenderingOptionsOptions](/api/payment-link/create?api-version=2025-07-30.basil#create_payment_link-invoice_creation-invoice_data-rendering_options-template) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2025-07-30.basil`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to [v15.4.0](https://github.com/stripe/stripe-ruby/releases/tag/v15.4.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to [v12.4.0](https://github.com/stripe/stripe-python/releases/tag/v12.4.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to [v17.5.0](https://github.com/stripe/stripe-php/releases/tag/v17.5.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to [v29.4.0](https://github.com/stripe/stripe-java/releases/tag/v29.4.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to [v18.4.0](https://github.com/stripe/stripe-node/releases/tag/v18.4.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to [v82.4.0](https://github.com/stripe/stripe-go/releases/tag/v82.4.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to [v48.4.0](https://github.com/stripe/stripe-dotnet/releases/tag/v48.4.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

## Related changes

- [Enhances Checkout for app-to-web purchases](https://docs.stripe.com/changelog/basil/2025-07-30/checkout-origin-context.md)
- [Adds support for disabling future usage of Pix in Checkout Sessions](https://docs.stripe.com/changelog/basil/2025-07-30/disable-future-usage-of-pix-in-checkout-sessions.md)
- [Adds support for the NZ BECS Direct Debit local payment method in Checkout and Payment Links](https://docs.stripe.com/changelog/basil/2025-07-30/nz-bank-account-checkout-payment-links.md)
