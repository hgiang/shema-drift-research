# Adds support for issuing fraud challenges

## What’s new

[Issuing](https://docs.stripe.com/issuing.md) users can now see [fraud challenges](https://docs.stripe.com/issuing/controls/fraud-challenges.md) sent for [Authorizations](https://docs.stripe.com/api/issuing/authorizations/object.md?api-version=2024-11-20.acacia) in the `fraud_challenges` array, which also contains the status and outcome of the challenge.

A new `verified_by_fraud_challenge` field shows when fraud risk controls were bypassed for an authorisation due to a previously completed fraud challenge.

## Impact

Fraud challenges allow cardholders to retry transactions that were incorrectly declined by Stripe Issuing’s fraud risk controls. You can enable fraud challenges on the [Issuing settings](https://dashboard.stripe.com/settings/issuing/authorizations) Dashboard page.

## Changes

#### REST API

| Parameters | Change | Resources or endpoints |
| --- | --- | --- |
| `fraud_challenges`, `verified_by_fraud_challenge` | Added | [Issuing.Authorization](/api/issuing/authorizations/object?api-version=2024-11-20.acacia) |

#### Ruby

This change doesn’t affect the Ruby SDK.

#### Python

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `fraud_challenges`, `verified_by_fraud_challenge` | Added | [stripe.issuing.Authorization](/api/issuing/authorizations/object?api-version=2024-11-20.acacia) |

#### PHP

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `fraud_challenges`, `verified_by_fraud_challenge` | Added | [Issuing.Authorization](/api/issuing/authorizations/object?api-version=2024-11-20.acacia) |

#### Java

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `fraud_challenges`, `verified_by_fraud_challenge` | Added | [Issuing.Authorization](/api/issuing/authorizations/object?api-version=2024-11-20.acacia) |

#### Node.js

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `fraud_challenges`, `verified_by_fraud_challenge` | Added | [Issuing.Authorization](/api/issuing/authorizations/object?api-version=2024-11-20.acacia) |

#### Go

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `FraudChallenges`, `VerifiedByFraudChallenge` | Added | [IssuingAuthorization](/api/issuing/authorizations/object?api-version=2024-11-20.acacia) |

#### .NET

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `FraudChallenges`, `VerifiedByFraudChallenge` | Added | [IssuingAuthorization](/api/issuing/authorizations/object?api-version=2024-11-20.acacia) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2024-11-20.acacia`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to [v13.2.0](https://github.com/stripe/stripe-ruby/releases/tag/v13.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to [v11.3.0](https://github.com/stripe/stripe-python/releases/tag/v11.3.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to [v16.3.0](https://github.com/stripe/stripe-php/releases/tag/v16.3.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to [v28.1.0](https://github.com/stripe/stripe-java/releases/tag/v28.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to [v17.4.0](https://github.com/stripe/stripe-node/releases/tag/v17.4.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to [v81.1.0](https://github.com/stripe/stripe-go/releases/tag/v81.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to [v47.1.0](https://github.com/stripe/stripe-dotnet/releases/tag/v47.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

## Related changes

- [Adds support for merchant amount and currency for test mode authorisations](https://docs.stripe.com/changelog/acacia/2024-11-20/add-merchant-currency-and-merchant-amount-on-create-testmode-authorization-method.md)
