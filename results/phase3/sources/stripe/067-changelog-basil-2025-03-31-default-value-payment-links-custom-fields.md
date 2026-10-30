# Adds default value to custom fields on Payment Links

## What’s new

Adds the `default_value` parameter to the existing [custom_fields[][text]](https://docs.stripe.com/api/payment-link/create.md#create_payment_link-custom_fields-text), [custom_fields[][numeric]](https://docs.stripe.com/api/payment-link/create.md#create_payment_link-custom_fields-numeric) and [custom_fields[][dropdown]](https://docs.stripe.com/api/payment-link/create.md#create_payment_link-custom_fields-dropdown) parameters on the [Create a Payment Link](https://docs.stripe.com/api/payment-link/create.md?api-version=2025-03-31.basil) and [Update a Payment Link](https://docs.stripe.com/api/payment-link/update.md?api-version=2025-03-31.basil) endpoints.

## Impact

Payment Links users can now provide a default value when using custom fields. Default values prefill the form field on the payment page.

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `default_value` | Added | `PaymentLink#create.custom_fields[].dropdown`, `PaymentLink#create.custom_fields[].numeric`, `PaymentLink#create.custom_fields[].text`, `PaymentLink#update.custom_fields[].dropdown`, `PaymentLink#update.custom_fields[].numeric`, `PaymentLink#update.custom_fields[].text`, `PaymentLink.custom_fields[].dropdown`, `PaymentLink.custom_fields[].numeric`, `PaymentLink.custom_fields[].text` |

#### Ruby

This change doesn’t affect the Ruby SDK.

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `default_value` | Added | `PaymentLink.CreateParamsCustomFieldDropdown`, `PaymentLink.CreateParamsCustomFieldNumeric`, `PaymentLink.CreateParamsCustomFieldText`, `PaymentLink.CustomField.Dropdown`, `PaymentLink.CustomField.Numeric`, `PaymentLink.CustomField.Text`, `PaymentLink.UpdateParamsCustomFieldDropdown`, `PaymentLink.UpdateParamsCustomFieldNumeric`, `PaymentLink.UpdateParamsCustomFieldText` |

#### PHP

This change doesn’t affect the PHP SDK.

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `defaultValue` | Added | `PaymentLink.custom_fields[].dropdown`, `PaymentLink.custom_fields[].numeric`, `PaymentLink.custom_fields[].text`, `PaymentLinkCreateParams.custom_fields[].dropdown`, `PaymentLinkCreateParams.custom_fields[].numeric`, `PaymentLinkCreateParams.custom_fields[].text`, `PaymentLinkUpdateParams.custom_fields[].dropdown`, `PaymentLinkUpdateParams.custom_fields[].numeric`, `PaymentLinkUpdateParams.custom_fields[].text` |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `default_value` | Added | `PaymentLink.custom_fields[].dropdown`, `PaymentLink.custom_fields[].numeric`, `PaymentLink.custom_fields[].text`, `PaymentLinkCreateParams.custom_fields[].dropdown`, `PaymentLinkCreateParams.custom_fields[].numeric`, `PaymentLinkCreateParams.custom_fields[].text`, `PaymentLinkUpdateParams.custom_fields[].dropdown`, `PaymentLinkUpdateParams.custom_fields[].numeric`, `PaymentLinkUpdateParams.custom_fields[].text` |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `DefaultValue` | Added | `PaymentLinkCustomFieldsDropdownParams`, `PaymentLinkCustomFieldsDropdown`, `PaymentLinkCustomFieldsNumericParams`, `PaymentLinkCustomFieldsNumeric`, `PaymentLinkCustomFieldsTextParams`, `PaymentLinkCustomFieldsText` |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `DefaultValue` | Added | `PaymentLinkCustomFieldsDropdownOptions`, `PaymentLinkCustomFieldsDropdown`, `PaymentLinkCustomFieldsNumericOptions`, `PaymentLinkCustomFieldsNumeric`, `PaymentLinkCustomFieldsTextOptions`, `PaymentLinkCustomFieldsText` |

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
