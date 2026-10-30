# Adds Japan-specific fields to the Terminal Locations API

## What’s new

Adds new fields to the Terminal [Location](https://docs.stripe.com/api/terminal/locations.md?api-version=2025-09-30.clover) resource to support [creating locations](https://docs.stripe.com/api/terminal/locations/create.md?api-version=2025-09-30.clover) for addresses in Japan that you can associate with your readers.

## Impact

You can now [create locations](https://docs.stripe.com/api/terminal/locations/create.md?api-version=2025-09-30.clover) for addresses in Japan and associate them with your readers. This ensures that they automatically download the configuration needed to properly process charges in Japan. The [Terminal Location](https://docs.stripe.com/api/terminal/locations.md?api-version=2025-09-30.clover) object for Japan requires different fields than other countries. You can’t set the [address](https://docs.stripe.com/api/terminal/locations/create.md?api-version=2025-09-30.clover#create_terminal_location-address) field for locations in Japan.

The new [address_kana](https://docs.stripe.com/api/terminal/locations/create.md?api-version=2025-09-30.clover#create_terminal_location-address_kana) and [address_kanji](https://docs.stripe.com/api/terminal/locations/create.md?api-version=2025-09-30.clover#create_terminal_location-address_kanji) fields contain the same fields as the existing [address](https://docs.stripe.com/api/terminal/locations/create.md?api-version=2025-09-30.clover#create_terminal_location-address) field, with the addition of an optional `town` field. A valid [Terminal Location](https://docs.stripe.com/api/terminal/locations.md?api-version=2025-09-30.clover) in Japan must contain:

One or both of:

- `address_kana`
- `address_kanji`

At least one of:

- `display_name`
- `display_name_kana`
- `display_name_kanji`

The Terminal Location can optionally contain the `phone` field.

## Changes

#### REST API

| Parameters | Change | Resources or endpoints |
| --- | --- | --- |
| `address_kana`, `address_kanji`, `display_name_kana`, `display_name_kanji`, `phone` | Added | [Terminal.Location](/api/terminal/locations/object?api-version=2025-09-30.clover), [Terminal.Location#create](/api/terminal/locations/create?api-version=2025-09-30.clover), [Terminal.Location#update](/api/terminal/locations/update?api-version=2025-09-30.clover) |

| Fields | Change | From → to |
| --- | --- | --- |
| `Terminal.Location#create.address` | Changed | `required → optional` |
| `Terminal.Location#create.display_name` | Changed | `required → optional` |

#### Ruby

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `address_kana`, `address_kanji`, `display_name_kana`, `display_name_kanji`, `phone` | Added | [Terminal::Location](/api/terminal/locations/object?api-version=2025-09-30.clover), [Terminal::Location::CreateParams](/api/terminal/locations/create?api-version=2025-09-30.clover), [Terminal::Location::UpdateParams](/api/terminal/locations/update?api-version=2025-09-30.clover) |

| Fields | Change | From → to |
| --- | --- | --- |
| `Terminal::Location::CreateParams.address` | Changed | `required → optional` |
| `Terminal::Location::CreateParams.display_name` | Changed | `required → optional` |

#### Python

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `address_kana`, `address_kanji`, `display_name_kana`, `display_name_kanji`, `phone` | Added | [Terminal.Location](/api/terminal/locations/object?api-version=2025-09-30.clover), [terminal.Location.CreateParams](/api/terminal/locations/create?api-version=2025-09-30.clover), [terminal.Location.ModifyParams](/api/terminal/locations/update?api-version=2025-09-30.clover) |

| Fields | Change | From → to |
| --- | --- | --- |
| `terminal.Location.CreateParams.address` | Changed | `required → optional` |
| `terminal.Location.CreateParams.display_name` | Changed | `required → optional` |

#### PHP

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `address_kana`, `address_kanji`, `display_name_kana`, `display_name_kanji`, `phone` | Added | [Terminal.Location](/api/terminal/locations/object?api-version=2025-09-30.clover), [Terminal\Location.create().$params](/api/terminal/locations/create?api-version=2025-09-30.clover), [Terminal\Location.update().$params](/api/terminal/locations/update?api-version=2025-09-30.clover) |

| Fields | Change | From → to |
| --- | --- | --- |
| `Terminal\Location.create().$params.address` | Changed | `required → optional` |
| `Terminal\Location.create().$params.display_name` | Changed | `required → optional` |

#### Java

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `addressKana`, `addressKanji`, `displayNameKana`, `displayNameKanji`, `phone` | Added | [terminal.Location](/api/terminal/locations/object?api-version=2025-09-30.clover), [terminal.LocationCreateParams](/api/terminal/locations/create?api-version=2025-09-30.clover), [terminal.LocationUpdateParams](/api/terminal/locations/update?api-version=2025-09-30.clover) |

| Fields | Change | From → to |
| --- | --- | --- |
| `terminal.LocationCreateParams.address` | Changed | `required → optional` |
| `terminal.LocationCreateParams.displayName` | Changed | `required → optional` |

#### Node.js

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `address_kana`, `address_kanji`, `display_name_kana`, `display_name_kanji`, `phone` | Added | [Terminal.Location](/api/terminal/locations/object?api-version=2025-09-30.clover), [Terminal.LocationCreateParams](/api/terminal/locations/create?api-version=2025-09-30.clover), [Terminal.LocationUpdateParams](/api/terminal/locations/update?api-version=2025-09-30.clover) |

| Fields | Change | From → to |
| --- | --- | --- |
| `Terminal.LocationCreateParams.address` | Changed | `required → optional` |
| `Terminal.LocationCreateParams.display_name` | Changed | `required → optional` |

#### Go

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `AddressKana`, `AddressKanji`, `DisplayNameKana`, `DisplayNameKanji`, `Phone` | Added | [TerminalLocation](/api/terminal/locations/object?api-version=2025-09-30.clover), [TerminalLocationParams](/api/terminal/locations/update?api-version=2025-09-30.clover) |

#### .NET

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `AddressKana`, `AddressKanji`, `DisplayNameKana`, `DisplayNameKanji`, `Phone` | Added | [Terminal.Location](/api/terminal/locations/object?api-version=2025-09-30.clover), [Terminal.LocationCreateOptions](/api/terminal/locations/create?api-version=2025-09-30.clover), [Terminal.LocationUpdateOptions](/api/terminal/locations/update?api-version=2025-09-30.clover) |

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

- [Adds support for custom BBPOS WisePad 3 splash screens](https://docs.stripe.com/changelog/clover/2025-09-30/custom-bbpos-wisepad3-splash-screens.md)
