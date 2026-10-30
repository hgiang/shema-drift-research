# Credit grants can now be applied to specific prices

## What’s new

When you [create a credit grant](https://docs.stripe.com/api/billing/credit-grant/create.md?api-version=2025-02-24.acacia#create_billing_credit_grant-applicability_config-scope-price_type), you can now define the [scope](https://docs.stripe.com/api/billing/credit-grant/create.md?lang=curl&api-version=2025-02-24.acacia#create_billing_credit_grant-applicability_config-scope) of credit grants to cover a list of specific `prices` or a [price_type](https://docs.stripe.com/api/billing/credit-grant/create.md?api-version=2025-02-24.acacia#create_billing_credit_grant-applicability_config-scope-price_type) to apply to the credit grant. You must specify either `prices` or `price_type` when you create the credit grant. Currently, you can only specify metered prices in the `prices` list and only `metered` is supported for the `price_type`.

## Impact

This change enables granular control over which prices a credit grant can apply to. The new fields allow you to retrieve a balance summary for all credit grants that apply to a given list of prices.

## Changes

#### REST API

| Parameters | Change | Resources or endpoints |
| --- | --- | --- |
| `price_type`, `prices` | Added | `Billing.CreditBalanceSummary#retrieve.filter.applicability_scope`, `Billing.CreditGrant#create.applicability_config.scope`, `Billing.CreditGrant.applicability_config.scope` |

#### Ruby

This change doesn’t affect the Ruby SDK.

#### Python

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `price_type` | Added | `stripe.billing.CreditBalanceSummary.RetrieveParamsFilterApplicabilityScope`, `stripe.billing.CreditGrant.CreateParamsApplicabilityConfigScope`, `stripe.billing.CreditGrant.ApplicabilityConfig.Scope` |
| `prices` | Added | `stripe.billing.CreditBalanceSummary.RetrieveParamsFilterApplicabilityScope`, `stripe.billing.CreditGrant.CreateParamsApplicabilityConfigScope`, `stripe.billing.CreditGrant.ApplicabilityConfig.Scope` |

#### PHP

This change doesn’t affect the PHP SDK.

#### Java

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `price_type`, `prices` | Added | `Billing.CreditGrant.applicability_config.scope`, `billing.CreditBalanceSummaryRetrieveParams.filter.applicability_scope`, `billing.CreditGrantCreateParams.applicability_config.scope` |

#### Node.js

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `price_type`, `prices` | Added | `Billing.CreditBalanceSummaryRetrieveParams.filter.applicability_scope`, `Billing.CreditGrant.applicability_config.scope`, `Billing.CreditGrantCreateParams.applicability_config.scope` |

#### Go

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `PriceType`, `Prices` | Added | `BillingCreditBalanceSummaryFilterApplicabilityScopeParams`, `BillingCreditGrantApplicabilityConfigScopeParams`, `BillingCreditGrantApplicabilityConfigScope` |

#### .NET

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `PriceType`, `Prices` | Added | `BillingCreditBalanceSummaryFilterApplicabilityScopeOptions`, `BillingCreditGrantApplicabilityConfigScopeOptions`, `BillingCreditGrantApplicabilityConfigScope` |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2025-02-24.acacia`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to [v13.5.0](https://github.com/stripe/stripe-ruby/releases/tag/v13.5.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to [v11.6.0](https://github.com/stripe/stripe-python/releases/tag/v11.6.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to [v16.6.0](https://github.com/stripe/stripe-php/releases/tag/v16.6.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to [v28.4.0](https://github.com/stripe/stripe-java/releases/tag/v28.4.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to [v17.7.0](https://github.com/stripe/stripe-node/releases/tag/v17.7.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to [v81.4.0](https://github.com/stripe/stripe-go/releases/tag/v81.4.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to [v47.4.0](https://github.com/stripe/stripe-dotnet/releases/tag/v47.4.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

## Related changes

- [Credit grants can now be prioritised](https://docs.stripe.com/changelog/acacia/2025-02-24/billing-credits-priority.md)
