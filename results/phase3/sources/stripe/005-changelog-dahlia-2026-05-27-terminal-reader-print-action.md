# Adds support for printing images on Terminal readers with embedded printers

## What’s new

Adds the `print_content` enum value to the [action.type](https://docs.stripe.com/api/terminal/readers/object.md?api-version=2026-05-27.dahlia#terminal_reader_object-action-type) enum on the Terminal [Reader](https://docs.stripe.com/api/terminal/readers/object.md?api-version=2026-05-27.dahlia) object. Also adds the [print_content](https://docs.stripe.com/api/terminal/readers/object.md?api-version=2026-05-27.dahlia#terminal_reader_object-action-print_content) hash to the [action](https://docs.stripe.com/api/terminal/readers/object.md?api-version=2026-05-27.dahlia#terminal_reader_object-action) hash.

You can use this action to print images on Terminal readers with embedded printers, such as the Verifone V660p. The API method accepts JPEG and PNG images through `multipart/form-data` uploads to files.stripe.com.

## Impact

You can now print content (such as receipts, coupons, queue tickets and more) in your Terminal payment flows. See the [integration guide](https://docs.stripe.com/terminal/features/print-content.md) for more details.

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `print_content` | Added | [Terminal.Reader.action](/api/terminal/readers/object?api-version=2026-05-27.dahlia#terminal_reader_object-action) |

| Value | Change | Enum |
| --- | --- | --- |
| `print_content` | Added | [Terminal.Reader.action.type](/api/terminal/readers/object?api-version=2026-05-27.dahlia#terminal_reader_object-action-type) |

#### Ruby

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `print_content` | Added | [Terminal::Reader::Action](/api/terminal/readers/object?api-version=2026-05-27.dahlia#terminal_reader_object-action) |

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `print_content` | Added | [Terminal.Reader.Action](/api/terminal/readers/object?api-version=2026-05-27.dahlia#terminal_reader_object-action) |

| Value | Change | Enum |
| --- | --- | --- |
| `print_content` | Added | [Terminal.Reader.Action.type](/api/terminal/readers/object?api-version=2026-05-27.dahlia#terminal_reader_object-action-type) |

#### PHP

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `print_content` | Added | [Terminal.Reader.action](/api/terminal/readers/object?api-version=2026-05-27.dahlia#terminal_reader_object-action) |

| Value | Change | Enum |
| --- | --- | --- |
| `print_content` | Added | [Terminal.Reader.action.type](/api/terminal/readers/object?api-version=2026-05-27.dahlia#terminal_reader_object-action-type) |

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `printContent` | Added | [terminal.Reader.action](/api/terminal/readers/object?api-version=2026-05-27.dahlia#terminal_reader_object-action) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `print_content` | Added | [Terminal.Reader.action](/api/terminal/readers/object?api-version=2026-05-27.dahlia#terminal_reader_object-action) |

| Value | Change | Enum |
| --- | --- | --- |
| `print_content` | Added | [Terminal.Reader.action.type](/api/terminal/readers/object?api-version=2026-05-27.dahlia#terminal_reader_object-action-type) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `PrintContent` | Added | [TerminalReaderAction](/api/terminal/readers/object?api-version=2026-05-27.dahlia#terminal_reader_object-action) |

| Value | Change | Enum |
| --- | --- | --- |
| `print_content` | Added | [TerminalReaderAction.Type](/api/terminal/readers/object?api-version=2026-05-27.dahlia#terminal_reader_object-action-Type) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `PrintContent` | Added | [Terminal.Reader.Action](/api/terminal/readers/object?api-version=2026-05-27.dahlia#terminal_reader_object-action) |

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

- [Adds support for Verifone third-party device types to Terminal APIs](https://docs.stripe.com/changelog/dahlia/2026-05-27/verifone-third-party-device-types.md)
- [Adds API error details to Terminal reader action failures](https://docs.stripe.com/changelog/dahlia/2026-05-27/terminal-reader-action-failures-error-details.md)
