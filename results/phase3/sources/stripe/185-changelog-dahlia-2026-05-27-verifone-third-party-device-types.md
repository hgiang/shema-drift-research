# Adds Support for Verifone third-party device types to Terminal APIs

## What’s new

You can now use four new Verifone device types with Stripe Terminal APIs: [V660p](https://docs.stripe.com/terminal/payments/setup-reader/v660p.md), [UX700](https://docs.stripe.com/terminal/payments/setup-reader/ux700.md), [P630](https://docs.stripe.com/terminal/payments/setup-reader/p630.md) and [M425](https://docs.stripe.com/terminal/payments/setup-reader/m425.md), along with their simulated variants for testing.

The new device types are available in the [Terminal Reader API](https://docs.stripe.com/api/terminal/readers.md?api-version=2026-05-27.dahlia), [Terminal Configuration API](https://docs.stripe.com/api/terminal/configuration.md?api-version=2026-05-27.dahlia), [Terminal Device Deploy Group API](https://docs.stripe.com/api/terminal/device_deploy_groups.md?api-version=2026-05-27.dahlia) and [Terminal Device Asset Version API](https://docs.stripe.com/api/terminal/device_asset_versions.md?api-version=2026-05-27.dahlia).

## Impact

When creating Terminal configurations, you can specify device-specific settings for each Verifone device type. Learn more about [Terminal Configurations](https://docs.stripe.com/terminal/fleet/configurations-overview.md?dashboard-or-api=api).

If you’re using the V660p or UX700 device types, you can deploy third-party applications to these readers using the existing Device Deploy Group and Device Asset Version APIs. Learn more about [Apps on Devices](https://docs.stripe.com/terminal/features/apps-on-devices/overview.md).

## Changes

#### REST API

| Parameters | Change | Resources or endpoints |
| --- | --- | --- |
| `verifone_m425`, `verifone_p630`, `verifone_ux700`, `verifone_v660p` | Added | [Terminal.Configuration](/api/terminal/configuration/object?api-version=2026-05-27.dahlia#terminal_configuration_object), [Terminal.Configuration#create](/api/terminal/configuration/create?api-version=2026-05-27.dahlia#create_configuration), [Terminal.Configuration#update](/api/terminal/configuration/update?api-version=2026-05-27.dahlia#update_configuration) |

| Values | Change | Enums |
| --- | --- | --- |
| `simulated_verifone_m425`, `simulated_verifone_p630`, `simulated_verifone_ux700`, `simulated_verifone_v660p`, `verifone_m425`, `verifone_p630`, `verifone_ux700`, `verifone_v660p` | Added | [Terminal.Reader#list.device_type](/api/terminal/readers/list?api-version=2026-05-27.dahlia#list_terminal_reader-device_type), [Terminal.Reader.device_type](/api/terminal/readers/object?api-version=2026-05-27.dahlia#terminal_reader_object-device_type) |

#### Ruby

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `verifone_m425`, `verifone_p630`, `verifone_ux700`, `verifone_v660p` | Added | [Terminal::Configuration](/api/terminal/configuration/object?api-version=2026-05-27.dahlia#terminal_configuration_object), [Terminal::ConfigurationCreateParams](/api/terminal/configuration/create?api-version=2026-05-27.dahlia#create_configuration), [Terminal::ConfigurationUpdateParams](/api/terminal/configuration/update?api-version=2026-05-27.dahlia#update_configuration) |

#### Python

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `verifone_m425`, `verifone_p630`, `verifone_ux700`, `verifone_v660p` | Added | [Terminal.Configuration](/api/terminal/configuration/object?api-version=2026-05-27.dahlia#terminal_configuration_object), [terminal.ConfigurationCreateParams](/api/terminal/configuration/create?api-version=2026-05-27.dahlia#create_configuration), [terminal.ConfigurationModifyParams](/api/terminal/configuration/update?api-version=2026-05-27.dahlia#update_configuration) |

| Values | Change | Enums |
| --- | --- | --- |
| `simulated_verifone_m425`, `simulated_verifone_p630`, `simulated_verifone_ux700`, `simulated_verifone_v660p`, `verifone_m425`, `verifone_p630`, `verifone_ux700`, `verifone_v660p` | Added | [terminal.ReaderListParams.device_type](/api/terminal/readers/list?api-version=2026-05-27.dahlia#list_terminal_reader-device_type), [Terminal.Reader.device_type](/api/terminal/readers/object?api-version=2026-05-27.dahlia#terminal_reader_object-device_type) |

#### PHP

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `verifone_m425`, `verifone_p630`, `verifone_ux700`, `verifone_v660p` | Added | [Terminal.Configuration](/api/terminal/configuration/object?api-version=2026-05-27.dahlia#terminal_configuration_object), [Terminal\Configuration.create().$params](/api/terminal/configuration/create?api-version=2026-05-27.dahlia#create_configuration), [Terminal\Configuration.update().$params](/api/terminal/configuration/update?api-version=2026-05-27.dahlia#update_configuration) |

| Values | Change | Enum |
| --- | --- | --- |
| `simulated_verifone_m425`, `simulated_verifone_p630`, `simulated_verifone_ux700`, `simulated_verifone_v660p`, `verifone_m425`, `verifone_p630`, `verifone_ux700`, `verifone_v660p` | Added | [Terminal.Reader.device_type](/api/terminal/readers/object?api-version=2026-05-27.dahlia#terminal_reader_object-device_type) |

#### Java

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `verifoneM425`, `verifoneP630`, `verifoneUx700`, `verifoneV660p` | Added | [terminal.Configuration](/api/terminal/configuration/object?api-version=2026-05-27.dahlia#terminal_configuration_object), [terminal.ConfigurationCreateParams](/api/terminal/configuration/create?api-version=2026-05-27.dahlia#create_configuration), [terminal.ConfigurationUpdateParams](/api/terminal/configuration/update?api-version=2026-05-27.dahlia#update_configuration) |

| Values | Change | Enum |
| --- | --- | --- |
| `simulated_verifone_m425`, `simulated_verifone_p630`, `simulated_verifone_ux700`, `simulated_verifone_v660p`, `verifone_m425`, `verifone_p630`, `verifone_ux700`, `verifone_v660p` | Added | [terminal.ReaderListParams.deviceType](/api/terminal/readers/list?api-version=2026-05-27.dahlia#list_terminal_reader-deviceType) |

#### Node.js

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `verifone_m425`, `verifone_p630`, `verifone_ux700`, `verifone_v660p` | Added | [Terminal.Configuration](/api/terminal/configuration/object?api-version=2026-05-27.dahlia#terminal_configuration_object), [Terminal.ConfigurationCreateParams](/api/terminal/configuration/create?api-version=2026-05-27.dahlia#create_configuration), [Terminal.ConfigurationUpdateParams](/api/terminal/configuration/update?api-version=2026-05-27.dahlia#update_configuration) |

| Values | Change | Enums |
| --- | --- | --- |
| `simulated_verifone_m425`, `simulated_verifone_p630`, `simulated_verifone_ux700`, `simulated_verifone_v660p`, `verifone_m425`, `verifone_p630`, `verifone_ux700`, `verifone_v660p` | Added | [Terminal.ReaderListParams.device_type](/api/terminal/readers/list?api-version=2026-05-27.dahlia#list_terminal_reader-device_type), [Terminal.Reader.device_type](/api/terminal/readers/object?api-version=2026-05-27.dahlia#terminal_reader_object-device_type) |

#### Go

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `VerifoneM425`, `VerifoneP630`, `VerifoneUx700`, `VerifoneV660p` | Added | [TerminalConfiguration](/api/terminal/configuration/object?api-version=2026-05-27.dahlia#terminal_configuration_object), [TerminalConfigurationParams](/api/terminal/configuration/update?api-version=2026-05-27.dahlia#update_configuration) |

| Values | Change | Enum |
| --- | --- | --- |
| `simulated_verifone_m425`, `simulated_verifone_p630`, `simulated_verifone_ux700`, `simulated_verifone_v660p`, `verifone_m425`, `verifone_p630`, `verifone_ux700`, `verifone_v660p` | Added | [TerminalReader.DeviceType](/api/terminal/readers/object?api-version=2026-05-27.dahlia#terminal_reader_object-DeviceType) |

#### .NET

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `VerifoneM425`, `VerifoneP630`, `VerifoneUx700`, `VerifoneV660p` | Added | [Terminal.Configuration](/api/terminal/configuration/object?api-version=2026-05-27.dahlia#terminal_configuration_object), [Terminal.ConfigurationCreateOptions](/api/terminal/configuration/create?api-version=2026-05-27.dahlia#create_configuration), [Terminal.ConfigurationUpdateOptions](/api/terminal/configuration/update?api-version=2026-05-27.dahlia#update_configuration) |

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
- [Adds API error details to Terminal reader action failures](https://docs.stripe.com/changelog/dahlia/2026-05-27/terminal-reader-action-failures-error-details.md)
