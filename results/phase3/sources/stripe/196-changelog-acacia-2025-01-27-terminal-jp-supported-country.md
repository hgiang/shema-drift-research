# Adds support for collecting tips in JPY currency to Terminal

## What’s new

We added the Japanese JPY as a [supported currency](https://docs.stripe.com/currencies.md) to the Terminal [tipping configuration](https://docs.stripe.com/terminal/features/collecting-tips/overview.md). You can set this attribute when you [create](https://docs.stripe.com/api/terminal/configuration/create.md?api-version=2025-01-27.acacia) or [update](https://docs.stripe.com/api/terminal/configuration/update.md?api-version=2025-01-27.acacia) the Terminal [Configuration](https://docs.stripe.com/api/terminal/configuration.md?api-version=2025-01-27.acacia).

## Impact

Users in Japan can now [collect on-reader tips](https://docs.stripe.com/terminal/features/collecting-tips/on-reader.md) in the JPY currency.

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `jpy` | Added | [Terminal.Configuration#create.tipping](/api/terminal/configuration/create?api-version=2025-01-27.acacia#create_configuration-tipping), [Terminal.Configuration#update.tipping](/api/terminal/configuration/update?api-version=2025-01-27.acacia#update_configuration-tipping), [Terminal.Configuration.tipping](/api/terminal/configuration/object?api-version=2025-01-27.acacia#terminal_configuration_object-tipping) |

#### Ruby

This change doesn’t affect the Ruby SDK.

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `jpy` | Added | [stripe.terminal.Configuration.CreateParamsTipping](/api/terminal/configuration/create?api-version=2025-01-27.acacia#create_configuration-tipping), [stripe.terminal.Configuration.ModifyParamsTipping](/api/terminal/configuration/update?api-version=2025-01-27.acacia#update_configuration-tipping), [stripe.terminal.Configuration.Tipping](/api/terminal/configuration/object?api-version=2025-01-27.acacia#terminal_configuration_object-tipping) |

#### PHP

This change doesn’t affect the PHP SDK.

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `jpy` | Added | [Terminal.Configuration.tipping](/api/terminal/configuration/object?api-version=2025-01-27.acacia#terminal_configuration_object-tipping), [terminal.ConfigurationCreateParams.tipping](/api/terminal/configuration/create?api-version=2025-01-27.acacia#create_configuration-tipping), [terminal.ConfigurationUpdateParams.tipping](/api/terminal/configuration/update?api-version=2025-01-27.acacia#update_configuration-tipping) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `jpy` | Added | [Terminal.Configuration.tipping](/api/terminal/configuration/object?api-version=2025-01-27.acacia#terminal_configuration_object-tipping), [Terminal.ConfigurationCreateParams.tipping](/api/terminal/configuration/create?api-version=2025-01-27.acacia#create_configuration-tipping), [Terminal.ConfigurationUpdateParams.tipping](/api/terminal/configuration/update?api-version=2025-01-27.acacia#update_configuration-tipping) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `Jpy` | Added | [TerminalConfigurationTippingParams](/api/terminal/configuration/create?api-version=2025-01-27.acacia#create_configuration-tipping), [TerminalConfigurationTipping](/api/terminal/configuration/object?api-version=2025-01-27.acacia#terminal_configuration_object-tipping) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `Jpy` | Added | [TerminalConfigurationTippingOptions](/api/terminal/configuration/create?api-version=2025-01-27.acacia#create_configuration-tipping), [TerminalConfigurationTipping](/api/terminal/configuration/object?api-version=2025-01-27.acacia#terminal_configuration_object-tipping) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2025-01-27.acacia`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to [v13.4.0](https://github.com/stripe/stripe-ruby/releases/tag/v13.4.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to [v11.5.0](https://github.com/stripe/stripe-python/releases/tag/v11.5.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to [v16.5.0](https://github.com/stripe/stripe-php/releases/tag/v16.5.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to [v28.3.0](https://github.com/stripe/stripe-java/releases/tag/v28.3.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to [v17.6.0](https://github.com/stripe/stripe-node/releases/tag/v17.6.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to [v81.3.0](https://github.com/stripe/stripe-go/releases/tag/v81.3.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to [v47.3.0](https://github.com/stripe/stripe-dotnet/releases/tag/v47.3.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).
