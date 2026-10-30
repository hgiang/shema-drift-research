# Adds support for new tipping currencies to the Terminal Configuration object

## What’s new

Adds new parameters to the Terminal [Configuration](https://docs.stripe.com/api/terminal/configuration.md?api-version=2025-07-30.basil) object to enable tipping in additional local currencies:

| Country | Currency | Parameter |
| --- | --- | --- |
| United Arab Emirates | AED | [tipping.aed](https://docs.stripe.com/api/terminal/configuration/object.md?api-version=2025-07-30.basil#terminal_configuration_object-tipping-aed) |
| Bulgaria | BGN | [tipping.bgn](https://docs.stripe.com/api/terminal/configuration/object.md?api-version=2025-07-30.basil#terminal_configuration_object-tipping-bgn) |
| Hungary | HUF | [tipping.huf](https://docs.stripe.com/api/terminal/configuration/object.md?api-version=2025-07-30.basil#terminal_configuration_object-tipping-huf) |
| Romania | RON | [tipping.ron](https://docs.stripe.com/api/terminal/configuration/object.md?api-version=2025-07-30.basil#terminal_configuration_object-tipping-ron) |

## Impact

You can now configure your Terminal readers to accept tips in the local currency in the UAE (AED), Bulgaria (BGN), Hungary (HUF) and Romania (RON).

## Changes

#### REST API

| Parameters | Change | Resources or endpoints |
| --- | --- | --- |
| `aed`, `bgn`, `huf`, `ron` | Added | [Terminal.Configuration#create.tipping](/api/terminal/configuration/create?api-version=2025-07-30.basil#create_configuration-tipping), [Terminal.Configuration#update.tipping](/api/terminal/configuration/update?api-version=2025-07-30.basil#update_configuration-tipping), [Terminal.Configuration.tipping](/api/terminal/configuration/object?api-version=2025-07-30.basil#terminal_configuration_object-tipping) |

#### Ruby

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `aed`, `bgn`, `huf`, `ron` | Added | [Terminal::Configuration::CreateParams::Tipping](/api/terminal/configuration/create?api-version=2025-07-30.basil#create_configuration-tipping), [Terminal::Configuration::Tipping](/api/terminal/configuration/object?api-version=2025-07-30.basil#terminal_configuration_object-tipping), [Terminal::Configuration::UpdateParams::Tipping](/api/terminal/configuration/update?api-version=2025-07-30.basil#update_configuration-tipping) |

#### Python

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `aed`, `bgn`, `huf`, `ron` | Added | [Terminal.Configuration.Tipping](/api/terminal/configuration/object?api-version=2025-07-30.basil#terminal_configuration_object-tipping), [terminal.Configuration.CreateParamsTipping](/api/terminal/configuration/create?api-version=2025-07-30.basil#create_configuration-tipping), [terminal.Configuration.ModifyParamsTipping](/api/terminal/configuration/update?api-version=2025-07-30.basil#update_configuration-tipping) |

#### PHP

This change doesn’t affect the PHP SDK.

#### Java

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `aed`, `bgn`, `huf`, `ron` | Added | [terminal.Configuration.tipping](/api/terminal/configuration/object?api-version=2025-07-30.basil#terminal_configuration_object-tipping), [terminal.ConfigurationCreateParams.tipping](/api/terminal/configuration/create?api-version=2025-07-30.basil#create_configuration-tipping), [terminal.ConfigurationUpdateParams.tipping](/api/terminal/configuration/update?api-version=2025-07-30.basil#update_configuration-tipping) |

#### Node.js

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `aed`, `bgn`, `huf`, `ron` | Added | [Terminal.Configuration.tipping](/api/terminal/configuration/object?api-version=2025-07-30.basil#terminal_configuration_object-tipping), [Terminal.ConfigurationCreateParams.tipping](/api/terminal/configuration/create?api-version=2025-07-30.basil#create_configuration-tipping), [Terminal.ConfigurationUpdateParams.tipping](/api/terminal/configuration/update?api-version=2025-07-30.basil#update_configuration-tipping) |

#### Go

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `Aed`, `Bgn`, `Huf`, `Ron` | Added | [TerminalConfigurationTipping](/api/terminal/configuration/object?api-version=2025-07-30.basil#terminal_configuration_object-tipping), [TerminalConfigurationTippingParams](/api/terminal/configuration/create?api-version=2025-07-30.basil#create_configuration-tipping) |

#### .NET

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `Aed`, `Bgn`, `Huf`, `Ron` | Added | [Terminal.Configuration.Tipping](/api/terminal/configuration/object?api-version=2025-07-30.basil#terminal_configuration_object-tipping), [TerminalConfigurationTippingOptions](/api/terminal/configuration/create?api-version=2025-07-30.basil#create_configuration-tipping) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2025-07-30.basil`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to [v15.4.0](https://github.com/stripe/stripe-ruby/releases/tag/v15.4.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to [v12.4.0](https://github.com/stripe/stripe-python/releases/tag/v12.4.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to [v17.5.0](https://github.com/stripe/stripe-php/releases/tag/v17.5.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to [v29.4.0](https://github.com/stripe/stripe-java/releases/tag/v29.4.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to [v18.4.0](https://github.com/stripe/stripe-node/releases/tag/v18.4.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to [v82.4.0](https://github.com/stripe/stripe-go/releases/tag/v82.4.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to [v48.4.0](https://github.com/stripe/stripe-dotnet/releases/tag/v48.4.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).
