# Makes Payment Evaluation signal scores nullable

## What’s new

Makes the [score](https://docs.stripe.com/api/radar/payment-evaluation/object.md?api-version=2026-09-30.endive#radar_payment_evaluation_object-signals-fraudulent_payment-score) property nullable for all [signals](https://docs.stripe.com/api/radar/payment-evaluation/object.md?api-version=2026-09-30.endive#radar_payment_evaluation_object-signals) in [Payment Evaluations](https://docs.stripe.com/api/radar/payment-evaluation/object.md?api-version=2026-09-30.endive). Radar Standard users receive `null` for `score`. Other eligible Radar plans continue to return rounded numeric scores.

Radar Standard users must now use API version `2026-09-30.endive` or later for all [Payment Evaluation](https://docs.stripe.com/api/radar/payment-evaluation.md?api-version=2026-09-30.endive) requests.

## Why is this a breaking change?

Integrations that expect `score` to always contain a number can fail when it returns `null`. Previously, an unavailable score returned `-1`. After upgrading, it returns `null` instead.

Radar Standard users receive a `payment_evaluation_on_api_version_not_supported` error (HTTP status 403) when making a Payment Evaluation request using an API version earlier than `2026-09-30.endive`. Previously, these requests succeeded.

## Impact

Before upgrading, update your integration to handle `null` signal scores and replace checks for `-1` with checks for `null`. When a score isn’t available, use the corresponding signal’s `risk_level` property, such as [fraudulent_payment.risk_level](https://docs.stripe.com/api/radar/payment-evaluation/object.md?api-version=2026-09-30.endive#radar_payment_evaluation_object-signals-fraudulent_payment-risk_level). Risk levels remain available to Radar Standard users.

If you use Radar Standard, [upgrade your API version](https://docs.stripe.com/upgrades.md#how-can-i-upgrade-my-api) to `2026-09-30.endive` or later to continue using Payment Evaluations.

## Changes

#### REST API

| Fields | Change | From → to |
| --- | --- | --- |
| `Radar.PaymentEvaluation.signals.fraudulent_payment.score`, `Radar.PaymentEvaluation.signals.fraudulent_dispute.score`, `Radar.PaymentEvaluation.signals.early_fraud_warning.score`, `Radar.PaymentEvaluation.signals.stolen_card.score`, `Radar.PaymentEvaluation.signals.non_fraud_dispute.score`, `Radar.PaymentEvaluation.signals.bot.score` | Changed | `number → nullable(number)` |

| Code | Change |  |
| --- | --- | --- |
| `payment_evaluation_on_api_version_not_supported` | Added | `Invoice.last_finalization_error`, `PaymentIntent.last_payment_error`, `SetupAttempt.setup_error`, `SetupIntent.last_setup_error`, `StripeError`, `Terminal.Reader.action.api_error` |

#### Ruby

| Fields | Change | From → to |
| --- | --- | --- |
| `Radar::PaymentEvaluation::Signal::FraudulentPayment.score`, `Radar::PaymentEvaluation::Signal::FraudulentDispute.score`, `Radar::PaymentEvaluation::Signal::EarlyFraudWarning.score`, `Radar::PaymentEvaluation::Signal::StolenCard.score`, `Radar::PaymentEvaluation::Signal::NonFraudDispute.score`, `Radar::PaymentEvaluation::Signal::Bot.score` | Changed | `number → nullable(number)` |

#### Python

| Fields | Change | From → to |
| --- | --- | --- |
| `Radar.PaymentEvaluation.Signal.FraudulentPayment.score`, `Radar.PaymentEvaluation.Signal.FraudulentDispute.score`, `Radar.PaymentEvaluation.Signal.EarlyFraudWarning.score`, `Radar.PaymentEvaluation.Signal.StolenCard.score`, `Radar.PaymentEvaluation.Signal.NonFraudDispute.score`, `Radar.PaymentEvaluation.Signal.Bot.score` | Changed | `number → nullable(number)` |

| Code | Change |  |
| --- | --- | --- |
| `payment_evaluation_on_api_version_not_supported` | Added | `Invoice.LastFinalizationError`, `PaymentIntent.LastPaymentError`, `SetupAttempt.SetupError`, `SetupIntent.LastSetupError`, `StripeError`, `Terminal.Reader.Action.ApiError` |

#### PHP

| Fields | Change | From → to |
| --- | --- | --- |
| `Radar.PaymentEvaluation.signals.fraudulent_payment.score`, `Radar.PaymentEvaluation.signals.fraudulent_dispute.score`, `Radar.PaymentEvaluation.signals.early_fraud_warning.score`, `Radar.PaymentEvaluation.signals.stolen_card.score`, `Radar.PaymentEvaluation.signals.non_fraud_dispute.score`, `Radar.PaymentEvaluation.signals.bot.score` | Changed | `number → nullable(number)` |

| Code | Change |  |
| --- | --- | --- |
| `payment_evaluation_on_api_version_not_supported` | Added | `Invoice.last_finalization_error`, `PaymentIntent.last_payment_error`, `SetupAttempt.setup_error`, `SetupIntent.last_setup_error`, `StripeError`, `Terminal.Reader.action.api_error` |

#### Java

This change doesn’t affect the Java SDK.

#### Node.js

| Fields | Change | From → to |
| --- | --- | --- |
| `Radar.PaymentEvaluation.signals.fraudulent_payment.score`, `Radar.PaymentEvaluation.signals.fraudulent_dispute.score`, `Radar.PaymentEvaluation.signals.early_fraud_warning.score`, `Radar.PaymentEvaluation.signals.stolen_card.score`, `Radar.PaymentEvaluation.signals.non_fraud_dispute.score`, `Radar.PaymentEvaluation.signals.bot.score` | Changed | `number → number | null` |

| Code | Change |  |
| --- | --- | --- |
| `payment_evaluation_on_api_version_not_supported` | Added | `Invoice.last_finalization_error`, `PaymentIntent.last_payment_error`, `SetupAttempt.setup_error`, `SetupIntent.last_setup_error`, `StripeError`, `Terminal.Reader.action.api_error` |

#### Go

| Code | Change |  |
| --- | --- | --- |
| `payment_evaluation_on_api_version_not_supported` | Added | `Error`, `InvoiceLastFinalizationError`, `PaymentIntentLastPaymentError`, `SetupAttemptSetupError`, `SetupIntentLastSetupError`, `StripeError`, `TerminalReaderActionApiError` |

#### .NET

| Fields | Change | From → to |
| --- | --- | --- |
| `Radar.PaymentEvaluation.Signals.FraudulentPayment.Score`, `Radar.PaymentEvaluation.Signals.FraudulentDispute.Score`, `Radar.PaymentEvaluation.Signals.EarlyFraudWarning.Score`, `Radar.PaymentEvaluation.Signals.StolenCard.Score`, `Radar.PaymentEvaluation.Signals.NonFraudDispute.Score`, `Radar.PaymentEvaluation.Signals.Bot.Score` | Changed | `number → nullable(number)` |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2026-09-30.endive`
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

- [Removes the payment method types parameter from Checkout Sessions](https://docs.stripe.com/changelog/endive/2026-09-30/remove-payment-method-types-checkout-sessions.md)
- [Adds support for Data Share Only for 3D Secure authentication](https://docs.stripe.com/changelog/endive/2026-09-30/data-share-only.md)
- [Removes PayTo-specific fields from Payment Methods](https://docs.stripe.com/changelog/endive/2026-09-30/removed-payto-fields.md)
- [Removes the payment method types parameter from Payment Intents and Setup Intents](https://docs.stripe.com/changelog/endive/2026-09-30/removes-the-payment-method-types-parameter-from-payment-intents-and-setup-intents.md)
- [Returns specific decline codes for BLIK payment failures](https://docs.stripe.com/changelog/endive/2026-09-30/blik-granular-decline-codes.md)
- [Deprecates the payment request button](https://docs.stripe.com/changelog/endive/2026-09-30/deprecate-payment-request-button.md)
- [Shows pending-authorization UI for MB WAY, Bizum, and BLIK with stripe.handleNextAction](https://docs.stripe.com/changelog/endive/2026-09-30/handle-next-action-mb-way-bizum-ui.md)
- [Removes support for the payment method types option in Elements](https://docs.stripe.com/changelog/endive/2026-09-30/remove-elements-deferred-intent-payment-method-types.md)
- [Saves Bancontact payment details for future off-session payments in Checkout](https://docs.stripe.com/changelog/endive/2026-09-30/bancontact-off-session-payments-checkout.md)
- [Adds the Standalone 3D Secure API](https://docs.stripe.com/changelog/endive/2026-09-30/standalone-3ds.md)
- [Adds support for SeQura payments](https://docs.stripe.com/changelog/endive/2026-09-30/sequra-payments.md)
- [Adds card-present payment methods to allowed payment method types](https://docs.stripe.com/changelog/endive/2026-09-30/card-present-and-interac-present-enum-values-for-allowed-payment-method-types.md)
- [Adds Link funding source group details on Payment Records](https://docs.stripe.com/changelog/endive/2026-09-30/link-funding-source-group-payment-records.md)
- [Adds early fraud warnings and fraudulent dispute signals for Payment Evaluations](https://docs.stripe.com/changelog/endive/2026-09-30/new-radar-signals-for-payment-evaluations.md)
- [Adds the ability to report cancelled payments](https://docs.stripe.com/changelog/endive/2026-09-30/reporting-canceled-payments.md)
- [Adds support for expanding the mandate on card payment method details](https://docs.stripe.com/changelog/endive/2026-09-30/expand-mandate-on-card-payments-details.md)
- [Adds the Payment Record property to the Payment Intent object](https://docs.stripe.com/changelog/endive/2026-09-30/payment-records-on-payment-intents.md)
- [Adds Link wallet details to Payment Records for card payments](https://docs.stripe.com/changelog/endive/2026-09-30/adds-link-wallet-details-to-payment-records-for-card-payments.md)
- [Adds 3D Secure versions 2.3.0 and 2.3.1 to Payment Records](https://docs.stripe.com/changelog/endive/2026-09-30/3d-secure-payment-records.md)
- [Adds support for BLIK recurring off-session payments](https://docs.stripe.com/changelog/endive/2026-09-30/blik-recurring-off-session-payments.md)
- [Adds PayPay support for one-time online payments in Japan](https://docs.stripe.com/changelog/endive/2026-09-30/paypay-payments-japan.md)
- [Exposes the network response electronic commerce indicator on card charges](https://docs.stripe.com/changelog/endive/2026-09-30/view-network-response-eci-on-card-charges.md)
- [Adds payment method type information for failed payments](https://docs.stripe.com/changelog/endive/2026-09-30/payment-method-type-payment-failures.md)
- [Adds MoMo payment method details to Payment Records](https://docs.stripe.com/changelog/endive/2026-09-30/adds-momo-payment-method-details-to-payment-records.md)
