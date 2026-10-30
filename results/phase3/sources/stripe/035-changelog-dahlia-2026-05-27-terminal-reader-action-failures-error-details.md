# Adds API error details to Terminal reader action failures

## What’s new

Adds an [api_error](https://docs.stripe.com/api/terminal/readers/object.md?api-version=2026-05-27.dahlia#terminal_reader_object-action-api_error) hash to the Terminal Reader [action](https://docs.stripe.com/api/terminal/readers/object.md?api-version=2026-05-27.dahlia#terminal_reader_object-action) for server-driven integrations. When a reader action fails due to a Stripe API error, such as a card decline, `api_error` contains the error `type`, `code`, `message`, `decline_code`, `doc_url`, `request_log_url` and `param`. When the failure originates from the reader itself, such as a customer cancellation, `api_error` is null. Don’t parse `api_error.message` for programmatic logic; use `type` or `code` instead. This requires reader software version 2.42 or later.

On older readers, `api_error` is always null. See [Handle payment failures](https://docs.stripe.com/terminal/payments/collect-card-payment.md?terminal-sdk-platform=server-driven#payment-failures) for integration guidance.

## Impact

You can now determine whether a server-driven [reader action failure](https://docs.stripe.com/terminal/payments/collect-card-payment.md?terminal-sdk-platform=server-driven#payment-failures) originates from the Stripe API or from the reader, and identify which error messages to show to cardholders. Use [api_error.type](https://docs.stripe.com/api/terminal/readers/object.md?api-version=2026-05-27.dahlia#terminal_reader_object-action-api_error-type) to identify `card_error` failures to display to cardholders. Use [api_error.doc_url](https://docs.stripe.com/api/terminal/readers/object.md?api-version=2026-05-27.dahlia#terminal_reader_object-action-api_error-doc_url) for guidance on handling each specific error code.

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `api_error` | Added | [Terminal.Reader.action](/api/terminal/readers/object?api-version=2026-05-27.dahlia#terminal_reader_object-action) |

#### Ruby

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `api_error` | Added | [Terminal::Reader::Action](/api/terminal/readers/object?api-version=2026-05-27.dahlia#terminal_reader_object-action) |

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `api_error` | Added | [Terminal.Reader.Action](/api/terminal/readers/object?api-version=2026-05-27.dahlia#terminal_reader_object-action) |

#### PHP

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `api_error` | Added | [Terminal.Reader.action](/api/terminal/readers/object?api-version=2026-05-27.dahlia#terminal_reader_object-action) |

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `apiError` | Added | [terminal.Reader.action](/api/terminal/readers/object?api-version=2026-05-27.dahlia#terminal_reader_object-action) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `api_error` | Added | [Terminal.Reader.action](/api/terminal/readers/object?api-version=2026-05-27.dahlia#terminal_reader_object-action) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `APIError` | Added | [TerminalReaderAction](/api/terminal/readers/object?api-version=2026-05-27.dahlia#terminal_reader_object-action) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `ApiError` | Added | [Terminal.Reader.Action](/api/terminal/readers/object?api-version=2026-05-27.dahlia#terminal_reader_object-action) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2026-05-27.dahlia`
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

- [Adds support for printing images on Terminal readers with embedded printers](https://docs.stripe.com/changelog/dahlia/2026-05-27/terminal-reader-print-action.md)
- [Adds support for Verifone third-party device types to Terminal APIs](https://docs.stripe.com/changelog/dahlia/2026-05-27/verifone-third-party-device-types.md)
