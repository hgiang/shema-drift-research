# Use configurable capture methods and set up future usage for South Korean payment methods

## What’s new

The following South Korean payment methods now support setting the [capture_method](https://docs.stripe.com/api/checkout/sessions/create.md?api-version=2024-11-20.acacia#create_checkout_session-payment_intent_data-capture_method) to `manual`, which overrides the configuration for the *Session* (A Checkout Session represents your customer's session as they pay for one-time purchases or subscriptions through Checkout. After a successful payment, the Checkout Session contains a reference to the Customer, and either the successful PaymentIntent or an active Subscription):

- [South Korean cards](https://docs.stripe.com/payments/kr-card/accept-a-payment.md)
- [Naver Pay](https://docs.stripe.com/payments/naver-pay/accept-a-payment.md)
- [Kakao Pay](https://docs.stripe.com/payments/kakao-pay/accept-a-payment.md)
- [Samsung Pay](https://docs.stripe.com/payments/samsung-pay/accept-a-payment.md)
- [PAYCO](https://docs.stripe.com/payments/payco/accept-a-payment.md)

The following South Korean payment methods now support [setup_future_usage](https://docs.stripe.com/api/checkout/sessions/create.md?api-version=2024-11-20.acacia#create_checkout_session-payment_intent_data-setup_future_usage), which you set when you create a Session:

- [South Korean cards](https://docs.stripe.com/payments/kr-card/accept-a-payment.md)
- [Naver Pay](https://docs.stripe.com/payments/naver-pay/accept-a-payment.md)
- [Kakao Pay](https://docs.stripe.com/payments/kakao-pay/accept-a-payment.md)

## Impact

You can now override the default automatic capture of a payment transaction using South Korean payment methods when you create a Checkout Session. Set [capture_method](https://docs.stripe.com/api/checkout/sessions/create.md?api-version=2024-11-20.acacia#create_checkout_session-payment_intent_data-capture_method) to `manual` on the `payment_method_options` parameter for the specific payment method to [place a hold on the payment method](https://docs.stripe.com/payments/place-a-hold-on-a-payment-method.md).

- [South Korean cards](https://docs.stripe.com/api/checkout/sessions/create.md?api-version=2024-11-20.acacia#create_checkout_session-payment_method_options-kr_card)
- [Naver Pay](https://docs.stripe.com/api/checkout/sessions/create.md?api-version=2024-11-20.acacia#create_checkout_session-payment_method_options-naver_pay)
- [Kakao Pay](https://docs.stripe.com/api/checkout/sessions/create.md?api-version=2024-11-20.acacia#create_checkout_session-payment_method_options-kakao_pay)
- [Samsung Pay](https://docs.stripe.com/api/checkout/sessions/create.md?api-version=2024-11-20.acacia#create_checkout_session-payment_method_options-samsung_pay)
- [PAYCO](https://docs.stripe.com/api/checkout/sessions/create.md?api-version=2024-11-20.acacia#create_checkout_session-payment_method_options-payco)

You can now specify whether to [save South Korean payment method details](https://docs.stripe.com/payments/save-during-payment.md) during payment when you [create a Checkout Session](https://docs.stripe.com/api/checkout/sessions/create.md?api-version=2024-11-20.acacia). For example, set [setup_future_usage](https://docs.stripe.com/api/checkout/sessions/create.md?api-version=2024-11-20.acacia#create_checkout_session-payment_intent_data-setup_future_usage) to `off_session` in the `payment_method_options` parameter for the specific payment method to enable charging the customer at a later time, such as for a cancellation fee.

- [South Korean cards](https://docs.stripe.com/api/checkout/sessions/create.md?api-version=2024-11-20.acacia#create_checkout_session-payment_method_options-kr_card)
- [Naver Pay](https://docs.stripe.com/api/checkout/sessions/create.md?api-version=2024-11-20.acacia#create_checkout_session-payment_method_options-naver_pay)
- [Kakao Pay](https://docs.stripe.com/api/checkout/sessions/create.md?api-version=2024-11-20.acacia#create_checkout_session-payment_method_options-kakao_pay)

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `capture_method` | Added | [Checkout.Session#create.payment_method_options.kakao_pay](/api/checkout/sessions/create?api-version=2024-11-20.acacia#create_checkout_session-payment_method_options-kakao_pay), [Checkout.Session#create.payment_method_options.kr_card](/api/checkout/sessions/create?api-version=2024-11-20.acacia#create_checkout_session-payment_method_options-kr_card), [Checkout.Session#create.payment_method_options.naver_pay](/api/checkout/sessions/create?api-version=2024-11-20.acacia#create_checkout_session-payment_method_options-naver_pay), [Checkout.Session#create.payment_method_options.payco](/api/checkout/sessions/create?api-version=2024-11-20.acacia#create_checkout_session-payment_method_options-payco), [Checkout.Session#create.payment_method_options.samsung_pay](/api/checkout/sessions/create?api-version=2024-11-20.acacia#create_checkout_session-payment_method_options-samsung_pay) |

#### Ruby

This change doesn’t affect the Ruby SDK.

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `capture_method` | Added | [stripe.checkout.Session.CreateParamsPaymentMethodOptionsKakaoPay](/api/checkout/sessions/create?api-version=2024-11-20.acacia#create_checkout_session-payment_method_options-kakao_pay), [stripe.checkout.Session.CreateParamsPaymentMethodOptionsKrCard](/api/checkout/sessions/create?api-version=2024-11-20.acacia#create_checkout_session-payment_method_options-kr_card), [stripe.checkout.Session.CreateParamsPaymentMethodOptionsNaverPay](/api/checkout/sessions/create?api-version=2024-11-20.acacia#create_checkout_session-payment_method_options-naver_pay), [stripe.checkout.Session.CreateParamsPaymentMethodOptionsPayco](/api/checkout/sessions/create?api-version=2024-11-20.acacia#create_checkout_session-payment_method_options-payco), [stripe.checkout.Session.CreateParamsPaymentMethodOptionsSamsungPay](/api/checkout/sessions/create?api-version=2024-11-20.acacia#create_checkout_session-payment_method_options-samsung_pay) |

#### PHP

This change doesn’t affect the PHP SDK.

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `capture_method` | Added | [checkout.SessionCreateParams.payment_method_options.kakao_pay](/api/checkout/sessions/create?api-version=2024-11-20.acacia#create_checkout_session-payment_method_options-kakao_pay), [checkout.SessionCreateParams.payment_method_options.kr_card](/api/checkout/sessions/create?api-version=2024-11-20.acacia#create_checkout_session-payment_method_options-kr_card), [checkout.SessionCreateParams.payment_method_options.naver_pay](/api/checkout/sessions/create?api-version=2024-11-20.acacia#create_checkout_session-payment_method_options-naver_pay), [checkout.SessionCreateParams.payment_method_options.payco](/api/checkout/sessions/create?api-version=2024-11-20.acacia#create_checkout_session-payment_method_options-payco), [checkout.SessionCreateParams.payment_method_options.samsung_pay](/api/checkout/sessions/create?api-version=2024-11-20.acacia#create_checkout_session-payment_method_options-samsung_pay) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `capture_method` | Added | [Checkout.SessionCreateParams.payment_method_options.kakao_pay](/api/checkout/sessions/create?api-version=2024-11-20.acacia#create_checkout_session-payment_method_options-kakao_pay), [Checkout.SessionCreateParams.payment_method_options.kr_card](/api/checkout/sessions/create?api-version=2024-11-20.acacia#create_checkout_session-payment_method_options-kr_card), [Checkout.SessionCreateParams.payment_method_options.naver_pay](/api/checkout/sessions/create?api-version=2024-11-20.acacia#create_checkout_session-payment_method_options-naver_pay), [Checkout.SessionCreateParams.payment_method_options.payco](/api/checkout/sessions/create?api-version=2024-11-20.acacia#create_checkout_session-payment_method_options-payco), [Checkout.SessionCreateParams.payment_method_options.samsung_pay](/api/checkout/sessions/create?api-version=2024-11-20.acacia#create_checkout_session-payment_method_options-samsung_pay) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `CaptureMethod` | Added | [CheckoutSessionPaymentMethodOptionsKakaoPayParams](/api/checkout/sessions/create?api-version=2024-11-20.acacia#create_checkout_session-payment_method_options-kakao_pay), [CheckoutSessionPaymentMethodOptionsKrCardParams](/api/checkout/sessions/create?api-version=2024-11-20.acacia#create_checkout_session-payment_method_options-kr_card), [CheckoutSessionPaymentMethodOptionsNaverPayParams](/api/checkout/sessions/create?api-version=2024-11-20.acacia#create_checkout_session-payment_method_options-naver_pay), [CheckoutSessionPaymentMethodOptionsPaycoParams](/api/checkout/sessions/create?api-version=2024-11-20.acacia#create_checkout_session-payment_method_options-payco), [CheckoutSessionPaymentMethodOptionsSamsungPayParams](/api/checkout/sessions/create?api-version=2024-11-20.acacia#create_checkout_session-payment_method_options-samsung_pay) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `CaptureMethod` | Added | [CheckoutSessionPaymentMethodOptionsKakaoPayOptions](/api/checkout/sessions/create?api-version=2024-11-20.acacia#create_checkout_session-payment_method_options-kakao_pay), [CheckoutSessionPaymentMethodOptionsKrCardOptions](/api/checkout/sessions/create?api-version=2024-11-20.acacia#create_checkout_session-payment_method_options-kr_card), [CheckoutSessionPaymentMethodOptionsNaverPayOptions](/api/checkout/sessions/create?api-version=2024-11-20.acacia#create_checkout_session-payment_method_options-naver_pay), [CheckoutSessionPaymentMethodOptionsPaycoOptions](/api/checkout/sessions/create?api-version=2024-11-20.acacia#create_checkout_session-payment_method_options-payco), [CheckoutSessionPaymentMethodOptionsSamsungPayOptions](/api/checkout/sessions/create?api-version=2024-11-20.acacia#create_checkout_session-payment_method_options-samsung_pay) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2024-11-20.acacia`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to [v13.2.0](https://github.com/stripe/stripe-ruby/releases/tag/v13.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to [v11.3.0](https://github.com/stripe/stripe-python/releases/tag/v11.3.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to [v16.3.0](https://github.com/stripe/stripe-php/releases/tag/v16.3.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to [v28.1.0](https://github.com/stripe/stripe-java/releases/tag/v28.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to [v17.4.0](https://github.com/stripe/stripe-node/releases/tag/v17.4.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to [v81.1.0](https://github.com/stripe/stripe-go/releases/tag/v81.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to [v47.1.0](https://github.com/stripe/stripe-dotnet/releases/tag/v47.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

## Related changes

- [Adds network decline code field for Swish and BLIK refunds](https://docs.stripe.com/changelog/acacia/2024-11-20/refunds-network-decline-code.md)
- [Adds support for SEPA Direct Debit and Bacs Direct Debit mandate reference prefixes in Checkout Sessions](https://docs.stripe.com/changelog/acacia/2024-11-20/checkout-sessions-sepa-debit-bacs-debit-mandate-options.md)
- [Specifying an originating payment method for Inbound Transfers is now optional](https://docs.stripe.com/changelog/acacia/2024-11-20/inbound-transfers-optional-pm.md)
