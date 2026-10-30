# Tax Registration API now supports twelve new countries

## What’s new

Adds support for Aruba, Azerbaijan, Bangladesh, Benin, Burkina Faso, Cameroon, Cape Verde, Ethiopia, India, Kyrgyzstan, Laos and the Philippines in the [Tax Registration API](https://docs.stripe.com/api/tax/registrations.md?api-version=2025-04-30.basil).

## Impact

This change expands the geographic coverage of the Tax Registration resource to include the twelve countries listed below. It allows businesses operating in or selling to these countries to register and manage their tax information through Stripe.

- `aw`: Aruba
- `az`: Azerbaijan
- `bd`: Bangladesh
- `bf`: Burkina Faso
- `bj`: Benin
- `cm`: Cameroon
- `cv`: Cape Verde
- `et`: Ethiopia
- `in`: India
- `kg`: Kyrgyzstan
- `la`: Laos
- `ph`: Philippines

## Changes

#### REST API

| Parameters | Change | Resources or endpoints |
| --- | --- | --- |
| `aw`, `az`, `bd`, `bf`, `bj`, `cm`, `cv`, `et`, `in`, `kg`, `la`, `ph` | Added | [Tax.Registration#create.country_options](/api/tax/registrations/create?api-version=2025-04-30.basil#tax_registration_create-country_options), [Tax.Registration.country_options](/api/tax/registrations/object?api-version=2025-04-30.basil#tax_registration_object-country_options) |

#### Ruby

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `aw`, `az`, `bd`, `bf`, `bj`, `cm`, `cv`, `et`, `in`, `kg`, `la`, `ph` | Added | [Tax::Registration::CountryOption](/api/tax/registrations/object?api-version=2025-04-30.basil#tax_registration_object-country_options), [Tax::Registration::CreateParams::CountryOption](/api/tax/registrations/create?api-version=2025-04-30.basil#tax_registration_create-country_options) |

#### Python

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `aw`, `az`, `bd`, `bf`, `bj`, `cm`, `cv`, `et`, `in`, `kg`, `la`, `ph` | Added | [Tax.Registration.CountryOption](/api/tax/registrations/object?api-version=2025-04-30.basil#tax_registration_object-country_options), [tax.Registration.CreateParamsCountryOption](/api/tax/registrations/create?api-version=2025-04-30.basil#tax_registration_create-country_options), [tax.RegistrationService.CreateParamsCountryOption](/api/tax/registrations/create?api-version=2025-04-30.basil#tax_registration_create-country_options) |

#### PHP

This change doesn’t affect the PHP SDK.

#### Java

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `aw`, `az`, `bd`, `bf`, `bj`, `cm`, `cv`, `et`, `in`, `kg`, `la`, `ph` | Added | [tax.Registration.country_options](/api/tax/registrations/object?api-version=2025-04-30.basil#tax_registration_object-country_options), [tax.RegistrationCreateParams.country_options](/api/tax/registrations/create?api-version=2025-04-30.basil#tax_registration_create-country_options) |

#### Node.js

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `aw`, `az`, `bd`, `bf`, `bj`, `cm`, `cv`, `et`, `in`, `kg`, `la`, `ph` | Added | [Tax.Registration.country_options](/api/tax/registrations/object?api-version=2025-04-30.basil#tax_registration_object-country_options), [Tax.RegistrationCreateParams.country_options](/api/tax/registrations/create?api-version=2025-04-30.basil#tax_registration_create-country_options) |

#### Go

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `Aw`, `Az`, `Bd`, `Bf`, `Bj`, `Cm`, `Cv`, `ET`, `In`, `Kg`, `La`, `Ph` | Added | [TaxRegistrationCountryOptionsParams](/api/tax/registrations/create?api-version=2025-04-30.basil#tax_registration_create-country_options), [TaxRegistrationCountryOptions](/api/tax/registrations/object?api-version=2025-04-30.basil#tax_registration_object-country_options) |

#### .NET

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `Aw`, `Az`, `Bd`, `Bf`, `Bj`, `Cm`, `Cv`, `Et`, `In`, `Kg`, `La`, `Ph` | Added | [Tax.Registration.CountryOptions](/api/tax/registrations/object?api-version=2025-04-30.basil#tax_registration_object-country_options), [TaxRegistrationCountryOptionsOptions](/api/tax/registrations/create?api-version=2025-04-30.basil#tax_registration_create-country_options) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2025-04-30.basil`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to [v15.1.0](https://github.com/stripe/stripe-ruby/releases/tag/v15.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to [v12.1.0](https://github.com/stripe/stripe-python/releases/tag/v12.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to [v17.2.0](https://github.com/stripe/stripe-php/releases/tag/v17.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to [v29.1.0](https://github.com/stripe/stripe-java/releases/tag/v29.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to [v18.1.0](https://github.com/stripe/stripe-node/releases/tag/v18.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to [v82.1.0](https://github.com/stripe/stripe-go/releases/tag/v82.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to [v48.1.0](https://github.com/stripe/stripe-dotnet/releases/tag/v48.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

## Related changes

- [Adds support for tax ID types in ten new countries](https://docs.stripe.com/changelog/basil/2025-04-30/add-tax-ids.md)
