# Adds support for listing a payment method's mandates

## What’s new

Improves mandate listing in the API by providing the ability to:

- View a payment method’s latest active mandate with the [latest_active_mandate](https://docs.stripe.com/api/payment_methods/object.md?api-version=2025-08-27.preview#payment_method_object-latest_active_mandate) property.
- List all of a payment method’s attached mandates with [Mandates List](https://docs.stripe.com/api/mandates/list.md?api-version=2025-08-27.preview).

## Impact

These improvements provide more consistent access to mandates to help simplify your workflow. You can now view all of a payment method’s mandates by using the [Mandates List](https://docs.stripe.com/api/mandates/list.md?api-version=2025-08-27.preview) endpoint. You can also identify whether a mandate is attached to a payment method by using the [latest_active_mandate](https://docs.stripe.com/api/payment_methods/object.md?api-version=2025-08-27.preview#payment_method_object-latest_active_mandate) property.

## Changes

#### REST API

| Endpoint | Change | Resource |
| --- | --- | --- |
| `list` | Added | [Mandate](/api/mandates/list?api-version=2025-08-27.preview) |

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `latest_active_mandate` | Added | [PaymentMethod](/api/payment_methods/object?api-version=2025-08-27.preview) |

#### Ruby

| Method | Change | Resource |
| --- | --- | --- |
| `list` | Added | [Mandate](/api/mandates/list?api-version=2025-08-27.preview) |

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `latest_active_mandate` | Added | [PaymentMethod](/api/payment_methods/object?api-version=2025-08-27.preview) |

#### Python

| Method | Change | Resource |
| --- | --- | --- |
| `list` | Added | [Mandate](/api/mandates/list?api-version=2025-08-27.preview) |

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `latest_active_mandate` | Added | [PaymentMethod](/api/payment_methods/object?api-version=2025-08-27.preview) |

#### PHP

| Method | Change | Resource |
| --- | --- | --- |
| `all` | Added | [Mandate](/api/mandates/list?api-version=2025-08-27.preview) |

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `latest_active_mandate` | Added | [PaymentMethod](/api/payment_methods/object?api-version=2025-08-27.preview) |

#### Java

| Method | Change | Resource |
| --- | --- | --- |
| `list` | Added | [Mandate](/api/mandates/list?api-version=2025-08-27.preview) |

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `latestActiveMandate` | Added | [PaymentMethod](/api/payment_methods/object?api-version=2025-08-27.preview) |

#### Node.js

| Method | Change | Resource |
| --- | --- | --- |
| `list` | Added | [Mandate](/api/mandates/list?api-version=2025-08-27.preview) |

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `latest_active_mandate` | Added | [PaymentMethod](/api/payment_methods/object?api-version=2025-08-27.preview) |

#### Go

| Method | Change | Resource |
| --- | --- | --- |
| `List` | Added | [Mandate](/api/mandates/list?api-version=2025-08-27.preview) |

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `LatestActiveMandate` | Added | [PaymentMethod](/api/payment_methods/object?api-version=2025-08-27.preview) |

#### .NET

| Method | Change | Resource |
| --- | --- | --- |
| `List` | Added | [Mandate](/api/mandates/list?api-version=2025-08-27.preview) |

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `LatestActiveMandate` | Added | [PaymentMethod](/api/payment_methods/object?api-version=2025-08-27.preview) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2025-08-27.preview`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to [v15.6.0-beta.1](https://github.com/stripe/stripe-ruby/releases/tag/v15.6.0-beta.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to [v12.6.0b1](https://github.com/stripe/stripe-python/releases/tag/v12.6.0b1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to [v17.7.0-beta.1](https://github.com/stripe/stripe-php/releases/tag/v17.7.0-beta.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to [v29.6.0-beta.1](https://github.com/stripe/stripe-java/releases/tag/v29.6.0-beta.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to [v18.6.0-beta.1](https://github.com/stripe/stripe-node/releases/tag/v18.6.0-beta.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to [v82.6.0-beta.1](https://github.com/stripe/stripe-go/releases/tag/v82.6.0-beta.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to [v48.6.0-beta.1](https://github.com/stripe/stripe-dotnet/releases/tag/v48.6.0-beta.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).
