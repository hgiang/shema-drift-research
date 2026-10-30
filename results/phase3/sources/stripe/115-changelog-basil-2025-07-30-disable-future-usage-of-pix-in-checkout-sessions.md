# Adds support for disabling future usage in Checkout sessions

## What’s new

You can now set [setup_future_usage](https://docs.stripe.com/api/checkout/sessions/object.md?api-version=2025-07-30.basil#checkout_session_object-payment_method_options-pix-setup_future_usage) to `none` for Pix payment method options when creating a [Checkout Session](https://docs.stripe.com/api/checkout/sessions/object.md?api-version=2025-07-30.basil).

## Impact

This update lets you specify that you don’t intend to reuse a Pix payment method for future payments when creating a Checkout Session. By setting `setup_future_usage = none`, you ensure that the provided payment method is used only for the current transaction.

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `setup_future_usage` | Added | [Checkout.Session#create.payment_method_options.pix](/api/checkout/sessions/create?api-version=2025-07-30.basil#create_checkout_session-payment_method_options), [Checkout.Session.payment_method_options.pix](/api/checkout/sessions/object?api-version=2025-07-30.basil#checkout_session_object-payment_method_options) |

#### Ruby

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `setup_future_usage` | Added | [Checkout::Session::CreateParams::PaymentMethodOption::Pix](/api/checkout/sessions/create?api-version=2025-07-30.basil#create_checkout_session-payment_method_options), [Checkout::Session::PaymentMethodOption::Pix](/api/checkout/sessions/object?api-version=2025-07-30.basil#checkout_session_object-payment_method_options) |

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `setup_future_usage` | Added | [Checkout.Session.PaymentMethodOption.Pix](/api/checkout/sessions/object?api-version=2025-07-30.basil#checkout_session_object-payment_method_options), [checkout.Session.CreateParamsPaymentMethodOptionPix](/api/checkout/sessions/create?api-version=2025-07-30.basil#create_checkout_session-payment_method_options) |

#### PHP

This change doesn’t affect the PHP SDK.

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `setupFutureUsage` | Added | [checkout.Session.payment_method_options.pix](/api/checkout/sessions/object?api-version=2025-07-30.basil#checkout_session_object-payment_method_options), [checkout.SessionCreateParams.payment_method_options.pix](/api/checkout/sessions/create?api-version=2025-07-30.basil#create_checkout_session-payment_method_options) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `setup_future_usage` | Added | [Checkout.Session.payment_method_options.pix](/api/checkout/sessions/object?api-version=2025-07-30.basil#checkout_session_object-payment_method_options), [Checkout.SessionCreateParams.payment_method_options.pix](/api/checkout/sessions/create?api-version=2025-07-30.basil#create_checkout_session-payment_method_options) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `SetupFutureUsage` | Added | [CheckoutSessionPaymentMethodOptionsPix](/api/checkout/sessions/object?api-version=2025-07-30.basil#checkout_session_object-payment_method_options), [CheckoutSessionPaymentMethodOptionsPixParams](/api/checkout/sessions/object?api-version=2025-07-30.basil#checkout_session_object-payment_method_options) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `SetupFutureUsage` | Added | [Checkout.Session.PaymentMethodOptions.Pix](/api/checkout/sessions/object?api-version=2025-07-30.basil#checkout_session_object-payment_method_options), [CheckoutSessionPaymentMethodOptionsPixOptions](/api/checkout/sessions/object?api-version=2025-07-30.basil#checkout_session_object-payment_method_options) |

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
- [Adds support for Invoice Rendering Templates on Checkout and Payment Links](https://docs.stripe.com/changelog/basil/2025-07-30/checkout-payment-link-invoice-rendering-templates.md)
- [Adds support for the NZ BECS Direct Debit local payment method in Checkout and Payment Links](https://docs.stripe.com/changelog/basil/2025-07-30/nz-bank-account-checkout-payment-links.md)
