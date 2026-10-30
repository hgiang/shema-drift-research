# Adds fraud risk assessments to Issuing Authorisations

## What’s new

If you use [Radar](https://docs.stripe.com/issuing/controls/radar.md), [Issuing Authorisations](https://docs.stripe.com/api/issuing/authorizations.md?api-version=2025-11-17.clover) now include the GA version of the [risk_assessment.fraud_risk](https://docs.stripe.com/api/issuing/authorizations/object.md?api-version=2025-11-17.clover#issuing_authorization_object-risk_assessment-fraud_risk) property, which provides Stripe’s assessment of fraud likelihood for the authorisation.

The `risk_assessment.fraud_risk` property contains:

- [level](https://docs.stripe.com/api/issuing/authorizations/object.md?api-version=2025-11-17.clover#issuing_authorization_object-risk_assessment-fraud_risk-level): A string indicating the fraud risk level (`elevated`, `highest`, `low`, `normal`, `not_assessed`, or `unknown`).
- [score](https://docs.stripe.com/api/issuing/authorizations/object.md?api-version=2025-11-17.clover#issuing_authorization_object-risk_assessment-fraud_risk-score): A float representing the numerical fraud risk score.

This assessment helps you make informed decisions about whether to approve or decline authorisation requests based on Stripe’s fraud detection algorithms.

## Impact

You can access fraud risk information directly from the [Authorisation](https://docs.stripe.com/api/issuing/authorizations.md?api-version=2025-11-17.clover) object to enhance your fraud prevention strategies. The data is available immediately when you retrieve an Authorisation and you can use it to implement custom authorisation logic or monitoring workflows.

If you’re currently using the preview of Radar, this GA release differs in the following ways:

- We now provide an expanded set of possible risk levels.
- Fraud risk scores are floats instead of integers.
- Two fields have been renamed:
  - `risk_level` is now `level`
  - `fraud_score` is now `score`.

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `fraud_risk` | Added | [Issuing.Authorization.testHelpers#create.risk_assessment](/api/issuing/authorizations/test_mode_create?api-version=2025-11-17.clover#create_issuing_authorization-risk_assessment) |

#### Ruby

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `fraud_risk` | Added | [Issuing::AuthorizationCreateParams::RiskAssessment](/api/issuing/authorizations/test_mode_create?api-version=2025-11-17.clover#create_issuing_authorization-risk_assessment) |

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `fraud_risk` | Added | [issuing.AuthorizationCreateParamsRiskAssessment](/api/issuing/authorizations/test_mode_create?api-version=2025-11-17.clover#create_issuing_authorization-risk_assessment) |

#### PHP

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `fraud_risk` | Added | [Issuing\Authorization.create().$params.risk_assessment](/api/issuing/authorizations/test_mode_create?api-version=2025-11-17.clover#create_issuing_authorization-risk_assessment) |

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `fraudRisk` | Added | [issuing.AuthorizationCreateParams.risk_assessment](/api/issuing/authorizations/test_mode_create?api-version=2025-11-17.clover#create_issuing_authorization-risk_assessment) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `fraud_risk` | Added | [Issuing.AuthorizationCreateParams.testHelpers.risk_assessment](/api/issuing/authorizations/test_mode_create?api-version=2025-11-17.clover#create_issuing_authorization-risk_assessment) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `FraudRisk` | Added | [IssuingAuthorizationRiskAssessmentParams](/api/issuing/authorizations/test_mode_create?api-version=2025-11-17.clover#create_issuing_authorization-risk_assessment) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `FraudRisk` | Added | [IssuingAuthorizationRiskAssessmentOptions](/api/issuing/authorizations/test_mode_create?api-version=2025-11-17.clover#create_issuing_authorization-risk_assessment) |

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

- [Adds a fraud warning for potentially compromised Issuing Cards](https://docs.stripe.com/changelog/clover/2025-11-17/issuing-fraud-warnings.md)
