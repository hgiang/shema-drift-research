# Removes currency conversion field from Checkout Sessions

## What’s new

Removes the [currency_conversion](https://docs.stripe.com/api/checkout/sessions/object.md?api-version=2025-09-30.clover#checkout_session_object-currency_conversion) field from [Checkout Sessions](https://docs.stripe.com/api/checkout/sessions.md?api-version=2025-09-30.clover).

## Why is this a breaking change?

Previously, the [currency_conversion](https://docs.stripe.com/api/checkout/sessions/object.md?api-version=2025-09-30.clover#checkout_session_object-currency_conversion) field provided details about [Adaptive Pricing](https://docs.stripe.com/api/payments/currencies/localize-prices/adaptive-pricing.md?api-version=2025-09-30.clover) for Checkout Sessions created before 30/03/2025. Any Checkout Sessions created after 30/03/2025 that use Adaptive Pricing have the [presentment_details](https://docs.stripe.com/api/checkout/sessions/object.md?api-version=2025-09-30.clover#checkout_session_object-presentment_details) field populated instead.

## Impact

The [currency_conversion](https://docs.stripe.com/api/checkout/sessions/object.md?api-version=2025-09-30.clover#checkout_session_object-currency_conversion) field contains currency and amount information when [Adaptive Pricing](https://docs.stripe.com/api/payments/currencies/localize-prices/adaptive-pricing.md?api-version=2025-09-30.clover) was used on a Checkout Session.

To get this information starting with API version `2025-09-30.clover` or later:

- For Checkout Session objects created before 2025-03-30, use the top level fields on the Checkout Session object
- For Checkout Session objects created on or after 30/03/2025, use the [presentment_details](https://docs.stripe.com/api/checkout/sessions/object.md?api-version=2025-09-30.clover#checkout_session_object-presentment_details) field stored on the Checkout Session object

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `currency_conversion` | Changed | [Checkout.Session](/api/checkout/sessions/object?api-version=2025-09-30.clover) |

#### Ruby

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `currency_conversion` | Changed | [Checkout::Session](/api/checkout/sessions/object?api-version=2025-09-30.clover) |

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `currency_conversion` | Changed | [Checkout.Session](/api/checkout/sessions/object?api-version=2025-09-30.clover) |

#### PHP

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `currency_conversion` | Changed | [Checkout.Session](/api/checkout/sessions/object?api-version=2025-09-30.clover) |

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `currencyConversion` | Changed | [checkout.Session](/api/checkout/sessions/object?api-version=2025-09-30.clover) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `currency_conversion` | Changed | [Checkout.Session](/api/checkout/sessions/object?api-version=2025-09-30.clover) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `CurrencyConversion` | Changed | [CheckoutSession](/api/checkout/sessions/object?api-version=2025-09-30.clover) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `CurrencyConversion` | Changed | [Checkout.Session](/api/checkout/sessions/object?api-version=2025-09-30.clover) |

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
- [Removes support for the redirectToCheckout method](https://docs.stripe.com/changelog/clover/2025-09-30/remove-redirect-to-checkout.md)
- [Updates initCheckout to be synchronous](https://docs.stripe.com/changelog/clover/2025-09-30/update-init-checkout-synchronous.md)
- [Adds support for collecting business and individual names in Checkout Sessions](https://docs.stripe.com/changelog/clover/2025-09-30/checkout-name-collection.md)
- [Adds the ability to exclude payment methods from Checkout Sessions and Payment Intents](https://docs.stripe.com/changelog/clover/2025-09-30/exclude-payment-methods-checkout-sessions.md)
- [Adds support for setting the capture method for specific payment methods with the Checkout Sessions API](https://docs.stripe.com/changelog/clover/2025-09-30/checkout-capture-method-per-payment-method.md)
- [Adds support for configuring branding settings for Checkout Sessions](https://docs.stripe.com/changelog/clover/2025-09-30/checkout-sessions-branding-settings.md)
- [Enables specifying units of measurement for Products](https://docs.stripe.com/changelog/clover/2025-09-30/product-data-unit-label.md)
