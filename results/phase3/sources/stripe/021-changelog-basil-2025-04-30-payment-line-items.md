# Adds support for payment line items

## What’s new

You can now add the line items associated with a payment when creating a [PaymentIntent](https://docs.stripe.com/api/payment_intents/create.md?api-version=2025-04-30.preview) by passing in the [payment_details](https://docs.stripe.com/api/payment_intents/create.md?api-version=2025-04-30.preview#create_payment_intent-payment_details) and [amount_details](https://docs.stripe.com/api/payment_intents/create.md?api-version=2025-04-30.preview#create_payment_intent-amount_detail) params.

See detailed feature eligibility, restrictions, and integration docs in the official [payment line items documentation](https://docs.stripe.com/payments/payment-line-items.md).

## Impact

Payment line items is a feature in the Payment Intents API that provides benefits for cards and local payment methods processing:

- **Cost savings for eligible commercial cards for *IC+ users* (A pricing plan where businesses pay the variable network cost for each transaction plus the Stripe fee rather than a flat rate for all transactions. This pricing model provides more visibility into payments costs):** By passing payment line items, you can participate in the Level 2/Level 3 (L2/L3) programme that major card networks administer. For eligible commercial cards, passing line item data can provide interchange fee savings.
- **Facilitate reconciliation:** Passing line item data can also facilitate reconciliation for your customers. For example, if you primarily serve government customers, it will aid the customer in reconciling a purchase against what shows up on their statement.
- **Improved authorisation rates:** Payment methods like Klarna and PayPal use line item data in their underwriting models, potentially allowing them to approve more credit based payment options when line items data is passed.

## Changes

#### REST API

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [PaymentIntentAmountDetailsLineItem](/api/payment_intents/object?api-version=2025-04-30.preview#payment_intent_object-amount_details-line_items) |

| Endpoint | Change | Resource |
| --- | --- | --- |
| `list` | Added | [PaymentIntentAmountDetailsLineItem](/api/payment_intents/object?api-version=2025-04-30.preview#payment_intent_object-amount_details-line_items) |

| Parameters | Change | Resources or endpoints |
| --- | --- | --- |
| `customer_reference`, `order_reference` | Added | [Charge#capture.payment_details](/api/charges/capture?api-version=2025-04-30.preview#capture_charge-payment_details), [Charge#update.payment_details](/api/charges/update?api-version=2025-04-30.preview#update_charge-payment_details), [PaymentIntent#capture.payment_details](/api/payment_intents/capture?api-version=2025-04-30.preview#capture_payment_intent-payment_details), [PaymentIntent#confirm.payment_details](/api/payment_intents/confirm?api-version=2025-04-30.preview#confirm_payment_intent-payment_details), [PaymentIntent#create.payment_details](/api/payment_intents/create?api-version=2025-04-30.preview#create_payment_intent-payment_details), [PaymentIntent#update.payment_details](/api/payment_intents/update?api-version=2025-04-30.preview#update_payment_intent-payment_details), [PaymentIntent.payment_details](/api/payment_intents/object?api-version=2025-04-30.preview#payment_intent_object-payment_details) |
| `discount_amount`, `line_items`, `shipping`, `tax` | Added | [PaymentIntent.amount_details](/api/payment_intents/object?api-version=2025-04-30.preview#payment_intent_object-amount_details) |

#### Ruby

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [PaymentIntentAmountDetailsLineItem](/api/payment_intents/object?api-version=2025-04-30.preview#payment_intent_object-amount_details-line_items) |

| Method | Change | Resource |
| --- | --- | --- |
| `list` | Added | [PaymentIntentAmountDetailsLineItem](/api/payment_intents/object?api-version=2025-04-30.preview#payment_intent_object-amount_details-line_items) |

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `customer_reference`, `order_reference` | Added | [Charge::CaptureParams::PaymentDetail](/api/charges/capture?api-version=2025-04-30.preview#capture_charge-payment_details), [Charge::UpdateParams::PaymentDetail](/api/charges/update?api-version=2025-04-30.preview#update_charge-payment_details), [PaymentIntent::CaptureParams::PaymentDetail](/api/payment_intents/capture?api-version=2025-04-30.preview#capture_payment_intent-payment_details), [PaymentIntent::ConfirmParams::PaymentDetail](/api/payment_intents/confirm?api-version=2025-04-30.preview#confirm_payment_intent-payment_details), [PaymentIntent::CreateParams::PaymentDetail](/api/payment_intents/create?api-version=2025-04-30.preview#create_payment_intent-payment_details), [PaymentIntent::PaymentDetail](/api/payment_intents/object?api-version=2025-04-30.preview#payment_intent_object-payment_details), [PaymentIntent::UpdateParams::PaymentDetail](/api/payment_intents/update?api-version=2025-04-30.preview#update_payment_intent-payment_details) |
| `discount_amount`, `line_items`, `shipping`, `tax` | Added | [PaymentIntent::AmountDetail](/api/payment_intents/object?api-version=2025-04-30.preview#payment_intent_object-amount_details) |

#### Python

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [PaymentIntentAmountDetailsLineItem](/api/payment_intents/object?api-version=2025-04-30.preview#payment_intent_object-amount_details-line_items) |

| Method | Change | Resource |
| --- | --- | --- |
| `list` | Added | [PaymentIntentAmountDetailsLineItem](/api/payment_intents/object?api-version=2025-04-30.preview#payment_intent_object-amount_details-line_items) |

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `customer_reference`, `order_reference` | Added | [Charge.CaptureParamsPaymentDetail](/api/charges/capture?api-version=2025-04-30.preview#capture_charge-payment_details), [Charge.ModifyParamsPaymentDetail](/api/charges/update?api-version=2025-04-30.preview#update_charge-payment_details), [PaymentIntent.CaptureParamsPaymentDetail](/api/payment_intents/capture?api-version=2025-04-30.preview#capture_payment_intent-payment_details), [PaymentIntent.ConfirmParamsPaymentDetail](/api/payment_intents/confirm?api-version=2025-04-30.preview#confirm_payment_intent-payment_details), [PaymentIntent.CreateParamsPaymentDetail](/api/payment_intents/create?api-version=2025-04-30.preview#create_payment_intent-payment_details), [PaymentIntent.ModifyParamsPaymentDetail](/api/payment_intents/update?api-version=2025-04-30.preview#update_payment_intent-payment_details), [PaymentIntent.PaymentDetail](/api/payment_intents/object?api-version=2025-04-30.preview#payment_intent_object-payment_details) |
| `discount_amount`, `line_items`, `shipping`, `tax` | Added | [PaymentIntent.AmountDetail](/api/payment_intents/object?api-version=2025-04-30.preview#payment_intent_object-amount_details) |

#### PHP

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [PaymentIntentAmountDetailsLineItem](/api/payment_intents/object?api-version=2025-04-30.preview#payment_intent_object-amount_details-line_items) |

| Method | Change | Resource |
| --- | --- | --- |
| `all` | Added | [PaymentIntentAmountDetailsLineItem](/api/payment_intents/object?api-version=2025-04-30.preview#payment_intent_object-amount_details-line_items) |

#### Java

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [PaymentIntentAmountDetailsLineItem](/api/payment_intents/object?api-version=2025-04-30.preview#payment_intent_object-amount_details-line_items) |

| Method | Change | Resource |
| --- | --- | --- |
| `list` | Added | [PaymentIntentAmountDetailsLineItem](/api/payment_intents/object?api-version=2025-04-30.preview#payment_intent_object-amount_details-line_items) |

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `customerReference`, `orderReference` | Added | [ChargeCaptureParams.payment_details](/api/charges/capture?api-version=2025-04-30.preview#capture_charge-payment_details), [ChargeUpdateParams.payment_details](/api/charges/update?api-version=2025-04-30.preview#update_charge-payment_details), [PaymentIntent.payment_details](/api/payment_intents/object?api-version=2025-04-30.preview#payment_intent_object-payment_details), [PaymentIntentCaptureParams.payment_details](/api/payment_intents/capture?api-version=2025-04-30.preview#capture_payment_intent-payment_details), [PaymentIntentConfirmParams.payment_details](/api/payment_intents/confirm?api-version=2025-04-30.preview#confirm_payment_intent-payment_details), [PaymentIntentCreateParams.payment_details](/api/payment_intents/create?api-version=2025-04-30.preview#create_payment_intent-payment_details), [PaymentIntentUpdateParams.payment_details](/api/payment_intents/update?api-version=2025-04-30.preview#update_payment_intent-payment_details) |
| `discountAmount`, `lineItems`, `shipping`, `tax` | Added | [PaymentIntent.amount_details](/api/payment_intents/object?api-version=2025-04-30.preview#payment_intent_object-amount_details) |

#### Node.js

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [PaymentIntentAmountDetailsLineItem](/api/payment_intents/object?api-version=2025-04-30.preview#payment_intent_object-amount_details-line_items) |

| Method | Change | Resource |
| --- | --- | --- |
| `list` | Added | [PaymentIntentAmountDetailsLineItem](/api/payment_intents/object?api-version=2025-04-30.preview#payment_intent_object-amount_details-line_items) |

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `customer_reference`, `order_reference` | Added | [ChargeCaptureParams.payment_details](/api/charges/capture?api-version=2025-04-30.preview#capture_charge-payment_details), [ChargeUpdateParams.payment_details](/api/charges/update?api-version=2025-04-30.preview#update_charge-payment_details), [PaymentIntent.payment_details](/api/payment_intents/object?api-version=2025-04-30.preview#payment_intent_object-payment_details), [PaymentIntentCaptureParams.payment_details](/api/payment_intents/capture?api-version=2025-04-30.preview#capture_payment_intent-payment_details), [PaymentIntentConfirmParams.payment_details](/api/payment_intents/confirm?api-version=2025-04-30.preview#confirm_payment_intent-payment_details), [PaymentIntentCreateParams.payment_details](/api/payment_intents/create?api-version=2025-04-30.preview#create_payment_intent-payment_details), [PaymentIntentUpdateParams.payment_details](/api/payment_intents/update?api-version=2025-04-30.preview#update_payment_intent-payment_details) |
| `discount_amount`, `line_items`, `shipping`, `tax` | Added | [PaymentIntent.amount_details](/api/payment_intents/object?api-version=2025-04-30.preview#payment_intent_object-amount_details) |

#### Go

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [PaymentIntentAmountDetailsLineItem](/api/payment_intents/object?api-version=2025-04-30.preview#payment_intent_object-amount_details-line_items) |

| Method | Change | Resource |
| --- | --- | --- |
| `List` | Added | [PaymentIntentAmountDetailsLineItem](/api/payment_intents/object?api-version=2025-04-30.preview#payment_intent_object-amount_details-line_items) |

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `CustomerReference`, `OrderReference` | Added | [ChargeCapturePaymentDetailsParams](/api/charges/capture?api-version=2025-04-30.preview#capture_charge-payment_details), [ChargePaymentDetailsParams](/api/charges/update?api-version=2025-04-30.preview#update_charge-payment_details), [PaymentIntentCapturePaymentDetailsParams](/api/payment_intents/capture?api-version=2025-04-30.preview#capture_payment_intent-payment_details), [PaymentIntentConfirmPaymentDetailsParams](/api/payment_intents/confirm?api-version=2025-04-30.preview#confirm_payment_intent-payment_details), [PaymentIntentPaymentDetails](/api/payment_intents/object?api-version=2025-04-30.preview#payment_intent_object-payment_details), [PaymentIntentPaymentDetailsParams](/api/payment_intents/create?api-version=2025-04-30.preview#create_payment_intent-payment_details) |
| `DiscountAmount`, `LineItems`, `Shipping`, `Tax` | Added | [PaymentIntentAmountDetails](/api/payment_intents/object?api-version=2025-04-30.preview#payment_intent_object-amount_details) |

#### .NET

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [PaymentIntentAmountDetailsLineItem](/api/payment_intents/object?api-version=2025-04-30.preview#payment_intent_object-amount_details-line_items) |

| Method | Change | Resource |
| --- | --- | --- |
| `List` | Added | [PaymentIntentAmountDetailsLineItem](/api/payment_intents/object?api-version=2025-04-30.preview#payment_intent_object-amount_details-line_items) |

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `CustomerReference`, `OrderReference` | Added | [ChargePaymentDetailsOptions](/api/charges/capture?api-version=2025-04-30.preview#capture_charge-payment_details), [PaymentIntent.PaymentDetails](/api/payment_intents/object?api-version=2025-04-30.preview#payment_intent_object-payment_details), [PaymentIntentPaymentDetailsOptions](/api/payment_intents/create?api-version=2025-04-30.preview#create_payment_intent-payment_details) |
| `DiscountAmount`, `LineItems`, `Shipping`, `Tax` | Added | [PaymentIntent.AmountDetails](/api/payment_intents/object?api-version=2025-04-30.preview#payment_intent_object-amount_details) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2025-04-30.preview`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to [v15.2.0-beta.1](https://github.com/stripe/stripe-ruby/releases/tag/v15.2.0-beta.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to [v12.2.0b1](https://github.com/stripe/stripe-python/releases/tag/v12.2.0b1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to [v17.3.0-beta.1](https://github.com/stripe/stripe-php/releases/tag/v17.3.0-beta.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to [v29.2.0-beta.1](https://github.com/stripe/stripe-java/releases/tag/v29.2.0-beta.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to [v18.2.0-beta.1](https://github.com/stripe/stripe-node/releases/tag/v18.2.0-beta.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to [v82.2.0-beta.2](https://github.com/stripe/stripe-go/releases/tag/v82.2.0-beta.2)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to [v48.2.0-beta.2](https://github.com/stripe/stripe-dotnet/releases/tag/v48.2.0-beta.2)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).
