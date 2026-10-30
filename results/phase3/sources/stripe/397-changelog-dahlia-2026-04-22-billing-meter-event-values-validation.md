# Adds validation for billing meter event values with more than 15 digits

## What’s new

Introduces validation that rejects billing meter event values with more than 15 significant digits. For the synchronous API, requests with such values now return a 400 error. For async meter events, Stripe reports the rejection through the [v1.billing.meter.error_report_triggered](https://docs.stripe.com/api/v2/core/events/event-types.md?api-version=2026-04-22.dahlia#v2_event_types-v1.billing.meter.error_report_triggered) event with the new `meter_event_value_too_many_digits` error code.

The error message provides specific details about the validation failure: “The value in the event payload can have at most `max_digits` digits. Received `value`.”

## Why is this a breaking change?

This change is breaking because it introduces new validation that can cause API requests to fail. If your integration currently sends usage values with more than 15 significant digits, those requests now return a `400` error instead of being processed. You must update your code to make sure all usage values contain 15 or fewer significant digits before sending them to the [Meter Events](https://docs.stripe.com/api/billing/meter-event.md?api-version=2026-04-22.preview) API.

## Impact

If your integration sends usage values with more than 15 significant digits, modify your code to validate and truncate or round these values before making API requests. This prevents data corruption that can occur due to double precision loss in the usage aggregation pipeline.

You can now also handle the new `meter_event_value_too_many_digits` error code in your error handling logic to provide appropriate feedback when validation fails.

## Changes

#### REST API

| Value | Change | Enums |
| --- | --- | --- |
| `meter_event_value_too_many_digits` | Added | [EventsV1BillingMeterErrorReportTriggeredEvent.reason.error_types[]](/api/v2/core/events/event-types?api-version=2026-04-22.preview#v2_event_types-v1.billing.meter.error_report_triggered-data-reason-error_types-code), [EventsV1BillingMeterNoMeterFoundEvent.reason.error_types[]](/api/v2/core/events/event-types?api-version=2026-04-22.preview#v2_event_types-v1.billing.meter.no_meter_found-data-reason-error_types-code) |

#### Ruby

This change doesn’t affect the Ruby SDK.

#### Python

| Value | Change | Enums |
| --- | --- | --- |
| `meter_event_value_too_many_digits` | Added | [EventsV1BillingMeterErrorReportTriggeredEvent.Reason.ErrorType](/api/v2/core/events/event-types?api-version=2026-04-22.preview#v2_event_types-v1.billing.meter.error_report_triggered-data-reason-error_types-code), [EventsV1BillingMeterNoMeterFoundEvent.Reason.ErrorType](/api/v2/core/events/event-types?api-version=2026-04-22.preview#v2_event_types-v1.billing.meter.no_meter_found-data-reason-error_types-code) |

#### PHP

| Value | Change | Enums |
| --- | --- | --- |
| `meter_event_value_too_many_digits` | Added | [EventsV1BillingMeterErrorReportTriggeredEvent.reason.error_types[]](/api/v2/core/events/event-types?api-version=2026-04-22.preview#v2_event_types-v1.billing.meter.error_report_triggered-data-reason-error_types-code), [EventsV1BillingMeterNoMeterFoundEvent.reason.error_types[]](/api/v2/core/events/event-types?api-version=2026-04-22.preview#v2_event_types-v1.billing.meter.no_meter_found-data-reason-error_types-code) |

#### Java

| Value | Change | Enums |
| --- | --- | --- |
| `meter_event_value_too_many_digits` | Added | [EventsV1BillingMeterErrorReportTriggeredEvent.reason.error_types[]](/api/v2/core/events/event-types?api-version=2026-04-22.preview#v2_event_types-v1.billing.meter.error_report_triggered-data-reason-error_types-code), [EventsV1BillingMeterNoMeterFoundEvent.reason.error_types[]](/api/v2/core/events/event-types?api-version=2026-04-22.preview#v2_event_types-v1.billing.meter.no_meter_found-data-reason-error_types-code) |

#### Node.js

| Value | Change | Enums |
| --- | --- | --- |
| `meter_event_value_too_many_digits` | Added | [EventsV1BillingMeterErrorReportTriggeredEvent.reason.error_types[]](/api/v2/core/events/event-types?api-version=2026-04-22.preview#v2_event_types-v1.billing.meter.error_report_triggered-data-reason-error_types-code), [EventsV1BillingMeterNoMeterFoundEvent.reason.error_types[]](/api/v2/core/events/event-types?api-version=2026-04-22.preview#v2_event_types-v1.billing.meter.no_meter_found-data-reason-error_types-code) |

#### Go

| Value | Change | Enums |
| --- | --- | --- |
| `meter_event_value_too_many_digits` | Added | [EventsV1BillingMeterErrorReportTriggeredEventReasonErrorType](/api/v2/core/events/event-types?api-version=2026-04-22.preview#v2_event_types-v1.billing.meter.error_report_triggered-data-reason-error_types-code), [EventsV1BillingMeterNoMeterFoundEventReasonErrorType](/api/v2/core/events/event-types?api-version=2026-04-22.preview#v2_event_types-v1.billing.meter.no_meter_found-data-reason-error_types-code) |

#### .NET

This change doesn’t affect the .NET SDK.

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2026-04-22.preview`
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

- [Adds Blik as a supported payment method for recurring payments in Stripe Billing](https://docs.stripe.com/changelog/dahlia/2026-04-22/stripe-billing-blik-recurring-payments.md)
