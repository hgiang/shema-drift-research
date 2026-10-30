# Adds a Charge Transaction Id for several payment methods

## What’s new

Adds the `transaction_id` field to the [Charge](https://docs.stripe.com/api/charge/object.md?api-version=2025-08-27.basil) object under `payment_method_details` for the following payment methods:

- [Alma](https://docs.stripe.com/payments/alma.md)
- [Amazon Pay](https://docs.stripe.com/payments/amazon-pay.md)
- [Billie](https://docs.stripe.com/payments/billie.md)
- [Kakao Pay](https://docs.stripe.com/payments/kakao-pay/accept-a-payment.md)
- [Korean Cards](https://docs.stripe.com/payments/kr-card/accept-a-payment.md)
- [Naver Pay](https://docs.stripe.com/payments/naver-pay/accept-a-payment.md)
- [Payco](https://docs.stripe.com/payments/payco/accept-a-payment.md)
- [Revolut Pay](https://docs.stripe.com/payments/revolut-pay.md)
- [Samsung Pay](https://docs.stripe.com/payments/samsung-pay/accept-a-payment.md)
- [Satispay](https://docs.stripe.com/payments/satispay.md)

## Impact

Payment methods use their own transaction IDs to identify payments. These IDs might be shown to customers, and customers can refer to them when communicating with you. You can now get these transaction IDs within the [Charge](https://docs.stripe.com/api/charge/object.md?api-version=2025-08-27.basil) object to identify the corresponding Charge.

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `transaction_id` | Added | [Charge.payment_method_details.alma](/api/charges/object?api-version=2025-08-27.basil#charge_object-payment_method_details-alma), [Charge.payment_method_details.amazon_pay](/api/charges/object?api-version=2025-08-27.basil#charge_object-payment_method_details-amazon_pay), [Charge.payment_method_details.billie](/api/charges/object?api-version=2025-08-27.basil#charge_object-payment_method_details-billie), [Charge.payment_method_details.kakao_pay](/api/charges/object?api-version=2025-08-27.basil#charge_object-payment_method_details-kakao_pay), [Charge.payment_method_details.kr_card](/api/charges/object?api-version=2025-08-27.basil#charge_object-payment_method_details-kr_card), [Charge.payment_method_details.naver_pay](/api/charges/object?api-version=2025-08-27.basil#charge_object-payment_method_details-naver_pay), [Charge.payment_method_details.payco](/api/charges/object?api-version=2025-08-27.basil#charge_object-payment_method_details-payco), [Charge.payment_method_details.revolut_pay](/api/charges/object?api-version=2025-08-27.basil#charge_object-payment_method_details-revolut_pay), [Charge.payment_method_details.samsung_pay](/api/charges/object?api-version=2025-08-27.basil#charge_object-payment_method_details-samsung_pay), [Charge.payment_method_details.satispay](/api/charges/object?api-version=2025-08-27.basil#charge_object-payment_method_details-satispay) |

#### Ruby

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `transaction_id` | Added | [Charge::PaymentMethodDetail::Alma](/api/charges/object?api-version=2025-08-27.basil#charge_object-payment_method_details-alma), [Charge::PaymentMethodDetail::AmazonPay](/api/charges/object?api-version=2025-08-27.basil#charge_object-payment_method_details-amazon_pay), [Charge::PaymentMethodDetail::Billie](/api/charges/object?api-version=2025-08-27.basil#charge_object-payment_method_details-billie), [Charge::PaymentMethodDetail::KakaoPay](/api/charges/object?api-version=2025-08-27.basil#charge_object-payment_method_details-kakao_pay), [Charge::PaymentMethodDetail::KrCard](/api/charges/object?api-version=2025-08-27.basil#charge_object-payment_method_details-kr_card), [Charge::PaymentMethodDetail::NaverPay](/api/charges/object?api-version=2025-08-27.basil#charge_object-payment_method_details-naver_pay), [Charge::PaymentMethodDetail::Payco](/api/charges/object?api-version=2025-08-27.basil#charge_object-payment_method_details-payco), [Charge::PaymentMethodDetail::RevolutPay](/api/charges/object?api-version=2025-08-27.basil#charge_object-payment_method_details-revolut_pay), [Charge::PaymentMethodDetail::SamsungPay](/api/charges/object?api-version=2025-08-27.basil#charge_object-payment_method_details-samsung_pay), [Charge::PaymentMethodDetail::Satispay](/api/charges/object?api-version=2025-08-27.basil#charge_object-payment_method_details-satispay) |

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `transaction_id` | Added | [Charge.PaymentMethodDetail.Alma](/api/charges/object?api-version=2025-08-27.basil#charge_object-payment_method_details-alma), [Charge.PaymentMethodDetail.AmazonPay](/api/charges/object?api-version=2025-08-27.basil#charge_object-payment_method_details-amazon_pay), [Charge.PaymentMethodDetail.Billie](/api/charges/object?api-version=2025-08-27.basil#charge_object-payment_method_details-billie), [Charge.PaymentMethodDetail.KakaoPay](/api/charges/object?api-version=2025-08-27.basil#charge_object-payment_method_details-kakao_pay), [Charge.PaymentMethodDetail.KrCard](/api/charges/object?api-version=2025-08-27.basil#charge_object-payment_method_details-kr_card), [Charge.PaymentMethodDetail.NaverPay](/api/charges/object?api-version=2025-08-27.basil#charge_object-payment_method_details-naver_pay), [Charge.PaymentMethodDetail.Payco](/api/charges/object?api-version=2025-08-27.basil#charge_object-payment_method_details-payco), [Charge.PaymentMethodDetail.RevolutPay](/api/charges/object?api-version=2025-08-27.basil#charge_object-payment_method_details-revolut_pay), [Charge.PaymentMethodDetail.SamsungPay](/api/charges/object?api-version=2025-08-27.basil#charge_object-payment_method_details-samsung_pay), [Charge.PaymentMethodDetail.Satispay](/api/charges/object?api-version=2025-08-27.basil#charge_object-payment_method_details-satispay) |

#### PHP

This change doesn’t affect the PHP SDK.

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `transactionId` | Added | [Charge.payment_method_details.alma](/api/charges/object?api-version=2025-08-27.basil#charge_object-payment_method_details-alma), [Charge.payment_method_details.amazon_pay](/api/charges/object?api-version=2025-08-27.basil#charge_object-payment_method_details-amazon_pay), [Charge.payment_method_details.billie](/api/charges/object?api-version=2025-08-27.basil#charge_object-payment_method_details-billie), [Charge.payment_method_details.kakao_pay](/api/charges/object?api-version=2025-08-27.basil#charge_object-payment_method_details-kakao_pay), [Charge.payment_method_details.kr_card](/api/charges/object?api-version=2025-08-27.basil#charge_object-payment_method_details-kr_card), [Charge.payment_method_details.naver_pay](/api/charges/object?api-version=2025-08-27.basil#charge_object-payment_method_details-naver_pay), [Charge.payment_method_details.payco](/api/charges/object?api-version=2025-08-27.basil#charge_object-payment_method_details-payco), [Charge.payment_method_details.revolut_pay](/api/charges/object?api-version=2025-08-27.basil#charge_object-payment_method_details-revolut_pay), [Charge.payment_method_details.samsung_pay](/api/charges/object?api-version=2025-08-27.basil#charge_object-payment_method_details-samsung_pay), [Charge.payment_method_details.satispay](/api/charges/object?api-version=2025-08-27.basil#charge_object-payment_method_details-satispay) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `transaction_id` | Added | [Charge.payment_method_details.alma](/api/charges/object?api-version=2025-08-27.basil#charge_object-payment_method_details-alma), [Charge.payment_method_details.amazon_pay](/api/charges/object?api-version=2025-08-27.basil#charge_object-payment_method_details-amazon_pay), [Charge.payment_method_details.billie](/api/charges/object?api-version=2025-08-27.basil#charge_object-payment_method_details-billie), [Charge.payment_method_details.kakao_pay](/api/charges/object?api-version=2025-08-27.basil#charge_object-payment_method_details-kakao_pay), [Charge.payment_method_details.kr_card](/api/charges/object?api-version=2025-08-27.basil#charge_object-payment_method_details-kr_card), [Charge.payment_method_details.naver_pay](/api/charges/object?api-version=2025-08-27.basil#charge_object-payment_method_details-naver_pay), [Charge.payment_method_details.payco](/api/charges/object?api-version=2025-08-27.basil#charge_object-payment_method_details-payco), [Charge.payment_method_details.revolut_pay](/api/charges/object?api-version=2025-08-27.basil#charge_object-payment_method_details-revolut_pay), [Charge.payment_method_details.samsung_pay](/api/charges/object?api-version=2025-08-27.basil#charge_object-payment_method_details-samsung_pay), [Charge.payment_method_details.satispay](/api/charges/object?api-version=2025-08-27.basil#charge_object-payment_method_details-satispay) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `TransactionID` | Added | [ChargePaymentMethodDetailsAlma](/api/charges/object?api-version=2025-08-27.basil#charge_object-payment_method_details-alma), [ChargePaymentMethodDetailsAmazonPay](/api/charges/object?api-version=2025-08-27.basil#charge_object-payment_method_details-amazon_pay), [ChargePaymentMethodDetailsBillie](/api/charges/object?api-version=2025-08-27.basil#charge_object-payment_method_details-billie), [ChargePaymentMethodDetailsKakaoPay](/api/charges/object?api-version=2025-08-27.basil#charge_object-payment_method_details-kakao_pay), [ChargePaymentMethodDetailsKrCard](/api/charges/object?api-version=2025-08-27.basil#charge_object-payment_method_details-kr_card), [ChargePaymentMethodDetailsNaverPay](/api/charges/object?api-version=2025-08-27.basil#charge_object-payment_method_details-naver_pay), [ChargePaymentMethodDetailsPayco](/api/charges/object?api-version=2025-08-27.basil#charge_object-payment_method_details-payco), [ChargePaymentMethodDetailsRevolutPay](/api/charges/object?api-version=2025-08-27.basil#charge_object-payment_method_details-revolut_pay), [ChargePaymentMethodDetailsSamsungPay](/api/charges/object?api-version=2025-08-27.basil#charge_object-payment_method_details-samsung_pay), [ChargePaymentMethodDetailsSatispay](/api/charges/object?api-version=2025-08-27.basil#charge_object-payment_method_details-satispay) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `TransactionId` | Added | [Charge.PaymentMethodDetails.Alma](/api/charges/object?api-version=2025-08-27.basil#charge_object-payment_method_details-alma), [Charge.PaymentMethodDetails.AmazonPay](/api/charges/object?api-version=2025-08-27.basil#charge_object-payment_method_details-amazon_pay), [Charge.PaymentMethodDetails.Billie](/api/charges/object?api-version=2025-08-27.basil#charge_object-payment_method_details-billie), [Charge.PaymentMethodDetails.KakaoPay](/api/charges/object?api-version=2025-08-27.basil#charge_object-payment_method_details-kakao_pay), [Charge.PaymentMethodDetails.KrCard](/api/charges/object?api-version=2025-08-27.basil#charge_object-payment_method_details-kr_card), [Charge.PaymentMethodDetails.NaverPay](/api/charges/object?api-version=2025-08-27.basil#charge_object-payment_method_details-naver_pay), [Charge.PaymentMethodDetails.Payco](/api/charges/object?api-version=2025-08-27.basil#charge_object-payment_method_details-payco), [Charge.PaymentMethodDetails.RevolutPay](/api/charges/object?api-version=2025-08-27.basil#charge_object-payment_method_details-revolut_pay), [Charge.PaymentMethodDetails.SamsungPay](/api/charges/object?api-version=2025-08-27.basil#charge_object-payment_method_details-samsung_pay), [Charge.PaymentMethodDetails.Satispay](/api/charges/object?api-version=2025-08-27.basil#charge_object-payment_method_details-satispay) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2025-08-27.basil`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to [v15.5.0](https://github.com/stripe/stripe-ruby/releases/tag/v15.5.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to [v12.5.0](https://github.com/stripe/stripe-python/releases/tag/v12.5.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to [v17.6.0](https://github.com/stripe/stripe-php/releases/tag/v17.6.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to [v29.5.0](https://github.com/stripe/stripe-java/releases/tag/v29.5.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to [v18.5.0](https://github.com/stripe/stripe-node/releases/tag/v18.5.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to [v82.5.0](https://github.com/stripe/stripe-go/releases/tag/v82.5.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to [v48.5.0](https://github.com/stripe/stripe-dotnet/releases/tag/v48.5.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

## Related changes

- [Adds PayPay settings to the Account object](https://docs.stripe.com/changelog/basil/2025-08-27/add_paypay_payments_settings.md)
- [Adds the number of instalments for Alma payments to Charge objects](https://docs.stripe.com/changelog/basil/2025-08-27/alma-installments.md)
- [Adds support to include the IOF tax in the amount for Pix payments](https://docs.stripe.com/changelog/basil/2025-08-27/pix-payments-iof-tax.md)
- [Adds excluded payment method types to the Payment Intents API](https://docs.stripe.com/changelog/basil/2025-08-27/cs_add_excluded_payment_method_types_pi.md)
