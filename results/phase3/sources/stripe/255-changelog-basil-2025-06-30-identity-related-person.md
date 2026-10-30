# Verification Sessions can now collect verification information for a related Person

## What’s new

Connect platforms can now use [Stripe Identity](https://docs.stripe.com/identity.md) to collect [required verification information](https://docs.stripe.com/connect/required-verification-information.md), such as the `document` or `proof_of_liveness` for a [Person](https://docs.stripe.com/api/persons.md?api-version=2025-06-30.basil), while onboarding a connected account.

## Impact

When [creating a VerificationSession](https://docs.stripe.com/api/identity/verification_sessions/create.md?api-version=2025-06-30.basil), use the [related_person](https://docs.stripe.com/api/identity/verification_sessions/object.md?api-version=2025-06-30.basil#identity_verification_session_object-related_person) parameter to associate the session with a person from one of your connected accounts who’s required to provide a `document` or `proof_of_liveness`.

After Stripe completes verification, collected data is attached to the associated person, fulfilling all unmet requirements.

## Changes

#### REST API

| Parameters | Change | Resources or endpoints |
| --- | --- | --- |
| `related_person` | Added | [Identity.VerificationSession](/api/identity/verification_sessions/object?api-version=2025-06-30.basil), [Identity.VerificationSession#create](/api/identity/verification_sessions/create?api-version=2025-06-30.basil) |
| `matching` | Added | [Identity.VerificationSession.options](/api/identity/verification_sessions/object?api-version=2025-06-30.basil#identity_verification_session_object-options) |

#### Ruby

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `related_person` | Added | [Identity::VerificationSession](/api/identity/verification_sessions/object?api-version=2025-06-30.basil), [Identity::VerificationSession::CreateParams](/api/identity/verification_sessions/create?api-version=2025-06-30.basil) |
| `matching` | Added | [Identity::VerificationSession::Option](/api/identity/verification_sessions/object?api-version=2025-06-30.basil#identity_verification_session_object-options) |

#### Python

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `related_person` | Added | [Identity.VerificationSession](/api/identity/verification_sessions/object?api-version=2025-06-30.basil), [identity.VerificationSession.CreateParams](/api/identity/verification_sessions/create?api-version=2025-06-30.basil) |
| `matching` | Added | [Identity.VerificationSession.Option](/api/identity/verification_sessions/object?api-version=2025-06-30.basil#identity_verification_session_object-options) |

#### PHP

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `related_person` | Added | [Identity.VerificationSession](/api/identity/verification_sessions/object?api-version=2025-06-30.basil) |
| `matching` | Added | [Identity.VerificationSession.options](/api/identity/verification_sessions/object?api-version=2025-06-30.basil#identity_verification_session_object-options) |

#### Java

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `relatedPerson` | Added | [identity.VerificationSession](/api/identity/verification_sessions/object?api-version=2025-06-30.basil), [identity.VerificationSessionCreateParams](/api/identity/verification_sessions/create?api-version=2025-06-30.basil) |
| `matching` | Added | [identity.VerificationSession.options](/api/identity/verification_sessions/object?api-version=2025-06-30.basil#identity_verification_session_object-options) |

#### Node.js

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `related_person` | Added | [Identity.VerificationSession](/api/identity/verification_sessions/object?api-version=2025-06-30.basil), [Identity.VerificationSessionCreateParams](/api/identity/verification_sessions/create?api-version=2025-06-30.basil) |
| `matching` | Added | [Identity.VerificationSession.options](/api/identity/verification_sessions/object?api-version=2025-06-30.basil#identity_verification_session_object-options) |

#### Go

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `RelatedPerson` | Added | [IdentityVerificationSession](/api/identity/verification_sessions/object?api-version=2025-06-30.basil), [IdentityVerificationSessionParams](/api/identity/verification_sessions/create?api-version=2025-06-30.basil) |
| `Matching` | Added | [IdentityVerificationSessionOptions](/api/identity/verification_sessions/object?api-version=2025-06-30.basil#identity_verification_session_object-options) |

#### .NET

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `RelatedPerson` | Added | [Identity.VerificationSession](/api/identity/verification_sessions/object?api-version=2025-06-30.basil), [Identity.VerificationSessionCreateOptions](/api/identity/verification_sessions/create?api-version=2025-06-30.basil) |
| `Matching` | Added | [Identity.VerificationSession.Options](/api/identity/verification_sessions/object?api-version=2025-06-30.basil#identity_verification_session_object-options) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2025-06-30.basil`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to [v15.3.0](https://github.com/stripe/stripe-ruby/releases/tag/v15.3.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to [v12.3.0](https://github.com/stripe/stripe-python/releases/tag/v12.3.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to [v17.4.0](https://github.com/stripe/stripe-php/releases/tag/v17.4.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to [v29.3.0](https://github.com/stripe/stripe-java/releases/tag/v29.3.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to [v18.3.0](https://github.com/stripe/stripe-node/releases/tag/v18.3.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to [v82.3.0](https://github.com/stripe/stripe-go/releases/tag/v82.3.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to [v48.3.0](https://github.com/stripe/stripe-dotnet/releases/tag/v48.3.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

## Related changes

- [Adds the ability to provide proof-of-address documents for connected accounts](https://docs.stripe.com/changelog/basil/2025-06-30/accounts-proof-of-address.md)
- [Adds more flexible schedules for monthly and weekly payouts](https://docs.stripe.com/changelog/basil/2025-06-30/flexible-schedules-payouts.md)
