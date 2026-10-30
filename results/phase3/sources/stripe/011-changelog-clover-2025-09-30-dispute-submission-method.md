# Adds the ability to choose how you submit a dispute response

## What’s new

Specify how you plan to submit your response to a dispute by setting the [intended_submission_method](https://docs.stripe.com/api/disputes/object.md?api-version=2025-09-30.preview#dispute_object-intended_submission_method) parameter on a [Dispute](https://docs.stripe.com/api/disputes/object.md?api-version=2025-09-30.preview).

The options for `intended_submission_method` are:

- `manual`: You’ll submit the manual packet if you upload evidence and won’t ever use Smart Disputes to respond to the dispute.
- `prefer_manual`: You’ll submit the manual packet if you upload evidence, but use Smart Disputes if you have no evidence to add to the dispute response.
- `prefer_smart_disputes`: You’ll let Smart Disputes submit the dispute response if it detects Stripe evidence, but use the manual packet otherwise.
- `smart_disputes`: You’ll let Smart Disputes submit the dispute response if it detects Stripe evidence and won’t use the manual packet.

## Impact

Modify a dispute’s `intended_submission_method` to specify how you plan to submit your response to the dispute. This setting also impacts how Stripe behaves when a dispute reaches its due date. The value defaults to `prefer_manual`, which matches the timeout behaviour prior to adding the new parameter.

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `intended_submission_method` | Added | [Dispute](/api/disputes/object?api-version=2025-09-30.preview), [Dispute#update](/api/disputes/update?api-version=2025-09-30.preview) |

#### Ruby

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `intended_submission_method` | Added | [Dispute](/api/disputes/object?api-version=2025-09-30.preview), [Dispute::UpdateParams](/api/disputes/update?api-version=2025-09-30.preview) |

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `intended_submission_method` | Added | [Dispute](/api/disputes/object?api-version=2025-09-30.preview), [Dispute.ModifyParams](/api/disputes/update?api-version=2025-09-30.preview) |

#### PHP

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `intended_submission_method` | Added | [Dispute](/api/disputes/object?api-version=2025-09-30.preview), [Dispute.update().$params](/api/disputes/update?api-version=2025-09-30.preview) |

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `intendedSubmissionMethod` | Added | [Dispute](/api/disputes/object?api-version=2025-09-30.preview), [DisputeUpdateParams](/api/disputes/update?api-version=2025-09-30.preview) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `intended_submission_method` | Added | [Dispute](/api/disputes/object?api-version=2025-09-30.preview), [DisputeUpdateParams](/api/disputes/update?api-version=2025-09-30.preview) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `IntendedSubmissionMethod` | Added | [Dispute](/api/disputes/object?api-version=2025-09-30.preview), [DisputeParams](/api/disputes/update?api-version=2025-09-30.preview) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `IntendedSubmissionMethod` | Added | [Dispute](/api/disputes/object?api-version=2025-09-30.preview), [DisputeUpdateOptions](/api/disputes/update?api-version=2025-09-30.preview) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2025-09-30.preview`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to [v16.1.0-beta.1](https://github.com/stripe/stripe-ruby/releases/tag/v16.1.0-beta.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to [v13.1.2b1](https://github.com/stripe/stripe-python/releases/tag/v13.1.2b1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to [v18.1.0-beta.1](https://github.com/stripe/stripe-php/releases/tag/v18.1.0-beta.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to [v30.1.0-beta.1](https://github.com/stripe/stripe-java/releases/tag/v30.1.0-beta.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to [v19.2.0-beta.1](https://github.com/stripe/stripe-node/releases/tag/v19.2.0-beta.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to [v83.1.0-beta.1](https://github.com/stripe/stripe-go/releases/tag/v83.1.0-beta.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to [v49.1.0-beta.1](https://github.com/stripe/stripe-dotnet/releases/tag/v49.1.0-beta.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

## Related changes

- [Restructures Smart Disputes recommended evidence field](https://docs.stripe.com/changelog/clover/2025-09-30/restructure-smart-disputes-recommended-evidence.md)
- [Adds Outbound Setup Intents to create usable payout methods](https://docs.stripe.com/changelog/clover/2025-09-30/outbound-setup-intents.md)
- [Adds support for PayPay as a local payment method](https://docs.stripe.com/changelog/clover/2025-09-30/add-paypay-public-preview.md)
