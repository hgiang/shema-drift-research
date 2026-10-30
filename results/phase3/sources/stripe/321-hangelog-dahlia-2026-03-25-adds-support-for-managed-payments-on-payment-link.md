# Adds support for Managed Payments on payment links

## What’s new

Adds support for [Managed Payments](https://docs.stripe.com/payments/managed-payments.md), where Stripe acts as the merchant of record for digital products, when using [payment links](https://docs.stripe.com/payment-links.md). When you create a payment link, enable Managed Payments by setting the new [managed_payments.enabled](https://docs.stripe.com/api/payment_links/create.md?api-version=2026-03-25.preview#create_payment_link-managed_payments-enabled) parameter to true.

## Impact

You can now use Managed Payments to sell digital products through payment links.

You can create payment links with Managed Payments enabled [in the Dashboard](https://dashboard.stripe.com/payment-links/create) or using [the Payment Links API](https://docs.stripe.com/api/payment_links.md?api-version=2026-03-25.preview).

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `managed_payments` | Added | [PaymentLink](/api/payment-link/object?api-version=2026-03-25.preview), [PaymentLink#create](/api/payment-link/create?api-version=2026-03-25.preview) |

#### Ruby

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `managed_payments` | Added | [PaymentLink](/api/payment-link/object?api-version=2026-03-25.preview), [PaymentLinkCreateParams](/api/payment-link/create?api-version=2026-03-25.preview) |

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `managed_payments` | Added | [PaymentLink](/api/payment-link/object?api-version=2026-03-25.preview), [PaymentLinkCreateParams](/api/payment-link/create?api-version=2026-03-25.preview) |

#### PHP

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `managed_payments` | Added | [PaymentLink](/api/payment-link/object?api-version=2026-03-25.preview), [PaymentLink.create().$params](/api/payment-link/create?api-version=2026-03-25.preview) |

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `managedPayments` | Added | [PaymentLink](/api/payment-link/object?api-version=2026-03-25.preview), [PaymentLinkCreateParams](/api/payment-link/create?api-version=2026-03-25.preview) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `managed_payments` | Added | [PaymentLink](/api/payment-link/object?api-version=2026-03-25.preview), [PaymentLinkCreateParams](/api/payment-link/create?api-version=2026-03-25.preview) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `ManagedPayments` | Added | [PaymentLink](/api/payment-link/object?api-version=2026-03-25.preview), [PaymentLinkParams](/api/payment-link/create?api-version=2026-03-25.preview) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `ManagedPayments` | Added | [PaymentLink](/api/payment-link/object?api-version=2026-03-25.preview), [PaymentLinkCreateOptions](/api/payment-link/create?api-version=2026-03-25.preview) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2026-03-25.preview`
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
