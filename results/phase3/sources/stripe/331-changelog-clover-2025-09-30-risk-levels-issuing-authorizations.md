# Updates risk levels for Issuing Authorisations to use standard values

## What’s new

To be consistent with other Stripe APIs, we renamed the [risk levels](https://docs.stripe.com/api/issuing/authorizations/object.md?api-version=2025-09-30.clover#issuing_authorization_object-risk_assessment-merchant_dispute_risk-risk_level) for [Issuing Authorisations](https://docs.stripe.com/api/issuing/authorizations.md?api-version=2025-09-30.clover) to the following standard values:

- `unknown`
- `not_assessed`
- `low`
- `normal`
- `elevated`
- `highest`

## Why is this a breaking change?

This change renames existing enum values for risk levels and introduces new values to match other Stripe APIs. Referencing the previous enum values in your integration or failing to handle the new values might affect risk evaluation accuracy.

## Impact

You must support these new enum values and remove use of the previous values.

- The [risk_assessment.merchant_dispute_risk.risk_level](https://docs.stripe.com/api/issuing/authorizations/object.md?api-version=2025-09-30.clover#issuing_authorization_object-risk_assessment-merchant_dispute_risk-risk_level) field adds `low` as a new value and replaces `high` with `highest`.
- The [risk_assessment.card_testing_risk.risk_level](https://docs.stripe.com/api/issuing/authorizations/object.md?api-version=2025-09-30.clover#issuing_authorization_object-risk_assessment-card_testing_risk-risk_level) field adds `low` as a new value. Existing authorisations with this field set to `high` will now show as `elevated` risk level.

## Changes

#### REST API

| Parameters | Change | Resources or endpoints |
| --- | --- | --- |
| `fraud_disputability_likelihood`, `risk_assessment` | Added | [Issuing.Authorization.testHelpers#create](/api/issuing/authorizations/test_mode_create?api-version=2025-09-30.clover#create_issuing_authorization) |

#### Ruby

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `fraud_disputability_likelihood`, `risk_assessment` | Added | [Issuing::Authorization::CreateParams](/api/issuing/authorizations/test_mode_create?api-version=2025-09-30.clover#create_issuing_authorization) |

#### Python

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `fraud_disputability_likelihood`, `risk_assessment` | Added | [issuing.Authorization.CreateParams](/api/issuing/authorizations/test_mode_create?api-version=2025-09-30.clover#create_issuing_authorization) |

#### PHP

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `fraud_disputability_likelihood`, `risk_assessment` | Added | [Issuing\Authorization.create().$params](/api/issuing/authorizations/test_mode_create?api-version=2025-09-30.clover#create_issuing_authorization) |

#### Java

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `fraudDisputabilityLikelihood`, `riskAssessment` | Added | [issuing.AuthorizationCreateParams](/api/issuing/authorizations/test_mode_create?api-version=2025-09-30.clover#create_issuing_authorization) |

#### Node.js

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `fraud_disputability_likelihood`, `risk_assessment` | Added | [Issuing.AuthorizationCreateParams.testHelpers](/api/issuing/authorizations/test_mode_create?api-version=2025-09-30.clover#create_issuing_authorization) |

#### Go

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `FraudDisputabilityLikelihood`, `RiskAssessment` | Added | [IssuingAuthorizationParams](/api/issuing/authorizations/test_mode_create?api-version=2025-09-30.clover#create_issuing_authorization) |

#### .NET

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `FraudDisputabilityLikelihood`, `RiskAssessment` | Added | [Issuing.TestHelpersAuthorizationCreateOptions](/api/issuing/authorizations/test_mode_create?api-version=2025-09-30.clover#create_issuing_authorization) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2025-09-30.clover`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to [v16.0.0](https://github.com/stripe/stripe-ruby/releases/tag/v16.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to [v13.0.1](https://github.com/stripe/stripe-python/releases/tag/v13.0.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to [v18.0.0](https://github.com/stripe/stripe-php/releases/tag/v18.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to [v30.0.0](https://github.com/stripe/stripe-java/releases/tag/v30.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to [v19.1.0](https://github.com/stripe/stripe-node/releases/tag/v19.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to [v83.0.0](https://github.com/stripe/stripe-go/releases/tag/v83.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to [v49.0.0](https://github.com/stripe/stripe-dotnet/releases/tag/v49.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).
