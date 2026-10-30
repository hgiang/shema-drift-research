# Adds active status filtering to payment method configurations

## What’s new

You can now filter payment method configurations by their active status using the new [active](https://docs.stripe.com/api/payment_method_configurations/list.md?api-version=2026-05-27.dahlia#list_payment_method_configurations-active) parameter on the [List PaymentMethodConfigurations](https://docs.stripe.com/api/payment_method_configurations/list.md?api-version=2026-05-27.dahlia) endpoint.

## Impact

You can retrieve active [payment method configurations](https://docs.stripe.com/payments/payment-method-configurations.md) without needing to filter results on your end. This is useful when you need to display only active payment options to customers or when managing configurations in your Dashboard.

**Specific actions you can take:**

- Filter for active configurations by including `active=true` in your API request.
- Retrieve inactive configurations by including `active=false`.
- Retrieve all configurations, regardless of status, by omitting the `active` parameter entirely.
- Update your existing list calls to leverage this filtering for better performance.
- Modify your customer-facing payment flows to show only active payment methods by adding `active=true`.

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `active` | Added | [PaymentMethodConfiguration#list](/api/payment_method_configurations/list?api-version=2026-05-27.dahlia#list_payment_method_configurations) |

#### Ruby

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `active` | Added | [PaymentMethodConfigurationListParams](/api/payment_method_configurations/list?api-version=2026-05-27.dahlia#list_payment_method_configurations) |

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `active` | Added | [PaymentMethodConfigurationListParams](/api/payment_method_configurations/list?api-version=2026-05-27.dahlia#list_payment_method_configurations) |

#### PHP

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `active` | Added | [PaymentMethodConfiguration.all().$params](/api/payment_method_configurations/list?api-version=2026-05-27.dahlia#list_payment_method_configurations) |

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `active` | Added | [PaymentMethodConfigurationListParams](/api/payment_method_configurations/list?api-version=2026-05-27.dahlia#list_payment_method_configurations) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `active` | Added | [PaymentMethodConfigurationListParams](/api/payment_method_configurations/list?api-version=2026-05-27.dahlia#list_payment_method_configurations) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `Active` | Added | [PaymentMethodConfigurationListParams](/api/payment_method_configurations/list?api-version=2026-05-27.dahlia#list_payment_method_configurations) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `Active` | Added | [PaymentMethodConfigurationListOptions](/api/payment_method_configurations/list?api-version=2026-05-27.dahlia#list_payment_method_configurations) |

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

- [Adds support for Twint as a payment method for recurring payments](https://docs.stripe.com/changelog/dahlia/2026-05-27/recurring-payments-twint.md)
- [Adds destination payment description and metadata support to transfer data](https://docs.stripe.com/changelog/dahlia/2026-05-27/transfer-data-destination-payment-description-and-metadata.md)
- [Adds card brand restrictions to Payment Links](https://docs.stripe.com/changelog/dahlia/2026-05-27/adds-card-brand-restrictions-to-payment-links.md)
- [Adds support for Scalapay payments](https://docs.stripe.com/changelog/dahlia/2026-05-27/scalapay-payments.md)
