# Adds support for tipping in Gibraltar pounds on Terminal readers

## What’s new

Introduces support for tipping on Terminal readers using the local currency of Gibraltar pounds (GIP) by specifying [tipping.gip](https://docs.stripe.com/api/terminal/configuration/object.md?api-version=2025-10-29.clover#terminal_configuration_object-tipping-gip) on the [Configuration](https://docs.stripe.com/api/terminal/configuration/object.md?api-version=2025-10-29.clover) .

## Impact

You can now configure your Terminal readers to accept tips in the local currency of Gibraltar pounds (GIP).

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `gip` | Added | [Terminal.Configuration#create.tipping](/api/terminal/configuration/create?api-version=2025-10-29.clover#create_terminal_configuration-tipping), [Terminal.Configuration#update.tipping](/api/terminal/configuration/update?api-version=2025-10-29.clover#update_terminal_configuration-tipping), [Terminal.Configuration.tipping](/api/terminal/configuration/object?api-version=2025-10-29.clover#terminal_configuration_object-tipping) |

#### Ruby

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `gip` | Added | [Terminal::Configuration::CreateParams::Tipping](/api/terminal/configuration/create?api-version=2025-10-29.clover#create_terminal_configuration-tipping), [Terminal::Configuration::Tipping](/api/terminal/configuration/object?api-version=2025-10-29.clover#terminal_configuration_object-tipping), [Terminal::Configuration::UpdateParams::Tipping](/api/terminal/configuration/update?api-version=2025-10-29.clover#update_terminal_configuration-tipping) |

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `gip` | Added | [Terminal.Configuration.Tipping](/api/terminal/configuration/object?api-version=2025-10-29.clover#terminal_configuration_object-tipping), [terminal.Configuration.CreateParamsTipping](/api/terminal/configuration/create?api-version=2025-10-29.clover#create_terminal_configuration-tipping), [terminal.Configuration.ModifyParamsTipping](/api/terminal/configuration/update?api-version=2025-10-29.clover#update_terminal_configuration-tipping) |

#### PHP

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `gip` | Added | [Terminal.Configuration.tipping](/api/terminal/configuration/object?api-version=2025-10-29.clover#terminal_configuration_object-tipping), [Terminal\Configuration.create().$params.tipping](/api/terminal/configuration/create?api-version=2025-10-29.clover#create_terminal_configuration-tipping), [Terminal\Configuration.update().$params.tipping](/api/terminal/configuration/update?api-version=2025-10-29.clover#update_terminal_configuration-tipping) |

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `gip` | Added | [terminal.Configuration.tipping](/api/terminal/configuration/object?api-version=2025-10-29.clover#terminal_configuration_object-tipping), [terminal.ConfigurationCreateParams.tipping](/api/terminal/configuration/create?api-version=2025-10-29.clover#create_terminal_configuration-tipping), [terminal.ConfigurationUpdateParams.tipping](/api/terminal/configuration/update?api-version=2025-10-29.clover#update_terminal_configuration-tipping) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `gip` | Added | [Terminal.Configuration.tipping](/api/terminal/configuration/object?api-version=2025-10-29.clover#terminal_configuration_object-tipping), [Terminal.ConfigurationCreateParams.tipping](/api/terminal/configuration/create?api-version=2025-10-29.clover#create_terminal_configuration-tipping), [Terminal.ConfigurationUpdateParams.tipping](/api/terminal/configuration/update?api-version=2025-10-29.clover#update_terminal_configuration-tipping) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `Gip` | Added | [TerminalConfigurationTipping](/api/terminal/configuration/object?api-version=2025-10-29.clover#terminal_configuration_object-tipping), [TerminalConfigurationTippingParams](/api/terminal/configuration/update?api-version=2025-10-29.clover#update_terminal_configuration-tipping) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `Gip` | Added | [Terminal.Configuration.Tipping](/api/terminal/configuration/object?api-version=2025-10-29.clover#terminal_configuration_object-tipping), [TerminalConfigurationTippingOptions](/api/terminal/configuration/update?api-version=2025-10-29.clover#update_terminal_configuration-tipping) |

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

- [Adds a field for a Terminal reader’s last connection timestamp](https://docs.stripe.com/changelog/clover/2025-10-29/terminal-reader-last-seen.md)
