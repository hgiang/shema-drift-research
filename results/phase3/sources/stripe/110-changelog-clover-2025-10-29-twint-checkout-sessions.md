# Adds TWINT payment method options to Checkout Sessions

## What’s new

Adds the [payment_method_options.twint.setup_future_usage](https://docs.stripe.com/api/checkout/sessions/create.md?api-version=2025-10-29.clover#create_checkout_session-payment_method_options-twint-setup_future_usage) parameter to [Checkout Sessions](https://docs.stripe.com/api/checkout/sessions.md?api-version=2025-10-29.clover). This parameter accepts the `none` value to indicate that you don’t intend to reuse the TWINT payment method.

## Impact

This change enables you to indicate that you don’t intend to reuse the TWINT payment method and want to override the behaviour defined in the top-level [setup_future_usage](https://docs.stripe.com/api/checkout/sessions/create.md?api-version=2025-10-29.clover#create_checkout_session-payment_method_options-twint-setup_future_usage) parameter for this payment method.

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `twint` | Added | [Checkout.Session#create.payment_method_options](/api/checkout/sessions/create?api-version=2025-10-29.clover#create_checkout_session-payment_method_options), [Checkout.Session.payment_method_options](/api/checkout/sessions/object?api-version=2025-10-29.clover#checkout_session_object-payment_method_options) |

#### Ruby

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `twint` | Added | [Checkout::Session::CreateParams::PaymentMethodOption](/api/checkout/sessions/create?api-version=2025-10-29.clover#create_checkout_session-payment_method_options), [Checkout::Session::PaymentMethodOption](/api/checkout/sessions/object?api-version=2025-10-29.clover#checkout_session_object-payment_method_options) |

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `twint` | Added | [Checkout.Session.PaymentMethodOption](/api/checkout/sessions/object?api-version=2025-10-29.clover#checkout_session_object-payment_method_options), [checkout.Session.CreateParamsPaymentMethodOption](/api/checkout/sessions/create?api-version=2025-10-29.clover#create_checkout_session-payment_method_options) |

#### PHP

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `twint` | Added | [Checkout.Session.payment_method_options](/api/checkout/sessions/object?api-version=2025-10-29.clover#checkout_session_object-payment_method_options), [Checkout\Session.create().$params.payment_method_option](/api/checkout/sessions/create?api-version=2025-10-29.clover#create_checkout_session-payment_method_options) |

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `twint` | Added | [checkout.Session.payment_method_options](/api/checkout/sessions/object?api-version=2025-10-29.clover#checkout_session_object-payment_method_options), [checkout.SessionCreateParams.payment_method_options](/api/checkout/sessions/create?api-version=2025-10-29.clover#create_checkout_session-payment_method_options) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `twint` | Added | [Checkout.Session.payment_method_options](/api/checkout/sessions/object?api-version=2025-10-29.clover#checkout_session_object-payment_method_options), [Checkout.SessionCreateParams.payment_method_options](/api/checkout/sessions/create?api-version=2025-10-29.clover#create_checkout_session-payment_method_options) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `TWINT` | Added | [CheckoutSessionPaymentMethodOptions](/api/checkout/sessions/object?api-version=2025-10-29.clover#checkout_session_object-payment_method_options), [CheckoutSessionPaymentMethodOptionsParams](/api/checkout/sessions/create?api-version=2025-10-29.clover#create_checkout_session-payment_method_options) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `Twint` | Added | [Checkout.Session.PaymentMethodOptions](/api/checkout/sessions/object?api-version=2025-10-29.clover#checkout_session_object-payment_method_options), [CheckoutSessionPaymentMethodOptionsOptions](/api/checkout/sessions/create?api-version=2025-10-29.clover#create_checkout_session-payment_method_options) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2025-10-29.clover`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to [v17.1.0](https://github.com/stripe/stripe-ruby/releases/tag/v17.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to [v13.1.0](https://github.com/stripe/stripe-python/releases/tag/v13.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to [v18.1.0](https://github.com/stripe/stripe-php/releases/tag/v18.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to [v30.1.0](https://github.com/stripe/stripe-java/releases/tag/v30.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to [v19.2.0](https://github.com/stripe/stripe-node/releases/tag/v19.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to [v83.1.0](https://github.com/stripe/stripe-go/releases/tag/v83.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to [v49.1.0](https://github.com/stripe/stripe-dotnet/releases/tag/v49.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

## Related changes

- [Adds MB WAY to payment method configurations](https://docs.stripe.com/changelog/clover/2025-10-29/mb-way-payment-method-configuration.md)
- [Adds support for specifying payment method configurations to the customer portal](https://docs.stripe.com/changelog/clover/2025-10-29/customer-portal-payment-method-configurations.md)
- [Adds MB WAY payment method to Payment Links and Checkout Sessions](https://docs.stripe.com/changelog/clover/2025-10-29/mb-way-payment-link-checkout-sessions.md)
- [Adds the ability to exclude payment methods when using Setup Intents](https://docs.stripe.com/changelog/clover/2025-10-29/exclude-payment-methods-setup-intents.md)
- [Adds Klarna reference parameters for line items in Payment Intents](https://docs.stripe.com/changelog/clover/2025-10-29/klarna-line-item-reference.md)
- [Adds a subscription reference to Klarna line items in Payment Intents](https://docs.stripe.com/changelog/clover/2025-10-29/klarna-items-payment-intents.md)
- [Adds support for custom payment methods](https://docs.stripe.com/changelog/clover/2025-10-29/custom-payment-methods.md)
