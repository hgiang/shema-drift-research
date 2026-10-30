# Adds PayPay settings to the Account object

## What’s new

We added two new fields to the [Account](https://docs.stripe.com/api/accounts/object.md?api-version=2025-08-27.basil) object to store additional information required for onboarding connected accounts to PayPay:

- `settings.paypay_payments.goods_type`
- `business_profile.specified_commercial_transactions_act_url`

## Impact

Connect platforms can now onboard connected accounts to PayPay by using the [Accounts](https://docs.stripe.com/api/accounts.md?api-version=2025-08-27.basil) API. PayPay requires additional information about the connected account to process onboarding requests. If you update any of these new fields, PayPay automatically attempts onboarding for the applicable connected account.

## Changes

#### REST API

| Parameters | Change | Resources or endpoints |
| --- | --- | --- |
| `specified_commercial_transactions_act_url` | Added | [Account#create.business_profile](/api/accounts/create?api-version=2025-08-27.basil#account_object-business_profile-specified_commercial_transactions_act_url), [Account#update.business_profile](/api/accounts/update?api-version=2025-08-27.basil#account_object-business_profile-specified_commercial_transactions_act_url), [Account.business_profile](/api/accounts/object?api-version=2025-08-27.basil#account_object-business_profile-specified_commercial_transactions_act_url) |
| `paypay_payments` | Added | [Account#create.settings](/api/accounts/create?api-version=2025-08-27.basil#create_account-settings-paypay_payments), [Account#update.settings](/api/accounts/update?api-version=2025-08-27.basil#update_account-settings-paypay_payments) |

#### Ruby

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `specified_commercial_transactions_act_url` | Added | [Account::BusinessProfile](/api/accounts/object?api-version=2025-08-27.basil#account_object-business_profile-specified_commercial_transactions_act_url), [Account::CreateParams::BusinessProfile](/api/accounts/create?api-version=2025-08-27.basil#account_object-business_profile-specified_commercial_transactions_act_url), [Account::UpdateParams::BusinessProfile](/api/accounts/update?api-version=2025-08-27.basil#account_object-business_profile-specified_commercial_transactions_act_url) |
| `paypay_payments` | Added | [Account::CreateParams::Setting](/api/accounts/create?api-version=2025-08-27.basil#create_account-settings-paypay_payments), [Account::UpdateParams::Setting](/api/accounts/update?api-version=2025-08-27.basil#update_account-settings-paypay_payments) |

#### Python

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `specified_commercial_transactions_act_url` | Added | [Account.BusinessProfile](/api/accounts/object?api-version=2025-08-27.basil#account_object-business_profile-specified_commercial_transactions_act_url), [Account.CreateParamsBusinessProfile](/api/accounts/create?api-version=2025-08-27.basil#account_object-business_profile-specified_commercial_transactions_act_url), [Account.ModifyParamsBusinessProfile](/api/accounts/update?api-version=2025-08-27.basil#account_object-business_profile-specified_commercial_transactions_act_url) |
| `paypay_payments` | Added | [Account.CreateParamsSetting](/api/accounts/create?api-version=2025-08-27.basil#create_account-settings-paypay_payments), [Account.ModifyParamsSetting](/api/accounts/update?api-version=2025-08-27.basil#update_account-settings-paypay_payments) |

#### PHP

This change doesn’t affect the PHP SDK.

#### Java

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `specifiedCommercialTransactionsActUrl` | Added | [Account.business_profile](/api/accounts/object?api-version=2025-08-27.basil#account_object-business_profile-specified_commercial_transactions_act_url), [AccountCreateParams.business_profile](/api/accounts/create?api-version=2025-08-27.basil#account_object-business_profile-specified_commercial_transactions_act_url), [AccountUpdateParams.business_profile](/api/accounts/update?api-version=2025-08-27.basil#account_object-business_profile-specified_commercial_transactions_act_url) |
| `paypayPayments` | Added | [AccountCreateParams.settings](/api/accounts/create?api-version=2025-08-27.basil#create_account-settings-paypay_payments), [AccountUpdateParams.settings](/api/accounts/update?api-version=2025-08-27.basil#update_account-settings-paypay_payments) |

#### Node.js

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `specified_commercial_transactions_act_url` | Added | [Account.business_profile](/api/accounts/object?api-version=2025-08-27.basil#account_object-business_profile-specified_commercial_transactions_act_url), [AccountCreateParams.business_profile](/api/accounts/create?api-version=2025-08-27.basil#account_object-business_profile-specified_commercial_transactions_act_url), [AccountUpdateParams.business_profile](/api/accounts/update?api-version=2025-08-27.basil#account_object-business_profile-specified_commercial_transactions_act_url) |
| `paypay_payments` | Added | [AccountCreateParams.settings](/api/accounts/create?api-version=2025-08-27.basil#create_account-settings-paypay_payments), [AccountUpdateParams.settings](/api/accounts/update?api-version=2025-08-27.basil#update_account-settings-paypay_payments) |

#### Go

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `SpecifiedCommercialTransactionsActURL` | Added | [AccountBusinessProfile](/api/accounts/object?api-version=2025-08-27.basil#account_object-business_profile-specified_commercial_transactions_act_url), [AccountBusinessProfileParams](/api/accounts/create?api-version=2025-08-27.basil#account_object-business_profile-specified_commercial_transactions_act_url) |
| `PaypayPayments` | Added | [AccountSettingsParams](/api/accounts/create?api-version=2025-08-27.basil#create_account-settings-paypay_payments) |

#### .NET

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `SpecifiedCommercialTransactionsActUrl` | Added | [Account.BusinessProfile](/api/accounts/object?api-version=2025-08-27.basil#account_object-business_profile-specified_commercial_transactions_act_url), [AccountBusinessProfileOptions](/api/accounts/create?api-version=2025-08-27.basil#account_object-business_profile-specified_commercial_transactions_act_url) |
| `PaypayPayments` | Added | [AccountSettingsOptions](/api/accounts/create?api-version=2025-08-27.basil#create_account-settings-paypay_payments) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2025-08-27.basil`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to [v15.5.0](https://github.com/stripe/stripe-ruby/releases/tag/v15.5.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to [v12.5.0](https://github.com/stripe/stripe-python/releases/tag/v12.5.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to [v17.6.0](https://github.com/stripe/stripe-php/releases/tag/v17.6.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to [v29.5.0](https://github.com/stripe/stripe-java/releases/tag/v29.5.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to [v18.5.0](https://github.com/stripe/stripe-node/releases/tag/v18.5.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to [v82.5.0](https://github.com/stripe/stripe-go/releases/tag/v82.5.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to [v48.5.0](https://github.com/stripe/stripe-dotnet/releases/tag/v48.5.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

## Related changes

- [Adds a Charge transaction ID for several payment methods](https://docs.stripe.com/changelog/basil/2025-08-27/transaction-id.md)
- [Adds the number of instalments for Alma payments to Charge objects](https://docs.stripe.com/changelog/basil/2025-08-27/alma-installments.md)
- [Adds support to include the IOF tax in the amount for Pix payments](https://docs.stripe.com/changelog/basil/2025-08-27/pix-payments-iof-tax.md)
- [Adds excluded payment method types to the Payment Intents API](https://docs.stripe.com/changelog/basil/2025-08-27/cs_add_excluded_payment_method_types_pi.md)
