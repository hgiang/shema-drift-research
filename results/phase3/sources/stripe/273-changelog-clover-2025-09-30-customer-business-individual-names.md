# Adds support for business and individual names on Customers

## What’s new

Adds [business_name](https://docs.stripe.com/api/customers/object.md?api-version=2025-09-30.clover#customer_object-business_name) and [individual_name](https://docs.stripe.com/api/customers/object.md?api-version=2025-09-30.clover#customer_object-individual_name) fields to [Customers](https://docs.stripe.com/api/customers/object.md?api-version=2025-09-30.clover).

## Impact

You can now save customers’ business and individual names. When you create a Customer without specifying the [name](https://docs.stripe.com/api/customers/object.md?api-version=2025-09-30.clover#customer_object-name), it’s automatically set to either the `business_name` or `individual_name`, prioritised in that order.

## Changes

#### REST API

| Parameters | Change | Resources or endpoints |
| --- | --- | --- |
| `business_name`, `individual_name` | Added | [Customer](/api/customers/object?api-version=2025-09-30.clover), [Customer#create](/api/customers/create?api-version=2025-09-30.clover), [Customer#update](/api/customers/update?api-version=2025-09-30.clover) |

#### Ruby

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `business_name`, `individual_name` | Added | [Customer](/api/customers/object?api-version=2025-09-30.clover), [Customer::CreateParams](/api/customers/create?api-version=2025-09-30.clover), [Customer::UpdateParams](/api/customers/update?api-version=2025-09-30.clover) |

#### Python

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `business_name`, `individual_name` | Added | [Customer](/api/customers/object?api-version=2025-09-30.clover), [Customer.CreateParams](/api/customers/create?api-version=2025-09-30.clover), [Customer.ModifyParams](/api/customers/update?api-version=2025-09-30.clover) |

#### PHP

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `business_name`, `individual_name` | Added | [Customer](/api/customers/object?api-version=2025-09-30.clover), [Customer.create().$params](/api/customers/create?api-version=2025-09-30.clover), [Customer.update().$params](/api/customers/update?api-version=2025-09-30.clover) |

#### Java

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `businessName`, `individualName` | Added | [Customer](/api/customers/object?api-version=2025-09-30.clover), [CustomerCreateParams](/api/customers/create?api-version=2025-09-30.clover), [CustomerUpdateParams](/api/customers/update?api-version=2025-09-30.clover) |

#### Node.js

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `business_name`, `individual_name` | Added | [Customer](/api/customers/object?api-version=2025-09-30.clover), [CustomerCreateParams](/api/customers/create?api-version=2025-09-30.clover), [CustomerUpdateParams](/api/customers/update?api-version=2025-09-30.clover) |

#### Go

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `BusinessName`, `IndividualName` | Added | [Customer](/api/customers/object?api-version=2025-09-30.clover), [CustomerParams](/api/customers/object?api-version=2025-09-30.clover) |

#### .NET

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `BusinessName`, `IndividualName` | Added | [Customer](/api/customers/object?api-version=2025-09-30.clover), [CustomerCreateOptions](/api/customers/create?api-version=2025-09-30.clover), [CustomerUpdateOptions](/api/customers/update?api-version=2025-09-30.clover) |

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
