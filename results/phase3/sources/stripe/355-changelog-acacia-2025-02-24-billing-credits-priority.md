# Credit grants can now be prioritised

## What’s new

This change adds the [priority](https://docs.stripe.com/api/billing/credit-grant/object.md?api-version=2025-02-24.acacia#billing_credit_grant_object-priority) parameter to the [Credit Grant](https://docs.stripe.com/api/billing/credit-grant.md?api-version=2025-02-24.acacia) resource.

## Impact

You can set custom priorities for applying credit grants. When you apply multiple credit grants to an invoice or line item, you can set [priority](https://docs.stripe.com/api/billing/credit-grant/object.md?api-version=2025-02-24.acacia#billing_credit_grant_object-priority) values for each credit grant to specify which grants should be evaluated first. These values range from `0` to `100`, with lower values indicating higher priority.

Learn how to [apply credit grants](https://docs.stripe.com/billing/subscriptions/usage-based/billing-credits.md#multiple-credit-grants).

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `priority` | Added | `Billing.CreditGrant#create`, [Billing.CreditGrant](/api/billing/credit-grant?api-version=2025-02-24.acacia) |

#### Ruby

This change doesn’t affect the Ruby SDK.

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `priority` | Added | `stripe.billing.CreditGrant.CreateParams`, `stripe.billing.CreditGrant` |

#### PHP

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `priority` | Added | [Billing.CreditGrant](/api/billing/credit-grant?api-version=2025-02-24.acacia) |

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `priority` | Added | [Billing.CreditGrant](/api/billing/credit-grant?api-version=2025-02-24.acacia), `billing.CreditGrantCreateParams` |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `priority` | Added | `Billing.CreditGrantCreateParams`, [Billing.CreditGrant](/api/billing/credit-grant?api-version=2025-02-24.acacia) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `Priority` | Added | `BillingCreditGrantParams`, `BillingCreditGrant` |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `Priority` | Added | `Billing.CreditGrantCreateOptions`, `BillingCreditGrant` |

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

- [Credit grants can now be applied to specific prices](https://docs.stripe.com/changelog/acacia/2025-02-24/billing-credits-price-level-applicability.md)
