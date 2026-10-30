# Adds payment method options for Sunbit in Checkout Sessions

## What’s new

Adds support for [payment_method_options.sunbit](https://docs.stripe.com/api/checkout/sessions/create.md?api-version=2026-06-24.dahlia#create_checkout_session-payment_method_options-sunbit) on the [Checkout Session](https://docs.stripe.com/api/checkout/sessions.md?api-version=2026-06-24.dahlia) object. You can now configure the following options when using [Sunbit](https://docs.stripe.com/payments/sunbit.md) as a payment method in a Checkout Session:

- [capture_method](https://docs.stripe.com/api/checkout/sessions/create.md?api-version=2026-06-24.dahlia#create_checkout_session-payment_method_options-sunbit-capture_method): Controls when funds are captured from the customer’s account. Set to `manual` to place a hold on funds and capture them later.
- [setup_future_usage](https://docs.stripe.com/api/checkout/sessions/create.md?api-version=2026-06-24.dahlia#create_checkout_session-payment_method_options-sunbit-setup_future_usage): Indicates whether you intend to make future payments with the payment method collected in this session. Set to `none` to indicate no future usage.

These options are available on both the `POST /v1/checkout/sessions` request and the `GET /v1/checkout/sessions/:id` response.

## Impact

You can now set `capture_method` and `setup_future_usage` at the `payment_method_options.sunbit` level to override the top-level values set on the Checkout Session. You can also use `manual` capture with Sunbit payments in Checkout Sessions, giving you greater control over when funds are captured after authorisation. To use manual capture, set `capture_method` to `manual` when you [create a Checkout Session](https://docs.stripe.com/api/checkout/sessions/create.md?api-version=2026-06-24.dahlia).

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `sunbit` | Added | [Checkout.Session#create.payment_method_options](/api/checkout/sessions/create?api-version=2026-06-24.dahlia#create_checkout_session-payment_method_options), [Checkout.Session.payment_method_options](/api/checkout/sessions/object?api-version=2026-06-24.dahlia#checkout_session_object-payment_method_options) |

#### Ruby

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `sunbit` | Added | [Checkout::Session::PaymentMethodOption](/api/checkout/sessions/object?api-version=2026-06-24.dahlia#checkout_session_object-payment_method_options), [Checkout::SessionCreateParams::PaymentMethodOption](/api/checkout/sessions/create?api-version=2026-06-24.dahlia#create_checkout_session-payment_method_options) |

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `sunbit` | Added | [Checkout.Session.PaymentMethodOption](/api/checkout/sessions/object?api-version=2026-06-24.dahlia#checkout_session_object-payment_method_options), [checkout.SessionCreateParamsPaymentMethodOption](/api/checkout/sessions/create?api-version=2026-06-24.dahlia#create_checkout_session-payment_method_options) |

#### PHP

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `sunbit` | Added | [Checkout.Session.payment_method_options](/api/checkout/sessions/object?api-version=2026-06-24.dahlia#checkout_session_object-payment_method_options), [Checkout\Session.create().$params.payment_method_option](/api/checkout/sessions/create?api-version=2026-06-24.dahlia#create_checkout_session-payment_method_options) |

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `sunbit` | Added | [checkout.Session.payment_method_options](/api/checkout/sessions/object?api-version=2026-06-24.dahlia#checkout_session_object-payment_method_options), [checkout.SessionCreateParams.payment_method_options](/api/checkout/sessions/create?api-version=2026-06-24.dahlia#create_checkout_session-payment_method_options) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `sunbit` | Added | [Checkout.Session.payment_method_options](/api/checkout/sessions/object?api-version=2026-06-24.dahlia#checkout_session_object-payment_method_options), [Checkout.SessionCreateParams.payment_method_options](/api/checkout/sessions/create?api-version=2026-06-24.dahlia#create_checkout_session-payment_method_options) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `Sunbit` | Added | [CheckoutSessionPaymentMethodOptions](/api/checkout/sessions/object?api-version=2026-06-24.dahlia#checkout_session_object-payment_method_options), [CheckoutSessionPaymentMethodOptionsParams](/api/checkout/sessions/create?api-version=2026-06-24.dahlia#create_checkout_session-payment_method_options) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `Sunbit` | Added | [Checkout.Session.PaymentMethodOptions](/api/checkout/sessions/object?api-version=2026-06-24.dahlia#checkout_session_object-payment_method_options), [CheckoutSessionPaymentMethodOptionsOptions](/api/checkout/sessions/create?api-version=2026-06-24.dahlia#create_checkout_session-payment_method_options) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2026-06-24.dahlia`
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

- [Adds buyer ID support for Bizum payments](https://docs.stripe.com/changelog/dahlia/2026-06-24/bizum-payments-buyer-id.md)
- [Enables manual capture for Sunbit payments](https://docs.stripe.com/changelog/dahlia/2026-06-24/enables-manual-capture-for-sunbit-payments.md)
- [Adds buyer ID support for BLIK payments](https://docs.stripe.com/changelog/dahlia/2026-06-24/blik-payments-buyer-id.md)
- [Adds a fingerprint to Pix payment method details](https://docs.stripe.com/changelog/dahlia/2026-06-24/pix-fingerprint-payment-method-details.md)
- [Adds transaction link ID to card payment method details for Mastercard and Maestro transactions](https://docs.stripe.com/changelog/dahlia/2026-06-24/card-payment-method-details-transaction-link-id.md)
- [Adds support for the Sui network and USDsui token for crypto payments](https://docs.stripe.com/changelog/dahlia/2026-06-24/sui-network-and-usdsui-token-support.md)
- [Adds support for Mastercard compliance disputes](https://docs.stripe.com/changelog/dahlia/2026-06-24/mastercard-compliance-disputes.md)
- [Adds support for recurring payments with Satispay](https://docs.stripe.com/changelog/dahlia/2026-06-24/satispay-recurring-payments.md)
