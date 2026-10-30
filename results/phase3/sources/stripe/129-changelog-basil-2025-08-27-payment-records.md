# Additional properties on PaymentRecord and PaymentAttemptRecord

## What’s new

Makes the following changes to the `PaymentAttemptRecord` and `PaymentRecord` resources:

- Adds support for storing and reading amounts using the new `amount`, `amount_authorized` and `amount_refunded` properties.
- Adds support for storing and reading processor details using the new `processor_details` property.
- Removes support for storing and reading a top-level payment reference by removing the `payment_reference` property. This is replaced by `processor_details.custom.payment_reference`.

## Impact

Preview users of the Payment Records API can now use the following properties of the `PaymentAttemptRecord` and `PaymentRecord` resources:

- `amount`
- `amount_authorized`
- `amount_refunded`
- `processor_details`

Preview users of the Payment Records API can now use the `processor_details` parameter on the `report_payment` method.

Preview users of the Payment Records API can no longer use the top-level `payment_reference` property of the `PaymentAttemptRecord` and `PaymentRecord` resources. However, you can still use it with the `payment_records_beta=v1` header.

## Changes

#### REST API

| Parameters | Change | Resources or endpoints |
| --- | --- | --- |
| `amount`, `amount_authorized`, `amount_refunded`, `application` | Added | [PaymentAttemptRecord](/api/payment-attempt-record/object?api-version=2025-08-27.preview), [PaymentRecord](/api/payment-record/object?api-version=2025-08-27.preview) |
| `processor_details` | Added | [PaymentAttemptRecord](/api/payment-attempt-record/object?api-version=2025-08-27.preview), [PaymentRecord](/api/payment-record/object?api-version=2025-08-27.preview), [PaymentRecord#report_payment](/api/payment-record/report-payment/report?api-version=2025-08-27.preview) |
| `payment_reference` | Removed | [PaymentAttemptRecord](/api/payment-attempt-record/object?api-version=2025-08-27.preview), [PaymentRecord](/api/payment-record/object?api-version=2025-08-27.preview), [PaymentRecord#report_payment](/api/payment-record/report-payment/report?api-version=2025-08-27.preview) |

#### Ruby

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `amount`, `amount_authorized`, `amount_refunded`, `application` | Added | [PaymentAttemptRecord](/api/payment-attempt-record/object?api-version=2025-08-27.preview), [PaymentRecord](/api/payment-record/object?api-version=2025-08-27.preview) |
| `processor_details` | Added | [PaymentAttemptRecord](/api/payment-attempt-record/object?api-version=2025-08-27.preview), [PaymentRecord](/api/payment-record/object?api-version=2025-08-27.preview), [PaymentRecord::ReportPaymentParams](/api/payment-record/report-payment/report?api-version=2025-08-27.preview) |
| `payment_reference` | Removed | [PaymentAttemptRecord](/api/payment-attempt-record/object?api-version=2025-08-27.preview), [PaymentRecord](/api/payment-record/object?api-version=2025-08-27.preview), [PaymentRecord::ReportPaymentParams](/api/payment-record/report-payment/report?api-version=2025-08-27.preview) |

#### Python

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `amount`, `amount_authorized`, `amount_refunded`, `application` | Added | [PaymentAttemptRecord](/api/payment-attempt-record/object?api-version=2025-08-27.preview), [PaymentRecord](/api/payment-record/object?api-version=2025-08-27.preview) |
| `processor_details` | Added | [PaymentAttemptRecord](/api/payment-attempt-record/object?api-version=2025-08-27.preview), [PaymentRecord](/api/payment-record/object?api-version=2025-08-27.preview), [PaymentRecord.ReportPaymentParams](/api/payment-record/report-payment/report?api-version=2025-08-27.preview) |
| `payment_reference` | Removed | [PaymentAttemptRecord](/api/payment-attempt-record/object?api-version=2025-08-27.preview), [PaymentRecord](/api/payment-record/object?api-version=2025-08-27.preview), [PaymentRecord.ReportPaymentParams](/api/payment-record/report-payment/report?api-version=2025-08-27.preview) |

#### PHP

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `amount`, `amount_authorized`, `amount_refunded`, `application`, `processor_details` | Added | [PaymentAttemptRecord](/api/payment-attempt-record/object?api-version=2025-08-27.preview), [PaymentRecord](/api/payment-record/object?api-version=2025-08-27.preview) |
| `payment_reference` | Removed | [PaymentAttemptRecord](/api/payment-attempt-record/object?api-version=2025-08-27.preview), [PaymentRecord](/api/payment-record/object?api-version=2025-08-27.preview) |

#### Java

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `amount`, `amountAuthorized`, `amountRefunded`, `application` | Added | [PaymentAttemptRecord](/api/payment-attempt-record/object?api-version=2025-08-27.preview), [PaymentRecord](/api/payment-record/object?api-version=2025-08-27.preview) |
| `processorDetails` | Added | [PaymentAttemptRecord](/api/payment-attempt-record/object?api-version=2025-08-27.preview), [PaymentRecord](/api/payment-record/object?api-version=2025-08-27.preview), [PaymentRecordReportPaymentParams](/api/payment-record/report-payment/report?api-version=2025-08-27.preview) |
| `paymentReference` | Removed | [PaymentAttemptRecord](/api/payment-attempt-record/object?api-version=2025-08-27.preview), [PaymentRecord](/api/payment-record/object?api-version=2025-08-27.preview), [PaymentRecordReportPaymentParams](/api/payment-record/report-payment/report?api-version=2025-08-27.preview) |

#### Node.js

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `amount`, `amount_authorized`, `amount_refunded`, `application` | Added | [PaymentAttemptRecord](/api/payment-attempt-record/object?api-version=2025-08-27.preview), [PaymentRecord](/api/payment-record/object?api-version=2025-08-27.preview) |
| `processor_details` | Added | [PaymentAttemptRecord](/api/payment-attempt-record/object?api-version=2025-08-27.preview), [PaymentRecord](/api/payment-record/object?api-version=2025-08-27.preview), [PaymentRecordReportPaymentParams](/api/payment-record/report-payment/report?api-version=2025-08-27.preview) |
| `payment_reference` | Removed | [PaymentAttemptRecord](/api/payment-attempt-record/object?api-version=2025-08-27.preview), [PaymentRecord](/api/payment-record/object?api-version=2025-08-27.preview), [PaymentRecordReportPaymentParams](/api/payment-record/report-payment/report?api-version=2025-08-27.preview) |

#### Go

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `Amount`, `AmountAuthorized`, `AmountRefunded`, `Application` | Added | [PaymentAttemptRecord](/api/payment-attempt-record/object?api-version=2025-08-27.preview), [PaymentRecord](/api/payment-record/object?api-version=2025-08-27.preview) |
| `ProcessorDetails` | Added | [PaymentAttemptRecord](/api/payment-attempt-record/object?api-version=2025-08-27.preview), [PaymentRecord](/api/payment-record/object?api-version=2025-08-27.preview), [PaymentRecordReportPaymentParams](/api/payment-record/report-payment/report?api-version=2025-08-27.preview) |
| `PaymentReference` | Removed | [PaymentAttemptRecord](/api/payment-attempt-record/object?api-version=2025-08-27.preview), [PaymentRecord](/api/payment-record/object?api-version=2025-08-27.preview), [PaymentRecordReportPaymentParams](/api/payment-record/report-payment/report?api-version=2025-08-27.preview) |

#### .NET

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `Amount`, `AmountAuthorized`, `AmountRefunded`, `Application` | Added | [PaymentAttemptRecord](/api/payment-attempt-record/object?api-version=2025-08-27.preview), [PaymentRecord](/api/payment-record/object?api-version=2025-08-27.preview) |
| `ProcessorDetails` | Added | [PaymentAttemptRecord](/api/payment-attempt-record/object?api-version=2025-08-27.preview), [PaymentRecord](/api/payment-record/object?api-version=2025-08-27.preview), [PaymentRecordReportPaymentOptions](/api/payment-record/report-payment/report?api-version=2025-08-27.preview) |
| `PaymentReference` | Removed | [PaymentAttemptRecord](/api/payment-attempt-record/object?api-version=2025-08-27.preview), [PaymentRecord](/api/payment-record/object?api-version=2025-08-27.preview), [PaymentRecordReportPaymentOptions](/api/payment-record/report-payment/report?api-version=2025-08-27.preview) |

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
