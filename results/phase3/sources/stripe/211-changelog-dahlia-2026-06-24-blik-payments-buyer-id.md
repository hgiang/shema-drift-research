# Adds buyer ID support for BLIK payments

## What’s new

Adds the [buyer_id](https://docs.stripe.com/api/payment_methods/object.md?api-version=2026-06-24.dahlia#payment_method_object-blik-buyer_id) property to the [blik](https://docs.stripe.com/api/payment_methods/object.md?api-version=2026-06-24.dahlia#payment_method_object-blik) hash on the [PaymentMethod](https://docs.stripe.com/api/payment_methods/object.md?api-version=2026-06-24.dahlia) object and to the [payment_method_details.blik](https://docs.stripe.com/api/setup_attempts/object.md?api-version=2026-06-24.dahlia#setup_attempt_object-payment_method_details-blik) hash on the [SetupAttempt](https://docs.stripe.com/api/setup_attempts/object.md?api-version=2026-06-24.dahlia) object. The `buyer_id` property is a unique merchant-scoped identifier that helps identify the specific account holder making the payment.

The `buyer_id` property was previously available only on [Charges](https://docs.stripe.com/api/charges/object.md?api-version=2026-06-24.preview#charge_object-payment_method_details-blik-buyer_id).

## Impact

You can now access buyer identification information for BLIK PaymentMethods and SetupAttempts through the `buyer_id` property. This additional data point can help you:

- Implement sophisticated fraud detection rules
- Meet compliance requirements for payment monitoring
- Correlate payments from the same customer across multiple transactions and payment methods

The `buyer_id` property is read-only and populated automatically when provided by BLIK. No changes to your existing BLIK payment integration are required.

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `buyer_id` | Added | [ConfirmationToken.payment_method_preview.blik](/api/confirmation_tokens/object?api-version=2026-06-24.dahlia#confirmation_token_object-payment_method_preview-blik), [PaymentMethod.blik](/api/payment_methods/object?api-version=2026-06-24.dahlia#payment_method_object-blik) |

#### Ruby

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `buyer_id` | Added | [ConfirmationToken::PaymentMethodPreview::Blik](/api/confirmation_tokens/object?api-version=2026-06-24.dahlia#confirmation_token_object-payment_method_preview-blik), [PaymentMethod::Blik](/api/payment_methods/object?api-version=2026-06-24.dahlia#payment_method_object-blik) |

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `buyer_id` | Added | [ConfirmationToken.PaymentMethodPreview.Blik](/api/confirmation_tokens/object?api-version=2026-06-24.dahlia#confirmation_token_object-payment_method_preview-blik), [PaymentMethod.Blik](/api/payment_methods/object?api-version=2026-06-24.dahlia#payment_method_object-blik) |

#### PHP

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `buyer_id` | Added | [ConfirmationToken.payment_method_preview.blik](/api/confirmation_tokens/object?api-version=2026-06-24.dahlia#confirmation_token_object-payment_method_preview-blik), [PaymentMethod.blik](/api/payment_methods/object?api-version=2026-06-24.dahlia#payment_method_object-blik) |

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `buyerId` | Added | [ConfirmationToken.payment_method_preview.blik](/api/confirmation_tokens/object?api-version=2026-06-24.dahlia#confirmation_token_object-payment_method_preview-blik), [PaymentMethod.blik](/api/payment_methods/object?api-version=2026-06-24.dahlia#payment_method_object-blik) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `buyer_id` | Added | [ConfirmationToken.payment_method_preview.blik](/api/confirmation_tokens/object?api-version=2026-06-24.dahlia#confirmation_token_object-payment_method_preview-blik), [PaymentMethod.blik](/api/payment_methods/object?api-version=2026-06-24.dahlia#payment_method_object-blik) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `BuyerID` | Added | [ConfirmationTokenPaymentMethodPreviewBlik](/api/confirmation_tokens/object?api-version=2026-06-24.dahlia#confirmation_token_object-payment_method_preview-blik), [PaymentMethodBlik](/api/payment_methods/object?api-version=2026-06-24.dahlia#payment_method_object-blik) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `BuyerId` | Added | [ConfirmationToken.PaymentMethodPreview.Blik](/api/confirmation_tokens/object?api-version=2026-06-24.dahlia#confirmation_token_object-payment_method_preview-blik), [PaymentMethod.Blik](/api/payment_methods/object?api-version=2026-06-24.dahlia#payment_method_object-blik) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2026-06-24.dahlia`
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

- [Adds buyer ID support for Bizum payments](https://docs.stripe.com/changelog/dahlia/2026-06-24/bizum-payments-buyer-id.md)
- [Enables manual capture for Sunbit payments](https://docs.stripe.com/changelog/dahlia/2026-06-24/enables-manual-capture-for-sunbit-payments.md)
- [Adds a fingerprint to Pix payment method details](https://docs.stripe.com/changelog/dahlia/2026-06-24/pix-fingerprint-payment-method-details.md)
- [Adds transaction link ID to card payment method details for Mastercard and Maestro transactions](https://docs.stripe.com/changelog/dahlia/2026-06-24/card-payment-method-details-transaction-link-id.md)
- [Adds payment method options for Sunbit in Checkout Sessions](https://docs.stripe.com/changelog/dahlia/2026-06-24/sunbit-checkout-pmo.md)
- [Adds support for the Sui network and USDsui token for crypto payments](https://docs.stripe.com/changelog/dahlia/2026-06-24/sui-network-and-usdsui-token-support.md)
- [Adds support for Mastercard compliance disputes](https://docs.stripe.com/changelog/dahlia/2026-06-24/mastercard-compliance-disputes.md)
- [Adds support for recurring payments with Satispay](https://docs.stripe.com/changelog/dahlia/2026-06-24/satispay-recurring-payments.md)
