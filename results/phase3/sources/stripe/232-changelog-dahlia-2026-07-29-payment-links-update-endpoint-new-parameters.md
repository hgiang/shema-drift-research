# Adds the ability to update shipping options, consent collection, and future usage support on Payment Links

## What’s new

Adds support for three additional parameters when [updating a Payment Link](https://docs.stripe.com/api/payment-link/update.md?api-version=2026-07-29.dahlia):

- [shipping_options](https://docs.stripe.com/api/payment-link/update.md?api-version=2026-07-29.dahlia#update_payment_link-shipping_options): Accepts an array of up to five shipping rate objects, each with a `shipping_rate` ID corresponding to an existing [Shipping Rate](https://docs.stripe.com/api/shipping_rates.md?api-version=2026-07-29.dahlia). Pass an empty array to remove all shipping options from a Payment Link.

- [consent_collection](https://docs.stripe.com/api/payment-link/update.md?api-version=2026-07-29.dahlia#update_payment_link-consent_collection): Lets you update the following consent collection settings on an existing Payment Link:

  - [consent_collection.payment_method_reuse_agreement.position](https://docs.stripe.com/api/payment-link/update.md?api-version=2026-07-29.dahlia#update_payment_link-consent_collection-payment_method_reuse_agreement-position): Controls where the payment method reuse agreement is displayed.
  - [consent_collection.promotions](https://docs.stripe.com/api/payment-link/update.md?api-version=2026-07-29.dahlia#update_payment_link-consent_collection-promotions): Controls whether to display a checkbox for promotional communications consent.
  - [consent_collection.terms_of_service](https://docs.stripe.com/api/payment-link/update.md?api-version=2026-07-29.dahlia#update_payment_link-consent_collection-terms_of_service): Controls whether to display a checkbox for terms of service acceptance.

- [payment_intent_data.setup_future_usage](https://docs.stripe.com/api/payment-link/update.md?api-version=2026-07-29.dahlia#update_payment_link-payment_intent_data-setup_future_usage): Set to `on_session` or `off_session` to indicate how you intend to [reuse the payment method](https://docs.stripe.com/payments/payment-intents.md#future-usage) collected during the Checkout Session. Previously, API requests that included this parameter returned a `400` error.

Previously, these parameters were only configurable through the Dashboard.

## Impact

You can now programmatically manage shipping options, consent collection, and future payment usage on existing [Payment Links](https://docs.stripe.com/payment-links.md) without using the Dashboard. Together, these additions make it possible to use the API to build automated workflows that update Payment Link configuration in response to changes in your business logic including recurring payment setups, shipping rate changes, and consent policy updates.

## Changes

#### REST API

| Parameters | Change | Resources or endpoints |
| --- | --- | --- |
| `setup_future_usage` | Added | [PaymentLink#update.payment_intent_data](/api/payment-link/update?api-version=2026-07-29.dahlia#update_payment_link-payment_intent_data) |
| `shipping_options` | Added | [PaymentLink#update](/api/payment-link/update?api-version=2026-07-29.dahlia#update_payment_link) |
| `consent_collection` | Added | [PaymentLink#update](/api/payment-link/update?api-version=2026-07-29.dahlia#update_payment_link) |

#### Ruby

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `setup_future_usage` | Added | [PaymentLinkUpdateParams::PaymentIntentDatum](/api/payment-link/update?api-version=2026-07-29.dahlia#update_payment_link-payment_intent_data) |
| `shipping_options` | Added | [PaymentLinkUpdateParams](/api/payment-link/update?api-version=2026-07-29.dahlia#update_payment_link) |
| `consent_collection` | Added | [PaymentLinkUpdateParams](/api/payment-link/update?api-version=2026-07-29.dahlia#update_payment_link) |

#### Python

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `setup_future_usage` | Added | [PaymentLinkModifyParamsPaymentIntentDatum](/api/payment-link/update?api-version=2026-07-29.dahlia#update_payment_link-payment_intent_data) |
| `shipping_options` | Added | [PaymentLinkModifyParams](/api/payment-link/update?api-version=2026-07-29.dahlia#update_payment_link) |
| `consent_collection` | Added | [PaymentLinkModifyParams](/api/payment-link/update?api-version=2026-07-29.dahlia#update_payment_link) |

#### PHP

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `setup_future_usage` | Added | [PaymentLink.update().$params.payment_intent_datum](/api/payment-link/update?api-version=2026-07-29.dahlia#update_payment_link-payment_intent_data) |
| `shipping_options` | Added | [PaymentLink.update().$params](/api/payment-link/update?api-version=2026-07-29.dahlia#update_payment_link) |
| `consent_collection` | Added | [PaymentLink.update().$params](/api/payment-link/update?api-version=2026-07-29.dahlia#update_payment_link) |

#### Java

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `setupFutureUsage` | Added | [PaymentLinkUpdateParams.payment_intent_data](/api/payment-link/update?api-version=2026-07-29.dahlia#update_payment_link-payment_intent_data) |
| `shippingOptions` | Added | [PaymentLinkUpdateParams](/api/payment-link/update?api-version=2026-07-29.dahlia#update_payment_link) |
| `consentCollection` | Added | [PaymentLinkUpdateParams](/api/payment-link/update?api-version=2026-07-29.dahlia#update_payment_link) |

#### Node.js

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `setup_future_usage` | Added | [PaymentLinkUpdateParams.payment_intent_data](/api/payment-link/update?api-version=2026-07-29.dahlia#update_payment_link-payment_intent_data) |
| `shipping_options` | Added | [PaymentLinkUpdateParams](/api/payment-link/update?api-version=2026-07-29.dahlia#update_payment_link) |
| `consent_collection` | Added | [PaymentLinkUpdateParams](/api/payment-link/update?api-version=2026-07-29.dahlia#update_payment_link) |

#### Go

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `SetupFutureUsage` | Added | [PaymentLinkPaymentIntentDataParams](/api/payment-link/update?api-version=2026-07-29.dahlia#update_payment_link-payment_intent_data) |
| `ShippingOptions` | Added | [PaymentLinkParams](/api/payment-link/update?api-version=2026-07-29.dahlia#update_payment_link) |
| `ConsentCollection` | Added | [PaymentLinkParams](/api/payment-link/update?api-version=2026-07-29.dahlia#update_payment_link) |

#### .NET

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `SetupFutureUsage` | Added | [PaymentLinkPaymentIntentDataOptions](/api/payment-link/update?api-version=2026-07-29.dahlia#update_payment_link-payment_intent_data) |
| `ShippingOptions` | Added | [PaymentLinkUpdateOptions](/api/payment-link/update?api-version=2026-07-29.dahlia#update_payment_link) |
| `ConsentCollection` | Added | [PaymentLinkUpdateOptions](/api/payment-link/update?api-version=2026-07-29.dahlia#update_payment_link) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2026-07-29.dahlia`
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

- [Adds the ability to indicate that you don’t intend to reuse Samsung Pay and PAYCO payment method types](https://docs.stripe.com/changelog/dahlia/2026-07-29/samsung-pay-and-payco-setup-future-usage-none-only.md)
- [Adds customer and payment method details to the Refunds API](https://docs.stripe.com/changelog/dahlia/2026-07-29/adds-customer-and-payment-method-details-to-the-refunds-api.md)
- [Adds support for new banks to FPX payments](https://docs.stripe.com/changelog/dahlia/2026-07-29/fpx-payments-new-banks.md)
- [Adds CHAPS as a supported network for funding instructions](https://docs.stripe.com/changelog/dahlia/2026-07-29/chaps-as-supported-networks.md)
- [Adds the allowed payment method types parameter to Payment Intents and Setup Intents](https://docs.stripe.com/changelog/dahlia/2026-07-29/allowed-payment-method-types-parameter.md)
- [Adds MB WAY support to the hosted invoice page](https://docs.stripe.com/changelog/dahlia/2026-07-29/hosted-invoice-page-mb-way-support.md)
- [Adds card network details to the Dispute object](https://docs.stripe.com/changelog/dahlia/2026-07-29/dispute-payment-method-details-card-network.md)
- [Adds the ability to list Payment Records](https://docs.stripe.com/changelog/dahlia/2026-07-29/list-payment-records.md)
