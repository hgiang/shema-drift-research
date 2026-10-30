# Adds QR code support for Klarna payments with Terminal readers

## What’s new

Adds support for QR code-based [Klarna](https://docs.stripe.com/payments/klarna.md) payments on [Terminal](https://docs.stripe.com/terminal.md) smart readers. When you process a Klarna payment on a Terminal reader, Stripe generates a QR code that customers scan to complete their payment using the Klarna mobile app.

This update adds the [klarna_display_qr_code](https://docs.stripe.com/api/payment_intents/object.md?api-version=2026-04-22.dahlia#payment_intent_object-next_action-klarna_display_qr_code) next action type for the [Payment Intents API](https://docs.stripe.com/api/payment_intents.md?api-version=2026-04-22.dahlia). When a Klarna payment requires customer interaction on Terminal, the PaymentIntent returns this next action with:

- QR code data and image URLs (PNG and SVG formats) for display on the Terminal reader
- An expiry timestamp for the QR code

The Klarna [payment method details](https://docs.stripe.com/api/charges/object.md?api-version=2026-04-22.dahlia#charge_object-payment_method_details-klarna) hash now also includes the [reader](https://docs.stripe.com/api/terminal/readers/object.md?api-version=2026-04-22.dahlia#terminal_reader_object-id) and [location](https://docs.stripe.com/api/terminal/locations/object.md?api-version=2026-04-22.dahlia#terminal_location_object-id) fields when the payment originates from a Terminal reader. This helps provide more context about the location of the in-person transaction.

## Impact

You can accept Klarna payments in person using Terminal smart readers with QR code functionality. When customers choose Klarna as their payment method on your Terminal reader, they receive a QR code to scan with their mobile device, allowing them to complete the payment flow through the Klarna app while remaining in your physical location. This feature requires the Terminal reader to support QR code display capabilities. If QR code generation isn’t available, the payment flow falls back to the standard redirect URL method.

To use this feature, ensure your Terminal integration handles the `klarna_display_qr_code` next action type and can display the provided QR code images on compatible Terminal readers.

## Changes

#### REST API

| Parameters | Change | Resources or endpoints |
| --- | --- | --- |
| `location`, `reader` | Added | [PaymentAttemptRecord.payment_method_details.klarna](/api/payment-attempt-record/object?api-version=2026-04-22.dahlia#payment_attempt_record_object-payment_method_details-klarna), [Charge.payment_method_details.klarna](/api/charges/object?api-version=2026-04-22.dahlia#charge_object-payment_method_details-klarna), [PaymentRecord.payment_method_details.klarna](/api/payment-record/object?api-version=2026-04-22.dahlia#payment_record_object-payment_method_details-klarna) |
| `klarna_display_qr_code` | Added | [PaymentIntent.next_action](/api/payment_intents/object?api-version=2026-04-22.dahlia#payment_intent_object-next_action) |

#### Ruby

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `location`, `reader` | Added | [PaymentRecord::PaymentMethodDetail::Klarna](/api/payment-record/object?api-version=2026-04-22.dahlia#payment_record_object-payment_method_details-klarna), [Charge::PaymentMethodDetail::Klarna](/api/charges/object?api-version=2026-04-22.dahlia#charge_object-payment_method_details-klarna), [PaymentAttemptRecord::PaymentMethodDetail::Klarna](/api/payment-attempt-record/object?api-version=2026-04-22.dahlia#payment_attempt_record_object-payment_method_details-klarna) |
| `klarna_display_qr_code` | Added | [PaymentIntent::NextAction](/api/payment_intents/object?api-version=2026-04-22.dahlia#payment_intent_object-next_action) |

#### Python

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `klarna_display_qr_code` | Added | [PaymentIntent.NextAction](/api/payment_intents/object?api-version=2026-04-22.dahlia#payment_intent_object-next_action) |
| `location`, `reader` | Added | [PaymentRecord.PaymentMethodDetail.Klarna](/api/payment-record/object?api-version=2026-04-22.dahlia#payment_record_object-payment_method_details-klarna), [PaymentAttemptRecord.PaymentMethodDetail.Klarna](/api/payment-attempt-record/object?api-version=2026-04-22.dahlia#payment_attempt_record_object-payment_method_details-klarna), [Charge.PaymentMethodDetail.Klarna](/api/charges/object?api-version=2026-04-22.dahlia#charge_object-payment_method_details-klarna) |

#### PHP

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `location`, `reader` | Added | [PaymentAttemptRecord.payment_method_details.klarna](/api/payment-attempt-record/object?api-version=2026-04-22.dahlia#payment_attempt_record_object-payment_method_details-klarna), [Charge.payment_method_details.klarna](/api/charges/object?api-version=2026-04-22.dahlia#charge_object-payment_method_details-klarna), [PaymentRecord.payment_method_details.klarna](/api/payment-record/object?api-version=2026-04-22.dahlia#payment_record_object-payment_method_details-klarna) |
| `klarna_display_qr_code` | Added | [PaymentIntent.next_action](/api/payment_intents/object?api-version=2026-04-22.dahlia#payment_intent_object-next_action) |

#### Java

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `location`, `reader` | Added | [Charge.payment_method_details.klarna](/api/charges/object?api-version=2026-04-22.dahlia#charge_object-payment_method_details-klarna), [PaymentRecord.payment_method_details.klarna](/api/payment-record/object?api-version=2026-04-22.dahlia#payment_record_object-payment_method_details-klarna), [PaymentAttemptRecord.payment_method_details.klarna](/api/payment-attempt-record/object?api-version=2026-04-22.dahlia#payment_attempt_record_object-payment_method_details-klarna) |
| `klarnaDisplayQrCode` | Added | [PaymentIntent.next_action](/api/payment_intents/object?api-version=2026-04-22.dahlia#payment_intent_object-next_action) |

#### Node.js

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `klarna_display_qr_code` | Added | [PaymentIntent.next_action](/api/payment_intents/object?api-version=2026-04-22.dahlia#payment_intent_object-next_action) |
| `location`, `reader` | Added | [PaymentRecord.payment_method_details.klarna](/api/payment-record/object?api-version=2026-04-22.dahlia#payment_record_object-payment_method_details-klarna), [Charge.payment_method_details.klarna](/api/charges/object?api-version=2026-04-22.dahlia#charge_object-payment_method_details-klarna), [PaymentAttemptRecord.payment_method_details.klarna](/api/payment-attempt-record/object?api-version=2026-04-22.dahlia#payment_attempt_record_object-payment_method_details-klarna) |

#### Go

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `Location`, `Reader` | Added | [PaymentAttemptRecordPaymentMethodDetailsKlarna](/api/payment-attempt-record/object?api-version=2026-04-22.dahlia#payment_attempt_record_object-payment_method_details-klarna), [ChargePaymentMethodDetailsKlarna](/api/charges/object?api-version=2026-04-22.dahlia#charge_object-payment_method_details-klarna), [PaymentRecordPaymentMethodDetailsKlarna](/api/payment-record/object?api-version=2026-04-22.dahlia#payment_record_object-payment_method_details-klarna) |
| `KlarnaDisplayQRCode` | Added | [PaymentIntentNextAction](/api/payment_intents/object?api-version=2026-04-22.dahlia#payment_intent_object-next_action) |

#### .NET

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `Location`, `Reader` | Added | [Charge.PaymentMethodDetails.Klarna](/api/charges/object?api-version=2026-04-22.dahlia#charge_object-payment_method_details-klarna), [PaymentRecord.PaymentMethodDetails.Klarna](/api/payment-record/object?api-version=2026-04-22.dahlia#payment_record_object-payment_method_details-klarna), [PaymentAttemptRecord.PaymentMethodDetails.Klarna](/api/payment-attempt-record/object?api-version=2026-04-22.dahlia#payment_attempt_record_object-payment_method_details-klarna) |
| `KlarnaDisplayQrCode` | Added | [PaymentIntent.NextAction](/api/payment_intents/object?api-version=2026-04-22.dahlia#payment_intent_object-next_action) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2026-04-22.dahlia`
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

- [Adds support for Sunbit, a Buy Now, Pay Later payment method](https://docs.stripe.com/changelog/dahlia/2026-04-22/sunbit-buy-now-pay-later-support.md)
- [Adds support for Pix recurring payments](https://docs.stripe.com/changelog/dahlia/2026-04-22/pix-recurring-payments-support.md)
- [Adds the moto property to Setup Attempt payment method details for cards](https://docs.stripe.com/changelog/dahlia/2026-04-22/setup-attempt-payment-method-details-for-cards-moto.md)
- [Adds support for Managed Payments, Stripe’s merchant of record solution](https://docs.stripe.com/changelog/dahlia/2026-04-22/managed-payments.md)
