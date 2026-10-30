# Adds a Canada financing disclaimer variant for Capital for Platforms

## What’s new

Adds `fundbox_ca_financing` as a supported value for the [disclaimer_variant](https://docs.stripe.com/api/capital/connect_financing_object.md?api-version=2026-09-30.preview#financing_offer_object-disclaimer_variant) property on the [Capital Financing Offer](https://docs.stripe.com/api/capital/connect_financing_object.md?api-version=2026-09-30.preview#financing_offer_object-disclaimer_variant) and [Capital Financing Summary](https://docs.stripe.com/api/capital/financing_summary_object.md?api-version=2026-09-30.preview#financing_summary_object-details-disclaimer_variant) objects. The new value identifies financing offers provided by Fundbox in Canada.

## Impact

Platforms onboarded for Fundbox financing in Canada can use `disclaimer_variant` to identify these offers and display the corresponding required financing disclaimer. Integrations that validate this property against a fixed set of values must accept `fundbox_ca_financing`.

## Changes

#### REST API

| Value | Change | Enums |
| --- | --- | --- |
| `fundbox_ca_financing` | Added | [Capital.FinancingOffer.disclaimer_variant](/api/capital/connect_financing_object?api-version=2026-09-30.preview#financing_offer_object-disclaimer_variant), [Capital.FinancingSummary.details.disclaimer_variant](/api/capital/financing_summary_object?api-version=2026-09-30.preview#financing_summary_object-details-disclaimer_variant) |

#### Ruby

This change doesn’t affect the Ruby SDK.

#### Python

| Value | Change | Enums |
| --- | --- | --- |
| `fundbox_ca_financing` | Added | [Capital.FinancingOffer.disclaimer_variant](/api/capital/connect_financing_object?api-version=2026-09-30.preview#financing_offer_object-disclaimer_variant), [Capital.FinancingSummary.Detail.disclaimer_variant](/api/capital/financing_summary_object?api-version=2026-09-30.preview#financing_summary_object-details-disclaimer_variant) |

#### PHP

| Value | Change | Enums |
| --- | --- | --- |
| `fundbox_ca_financing` | Added | [Capital.FinancingOffer.disclaimer_variant](/api/capital/connect_financing_object?api-version=2026-09-30.preview#financing_offer_object-disclaimer_variant), [Capital.FinancingSummary.details.disclaimer_variant](/api/capital/financing_summary_object?api-version=2026-09-30.preview#financing_summary_object-details-disclaimer_variant) |

#### Java

This change doesn’t affect the Java SDK.

#### Node.js

| Value | Change | Enums |
| --- | --- | --- |
| `fundbox_ca_financing` | Added | [Capital.FinancingOffer.disclaimer_variant](/api/capital/connect_financing_object?api-version=2026-09-30.preview#financing_offer_object-disclaimer_variant), [Capital.FinancingSummary.details.disclaimer_variant](/api/capital/financing_summary_object?api-version=2026-09-30.preview#financing_summary_object-details-disclaimer_variant) |

#### Go

| Value | Change | Enums |
| --- | --- | --- |
| `fundbox_ca_financing` | Added | [CapitalFinancingOffer.DisclaimerVariant](/api/capital/connect_financing_object?api-version=2026-09-30.preview#financing_offer_object-DisclaimerVariant), [CapitalFinancingSummaryDetails.DisclaimerVariant](/api/capital/financing_summary_object?api-version=2026-09-30.preview#financing_summary_object-details-DisclaimerVariant) |

#### .NET

This change doesn’t affect the .NET SDK.

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
