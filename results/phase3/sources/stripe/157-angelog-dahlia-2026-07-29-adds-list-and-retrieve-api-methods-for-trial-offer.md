# Adds the ability to list and retrieve trial offers

## What’s new

Adds the ability to [list](https://docs.stripe.com/api/product-catalog/trial-offer/list.md?api-version=2026-07-29.preview) and [retrieve](https://docs.stripe.com/api/product-catalog/trial-offer/retrieve.md?api-version=2026-07-29.preview) your [Trial Offers](https://docs.stripe.com/api/product-catalog/trial-offer/object.md?api-version=2026-07-29.preview). You can list all Trial Offers with support for filtering by price and creation date, or retrieve a single Trial Offer by ID.

## Impact

You can now list all your Trial Offer objects or retrieve a single Trial Offer. For more information about using the Trial Offer API to manage free and paid introductory periods for subscriptions, see [Configure trial offers](https://docs.stripe.com/billing/subscriptions/trials.md).

## Changes

#### REST API

| Endpoints | Change | Resource |
| --- | --- | --- |
| `list`, `retrieve` | Added | [ProductCatalog.TrialOffer](/api/product-catalog/trial-offer/object?api-version=2026-07-29.preview#product_catalog_trial_offer_object) |

#### Ruby

| Methods | Change | Resource |
| --- | --- | --- |
| `list`, `retrieve` | Added | [ProductCatalog::TrialOffer](/api/product-catalog/trial-offer/object?api-version=2026-07-29.preview#product_catalog_trial_offer_object) |

#### Python

| Methods | Change | Resource |
| --- | --- | --- |
| `list`, `retrieve` | Added | [product_catalog.TrialOffer](/api/product-catalog/trial-offer/object?api-version=2026-07-29.preview#product_catalog_trial_offer_object) |

#### PHP

| Methods | Change | Resource |
| --- | --- | --- |
| `all`, `retrieve` | Added | [ProductCatalog.TrialOffer](/api/product-catalog/trial-offer/object?api-version=2026-07-29.preview#product_catalog_trial_offer_object) |

#### Java

| Methods | Change | Resource |
| --- | --- | --- |
| `list`, `retrieve` | Added | [productcatalog.TrialOffer](/api/product-catalog/trial-offer/object?api-version=2026-07-29.preview#product_catalog_trial_offer_object) |

#### Node.js

| Methods | Change | Resource |
| --- | --- | --- |
| `list`, `retrieve` | Added | [ProductCatalog.TrialOffer](/api/product-catalog/trial-offer/object?api-version=2026-07-29.preview#product_catalog_trial_offer_object) |

#### Go

| Methods | Change | Resource |
| --- | --- | --- |
| `Get`, `List` | Added | [ProductCatalogTrialOffer](/api/product-catalog/trial-offer/object?api-version=2026-07-29.preview#product_catalog_trial_offer_object) |

#### .NET

| Methods | Change | Resource |
| --- | --- | --- |
| `Get`, `List` | Added | [ProductCatalog.TrialOffer](/api/product-catalog/trial-offer/object?api-version=2026-07-29.preview#product_catalog_trial_offer_object) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2026-07-29.preview`
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
