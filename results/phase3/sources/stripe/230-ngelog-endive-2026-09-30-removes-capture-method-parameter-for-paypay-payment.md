# Removes the capture method parameter for PayPay payments

## What’s new

PayPay is now generally available to eligible businesses in Japan for one-time online payments. As part of this release, the [capture_method](https://docs.stripe.com/api/payment_intents/create.md?api-version=2026-08-26.preview#create_payment_intent-payment_method_options-paypay-capture_method) parameter on the [payment_method_options.paypay](https://docs.stripe.com/api/payment_intents/confirm.md?api-version=2026-08-26.preview#confirm_payment_intent-payment_method_options-paypay) hash is removed from the public preview channel.

## Why is this a breaking change?

Integrations that reference the `capture_method` parameter might encounter compilation or type-checking errors after upgrading their API version.

Although this is structurally a breaking API change, manual capture never functioned for PayPay. Requests attempting to use `capture_method=manual` were already rejected.

## Impact

Most integrations don’t need to make any changes. If your integration sets `payment_method_options.paypay.capture_method`, remove that parameter before upgrading your API version.

PayPay payments continue to use automatic capture. This change doesn’t affect integrations that weren’t setting the parameter, and it doesn’t remove any previously functioning manualcapture behaviour.

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `capture_method` | Removed | [PaymentIntent#confirm.payment_method_options.paypay](/api/payment_intents/confirm?api-version=2026-09-30.preview#confirm_payment_intent-payment_method_options-paypay), [PaymentIntent#create.payment_method_options.paypay](/api/payment_intents/create?api-version=2026-09-30.preview#create_payment_intent-payment_method_options-paypay), [PaymentIntent#update.payment_method_options.paypay](/api/payment_intents/update?api-version=2026-09-30.preview#update_payment_intent-payment_method_options-paypay) |

| Field | Change | From → to |
| --- | --- | --- |
| `Account.business_profile.specified_commercial_transactions_act_url` | Changed | `optional → required` |

#### Ruby

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `capture_method` | Removed | [PaymentIntentConfirmParams::PaymentMethodOption::Paypay](/api/payment_intents/confirm?api-version=2026-09-30.preview#confirm_payment_intent-payment_method_options-paypay), [PaymentIntentCreateParams::PaymentMethodOption::Paypay](/api/payment_intents/create?api-version=2026-09-30.preview#create_payment_intent-payment_method_options-paypay), [PaymentIntentUpdateParams::PaymentMethodOption::Paypay](/api/payment_intents/update?api-version=2026-09-30.preview#update_payment_intent-payment_method_options-paypay) |

| Field | Change | From → to |
| --- | --- | --- |
| `Account::BusinessProfile.specified_commercial_transactions_act_url` | Changed | `optional → required` |

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `capture_method` | Removed | [PaymentIntentConfirmParamsPaymentMethodOptionPaypay](/api/payment_intents/confirm?api-version=2026-09-30.preview#confirm_payment_intent-payment_method_options-paypay), [PaymentIntentCreateParamsPaymentMethodOptionPaypay](/api/payment_intents/create?api-version=2026-09-30.preview#create_payment_intent-payment_method_options-paypay), [PaymentIntentModifyParamsPaymentMethodOptionPaypay](/api/payment_intents/update?api-version=2026-09-30.preview#update_payment_intent-payment_method_options-paypay) |

| Field | Change | From → to |
| --- | --- | --- |
| `Account.BusinessProfile.specified_commercial_transactions_act_url` | Changed | `optional → required` |

#### PHP

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `capture_method` | Removed | [PaymentIntent.confirm().$params.payment_method_option.paypay](/api/payment_intents/confirm?api-version=2026-09-30.preview#confirm_payment_intent-payment_method_options-paypay), [PaymentIntent.create().$params.payment_method_option.paypay](/api/payment_intents/create?api-version=2026-09-30.preview#create_payment_intent-payment_method_options-paypay), [PaymentIntent.update().$params.payment_method_option.paypay](/api/payment_intents/update?api-version=2026-09-30.preview#update_payment_intent-payment_method_options-paypay) |

| Field | Change | From → to |
| --- | --- | --- |
| `Account.business_profile.specified_commercial_transactions_act_url` | Changed | `optional → required` |

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `captureMethod` | Removed | [PaymentIntentConfirmParams.payment_method_options.paypay](/api/payment_intents/confirm?api-version=2026-09-30.preview#confirm_payment_intent-payment_method_options-paypay), [PaymentIntentCreateParams.payment_method_options.paypay](/api/payment_intents/create?api-version=2026-09-30.preview#create_payment_intent-payment_method_options-paypay), [PaymentIntentUpdateParams.payment_method_options.paypay](/api/payment_intents/update?api-version=2026-09-30.preview#update_payment_intent-payment_method_options-paypay) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `capture_method` | Removed | [PaymentIntentConfirmParams.payment_method_options.paypay](/api/payment_intents/confirm?api-version=2026-09-30.preview#confirm_payment_intent-payment_method_options-paypay), [PaymentIntentCreateParams.payment_method_options.paypay](/api/payment_intents/create?api-version=2026-09-30.preview#create_payment_intent-payment_method_options-paypay), [PaymentIntentUpdateParams.payment_method_options.paypay](/api/payment_intents/update?api-version=2026-09-30.preview#update_payment_intent-payment_method_options-paypay) |

| Field | Change | From → to |
| --- | --- | --- |
| `Account.business_profile.specified_commercial_transactions_act_url` | Changed | `optional → required` |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `CaptureMethod` | Removed | [PaymentIntentConfirmPaymentMethodOptionsPaypayParams](/api/payment_intents/confirm?api-version=2026-09-30.preview#confirm_payment_intent-payment_method_options-paypay), [PaymentIntentPaymentMethodOptionsPaypayParams](/api/payment_intents/create?api-version=2026-09-30.preview#create_payment_intent-payment_method_options-paypay) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `CaptureMethod` | Removed | [PaymentIntentPaymentMethodOptionsPaypayOptions](/api/payment_intents/create?api-version=2026-09-30.preview#create_payment_intent-payment_method_options-paypay) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2026-09-30.preview`
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

- [Adds page limit validation for dispute evidence](https://docs.stripe.com/changelog/endive/2026-09-30/page-limit-validation-for-dispute-evidence.md)
- [Adds the ability to update payment intent data on Checkout Sessions](https://docs.stripe.com/changelog/endive/2026-09-30/update-payment-intent-data-on-checkout-sessions.md)
- [Adds support for submitting evidence to appeal a dispute decision](https://docs.stripe.com/changelog/endive/2026-09-30/submit-evidence-to-appeal-dispute-decision.md)
- [Adds support for specifying card-on-file usage when saving and charging saved cards](https://docs.stripe.com/changelog/endive/2026-09-30/add-card-on-file-usage-indicators.md)
