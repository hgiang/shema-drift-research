# Adds buyer ID support for Bizum payments

## What’s new

Adds the [buyer_id](https://docs.stripe.com/api/payment_methods/object.md?api-version=2026-06-24.dahlia#payment_method_object-bizum-buyer_id) property to the [bizum](https://docs.stripe.com/api/payment_methods/object.md?api-version=2026-06-24.dahlia#payment_method_object-bizum) hash on the [Charge](https://docs.stripe.com/api/charges/object.md?api-version=2026-06-24.dahlia), [PaymentAttemptRecord](https://docs.stripe.com/api/payment-attempt-record/object.md?api-version=2026-06-24.dahlia), [PaymentRecord](https://docs.stripe.com/api/payment-record/object.md?api-version=2026-06-24.dahlia), and [PaymentMethod](https://docs.stripe.com/api/payment_methods/object.md?api-version=2026-06-24.dahlia) objects. The `buyer_id` is a unique identifier that [Bizum](https://docs.stripe.com/payments/bizum.md), a mobile payment method in Spain, assigns to the buyer. Stripe returns it on successful payments.

## Impact

You can now read the `buyer_id` property from the `bizum` hash on the Charge, PaymentAttemptRecord, PaymentRecord, and PaymentMethod objects to uniquely identify the buyer in a Bizum transaction. Use this identifier to support fraud detection and risk management workflows in your integration.

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `buyer_id` | Added | [Charge.payment_method_details.bizum](/api/charges/object?api-version=2026-06-24.dahlia#charge_object-payment_method_details-bizum), [PaymentAttemptRecord.payment_method_details.bizum](/api/payment-attempt-record/object?api-version=2026-06-24.dahlia#payment_attempt_record_object-payment_method_details-bizum), [PaymentRecord.payment_method_details.bizum](/api/payment-record/object?api-version=2026-06-24.dahlia#payment_record_object-payment_method_details-bizum), [ConfirmationToken.payment_method_preview.bizum](/api/confirmation_tokens/object?api-version=2026-06-24.dahlia#confirmation_token_object-payment_method_preview-bizum), [PaymentMethod.bizum](/api/payment_methods/object?api-version=2026-06-24.dahlia#payment_method_object-bizum) |

#### Ruby

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `buyer_id` | Added | [Charge::PaymentMethodDetail::Bizum](/api/charges/object?api-version=2026-06-24.dahlia#charge_object-payment_method_details-bizum), [PaymentAttemptRecord::PaymentMethodDetail::Bizum](/api/payment-attempt-record/object?api-version=2026-06-24.dahlia#payment_attempt_record_object-payment_method_details-bizum), [PaymentRecord::PaymentMethodDetail::Bizum](/api/payment-record/object?api-version=2026-06-24.dahlia#payment_record_object-payment_method_details-bizum), [ConfirmationToken::PaymentMethodPreview::Bizum](/api/confirmation_tokens/object?api-version=2026-06-24.dahlia#confirmation_token_object-payment_method_preview-bizum), [PaymentMethod::Bizum](/api/payment_methods/object?api-version=2026-06-24.dahlia#payment_method_object-bizum) |

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `buyer_id` | Added | [Charge.PaymentMethodDetail.Bizum](/api/charges/object?api-version=2026-06-24.dahlia#charge_object-payment_method_details-bizum), [PaymentAttemptRecord.PaymentMethodDetail.Bizum](/api/payment-attempt-record/object?api-version=2026-06-24.dahlia#payment_attempt_record_object-payment_method_details-bizum), [PaymentRecord.PaymentMethodDetail.Bizum](/api/payment-record/object?api-version=2026-06-24.dahlia#payment_record_object-payment_method_details-bizum), [ConfirmationToken.PaymentMethodPreview.Bizum](/api/confirmation_tokens/object?api-version=2026-06-24.dahlia#confirmation_token_object-payment_method_preview-bizum), [PaymentMethod.Bizum](/api/payment_methods/object?api-version=2026-06-24.dahlia#payment_method_object-bizum) |

#### PHP

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `buyer_id` | Added | [Charge.payment_method_details.bizum](/api/charges/object?api-version=2026-06-24.dahlia#charge_object-payment_method_details-bizum), [PaymentAttemptRecord.payment_method_details.bizum](/api/payment-attempt-record/object?api-version=2026-06-24.dahlia#payment_attempt_record_object-payment_method_details-bizum), [PaymentRecord.payment_method_details.bizum](/api/payment-record/object?api-version=2026-06-24.dahlia#payment_record_object-payment_method_details-bizum), [ConfirmationToken.payment_method_preview.bizum](/api/confirmation_tokens/object?api-version=2026-06-24.dahlia#confirmation_token_object-payment_method_preview-bizum), [PaymentMethod.bizum](/api/payment_methods/object?api-version=2026-06-24.dahlia#payment_method_object-bizum) |

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `buyerId` | Added | [Charge.payment_method_details.bizum](/api/charges/object?api-version=2026-06-24.dahlia#charge_object-payment_method_details-bizum), [PaymentAttemptRecord.payment_method_details.bizum](/api/payment-attempt-record/object?api-version=2026-06-24.dahlia#payment_attempt_record_object-payment_method_details-bizum), [PaymentRecord.payment_method_details.bizum](/api/payment-record/object?api-version=2026-06-24.dahlia#payment_record_object-payment_method_details-bizum), [ConfirmationToken.payment_method_preview.bizum](/api/confirmation_tokens/object?api-version=2026-06-24.dahlia#confirmation_token_object-payment_method_preview-bizum), [PaymentMethod.bizum](/api/payment_methods/object?api-version=2026-06-24.dahlia#payment_method_object-bizum) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `buyer_id` | Added | [Charge.payment_method_details.bizum](/api/charges/object?api-version=2026-06-24.dahlia#charge_object-payment_method_details-bizum), [PaymentAttemptRecord.payment_method_details.bizum](/api/payment-attempt-record/object?api-version=2026-06-24.dahlia#payment_attempt_record_object-payment_method_details-bizum), [PaymentRecord.payment_method_details.bizum](/api/payment-record/object?api-version=2026-06-24.dahlia#payment_record_object-payment_method_details-bizum), [ConfirmationToken.payment_method_preview.bizum](/api/confirmation_tokens/object?api-version=2026-06-24.dahlia#confirmation_token_object-payment_method_preview-bizum), [PaymentMethod.bizum](/api/payment_methods/object?api-version=2026-06-24.dahlia#payment_method_object-bizum) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `BuyerID` | Added | [ChargePaymentMethodDetailsBizum](/api/charges/object?api-version=2026-06-24.dahlia#charge_object-payment_method_details-bizum), [PaymentAttemptRecordPaymentMethodDetailsBizum](/api/payment-attempt-record/object?api-version=2026-06-24.dahlia#payment_attempt_record_object-payment_method_details-bizum), [PaymentRecordPaymentMethodDetailsBizum](/api/payment-record/object?api-version=2026-06-24.dahlia#payment_record_object-payment_method_details-bizum), [ConfirmationTokenPaymentMethodPreviewBizum](/api/confirmation_tokens/object?api-version=2026-06-24.dahlia#confirmation_token_object-payment_method_preview-bizum), [PaymentMethodBizum](/api/payment_methods/object?api-version=2026-06-24.dahlia#payment_method_object-bizum) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `BuyerId` | Added | [Charge.PaymentMethodDetails.Bizum](/api/charges/object?api-version=2026-06-24.dahlia#charge_object-payment_method_details-bizum), [PaymentAttemptRecord.PaymentMethodDetails.Bizum](/api/payment-attempt-record/object?api-version=2026-06-24.dahlia#payment_attempt_record_object-payment_method_details-bizum), [PaymentRecord.PaymentMethodDetails.Bizum](/api/payment-record/object?api-version=2026-06-24.dahlia#payment_record_object-payment_method_details-bizum), [ConfirmationToken.PaymentMethodPreview.Bizum](/api/confirmation_tokens/object?api-version=2026-06-24.dahlia#confirmation_token_object-payment_method_preview-bizum), [PaymentMethod.Bizum](/api/payment_methods/object?api-version=2026-06-24.dahlia#payment_method_object-bizum) |

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

- [Enables manual capture for Sunbit payments](https://docs.stripe.com/changelog/dahlia/2026-06-24/enables-manual-capture-for-sunbit-payments.md)
- [Adds buyer ID support for BLIK payments](https://docs.stripe.com/changelog/dahlia/2026-06-24/blik-payments-buyer-id.md)
- [Adds a fingerprint to Pix payment method details](https://docs.stripe.com/changelog/dahlia/2026-06-24/pix-fingerprint-payment-method-details.md)
- [Adds transaction link ID to card payment method details for Mastercard and Maestro transactions](https://docs.stripe.com/changelog/dahlia/2026-06-24/card-payment-method-details-transaction-link-id.md)
- [Adds payment method options for Sunbit in Checkout Sessions](https://docs.stripe.com/changelog/dahlia/2026-06-24/sunbit-checkout-pmo.md)
- [Adds support for the Sui network and USDsui token for crypto payments](https://docs.stripe.com/changelog/dahlia/2026-06-24/sui-network-and-usdsui-token-support.md)
- [Adds support for Mastercard compliance disputes](https://docs.stripe.com/changelog/dahlia/2026-06-24/mastercard-compliance-disputes.md)
- [Adds support for recurring payments with Satispay](https://docs.stripe.com/changelog/dahlia/2026-06-24/satispay-recurring-payments.md)
