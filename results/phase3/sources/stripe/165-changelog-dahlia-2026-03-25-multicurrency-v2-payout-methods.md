# Adds multicurrency support for v2 payout methods

## What’s new

Adds the ability to create [v2 Payout Methods](https://docs.stripe.com/api/v2/money-management/payout-methods.md?api-version=2026-03-25.preview) that can receive [payouts](https://docs.stripe.com/payouts.md) in foreign currencies. Previously, v2 Payout Methods could only be US-issued debit cards that receive payouts in USD or bank accounts that receive payouts in their country’s local currency.

Adds the ability to specify a payout method’s currency by adding the required `currency` parameter to endpoints that create v2 Payout Methods and adding the `supported_currencies` property to objects that represent v2 Payout Methods. The `supported_currencies` property is a single-element array that contains the currency specified in the `currency` parameter.

`currency` and `supported_currencies` are at the top level of creation requests and responses, respectively, for [US Bank Accounts](https://docs.stripe.com/api/v2/core/vault/us-bank-accounts.md?api-version=2026-03-25.preview) and [GB Bank Accounts](https://docs.stripe.com/api/v2/core/vault/gb-bank-accounts.md?api-version=2026-03-25.preview), and in card or bank account hashes for [Payout Methods](https://docs.stripe.com/api/v2/money-management/payout-methods.md?api-version=2026-03-25.preview) and [Outbound Setup Intents](https://docs.stripe.com/api/v2/money-management/outbound-setup-intents.md?api-version=2026-03-25.preview).

Also adds the `currencies` property to the [countries](https://docs.stripe.com/api/v2/money-management/payout-methods-bank-account-specs/object.md?api-version=2026-03-25.preview#v2_payout_methods_bank_account_spec_object-countries) hash on the Payout Methods Bank Account Spec object. This property contains currency-specific credential requirements.

Also adds multicurrency payout support to GB bank accounts by making the following updates to the GB Bank Accounts API:

- Makes the [sort_code](https://docs.stripe.com/api/v2/core/vault/gb-bank-accounts/create.md?api-version=2026-03-25.preview#v2_create_gb_bank_accounts-sort_code) and [account_number](https://docs.stripe.com/api/v2/core/vault/gb-bank-accounts/create.md?api-version=2026-03-25.preview#v2_create_gb_bank_accounts-account_number) parameters only required for GBP accounts
- Adds the [iban](https://docs.stripe.com/api/v2/core/vault/gb-bank-accounts/create.md?api-version=2026-03-25.preview#v2_create_gb_bank_accounts-iban) parameter for non-GBP currencies

> #### v2 money movement flows and Global Payouts
> 
> v2 money movement flows such as [OutboundPayments](https://docs.stripe.com/api/v2/money-management/outbound-payments.md?api-version=2026-03-25.preview), [OutboundTransfers](https://docs.stripe.com/api/v2/money-management/outbound-transfers.md?api-version=2026-03-25.preview), and [InboundTransfers](https://docs.stripe.com/api/v2/money-management/inbound-transfers.md?api-version=2026-03-25.preview) don’t support multicurrency `PayoutMethods`. You can use them only with `PayoutMethods` set up with the local currency.

## Why is this a breaking change?

The `currency` parameter is now required when creating v2 Payout Method credentials. If your integration creates v2 Payout Methods using US Bank Accounts, GB Bank Accounts, or Outbound Setup Intents, you must update your code to specify a `currency` value.

## Impact

v2 Payout Methods now support foreign currencies for payouts. They don’t default to the payout account’s local currency, so you now need to specify the currency when creating them. Attempting to create a v2 Payout Method without specifying the `currency` parameter will fail.

Multicurrency support on v2 Payout Methods allows you to use them for payouts to connected accounts instead of using [External Bank Accounts](https://docs.stripe.com/api/external_accounts.md?api-version=2026-03-25.preview) or [External Account Cards](https://docs.stripe.com/api/external_account_cards.md?api-version=2026-03-25.preview).

When [creating GB Bank Accounts](https://docs.stripe.com/api/v2/core/vault/gb-bank-accounts/create.md?api-version=2026-03-25.preview), you now only need to include the `sort_code` and `account_number` for payout accounts that use GBP. For GB Bank Accounts that receive payouts in other currencies, specify the `iban` parameter instead. You need to include either only the `iban` or both the `sort_code` and `account_number`, depending on the currency.

Each Payout Method can support only one currency. To represent a payout account that accepts multiple currencies, you need to create a separate object for each supported currency.

To identify a Payout Method’s currency, check the `supported_currencies` property of the corresponding [US Bank Account](https://docs.stripe.com/api/v2/core/vault/us-bank-accounts/object.md?api-version=2026-03-25.preview#v2_us_bank_account_object-supported_currencies) or [GBBankAccount](https://docs.stripe.com/api/v2/core/vault/gb-bank-accounts/object.md?api-version=2026-03-25.preview#v2_gb_bank_account_object-supported_currencies), or the Payout Method’s [bank_account](https://docs.stripe.com/api/v2/money-management/payout-methods/object.md?api-version=2026-03-25.preview#v2_payout_method_object-bank_account-supported_currencies) or [card](https://docs.stripe.com/api/v2/money-management/payout-methods/object.md?api-version=2026-03-25.preview#v2_payout_method_object-card-supported_currencies) hash.

## Changes

#### REST API

| Parameters | Change | Resources or endpoints |
| --- | --- | --- |
| `supported_currencies` | Added | [V2.Core.Vault.GbBankAccount](/api/v2/core/vault/gb-bank-accounts/object?api-version=2026-03-25.preview), [V2.Core.Vault.UsBankAccount](/api/v2/core/vault/us-bank-accounts/object?api-version=2026-03-25.preview), [V2.MoneyManagement.PayoutMethod.card](/api/v2/money-management/payout-methods/object?api-version=2026-03-25.preview#v2_payout_method_object-card) |
| `currencies` | Added | [V2.MoneyManagement.PayoutMethodsBankAccountSpec.countries.value.fields[]](/api/v2/money-management/payout-methods-bank-account-specs/object?api-version=2026-03-25.preview#v2_payout_methods_bank_account_spec_object-countries-value-fields) |
| `currency` | Added | [V2.Core.Vault.GbBankAccount#create](/api/v2/core/vault/gb-bank-accounts/create?api-version=2026-03-25.preview), [V2.Core.Vault.UsBankAccount#create](/api/v2/core/vault/us-bank-accounts/create?api-version=2026-03-25.preview), [V2.MoneyManagement.OutboundSetupIntent#create.payout_method_data.bank_account](/api/v2/money-management/outbound-setup-intents/create?api-version=2026-03-25.preview#v2_create_outbound_setup_intents-payout_method_data-bank_account), [V2.MoneyManagement.OutboundSetupIntent#create.payout_method_data.card](/api/v2/money-management/outbound-setup-intents/create?api-version=2026-03-25.preview#v2_create_outbound_setup_intents-payout_method_data-card), [V2.MoneyManagement.OutboundSetupIntent#update.payout_method_data.bank_account](/api/v2/money-management/outbound-setup-intents/update?api-version=2026-03-25.preview#v2_update_outbound_setup_intents-payout_method_data-bank_account), [V2.MoneyManagement.OutboundSetupIntent#update.payout_method_data.card](/api/v2/money-management/outbound-setup-intents/update?api-version=2026-03-25.preview#v2_update_outbound_setup_intents-payout_method_data-card) |
| `iban` | Added | [V2.Core.Vault.GbBankAccount#create](/api/v2/core/vault/gb-bank-accounts/create?api-version=2026-03-25.preview) |

| Value | Change | Enum |
| --- | --- | --- |
| `currency` | Added | `invalid_payment_method` |

| Fields | Change | From → to |
| --- | --- | --- |
| `V2.Core.Vault.GbBankAccount#create.sort_code`, `V2.Core.Vault.GbBankAccount.sort_code` | Changed | `required → optional` |
| `V2.Core.Vault.GbBankAccount#create.account_number` | Changed | `required → optional` |

#### Ruby

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `supported_currencies` | Added | [V2::Core::Vault::GbBankAccount](/api/v2/core/vault/gb-bank-accounts/object?api-version=2026-03-25.preview), [V2::Core::Vault::UsBankAccount](/api/v2/core/vault/us-bank-accounts/object?api-version=2026-03-25.preview), [V2::MoneyManagement::PayoutMethod::Card](/api/v2/money-management/payout-methods/object?api-version=2026-03-25.preview#v2_payout_method_object-card) |
| `currencies` | Added | [V2::MoneyManagement::PayoutMethodsBankAccountSpec::Country::Field](/api/v2/money-management/payout-methods-bank-account-specs/object?api-version=2026-03-25.preview#v2_payout_methods_bank_account_spec_object-countries-value-fields) |
| `currency` | Added | [V2::Core::Vault::GbBankAccountCreateParams](/api/v2/core/vault/gb-bank-accounts/create?api-version=2026-03-25.preview), [V2::Core::Vault::UsBankAccountCreateParams](/api/v2/core/vault/us-bank-accounts/create?api-version=2026-03-25.preview), [V2::MoneyManagement::OutboundSetupIntentCreateParams::PayoutMethodDatum::BankAccount](/api/v2/money-management/outbound-setup-intents/create?api-version=2026-03-25.preview#v2_create_outbound_setup_intents-payout_method_data-bank_account), [V2::MoneyManagement::OutboundSetupIntentCreateParams::PayoutMethodDatum::Card](/api/v2/money-management/outbound-setup-intents/create?api-version=2026-03-25.preview#v2_create_outbound_setup_intents-payout_method_data-card), [V2::MoneyManagement::OutboundSetupIntentUpdateParams::PayoutMethodDatum::BankAccount](/api/v2/money-management/outbound-setup-intents/update?api-version=2026-03-25.preview#v2_update_outbound_setup_intents-payout_method_data-bank_account), [V2::MoneyManagement::OutboundSetupIntentUpdateParams::PayoutMethodDatum::Card](/api/v2/money-management/outbound-setup-intents/update?api-version=2026-03-25.preview#v2_update_outbound_setup_intents-payout_method_data-card) |
| `iban` | Added | [V2::Core::Vault::GbBankAccountCreateParams](/api/v2/core/vault/gb-bank-accounts/create?api-version=2026-03-25.preview) |

| Fields | Change | From → to |
| --- | --- | --- |
| `V2::Core::Vault::GbBankAccount.sort_code`, `V2::Core::Vault::GbBankAccountCreateParams.sort_code` | Changed | `required → optional` |
| `V2::Core::Vault::GbBankAccountCreateParams.account_number` | Changed | `required → optional` |

#### Python

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `supported_currencies` | Added | [V2.Core.Vault.GbBankAccount](/api/v2/core/vault/gb-bank-accounts/object?api-version=2026-03-25.preview), [V2.Core.Vault.UsBankAccount](/api/v2/core/vault/us-bank-accounts/object?api-version=2026-03-25.preview), [V2.MoneyManagement.PayoutMethod.Card](/api/v2/money-management/payout-methods/object?api-version=2026-03-25.preview#v2_payout_method_object-card) |
| `currencies` | Added | [V2.MoneyManagement.PayoutMethodsBankAccountSpec.Country.Field](/api/v2/money-management/payout-methods-bank-account-specs/object?api-version=2026-03-25.preview#v2_payout_methods_bank_account_spec_object-countries-value-fields) |
| `currency` | Added | [v2.core.vault.GbBankAccountCreateParams](/api/v2/core/vault/gb-bank-accounts/create?api-version=2026-03-25.preview), [v2.core.vault.UsBankAccountCreateParams](/api/v2/core/vault/us-bank-accounts/create?api-version=2026-03-25.preview), [v2.money_management.OutboundSetupIntentCreateParamsPayoutMethodDatumBankAccount](/api/v2/money-management/outbound-setup-intents/create?api-version=2026-03-25.preview#v2_create_outbound_setup_intents-payout_method_data-bank_account), [v2.money_management.OutboundSetupIntentCreateParamsPayoutMethodDatumCard](/api/v2/money-management/outbound-setup-intents/create?api-version=2026-03-25.preview#v2_create_outbound_setup_intents-payout_method_data-card), [v2.money_management.OutboundSetupIntentModifyParamsPayoutMethodDatumBankAccount](/api/v2/money-management/outbound-setup-intents/update?api-version=2026-03-25.preview#v2_update_outbound_setup_intents-payout_method_data-bank_account), [v2.money_management.OutboundSetupIntentModifyParamsPayoutMethodDatumCard](/api/v2/money-management/outbound-setup-intents/update?api-version=2026-03-25.preview#v2_update_outbound_setup_intents-payout_method_data-card) |
| `iban` | Added | [v2.core.vault.GbBankAccountCreateParams](/api/v2/core/vault/gb-bank-accounts/create?api-version=2026-03-25.preview) |

| Value | Change | Enum |
| --- | --- | --- |
| `currency` | Added | `InvalidPaymentMethodError` |

| Fields | Change | From → to |
| --- | --- | --- |
| `V2.Core.Vault.GbBankAccount.sort_code`, `v2.core.vault.GbBankAccountCreateParams.sort_code` | Changed | `required → optional` |
| `v2.core.vault.GbBankAccountCreateParams.account_number` | Changed | `required → optional` |

#### PHP

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `supported_currencies` | Added | [V2.Core.Vault.GbBankAccount](/api/v2/core/vault/gb-bank-accounts/object?api-version=2026-03-25.preview), [V2.Core.Vault.UsBankAccount](/api/v2/core/vault/us-bank-accounts/object?api-version=2026-03-25.preview), [V2.MoneyManagement.PayoutMethod.card](/api/v2/money-management/payout-methods/object?api-version=2026-03-25.preview#v2_payout_method_object-card) |
| `currencies` | Added | [V2.MoneyManagement.PayoutMethodsBankAccountSpec.countries.value.fields[]](/api/v2/money-management/payout-methods-bank-account-specs/object?api-version=2026-03-25.preview#v2_payout_methods_bank_account_spec_object-countries-value-fields) |
| `currency` | Added | [V2\Core\Vault\GbBankAccount.create().$params](/api/v2/core/vault/gb-bank-accounts/create?api-version=2026-03-25.preview), [V2\Core\Vault\UsBankAccount.create().$params](/api/v2/core/vault/us-bank-accounts/create?api-version=2026-03-25.preview), [V2\MoneyManagement\OutboundSetupIntent.create().$params.payout_method_datum.bank_account](/api/v2/money-management/outbound-setup-intents/create?api-version=2026-03-25.preview#v2_create_outbound_setup_intents-payout_method_data-bank_account), [V2\MoneyManagement\OutboundSetupIntent.create().$params.payout_method_datum.card](/api/v2/money-management/outbound-setup-intents/create?api-version=2026-03-25.preview#v2_create_outbound_setup_intents-payout_method_data-card), [V2\MoneyManagement\OutboundSetupIntent.update().$params.payout_method_datum.bank_account](/api/v2/money-management/outbound-setup-intents/update?api-version=2026-03-25.preview#v2_update_outbound_setup_intents-payout_method_data-bank_account), [V2\MoneyManagement\OutboundSetupIntent.update().$params.payout_method_datum.card](/api/v2/money-management/outbound-setup-intents/update?api-version=2026-03-25.preview#v2_update_outbound_setup_intents-payout_method_data-card) |
| `iban` | Added | [V2\Core\Vault\GbBankAccount.create().$params](/api/v2/core/vault/gb-bank-accounts/create?api-version=2026-03-25.preview) |

| Value | Change | Enum |
| --- | --- | --- |
| `currency` | Added | `InvalidPaymentMethodException` |

| Fields | Change | From → to |
| --- | --- | --- |
| `V2.Core.Vault.GbBankAccount.sort_code`, `V2\Core\Vault\GbBankAccount.create().$params.sort_code` | Changed | `required → optional` |
| `V2\Core\Vault\GbBankAccount.create().$params.account_number` | Changed | `required → optional` |

#### Java

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `supportedCurrencies` | Added | [v2.core.vault.GbBankAccount](/api/v2/core/vault/gb-bank-accounts/object?api-version=2026-03-25.preview), [v2.core.vault.UsBankAccount](/api/v2/core/vault/us-bank-accounts/object?api-version=2026-03-25.preview), [v2.moneymanagement.PayoutMethod.card](/api/v2/money-management/payout-methods/object?api-version=2026-03-25.preview#v2_payout_method_object-card) |
| `currencies` | Added | [v2.moneymanagement.PayoutMethodsBankAccountSpec.countries.value.fields[]](/api/v2/money-management/payout-methods-bank-account-specs/object?api-version=2026-03-25.preview#v2_payout_methods_bank_account_spec_object-countries-value-fields) |
| `currency` | Added | [v2.core.vault.GbBankAccountCreateParams](/api/v2/core/vault/gb-bank-accounts/create?api-version=2026-03-25.preview), [v2.core.vault.UsBankAccountCreateParams](/api/v2/core/vault/us-bank-accounts/create?api-version=2026-03-25.preview), [v2.moneymanagement.OutboundSetupIntentCreateParams.payout_method_data.bank_account](/api/v2/money-management/outbound-setup-intents/create?api-version=2026-03-25.preview#v2_create_outbound_setup_intents-payout_method_data-bank_account), [v2.moneymanagement.OutboundSetupIntentCreateParams.payout_method_data.card](/api/v2/money-management/outbound-setup-intents/create?api-version=2026-03-25.preview#v2_create_outbound_setup_intents-payout_method_data-card), [v2.moneymanagement.OutboundSetupIntentUpdateParams.payout_method_data.bank_account](/api/v2/money-management/outbound-setup-intents/update?api-version=2026-03-25.preview#v2_update_outbound_setup_intents-payout_method_data-bank_account), [v2.moneymanagement.OutboundSetupIntentUpdateParams.payout_method_data.card](/api/v2/money-management/outbound-setup-intents/update?api-version=2026-03-25.preview#v2_update_outbound_setup_intents-payout_method_data-card) |
| `iban` | Added | [v2.core.vault.GbBankAccountCreateParams](/api/v2/core/vault/gb-bank-accounts/create?api-version=2026-03-25.preview) |

| Value | Change | Enum |
| --- | --- | --- |
| `currency` | Added | `InvalidPaymentMethodException` |

| Fields | Change | From → to |
| --- | --- | --- |
| `v2.core.vault.GbBankAccountCreateParams.accountNumber` | Changed | `required → optional` |
| `v2.core.vault.GbBankAccountCreateParams.sortCode` | Changed | `required → optional` |

#### Node.js

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `supported_currencies` | Added | [V2.Core.Vault.GbBankAccount](/api/v2/core/vault/gb-bank-accounts/object?api-version=2026-03-25.preview), [V2.Core.Vault.UsBankAccount](/api/v2/core/vault/us-bank-accounts/object?api-version=2026-03-25.preview), [V2.MoneyManagement.PayoutMethod.card](/api/v2/money-management/payout-methods/object?api-version=2026-03-25.preview#v2_payout_method_object-card) |
| `currencies` | Added | [V2.MoneyManagement.PayoutMethodsBankAccountSpec.countries.value.fields[]](/api/v2/money-management/payout-methods-bank-account-specs/object?api-version=2026-03-25.preview#v2_payout_methods_bank_account_spec_object-countries-value-fields) |
| `currency` | Added | [V2.Core.Vault.GbBankAccountCreateParams](/api/v2/core/vault/gb-bank-accounts/create?api-version=2026-03-25.preview), [V2.Core.Vault.UsBankAccountCreateParams](/api/v2/core/vault/us-bank-accounts/create?api-version=2026-03-25.preview), [V2.MoneyManagement.OutboundSetupIntentCreateParams.payout_method_data.bank_account](/api/v2/money-management/outbound-setup-intents/create?api-version=2026-03-25.preview#v2_create_outbound_setup_intents-payout_method_data-bank_account), [V2.MoneyManagement.OutboundSetupIntentCreateParams.payout_method_data.card](/api/v2/money-management/outbound-setup-intents/create?api-version=2026-03-25.preview#v2_create_outbound_setup_intents-payout_method_data-card), [V2.MoneyManagement.OutboundSetupIntentUpdateParams.payout_method_data.bank_account](/api/v2/money-management/outbound-setup-intents/update?api-version=2026-03-25.preview#v2_update_outbound_setup_intents-payout_method_data-bank_account), [V2.MoneyManagement.OutboundSetupIntentUpdateParams.payout_method_data.card](/api/v2/money-management/outbound-setup-intents/update?api-version=2026-03-25.preview#v2_update_outbound_setup_intents-payout_method_data-card) |
| `iban` | Added | [V2.Core.Vault.GbBankAccountCreateParams](/api/v2/core/vault/gb-bank-accounts/create?api-version=2026-03-25.preview) |

| Value | Change | Enum |
| --- | --- | --- |
| `currency` | Added | `InvalidPaymentMethodError` |

| Fields | Change | From → to |
| --- | --- | --- |
| `V2.Core.Vault.GbBankAccount.sort_code`, `V2.Core.Vault.GbBankAccountCreateParams.sort_code` | Changed | `required → optional` |
| `V2.Core.Vault.GbBankAccountCreateParams.account_number` | Changed | `required → optional` |

#### Go

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `SupportedCurrencies` | Added | [V2CoreVaultGbBankAccount](/api/v2/core/vault/gb-bank-accounts/object?api-version=2026-03-25.preview), [V2CoreVaultUsBankAccount](/api/v2/core/vault/us-bank-accounts/object?api-version=2026-03-25.preview), [V2MoneyManagementPayoutMethodCard](/api/v2/money-management/payout-methods/object?api-version=2026-03-25.preview#v2_payout_method_object-card) |
| `Currencies` | Added | [V2MoneyManagementPayoutMethodsBankAccountSpecCountriesField](/api/v2/money-management/payout-methods-bank-account-specs/object?api-version=2026-03-25.preview#v2_payout_methods_bank_account_spec_object-countries-value-fields) |
| `Currency` | Added | [V2CoreVaultGbBankAccountParams](/api/v2/core/vault/gb-bank-accounts/create?api-version=2026-03-25.preview), [V2CoreVaultUsBankAccountParams](/api/v2/core/vault/us-bank-accounts/create?api-version=2026-03-25.preview), [V2MoneyManagementOutboundSetupIntentPayoutMethodDataBankAccountParams](/api/v2/money-management/outbound-setup-intents/create?api-version=2026-03-25.preview#v2_create_outbound_setup_intents-payout_method_data-bank_account), [V2MoneyManagementOutboundSetupIntentPayoutMethodDataCardParams](/api/v2/money-management/outbound-setup-intents/create?api-version=2026-03-25.preview#v2_create_outbound_setup_intents-payout_method_data-card) |
| `IBAN` | Added | [V2CoreVaultGbBankAccountParams](/api/v2/core/vault/gb-bank-accounts/create?api-version=2026-03-25.preview) |

| Value | Change | Enum |
| --- | --- | --- |
| `currency` | Added | `InvalidPaymentMethodError` |

#### .NET

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `SupportedCurrencies` | Added | [V2.Core.Vault.GbBankAccount](/api/v2/core/vault/gb-bank-accounts/object?api-version=2026-03-25.preview), [V2.Core.Vault.UsBankAccount](/api/v2/core/vault/us-bank-accounts/object?api-version=2026-03-25.preview), [V2.MoneyManagement.PayoutMethod.Card](/api/v2/money-management/payout-methods/object?api-version=2026-03-25.preview#v2_payout_method_object-card) |
| `Currencies` | Added | [V2.MoneyManagement.PayoutMethodsBankAccountSpec.Countries.Field](/api/v2/money-management/payout-methods-bank-account-specs/object?api-version=2026-03-25.preview#v2_payout_methods_bank_account_spec_object-countries-value-fields) |
| `Currency` | Added | [V2.Core.Vault.GbBankAccountCreateOptions](/api/v2/core/vault/gb-bank-accounts/create?api-version=2026-03-25.preview), [V2.Core.Vault.UsBankAccountCreateOptions](/api/v2/core/vault/us-bank-accounts/create?api-version=2026-03-25.preview), [V2MoneyManagementOutboundSetupIntentPayoutMethodDataBankAccountOptions](/api/v2/money-management/outbound-setup-intents/create?api-version=2026-03-25.preview#v2_create_outbound_setup_intents-payout_method_data-bank_account), [V2MoneyManagementOutboundSetupIntentPayoutMethodDataCardOptions](/api/v2/money-management/outbound-setup-intents/create?api-version=2026-03-25.preview#v2_create_outbound_setup_intents-payout_method_data-card) |
| `Iban` | Added | [V2.Core.Vault.GbBankAccountCreateOptions](/api/v2/core/vault/gb-bank-accounts/create?api-version=2026-03-25.preview) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2026-03-25.preview`
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

- [Restricts Accounts v2 identity properties for some Global Payouts use cases](https://docs.stripe.com/changelog/dahlia/2026-03-25/accounts-identity-fields-global-payouts.md)
- [Adds the restricted property to the Payout Method object](https://docs.stripe.com/changelog/dahlia/2026-03-25/payout-method-restricted-property.md)
- [Expands Global Payouts cross-border payout destinations to three additional countries](https://docs.stripe.com/changelog/dahlia/2026-03-25/cross-border-payouts-new-countries.md)
