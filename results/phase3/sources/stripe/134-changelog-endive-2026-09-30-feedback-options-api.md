# Adds the Feedback Options API

## What’s new

Adds the [Billing Feedback Option](https://docs.stripe.com/api/billing/feedback-option.md?api-version=2026-09-30.endive) resource, which represents custom cancellation reasons for subscriptions.

You can [create](https://docs.stripe.com/api/billing/feedback-option/create.md?api-version=2026-09-30.endive), [retrieve](https://docs.stripe.com/api/billing/feedback-option/retrieve.md?api-version=2026-09-30.endive), [update](https://docs.stripe.com/api/billing/feedback-option/update.md?api-version=2026-09-30.endive), [list](https://docs.stripe.com/api/billing/feedback-option/list.md?api-version=2026-09-30.endive) and [deactivate](https://docs.stripe.com/api/billing/feedback-option/deactivate.md?api-version=2026-09-30.endive) feedback options. You can also configure feedback options on the [customer portal configuration](https://docs.stripe.com/api/customer_portal/configurations/object.md?api-version=2026-09-30.endive) to present them to customers cancelling through the portal.

## Impact

The Feedback Options API allows you to define custom cancellation reasons that subscribers can select when cancelling a subscription. Configure feedback options on your customer portal to present them during portal cancellation flows, enabling you to collect structured cancellation data and understand why customers are leaving.

## Changes

#### REST API

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [Billing.FeedbackOption](/api/billing/feedback-option/object?api-version=2026-09-30.endive) |

| Endpoints | Change | Resource |
| --- | --- | --- |
| `create`, `deactivate`, `list`, `retrieve`, `update` | Added | [Billing.FeedbackOption](/api/billing/feedback-option/object?api-version=2026-09-30.endive) |

| Code | Change |  |
| --- | --- | --- |
| `invalid_canceled_subscription_fields` | Added | `Invoice.last_finalization_error`, `PaymentIntent.last_payment_error`, `SetupAttempt.setup_error`, `SetupIntent.last_setup_error`, `StripeError`, `Terminal.Reader.action.api_error` |

#### Ruby

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [Billing::FeedbackOption](/api/billing/feedback-option/object?api-version=2026-09-30.endive) |

| Methods | Change | Resource |
| --- | --- | --- |
| `create`, `deactivate`, `list`, `retrieve`, `update` | Added | [Billing::FeedbackOption](/api/billing/feedback-option/object?api-version=2026-09-30.endive) |

#### Python

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [billing.FeedbackOption](/api/billing/feedback-option/object?api-version=2026-09-30.endive) |

| Methods | Change | Resource |
| --- | --- | --- |
| `create`, `deactivate`, `list`, `modify`, `retrieve` | Added | [billing.FeedbackOption](/api/billing/feedback-option/object?api-version=2026-09-30.endive) |

| Code | Change |  |
| --- | --- | --- |
| `invalid_canceled_subscription_fields` | Added | `Invoice.LastFinalizationError`, `PaymentIntent.LastPaymentError`, `SetupAttempt.SetupError`, `SetupIntent.LastSetupError`, `StripeError`, `Terminal.Reader.Action.ApiError` |

#### PHP

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [Billing.FeedbackOption](/api/billing/feedback-option/object?api-version=2026-09-30.endive) |

| Methods | Change | Resource |
| --- | --- | --- |
| `all`, `create`, `deactivate`, `retrieve`, `update` | Added | [Billing.FeedbackOption](/api/billing/feedback-option/object?api-version=2026-09-30.endive) |

| Code | Change |  |
| --- | --- | --- |
| `invalid_canceled_subscription_fields` | Added | `Invoice.last_finalization_error`, `PaymentIntent.last_payment_error`, `SetupAttempt.setup_error`, `SetupIntent.last_setup_error`, `StripeError`, `Terminal.Reader.action.api_error` |

#### Java

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [billing.FeedbackOption](/api/billing/feedback-option/object?api-version=2026-09-30.endive) |

| Methods | Change | Resource |
| --- | --- | --- |
| `create`, `deactivate`, `list`, `retrieve`, `update` | Added | [billing.FeedbackOption](/api/billing/feedback-option/object?api-version=2026-09-30.endive) |

#### Node.js

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [Billing.FeedbackOption](/api/billing/feedback-option/object?api-version=2026-09-30.endive) |

| Methods | Change | Resource |
| --- | --- | --- |
| `create`, `deactivate`, `list`, `retrieve`, `update` | Added | [Billing.FeedbackOption](/api/billing/feedback-option/object?api-version=2026-09-30.endive) |

| Code | Change |  |
| --- | --- | --- |
| `invalid_canceled_subscription_fields` | Added | `Invoice.last_finalization_error`, `PaymentIntent.last_payment_error`, `SetupAttempt.setup_error`, `SetupIntent.last_setup_error`, `StripeError`, `Terminal.Reader.action.api_error` |

#### Go

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [BillingFeedbackOption](/api/billing/feedback-option/object?api-version=2026-09-30.endive) |

| Methods | Change | Resource |
| --- | --- | --- |
| `Deactivate`, `Get`, `List`, `New`, `Update` | Added | [BillingFeedbackOption](/api/billing/feedback-option/object?api-version=2026-09-30.endive) |

| Code | Change |  |
| --- | --- | --- |
| `invalid_canceled_subscription_fields` | Added | `Error`, `InvoiceLastFinalizationError`, `PaymentIntentLastPaymentError`, `SetupAttemptSetupError`, `SetupIntentLastSetupError`, `StripeError`, `TerminalReaderActionApiError` |

#### .NET

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [Billing.FeedbackOption](/api/billing/feedback-option/object?api-version=2026-09-30.endive) |

| Methods | Change | Resource |
| --- | --- | --- |
| `Create`, `Deactivate`, `Get`, `List`, `Update` | Added | [Billing.FeedbackOption](/api/billing/feedback-option/object?api-version=2026-09-30.endive) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2026-09-30.endive`
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

- [Unifies the billing cycle anchor format across Subscriptions and Invoices](https://docs.stripe.com/changelog/endive/2026-09-30/polymorphic-billing-cycle-anchor.md)
- [Adds invoicing rules to Invoice Items](https://docs.stripe.com/changelog/endive/2026-09-30/invoicing-rules-for-invoice-items.md)
- [Adds reference and company details parameters for Billie](https://docs.stripe.com/changelog/endive/2026-09-30/reference-and-company-details-billie.md)
- [Adds the ability to clear invoicing rules on Invoice Items](https://docs.stripe.com/changelog/endive/2026-09-30/clear-invoicing-rules-on-invoice-items.md)
- [Adds proration details for Invoice Items using classic billing mode](https://docs.stripe.com/changelog/endive/2026-09-30/invoice-items-proration-details.md)
- [Makes trial offers generally available](https://docs.stripe.com/changelog/endive/2026-09-30/trial-offer-ga.md)
- [Adds detailed status to explain why an invoice is uncollectible](https://docs.stripe.com/changelog/endive/2026-09-30/invoice-uncollectible-status-detail.md)
- [Adds support for scheduling Subscription cancellation as part of pending update](https://docs.stripe.com/changelog/endive/2026-09-30/scheduled-subscription-cancellation.md)
- [Adds the ability to pause and resume Subscriptions on demand](https://docs.stripe.com/changelog/endive/2026-09-30/pause-subscription.md)
