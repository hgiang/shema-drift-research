# Adds a card-presence spending control for Issuing

## What’s new

Adds the [card_presence](https://docs.stripe.com/api/issuing/authorizations/object.md?api-version=2026-04-22.dahlia#issuing_authorization_object-card_presence) property to the [Issuing Authorisation](https://docs.stripe.com/api/issuing/authorizations/object.md?api-version=2026-04-22.dahlia) object. Also adds the [allowed_card_presences](https://docs.stripe.com/api/issuing/cards/object.md?api-version=2026-04-22.dahlia#issuing_card_object-spending_controls-allowed_card_presences) and [blocked_card_presences](https://docs.stripe.com/api/issuing/cards/object.md?api-version=2026-04-22.dahlia#issuing_card_object-spending_controls-blocked_card_presences) properties to the [Issuing Card](https://docs.stripe.com/api/issuing/cards/object.md?api-version=2026-04-22.dahlia) and [Issuing Cardholder](https://docs.stripe.com/api/issuing/cardholders/object.md?api-version=2026-04-22.dahlia) objects.

These new spending controls for Issuing let you restrict transactions based on whether or not a card is present.

## Impact

You can now allow or block Issuing authorisations based on whether or not the card was present during the transaction. You can see the status of card presence in the Issuing Authorisations API to understand which authorisations these spending controls will decline. [Learn more about Issuing spending controls](https://docs.stripe.com/issuing/controls/spending-controls.md).

## Changes

#### REST API

| Parameters | Change | Resources or endpoints |
| --- | --- | --- |
| `card_presence` | Added | [Issuing.Authorization](/api/issuing/authorizations/object?api-version=2026-04-22.dahlia#issuing_authorization_object) |
| `allowed_card_presences`, `blocked_card_presences` | Added | [Issuing.Card#create.spending_controls](/api/issuing/cards/create?api-version=2026-04-22.dahlia#create_issuing_card-spending_controls), [Issuing.Card#update.spending_controls](/api/issuing/cards/update?api-version=2026-04-22.dahlia#update_issuing_card-spending_controls), [Issuing.Card.spending_controls](/api/issuing/cards/object?api-version=2026-04-22.dahlia#issuing_card_object-spending_controls), [Issuing.Cardholder#create.spending_controls](/api/issuing/cardholders/create?api-version=2026-04-22.dahlia#create_issuing_cardholder-spending_controls), [Issuing.Cardholder#update.spending_controls](/api/issuing/cardholders/update?api-version=2026-04-22.dahlia#update_issuing_cardholder-spending_controls), [Issuing.Cardholder.spending_controls](/api/issuing/cardholders/object?api-version=2026-04-22.dahlia#issuing_cardholder_object-spending_controls) |

#### Ruby

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `card_presence` | Added | [Issuing::Authorization](/api/issuing/authorizations/object?api-version=2026-04-22.dahlia#issuing_authorization_object) |
| `allowed_card_presences`, `blocked_card_presences` | Added | [Issuing::Card::SpendingControl](/api/issuing/cards/object?api-version=2026-04-22.dahlia#issuing_card_object-spending_controls), [Issuing::CardCreateParams::SpendingControl](/api/issuing/cards/create?api-version=2026-04-22.dahlia#create_issuing_card-spending_controls), [Issuing::CardUpdateParams::SpendingControl](/api/issuing/cards/update?api-version=2026-04-22.dahlia#update_issuing_card-spending_controls), [Issuing::Cardholder::SpendingControl](/api/issuing/cardholders/object?api-version=2026-04-22.dahlia#issuing_cardholder_object-spending_controls), [Issuing::CardholderCreateParams::SpendingControl](/api/issuing/cardholders/create?api-version=2026-04-22.dahlia#create_issuing_cardholder-spending_controls), [Issuing::CardholderUpdateParams::SpendingControl](/api/issuing/cardholders/update?api-version=2026-04-22.dahlia#update_issuing_cardholder-spending_controls) |

#### Python

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `card_presence` | Added | [Issuing.Authorization](/api/issuing/authorizations/object?api-version=2026-04-22.dahlia#issuing_authorization_object) |
| `allowed_card_presences`, `blocked_card_presences` | Added | [Issuing.Card.SpendingControl](/api/issuing/cards/object?api-version=2026-04-22.dahlia#issuing_card_object-spending_controls), [Issuing.Cardholder.SpendingControl](/api/issuing/cardholders/object?api-version=2026-04-22.dahlia#issuing_cardholder_object-spending_controls), [issuing.CardCreateParamsSpendingControl](/api/issuing/cards/create?api-version=2026-04-22.dahlia#create_issuing_card-spending_controls), [issuing.CardModifyParamsSpendingControl](/api/issuing/cards/update?api-version=2026-04-22.dahlia#update_issuing_card-spending_controls), [issuing.CardholderCreateParamsSpendingControl](/api/issuing/cardholders/create?api-version=2026-04-22.dahlia#create_issuing_cardholder-spending_controls), [issuing.CardholderModifyParamsSpendingControl](/api/issuing/cardholders/update?api-version=2026-04-22.dahlia#update_issuing_cardholder-spending_controls) |

#### PHP

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `card_presence` | Added | [Issuing.Authorization](/api/issuing/authorizations/object?api-version=2026-04-22.dahlia#issuing_authorization_object) |
| `allowed_card_presences`, `blocked_card_presences` | Added | [Issuing.Card.spending_controls](/api/issuing/cards/object?api-version=2026-04-22.dahlia#issuing_card_object-spending_controls), [Issuing.Cardholder.spending_controls](/api/issuing/cardholders/object?api-version=2026-04-22.dahlia#issuing_cardholder_object-spending_controls), [Issuing\Card.create().$params.spending_control](/api/issuing/cards/create?api-version=2026-04-22.dahlia#create_issuing_card-spending_controls), [Issuing\Card.update().$params.spending_control](/api/issuing/cards/update?api-version=2026-04-22.dahlia#update_issuing_card-spending_controls), [Issuing\Cardholder.create().$params.spending_control](/api/issuing/cardholders/create?api-version=2026-04-22.dahlia#create_issuing_cardholder-spending_controls), [Issuing\Cardholder.update().$params.spending_control](/api/issuing/cardholders/update?api-version=2026-04-22.dahlia#update_issuing_cardholder-spending_controls) |

#### Java

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `cardPresence` | Added | [issuing.Authorization](/api/issuing/authorizations/object?api-version=2026-04-22.dahlia#issuing_authorization_object) |
| `allowedCardPresences`, `blockedCardPresences` | Added | [issuing.Card.spending_controls](/api/issuing/cards/object?api-version=2026-04-22.dahlia#issuing_card_object-spending_controls), [issuing.CardCreateParams.spending_controls](/api/issuing/cards/create?api-version=2026-04-22.dahlia#create_issuing_card-spending_controls), [issuing.CardUpdateParams.spending_controls](/api/issuing/cards/update?api-version=2026-04-22.dahlia#update_issuing_card-spending_controls), [issuing.Cardholder.spending_controls](/api/issuing/cardholders/object?api-version=2026-04-22.dahlia#issuing_cardholder_object-spending_controls), [issuing.CardholderCreateParams.spending_controls](/api/issuing/cardholders/create?api-version=2026-04-22.dahlia#create_issuing_cardholder-spending_controls), [issuing.CardholderUpdateParams.spending_controls](/api/issuing/cardholders/update?api-version=2026-04-22.dahlia#update_issuing_cardholder-spending_controls) |

#### Node.js

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `card_presence` | Added | [Issuing.Authorization](/api/issuing/authorizations/object?api-version=2026-04-22.dahlia#issuing_authorization_object) |
| `allowed_card_presences`, `blocked_card_presences` | Added | [Issuing.Card.spending_controls](/api/issuing/cards/object?api-version=2026-04-22.dahlia#issuing_card_object-spending_controls), [Issuing.CardCreateParams.spending_controls](/api/issuing/cards/create?api-version=2026-04-22.dahlia#create_issuing_card-spending_controls), [Issuing.CardUpdateParams.spending_controls](/api/issuing/cards/update?api-version=2026-04-22.dahlia#update_issuing_card-spending_controls), [Issuing.Cardholder.spending_controls](/api/issuing/cardholders/object?api-version=2026-04-22.dahlia#issuing_cardholder_object-spending_controls), [Issuing.CardholderCreateParams.spending_controls](/api/issuing/cardholders/create?api-version=2026-04-22.dahlia#create_issuing_cardholder-spending_controls), [Issuing.CardholderUpdateParams.spending_controls](/api/issuing/cardholders/update?api-version=2026-04-22.dahlia#update_issuing_cardholder-spending_controls) |

#### Go

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `CardPresence` | Added | [IssuingAuthorization](/api/issuing/authorizations/object?api-version=2026-04-22.dahlia#issuing_authorization_object) |
| `AllowedCardPresences`, `BlockedCardPresences` | Added | [IssuingCardSpendingControls](/api/issuing/cards/object?api-version=2026-04-22.dahlia#issuing_card_object-spending_controls), [IssuingCardSpendingControlsParams](/api/issuing/cards/create?api-version=2026-04-22.dahlia#create_issuing_card-spending_controls), [IssuingCardholderSpendingControls](/api/issuing/cardholders/object?api-version=2026-04-22.dahlia#issuing_cardholder_object-spending_controls), [IssuingCardholderSpendingControlsParams](/api/issuing/cardholders/create?api-version=2026-04-22.dahlia#create_issuing_cardholder-spending_controls) |

#### .NET

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `CardPresence` | Added | [Issuing.Authorization](/api/issuing/authorizations/object?api-version=2026-04-22.dahlia#issuing_authorization_object) |
| `AllowedCardPresences`, `BlockedCardPresences` | Added | [Issuing.Card.SpendingControls](/api/issuing/cards/object?api-version=2026-04-22.dahlia#issuing_card_object-spending_controls), [Issuing.Cardholder.SpendingControls](/api/issuing/cardholders/object?api-version=2026-04-22.dahlia#issuing_cardholder_object-spending_controls), [IssuingCardSpendingControlsOptions](/api/issuing/cards/create?api-version=2026-04-22.dahlia#create_issuing_card-spending_controls), [IssuingCardholderSpendingControlsOptions](/api/issuing/cardholders/create?api-version=2026-04-22.dahlia#create_issuing_cardholder-spending_controls) |

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
