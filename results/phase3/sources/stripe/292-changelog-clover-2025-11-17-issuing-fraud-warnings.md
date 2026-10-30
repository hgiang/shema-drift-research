# Adds a fraud warning for potentially compromised Issuing Cards

## What’s new

[Issuing Cards](https://docs.stripe.com/api/issuing/cards/object.md?api-version=2025-11-17.clover) now specify when they’ve been reported as compromised by the cardholder in the [latest_fraud_warning](https://docs.stripe.com/api/issuing/cards/object.md?api-version=2025-11-17.clover#issuing_card_object-latest_fraud_warning) property, serving as an indicator for issuers to cancel and reissue the affected cards.

## Impact

We recommend you monitor this property to know if a card is potentially compromised and susceptible to fraud. Use this property to make card status changes to prevent fraudulent transactions on the card. Any value in this field indicates that the card might be compromised.

Listen for [issuing_card.updated](https://docs.stripe.com/api/events/types.md?api-version=2025-11-17.clover#event_types-issuing_card.updated) webhook events to know when a card’s fraud warning status changes as a result of a cardholder reporting fraud. [Radar](https://docs.stripe.com/issuing/controls/radar.md) provides additional updates in this field when Stripe’s fraud detection systems detect a possible compromise.

Read more about [managing fraud on Stripe Issuing](https://docs.stripe.com/issuing/manage-fraud.md).

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `latest_fraud_warning` | Added | [Issuing.Card](/api/issuing/cards/object?api-version=2025-11-17.clover) |

#### Ruby

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `latest_fraud_warning` | Added | [Issuing::Card](/api/issuing/cards/object?api-version=2025-11-17.clover) |

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `latest_fraud_warning` | Added | [Issuing.Card](/api/issuing/cards/object?api-version=2025-11-17.clover) |

#### PHP

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `latest_fraud_warning` | Added | [Issuing.Card](/api/issuing/cards/object?api-version=2025-11-17.clover) |

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `latestFraudWarning` | Added | [issuing.Card](/api/issuing/cards/object?api-version=2025-11-17.clover) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `latest_fraud_warning` | Added | [Issuing.Card](/api/issuing/cards/object?api-version=2025-11-17.clover) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `LatestFraudWarning` | Added | [IssuingCard](/api/issuing/cards/object?api-version=2025-11-17.clover) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `LatestFraudWarning` | Added | [Issuing.Card](/api/issuing/cards/object?api-version=2025-11-17.clover) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2025-11-17.clover`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to [v17.2.0](https://github.com/stripe/stripe-ruby/releases/tag/v17.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to [v13.2.0](https://github.com/stripe/stripe-python/releases/tag/v13.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to [v18.2.0](https://github.com/stripe/stripe-php/releases/tag/v18.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to [v30.2.0](https://github.com/stripe/stripe-java/releases/tag/v30.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to [v19.3.0](https://github.com/stripe/stripe-node/releases/tag/v19.3.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to [v83.2.0](https://github.com/stripe/stripe-go/releases/tag/v83.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to [v49.2.0](https://github.com/stripe/stripe-dotnet/releases/tag/v49.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

## Related changes

- [Adds fraud risk assessments to Issuing Authorisations](https://docs.stripe.com/changelog/clover/2025-11-17/fraud-risk-assessments-for-issuing-authorizations.md)
