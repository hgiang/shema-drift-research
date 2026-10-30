# Adds support for saving and reusing Naver Pay payment methods

## What’s new

You can save Naver Pay payment methods and use them for future payments.

## Impact

You can now use Naver Pay with:

- [SetupIntent](https://docs.stripe.com/api/setup_intents.md?api-version=2025-03-31.basil): Save payment method details without making a payment and make payments in the future.
- [setup_future_usage](https://docs.stripe.com/api/payment_intents/object.md?api-version=2025-03-31.basil#payment_intent_object-setup_future_usage): Save payment details during payment and make additional payments in the future.

Use the `buyer_id` parameter in [PaymentMethod.naver_pay](https://docs.stripe.com/api/payment_methods/object.md?api-version=2025-03-31.basil#payment_method_object-naver_pay-buyer_id) and [SetupAttempt.payment_method_details.naver_pay](https://docs.stripe.com/api/setup_attempts/object.md?api-version=2025-03-31.basil#setup_attempt_object-payment_method_details-naver_pay-buyer_id) to check if two Naver Pay accounts are the same.

## Changes

#### REST API

| Parameters | Change | Resources or endpoints |
| --- | --- | --- |
| `buyer_id` | Added | `ConfirmationToken.payment_method_preview.naver_pay`, `PaymentMethod.naver_pay` |
| `naver_pay` | Added | [Mandate.payment_method_details](/api/mandates/object?api-version=2025-03-31.basil#mandate_object-payment_method_details), [SetupAttempt.payment_method_details](/api/setup_attempts/object?api-version=2025-03-31.basil#setup_attempt_object-payment_method_details) |
| `setup_future_usage` | Added | [PaymentIntent#confirm.payment_method_options.naver_pay](/api/payment_intents/confirm?api-version=2025-03-31.basil#confirm_payment_intent-payment_method_options-naver_pay), `PaymentIntent#create.payment_method_options.naver_pay`, `PaymentIntent#update.payment_method_options.naver_pay`, `PaymentIntent.payment_method_options.naver_pay` |

#### Ruby

This change doesn’t affect the Ruby SDK.

#### Python

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `buyer_id` | Added | `ConfirmationToken.PaymentMethodPreview.NaverPay`, `CustomerPaymentMethod.NaverPay`, `PaymentMethod.NaverPay` |
| `naver_pay` | Added | `Mandate.PaymentMethodDetail`, `SetupAttempt.PaymentMethodDetail` |
| `setup_future_usage` | Added | [PaymentIntent.ConfirmParamsPaymentMethodOptionNaverPay](/api/payment_intents/confirm?api-version=2025-03-31.basil#confirm_payment_intent-payment_method_options-naver_pay), `PaymentIntent.CreateParamsPaymentMethodOptionNaverPay`, `PaymentIntent.PaymentMethodOption.NaverPay`, `PaymentIntent.UpdateParamsPaymentMethodOptionNaverPay` |

#### PHP

This change doesn’t affect the PHP SDK.

#### Java

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `buyerId` | Added | `ConfirmationToken.payment_method_preview.naver_pay`, `CustomerPaymentMethod.naver_pay`, `PaymentMethod.naver_pay` |
| `naverPay` | Added | [Mandate.payment_method_details](/api/mandates/object?api-version=2025-03-31.basil#mandate_object-payment_method_details), [SetupAttempt.payment_method_details](/api/setup_attempts/object?api-version=2025-03-31.basil#setup_attempt_object-payment_method_details) |
| `setupFutureUsage` | Added | `PaymentIntent.payment_method_options.naver_pay`, [PaymentIntentConfirmParams.payment_method_options.naver_pay](/api/payment_intents/confirm?api-version=2025-03-31.basil#confirm_payment_intent-payment_method_options-naver_pay), `PaymentIntentCreateParams.payment_method_options.naver_pay`, `PaymentIntentUpdateParams.payment_method_options.naver_pay` |

#### Node.js

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `buyer_id` | Added | `ConfirmationToken.payment_method_preview.naver_pay`, `CustomerPaymentMethod.naver_pay`, `PaymentMethod.naver_pay` |
| `naver_pay` | Added | [Mandate.payment_method_details](/api/mandates/object?api-version=2025-03-31.basil#mandate_object-payment_method_details), [SetupAttempt.payment_method_details](/api/setup_attempts/object?api-version=2025-03-31.basil#setup_attempt_object-payment_method_details) |
| `setup_future_usage` | Added | `PaymentIntent.payment_method_options.naver_pay`, [PaymentIntentConfirmParams.payment_method_options.naver_pay](/api/payment_intents/confirm?api-version=2025-03-31.basil#confirm_payment_intent-payment_method_options-naver_pay), `PaymentIntentCreateParams.payment_method_options.naver_pay`, `PaymentIntentUpdateParams.payment_method_options.naver_pay` |

#### Go

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `BuyerID` | Added | `ConfirmationTokenPaymentMethodPreviewNaverPay`, `PaymentMethodNaverPay` |
| `NaverPay` | Added | [MandatePaymentMethodDetails](/api/mandates/object?api-version=2025-03-31.basil#mandate_object-payment_method_details), [SetupAttemptPaymentMethodDetails](/api/setup_attempts/object?api-version=2025-03-31.basil#setup_attempt_object-payment_method_details) |
| `SetupFutureUsage` | Added | [PaymentIntentConfirmPaymentMethodOptionsNaverPayParams](/api/payment_intents/confirm?api-version=2025-03-31.basil#confirm_payment_intent-payment_method_options-naver_pay), `PaymentIntentPaymentMethodOptionsNaverPayParams`, `PaymentIntentPaymentMethodOptionsNaverPay` |

#### .NET

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `BuyerId` | Added | `ConfirmationTokenPaymentMethodPreviewNaverPay`, `CustomerPaymentMethodNaverPay`, `PaymentMethodNaverPay` |
| `NaverPay` | Added | [MandatePaymentMethodDetails](/api/mandates/object?api-version=2025-03-31.basil#mandate_object-payment_method_details), [SetupAttemptPaymentMethodDetails](/api/setup_attempts/object?api-version=2025-03-31.basil#setup_attempt_object-payment_method_details) |
| `SetupFutureUsage` | Added | `PaymentIntentPaymentMethodOptionsNaverPayOptions`, `PaymentIntentPaymentMethodOptionsNaverPay` |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2025-03-31.basil`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to [v15.0.0](https://github.com/stripe/stripe-ruby/releases/tag/v15.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to [v12.0.0](https://github.com/stripe/stripe-python/releases/tag/v12.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to [v17.0.0](https://github.com/stripe/stripe-php/releases/tag/v17.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to [v29.0.0](https://github.com/stripe/stripe-java/releases/tag/v29.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to [v18.0.0](https://github.com/stripe/stripe-node/releases/tag/v18.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to [v82.0.0](https://github.com/stripe/stripe-go/releases/tag/v82.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to [v48.0.0](https://github.com/stripe/stripe-dotnet/releases/tag/v48.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

## Related changes

- [Updates the Vault and Forward API to return a 402 status code for upstream request timeouts](https://docs.stripe.com/changelog/basil/2025-03-31/vault-forward-api-returns-402.md)
- [Removes manual capture method for Interac cards](https://docs.stripe.com/changelog/basil/2025-03-31/deprecate-interac-present-manual-capture-method.md)
- [Payment Methods won’t allow modifying fields for Naver Pay after the object is first created](https://docs.stripe.com/changelog/basil/2025-03-31/naver-pay-payment-method.md)
- [Partially capturing or cancelling payments no longer creates a Refund](https://docs.stripe.com/changelog/basil/2025-03-31/remove-refund-from-partial-capture-and-payment-cancellation-flow.md)
- [Adds support for Klarna in the hosted invoice page](https://docs.stripe.com/changelog/basil/2025-03-31/klarna-send-invoice.md)
- [Adds ability to configure saved payment methods for one-time payments on the hosted invoice page](https://docs.stripe.com/changelog/basil/2025-03-31/hosted-payment-method-save.md)
- [Adds support for the Billie local payment method](https://docs.stripe.com/changelog/basil/2025-03-31/add-billie.md)
- [Adds support for the Satispay local payment method](https://docs.stripe.com/changelog/basil/2025-03-31/satispay-lpm.md)
- [Makes the client parameter optional for WeChat Pay until confirmation](https://docs.stripe.com/changelog/basil/2025-03-31/lient-param-optional-wechatpay-before-confirmation.md)
- [Adds support for the New Zealand BECS Direct Debit local payment method](https://docs.stripe.com/changelog/basil/2025-03-31/nz-bank-account.md)
