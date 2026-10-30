# Adds support for pre-tax credit amount information to credit notes

## What’s new

Adds `pretax_credit_amounts` attribute to the `CreditNote` and `CreditNoteLineItem` resources. This field contains information about billing credits, along with other pre-tax credits like discounts, that were applied to the original invoice for which a credit note was issued.

## Impact

You can now see a breakdown of credits applied to an invoice before tax calculations, including discounts. This information shows which credit notes were issued and how they relate to the invoice.

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `pretax_credit_amounts` | Added | [CreditNote](/api/credit_notes/object?api-version=2024-10-28.acacia), [CreditNoteLineItem](/api/credit_notes/line_item?api-version=2024-10-28.acacia) |

#### Ruby

This change doesn’t affect the Ruby SDK.

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `pretax_credit_amounts` | Added | [stripe.CreditNote](/api/credit_notes/object?api-version=2024-10-28.acacia), [stripe.CreditNoteLineItem](/api/credit_notes/line_item?api-version=2024-10-28.acacia) |

#### PHP

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `pretax_credit_amounts` | Added | [CreditNote](/api/credit_notes/object?api-version=2024-10-28.acacia), [CreditNoteLineItem](/api/credit_notes/line_item?api-version=2024-10-28.acacia) |

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `pretax_credit_amounts` | Added | [CreditNote](/api/credit_notes/object?api-version=2024-10-28.acacia), [CreditNoteLineItem](/api/credit_notes/line_item?api-version=2024-10-28.acacia) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `pretax_credit_amounts` | Added | [CreditNote](/api/credit_notes/object?api-version=2024-10-28.acacia), [CreditNoteLineItem](/api/credit_notes/line_item?api-version=2024-10-28.acacia) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `PretaxCreditAmounts` | Added | [CreditNote](/api/credit_notes/object?api-version=2024-10-28.acacia), [CreditNoteLineItem](/api/credit_notes/line_item?api-version=2024-10-28.acacia) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `PretaxCreditAmounts` | Added | [CreditNote](/api/credit_notes/object?api-version=2024-10-28.acacia), [CreditNoteLineItem](/api/credit_notes/line_item?api-version=2024-10-28.acacia) |

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

## Related changes

- [Adds Credit Grant APIs and resources](https://docs.stripe.com/changelog/acacia/2024-10-28/billing-credits-apis.md)
- [Adds support for pre-tax credit amount information to invoices](https://docs.stripe.com/changelog/acacia/2024-10-28/billing-credits-invoice.md)
