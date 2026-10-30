# Adds support for submitting evidence to appeal a dispute decision

## What’s new

Adds the [appeal](https://docs.stripe.com/api/disputes/object.md?api-version=2026-09-30.preview#dispute_object-evidence-appeal) parameter to the [evidence](https://docs.stripe.com/api/disputes/object.md?api-version=2026-09-30.preview#dispute_object-evidence) hash on the [Dispute](https://docs.stripe.com/api/disputes/object.md?api-version=2026-09-30.preview) object. This parameter lets you stage or submit appeal evidence for eligible disputes.

Also adds two new enum values to the [status](https://docs.stripe.com/api/disputes/object.md?api-version=2026-09-30.preview#dispute_object-status) property for tracking the appeal lifecycle: `appeal_needs_response` and `appeal_under_review`.

## Impact

You can now submit appeal evidence by setting [reason_for_filing](https://docs.stripe.com/api/disputes/object.md?api-version=2026-09-30.preview#dispute_object-evidence-appeal-card-reason_for_filing) and [supporting_files](https://docs.stripe.com/api/disputes/object.md?api-version=2026-09-30.preview#dispute_object-evidence-appeal-card-supporting_files) when updating a Dispute. Use this feature only for eligible disputes with a [status](https://docs.stripe.com/api/disputes/object.md?api-version=2026-09-30.preview#dispute_object-status) of `appeal_needs_response`. You can’t update regular dispute evidence during the appeal stage.

To submit evidence immediately, either set the [submit](https://docs.stripe.com/api/disputes/update.md?api-version=2026-09-30.preview#update_dispute-submit) parameter to `true` or omit it (the default is `true`). To stage evidence without submitting it, set `submit=false`. You can stage the reason and supporting files separately, or submit them in the same request.

Before submitting, include a nonempty `reason_for_filing`. You can also include up to five supporting file IDs uploaded with the [dispute_evidence](https://docs.stripe.com/file-upload.md) purpose. After submission, the dispute status changes to `appeal_under_review` and appeal evidence can’t be updated. Use [charge.dispute.updated](https://docs.stripe.com/api/events/types.md?api-version=2026-09-30.preview#event_types-charge.dispute.updated) to detect appeal status changes and the evidence deadline. See [Appeal a dispute decision using the API](https://docs.stripe.com/disputes/arbitration.md#appeal-a-dispute-decision-using-the-api) for implementation details.

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `appeal` | Added | [Dispute#update.evidence](/api/disputes/update?api-version=2026-09-30.preview#update_dispute-evidence), [Dispute.evidence](/api/disputes/object?api-version=2026-09-30.preview#dispute_object-evidence) |

| Values | Change | Enum |
| --- | --- | --- |
| `appeal_needs_response`, `appeal_under_review` | Added | [Dispute.status](/api/disputes/object?api-version=2026-09-30.preview#dispute_object-status) |

#### Ruby

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `appeal` | Added | [Dispute::Evidence](/api/disputes/object?api-version=2026-09-30.preview#dispute_object-evidence), [DisputeUpdateParams::Evidence](/api/disputes/update?api-version=2026-09-30.preview#update_dispute-evidence) |

| Values | Change | Enum |
| --- | --- | --- |
| `appeal_needs_response`, `appeal_under_review` | Added | [Dispute.status](/api/disputes/object?api-version=2026-09-30.preview#dispute_object-status) |

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `appeal` | Added | [Dispute.Evidence](/api/disputes/object?api-version=2026-09-30.preview#dispute_object-evidence), [DisputeModifyParamsEvidence](/api/disputes/update?api-version=2026-09-30.preview#update_dispute-evidence) |

| Values | Change | Enum |
| --- | --- | --- |
| `appeal_needs_response`, `appeal_under_review` | Added | [Dispute.status](/api/disputes/object?api-version=2026-09-30.preview#dispute_object-status) |

#### PHP

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `appeal` | Added | [Dispute.evidence](/api/disputes/object?api-version=2026-09-30.preview#dispute_object-evidence), [Dispute.update().$params.evidence](/api/disputes/update?api-version=2026-09-30.preview#update_dispute-evidence) |

| Values | Change | Enum |
| --- | --- | --- |
| `appeal_needs_response`, `appeal_under_review` | Added | [Dispute.status](/api/disputes/object?api-version=2026-09-30.preview#dispute_object-status) |

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `appeal` | Added | [Dispute.evidence](/api/disputes/object?api-version=2026-09-30.preview#dispute_object-evidence), [DisputeUpdateParams.evidence](/api/disputes/update?api-version=2026-09-30.preview#update_dispute-evidence) |

| Values | Change | Enum |
| --- | --- | --- |
| `appeal_needs_response`, `appeal_under_review` | Added | [Dispute.status](/api/disputes/object?api-version=2026-09-30.preview#dispute_object-status) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `appeal` | Added | [Dispute.evidence](/api/disputes/object?api-version=2026-09-30.preview#dispute_object-evidence), [DisputeUpdateParams.evidence](/api/disputes/update?api-version=2026-09-30.preview#update_dispute-evidence) |

| Values | Change | Enum |
| --- | --- | --- |
| `appeal_needs_response`, `appeal_under_review` | Added | [Dispute.status](/api/disputes/object?api-version=2026-09-30.preview#dispute_object-status) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `Appeal` | Added | [DisputeEvidence](/api/disputes/object?api-version=2026-09-30.preview#dispute_object-evidence), [DisputeEvidenceParams](/api/disputes/update?api-version=2026-09-30.preview#update_dispute-evidence) |

| Values | Change | Enum |
| --- | --- | --- |
| `appeal_needs_response`, `appeal_under_review` | Added | [Dispute.Status](/api/disputes/object?api-version=2026-09-30.preview#dispute_object-status) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `Appeal` | Added | [Dispute.Evidence](/api/disputes/object?api-version=2026-09-30.preview#dispute_object-evidence), [DisputeEvidenceOptions](/api/disputes/update?api-version=2026-09-30.preview#update_dispute-evidence) |

| Values | Change | Enum |
| --- | --- | --- |
| `appeal_needs_response`, `appeal_under_review` | Added | [Dispute.Status](/api/disputes/object?api-version=2026-09-30.preview#dispute_object-status) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2026-09-30.preview`
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

## Related changes

- [Adds page limit validation for dispute evidence](https://docs.stripe.com/changelog/endive/2026-09-30/page-limit-validation-for-dispute-evidence.md)
- [Removes the capture method parameter for PayPay payments](https://docs.stripe.com/changelog/endive/2026-09-30/removes-capture-method-parameter-for-paypay-payments.md)
- [Adds the ability to update payment intent data on Checkout Sessions](https://docs.stripe.com/changelog/endive/2026-09-30/update-payment-intent-data-on-checkout-sessions.md)
- [Adds support for specifying card-on-file usage when saving and charging saved cards](https://docs.stripe.com/changelog/endive/2026-09-30/add-card-on-file-usage-indicators.md)
