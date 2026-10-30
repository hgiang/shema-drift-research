# Adds details about offline collection on card_present PaymentMethod objects

## What’s new

This change provides visibility into `card_present` [Payment Methods](https://docs.stripe.com/api/payment_methods.md?api-version=2024-09-30.acacia) collected offline, allowing you to track and manage offline transactions processed through the Terminal mobile SDKs. By including a `type` field set to `deferred`, you can accurately report and reconcile offline `card_present` transactions.

## Changes

#### REST API

| Parameters | Change | Resources or endpoints |
| --- | --- | --- |
| `offline` | Added | [ConfirmationToken.payment_method_preview.card_present](/api/confirmation_tokens/object?api-version=2024-09-30.acacia#confirmation_token_object-payment_method_preview-card_present), [PaymentMethod.card_present](/api/payment_methods/object?api-version=2024-09-30.acacia#payment_method_object-card_present) |
| `type` | Added | [Charge.payment_method_details.card_present.offline](/api/charges/object?api-version=2024-09-30.acacia#charge_object-payment_method_details-card_present-offline), [ConfirmationToken.payment_method_preview.card.generated_from.payment_method_details.card_present.offline](/api/confirmation_tokens/object?api-version=2024-09-30.acacia#confirmation_token_object-payment_method_preview-card-generated_from-payment_method_details-card_present-offline), [ConfirmationToken.payment_method_preview.card_present.offline](/api/confirmation_tokens/object?api-version=2024-09-30.acacia#confirmation_token_object-payment_method_preview-card_present-offline), [PaymentMethod.card.generated_from.payment_method_details.card_present.offline](/api/payment_methods/object?api-version=2024-09-30.acacia#payment_method_object-card-generated_from-payment_method_details-card_present-offline), [PaymentMethod.card_present.offline](/api/payment_methods/object?api-version=2024-09-30.acacia#payment_method_object-card_present-offline), [SetupAttempt.payment_method_details.card_present.offline](/api/setup_attempts/object?api-version=2024-09-30.acacia#setup_attempt_object-setup_error-code) |

#### Ruby

This change doesn’t affect the Ruby SDK.

#### Python

This change doesn’t affect the Python SDK.

#### PHP

This change doesn’t affect the PHP SDK.

#### Java

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `offline` | Added | [ConfirmationToken.payment_method_preview.card_present](/api/confirmation_tokens/object?api-version=2024-09-30.acacia#confirmation_token_object-payment_method_preview-card_present), [PaymentMethod.card_present](/api/payment_methods/object?api-version=2024-09-30.acacia#payment_method_object-card_present) |
| `type` | Added | [Charge.payment_method_details.card_present.offline](/api/charges/object?api-version=2024-09-30.acacia#charge_object-payment_method_details-card_present-offline), [ConfirmationToken.payment_method_preview.card.generated_from.payment_method_details.card_present.offline](/api/confirmation_tokens/object?api-version=2024-09-30.acacia#confirmation_token_object-payment_method_preview-card-generated_from-payment_method_details-card_present-offline), [PaymentMethod.card.generated_from.payment_method_details.card_present.offline](/api/payment_methods/object?api-version=2024-09-30.acacia#payment_method_object-card-generated_from-payment_method_details-card_present-offline), [SetupAttempt.payment_method_details.card_present.offline](/api/setup_attempts/object?api-version=2024-09-30.acacia#setup_attempt_object-setup_error-code) |

#### Node.js

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `offline` | Added | [ConfirmationToken.payment_method_preview.card_present](/api/confirmation_tokens/object?api-version=2024-09-30.acacia#confirmation_token_object-payment_method_preview-card_present), [PaymentMethod.card_present](/api/payment_methods/object?api-version=2024-09-30.acacia#payment_method_object-card_present) |
| `type` | Added | [Charge.payment_method_details.card_present.offline](/api/charges/object?api-version=2024-09-30.acacia#charge_object-payment_method_details-card_present-offline) |

#### Go

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `Offline` | Added | [ConfirmationTokenPaymentMethodPreviewCardPresent](/api/confirmation_tokens/object?api-version=2024-09-30.acacia#confirmation_token_object-payment_method_preview-card_present), [PaymentMethodCardPresent](/api/payment_methods/object?api-version=2024-09-30.acacia#payment_method_object-card_present) |
| `Type` | Added | [ChargePaymentMethodDetailsCardPresentOffline](/api/charges/object?api-version=2024-09-30.acacia#charge_object-payment_method_details-card_present-offline), [ConfirmationTokenPaymentMethodPreviewCardGeneratedFromPaymentMethodDetailsCardPresentOffline](/api/confirmation_tokens/object?api-version=2024-09-30.acacia#confirmation_token_object-payment_method_preview-card-generated_from-payment_method_details-card_present-offline), [PaymentMethodCardGeneratedFromPaymentMethodDetailsCardPresentOffline](/api/payment_methods/object?api-version=2024-09-30.acacia#payment_method_object-card-generated_from-payment_method_details-card_present-offline), [SetupAttemptPaymentMethodDetailsCardPresentOffline](/api/setup_attempts/object?api-version=2024-09-30.acacia#setup_attempt_object-setup_error-code) |

#### .NET

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `Offline` | Added | [ConfirmationTokenPaymentMethodPreviewCardPresent](/api/confirmation_tokens/object?api-version=2024-09-30.acacia#confirmation_token_object-payment_method_preview-card_present), [PaymentMethodCardPresent](/api/payment_methods/object?api-version=2024-09-30.acacia#payment_method_object-card_present) |
| `Type` | Added | [ChargePaymentMethodDetailsCardPresentOffline](/api/charges/object?api-version=2024-09-30.acacia#charge_object-payment_method_details-card_present-offline), [ConfirmationTokenPaymentMethodPreviewCardGeneratedFromPaymentMethodDetailsCardPresentOffline](/api/confirmation_tokens/object?api-version=2024-09-30.acacia#confirmation_token_object-payment_method_preview-card-generated_from-payment_method_details-card_present-offline), [PaymentMethodCardGeneratedFromPaymentMethodDetailsCardPresentOffline](/api/payment_methods/object?api-version=2024-09-30.acacia#payment_method_object-card-generated_from-payment_method_details-card_present-offline), [SetupAttemptPaymentMethodDetailsCardPresentOffline](/api/setup_attempts/object?api-version=2024-09-30.acacia#setup_attempt_object-setup_error-code) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2024-09-30.acacia`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to [v13.0.0](https://github.com/stripe/stripe-ruby/releases/tag/v13.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to [v11.0.0](https://github.com/stripe/stripe-python/releases/tag/v11.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to [v16.0.0](https://github.com/stripe/stripe-php/releases/tag/v16.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to [v27.0.0](https://github.com/stripe/stripe-java/releases/tag/v27.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to [v17.0.0](https://github.com/stripe/stripe-node/releases/tag/v17.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to [v80.0.0](https://github.com/stripe/stripe-go/releases/tag/v80.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to [v46.0.0](https://github.com/stripe/stripe-dotnet/releases/tag/v46.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

## Related changes

- [Updates consent modelling for saving cards with Terminal](https://docs.stripe.com/changelog/acacia/2024-09-30/terminal-remove-customer-consent-require-allow-redisplay.md)
- [Adds support for configuring the reboot time setting](https://docs.stripe.com/changelog/acacia/2024-09-30/terminal-reboot-window.md)
- [Adds the Stripe S700 reader as a valid device type](https://docs.stripe.com/changelog/acacia/2024-09-30/terminal-reader-s700.md)
