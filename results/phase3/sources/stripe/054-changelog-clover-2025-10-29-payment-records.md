# Adds Payment Records and Payment Attempt Records

## What’s new

Adds [PaymentRecords](https://docs.stripe.com/api/payment-record.md?api-version=2025-10-29.clover) and [PaymentAttemptRecords](https://docs.stripe.com/api/payment-attempt-record.md?api-version=2025-10-29.clover), which allow you to report payments processed outside of Stripe. They also enable features such as [subscriptions](https://docs.stripe.com/subscriptions.md) and [invoices](https://docs.stripe.com/invoicing.md) to work with payments processed through third-party payment processors.

## Impact

You can now use Payment Records to record payments processed through your own payment processor, enabling functionality such as the following:

- Use subscriptions and invoices [with payments that are processed outside of Stripe](https://docs.stripe.com/billing/subscriptions/third-party-payment-processing.md).
- Record external payments in Stripe so you can include them in your accounting and reporting.

## Changes

#### REST API

|  | Change | Resources |
| --- | --- | --- |
|  | Added | [PaymentAttemptRecord](/api/payment-attempt-record/object?api-version=2025-10-29.clover), [PaymentRecord](/api/payment-record/object?api-version=2025-10-29.clover) |

| Endpoints | Change | Resources |
| --- | --- | --- |
| `list`, `retrieve` | Added | [PaymentAttemptRecord](/api/payment-attempt-record/object?api-version=2025-10-29.clover) |
| `report_payment`, `report_payment_attempt`, `report_payment_attempt_canceled`, `report_payment_attempt_failed`, `report_payment_attempt_guaranteed`, `report_payment_attempt_informational`, `report_refund`, `retrieve` | Added | [PaymentRecord](/api/payment-record/object?api-version=2025-10-29.clover) |

#### Ruby

|  | Change | Resources |
| --- | --- | --- |
|  | Added | [PaymentAttemptRecord](/api/payment-attempt-record/object?api-version=2025-10-29.clover), [PaymentRecord](/api/payment-record/object?api-version=2025-10-29.clover) |

| Methods | Change | Resources |
| --- | --- | --- |
| `list`, `retrieve` | Added | [PaymentAttemptRecord](/api/payment-attempt-record/object?api-version=2025-10-29.clover) |
| `report_payment`, `report_payment_attempt`, `report_payment_attempt_canceled`, `report_payment_attempt_failed`, `report_payment_attempt_guaranteed`, `report_payment_attempt_informational`, `report_refund`, `retrieve` | Added | [PaymentRecord](/api/payment-record/object?api-version=2025-10-29.clover) |

#### Python

|  | Change | Resources |
| --- | --- | --- |
|  | Added | [PaymentAttemptRecord](/api/payment-attempt-record/object?api-version=2025-10-29.clover), [PaymentRecord](/api/payment-record/object?api-version=2025-10-29.clover) |

| Methods | Change | Resources |
| --- | --- | --- |
| `list`, `retrieve` | Added | [PaymentAttemptRecord](/api/payment-attempt-record/object?api-version=2025-10-29.clover) |
| `report_payment`, `report_payment_attempt`, `report_payment_attempt_canceled`, `report_payment_attempt_failed`, `report_payment_attempt_guaranteed`, `report_payment_attempt_informational`, `report_refund`, `retrieve` | Added | [PaymentRecord](/api/payment-record/object?api-version=2025-10-29.clover) |

#### PHP

|  | Change | Resources |
| --- | --- | --- |
|  | Added | [PaymentAttemptRecord](/api/payment-attempt-record/object?api-version=2025-10-29.clover), [PaymentRecord](/api/payment-record/object?api-version=2025-10-29.clover) |

| Methods | Change | Resources |
| --- | --- | --- |
| `all`, `retrieve` | Added | [PaymentAttemptRecord](/api/payment-attempt-record/object?api-version=2025-10-29.clover) |
| `report_payment`, `report_payment_attempt`, `report_payment_attempt_canceled`, `report_payment_attempt_failed`, `report_payment_attempt_guaranteed`, `report_payment_attempt_informational`, `report_refund`, `retrieve` | Added | [PaymentRecord](/api/payment-record/object?api-version=2025-10-29.clover) |

#### Java

|  | Change | Resources |
| --- | --- | --- |
|  | Added | [PaymentAttemptRecord](/api/payment-attempt-record/object?api-version=2025-10-29.clover), [PaymentRecord](/api/payment-record/object?api-version=2025-10-29.clover) |

| Methods | Change | Resources |
| --- | --- | --- |
| `list`, `retrieve` | Added | [PaymentAttemptRecord](/api/payment-attempt-record/object?api-version=2025-10-29.clover) |
| `report_payment`, `report_payment_attempt`, `report_payment_attempt_canceled`, `report_payment_attempt_failed`, `report_payment_attempt_guaranteed`, `report_payment_attempt_informational`, `report_refund`, `retrieve` | Added | [PaymentRecord](/api/payment-record/object?api-version=2025-10-29.clover) |

#### Node.js

|  | Change | Resources |
| --- | --- | --- |
|  | Added | [PaymentAttemptRecord](/api/payment-attempt-record/object?api-version=2025-10-29.clover), [PaymentRecord](/api/payment-record/object?api-version=2025-10-29.clover) |

| Methods | Change | Resources |
| --- | --- | --- |
| `list`, `retrieve` | Added | [PaymentAttemptRecord](/api/payment-attempt-record/object?api-version=2025-10-29.clover) |
| `report_payment`, `report_payment_attempt`, `report_payment_attempt_canceled`, `report_payment_attempt_failed`, `report_payment_attempt_guaranteed`, `report_payment_attempt_informational`, `report_refund`, `retrieve` | Added | [PaymentRecord](/api/payment-record/object?api-version=2025-10-29.clover) |

#### Go

|  | Change | Resources |
| --- | --- | --- |
|  | Added | [PaymentAttemptRecord](/api/payment-attempt-record/object?api-version=2025-10-29.clover), [PaymentRecord](/api/payment-record/object?api-version=2025-10-29.clover) |

| Methods | Change | Resources |
| --- | --- | --- |
| `Get`, `List` | Added | [PaymentAttemptRecord](/api/payment-attempt-record/object?api-version=2025-10-29.clover) |
| `Get`, `ReportPayment`, `ReportPaymentAttempt`, `ReportPaymentAttemptCanceled`, `ReportPaymentAttemptFailed`, `ReportPaymentAttemptGuaranteed`, `ReportPaymentAttemptInformational`, `ReportRefund` | Added | [PaymentRecord](/api/payment-record/object?api-version=2025-10-29.clover) |

#### .NET

|  | Change | Resources |
| --- | --- | --- |
|  | Added | [PaymentAttemptRecord](/api/payment-attempt-record/object?api-version=2025-10-29.clover), [PaymentRecord](/api/payment-record/object?api-version=2025-10-29.clover) |

| Methods | Change | Resources |
| --- | --- | --- |
| `Get`, `List` | Added | [PaymentAttemptRecord](/api/payment-attempt-record/object?api-version=2025-10-29.clover) |
| `Get`, `ReportPayment`, `ReportPaymentAttempt`, `ReportPaymentAttemptCanceled`, `ReportPaymentAttemptFailed`, `ReportPaymentAttemptGuaranteed`, `ReportPaymentAttemptInformational`, `ReportRefund` | Added | [PaymentRecord](/api/payment-record/object?api-version=2025-10-29.clover) |

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
