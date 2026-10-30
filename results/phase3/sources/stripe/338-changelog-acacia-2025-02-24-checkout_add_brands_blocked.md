# Adds support for blocking specific card brands in Checkout Sessions

## What’s new

Adds the [payment_method_options.card.restrictions.brands_blocked](https://docs.stripe.com/api/checkout/sessions/create.md?api-version=2025-02-24.acacia#create_checkout_session-payment_method_options-card-restrictions-brands_blocked) parameter to the [Create a Checkout Session](https://docs.stripe.com/api/checkout/sessions/create.md?api-version=2025-02-24.acacia) method. You can pass in an array of card brands that you don’t want the Checkout Session to allow.

## Impact

For details about how to filter card brands in Checkout, see the [guide on customising Checkout behaviour](https://docs.stripe.com/payments/checkout/customization/card-brands.md).

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `restrictions` | Added | [Checkout.Session#create.payment_method_options.card](/api/checkout/sessions/create?api-version=2025-02-24.acacia#create_checkout_session-payment_method_options-card), [Checkout.Session.payment_method_options.card](/api/checkout/sessions/object?api-version=2025-02-24.acacia#checkout_session_object-payment_method_options-card) |

#### Ruby

This change doesn’t affect the Ruby SDK.

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `restrictions` | Added | [stripe.checkout.Session.CreateParamsPaymentMethodOptionsCard](/api/checkout/sessions/create?api-version=2025-02-24.acacia#create_checkout_session-payment_method_options-card), [stripe.checkout.Session.PaymentMethodOptions.Card](/api/checkout/sessions/object?api-version=2025-02-24.acacia#checkout_session_object-payment_method_options-card) |

#### PHP

This change doesn’t affect the PHP SDK.

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `restrictions` | Added | [Checkout.Session.payment_method_options.card](/api/checkout/sessions/object?api-version=2025-02-24.acacia#checkout_session_object-payment_method_options-card), [checkout.SessionCreateParams.payment_method_options.card](/api/checkout/sessions/create?api-version=2025-02-24.acacia#create_checkout_session-payment_method_options-card) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `restrictions` | Added | [Checkout.Session.payment_method_options.card](/api/checkout/sessions/object?api-version=2025-02-24.acacia#checkout_session_object-payment_method_options-card), [Checkout.SessionCreateParams.payment_method_options.card](/api/checkout/sessions/create?api-version=2025-02-24.acacia#create_checkout_session-payment_method_options-card) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `Restrictions` | Added | [CheckoutSessionPaymentMethodOptionsCardParams](/api/checkout/sessions/object?api-version=2025-02-24.acacia#checkout_session_object-payment_method_options-card), [CheckoutSessionPaymentMethodOptionsCard](/api/checkout/sessions/object?api-version=2025-02-24.acacia#checkout_session_object-payment_method_options-card) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `Restrictions` | Added | [CheckoutSessionPaymentMethodOptionsCardOptions](/api/checkout/sessions/object?api-version=2025-02-24.acacia#checkout_session_object-payment_method_options-card), [CheckoutSessionPaymentMethodOptionsCard](/api/checkout/sessions/object?api-version=2025-02-24.acacia#checkout_session_object-payment_method_options-card) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2025-02-24.acacia`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to [v13.5.0](https://github.com/stripe/stripe-ruby/releases/tag/v13.5.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to [v11.6.0](https://github.com/stripe/stripe-python/releases/tag/v11.6.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to [v16.6.0](https://github.com/stripe/stripe-php/releases/tag/v16.6.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to [v28.4.0](https://github.com/stripe/stripe-java/releases/tag/v28.4.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to [v17.7.0](https://github.com/stripe/stripe-node/releases/tag/v17.7.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to [v81.4.0](https://github.com/stripe/stripe-go/releases/tag/v81.4.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to [v47.4.0](https://github.com/stripe/stripe-dotnet/releases/tag/v47.4.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

## Related changes

- [Checkout Sessions now group customer information in one field](https://docs.stripe.com/changelog/acacia/2025-02-24/checkout-sessions-collected-info.md)
