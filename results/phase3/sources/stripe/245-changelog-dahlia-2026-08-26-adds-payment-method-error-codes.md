# Adds new error codes for payment method failures

## What’s new

Adds the following new error codes to report failure states across payment method types, countries and regions:

- `authentication_failure`
- `expired_payment_method`
- `incorrect_postal_code`
- `payment_method_restricted`

For detailed descriptions, see the [error codes](https://docs.stripe.com/error-codes.md) reference.

## Impact

This change does not remove any error codes, so no immediate action is required. To support a wider range of error cases on the impacted endpoints, update your error handling to recognise `authentication_failure`, `expired_payment_method`, `incorrect_postal_code` and `payment_method_restricted`.

The new code `payment_method_restricted` identifies issuer or platform restrictions such as those imposed after a card is reported lost or stolen. The other new error codes (`authentication_failure`, `expired_payment_method` and `incorrect_postal_code`) are similar to existing error codes, but represent failures consistently across payment method types, countries, and regions.

Previously, authentication failures reflected their specific payment object, such as `payment_intent_authentication_failure` and `setup_intent_authentication_failure`, excluding other integration paths. Payment method expiry and postal code errors reflected card-specific `expired_card` and region-specific `incorrect_zip`, respectively, excluding the many other payment method types and regions.

## Changes

#### REST API

| Codes | Change |  |
| --- | --- | --- |
| `authentication_failure`, `expired_payment_method`, `incorrect_postal_code`, `payment_method_restricted` | Added | `Invoice.last_finalization_error`, `PaymentIntent.last_payment_error`, `SetupAttempt.setup_error`, `SetupIntent.last_setup_error`, `StripeError`, `Terminal.Reader.action.api_error` |

#### Ruby

This change doesn’t affect the Ruby SDK.

#### Python

| Codes | Change |  |
| --- | --- | --- |
| `authentication_failure`, `expired_payment_method`, `incorrect_postal_code`, `payment_method_restricted` | Added | `Invoice.LastFinalizationError`, `PaymentIntent.LastPaymentError`, `SetupAttempt.SetupError`, `SetupIntent.LastSetupError`, `StripeError`, `Terminal.Reader.Action.ApiError` |

#### PHP

| Codes | Change |  |
| --- | --- | --- |
| `authentication_failure`, `expired_payment_method`, `incorrect_postal_code`, `payment_method_restricted` | Added | `Invoice.last_finalization_error`, `PaymentIntent.last_payment_error`, `SetupAttempt.setup_error`, `SetupIntent.last_setup_error`, `StripeError`, `Terminal.Reader.action.api_error` |

#### Java

This change doesn’t affect the Java SDK.

#### Node.js

| Codes | Change |  |
| --- | --- | --- |
| `authentication_failure`, `expired_payment_method`, `incorrect_postal_code`, `payment_method_restricted` | Added | `Invoice.last_finalization_error`, `PaymentIntent.last_payment_error`, `SetupAttempt.setup_error`, `SetupIntent.last_setup_error`, `StripeError`, `Terminal.Reader.action.api_error` |

#### Go

| Codes | Change |  |
| --- | --- | --- |
| `authentication_failure`, `expired_payment_method`, `incorrect_postal_code`, `payment_method_restricted` | Added | `Error`, `InvoiceLastFinalizationError`, `PaymentIntentLastPaymentError`, `SetupAttemptSetupError`, `SetupIntentLastSetupError`, `StripeError`, `TerminalReaderActionApiError` |

#### .NET

This change doesn’t affect the .NET SDK.

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2026-08-26.dahlia`
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

- [Adds support for updating Connect parameters of an existing Payment Link](https://docs.stripe.com/changelog/dahlia/2026-08-26/adds-connect-parameters-to-the-payment-link-update-method.md)
- [Adds a funding source identifier to Link payments](https://docs.stripe.com/changelog/dahlia/2026-08-26/adds-funding-source-group-property-for-link-payments.md)
- [Adds the ability to restrict card funding types in Checkout Sessions](https://docs.stripe.com/changelog/dahlia/2026-08-26/adds-card-funding-type-filtering-to-checkout-sessions.md)
- [Adds support for metadata in confirmation tokens](https://docs.stripe.com/changelog/dahlia/2026-08-26/adds-metadata-support-to-confirmation-tokens.md)
- [Adds a funding source identifier to Link wallet card payments](https://docs.stripe.com/changelog/dahlia/2026-08-26/adds-funding-source-group-property-to-link-wallet-payments-on-card-charges.md)
