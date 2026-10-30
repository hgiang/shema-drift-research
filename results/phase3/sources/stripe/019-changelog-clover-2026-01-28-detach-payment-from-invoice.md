# Adds the ability to detach a PaymentIntent from an Invoice

## What’s new

You can now detach a [PaymentIntent](https://docs.stripe.com/api/payment_intents.md?api-version=2026-01-28.preview) from an [Invoice](https://docs.stripe.com/api/invoices.md?api-version=2026-01-28.preview) using the new [detach payment](https://docs.stripe.com/api/invoices/detach_payment.md?api-version=2026-01-28.preview) API method. When you detach a payment from an invoice, the PaymentIntent becomes available for use with other invoices or payment flows, and the invoice returns to an unpaid state.

When you detach a payment, Stripe generates an [invoice_payment.detached](https://docs.stripe.com/api/events/types.md?api-version=2026-01-28.preview#event_types-invoice_payment.detached) event.

## Impact

You can now detach a payment from an invoice, allowing you to reopen paid invoices. This provides more flexibility in managing payment and reconciliation flows.

Detaching a payment reopens an invoice if it creates an unpaid balance, transitioning the invoice’s [status](https://docs.stripe.com/api/invoices/object.md?api-version=2026-01-28.preview#invoice_object-status) from `paid` to `open`. Stripe automatically generates a new default PaymentIntent for the remaining amount.

## Changes

#### REST API

| Endpoint | Change | Resource |
| --- | --- | --- |
| `detach_payment` | Added | [Invoice](/api/invoices/object?api-version=2026-01-28.preview) |

|  | Change | Event type |
| --- | --- | --- |
| `invoice_payment.detached` | Added | `InvoicePayment` |

#### Ruby

| Method | Change | Resource |
| --- | --- | --- |
| `detach_payment` | Added | [Invoice](/api/invoices/object?api-version=2026-01-28.preview) |

#### Python

| Method | Change | Resource |
| --- | --- | --- |
| `detach_payment` | Added | [Invoice](/api/invoices/object?api-version=2026-01-28.preview) |

|  | Change | Event type |
| --- | --- | --- |
| `invoice_payment.detached` | Added | `InvoicePayment` |

#### PHP

| Method | Change | Resource |
| --- | --- | --- |
| `detach_payment` | Added | [Invoice](/api/invoices/object?api-version=2026-01-28.preview) |

|  | Change | Event type |
| --- | --- | --- |
| `INVOICE_PAYMENT_DETACHED` | Added | `InvoicePayment` |

#### Java

| Method | Change | Resource |
| --- | --- | --- |
| `detach_payment` | Added | [Invoice](/api/invoices/object?api-version=2026-01-28.preview) |

|  | Change | Event type |
| --- | --- | --- |
| `invoice_payment.detached` | Added | `InvoicePayment` |

#### Node.js

| Method | Change | Resource |
| --- | --- | --- |
| `detach_payment` | Added | [Invoice](/api/invoices/object?api-version=2026-01-28.preview) |

|  | Change | Event type |
| --- | --- | --- |
| `InvoicePaymentDetachedEvent` | Added | `InvoicePayment` |

#### Go

| Method | Change | Resource |
| --- | --- | --- |
| `DetachPayment` | Added | [Invoice](/api/invoices/object?api-version=2026-01-28.preview) |

|  | Change | Event type |
| --- | --- | --- |
| `EventTypeInvoicePaymentDetached` | Added | `InvoicePayment` |

#### .NET

| Method | Change | Resource |
| --- | --- | --- |
| `DetachPayment` | Added | [Invoice](/api/invoices/object?api-version=2026-01-28.preview) |

|  | Change | Event type |
| --- | --- | --- |
| `InvoicePaymentDetached` | Added | `InvoicePayment` |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2026-01-28.preview`
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
