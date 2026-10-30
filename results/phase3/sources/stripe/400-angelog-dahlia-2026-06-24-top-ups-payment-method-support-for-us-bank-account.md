# Adds payment method and payment method options to the Top-ups API (US bank accounts only)

## What’s new

Two optional parameters are now available on the [create a top-up](https://docs.stripe.com/api/topups/create.md?api-version=2026-06-24.dahlia) endpoint:

- [payment_method](https://docs.stripe.com/api/topups/create.md?api-version=2026-06-24.dahlia#create_topup-payment_method): The ID of a [PaymentMethod](https://docs.stripe.com/api/payment_methods.md?api-version=2026-06-24.dahlia) object to use for the top-up. Currently only supports `us_bank_account` payment method types.
- [payment_method_options](https://docs.stripe.com/api/topups/create.md?api-version=2026-06-24.dahlia#create_topup-payment_method_options): An object for payment method-specific configuration for the `us_bank_account` payment method type.

## Impact

You can now fund a top-up from a US bank account using the Payment Methods API. Pass a Payment Method object ID of type `us_bank_account` in the `payment_method` parameter when you create a top-up. Use `payment_method_options` to configure payment method-specific behaviour.

## Changes

#### REST API

| Parameters | Change | Resources or endpoints |
| --- | --- | --- |
| `payment_method`, `payment_method_options` | Added | [Topup#create](/api/topups/create?api-version=2026-06-24.dahlia#create_topup) |

#### Ruby

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `payment_method`, `payment_method_options` | Added | [TopupCreateParams](/api/topups/create?api-version=2026-06-24.dahlia#create_topup) |

#### Python

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `payment_method`, `payment_method_options` | Added | [TopupCreateParams](/api/topups/create?api-version=2026-06-24.dahlia#create_topup) |

#### PHP

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `payment_method`, `payment_method_options` | Added | [Topup.create().$params](/api/topups/create?api-version=2026-06-24.dahlia#create_topup) |

#### Java

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `paymentMethod`, `paymentMethodOptions` | Added | [TopupCreateParams](/api/topups/create?api-version=2026-06-24.dahlia#create_topup) |

#### Node.js

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `payment_method`, `payment_method_options` | Added | [TopupCreateParams](/api/topups/create?api-version=2026-06-24.dahlia#create_topup) |

#### Go

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `PaymentMethod`, `PaymentMethodOptions` | Added | [TopupParams](/api/topups/create?api-version=2026-06-24.dahlia#create_topup) |

#### .NET

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `PaymentMethod`, `PaymentMethodOptions` | Added | [TopupCreateOptions](/api/topups/create?api-version=2026-06-24.dahlia#create_topup) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2026-06-24.dahlia`
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
