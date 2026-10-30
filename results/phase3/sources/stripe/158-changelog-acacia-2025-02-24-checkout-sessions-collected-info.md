# Checkout Sessions now group customer information in one field

## What’s new

Adds the [collected_information](https://docs.stripe.com/api/checkout/sessions/object.md?api-version=2025-02-24.acacia#checkout_session_object-collected_information) object to group information about the customer collected within the Checkout Session.

## Impact

The [shipping_details](https://docs.stripe.com/api/checkout/sessions/object.md?api-version=2025-02-24.acacia#checkout_session_object-collected_information-shipping_details) property is now available in the `collected_information` object. This enables support for [dynamically updating shipping options in Checkout](https://docs.stripe.com/payments/checkout/custom-shipping-options.md).

We plan to remove the legacy [shipping_details](https://docs.stripe.com/api/checkout/sessions/object.md?api-version=2025-02-24.acacia#checkout_session_object-shipping_details) field from the Checkout Session resource in a future release. To prepare, update your integration to replace any references to `shipping_details` with `collected_information.shipping_details`.

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `collected_information` | Added | `Checkout.Session#update`, [Checkout.Session](/api/checkout/sessions/object?api-version=2025-02-24.acacia) |

#### Ruby

This change doesn’t affect the Ruby SDK.

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `collected_information` | Added | `stripe.checkout.Session.ModifyParams`, [stripe.checkout.Session](/api/checkout/sessions/object?api-version=2025-02-24.acacia) |

#### PHP

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `collected_information` | Added | [Checkout.Session](/api/checkout/sessions/object?api-version=2025-02-24.acacia) |

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `collected_information` | Added | [Checkout.Session](/api/checkout/sessions/object?api-version=2025-02-24.acacia), `checkout.SessionUpdateParams` |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `collected_information` | Added | `Checkout.SessionUpdateParams`, [Checkout.Session](/api/checkout/sessions/object?api-version=2025-02-24.acacia) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `CollectedInformation` | Added | [CheckoutSessionParams](/api/checkout/sessions/object?api-version=2025-02-24.acacia), [CheckoutSession](/api/checkout/sessions/object?api-version=2025-02-24.acacia) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `CollectedInformation` | Added | `Checkout.SessionUpdateOptions`, [CheckoutSession](/api/checkout/sessions/object?api-version=2025-02-24.acacia) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2025-02-24.acacia`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to [v13.5.0](https://github.com/stripe/stripe-ruby/releases/tag/v13.5.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to [v11.6.0](https://github.com/stripe/stripe-python/releases/tag/v11.6.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to [v16.6.0](https://github.com/stripe/stripe-php/releases/tag/v16.6.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to [v28.4.0](https://github.com/stripe/stripe-java/releases/tag/v28.4.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to [v17.7.0](https://github.com/stripe/stripe-node/releases/tag/v17.7.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to [v81.4.0](https://github.com/stripe/stripe-go/releases/tag/v81.4.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to [v47.4.0](https://github.com/stripe/stripe-dotnet/releases/tag/v47.4.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

## Related changes

- [Adds support for blocking specific card brands in Checkout Sessions](https://docs.stripe.com/changelog/acacia/2025-02-24/checkout_add_brands_blocked.md)
