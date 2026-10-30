# Adds support for payment line items

## What’s new

You can now add the line items associated with a payment when creating a [PaymentIntent](https://docs.stripe.com/api/payment_intents/create.md?api-version=2025-10-29) by passing in the [payment_details](https://docs.stripe.com/api/payment_intents/create.md?api-version=2025-10-29#create_payment_intent-payment_details) and [amount_details](https://docs.stripe.com/api/payment_intents/create.md?api-version=2025-10-29#create_payment_intent-amount_detail) parameters.

For more information, read more about [payment line items](https://docs.stripe.com/payments/payment-line-items.md).

## Impact

Payment Intents can now specify line items. When provided, they result in these benefits:

- **Cost savings for eligible commercial cards for *IC+ users* (A pricing plan where businesses pay the variable network cost for each transaction plus the Stripe fee rather than a flat rate for all transactions. This pricing model provides more visibility into payments costs):** By passing payment line items, you can participate in the Level 2/Level 3 (L2/L3) programme that major card networks administer. For eligible commercial cards, passing line item data can provide interchange fee savings.
- **Facilitate reconciliation:** Passing line item data can also facilitate reconciliation for your customers. For example, if you primarily serve government customers, it will aid the customer in reconciling a purchase against what shows up on their statement.
- **Improved authorisation rates:** Payment methods like Klarna and PayPal use line item data in their underwriting models, potentially allowing them to approve more credit based payment options when line items data is passed.

## Changes

#### REST API

|  | Change | Resource |
| --- | --- | --- |
|  | Added | `PaymentIntentAmountDetailsLineItem` |

| Endpoint | Change | Resource |
| --- | --- | --- |
| `list` | Added | `PaymentIntentAmountDetailsLineItem` |

| Parameters | Change | Resources or endpoints |
| --- | --- | --- |
| `amount_details` | Added | [PaymentIntent#capture](/api/payment_intents/capture?api-version=2025-10-29.clover), [PaymentIntent#confirm](/api/payment_intents/confirm?api-version=2025-10-29.clover), [PaymentIntent#create](/api/payment_intents/create?api-version=2025-10-29.clover), [PaymentIntent#increment_authorization](/api/payment_intents/increment_authorization?api-version=2025-10-29.clover#increment_payment_intent), [PaymentIntent#update](/api/payment_intents/update?api-version=2025-10-29.clover) |
| `payment_details` | Added | [PaymentIntent](/api/payment_intents/object?api-version=2025-10-29.clover), [PaymentIntent#capture](/api/payment_intents/capture?api-version=2025-10-29.clover), [PaymentIntent#confirm](/api/payment_intents/confirm?api-version=2025-10-29.clover), [PaymentIntent#create](/api/payment_intents/create?api-version=2025-10-29.clover), [PaymentIntent#increment_authorization](/api/payment_intents/increment_authorization?api-version=2025-10-29.clover#increment_payment_intent), [PaymentIntent#update](/api/payment_intents/update?api-version=2025-10-29.clover) |
| `discount_amount`, `line_items`, `shipping`, `tax` | Added | [PaymentIntent.amount_details](/api/payment_intents/object-amount_details?api-version=2025-10-29.clover) |

#### Ruby

|  | Change | Resource |
| --- | --- | --- |
|  | Added | `PaymentIntentAmountDetailsLineItem` |

| Method | Change | Resource |
| --- | --- | --- |
| `list` | Added | `PaymentIntentAmountDetailsLineItem` |

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `amount_details` | Added | [PaymentIntent::CaptureParams](/api/payment_intents/capture?api-version=2025-10-29.clover), [PaymentIntent::ConfirmParams](/api/payment_intents/confirm?api-version=2025-10-29.clover), [PaymentIntent::CreateParams](/api/payment_intents/create?api-version=2025-10-29.clover), [PaymentIntent::IncrementAuthorizationParams](/api/payment_intents/increment_authorization?api-version=2025-10-29.clover#increment_payment_intent), [PaymentIntent::UpdateParams](/api/payment_intents/update?api-version=2025-10-29.clover) |
| `payment_details` | Added | [PaymentIntent](/api/payment_intents/object?api-version=2025-10-29.clover), [PaymentIntent::CaptureParams](/api/payment_intents/capture?api-version=2025-10-29.clover), [PaymentIntent::ConfirmParams](/api/payment_intents/confirm?api-version=2025-10-29.clover), [PaymentIntent::CreateParams](/api/payment_intents/create?api-version=2025-10-29.clover), [PaymentIntent::IncrementAuthorizationParams](/api/payment_intents/increment_authorization?api-version=2025-10-29.clover#increment_payment_intent), [PaymentIntent::UpdateParams](/api/payment_intents/update?api-version=2025-10-29.clover) |
| `discount_amount`, `line_items`, `shipping`, `tax` | Added | [PaymentIntent::AmountDetail](/api/payment_intents/object-amount_details?api-version=2025-10-29.clover) |

#### Python

|  | Change | Resource |
| --- | --- | --- |
|  | Added | `PaymentIntentAmountDetailsLineItem` |

| Method | Change | Resource |
| --- | --- | --- |
| `list` | Added | `PaymentIntentAmountDetailsLineItem` |

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `amount_details` | Added | [PaymentIntent.CaptureParams](/api/payment_intents/capture?api-version=2025-10-29.clover), [PaymentIntent.ConfirmParams](/api/payment_intents/confirm?api-version=2025-10-29.clover), [PaymentIntent.CreateParams](/api/payment_intents/create?api-version=2025-10-29.clover), [PaymentIntent.IncrementAuthorizationParams](/api/payment_intents/increment_authorization?api-version=2025-10-29.clover#increment_payment_intent), [PaymentIntent.ModifyParams](/api/payment_intents/update?api-version=2025-10-29.clover) |
| `payment_details` | Added | [PaymentIntent](/api/payment_intents/object?api-version=2025-10-29.clover), [PaymentIntent.CaptureParams](/api/payment_intents/capture?api-version=2025-10-29.clover), [PaymentIntent.ConfirmParams](/api/payment_intents/confirm?api-version=2025-10-29.clover), [PaymentIntent.CreateParams](/api/payment_intents/create?api-version=2025-10-29.clover), [PaymentIntent.IncrementAuthorizationParams](/api/payment_intents/increment_authorization?api-version=2025-10-29.clover#increment_payment_intent), [PaymentIntent.ModifyParams](/api/payment_intents/update?api-version=2025-10-29.clover) |
| `discount_amount`, `line_items`, `shipping`, `tax` | Added | [PaymentIntent.AmountDetail](/api/payment_intents/object-amount_details?api-version=2025-10-29.clover) |

#### PHP

|  | Change | Resource |
| --- | --- | --- |
|  | Added | `PaymentIntentAmountDetailsLineItem` |

| Method | Change | Resource |
| --- | --- | --- |
| `all` | Added | `PaymentIntentAmountDetailsLineItem` |

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `amount_details` | Added | [PaymentIntent.capture().$params](/api/payment_intents/capture?api-version=2025-10-29.clover), [PaymentIntent.confirm().$params](/api/payment_intents/confirm?api-version=2025-10-29.clover), [PaymentIntent.create().$params](/api/payment_intents/create?api-version=2025-10-29.clover), [PaymentIntent.increment_authorization().$params](/api/payment_intents/increment_authorization?api-version=2025-10-29.clover#increment_payment_intent), [PaymentIntent.update().$params](/api/payment_intents/update?api-version=2025-10-29.clover) |
| `payment_details` | Added | [PaymentIntent](/api/payment_intents/object?api-version=2025-10-29.clover), [PaymentIntent.capture().$params](/api/payment_intents/capture?api-version=2025-10-29.clover), [PaymentIntent.confirm().$params](/api/payment_intents/confirm?api-version=2025-10-29.clover), [PaymentIntent.create().$params](/api/payment_intents/create?api-version=2025-10-29.clover), [PaymentIntent.increment_authorization().$params](/api/payment_intents/increment_authorization?api-version=2025-10-29.clover#increment_payment_intent), [PaymentIntent.update().$params](/api/payment_intents/update?api-version=2025-10-29.clover) |
| `discount_amount`, `line_items`, `shipping`, `tax` | Added | [PaymentIntent.amount_details](/api/payment_intents/object-amount_details?api-version=2025-10-29.clover) |

#### Java

|  | Change | Resource |
| --- | --- | --- |
|  | Added | `PaymentIntentAmountDetailsLineItem` |

| Method | Change | Resource |
| --- | --- | --- |
| `list` | Added | `PaymentIntentAmountDetailsLineItem` |

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `amountDetails` | Added | [PaymentIntentCaptureParams](/api/payment_intents/capture?api-version=2025-10-29.clover), [PaymentIntentConfirmParams](/api/payment_intents/confirm?api-version=2025-10-29.clover), [PaymentIntentCreateParams](/api/payment_intents/create?api-version=2025-10-29.clover), [PaymentIntentIncrementAuthorizationParams](/api/payment_intents/increment_authorization?api-version=2025-10-29.clover#increment_payment_intent), [PaymentIntentUpdateParams](/api/payment_intents/update?api-version=2025-10-29.clover) |
| `paymentDetails` | Added | [PaymentIntent](/api/payment_intents/object?api-version=2025-10-29.clover), [PaymentIntentCaptureParams](/api/payment_intents/capture?api-version=2025-10-29.clover), [PaymentIntentConfirmParams](/api/payment_intents/confirm?api-version=2025-10-29.clover), [PaymentIntentCreateParams](/api/payment_intents/create?api-version=2025-10-29.clover), [PaymentIntentIncrementAuthorizationParams](/api/payment_intents/increment_authorization?api-version=2025-10-29.clover#increment_payment_intent), [PaymentIntentUpdateParams](/api/payment_intents/update?api-version=2025-10-29.clover) |
| `discountAmount`, `lineItems`, `shipping`, `tax` | Added | [PaymentIntent.amount_details](/api/payment_intents/object-amount_details?api-version=2025-10-29.clover) |

#### Node.js

|  | Change | Resource |
| --- | --- | --- |
|  | Added | `PaymentIntentAmountDetailsLineItem` |

| Method | Change | Resource |
| --- | --- | --- |
| `list` | Added | `PaymentIntentAmountDetailsLineItem` |

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `amount_details` | Added | [PaymentIntentCaptureParams](/api/payment_intents/capture?api-version=2025-10-29.clover), [PaymentIntentConfirmParams](/api/payment_intents/confirm?api-version=2025-10-29.clover), [PaymentIntentCreateParams](/api/payment_intents/create?api-version=2025-10-29.clover), [PaymentIntentIncrementAuthorizationParams](/api/payment_intents/increment_authorization?api-version=2025-10-29.clover#increment_payment_intent), [PaymentIntentUpdateParams](/api/payment_intents/update?api-version=2025-10-29.clover) |
| `payment_details` | Added | [PaymentIntent](/api/payment_intents/object?api-version=2025-10-29.clover), [PaymentIntentCaptureParams](/api/payment_intents/capture?api-version=2025-10-29.clover), [PaymentIntentConfirmParams](/api/payment_intents/confirm?api-version=2025-10-29.clover), [PaymentIntentCreateParams](/api/payment_intents/create?api-version=2025-10-29.clover), [PaymentIntentIncrementAuthorizationParams](/api/payment_intents/increment_authorization?api-version=2025-10-29.clover#increment_payment_intent), [PaymentIntentUpdateParams](/api/payment_intents/update?api-version=2025-10-29.clover) |
| `discount_amount`, `line_items`, `shipping`, `tax` | Added | [PaymentIntent.amount_details](/api/payment_intents/object-amount_details?api-version=2025-10-29.clover) |

#### Go

|  | Change | Resource |
| --- | --- | --- |
|  | Added | `PaymentIntentAmountDetailsLineItem` |

| Method | Change | Resource |
| --- | --- | --- |
| `List` | Added | `PaymentIntentAmountDetailsLineItem` |

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `AmountDetails` | Added | [PaymentIntentCaptureParams](/api/payment_intents/capture?api-version=2025-10-29.clover), [PaymentIntentConfirmParams](/api/payment_intents/confirm?api-version=2025-10-29.clover), [PaymentIntentIncrementAuthorizationParams](/api/payment_intents/increment_authorization?api-version=2025-10-29.clover#increment_payment_intent), [PaymentIntentParams](/api/payment_intents/create?api-version=2025-10-29.clover) |
| `PaymentDetails` | Added | [PaymentIntent](/api/payment_intents/object?api-version=2025-10-29.clover), [PaymentIntentCaptureParams](/api/payment_intents/capture?api-version=2025-10-29.clover), [PaymentIntentConfirmParams](/api/payment_intents/confirm?api-version=2025-10-29.clover), [PaymentIntentIncrementAuthorizationParams](/api/payment_intents/increment_authorization?api-version=2025-10-29.clover#increment_payment_intent), [PaymentIntentParams](/api/payment_intents/create?api-version=2025-10-29.clover) |
| `DiscountAmount`, `LineItems`, `Shipping`, `Tax` | Added | [PaymentIntentAmountDetails](/api/payment_intents/object-amount_details?api-version=2025-10-29.clover) |

#### .NET

|  | Change | Resource |
| --- | --- | --- |
|  | Added | `PaymentIntentAmountDetailsLineItem` |

| Method | Change | Resource |
| --- | --- | --- |
| `List` | Added | `PaymentIntentAmountDetailsLineItem` |

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `AmountDetails` | Added | [PaymentIntentCaptureOptions](/api/payment_intents/capture?api-version=2025-10-29.clover), [PaymentIntentConfirmOptions](/api/payment_intents/confirm?api-version=2025-10-29.clover), [PaymentIntentCreateOptions](/api/payment_intents/create?api-version=2025-10-29.clover), [PaymentIntentIncrementAuthorizationOptions](/api/payment_intents/increment_authorization?api-version=2025-10-29.clover#increment_payment_intent), [PaymentIntentUpdateOptions](/api/payment_intents/update?api-version=2025-10-29.clover) |
| `PaymentDetails` | Added | [PaymentIntent](/api/payment_intents/object?api-version=2025-10-29.clover), [PaymentIntentCaptureOptions](/api/payment_intents/capture?api-version=2025-10-29.clover), [PaymentIntentConfirmOptions](/api/payment_intents/confirm?api-version=2025-10-29.clover), [PaymentIntentCreateOptions](/api/payment_intents/create?api-version=2025-10-29.clover), [PaymentIntentIncrementAuthorizationOptions](/api/payment_intents/increment_authorization?api-version=2025-10-29.clover#increment_payment_intent), [PaymentIntentUpdateOptions](/api/payment_intents/update?api-version=2025-10-29.clover) |
| `DiscountAmount`, `LineItems`, `Shipping`, `Tax` | Added | [PaymentIntent.AmountDetails](/api/payment_intents/object-amount_details?api-version=2025-10-29.clover) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2025-10-29.clover`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to [v17.1.0](https://github.com/stripe/stripe-ruby/releases/tag/v17.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to [v13.1.0](https://github.com/stripe/stripe-python/releases/tag/v13.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to [v18.1.0](https://github.com/stripe/stripe-php/releases/tag/v18.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to [v30.1.0](https://github.com/stripe/stripe-java/releases/tag/v30.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to [v19.2.0](https://github.com/stripe/stripe-node/releases/tag/v19.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to [v83.1.0](https://github.com/stripe/stripe-go/releases/tag/v83.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to [v49.1.0](https://github.com/stripe/stripe-dotnet/releases/tag/v49.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).
