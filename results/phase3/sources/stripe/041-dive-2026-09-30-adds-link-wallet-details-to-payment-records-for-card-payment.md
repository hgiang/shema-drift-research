# Adds Link wallet details to Payment Records for card payments

## What’s new

[Payment Records](https://docs.stripe.com/api/payment-record/object.md?api-version=2026-09-30.endive) and [Payment Attempt Records](https://docs.stripe.com/api/payment-attempt-record/object.md?api-version=2026-09-30.endive) now identify [Link card payments](https://docs.stripe.com/payments/link/link-payment-methods.md) in wallet details.

For Link card payments, [payment_method_details](https://docs.stripe.com/api/payment-record/object.md?api-version=2026-09-30.endive#payment_record_object-payment_method_details) now include a [wallet.type](https://docs.stripe.com/api/payment-record/object.md?api-version=2026-09-30.endive#payment_record_object-payment_method_details-card-wallet-type) value of `link`. The [wallet.link](https://docs.stripe.com/api/payment-record/object.md?api-version=2026-09-30.endive#payment_record_object-payment_method_details-card-wallet-link) object may include the [funding_source_group](https://docs.stripe.com/api/payment-record/object.md?api-version=2026-09-30.endive#payment_record_object-payment_method_details-card-wallet-link-funding_source_group) property, which identifies the [funding source group](https://docs.stripe.com/payments/link/link-payment-methods.md) used when confirming a [Link](https://docs.stripe.com/payments/link.md) card payment.

## Impact

If your integration reads wallet details from Payment Records or Payment Attempt Records, [Link card payments](https://docs.stripe.com/payments/link/link-payment-methods.md) may now include a `wallet.type` value of `link` and an optional `wallet.link.funding_source_group` property.

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `link` | Added | [PaymentAttemptRecord.payment_method_details.card.wallet](/api/payment-attempt-record/object?api-version=2026-09-30.endive#payment_attempt_record_object-payment_method_details-card-wallet), [PaymentRecord.payment_method_details.card.wallet](/api/payment-record/object?api-version=2026-09-30.endive#payment_record_object-payment_method_details-card-wallet) |

#### Ruby

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `link` | Added | [PaymentAttemptRecord::PaymentMethodDetail::Card::Wallet](/api/payment-attempt-record/object?api-version=2026-09-30.endive#payment_attempt_record_object-payment_method_details-card-wallet), [PaymentRecord::PaymentMethodDetail::Card::Wallet](/api/payment-record/object?api-version=2026-09-30.endive#payment_record_object-payment_method_details-card-wallet) |

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `link` | Added | [PaymentAttemptRecord.PaymentMethodDetail.Card.Wallet](/api/payment-attempt-record/object?api-version=2026-09-30.endive#payment_attempt_record_object-payment_method_details-card-wallet), [PaymentRecord.PaymentMethodDetail.Card.Wallet](/api/payment-record/object?api-version=2026-09-30.endive#payment_record_object-payment_method_details-card-wallet) |

#### PHP

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `link` | Added | [PaymentAttemptRecord.payment_method_details.card.wallet](/api/payment-attempt-record/object?api-version=2026-09-30.endive#payment_attempt_record_object-payment_method_details-card-wallet), [PaymentRecord.payment_method_details.card.wallet](/api/payment-record/object?api-version=2026-09-30.endive#payment_record_object-payment_method_details-card-wallet) |

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `link` | Added | [PaymentAttemptRecord.payment_method_details.card.wallet](/api/payment-attempt-record/object?api-version=2026-09-30.endive#payment_attempt_record_object-payment_method_details-card-wallet), [PaymentRecord.payment_method_details.card.wallet](/api/payment-record/object?api-version=2026-09-30.endive#payment_record_object-payment_method_details-card-wallet) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `link` | Added | [PaymentAttemptRecord.payment_method_details.card.wallet](/api/payment-attempt-record/object?api-version=2026-09-30.endive#payment_attempt_record_object-payment_method_details-card-wallet), [PaymentRecord.payment_method_details.card.wallet](/api/payment-record/object?api-version=2026-09-30.endive#payment_record_object-payment_method_details-card-wallet) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `Link` | Added | [PaymentAttemptRecordPaymentMethodDetailsCardWallet](/api/payment-attempt-record/object?api-version=2026-09-30.endive#payment_attempt_record_object-payment_method_details-card-wallet), [PaymentRecordPaymentMethodDetailsCardWallet](/api/payment-record/object?api-version=2026-09-30.endive#payment_record_object-payment_method_details-card-wallet) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `Link` | Added | [PaymentAttemptRecord.PaymentMethodDetails.Card.Wallet](/api/payment-attempt-record/object?api-version=2026-09-30.endive#payment_attempt_record_object-payment_method_details-card-wallet), [PaymentRecord.PaymentMethodDetails.Card.Wallet](/api/payment-record/object?api-version=2026-09-30.endive#payment_record_object-payment_method_details-card-wallet) |

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
- [Makes Payment Evaluation signal scores nullable](https://docs.stripe.com/changelog/endive/2026-09-30/payment-evaluations-nullable-score.md)
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
- [Adds 3D Secure versions 2.3.0 and 2.3.1 to Payment Records](https://docs.stripe.com/changelog/endive/2026-09-30/3d-secure-payment-records.md)
- [Adds support for BLIK recurring off-session payments](https://docs.stripe.com/changelog/endive/2026-09-30/blik-recurring-off-session-payments.md)
- [Adds PayPay support for one-time online payments in Japan](https://docs.stripe.com/changelog/endive/2026-09-30/paypay-payments-japan.md)
- [Exposes the network response electronic commerce indicator on card charges](https://docs.stripe.com/changelog/endive/2026-09-30/view-network-response-eci-on-card-charges.md)
- [Adds payment method type information for failed payments](https://docs.stripe.com/changelog/endive/2026-09-30/payment-method-type-payment-failures.md)
- [Adds MoMo payment method details to Payment Records](https://docs.stripe.com/changelog/endive/2026-09-30/adds-momo-payment-method-details-to-payment-records.md)
