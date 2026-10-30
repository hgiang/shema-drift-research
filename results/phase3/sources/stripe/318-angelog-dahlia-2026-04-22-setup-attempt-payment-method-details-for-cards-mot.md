# Adds the moto property to Setup Attempt payment method details for cards

## What’s new

Adds the [moto](https://docs.stripe.com/api/setup_attempts/object.md?api-version=2026-04-22.dahlia#setup_attempt_object-payment_method_details-card-moto) boolean property to [Setup Attempts](https://docs.stripe.com/api/setup_attempts/object.md?api-version=2026-04-22.dahlia) objects under the [payment_method_details.card](https://docs.stripe.com/api/setup_attempts/object.md?api-version=2026-04-22.dahlia#setup_attempt_object-payment_method_details-card) hash. This property indicates whether the payment is MOTO (Mail Order/Telephone Order) and out of scope for Strong Customer Authentication (SCA) requirements.

This change brings parity with the [Charges](https://docs.stripe.com/api/charges.md?api-version=2026-04-22.dahlia) API, which already includes the [moto](https://docs.stripe.com/api/charges/object.md?api-version=2026-04-22.dahlia#charge_object-payment_method_details-card-moto) property in its payment method details for card payments.

## Impact

You can now access MOTO status information directly from Setup Attempt objects when working with card payment methods. This helps you with compliance and reporting, because it’s easier to identify which Setup Attempts were processed as MOTO transactions and are out of scope for SCA requirements.

If you’re already handling MOTO information for [Payment Intents](https://docs.stripe.com/api/payment_intents.md?api-version=2026-04-22.dahlia#payment_intent_object-latest_charge), you can now apply the same logic to [Setup Intents](https://docs.stripe.com/api/setup_intents.md?api-version=2026-04-22.dahlia#setup_intent_object-latest_attempt) for a consistent approach across both payment flows.

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `moto` | Added | [SetupAttempt.payment_method_details.card](/api/setup_attempts/object?api-version=2026-04-22.dahlia#setup_attempt_object-payment_method_details-card) |

#### Ruby

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `moto` | Added | [SetupAttempt::PaymentMethodDetail::Card](/api/setup_attempts/object?api-version=2026-04-22.dahlia#setup_attempt_object-payment_method_details-card) |

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `moto` | Added | [SetupAttempt.PaymentMethodDetail.Card](/api/setup_attempts/object?api-version=2026-04-22.dahlia#setup_attempt_object-payment_method_details-card) |

#### PHP

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `moto` | Added | [SetupAttempt.payment_method_details.card](/api/setup_attempts/object?api-version=2026-04-22.dahlia#setup_attempt_object-payment_method_details-card) |

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `moto` | Added | [SetupAttempt.payment_method_details.card](/api/setup_attempts/object?api-version=2026-04-22.dahlia#setup_attempt_object-payment_method_details-card) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `moto` | Added | [SetupAttempt.payment_method_details.card](/api/setup_attempts/object?api-version=2026-04-22.dahlia#setup_attempt_object-payment_method_details-card) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `MOTO` | Added | [SetupAttemptPaymentMethodDetailsCard](/api/setup_attempts/object?api-version=2026-04-22.dahlia#setup_attempt_object-payment_method_details-card) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `Moto` | Added | [SetupAttempt.PaymentMethodDetails.Card](/api/setup_attempts/object?api-version=2026-04-22.dahlia#setup_attempt_object-payment_method_details-card) |

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
- [Adds QR code support for Klarna payments with Terminal readers](https://docs.stripe.com/changelog/dahlia/2026-04-22/klarna-payments-with-terminal-readers-qr-code-support.md)
- [Adds support for Managed Payments, Stripe’s merchant of record solution](https://docs.stripe.com/changelog/dahlia/2026-04-22/managed-payments.md)
