# Adds support for the Stripe Reader S710

## What’s new

Adds support for the new [Stripe Reader S710](https://docs.stripe.com/terminal/readers/stripe-reader-s700-s710.md) Terminal device. `stripe_s710` and `simulated_stripe_s710` are now supported values for the [device_type](https://docs.stripe.com/api/terminal/readers/object.md?api-version=2026-02-25.clover#terminal_reader_object-device_type) property on the [Terminal Reader](https://docs.stripe.com/api/terminal/readers/object.md?api-version=2026-02-25.clover) object.

Additionally, adds a new [stripe_s710](https://docs.stripe.com/api/terminal/configuration/object.md?api-version=2026-02-25.clover#terminal_configuration_object-stripe_s710) hash that includes a [splashscreen](https://docs.stripe.com/api/terminal/configuration/object.md?api-version=2026-02-25.clover#terminal_configuration_object-stripe_s710-splashscreen) parameter. You can use this parameter to configure the splash screen display for S710 devices when you [create](https://docs.stripe.com/api/terminal/configuration/create.md?api-version=2026-02-25.clover) or [update](https://docs.stripe.com/api/terminal/configuration/update.md?api-version=2026-02-25.clover) Terminal Configurations.

## Impact

You can now integrate Stripe Reader S710 devices into your payment processing workflow. If you’re using Terminal Configurations to customise device behaviour, you can configure splash screen settings specifically for S710 devices using the new `stripe_s710.splashscreen` parameter.

## Changes

#### REST API

| Parameters | Change | Resources or endpoints |
| --- | --- | --- |
| `cellular`, `stripe_s710` | Added | [Terminal.Configuration](/api/terminal/configuration/object?api-version=2026-02-25.clover), [Terminal.Configuration#create](/api/terminal/configuration/create?api-version=2026-02-25.clover), [Terminal.Configuration#update](/api/terminal/configuration/update?api-version=2026-02-25.clover) |

| Values | Change | Enums |
| --- | --- | --- |
| `simulated_stripe_s710`, `stripe_s710` | Added | [Terminal.Reader#list](/api/terminal/readers/list?api-version=2026-02-25.clover#list_terminal_reader-device_type), [Terminal.Reader](/api/terminal/readers/list?api-version=2026-02-25.clover#list_terminal_reader-device_type) |

#### Ruby

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `cellular`, `stripe_s710` | Added | [Terminal::Configuration](/api/terminal/configuration/object?api-version=2026-02-25.clover), [Terminal::ConfigurationCreateParams](/api/terminal/configuration/create?api-version=2026-02-25.clover), [Terminal::ConfigurationUpdateParams](/api/terminal/configuration/update?api-version=2026-02-25.clover) |

#### Python

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `cellular`, `stripe_s710` | Added | [Terminal.Configuration](/api/terminal/configuration/object?api-version=2026-02-25.clover), [terminal.ConfigurationCreateParams](/api/terminal/configuration/create?api-version=2026-02-25.clover), [terminal.ConfigurationModifyParams](/api/terminal/configuration/update?api-version=2026-02-25.clover) |

| Values | Change | Enums |
| --- | --- | --- |
| `simulated_stripe_s710`, `stripe_s710` | Added | [terminal.ReaderListParams](/api/terminal/readers/list?api-version=2026-02-25.clover#list_terminal_reader-device_type), [Terminal.Reader](/api/terminal/readers/list?api-version=2026-02-25.clover#list_terminal_reader-device_type) |

#### PHP

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `cellular`, `stripe_s710` | Added | [Terminal.Configuration](/api/terminal/configuration/object?api-version=2026-02-25.clover), [Terminal\Configuration.create().$params](/api/terminal/configuration/create?api-version=2026-02-25.clover), [Terminal\Configuration.update().$params](/api/terminal/configuration/update?api-version=2026-02-25.clover) |

| Values | Change | Enum |
| --- | --- | --- |
| `simulated_stripe_s710`, `stripe_s710` | Added | [Terminal.Reader](/api/terminal/readers/object?api-version=2026-02-25.clover#terminal_reader_object-device_type) |

#### Java

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `cellular`, `stripeS710` | Added | [terminal.Configuration](/api/terminal/configuration/object?api-version=2026-02-25.clover), [terminal.ConfigurationCreateParams](/api/terminal/configuration/create?api-version=2026-02-25.clover), [terminal.ConfigurationUpdateParams](/api/terminal/configuration/update?api-version=2026-02-25.clover) |

| Values | Change | Enum |
| --- | --- | --- |
| `simulated_stripe_s710`, `stripe_s710` | Added | [terminal.ReaderListParams](/api/terminal/readers/list?api-version=2026-02-25.clover#list_terminal_reader-device_type) |

#### Node.js

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `cellular`, `stripe_s710` | Added | [Terminal.Configuration](/api/terminal/configuration/object?api-version=2026-02-25.clover), [Terminal.ConfigurationCreateParams](/api/terminal/configuration/create?api-version=2026-02-25.clover), [Terminal.ConfigurationUpdateParams](/api/terminal/configuration/update?api-version=2026-02-25.clover) |

| Values | Change | Enums |
| --- | --- | --- |
| `simulated_stripe_s710`, `stripe_s710` | Added | [Terminal.ReaderListParams](/api/terminal/readers/list?api-version=2026-02-25.clover#list_terminal_reader-device_type), [Terminal.Reader](/api/terminal/readers/list?api-version=2026-02-25.clover#list_terminal_reader-device_type) |

#### Go

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `Cellular`, `StripeS710` | Added | [TerminalConfiguration](/api/terminal/configuration/object?api-version=2026-02-25.clover), [TerminalConfigurationParams](/api/terminal/configuration/update?api-version=2026-02-25.clover) |

| Values | Change | Enum |
| --- | --- | --- |
| `simulated_stripe_s710`, `stripe_s710` | Added | [TerminalReader](/api/terminal/readers/object?api-version=2026-02-25.clover#terminal_reader_object-device_type) |

#### .NET

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `Cellular`, `StripeS710` | Added | [Terminal.Configuration](/api/terminal/configuration/object?api-version=2026-02-25.clover), [Terminal.ConfigurationCreateOptions](/api/terminal/configuration/create?api-version=2026-02-25.clover), [Terminal.ConfigurationUpdateOptions](/api/terminal/configuration/update?api-version=2026-02-25.clover) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2026-02-25.clover`
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

- [Adds Terminal reader and location to payment method details](https://docs.stripe.com/changelog/clover/2026-02-25/terminal-reader-and-location.md)
- [Adds the ability to manage cellular connectivity settings for Terminal readers](https://docs.stripe.com/changelog/clover/2026-02-25/terminal-cellular-configuration.md)
- [Adds support for uploading Terminal Wi-Fi certificates and private keys](https://docs.stripe.com/changelog/clover/2026-02-25/terminal-wifi-certificates-and-private-keys.md)
