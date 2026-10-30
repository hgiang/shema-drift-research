# Adds ability to configure WiFi for Terminal readers

## What’s new

Adds the ability to remotely configure the [WiFi network](https://docs.stripe.com/api/terminal/configuration/object.md?api-version=2025-03-31.basil#terminal_configuration_object-wifi) for Terminal sPOS readers through the Terminal Configuration API object. After setting a remote WiFi network, the reader displays it as a **Configured network**. We support WPA/WPA2 Personal and Enterprise networks, including EAP-TLS certificates.

## Impact

Readers with remotely configured WiFi credentials can connect to the network automatically, without requiring the end user to enter any additional information. To fetch the remotely configured network from the server, the reader must first connect to a local WiFi network.

Learn more about [Terminal configurations](https://docs.stripe.com/terminal/fleet/configurations-overview.md).

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `wifi` | Added | [Terminal.Configuration#create](/api/terminal/configuration/create?api-version=2025-03-31.basil), [Terminal.Configuration#update](/api/terminal/configuration/update?api-version=2025-03-31.basil), [Terminal.Configuration](/api/terminal/configuration/object?api-version=2025-03-31.basil) |

#### Ruby

This change doesn’t affect the Ruby SDK.

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `wifi` | Added | [stripe.terminal.Configuration.CreateParams](/api/terminal/configuration/create?api-version=2025-03-31.basil), [stripe.terminal.Configuration.ModifyParams](/api/terminal/configuration/update?api-version=2025-03-31.basil), [stripe.terminal.Configuration](/api/terminal/configuration/object?api-version=2025-03-31.basil) |

#### PHP

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `wifi` | Added | [Terminal.Configuration](/api/terminal/configuration/object?api-version=2025-03-31.basil) |

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `wifi` | Added | [Terminal.Configuration](/api/terminal/configuration/object?api-version=2025-03-31.basil), [terminal.ConfigurationCreateParams](/api/terminal/configuration/create?api-version=2025-03-31.basil), [terminal.ConfigurationUpdateParams](/api/terminal/configuration/update?api-version=2025-03-31.basil) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `wifi` | Added | [Terminal.ConfigurationCreateParams](/api/terminal/configuration/create?api-version=2025-03-31.basil), [Terminal.ConfigurationUpdateParams](/api/terminal/configuration/update?api-version=2025-03-31.basil), [Terminal.Configuration](/api/terminal/configuration/object?api-version=2025-03-31.basil) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `Wifi` | Added | [TerminalConfigurationParams](/api/terminal/configuration/create?api-version=2025-03-31.basil), [TerminalConfiguration](/api/terminal/configuration/object?api-version=2025-03-31.basil) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `Wifi` | Added | [Terminal.ConfigurationCreateOptions](/api/terminal/configuration/create?api-version=2025-03-31.basil), [Terminal.ConfigurationUpdateOptions](/api/terminal/configuration/update?api-version=2025-03-31.basil), [TerminalConfiguration](/api/terminal/configuration/object?api-version=2025-03-31.basil) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2025-03-31.basil`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to [v15.0.0](https://github.com/stripe/stripe-ruby/releases/tag/v15.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to [v12.0.0](https://github.com/stripe/stripe-python/releases/tag/v12.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to [v17.0.0](https://github.com/stripe/stripe-php/releases/tag/v17.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to [v29.0.0](https://github.com/stripe/stripe-java/releases/tag/v29.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to [v18.0.0](https://github.com/stripe/stripe-node/releases/tag/v18.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to [v82.0.0](https://github.com/stripe/stripe-go/releases/tag/v82.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to [v48.0.0](https://github.com/stripe/stripe-dotnet/releases/tag/v48.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).
