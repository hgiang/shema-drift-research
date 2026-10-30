# Adds Girocard as a PaymentMethod brand and network

## What’s new

Allows you to use Girocard as a card brand and network in various payment method options, expanding the range of supported payment methods.

## Changes

#### REST API

| Value | Change | Enums |
| --- | --- | --- |
| `girocard` | Added | [PaymentIntent#confirm.payment_method_options.card.network](/api/payment_intents/confirm?api-version=2024-09-30.acacia#confirm_payment_intent-payment_method_options-card-network), [PaymentIntent#create.payment_method_options.card.network](/api/payment_intents/create?api-version=2024-09-30.acacia#create_payment_intent-payment_method_options-card-network), [PaymentIntent#update.payment_method_options.card.network](/api/payment_intents/update?api-version=2024-09-30.acacia#update_payment_intent-payment_method_options-card-network), [PaymentIntent.payment_method_options.card.network](/api/payment_intents/object?api-version=2024-09-30.acacia#payment_intent_object-payment_method_options-card-network), [SetupIntent#confirm.payment_method_options.card.network](/api/setup_intents/confirm?api-version=2024-09-30.acacia#confirm_setup_intent-payment_method_options-card-network), [SetupIntent#create.payment_method_options.card.network](/api/setup_intents/create?api-version=2024-09-30.acacia#create_setup_intent-payment_method_options-card-network), [SetupIntent#update.payment_method_options.card.network](/api/setup_intents/update?api-version=2024-09-30.acacia#update_setup_intent-payment_method_options-card-network), [SetupIntent.payment_method_options.card.network](/api/setup_intents/object?api-version=2024-09-30.acacia#setup_intent_object-payment_method_options-card-network), [Subscription#create.payment_settings.payment_method_options.card.network](/api/subscriptions/object?api-version=2024-09-30.acacia#subscription_object-payment_settings-payment_method_options-card-network), [Subscription#update.payment_settings.payment_method_options.card.network](/api/subscriptions/update?api-version=2024-09-30.acacia#update_subscription-payment_settings-payment_method_options-card-network), [Subscription.payment_settings.payment_method_options.card.network](/api/subscriptions/object?api-version=2024-09-30.acacia#subscription_object-payment_settings-payment_method_options-card-network) |

#### Ruby

This change doesn’t affect the Ruby SDK.

#### Python

This change doesn’t affect the Python SDK.

#### PHP

This change doesn’t affect the PHP SDK.

#### Java

| Value | Change | Enums |
| --- | --- | --- |
| `girocard` | Added | [PaymentIntentConfirmParams.payment_method_options.card.network](/api/payment_intents/confirm?api-version=2024-09-30.acacia#confirm_payment_intent-payment_method_options-card-network), [PaymentIntentCreateParams.payment_method_options.card.network](/api/payment_intents/create?api-version=2024-09-30.acacia#create_payment_intent-payment_method_options-card-network), [PaymentIntentUpdateParams.payment_method_options.card.network](/api/payment_intents/update?api-version=2024-09-30.acacia#update_payment_intent-payment_method_options-card-network), [SetupIntentConfirmParams.payment_method_options.card.network](/api/setup_intents/confirm?api-version=2024-09-30.acacia#confirm_setup_intent-payment_method_options-card-network), [SetupIntentCreateParams.payment_method_options.card.network](/api/setup_intents/create?api-version=2024-09-30.acacia#create_setup_intent-payment_method_options-card-network), [SetupIntentUpdateParams.payment_method_options.card.network](/api/setup_intents/update?api-version=2024-09-30.acacia#update_setup_intent-payment_method_options-card-network), [SubscriptionCreateParams.payment_settings.payment_method_options.card.network](/api/subscriptions/object?api-version=2024-09-30.acacia#subscription_object-payment_settings-payment_method_options-card-network), [SubscriptionUpdateParams.payment_settings.payment_method_options.card.network](/api/subscriptions/update?api-version=2024-09-30.acacia#update_subscription-payment_settings-payment_method_options-card-network) |

#### Node.js

| Value | Change | Enums |
| --- | --- | --- |
| `girocard` | Added | [PaymentIntent.payment_method_options.card.network](/api/payment_intents/object?api-version=2024-09-30.acacia#payment_intent_object-payment_method_options-card-network), [PaymentIntentConfirmParams.payment_method_options.card.network](/api/payment_intents/confirm?api-version=2024-09-30.acacia#confirm_payment_intent-payment_method_options-card-network), [PaymentIntentCreateParams.payment_method_options.card.network](/api/payment_intents/create?api-version=2024-09-30.acacia#create_payment_intent-payment_method_options-card-network), [PaymentIntentUpdateParams.payment_method_options.card.network](/api/payment_intents/update?api-version=2024-09-30.acacia#update_payment_intent-payment_method_options-card-network), [SetupIntent.payment_method_options.card.network](/api/setup_intents/object?api-version=2024-09-30.acacia#setup_intent_object-payment_method_options-card-network), [SetupIntentConfirmParams.payment_method_options.card.network](/api/setup_intents/confirm?api-version=2024-09-30.acacia#confirm_setup_intent-payment_method_options-card-network), [SetupIntentCreateParams.payment_method_options.card.network](/api/setup_intents/create?api-version=2024-09-30.acacia#create_setup_intent-payment_method_options-card-network), [SetupIntentUpdateParams.payment_method_options.card.network](/api/setup_intents/update?api-version=2024-09-30.acacia#update_setup_intent-payment_method_options-card-network), [Subscription.payment_settings.payment_method_options.card.network](/api/subscriptions/object?api-version=2024-09-30.acacia#subscription_object-payment_settings-payment_method_options-card-network), [SubscriptionCreateParams.payment_settings.payment_method_options.card.network](/api/subscriptions/object?api-version=2024-09-30.acacia#subscription_object-payment_settings-payment_method_options-card-network), [SubscriptionUpdateParams.payment_settings.payment_method_options.card.network](/api/subscriptions/update?api-version=2024-09-30.acacia#update_subscription-payment_settings-payment_method_options-card-network) |

#### Go

| Value | Change | Enums |
| --- | --- | --- |
| `girocard` | Added | [PaymentIntentPaymentMethodOptionsCardNetwork](/api/payment_intents/object?api-version=2024-09-30.acacia#payment_intent_object-payment_method_options-card-network), [SetupIntentPaymentMethodOptionsCardNetwork](/api/setup_intents/object?api-version=2024-09-30.acacia#setup_intent_object-payment_method_options-card-network), [SubscriptionPaymentSettingsPaymentMethodOptionsCardNetwork](/api/subscriptions/object?api-version=2024-09-30.acacia#subscription_object-payment_settings-payment_method_options-card-network) |

#### .NET

This change doesn’t affect the .NET SDK.

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

- [Adds support for three new payment methods: Multibanco, Twint, and Zip](https://docs.stripe.com/changelog/acacia/2024-09-30/payment-links-new-payment-methods.md)
- [Adds support for using the Multibanco payment method with  billing](https://docs.stripe.com/changelog/acacia/2024-09-30/billing-mutlibanco-support.md)
- [Adds Twint to the PaymentMethodConfiguration API](https://docs.stripe.com/changelog/acacia/2024-09-30/twint-support-payment-method-configuration.md)
