# Adds support for configuring the reboot time setting

## What’s new

The `reboot_window` parameter lets you set a custom time window for your Terminal reader to reboot and update software.

Create a new configuration for a Terminal reader. You can optionally add a `reboot_window`.

## Impact

This is useful for ensuring that reader reboots don’t interfere with business operations.

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `reboot_window` | Added | [Terminal.Configuration#create](/api/terminal/configuration/create?api-version=2024-09-30.acacia), [Terminal.Configuration#update](/api/terminal/configuration/update?api-version=2024-09-30.acacia), [Terminal.Configuration](/api/terminal/configuration/object?api-version=2024-09-30.acacia) |

#### Ruby

This change doesn’t affect the Ruby SDK.

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `reboot_window` | Added | [stripe.terminal.Configuration.CreateParams](/api/terminal/configuration/create?api-version=2024-09-30.acacia), [stripe.terminal.Configuration.ModifyParams](/api/terminal/configuration/update?api-version=2024-09-30.acacia), [stripe.terminal.Configuration](/api/terminal/configuration/object?api-version=2024-09-30.acacia) |

#### PHP

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `reboot_window` | Added | [Terminal.Configuration](/api/terminal/configuration/object?api-version=2024-09-30.acacia) |

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `reboot_window` | Added | [Terminal.Configuration](/api/terminal/configuration/object?api-version=2024-09-30.acacia), [terminal.ConfigurationCreateParams](/api/terminal/configuration/create?api-version=2024-09-30.acacia), [terminal.ConfigurationUpdateParams](/api/terminal/configuration/update?api-version=2024-09-30.acacia) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `reboot_window` | Added | [Terminal.ConfigurationCreateParams](/api/terminal/configuration/create?api-version=2024-09-30.acacia), [Terminal.ConfigurationUpdateParams](/api/terminal/configuration/update?api-version=2024-09-30.acacia), [Terminal.Configuration](/api/terminal/configuration/object?api-version=2024-09-30.acacia) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `RebootWindow` | Added | [TerminalConfigurationParams](/api/terminal/configuration/create?api-version=2024-09-30.acacia), [TerminalConfiguration](/api/terminal/configuration/object?api-version=2024-09-30.acacia) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `RebootWindow` | Added | [Terminal.ConfigurationCreateOptions](/api/terminal/configuration/create?api-version=2024-09-30.acacia), [Terminal.ConfigurationUpdateOptions](/api/terminal/configuration/update?api-version=2024-09-30.acacia), [TerminalConfiguration](/api/terminal/configuration/object?api-version=2024-09-30.acacia) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2024-09-30.acacia`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to [v13.0.0](https://github.com/stripe/stripe-ruby/releases/tag/v13.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to [v11.0.0](https://github.com/stripe/stripe-python/releases/tag/v11.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to [v16.0.0](https://github.com/stripe/stripe-php/releases/tag/v16.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to [v27.0.0](https://github.com/stripe/stripe-java/releases/tag/v27.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to [v17.0.0](https://github.com/stripe/stripe-node/releases/tag/v17.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to [v80.0.0](https://github.com/stripe/stripe-go/releases/tag/v80.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to [v46.0.0](https://github.com/stripe/stripe-dotnet/releases/tag/v46.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

## Related changes

- [Updates consent modelling for saving cards with Terminal](https://docs.stripe.com/changelog/acacia/2024-09-30/terminal-remove-customer-consent-require-allow-redisplay.md)
- [Adds the Stripe S700 reader as a valid device type](https://docs.stripe.com/changelog/acacia/2024-09-30/terminal-reader-s700.md)
- [Adds details about offline collection on `card_present` PaymentMethod objects](https://docs.stripe.com/changelog/acacia/2024-09-30/terminal-offline-details-card-present-paymentmethods.md)
