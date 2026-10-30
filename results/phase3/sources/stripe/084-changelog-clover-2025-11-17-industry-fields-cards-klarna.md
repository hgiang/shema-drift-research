# Adds industry-specific transaction details and purchase data for cards and Klarna

## What’s new

Adds fields for [card](https://docs.stripe.com/payments/cards.md) and [Klarna](https://docs.stripe.com/payments/klarna.md) payments to specify [industry-specific transaction details](https://docs.stripe.com/industry-metadata.md):

- **Car rentals:** [payment_details.car_rental_data](https://docs.stripe.com/api/payment_intents/create.md?api-version=2025-11-17.preview#create_payment_intent-payment_details-car_rental_data)
- **Lodging:** [payment_details.lodging_data](https://docs.stripe.com/api/payment_intents/create.md?api-version=2025-11-17.preview#create_payment_intent-payment_details-lodging_data)
- **Flights:** [payment_details.flight_data](https://docs.stripe.com/api/payment_intents/create.md?api-version=2025-11-17.preview#create_payment_intent-payment_details-flight_data)

You can provide [additional transaction details](https://docs.stripe.com/payments/klarna/supplementary-purchase-data.md) for Klarna payments [payment_method_options.klarna.supplementary_purchase_data](https://docs.stripe.com/api/payment_intents/create.md?api-version=2025-11-17.preview#create_payment_intent-payment_method_options-klarna-supplementary_purchase_data) to specify train, bus, ferry trips, round-trips, insurance, vouchers, marketplace sellers and event reservations.

When this functionality was first released with the [2025-11-17.preview](https://docs.stripe.com/changelog.md?channel=preview#2025-11-17.preview) API version, data passed to the `payment_details.car_rental_data`, `payment_details.lodging_data` and `payment_details.flight_data` parameters wasn’t saved to [PaymentIntent](https://docs.stripe.com/api/payment_intents.md?api-version=2025-11-17.preview) objects. We resolved this issue, and no changes to your integration code are required – the new data persistence logic applies automatically to all API requests using the `2025-11-17.preview` API version and later. You can now retrieve the industry metadata you’ve submitted through the Payment Intents API and receive it in events.

## Impact

Include these optional fields when creating or updating a [PaymentIntent](https://docs.stripe.com/api/payment_intents/object.md?api-version=2025-11-17.preview) using supported payment methods. This data helps payment processors better understand transactions, and can lead to more accurate risk scoring and improved approval rates.

You must provide industry-specific transaction details for certain merchant category codes to comply with card network requirements and to avoid potential cost downgrades. For Klarna, this additional context can improve how payments are assessed through Klarna’s risk assessment systems.

## Changes

#### REST API

| Parameters | Change | Resources or endpoints |
| --- | --- | --- |
| `car_rental_data`, `flight_data`, `lodging_data` | Added | [Charge#capture.payment_details](/api/charges/capture?api-version=2025-11-17.preview#capture_charge-payment_details), [Charge#update.payment_details](/api/charges/update?api-version=2025-11-17.preview#update_charge-payment_details), [PaymentIntent#capture.payment_details](/api/payment_intents/capture?api-version=2025-11-17.preview#capture_payment_intent-payment_details), [PaymentIntent#confirm.payment_details](/api/payment_intents/confirm?api-version=2025-11-17.preview#confirm_payment_intent-payment_details), [PaymentIntent#create.payment_details](/api/payment_intents/create?api-version=2025-11-17.preview#create_payment_intent-payment_details), [PaymentIntent#update.payment_details](/api/payment_intents/update?api-version=2025-11-17.preview#update_payment_intent-payment_details), [PaymentIntent#confirm.payment_method_options.klarna](/api/payment_intents/confirm?api-version=2025-11-17.preview#confirm_payment_intent-payment_method_options-klarna), [PaymentIntent#create.payment_method_options.klarna](/api/payment_intents/create?api-version=2025-11-17.preview#create_payment_intent-payment_method_options-klarna), [PaymentIntent#update.payment_method_options.klarna](/api/payment_intents/update?api-version=2025-11-17.preview#update_payment_intent-payment_method_options-klarna) |

#### Ruby

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `car_rental_data`, `flight_data`, `lodging_data` | Added | [ChargeCaptureParams::PaymentDetail](/api/charges/capture?api-version=2025-11-17.preview#capture_charge-payment_details), [ChargeUpdateParams::PaymentDetail](/api/charges/update?api-version=2025-11-17.preview#update_charge-payment_details), [PaymentIntentCaptureParams::PaymentDetail](/api/payment_intents/capture?api-version=2025-11-17.preview#capture_payment_intent-payment_details), [PaymentIntentConfirmParams::PaymentDetail](/api/payment_intents/confirm?api-version=2025-11-17.preview#confirm_payment_intent-payment_details), [PaymentIntentCreateParams::PaymentDetail](/api/payment_intents/create?api-version=2025-11-17.preview#create_payment_intent-payment_details), [PaymentIntentUpdateParams::PaymentDetail](/api/payment_intents/update?api-version=2025-11-17.preview#update_payment_intent-payment_details), [PaymentIntentConfirmParams::PaymentMethodOption::Klarna](/api/payment_intents/confirm?api-version=2025-11-17.preview#confirm_payment_intent-payment_method_options-klarna), [PaymentIntentCreateParams::PaymentMethodOption::Klarna](/api/payment_intents/create?api-version=2025-11-17.preview#create_payment_intent-payment_method_options-klarna), [PaymentIntentUpdateParams::PaymentMethodOption::Klarna](/api/payment_intents/update?api-version=2025-11-17.preview#update_payment_intent-payment_method_options-klarna) |

#### Python

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `car_rental_data`, `flight_data`, `lodging_data` | Added | [ChargeCaptureParamsPaymentDetail](/api/charges/capture?api-version=2025-11-17.preview#capture_charge-payment_details), [ChargeModifyParamsPaymentDetail](/api/charges/update?api-version=2025-11-17.preview#update_charge-payment_details), [PaymentIntentCaptureParamsPaymentDetail](/api/payment_intents/capture?api-version=2025-11-17.preview#capture_payment_intent-payment_details), [PaymentIntentConfirmParamsPaymentDetail](/api/payment_intents/confirm?api-version=2025-11-17.preview#confirm_payment_intent-payment_details), [PaymentIntentCreateParamsPaymentDetail](/api/payment_intents/create?api-version=2025-11-17.preview#create_payment_intent-payment_details), [PaymentIntentModifyParamsPaymentDetail](/api/payment_intents/update?api-version=2025-11-17.preview#update_payment_intent-payment_details), [PaymentIntentConfirmParamsPaymentMethodOptionKlarna](/api/payment_intents/confirm?api-version=2025-11-17.preview#confirm_payment_intent-payment_method_options-klarna), [PaymentIntentCreateParamsPaymentMethodOptionKlarna](/api/payment_intents/create?api-version=2025-11-17.preview#create_payment_intent-payment_method_options-klarna), [PaymentIntentModifyParamsPaymentMethodOptionKlarna](/api/payment_intents/update?api-version=2025-11-17.preview#update_payment_intent-payment_method_options-klarna) |

#### PHP

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `car_rental_data`, `flight_data`, `lodging_data` | Added | [Charge.capture().$params.payment_detail](/api/charges/capture?api-version=2025-11-17.preview#capture_charge-payment_details), [Charge.update().$params.payment_detail](/api/charges/update?api-version=2025-11-17.preview#update_charge-payment_details), [PaymentIntent.capture().$params.payment_detail](/api/payment_intents/capture?api-version=2025-11-17.preview#capture_payment_intent-payment_details), [PaymentIntent.confirm().$params.payment_detail](/api/payment_intents/confirm?api-version=2025-11-17.preview#confirm_payment_intent-payment_details), [PaymentIntent.create().$params.payment_detail](/api/payment_intents/create?api-version=2025-11-17.preview#create_payment_intent-payment_details), [PaymentIntent.update().$params.payment_detail](/api/payment_intents/update?api-version=2025-11-17.preview#update_payment_intent-payment_details), [PaymentIntent.confirm().$params.payment_method_option.klarna](/api/payment_intents/confirm?api-version=2025-11-17.preview#confirm_payment_intent-payment_method_options-klarna), [PaymentIntent.create().$params.payment_method_option.klarna](/api/payment_intents/create?api-version=2025-11-17.preview#create_payment_intent-payment_method_options-klarna), [PaymentIntent.update().$params.payment_method_option.klarna](/api/payment_intents/update?api-version=2025-11-17.preview#update_payment_intent-payment_method_options-klarna) |

#### Java

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `carRentalData`, `flightData`, `lodgingData` | Added | [ChargeCaptureParams.payment_details](/api/charges/capture?api-version=2025-11-17.preview#capture_charge-payment_details), [ChargeUpdateParams.payment_details](/api/charges/update?api-version=2025-11-17.preview#update_charge-payment_details), [PaymentIntentCaptureParams.payment_details](/api/payment_intents/capture?api-version=2025-11-17.preview#capture_payment_intent-payment_details), [PaymentIntentConfirmParams.payment_details](/api/payment_intents/confirm?api-version=2025-11-17.preview#confirm_payment_intent-payment_details), [PaymentIntentCreateParams.payment_details](/api/payment_intents/create?api-version=2025-11-17.preview#create_payment_intent-payment_details), [PaymentIntentUpdateParams.payment_details](/api/payment_intents/update?api-version=2025-11-17.preview#update_payment_intent-payment_details), [PaymentIntentConfirmParams.payment_method_options.klarna](/api/payment_intents/confirm?api-version=2025-11-17.preview#confirm_payment_intent-payment_method_options-klarna), [PaymentIntentCreateParams.payment_method_options.klarna](/api/payment_intents/create?api-version=2025-11-17.preview#create_payment_intent-payment_method_options-klarna), [PaymentIntentUpdateParams.payment_method_options.klarna](/api/payment_intents/update?api-version=2025-11-17.preview#update_payment_intent-payment_method_options-klarna) |

#### Node.js

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `car_rental_data`, `flight_data`, `lodging_data` | Added | [ChargeCaptureParams.payment_details](/api/charges/capture?api-version=2025-11-17.preview#capture_charge-payment_details), [ChargeUpdateParams.payment_details](/api/charges/update?api-version=2025-11-17.preview#update_charge-payment_details), [PaymentIntentCaptureParams.payment_details](/api/payment_intents/capture?api-version=2025-11-17.preview#capture_payment_intent-payment_details), [PaymentIntentConfirmParams.payment_details](/api/payment_intents/confirm?api-version=2025-11-17.preview#confirm_payment_intent-payment_details), [PaymentIntentCreateParams.payment_details](/api/payment_intents/create?api-version=2025-11-17.preview#create_payment_intent-payment_details), [PaymentIntentUpdateParams.payment_details](/api/payment_intents/update?api-version=2025-11-17.preview#update_payment_intent-payment_details), [PaymentIntentConfirmParams.payment_method_options.klarna](/api/payment_intents/confirm?api-version=2025-11-17.preview#confirm_payment_intent-payment_method_options-klarna), [PaymentIntentCreateParams.payment_method_options.klarna](/api/payment_intents/create?api-version=2025-11-17.preview#create_payment_intent-payment_method_options-klarna), [PaymentIntentUpdateParams.payment_method_options.klarna](/api/payment_intents/update?api-version=2025-11-17.preview#update_payment_intent-payment_method_options-klarna) |

#### Go

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `CarRentalData`, `FlightData`, `LodgingData` | Added | [ChargeCapturePaymentDetailsParams](/api/charges/capture?api-version=2025-11-17.preview#capture_charge-payment_details), [ChargePaymentDetailsParams](/api/charges/update?api-version=2025-11-17.preview#update_charge-payment_details), [PaymentIntentCapturePaymentDetailsParams](/api/payment_intents/capture?api-version=2025-11-17.preview#capture_payment_intent-payment_details), [PaymentIntentConfirmPaymentDetailsParams](/api/payment_intents/confirm?api-version=2025-11-17.preview#confirm_payment_intent-payment_details), [PaymentIntentPaymentDetailsParams](/api/payment_intents/create?api-version=2025-11-17.preview#create_payment_intent-payment_details), [PaymentIntentConfirmPaymentMethodOptionsKlarnaParams](/api/payment_intents/confirm?api-version=2025-11-17.preview#confirm_payment_intent-payment_method_options-klarna), [PaymentIntentPaymentMethodOptionsKlarnaParams](/api/payment_intents/create?api-version=2025-11-17.preview#create_payment_intent-payment_method_options-klarna) |

#### .NET

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `CarRentalData`, `FlightData`, `LodgingData` | Added | [ChargePaymentDetailsOptions](/api/charges/update?api-version=2025-11-17.preview#update_charge-payment_details), [PaymentIntentPaymentDetailsOptions](/api/payment_intents/create?api-version=2025-11-17.preview#create_payment_intent-payment_details), [PaymentIntentPaymentMethodOptionsKlarnaOptions](/api/payment_intents/create?api-version=2025-11-17.preview#create_payment_intent-payment_method_options-klarna) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2025-11-17.preview`
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
