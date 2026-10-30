# Includes deleted prices in trial offer price data

## What’s new

Expands the [Trial Offer](https://docs.stripe.com/api/product-catalog/trial-offer.md?api-version=2026-08-26.preview) object’s [price](https://docs.stripe.com/api/product-catalog/trial-offer/object.md?api-version=2026-08-26.preview#product_catalog_trial_offer_object-price) property and [end_behavior.transition.price](https://docs.stripe.com/api/product-catalog/trial-offer/object.md?api-version=2026-08-26.preview#product_catalog_trial_offer_object-end_behavior-transition-price) property to return a deleted [Price](https://docs.stripe.com/api/prices/object.md?api-version=2026-08-26.preview) object when the referenced Price has been deleted. Previously, expanding either property when its referenced Price was deleted returned an error. When expanded, the property can now return a Price object with `deleted` set to `true`.

## Why is this a breaking change?

The `price` property on the Trial Offer object previously always returned a full Price object when expanded. It can now return a deleted Price object with `deleted` set to `true`. If your code assumes the expanded value is always a full Price object, you must update it to handle a deleted price.

## Impact

You can now view deleted price values when you expand the `price` property on a [Trial Offer](https://docs.stripe.com/api/product-catalog/trial-offer.md?api-version=2026-08-26.preview). Previously, expanding the `price` property on a Trial Offer with a deleted price returned an error. Update your integration to handle the case where the returned price has `deleted` set to `true`.

## Changes

#### REST API

| Fields | Change | From → to |
| --- | --- | --- |
| `ProductCatalog.TrialOffer.end_behavior.transition.price`, `ProductCatalog.TrialOffer.price` | Changed | `$Price → deletable($Price)` |

#### Ruby

| Fields | Change | From → to |
| --- | --- | --- |
| `ProductCatalog::TrialOffer.price`, `ProductCatalog::TrialOffer::EndBehavior::Transition.price` | Changed | `$Price → deletable($Price)` |

#### Python

| Fields | Change | From → to |
| --- | --- | --- |
| `ProductCatalog.TrialOffer.EndBehavior.Transition.price`, `ProductCatalog.TrialOffer.price` | Changed | `$Price → deletable($Price)` |

#### PHP

| Fields | Change | From → to |
| --- | --- | --- |
| `ProductCatalog.TrialOffer.end_behavior.transition.price`, `ProductCatalog.TrialOffer.price` | Changed | `$Price → deletable($Price)` |

#### Java

| Fields | Change | From → to |
| --- | --- | --- |
| `productcatalog.TrialOffer.end_behavior.transition.price`, `productcatalog.TrialOffer.price` | Changed | `$Price → deletable($Price)` |

#### Node.js

| Fields | Change | From → to |
| --- | --- | --- |
| `ProductCatalog.TrialOffer.end_behavior.transition.price`, `ProductCatalog.TrialOffer.price` | Changed | `Price → deletable($Price)` |

#### Go

| Fields | Change | From → to |
| --- | --- | --- |
| `ProductCatalogTrialOffer.Price`, `ProductCatalogTrialOfferEndBehaviorTransition.Price` | Changed | `$Price → deletable($Price)` |

#### .NET

| Fields | Change | From → to |
| --- | --- | --- |
| `ProductCatalog.TrialOffer.EndBehavior.Transition.Price`, `ProductCatalog.TrialOffer.Price` | Changed | `$Price → deletable($Price)` |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2026-08-26.preview`
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
