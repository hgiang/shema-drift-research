# Extracts sex and place of birth from government-issued ID documents

## What’s new

Adds the `sex`, `unparsed_sex` and `unparsed_place_of_birth` fields to the [Verification Report](https://docs.stripe.com/api/identity/verification_reports/object.md?api-version=2025-05-28.basil) in the [document](https://docs.stripe.com/api/identity/verification_reports/object.md?api-version=2025-05-28.basil#identity_verification_report_object-document) section. If a document doesn’t contain this information, the corresponding value is null. For example, while passports usually include both sex and place of birth, a driver’s license might include sex but have a null value for `unparsed_place_of_birth`.

We recommend using `sex` because it’s parsed into an enum; however, you can use `unparsed_sex` if you need the raw value.

These fields are also available in the [Verification Session](https://docs.stripe.com/api/identity/verification_sessions.md?api-version=2025-05-28.basil) for the [last verification report](https://docs.stripe.com/api/identity/verification_sessions/object.md?api-version=2025-05-28.basil#identity_verification_session_object-last_verification_report) and in the [verified outputs](https://docs.stripe.com/api/identity/verification_sessions/object.md?api-version=2025-05-28.basil#identity_verification_session_object-verified_outputs).

Because these fields contain sensitive information, in order to retrieve them you need to use a [restricted API key](https://docs.stripe.com/identity/access-verification-results.md#create-restricted-key) and explicitly [expand them](https://docs.stripe.com/api/expanding_objects.md?api-version=2025-05-28.basil). For example, to retrieve the `sex` and `unparsed_place_of_birth` fields, follow the steps to [retrieve sensitive verification results](https://docs.stripe.com/identity/access-verification-results.md). The response might look like this:

```json
{
  "id": "vs_",
  "object": "identity.verification_session",
  ...
  "verified_outputs": {
    "first_name": "Jenny",
    "last_name": "Rosen",
    ...
    "sex": "female",
    "unparsed_place_of_birth": "U.S.A."
  }
}
```

## Impact

Platforms that need sex or place of birth information to fulfil additional KYC requirements, such as reporting them to an external agency, can now retrieve them using the [Identity API](https://docs.stripe.com/identity/verification-sessions.md).

## Changes

#### REST API

| Parameters | Change | Resources or endpoints |
| --- | --- | --- |
| `sex`, `unparsed_place_of_birth`, `unparsed_sex` | Added | [Identity.VerificationReport.document](/api/identity/verification_reports/object?api-version=2025-05-28.basil#identity_verification_report_object-document), [Identity.VerificationSession.verified_outputs](/api/identity/verification_sessions/object?api-version=2025-05-28.basil#identity_verification_session_object-verified_outputs) |

#### Ruby

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `sex`, `unparsed_place_of_birth`, `unparsed_sex` | Added | [Identity::VerificationReport::Document](/api/identity/verification_reports/object?api-version=2025-05-28.basil#identity_verification_report_object-document), [Identity::VerificationSession::VerifiedOutput](/api/identity/verification_sessions/object?api-version=2025-05-28.basil#identity_verification_session_object-verified_outputs) |

#### Python

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `sex`, `unparsed_place_of_birth`, `unparsed_sex` | Added | [Identity.VerificationReport.Document](/api/identity/verification_reports/object?api-version=2025-05-28.basil#identity_verification_report_object-document), [Identity.VerificationSession.VerifiedOutput](/api/identity/verification_sessions/object?api-version=2025-05-28.basil#identity_verification_session_object-verified_outputs) |

#### PHP

This change doesn’t affect the PHP SDK.

#### Java

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `sex`, `unparsedPlaceOfBirth`, `unparsedSex` | Added | [identity.VerificationReport.document](/api/identity/verification_reports/object?api-version=2025-05-28.basil#identity_verification_report_object-document), [identity.VerificationSession.verified_outputs](/api/identity/verification_sessions/object?api-version=2025-05-28.basil#identity_verification_session_object-verified_outputs) |

#### Node.js

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `sex`, `unparsed_place_of_birth`, `unparsed_sex` | Added | [Identity.VerificationReport.document](/api/identity/verification_reports/object?api-version=2025-05-28.basil#identity_verification_report_object-document), [Identity.VerificationSession.verified_outputs](/api/identity/verification_sessions/object?api-version=2025-05-28.basil#identity_verification_session_object-verified_outputs) |

#### Go

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `Sex`, `UnparsedPlaceOfBirth`, `UnparsedSex` | Added | [IdentityVerificationReportDocument](/api/identity/verification_reports/object?api-version=2025-05-28.basil#identity_verification_report_object-document), [IdentityVerificationSessionVerifiedOutputs](/api/identity/verification_sessions/object?api-version=2025-05-28.basil#identity_verification_session_object-verified_outputs) |

#### .NET

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `Sex`, `UnparsedPlaceOfBirth`, `UnparsedSex` | Added | [Identity.VerificationReport.Document](/api/identity/verification_reports/object?api-version=2025-05-28.basil#identity_verification_report_object-document), [Identity.VerificationSession.VerifiedOutputs](/api/identity/verification_sessions/object?api-version=2025-05-28.basil#identity_verification_session_object-verified_outputs) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2025-05-28.basil`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to [v15.2.0](https://github.com/stripe/stripe-ruby/releases/tag/v15.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to [v12.2.0](https://github.com/stripe/stripe-python/releases/tag/v12.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to [v17.3.0](https://github.com/stripe/stripe-php/releases/tag/v17.3.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to [v29.2.0](https://github.com/stripe/stripe-java/releases/tag/v29.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to [v18.2.0](https://github.com/stripe/stripe-node/releases/tag/v18.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to [v82.2.0](https://github.com/stripe/stripe-go/releases/tag/v82.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to [v48.2.0](https://github.com/stripe/stripe-dotnet/releases/tag/v48.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).
