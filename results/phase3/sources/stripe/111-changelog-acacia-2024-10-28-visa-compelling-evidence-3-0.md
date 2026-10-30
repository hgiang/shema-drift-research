# Uses Visa's Compelling Evidence 3.0 to respond to qualifying disputes

## What’s new

Adding a new [enhanced_evidence](https://docs.stripe.com/api/disputes/update.md?api-version=2024-10-28.acacia#update_dispute-evidence-enhanced_evidence) object to the [Dispute](https://docs.stripe.com/api/disputes.md?api-version=2024-10-28.acacia) resource allows you to [submit evidence](https://docs.stripe.com/api/disputes/update.md?api-version=2024-10-28.acacia#update_dispute-submit) using [Visa’s Compelling Evidence 3.0](https://docs.stripe.com/disputes/api/visa-ce3.md).

You can use the new [evidence_details.enhanced_eligibility](https://docs.stripe.com/api/disputes/object.md?api-version=2024-10-28.acacia#dispute_object-evidence_details-enhanced_eligibilitys) property to track [qualification](https://docs.stripe.com/disputes/api/visa-ce3.md#visa-qualifying-disputes).

## Impact

Submitting evidence using [Visa’s Compelling Evidence 3.0](https://docs.stripe.com/disputes/api/visa-ce3.md) typically results in an improved win rate for [qualifying disputes](https://docs.stripe.com/disputes/api/visa-ce3.md#visa-qualifying-disputes).

## Changes

#### REST API

| Parameters | Change | Resources or endpoints |
| --- | --- | --- |
| `enhanced_evidence` | Added | [Dispute#update.evidence](/api/disputes/update?api-version=2024-10-28.acacia#update_dispute-evidence), [Dispute.evidence](/api/disputes/object?api-version=2024-10-28.acacia#dispute_object-evidence) |
| `enhanced_eligibility_types` | Added | [Dispute](/api/disputes?api-version=2024-10-28.acacia) |
| `enhanced_eligibility` | Added | [Dispute.evidence_details](/api/disputes/object?api-version=2024-10-28.acacia#dispute_object-evidence_details) |

#### Ruby

This change doesn’t affect the Ruby SDK.

#### Python

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `enhanced_evidence` | Added | [stripe.Dispute.Evidence](/api/disputes/object?api-version=2024-10-28.acacia#dispute_object-evidence), [stripe.Dispute.ModifyParamsEvidence](/api/disputes/update?api-version=2024-10-28.acacia#update_dispute-evidence) |
| `enhanced_eligibility` | Added | [stripe.Dispute.EvidenceDetails](/api/disputes/object?api-version=2024-10-28.acacia#dispute_object-evidence_details) |
| `enhanced_eligibility_types` | Added | [stripe.Dispute](/api/disputes?api-version=2024-10-28.acacia) |

#### PHP

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `enhanced_eligibility_types` | Added | [Dispute](/api/disputes?api-version=2024-10-28.acacia) |

#### Java

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `enhanced_evidence` | Added | [Dispute.evidence](/api/disputes/object?api-version=2024-10-28.acacia#dispute_object-evidence), [DisputeUpdateParams.evidence](/api/disputes/update?api-version=2024-10-28.acacia#update_dispute-evidence) |
| `enhanced_eligibility_types` | Added | [Dispute](/api/disputes?api-version=2024-10-28.acacia) |
| `enhanced_eligibility` | Added | [Dispute.evidence_details](/api/disputes/object?api-version=2024-10-28.acacia#dispute_object-evidence_details) |

#### Node.js

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `enhanced_evidence` | Added | [Dispute.evidence](/api/disputes/object?api-version=2024-10-28.acacia#dispute_object-evidence), [DisputeUpdateParams.evidence](/api/disputes/update?api-version=2024-10-28.acacia#update_dispute-evidence) |
| `enhanced_eligibility_types` | Added | [Dispute](/api/disputes?api-version=2024-10-28.acacia) |
| `enhanced_eligibility` | Added | [Dispute.evidence_details](/api/disputes/object?api-version=2024-10-28.acacia#dispute_object-evidence_details) |

#### Go

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `EnhancedEvidence` | Added | [DisputeEvidenceParams](/api/disputes/update?api-version=2024-10-28.acacia#update_dispute-evidence), [DisputeEvidence](/api/disputes/object?api-version=2024-10-28.acacia#dispute_object-evidence) |
| `EnhancedEligibilityTypes` | Added | [Dispute](/api/disputes?api-version=2024-10-28.acacia) |
| `EnhancedEligibility` | Added | [DisputeEvidenceDetails](/api/disputes/object?api-version=2024-10-28.acacia#dispute_object-evidence_details) |

#### .NET

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `EnhancedEvidence` | Added | [DisputeEvidenceOptions](/api/disputes/update?api-version=2024-10-28.acacia#update_dispute-evidence), [DisputeEvidence](/api/disputes/object?api-version=2024-10-28.acacia#dispute_object-evidence) |
| `EnhancedEligibilityTypes` | Added | [Dispute](/api/disputes?api-version=2024-10-28.acacia) |
| `EnhancedEligibility` | Added | [DisputeEvidenceDetails](/api/disputes/object?api-version=2024-10-28.acacia#dispute_object-evidence_details) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2024-10-28.acacia`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to [v13.1.0](https://github.com/stripe/stripe-ruby/releases/tag/v13.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to [v11.2.0](https://github.com/stripe/stripe-python/releases/tag/v11.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to [v16.2.0](https://github.com/stripe/stripe-php/releases/tag/v16.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to [v28.0.0](https://github.com/stripe/stripe-java/releases/tag/v28.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to [v17.3.0](https://github.com/stripe/stripe-node/releases/tag/v17.3.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to [v81.0.0](https://github.com/stripe/stripe-go/releases/tag/v81.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to [v47.0.0](https://github.com/stripe/stripe-dotnet/releases/tag/v47.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).
