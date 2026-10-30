# Adds a webhook event type for Invoices that require a non-Stripe payment

## What’s new

Adds the [invoice.payment_attempt_required](https://docs.stripe.com/api/events/types.md?api-version=2025-10-29.clover#event_types-invoice.payment_attempt_required) webhook event type. Stripe sends a webhook event when a finalised invoice requires payment through a custom payment method. Listen for this event to process off-Stripe payments when the Invoice’s [collection_method](https://docs.stripe.com/api/invoices/object.md?api-version=2025-10-29.clove#invoice_object-collection_method) is `charge_automatically`.

## Impact

You can now receive notifications when invoices require payment through third-party processors. When you receive this event, process the payment using your custom payment method integration and report the result back to Stripe using [Payment Records](https://docs.stripe.com/api/payment-record.md?api-version=2025-10-27.clover). That eliminates the need for manual polling when using off-Stripe payment methods with invoices that you charge automatically.

## Changes

#### REST API

| Values | Change | Enums |
| --- | --- | --- |
| `invoice.payment_attempt_required` | Added | [Event](/api/events/object?api-version=2025-10-29.clover#event_object-type) |
| `invoice.payment_attempt_required` | Added | [WebhookEndpoint#update](/api/webhook_endpoints/update?api-version=2025-10-29.clover#update_webhook_endpoint-enabled_events), [WebhookEndpoint#create](/api/webhook_endpoints/update?api-version=2025-10-29.clover#update_webhook_endpoint-enabled_events) |

|  | Change | Event type |
| --- | --- | --- |
| `invoice.payment_attempt_required` | Added | [Invoice](/api/invoices/object?api-version=2025-10-29.clover) |

#### Ruby

This change doesn’t affect the Ruby SDK.

#### Python

| Values | Change | Enums |
| --- | --- | --- |
| `invoice.payment_attempt_required` | Added | [Event](/api/events/object?api-version=2025-10-29.clover#event_object-type) |
| `invoice.payment_attempt_required` | Added | [WebhookEndpoint.ModifyParams](/api/webhook_endpoints/update?api-version=2025-10-29.clover#update_webhook_endpoint-enabled_events), [WebhookEndpoint.CreateParams](/api/webhook_endpoints/update?api-version=2025-10-29.clover#update_webhook_endpoint-enabled_events) |

|  | Change | Event type |
| --- | --- | --- |
| `invoice.payment_attempt_required` | Added | [Invoice](/api/invoices/object?api-version=2025-10-29.clover) |

#### PHP

| Value | Change | Enum |
| --- | --- | --- |
| `invoice.payment_attempt_required` | Added | [Event](/api/events/object?api-version=2025-10-29.clover#event_object-type) |

|  | Change | Event type |
| --- | --- | --- |
| `INVOICE_PAYMENT_ATTEMPT_REQUIRED` | Added | [Invoice](/api/invoices/object?api-version=2025-10-29.clover) |

#### Java

| Value | Change | Enums |
| --- | --- | --- |
| `invoice.payment_attempt_required` | Added | [WebhookEndpointUpdateParams](/api/webhook_endpoints/update?api-version=2025-10-29.clover#update_webhook_endpoint-enabledEvents), [WebhookEndpointCreateParams](/api/webhook_endpoints/update?api-version=2025-10-29.clover#update_webhook_endpoint-enabledEvents) |

|  | Change | Event type |
| --- | --- | --- |
| `invoice.payment_attempt_required` | Added | [Invoice](/api/invoices/object?api-version=2025-10-29.clover) |

#### Node.js

| Values | Change | Enums |
| --- | --- | --- |
| `invoice.payment_attempt_required` | Added | [Event](/api/events/object?api-version=2025-10-29.clover#event_object-type) |
| `invoice.payment_attempt_required` | Added | [WebhookEndpointUpdateParams](/api/webhook_endpoints/update?api-version=2025-10-29.clover#update_webhook_endpoint-enabled_events), [WebhookEndpointCreateParams](/api/webhook_endpoints/update?api-version=2025-10-29.clover#update_webhook_endpoint-enabled_events) |

|  | Change | Event type |
| --- | --- | --- |
| `InvoicePaymentAttemptRequiredEvent` | Added | [Invoice](/api/invoices/object?api-version=2025-10-29.clover) |

#### Go

| Value | Change | Enum |
| --- | --- | --- |
| `invoice.payment_attempt_required` | Added | [Event](/api/events/object?api-version=2025-10-29.clover#event_object-Type) |

|  | Change | Event type |
| --- | --- | --- |
| `EventTypeInvoicePaymentAttemptRequired` | Added | [Invoice](/api/invoices/object?api-version=2025-10-29.clover) |

#### .NET

|  | Change | Event type |
| --- | --- | --- |
| `InvoicePaymentAttemptRequired` | Added | [Invoice](/api/invoices/object?api-version=2025-10-29.clover) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2025-10-29.clover`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to [v17.1.0](https://github.com/stripe/stripe-ruby/releases/tag/v17.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to [v13.1.0](https://github.com/stripe/stripe-python/releases/tag/v13.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to [v18.1.0](https://github.com/stripe/stripe-php/releases/tag/v18.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to [v30.1.0](https://github.com/stripe/stripe-java/releases/tag/v30.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to [v19.2.0](https://github.com/stripe/stripe-node/releases/tag/v19.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to [v83.1.0](https://github.com/stripe/stripe-go/releases/tag/v83.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to [v49.1.0](https://github.com/stripe/stripe-dotnet/releases/tag/v49.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

## Related changes

- [Adds support for using Payment Records with Invoices and Credit Notes](https://docs.stripe.com/changelog/clover/2025-10-29/invoicing-payment-records.md)
- [Updates the category field of Credit Grants to be optional](https://docs.stripe.com/changelog/clover/2025-10-29/credit-grant-optional-category.md)
