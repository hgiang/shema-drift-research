# Replaces tax association status fields

## What’s new

Replaces the `status` and `status_details` parameters with [tax_transaction_attempts](https://docs.stripe.com/api/tax/associations/object.md?api-version=preview#tax_association_object-tax_transaction_attempts) for the [Tax Association](https://docs.stripe.com/api/tax/associations.md?api-version=2025-05-28.preview) resource.

## Why is this a breaking change?

We removed the `status` and `status_details` parameters and introduced a new `tax_transaction_attempts` parameter. To use this new parameter, you must update your integration to use the new version.

## Impact

If your integration uses the `status` and `status_details` fields, update your tax association integration to use the `tax_transaction_attempts` field.

## Changes

#### REST API

| Parameters | Change | Resources or endpoints |
| --- | --- | --- |
| `tax_transaction_attempts` | Added | [Tax.Association](/api/tax/associations/object?api-version=2025-05-28.preview) |
| `status`, `status_details` | Removed | [Tax.Association](/api/tax/associations/object?api-version=2025-05-28.preview) |

#### Ruby

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `tax_transaction_attempts` | Added | [Tax::Association](/api/tax/associations/object?api-version=2025-05-28.preview) |
| `status`, `status_details` | Removed | [Tax::Association](/api/tax/associations/object?api-version=2025-05-28.preview) |

#### Python

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `tax_transaction_attempts` | Added | [Tax.Association](/api/tax/associations/object?api-version=2025-05-28.preview) |
| `status`, `status_details` | Removed | [Tax.Association](/api/tax/associations/object?api-version=2025-05-28.preview) |

#### PHP

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `tax_transaction_attempts` | Added | [Tax.Association](/api/tax/associations/object?api-version=2025-05-28.preview) |
| `status`, `status_details` | Removed | [Tax.Association](/api/tax/associations/object?api-version=2025-05-28.preview) |

#### Java

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `taxTransactionAttempts` | Added | [tax.Association](/api/tax/associations/object?api-version=2025-05-28.preview) |
| `status`, `statusDetails` | Removed | [tax.Association](/api/tax/associations/object?api-version=2025-05-28.preview) |

#### Node.js

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `tax_transaction_attempts` | Added | [Tax.Association](/api/tax/associations/object?api-version=2025-05-28.preview) |
| `status`, `status_details` | Removed | [Tax.Association](/api/tax/associations/object?api-version=2025-05-28.preview) |

#### Go

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `TaxTransactionAttempts` | Added | [TaxAssociation](/api/tax/associations/object?api-version=2025-05-28.preview) |
| `Status`, `StatusDetails` | Removed | [TaxAssociation](/api/tax/associations/object?api-version=2025-05-28.preview) |

#### .NET

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `TaxTransactionAttempts` | Added | [Tax.Association](/api/tax/associations/object?api-version=2025-05-28.preview) |
| `Status`, `StatusDetails` | Removed | [Tax.Association](/api/tax/associations/object?api-version=2025-05-28.preview) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2025-05-28.preview`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to [v15.3.0-beta.1](https://github.com/stripe/stripe-ruby/releases/tag/v15.3.0-beta.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to [v12.3.0b1](https://github.com/stripe/stripe-python/releases/tag/v12.3.0b1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to [v17.4.0-beta.2](https://github.com/stripe/stripe-php/releases/tag/v17.4.0-beta.2)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to [v29.3.0-beta.1](https://github.com/stripe/stripe-java/releases/tag/v29.3.0-beta.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to [v18.3.0-beta.1](https://github.com/stripe/stripe-node/releases/tag/v18.3.0-beta.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to [v82.3.0-beta.1](https://github.com/stripe/stripe-go/releases/tag/v82.3.0-beta.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to [v48.3.0-beta.1](https://github.com/stripe/stripe-dotnet/releases/tag/v48.3.0-beta.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

## Related changes

- [Renames Payment Intent field for linking tax calculation](https://docs.stripe.com/changelog/basil/2025-05-28/rename-async-workflows.md)
