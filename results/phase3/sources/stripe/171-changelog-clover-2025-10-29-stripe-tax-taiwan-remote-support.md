# Adds support for remote sellers in Taiwan to Stripe Tax

## What’s new

Stripe Tax now supports Taiwan for all remote businesses selling digital goods.

## Impact

This change expands the geographic coverage of the [Tax Registrations API](https://docs.stripe.com/api/tax/registrations.md?api-version=2025-10-29.clover) to include the Taiwan Simplified registration, enabling automatic tax calculation and collection.

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `tw` | Added | [Tax.Registration#create.country_options](/api/tax/registrations/create?api-version=2025-10-29.clover#create_tax_registration-country_options), [Tax.Registration.country_options](/api/tax/registrations/object?api-version=2025-10-29.clover#tax_registration_object-country_options) |

#### Ruby

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `tw` | Added | [Tax::Registration::CountryOption](/api/tax/registrations/object?api-version=2025-10-29.clover#tax_registration_object-country_options), [Tax::Registration::CreateParams::CountryOption](/api/tax/registrations/create?api-version=2025-10-29.clover#create_tax_registration-country_options) |

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `tw` | Added | [Tax.Registration.CountryOption](/api/tax/registrations/object?api-version=2025-10-29.clover#tax_registration_object-country_options), [tax.Registration.CreateParamsCountryOption](/api/tax/registrations/create?api-version=2025-10-29.clover#create_tax_registration-country_options) |

#### PHP

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `tw` | Added | [Tax.Registration.country_options](/api/tax/registrations/object?api-version=2025-10-29.clover#tax_registration_object-country_options), [Tax\Registration.create().$params.country_option](/api/tax/registrations/create?api-version=2025-10-29.clover#create_tax_registration-country_options) |

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `tw` | Added | [tax.Registration.country_options](/api/tax/registrations/object?api-version=2025-10-29.clover#tax_registration_object-country_options), [tax.RegistrationCreateParams.country_options](/api/tax/registrations/create?api-version=2025-10-29.clover#create_tax_registration-country_options) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `tw` | Added | [Tax.Registration.country_options](/api/tax/registrations/object?api-version=2025-10-29.clover#tax_registration_object-country_options), [Tax.RegistrationCreateParams.country_options](/api/tax/registrations/create?api-version=2025-10-29.clover#create_tax_registration-country_options) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `Tw` | Added | [TaxRegistrationCountryOptions](/api/tax/registrations/object?api-version=2025-10-29.clover#tax_registration_object-country_options), [TaxRegistrationCountryOptionsParams](/api/tax/registrations/create?api-version=2025-10-29.clover#create_tax_registration-country_options) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `Tw` | Added | [Tax.Registration.CountryOptions](/api/tax/registrations/object?api-version=2025-10-29.clover#tax_registration_object-country_options), [TaxRegistrationCountryOptionsOptions](/api/tax/registrations/create?api-version=2025-10-29.clover#create_tax_registration-country_options) |

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

- [Adds third-party tax providers for automatic tax calculation](https://docs.stripe.com/changelog/clover/2025-10-29/automatic-tax-provider.md)
