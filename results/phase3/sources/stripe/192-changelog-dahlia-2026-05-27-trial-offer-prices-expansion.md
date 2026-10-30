# Enables expansion of trial offer prices

## What’s new

You can now expand the [end_behavior.transition.price](https://docs.stripe.com/api/product-catalog/trial-offer/object.md?api-version=2026-05-27.preview#product_catalog_trial_offer_object-end_behavior-transition-price) property of [Trial Offers](https://docs.stripe.com/billing/subscriptions/trials.md). Previously, this property returned the price object’s ID as a string. With this change, you can now retrieve the full [Price](https://docs.stripe.com/api/prices/object.md?api-version=2026-05-27.preview) object by including `end_behavior.transition.price` in the [expand](https://docs.stripe.com/api/expanding_objects.md?api-version=2026-05-27.preview) parameter when creating or retrieving trial offers. Read more about [expanding responses](https://docs.stripe.com/expand.md).

## Impact

You can access complete pricing information without making separate API calls to retrieve Price objects on [trial offers](https://docs.stripe.com/billing/subscriptions/trials.md). When you expand the `price` property, you get immediate access to pricing details such as the amount, currency, billing interval and other Price object properties directly within the trial offer response.

To use this feature, include `end_behavior.transition.price` in the `expand` parameter when working with trial offers.

```curl
curl https://api.stripe.com/v1/product_catalog/trial_offers \
  -u "<<YOUR_SECRET_KEY>>:" \
  -H "Stripe-Version: 2026-05-27.preview" \
  -d "price={{PRICE_ID}}" \
  -d "duration[relative][iterations]=1" \
  -d "duration[type]=relative" \
  -d "end_behavior[transition][price]={{PRICE_ID}}" \
  -d "expand[]=end_behavior.transition.price"
```

If you don’t use the expand parameter, the field continues to return the price ID as a string, maintaining backward compatibility with existing integrations.

## Changes

#### REST API

| Field | Change | From → to |
| --- | --- | --- |
| `ProductCatalog.TrialOffer.end_behavior.transition.price` | Changed | `string → expandable($Price)` |

#### Ruby

| Field | Change | From → to |
| --- | --- | --- |
| `ProductCatalog::TrialOffer::EndBehavior::Transition.price` | Changed | `string → expandable($Price)` |

#### Python

| Field | Change | From → to |
| --- | --- | --- |
| `ProductCatalog.TrialOffer.EndBehavior.Transition.price` | Changed | `string → expandable($Price)` |

#### PHP

| Field | Change | From → to |
| --- | --- | --- |
| `ProductCatalog.TrialOffer.end_behavior.transition.price` | Changed | `string → expandable($Price)` |

#### Java

| Field | Change | From → to |
| --- | --- | --- |
| `productcatalog.TrialOffer.end_behavior.transition.price` | Changed | `string → expandable($Price)` |

#### Node.js

| Field | Change | From → to |
| --- | --- | --- |
| `ProductCatalog.TrialOffer.end_behavior.transition.price` | Changed | `string → expandable(Price)` |

#### Go

| Field | Change | From → to |
| --- | --- | --- |
| `ProductCatalogTrialOfferEndBehaviorTransition.Price` | Changed | `string → expandable($Price)` |

#### .NET

| Field | Change | From → to |
| --- | --- | --- |
| `ProductCatalog.TrialOffer.EndBehavior.Transition.Price` | Changed | `string → expandable($Price)` |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2026-05-27.preview`
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

- [Billed until property on subscription items is no longer included in responses by default](https://docs.stripe.com/changelog/dahlia/2026-05-27/subscription-item-billed-until-includable.md)
- [Adds the subscription pause endpoint](https://docs.stripe.com/changelog/dahlia/2026-05-27/pause-subscriptions.md)
