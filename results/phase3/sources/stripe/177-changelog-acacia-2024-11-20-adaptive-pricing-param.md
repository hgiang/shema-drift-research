# Adds support for enabling Adaptive Pricing per Checkout Session

## What’s new

We added support for enabling and disabling [Adaptive Pricing](https://docs.stripe.com/payments/currencies/localize-prices/adaptive-pricing.md) per Checkout Session with a new API parameter. This parameter overrides your Adaptive Pricing [Dashboard setting](https://dashboard.stripe.com/settings/adaptive-pricing).

## Impact

With this parameter, you can enable Adaptive Pricing programmatically per session, allowing for incremental rollouts and granular control when working with multiple integrations.

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `adaptive_pricing` | Added | [Checkout.Session#create](/api/checkout/sessions/create?api-version=2024-11-20.acacia), [Checkout.Session](/api/checkout/sessions/object?api-version=2024-11-20.acacia) |

#### Ruby

This change doesn’t affect the Ruby SDK.

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `adaptive_pricing` | Added | [stripe.checkout.Session.CreateParams](/api/checkout/sessions/create?api-version=2024-11-20.acacia), [stripe.checkout.Session](/api/checkout/sessions/object?api-version=2024-11-20.acacia) |

#### PHP

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `adaptive_pricing` | Added | [Checkout.Session](/api/checkout/sessions/object?api-version=2024-11-20.acacia) |

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `adaptive_pricing` | Added | [Checkout.Session](/api/checkout/sessions/object?api-version=2024-11-20.acacia), [checkout.SessionCreateParams](/api/checkout/sessions/create?api-version=2024-11-20.acacia) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `adaptive_pricing` | Added | [Checkout.SessionCreateParams](/api/checkout/sessions/create?api-version=2024-11-20.acacia), [Checkout.Session](/api/checkout/sessions/object?api-version=2024-11-20.acacia) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `AdaptivePricing` | Added | [CheckoutSessionParams](/api/checkout/sessions/object?api-version=2024-11-20.acacia), [CheckoutSession](/api/checkout/sessions/object?api-version=2024-11-20.acacia) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `AdaptivePricing` | Added | [Checkout.SessionCreateOptions](/api/checkout/sessions/create?api-version=2024-11-20.acacia), [CheckoutSession](/api/checkout/sessions/object?api-version=2024-11-20.acacia) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2024-11-20.acacia`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to [v13.2.0](https://github.com/stripe/stripe-ruby/releases/tag/v13.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to [v11.3.0](https://github.com/stripe/stripe-python/releases/tag/v11.3.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to [v16.3.0](https://github.com/stripe/stripe-php/releases/tag/v16.3.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to [v28.1.0](https://github.com/stripe/stripe-java/releases/tag/v28.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to [v17.4.0](https://github.com/stripe/stripe-node/releases/tag/v17.4.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to [v81.1.0](https://github.com/stripe/stripe-go/releases/tag/v81.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to [v47.1.0](https://github.com/stripe/stripe-dotnet/releases/tag/v47.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

## Related changes

- [Customise the submit button recurring Payment Links and Checkout Sessions](https://docs.stripe.com/changelog/acacia/2024-11-20/submit-type-recurring-cpl.md)
- [Adds support for advanced card features on Checkout Sessions](https://docs.stripe.com/changelog/acacia/2024-11-20/advanced-card-features.md)
- [Allows Link card-only integrations to accept non-card payments under Link card brand](https://docs.stripe.com/changelog/acacia/2024-11-20/link-card-brand.md)
- [Adds additional beneficiary information for bank transfer payments](https://docs.stripe.com/changelog/acacia/2024-11-20/new-bank-transfer-beneficiary-information.md)
