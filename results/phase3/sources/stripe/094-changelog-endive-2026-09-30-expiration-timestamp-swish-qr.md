# Adds an expiry timestamp to the Swish QR code object

## What’s new

Swish payment QR codes now include an [expires_at](https://docs.stripe.com/api/payment_intents/object.md?api-version=2026-09-30.endive#payment_intent_object-next_action-swish_handle_redirect_or_display_qr_code-qr_code-expires_at) timestamp for [Payment Intents](https://docs.stripe.com/api/payment_intents/object.md?api-version=2026-09-30.endive) with a [qr_code](https://docs.stripe.com/api/payment_intents/object.md?api-version=2026-09-30.endive#payment_intent_object-next_action-swish_handle_redirect_or_display_qr_code-qr_code) in [next_action.swish_handle_redirect_or_display_qr_code](https://docs.stripe.com/api/payment_intents/object.md?api-version=2026-09-30.endive#payment_intent_object-next_action-swish_handle_redirect_or_display_qr_code). This integer property contains the QR code’s expiry time as a Unix timestamp.

## Impact

Previously, your integration had to estimate when a Swish QR code expired.

You can now use the exact expiry time to display an accurate countdown and automatically hide expired QR codes. This provides clear guidance to customers and prevents attempts to scan a code that’s no longer valid.

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `expires_at` | Added | [PaymentIntent.next_action.swish_handle_redirect_or_display_qr_code.qr_code](/api/payment_intents/object?api-version=2026-09-30.endive#payment_intent_object-next_action-swish_handle_redirect_or_display_qr_code-qr_code) |

#### Ruby

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `expires_at` | Added | [PaymentIntent::NextAction::SwishHandleRedirectOrDisplayQrCode::QrCode](/api/payment_intents/object?api-version=2026-09-30.endive#payment_intent_object-next_action-swish_handle_redirect_or_display_qr_code-qr_code) |

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `expires_at` | Added | [PaymentIntent.NextAction.SwishHandleRedirectOrDisplayQrCode.QrCode](/api/payment_intents/object?api-version=2026-09-30.endive#payment_intent_object-next_action-swish_handle_redirect_or_display_qr_code-qr_code) |

#### PHP

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `expires_at` | Added | [PaymentIntent.next_action.swish_handle_redirect_or_display_qr_code.qr_code](/api/payment_intents/object?api-version=2026-09-30.endive#payment_intent_object-next_action-swish_handle_redirect_or_display_qr_code-qr_code) |

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `expiresAt` | Added | [PaymentIntent.next_action.swish_handle_redirect_or_display_qr_code.qr_code](/api/payment_intents/object?api-version=2026-09-30.endive#payment_intent_object-next_action-swish_handle_redirect_or_display_qr_code-qr_code) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `expires_at` | Added | [PaymentIntent.next_action.swish_handle_redirect_or_display_qr_code.qr_code](/api/payment_intents/object?api-version=2026-09-30.endive#payment_intent_object-next_action-swish_handle_redirect_or_display_qr_code-qr_code) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `ExpiresAt` | Added | [PaymentIntentNextActionSwishHandleRedirectOrDisplayQRCodeQRCode](/api/payment_intents/object?api-version=2026-09-30.endive#payment_intent_object-next_action-swish_handle_redirect_or_display_qr_code-qr_code) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `ExpiresAt` | Added | [PaymentIntent.NextAction.SwishHandleRedirectOrDisplayQrCode.QrCode](/api/payment_intents/object?api-version=2026-09-30.endive#payment_intent_object-next_action-swish_handle_redirect_or_display_qr_code-qr_code) |

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
