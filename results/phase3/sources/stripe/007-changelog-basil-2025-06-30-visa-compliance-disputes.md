# Adds Visa compliance disputes

## What’s new

[Visa compliance disputes](https://docs.stripe.com/disputes/api/visa-compliance.md) occur when card issuers believe transactions don’t conform to Visa’s network rules. If these disputes can’t be resolved between the parties, Visa resolves them for a fee.

This release adds Visa compliance disputes to the Stripe API. You can now determine if it’s a compliance dispute with the `payment_method_details.card.case_type` parameter. With this, the [enhanced_eligibility_types](https://docs.stripe.com/api/disputes/object.md?api-version=2025-06-30.basil#dispute_object-enhanced_eligibility_types) parameter now contains the `visa_compliance` value.

When contesting a Visa compliance dispute, Stripe collects a fee to cover the network costs in addition to the standard Stripe dispute fees. We refund this fee if you win the dispute.

## Impact

To contest a Visa compliance dispute, you must acknowledge the network fee by setting the `evidence.enhanced_evidence.visa_compliance.fee_acknowledged` parameter on the [Dispute](https://docs.stripe.com/api/disputes.md?api-version=2025-06-30.basil) to `true` when submitting dispute evidence.

After you acknowledge the fee, the `evidence_details.enhanced_eligibility.visa_compliance.status` value changes to `fee_acknowledged`.

Learn more about [responding to Visa compliance disputes](https://docs.stripe.com/disputes/api/visa-compliance.md#respond-to-visa-compliance-disputes-using-the-api).

## Changes

#### REST API

| Value | Change | Enum |
| --- | --- | --- |
| `compliance` | Added | [Dispute.payment_method_details.card.case_type](/api/disputes/object?api-version=2025-06-30.basil#dispute_object-payment_method_details-card-case_type) |

| Field | Change | From → to |
| --- | --- | --- |
| `Dispute.enhanced_eligibility_types` | Changed | [literal('visa_compelling_evidence_3') → enum('visa_compelling_evidence_3'|'visa_compliance')](/api/disputes/object?api-version=2025-06-30.basil#dispute_object-enhanced_eligibility_types) |

#### Ruby

| Field | Change | From → to |
| --- | --- | --- |
| `Dispute.enhanced_eligibility_types` | Changed | [literal('visa_compelling_evidence_3') → enum('visa_compelling_evidence_3'|'visa_compliance')](/api/disputes/object?api-version=2025-06-30.basil#dispute_object-enhanced_eligibility_types) |

#### Python

| Value | Change | Enum |
| --- | --- | --- |
| `compliance` | Added | [Dispute.PaymentMethodDetail.Card.case_type](/api/disputes/object?api-version=2025-06-30.basil#dispute_object-payment_method_details-card-case_type) |

| Field | Change | From → to |
| --- | --- | --- |
| `Dispute.enhanced_eligibility_types` | Changed | [literal('visa_compelling_evidence_3') → enum('visa_compelling_evidence_3'|'visa_compliance')](/api/disputes/object?api-version=2025-06-30.basil#dispute_object-enhanced_eligibility_types) |

#### PHP

| Field | Change | From → to |
| --- | --- | --- |
| `Dispute.enhanced_eligibility_types` | Changed | [literal('visa_compelling_evidence_3') → enum('visa_compelling_evidence_3'|'visa_compliance')](/api/disputes/object?api-version=2025-06-30.basil#dispute_object-enhanced_eligibility_types) |

#### Java

| Field | Change | From → to |
| --- | --- | --- |
| `Dispute.enhancedEligibilityTypes` | Changed | [literal('visa_compelling_evidence_3') → enum('visa_compelling_evidence_3'|'visa_compliance')](/api/disputes/object?api-version=2025-06-30.basil#dispute_object-enhanced_eligibility_types') |

#### Node.js

| Value | Change | Enum |
| --- | --- | --- |
| `compliance` | Added | [Dispute.payment_method_details.card.case_type](/api/disputes/object?api-version=2025-06-30.basil#dispute_object-payment_method_details-card-case_type) |

| Field | Change | From → to |
| --- | --- | --- |
| `Dispute.enhanced_eligibility_types` | Changed | [literal('visa_compelling_evidence_3') → enum('visa_compelling_evidence_3'|'visa_compliance')](/api/disputes/object?api-version=2025-06-30.basil#dispute_object-enhanced_eligibility_types) |

#### Go

| Value | Change | Enum |
| --- | --- | --- |
| `compliance` | Added | [DisputePaymentMethodDetailsCard.CaseType](/api/disputes/object?api-version=2025-06-30.basil#dispute_object-payment_method_details-card-case_type) |

| Field | Change | From → to |
| --- | --- | --- |
| `Dispute.EnhancedEligibilityTypes` | Changed | [literal('visa_compelling_evidence_3') → enum('visa_compelling_evidence_3'|'visa_compliance')](/api/disputes/object?api-version=2025-06-30.basil#dispute_object-enhanced_eligibility_types) |

#### .NET

| Field | Change | From → to |
| --- | --- | --- |
| `Dispute.EnhancedEligibilityTypes` | Changed | [literal('visa_compelling_evidence_3') → enum('visa_compelling_evidence_3'|'visa_compliance')](/api/disputes/object?api-version=2025-06-30.basil#dispute_object-enhanced_eligibility_types) |

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
