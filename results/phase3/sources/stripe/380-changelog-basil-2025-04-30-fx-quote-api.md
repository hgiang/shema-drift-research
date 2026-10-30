# Adds the FX Quote API to provide extended exchange rate quotes

## What’s new

The [FX Quote API](https://docs.stripe.com/api/fx_quotes.md?api-version=2025-04-30.preview) allows you to retrieve Stripe’s current exchange rate for any of our products. The API supports rates for all [135+ currencies](https://docs.stripe.com/currencies.md) that Stripe supports. You can also use the API to:

- Extend a given rate for 5 minutes, 1 hour, or 24 hours.
- Attach an extended FX rate to [PaymentIntent](https://docs.stripe.com/api/payment_intents.md?api-version=2025-04-30.preview) or [Transfer](https://docs.stripe.com/api/transfers.md?api-version=2025-04-30.preview) to process the transactions at the given extended rate.

## Impact

Use the FX Quote API to retrieve Stripe’s current FX rates and hedge against rate fluctuations by extending rates up to 24 hours. This allows you to localise your prices to global markets.

## Changes

#### REST API

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [FxQuote](/api/fx_quotes/object?api-version=2025-04-30.preview) |

| Endpoints | Change | Resource |
| --- | --- | --- |
| `create`, `list`, `retrieve` | Added | [FxQuote](/api/fx_quotes/object?api-version=2025-04-30.preview) |

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `fx_quote` | Added | [PaymentIntent#confirm](/api/payment_intents/confirm?api-version=2025-04-30.preview), [PaymentIntent#create](/api/payment_intents/create?api-version=2025-04-30.preview), [PaymentIntent#update](/api/payment_intents/update?api-version=2025-04-30.preview), [PaymentIntent](/api/payment_intents/object?api-version=2025-04-30.preview), [Transfer#create](/api/transfers/create?api-version=2025-04-30.preview), [Transfer](/api/transfers/object?api-version=2025-04-30.preview) |

| Values | Change | Enums |
| --- | --- | --- |
| `fx_quote.expired` | Added | [Event.type](/api/events/object?api-version=2025-04-30.preview#event_object-type) |
| `fx_quote.expired` | Added | [WebhookEndpoint#create.enabled_events](/api/webhook_endpoints/create?api-version=2025-04-30.preview#create_webhook_endpoint-enabled_events), [WebhookEndpoint#update.enabled_events](/api/webhook_endpoints/update?api-version=2025-04-30.preview#update_webhook_endpoint-enabled_events) |
| `fx_quote.expired` | Added | [Event.type](/api/events/object?api-version=2025-04-30.preview#event_object-type) |

#### Ruby

|  | Change | Resources |
| --- | --- | --- |
|  | Added | [FxQuote](/api/fx_quotes/object?api-version=2025-04-30.preview), `PaymentIntentAmountDetailsLineItem` |

| Methods | Change | Resource |
| --- | --- | --- |
| `create`, `list`, `retrieve` | Added | [FxQuote](/api/fx_quotes/object?api-version=2025-04-30.preview) |

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `fx_quote` | Added | [PaymentIntent::ConfirmParams](/api/payment_intents/confirm?api-version=2025-04-30.preview), [PaymentIntent::CreateParams](/api/payment_intents/create?api-version=2025-04-30.preview), [PaymentIntent::UpdateParams](/api/payment_intents/update?api-version=2025-04-30.preview), [PaymentIntent](/api/payment_intents/object?api-version=2025-04-30.preview), [Transfer::CreateParams](/api/transfers/create?api-version=2025-04-30.preview), [Transfer](/api/transfers/object?api-version=2025-04-30.preview) |

#### Python

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [FxQuote](/api/fx_quotes/object?api-version=2025-04-30.preview) |

| Methods | Change | Resource |
| --- | --- | --- |
| `create`, `list`, `retrieve` | Added | [FxQuote](/api/fx_quotes/object?api-version=2025-04-30.preview) |

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `fx_quote` | Added | [PaymentIntent.ConfirmParams](/api/payment_intents/confirm?api-version=2025-04-30.preview), [PaymentIntent.CreateParams](/api/payment_intents/create?api-version=2025-04-30.preview), [PaymentIntent.UpdateParams](/api/payment_intents/update?api-version=2025-04-30.preview), [PaymentIntent](/api/payment_intents/object?api-version=2025-04-30.preview), [Transfer.CreateParams](/api/transfers/create?api-version=2025-04-30.preview), [Transfer](/api/transfers/object?api-version=2025-04-30.preview) |

| Values | Change | Enums |
| --- | --- | --- |
| `fx_quote.expired` | Added | [Event.type](/api/events/object?api-version=2025-04-30.preview#event_object-type) |
| `fx_quote.expired` | Added | [WebhookEndpoint.CreateParams.enabled_events](/api/webhook_endpoints/create?api-version=2025-04-30.preview#create_webhook_endpoint-enabled_events), [WebhookEndpoint.UpdateParams.enabled_events](/api/webhook_endpoints/update?api-version=2025-04-30.preview#update_webhook_endpoint-enabled_events) |

#### PHP

|  | Change | Resources |
| --- | --- | --- |
|  | Added | [FxQuote](/api/fx_quotes/object?api-version=2025-04-30.preview), `PaymentIntentAmountDetailsLineItem` |

| Methods | Change | Resource |
| --- | --- | --- |
| `all`, `create`, `retrieve` | Added | [FxQuote](/api/fx_quotes/object?api-version=2025-04-30.preview) |

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `fx_quote` | Added | [PaymentIntent](/api/payment_intents/object?api-version=2025-04-30.preview), [Transfer](/api/transfers/object?api-version=2025-04-30.preview) |

| Value | Change | Enum |
| --- | --- | --- |
| `fx_quote.expired` | Added | [Event.type](/api/events/object?api-version=2025-04-30.preview#event_object-type) |

#### Java

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [FxQuote](/api/fx_quotes/object?api-version=2025-04-30.preview) |

| Methods | Change | Resource |
| --- | --- | --- |
| `create`, `list`, `retrieve` | Added | [FxQuote](/api/fx_quotes/object?api-version=2025-04-30.preview) |

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `fxQuote` | Added | [PaymentIntentConfirmParams](/api/payment_intents/confirm?api-version=2025-04-30.preview), [PaymentIntentCreateParams](/api/payment_intents/create?api-version=2025-04-30.preview), [PaymentIntentUpdateParams](/api/payment_intents/update?api-version=2025-04-30.preview), [PaymentIntent](/api/payment_intents/object?api-version=2025-04-30.preview), [TransferCreateParams](/api/transfers/create?api-version=2025-04-30.preview), [Transfer](/api/transfers/object?api-version=2025-04-30.preview) |

| Value | Change | Enums |
| --- | --- | --- |
| `fx_quote.expired` | Added | [WebhookEndpointCreateParams.enabledEvents](/api/webhook_endpoints/create?api-version=2025-04-30.preview#create_webhook_endpoint-enabled_events), [WebhookEndpointUpdateParams.enabledEvents](/api/webhook_endpoints/update?api-version=2025-04-30.preview#update_webhook_endpoint-enabled_events) |

#### Node.js

|  | Change | Resources |
| --- | --- | --- |
|  | Added | [FxQuote](/api/fx_quotes/object?api-version=2025-04-30.preview), `PaymentIntentAmountDetailsLineItem` |

| Methods | Change | Resource |
| --- | --- | --- |
| `create`, `list`, `retrieve` | Added | [FxQuote](/api/fx_quotes/object?api-version=2025-04-30.preview) |

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `fx_quote` | Added | [PaymentIntentConfirmParams](/api/payment_intents/confirm?api-version=2025-04-30.preview), [PaymentIntentCreateParams](/api/payment_intents/create?api-version=2025-04-30.preview), [PaymentIntentUpdateParams](/api/payment_intents/update?api-version=2025-04-30.preview), [PaymentIntent](/api/payment_intents/object?api-version=2025-04-30.preview), [TransferCreateParams](/api/transfers/create?api-version=2025-04-30.preview), [Transfer](/api/transfers/object?api-version=2025-04-30.preview) |

| Values | Change | Enums |
| --- | --- | --- |
| `fx_quote.expired` | Added | [Event.type](/api/events/object?api-version=2025-04-30.preview#event_object-type) |
| `fx_quote.expired` | Added | [WebhookEndpointCreateParams.enabled_events](/api/webhook_endpoints/create?api-version=2025-04-30.preview#create_webhook_endpoint-enabled_events), [WebhookEndpointUpdateParams.enabled_events](/api/webhook_endpoints/update?api-version=2025-04-30.preview#update_webhook_endpoint-enabled_events) |

#### Go

|  | Change | Resources |
| --- | --- | --- |
|  | Added | [FxQuote](/api/fx_quotes/object?api-version=2025-04-30.preview), `PaymentIntentAmountDetailsLineItem` |

| Methods | Change | Resource |
| --- | --- | --- |
| `Get`, `List`, `New` | Added | [FxQuote](/api/fx_quotes/object?api-version=2025-04-30.preview) |

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `FxQuote` | Added | [PaymentIntentConfirmParams](/api/payment_intents/confirm?api-version=2025-04-30.preview), [PaymentIntentParams](/api/payment_intents/create?api-version=2025-04-30.preview), [PaymentIntent](/api/payment_intents/object?api-version=2025-04-30.preview), [TransferParams](/api/transfers/create?api-version=2025-04-30.preview), [Transfer](/api/transfers/object?api-version=2025-04-30.preview) |

| Value | Change | Enum |
| --- | --- | --- |
| `fx_quote.expired` | Added | [Event.Type](/api/events/object?api-version=2025-04-30.preview#event_object-type) |

|  | Change | Event type |
| --- | --- | --- |
|  | Added | [EventTypeFxQuoteExpired](/api/events/types?api-version=2025-04-30.preview) |

#### .NET

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [FxQuote](/api/fx_quotes/object?api-version=2025-04-30.preview) |

| Methods | Change | Resource |
| --- | --- | --- |
| `Create`, `Get`, `List` | Added | [FxQuote](/api/fx_quotes/object?api-version=2025-04-30.preview) |

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `FxQuote` | Added | [PaymentIntentConfirmOptions](/api/payment_intents/confirm?api-version=2025-04-30.preview), [PaymentIntentCreateOptions](/api/payment_intents/create?api-version=2025-04-30.preview), [PaymentIntentUpdateOptions](/api/payment_intents/update?api-version=2025-04-30.preview), [PaymentIntent](/api/payment_intents/object?api-version=2025-04-30.preview), [TransferCreateOptions](/api/transfers/create?api-version=2025-04-30.preview), [Transfer](/api/transfers/object?api-version=2025-04-30.preview) |

|  | Change | Event type |
| --- | --- | --- |
|  | Added | [FxQuoteExpired](/api/events/types?api-version=2025-04-30.preview) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2025-04-30.preview`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to [v15.2.0-beta.1](https://github.com/stripe/stripe-ruby/releases/tag/v15.2.0-beta.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to [v12.2.0b1](https://github.com/stripe/stripe-python/releases/tag/v12.2.0b1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to [v17.3.0-beta.1](https://github.com/stripe/stripe-php/releases/tag/v17.3.0-beta.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to [v29.2.0-beta.1](https://github.com/stripe/stripe-java/releases/tag/v29.2.0-beta.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to [v18.2.0-beta.1](https://github.com/stripe/stripe-node/releases/tag/v18.2.0-beta.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to [v82.2.0-beta.2](https://github.com/stripe/stripe-go/releases/tag/v82.2.0-beta.2)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to [v48.2.0-beta.2](https://github.com/stripe/stripe-dotnet/releases/tag/v48.2.0-beta.2)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).
