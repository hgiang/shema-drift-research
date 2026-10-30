# Adds WeChat Pay payment method options to the Checkout Session response

## What’s new

The [wechat_pay](https://docs.stripe.com/api/checkout/sessions/object.md?api-version=2026-06-24.dahlia#checkout_session_object-payment_method_options-wechat_pay) property is now included in the [payment_method_options](https://docs.stripe.com/api/checkout/sessions/object.md?api-version=2026-06-24.dahlia#checkout_session_object-payment_method_options) hash returned when you [retrieve a Checkout Session](https://docs.stripe.com/api/checkout/sessions/retrieve.md?api-version=2026-06-24.dahlia). This property exposes the [WeChat Pay](https://docs.stripe.com/payments/wechat-pay.md) configuration for the session, including the following properties:

- [app_id](https://docs.stripe.com/api/checkout/sessions/object.md?api-version=2026-06-24.dahlia#checkout_session_object-payment_method_options-wechat_pay-app_id): The app ID registered with WeChat Pay.
- [client](https://docs.stripe.com/api/checkout/sessions/object.md?api-version=2026-06-24.dahlia#checkout_session_object-payment_method_options-wechat_pay-client): The client type used for the payment.
- [setup_future_usage](https://docs.stripe.com/api/checkout/sessions/object.md?api-version=2026-06-24.dahlia#checkout_session_object-payment_method_options-wechat_pay-setup_future_usage): Indicates whether the payment method is saved for future use.

Previously, these parameters were available when [creating a Checkout Session](https://docs.stripe.com/api/checkout/sessions/create.md?api-version=2026-06-24.dahlia) but were absent from the retrieve response.

## Impact

You can now read [WeChat Pay](https://docs.stripe.com/payments/wechat-pay.md) payment method configuration directly from the Checkout Session object when you retrieve a session. If your integration retrieves session details to inspect or display payment method options, the `wechat_pay` property is now available in the response.

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `wechat_pay` | Added | [Checkout.Session.payment_method_options](/api/checkout/sessions/object?api-version=2026-06-24.dahlia#checkout_session_object-payment_method_options) |

#### Ruby

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `wechat_pay` | Added | [Checkout::Session::PaymentMethodOption](/api/checkout/sessions/object?api-version=2026-06-24.dahlia#checkout_session_object-payment_method_options) |

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `wechat_pay` | Added | [Checkout.Session.PaymentMethodOption](/api/checkout/sessions/object?api-version=2026-06-24.dahlia#checkout_session_object-payment_method_options) |

#### PHP

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `wechat_pay` | Added | [Checkout.Session.payment_method_options](/api/checkout/sessions/object?api-version=2026-06-24.dahlia#checkout_session_object-payment_method_options) |

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `wechatPay` | Added | [checkout.Session.payment_method_options](/api/checkout/sessions/object?api-version=2026-06-24.dahlia#checkout_session_object-payment_method_options) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `wechat_pay` | Added | [Checkout.Session.payment_method_options](/api/checkout/sessions/object?api-version=2026-06-24.dahlia#checkout_session_object-payment_method_options) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `WeChatPay` | Added | [CheckoutSessionPaymentMethodOptions](/api/checkout/sessions/object?api-version=2026-06-24.dahlia#checkout_session_object-payment_method_options) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `WechatPay` | Added | [Checkout.Session.PaymentMethodOptions](/api/checkout/sessions/object?api-version=2026-06-24.dahlia#checkout_session_object-payment_method_options) |

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

- [Makes billing cycle anchor configuration available for Checkout Sessions in subscription mode](https://docs.stripe.com/changelog/dahlia/2026-06-24/checkout-sessions-billing-cycle-anchor-config.md)
