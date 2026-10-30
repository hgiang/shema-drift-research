# Adds the ability to exclude payment methods when using Setup Intents

## What’s new

Adds the [excluded_payment_method_types](https://docs.stripe.com/api/setup_intents/object.md?api-version=2025-10-29.clover#setup_intent_object-excluded_payment_method_types) parameter to use when you [create](https://docs.stripe.com/api/setup_intents/create.md?api-version=2025-10-29.clover) or [update](https://docs.stripe.com/api/setup_intents/update.md?api-version=2025-10-29.clover) transactions using [SetupIntents](https://docs.stripe.com/api/setup_intents.md?api-version=2025-10-29.clover).

## Impact

You can now use the `excluded_payment_method_types` parameter to exclude individual [dynamic payment methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.md) from a particular transaction.

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `excluded_payment_method_types` | Added | [SetupIntent](/api/setup_intents/object?api-version=2025-10-29.clover), [SetupIntent#create](/api/setup_intents/create?api-version=2025-10-29.clover), [SetupIntent#update](/api/setup_intents/update?api-version=2025-10-29.clover) |

#### Ruby

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `excluded_payment_method_types` | Added | [SetupIntent](/api/setup_intents/object?api-version=2025-10-29.clover), [SetupIntent::CreateParams](/api/setup_intents/create?api-version=2025-10-29.clover), [SetupIntent::UpdateParams](/api/setup_intents/update?api-version=2025-10-29.clover) |

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `excluded_payment_method_types` | Added | [SetupIntent](/api/setup_intents/object?api-version=2025-10-29.clover), [SetupIntent.CreateParams](/api/setup_intents/create?api-version=2025-10-29.clover), [SetupIntent.ModifyParams](/api/setup_intents/update?api-version=2025-10-29.clover) |

#### PHP

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `excluded_payment_method_types` | Added | [SetupIntent](/api/setup_intents/object?api-version=2025-10-29.clover), [SetupIntent.create().$params](/api/setup_intents/create?api-version=2025-10-29.clover), [SetupIntent.update().$params](/api/setup_intents/update?api-version=2025-10-29.clover) |

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `excludedPaymentMethodTypes` | Added | [SetupIntent](/api/setup_intents/object?api-version=2025-10-29.clover), [SetupIntentCreateParams](/api/setup_intents/create?api-version=2025-10-29.clover), [SetupIntentUpdateParams](/api/setup_intents/update?api-version=2025-10-29.clover) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `excluded_payment_method_types` | Added | [SetupIntent](/api/setup_intents/object?api-version=2025-10-29.clover), [SetupIntentCreateParams](/api/setup_intents/create?api-version=2025-10-29.clover), [SetupIntentUpdateParams](/api/setup_intents/update?api-version=2025-10-29.clover) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `ExcludedPaymentMethodTypes` | Added | [SetupIntent](/api/setup_intents/object?api-version=2025-10-29.clover), [SetupIntentParams](/api/setup_intents/create?api-version=2025-10-29.clover) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `ExcludedPaymentMethodTypes` | Added | [SetupIntent](/api/setup_intents/object?api-version=2025-10-29.clover), [SetupIntentCreateOptions](/api/setup_intents/create?api-version=2025-10-29.clover), [SetupIntentUpdateOptions](/api/setup_intents/update?api-version=2025-10-29.clover) |

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

## Related changes

- [Adds MB WAY to payment method configurations](https://docs.stripe.com/changelog/clover/2025-10-29/mb-way-payment-method-configuration.md)
- [Adds TWINT payment method options to Checkout Sessions](https://docs.stripe.com/changelog/clover/2025-10-29/twint-checkout-sessions.md)
- [Adds support for specifying payment method configurations to the customer portal](https://docs.stripe.com/changelog/clover/2025-10-29/customer-portal-payment-method-configurations.md)
- [Adds MB WAY payment method to Payment Links and Checkout Sessions](https://docs.stripe.com/changelog/clover/2025-10-29/mb-way-payment-link-checkout-sessions.md)
- [Adds Klarna reference parameters for line items in Payment Intents](https://docs.stripe.com/changelog/clover/2025-10-29/klarna-line-item-reference.md)
- [Adds a subscription reference to Klarna line items in Payment Intents](https://docs.stripe.com/changelog/clover/2025-10-29/klarna-items-payment-intents.md)
- [Adds support for custom payment methods](https://docs.stripe.com/changelog/clover/2025-10-29/custom-payment-methods.md)
