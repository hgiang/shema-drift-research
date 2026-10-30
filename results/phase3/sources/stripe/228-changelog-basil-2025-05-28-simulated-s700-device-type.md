# Adds simulated S700 device type to Reader API

## What’s new

You can now filter for `simulated_stripe_s700` as a [device_type](https://docs.stripe.com/api/terminal/readers/list.md?api-version=2025-05-28.basil#list_terminal_reader-device_type) when you [list all Readers](https://docs.stripe.com/api/terminal/readers/list.md?api-version=2025-05-28.basil).

## Impact

You can use a [simulated reader](https://docs.stripe.com/terminal/payments/connect-reader.md) to develop and test your app and simulate Terminal payments, without connecting to physical hardware.

## Changes

#### REST API

| Value | Change | Enums |
| --- | --- | --- |
| `simulated_stripe_s700` | Added | [Terminal.Reader#list.device_type](/api/terminal/readers/list?api-version=2025-05-28.basil#list_terminal_reader-device_type), [Terminal.Reader.device_type](/api/terminal/readers/object?api-version=2025-05-28.basil#terminal_reader_object-device_type) |

#### Ruby

This change doesn’t affect the Ruby SDK.

#### Python

| Value | Change | Enums |
| --- | --- | --- |
| `simulated_stripe_s700` | Added | [TerminalReader.device_type](/api/terminal/readers/object?api-version=2025-05-28.basil#terminal_reader_object-device_type), [terminal.Reader.ListParams.device_type](/api/terminal/readers/list?api-version=2025-05-28.basil#list_terminal_reader-device_type) |

#### PHP

| Value | Change | Enum |
| --- | --- | --- |
| `simulated_stripe_s700` | Added | [Terminal.Reader.device_type](/api/terminal/readers/object?api-version=2025-05-28.basil#terminal_reader_object-device_type) |

#### Java

| Value | Change | Enum |
| --- | --- | --- |
| `simulated_stripe_s700` | Added | [terminal.ReaderListParams.deviceType](/api/terminal/readers/list?api-version=2025-05-28.basil#list_terminal_reader-device_type) |

#### Node.js

| Value | Change | Enums |
| --- | --- | --- |
| `simulated_stripe_s700` | Added | [Terminal.Reader.device_type](/api/terminal/readers/object?api-version=2025-05-28.basil#terminal_reader_object-device_type), [Terminal.ReaderListParams.device_type](/api/terminal/readers/list?api-version=2025-05-28.basil#list_terminal_reader-device_type) |

#### Go

| Value | Change | Enum |
| --- | --- | --- |
| `simulated_stripe_s700` | Added | [TerminalReader.DeviceType](/api/terminal/readers/object?api-version=2025-05-28.basil#terminal_reader_object-device_type) |

#### .NET

This change doesn’t affect the .NET SDK.

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2025-05-28.basil`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to [v15.2.0](https://github.com/stripe/stripe-ruby/releases/tag/v15.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to [v12.2.0](https://github.com/stripe/stripe-python/releases/tag/v12.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to [v17.3.0](https://github.com/stripe/stripe-php/releases/tag/v17.3.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to [v29.2.0](https://github.com/stripe/stripe-java/releases/tag/v29.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to [v18.2.0](https://github.com/stripe/stripe-node/releases/tag/v18.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to [v82.2.0](https://github.com/stripe/stripe-go/releases/tag/v82.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to [v48.2.0](https://github.com/stripe/stripe-dotnet/releases/tag/v48.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).
