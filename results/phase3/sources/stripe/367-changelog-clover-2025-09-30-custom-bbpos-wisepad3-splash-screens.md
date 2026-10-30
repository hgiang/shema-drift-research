# Adds support for custom BBPOS WisePad 3 splash screens

## What’s new

BBPOS WisePad 3 splash screens can now be configured with the Terminal [Configuration API](https://docs.stripe.com/api/terminal/configuration.md?api-version=2025-09-30.clover).

## Impact

You can now assign a custom splash screen to BBPOS WisePad 3 devices. A splash screen is the default screen that displays when your reader is ready to accept payments. There is no change to existing configurations for other device types. See [Configure readers with a custom splash screen](https://docs.stripe.com/terminal/fleet/splash-screen.md) for more information.

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `bbpos_wisepad3` | Added | [Terminal.Configuration](/api/terminal/configuration/object?api-version=2025-09-30.clover), [Terminal.Configuration#create](/api/terminal/configuration/create?api-version=2025-09-30.clover#create_terminal_configuration), [Terminal.Configuration#update](/api/terminal/configuration/update?api-version=2025-09-30.clover#update_terminal_configuration) |

#### Ruby

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `bbpos_wisepad3` | Added | [Terminal::Configuration](/api/terminal/configuration/object?api-version=2025-09-30.clover), [Terminal::Configuration::CreateParams](/api/terminal/configuration/create?api-version=2025-09-30.clover#create_terminal_configuration), [Terminal::Configuration::UpdateParams](/api/terminal/configuration/update?api-version=2025-09-30.clover#update_terminal_configuration) |

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `bbpos_wisepad3` | Added | [Terminal.Configuration](/api/terminal/configuration/object?api-version=2025-09-30.clover), [terminal.Configuration.CreateParams](/api/terminal/configuration/create?api-version=2025-09-30.clover#create_terminal_configuration), [terminal.Configuration.ModifyParams](/api/terminal/configuration/update?api-version=2025-09-30.clover#update_terminal_configuration) |

#### PHP

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `bbpos_wisepad3` | Added | [Terminal.Configuration](/api/terminal/configuration/object?api-version=2025-09-30.clover), [Terminal\Configuration.create().$params](/api/terminal/configuration/create?api-version=2025-09-30.clover#create_terminal_configuration), [Terminal\Configuration.update().$params](/api/terminal/configuration/update?api-version=2025-09-30.clover#update_terminal_configuration) |

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `bbposWisepad3` | Added | [terminal.Configuration](/api/terminal/configuration/object?api-version=2025-09-30.clover), [terminal.ConfigurationCreateParams](/api/terminal/configuration/create?api-version=2025-09-30.clover#create_terminal_configuration), [terminal.ConfigurationUpdateParams](/api/terminal/configuration/update?api-version=2025-09-30.clover#update_terminal_configuration) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `bbpos_wisepad3` | Added | [Terminal.Configuration](/api/terminal/configuration/object?api-version=2025-09-30.clover), [Terminal.ConfigurationCreateParams](/api/terminal/configuration/create?api-version=2025-09-30.clover#create_terminal_configuration), [Terminal.ConfigurationUpdateParams](/api/terminal/configuration/update?api-version=2025-09-30.clover#update_terminal_configuration) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `BBPOSWisePad3` | Added | [TerminalConfiguration](/api/terminal/configuration/object?api-version=2025-09-30.clover), [TerminalConfigurationParams](/api/terminal/configuration/update?api-version=2025-09-30.clover#update_terminal_configuration) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `BbposWisepad3` | Added | [Terminal.Configuration](/api/terminal/configuration/object?api-version=2025-09-30.clover), [Terminal.ConfigurationCreateOptions](/api/terminal/configuration/create?api-version=2025-09-30.clover#create_terminal_configuration), [Terminal.ConfigurationUpdateOptions](/api/terminal/configuration/update?api-version=2025-09-30.clover#update_terminal_configuration) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2025-09-30.clover`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to [v16.0.0](https://github.com/stripe/stripe-ruby/releases/tag/v16.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to [v13.0.1](https://github.com/stripe/stripe-python/releases/tag/v13.0.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to [v18.0.0](https://github.com/stripe/stripe-php/releases/tag/v18.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to [v30.0.0](https://github.com/stripe/stripe-java/releases/tag/v30.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to [v19.1.0](https://github.com/stripe/stripe-node/releases/tag/v19.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to [v83.0.0](https://github.com/stripe/stripe-go/releases/tag/v83.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to [v49.0.0](https://github.com/stripe/stripe-dotnet/releases/tag/v49.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

## Related changes

- [Adds Japan-specific fields to the Terminal Locations API](https://docs.stripe.com/changelog/clover/2025-09-30/add-japan-fields-to-terminal-locations.md)
