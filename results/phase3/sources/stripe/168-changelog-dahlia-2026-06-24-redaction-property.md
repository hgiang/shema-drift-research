# Adds redaction details to additional API resources

## What’s new

Adds the [redaction](https://docs.stripe.com/api/cards/object.md?api-version=2026-06-24.preview#card_object-redaction) hash to additional API resources, including [Cards](https://docs.stripe.com/api/cards.md?api-version=2026-06-24.preview), [Charges](https://docs.stripe.com/api/charges.md?api-version=2026-06-24.preview), [Checkout Sessions](https://docs.stripe.com/api/checkout/sessions.md?api-version=2026-06-24.preview), [Issuing Authorisations](https://docs.stripe.com/api/issuing/authorizations.md?api-version=2026-06-24.preview), [Issuing Cards](https://docs.stripe.com/api/issuing/cards.md?api-version=2026-06-24.preview), [Issuing Cardholders](https://docs.stripe.com/api/issuing/cardholders.md?api-version=2026-06-24.preview), [Issuing Disputes](https://docs.stripe.com/api/issuing/disputes.md?api-version=2026-06-24.preview), [Issuing Transactions](https://docs.stripe.com/api/issuing/transactions.md?api-version=2026-06-24.preview), [PaymentIntents](https://docs.stripe.com/api/payment_intents.md?api-version=2026-06-24.preview), [Payment Methods](https://docs.stripe.com/api/payment_methods.md?api-version=2026-06-24.preview), [SetupIntents](https://docs.stripe.com/api/setup_intents.md?api-version=2026-06-24.preview), [Sources](https://docs.stripe.com/api/sources.md?api-version=2026-06-24.preview) and [Tokens](https://docs.stripe.com/api/tokens.md?api-version=2026-06-24.preview).

## Impact

You can now inspect redaction details on additional API resources. For more information, see the [Redaction Job API](https://docs.stripe.com/api/privacy/redaction-job.md?api-version=2026-06-24.preview).

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `redaction` | Added | [Card](/api/cards/object?api-version=2026-06-24.preview#card_object), [Charge](/api/charges/object?api-version=2026-06-24.preview#charge_object), [Checkout.Session](/api/checkout/sessions/object?api-version=2026-06-24.preview#checkout_session_object), [Issuing.Authorization](/api/issuing/authorizations/object?api-version=2026-06-24.preview#issuing_authorization_object), [Issuing.Card](/api/issuing/cards/object?api-version=2026-06-24.preview#issuing_card_object), [Issuing.Cardholder](/api/issuing/cardholders/object?api-version=2026-06-24.preview#issuing_cardholder_object), [Issuing.Dispute](/api/issuing/disputes/object?api-version=2026-06-24.preview#issuing_dispute_object), [Issuing.Transaction](/api/issuing/transactions/object?api-version=2026-06-24.preview#issuing_transaction_object), [PaymentIntent](/api/payment_intents/object?api-version=2026-06-24.preview#payment_intent_object), [PaymentMethod](/api/payment_methods/object?api-version=2026-06-24.preview#payment_method_object), [SetupIntent](/api/setup_intents/object?api-version=2026-06-24.preview#setup_intent_object), [Source](/api/sources/object?api-version=2026-06-24.preview#source_object), [Token](/api/tokens/object?api-version=2026-06-24.preview#token_object) |

#### Ruby

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `redaction` | Added | [Card](/api/cards/object?api-version=2026-06-24.preview#card_object), [Charge](/api/charges/object?api-version=2026-06-24.preview#charge_object), [Checkout::Session](/api/checkout/sessions/object?api-version=2026-06-24.preview#checkout_session_object), [Issuing::Authorization](/api/issuing/authorizations/object?api-version=2026-06-24.preview#issuing_authorization_object), [Issuing::Card](/api/issuing/cards/object?api-version=2026-06-24.preview#issuing_card_object), [Issuing::Cardholder](/api/issuing/cardholders/object?api-version=2026-06-24.preview#issuing_cardholder_object), [Issuing::Dispute](/api/issuing/disputes/object?api-version=2026-06-24.preview#issuing_dispute_object), [Issuing::Transaction](/api/issuing/transactions/object?api-version=2026-06-24.preview#issuing_transaction_object), [PaymentIntent](/api/payment_intents/object?api-version=2026-06-24.preview#payment_intent_object), [PaymentMethod](/api/payment_methods/object?api-version=2026-06-24.preview#payment_method_object), [SetupIntent](/api/setup_intents/object?api-version=2026-06-24.preview#setup_intent_object), [Source](/api/sources/object?api-version=2026-06-24.preview#source_object), [Token](/api/tokens/object?api-version=2026-06-24.preview#token_object) |

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `redaction` | Added | [Card](/api/cards/object?api-version=2026-06-24.preview#card_object), [Charge](/api/charges/object?api-version=2026-06-24.preview#charge_object), [Checkout.Session](/api/checkout/sessions/object?api-version=2026-06-24.preview#checkout_session_object), [Issuing.Authorization](/api/issuing/authorizations/object?api-version=2026-06-24.preview#issuing_authorization_object), [Issuing.Card](/api/issuing/cards/object?api-version=2026-06-24.preview#issuing_card_object), [Issuing.Cardholder](/api/issuing/cardholders/object?api-version=2026-06-24.preview#issuing_cardholder_object), [Issuing.Dispute](/api/issuing/disputes/object?api-version=2026-06-24.preview#issuing_dispute_object), [Issuing.Transaction](/api/issuing/transactions/object?api-version=2026-06-24.preview#issuing_transaction_object), [PaymentIntent](/api/payment_intents/object?api-version=2026-06-24.preview#payment_intent_object), [PaymentMethod](/api/payment_methods/object?api-version=2026-06-24.preview#payment_method_object), [SetupIntent](/api/setup_intents/object?api-version=2026-06-24.preview#setup_intent_object), [Source](/api/sources/object?api-version=2026-06-24.preview#source_object), [Token](/api/tokens/object?api-version=2026-06-24.preview#token_object) |

#### PHP

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `redaction` | Added | [Card](/api/cards/object?api-version=2026-06-24.preview#card_object), [Charge](/api/charges/object?api-version=2026-06-24.preview#charge_object), [Checkout.Session](/api/checkout/sessions/object?api-version=2026-06-24.preview#checkout_session_object), [Issuing.Authorization](/api/issuing/authorizations/object?api-version=2026-06-24.preview#issuing_authorization_object), [Issuing.Card](/api/issuing/cards/object?api-version=2026-06-24.preview#issuing_card_object), [Issuing.Cardholder](/api/issuing/cardholders/object?api-version=2026-06-24.preview#issuing_cardholder_object), [Issuing.Dispute](/api/issuing/disputes/object?api-version=2026-06-24.preview#issuing_dispute_object), [Issuing.Transaction](/api/issuing/transactions/object?api-version=2026-06-24.preview#issuing_transaction_object), [PaymentIntent](/api/payment_intents/object?api-version=2026-06-24.preview#payment_intent_object), [PaymentMethod](/api/payment_methods/object?api-version=2026-06-24.preview#payment_method_object), [SetupIntent](/api/setup_intents/object?api-version=2026-06-24.preview#setup_intent_object), [Source](/api/sources/object?api-version=2026-06-24.preview#source_object), [Token](/api/tokens/object?api-version=2026-06-24.preview#token_object) |

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `redaction` | Added | [Card](/api/cards/object?api-version=2026-06-24.preview#card_object), [Charge](/api/charges/object?api-version=2026-06-24.preview#charge_object), [PaymentIntent](/api/payment_intents/object?api-version=2026-06-24.preview#payment_intent_object), [PaymentMethod](/api/payment_methods/object?api-version=2026-06-24.preview#payment_method_object), [SetupIntent](/api/setup_intents/object?api-version=2026-06-24.preview#setup_intent_object), [Source](/api/sources/object?api-version=2026-06-24.preview#source_object), [Token](/api/tokens/object?api-version=2026-06-24.preview#token_object), [checkout.Session](/api/checkout/sessions/object?api-version=2026-06-24.preview#checkout_session_object), [issuing.Authorization](/api/issuing/authorizations/object?api-version=2026-06-24.preview#issuing_authorization_object), [issuing.Card](/api/issuing/cards/object?api-version=2026-06-24.preview#issuing_card_object), [issuing.Cardholder](/api/issuing/cardholders/object?api-version=2026-06-24.preview#issuing_cardholder_object), [issuing.Dispute](/api/issuing/disputes/object?api-version=2026-06-24.preview#issuing_dispute_object), [issuing.Transaction](/api/issuing/transactions/object?api-version=2026-06-24.preview#issuing_transaction_object) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `redaction` | Added | [Card](/api/cards/object?api-version=2026-06-24.preview#card_object), [Charge](/api/charges/object?api-version=2026-06-24.preview#charge_object), [Checkout.Session](/api/checkout/sessions/object?api-version=2026-06-24.preview#checkout_session_object), [Issuing.Authorization](/api/issuing/authorizations/object?api-version=2026-06-24.preview#issuing_authorization_object), [Issuing.Card](/api/issuing/cards/object?api-version=2026-06-24.preview#issuing_card_object), [Issuing.Cardholder](/api/issuing/cardholders/object?api-version=2026-06-24.preview#issuing_cardholder_object), [Issuing.Dispute](/api/issuing/disputes/object?api-version=2026-06-24.preview#issuing_dispute_object), [Issuing.Transaction](/api/issuing/transactions/object?api-version=2026-06-24.preview#issuing_transaction_object), [PaymentIntent](/api/payment_intents/object?api-version=2026-06-24.preview#payment_intent_object), [PaymentMethod](/api/payment_methods/object?api-version=2026-06-24.preview#payment_method_object), [SetupIntent](/api/setup_intents/object?api-version=2026-06-24.preview#setup_intent_object), [Source](/api/sources/object?api-version=2026-06-24.preview#source_object), [Token](/api/tokens/object?api-version=2026-06-24.preview#token_object) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `Redaction` | Added | [Card](/api/cards/object?api-version=2026-06-24.preview#card_object), [Charge](/api/charges/object?api-version=2026-06-24.preview#charge_object), [CheckoutSession](/api/checkout/sessions/object?api-version=2026-06-24.preview#checkout_session_object), [IssuingAuthorization](/api/issuing/authorizations/object?api-version=2026-06-24.preview#issuing_authorization_object), [IssuingCard](/api/issuing/cards/object?api-version=2026-06-24.preview#issuing_card_object), [IssuingCardholder](/api/issuing/cardholders/object?api-version=2026-06-24.preview#issuing_cardholder_object), [IssuingDispute](/api/issuing/disputes/object?api-version=2026-06-24.preview#issuing_dispute_object), [IssuingTransaction](/api/issuing/transactions/object?api-version=2026-06-24.preview#issuing_transaction_object), [PaymentIntent](/api/payment_intents/object?api-version=2026-06-24.preview#payment_intent_object), [PaymentMethod](/api/payment_methods/object?api-version=2026-06-24.preview#payment_method_object), [SetupIntent](/api/setup_intents/object?api-version=2026-06-24.preview#setup_intent_object), [Source](/api/sources/object?api-version=2026-06-24.preview#source_object), [Token](/api/tokens/object?api-version=2026-06-24.preview#token_object) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `Redaction` | Added | [Card](/api/cards/object?api-version=2026-06-24.preview#card_object), [Charge](/api/charges/object?api-version=2026-06-24.preview#charge_object), [Checkout.Session](/api/checkout/sessions/object?api-version=2026-06-24.preview#checkout_session_object), [Issuing.Authorization](/api/issuing/authorizations/object?api-version=2026-06-24.preview#issuing_authorization_object), [Issuing.Card](/api/issuing/cards/object?api-version=2026-06-24.preview#issuing_card_object), [Issuing.Cardholder](/api/issuing/cardholders/object?api-version=2026-06-24.preview#issuing_cardholder_object), [Issuing.Dispute](/api/issuing/disputes/object?api-version=2026-06-24.preview#issuing_dispute_object), [Issuing.Transaction](/api/issuing/transactions/object?api-version=2026-06-24.preview#issuing_transaction_object), [PaymentIntent](/api/payment_intents/object?api-version=2026-06-24.preview#payment_intent_object), [PaymentMethod](/api/payment_methods/object?api-version=2026-06-24.preview#payment_method_object), [SetupIntent](/api/setup_intents/object?api-version=2026-06-24.preview#setup_intent_object), [Source](/api/sources/object?api-version=2026-06-24.preview#source_object), [Token](/api/tokens/object?api-version=2026-06-24.preview#token_object) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2026-06-24.preview`
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
