# Adds support for reinstating Billing Credits on Invoice voiding

## What’s new

We added support for reinstating [Billing Credits](https://docs.stripe.com/billing/subscriptions/usage-based/billing-credits.md) when voiding an [Invoice](https://docs.stripe.com/invoicing.md).

## Impact

[Voiding an invoice](https://docs.stripe.com/api/invoices/void.md?api-version=2024-12-18.acacia) with credits applied reinstates the applied balance to the [credit grant](https://docs.stripe.com/api/billing/credit-grant.md?api-version=2024-12-18.acacia). If the credit grant is past the [expiration date](https://docs.stripe.com/api/billing/credit-grant/object.md?api-version=2024-12-18.acacia#billing_credit_grant_object-expires_at), the reinstated credits expire immediately.

See [Billing credits integration docs](https://docs.stripe.com/billing/subscriptions/usage-based/billing-credits.md#void-invoices-and-issue-credit-notes) to learn more.

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `credits_application_invoice_voided` | Added | [Billing.CreditBalanceTransaction.credit](/api/billing/credit-balance-transaction/object?api-version=2024-12-18.acacia#billing_credit_balance_transaction_object-credit) |

| Field | Change | From → to |
| --- | --- | --- |
| `Billing.CreditBalanceTransaction.credit.type` | Changed | `literal('credits_granted') → enum('credits_application_invoice_voided'|'credits_granted')` |

#### Ruby

This change doesn’t affect the Ruby SDK.

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `credits_application_invoice_voided` | Added | [stripe.billing.CreditBalanceTransaction.Credit](/api/billing/credit-balance-transaction/object?api-version=2024-12-18.acacia#billing_credit_balance_transaction_object-credit) |

| Value | Change | Enum |
| --- | --- | --- |
| `credits_application_invoice_voided` | Added | [stripe.billing.CreditBalanceTransaction.Credit.type](/api/billing/credit-balance-transaction/object?api-version=2024-12-18.acacia#billing_credit_balance_transaction_object-credit-type) |

#### PHP

This change doesn’t affect the PHP SDK.

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `credits_application_invoice_voided` | Added | [Billing.CreditBalanceTransaction.credit](/api/billing/credit-balance-transaction/object?api-version=2024-12-18.acacia#billing_credit_balance_transaction_object-credit) |

| Field | Change | From → to |
| --- | --- | --- |
| `Billing.CreditBalanceTransaction.credit.type` | Changed | `literal('credits_granted') → enum('credits_application_invoice_voided'|'credits_granted')` |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `credits_application_invoice_voided` | Added | [Billing.CreditBalanceTransaction.credit](/api/billing/credit-balance-transaction/object?api-version=2024-12-18.acacia#billing_credit_balance_transaction_object-credit) |

| Field | Change | From → to |
| --- | --- | --- |
| `Billing.CreditBalanceTransaction.credit.type` | Changed | `literal('credits_granted') → enum('credits_application_invoice_voided'|'credits_granted')` |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `CreditsApplicationInvoiceVoided` | Added | [BillingCreditBalanceTransactionCredit](/api/billing/credit-balance-transaction/object?api-version=2024-12-18.acacia#billing_credit_balance_transaction_object-credit) |

| Field | Change | From → to |
| --- | --- | --- |
| `BillingCreditBalanceTransactionCreditType` | Changed | `literal('credits_granted') → enum('credits_application_invoice_voided'|'credits_granted')` |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `CreditsApplicationInvoiceVoided` | Added | [BillingCreditBalanceTransactionCredit](/api/billing/credit-balance-transaction/object?api-version=2024-12-18.acacia#billing_credit_balance_transaction_object-credit) |

| Field | Change | From → to |
| --- | --- | --- |
| `BillingCreditBalanceTransactionCreditType` | Changed | `literal('credits_granted') → enum('credits_application_invoice_voided'|'credits_granted')` |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2024-12-18.acacia`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to [v13.3.0](https://github.com/stripe/stripe-ruby/releases/tag/v13.3.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to [v11.4.0](https://github.com/stripe/stripe-python/releases/tag/v11.4.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to [v16.4.0](https://github.com/stripe/stripe-php/releases/tag/v16.4.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to [v28.2.0](https://github.com/stripe/stripe-java/releases/tag/v28.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to [v17.5.0](https://github.com/stripe/stripe-node/releases/tag/v17.5.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to [v81.2.0](https://github.com/stripe/stripe-go/releases/tag/v81.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to [v47.2.0](https://github.com/stripe/stripe-dotnet/releases/tag/v47.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

## Related changes

- [Modify trial subscriptions created by Payment Links](https://docs.stripe.com/changelog/acacia/2024-12-18/add-trial-days-update-payment-links-api.md)
- [Billing Portal Configuration always returns period end date in responses](https://docs.stripe.com/changelog/acacia/2024-12-18/portal-config-schedule-at-period-end-required.md)
