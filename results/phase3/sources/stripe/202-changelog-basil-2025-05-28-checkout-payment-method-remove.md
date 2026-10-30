# Adds option to Checkout Sessions to let customers remove saved payment methods

## What’s new

Adds a new parameter called `saved_payment_method_options[payment_method_remove]` to the [Create a Checkout Session method](https://docs.stripe.com/api/checkout/sessions/create.md?api-version=2025-05-28.basil) that lets customers remove saved payment methods.

## Impact

To let your customers remove a saved payment method, use [payment_method_remove](https://docs.stripe.com/api/checkout/sessions/create.md?api-version=2025-05-28.basil#create_checkout_session-saved_payment_method_options-payment_method_remove) when you create a Checkout Session.

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `payment_method_remove` | Added | [Checkout.Session#create.saved_payment_method_options](/api/checkout/sessions/create?api-version=2025-05-28.basil#create_checkout_session-saved_payment_method_options-payment_method_remove) |

#### Ruby

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `payment_method_remove` | Added | [CheckoutSession::CreateParams::SavedPaymentMethodOption](/api/checkout/sessions/create?api-version=2025-05-28.basil#create_checkout_session-saved_payment_method_options-payment_method_remove) |

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `payment_method_remove` | Added | [checkout.Session.CreateParamsSavedPaymentMethodOption](/api/checkout/sessions/create?api-version=2025-05-28.basil#create_checkout_session-saved_payment_method_options-payment_method_remove) |

#### PHP

This change doesn’t affect the PHP SDK.

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `paymentMethodRemove` | Added | [checkout.SessionCreateParams.saved_payment_method_options](/api/checkout/sessions/create?api-version=2025-05-28.basil#create_checkout_session-saved_payment_method_options-payment_method_remove) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `payment_method_remove` | Added | [Checkout.SessionCreateParams.saved_payment_method_options](/api/checkout/sessions/create?api-version=2025-05-28.basil#create_checkout_session-saved_payment_method_options-payment_method_remove) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `PaymentMethodRemove` | Added | [CheckoutSessionSavedPaymentMethodOptionsParams](/api/checkout/sessions/create?api-version=2025-05-28.basil#create_checkout_session-saved_payment_method_options-payment_method_remove) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `PaymentMethodRemove` | Added | [CheckoutSessionSavedPaymentMethodOptionsOptions](/api/checkout/sessions/create?api-version=2025-05-28.basil#create_checkout_session-saved_payment_method_options-payment_method_remove) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2025-05-28.basil`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to [v15.2.0](https://github.com/stripe/stripe-ruby/releases/tag/v15.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to [v12.2.0](https://github.com/stripe/stripe-python/releases/tag/v12.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to [v17.3.0](https://github.com/stripe/stripe-php/releases/tag/v17.3.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to [v29.2.0](https://github.com/stripe/stripe-java/releases/tag/v29.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to [v18.2.0](https://github.com/stripe/stripe-node/releases/tag/v18.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to [v82.2.0](https://github.com/stripe/stripe-go/releases/tag/v82.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to [v48.2.0](https://github.com/stripe/stripe-dotnet/releases/tag/v48.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

## Related changes

- [Adds South Korean payment methods to the Payment Method Configurations API](https://docs.stripe.com/changelog/basil/2025-05-28/korea-payment-method-configuration.md)
- [Adds account capability for the Pix payment method for US-based sellers](https://docs.stripe.com/changelog/basil/2025-05-28/adds-pix-capability-for-us-sellers.md)
- [Adds capture method option to Satispay payments](https://docs.stripe.com/changelog/basil/2025-05-28/satispay-capture-method-option.md)
- [Adds support for setting up future usage of Naver Pay in Checkout Sessions](https://docs.stripe.com/changelog/basil/2025-05-28/naver-pay-update.md)
- [Adds support for WeChat Pay for Setup Intents](https://docs.stripe.com/changelog/basil/2025-05-28/setup-intents-wechat-pay.md)
- [Adds network decline codes for PayPal refunds](https://docs.stripe.com/changelog/basil/2025-05-28/paypal_refund_network_decline_code.md)
