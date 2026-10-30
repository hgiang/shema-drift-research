# Adds the Shared Payment Granted Token for managing payment methods shared by agents

## What’s new

Adds the [Shared Payment Granted Token](https://docs.stripe.com/api/shared-payment/granted-token/.md?api-version=2026-04-22.preview) for managing shared payment tokens for agentic commerce use cases. The SharedPaymentGrantedToken object includes the [agent_details](https://docs.stripe.com/api/shared-payment/granted-token/object.md?api-version=2026-04-22.preview#shared_payment_granted_token_object-agent_details) and [usage_limits](https://docs.stripe.com/api/shared-payment/granted-token/object.md?api-version=2026-04-22.preview#shared_payment_granted_token_object-usage_limits) properties, which provide additional context for token usage.

After you receive a SharedPaymentGrantedToken, you can pass the token using the [payment_method_data.shared_payment_granted_token](https://docs.stripe.com/api/payment_intents/create.md?api-version=2026-04-22.preview#create_payment_intent-payment_method_data-shared_payment_granted_token) parameter on the [PaymentIntent](https://docs.stripe.com/api/payment_intents.md?api-version=2026-04-22.preview) to complete the payment.

This release also includes test helpers to support your integration development:

- [Create a SharedPaymentGrantedToken](https://docs.stripe.com/api/shared-payment/granted-token/create.md?api-version=2026-04-22.preview): Create a token to simulate one being shared by an agent.
- [Revoke a SharedPaymentGrantedToken](https://docs.stripe.com/api/shared-payment/granted-token/revoke.md?api-version=2026-04-22.preview): Revoke a token to test how your integration handles different revoked token scenarios.

## Impact

You can now use the SharedPaymentGrantedToken to accept payments made by authorised agents on a customer’s behalf. This can help expand your payment capabilities beyond traditional customer-initiated transactions.

To learn more, see [Shared payment tokens](https://docs.stripe.com/agentic-commerce/concepts/shared-payment-tokens.md).

## Changes

#### REST API

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [SharedPayment.GrantedToken](/api/shared-payment/granted-token/object?api-version=2026-04-22.preview#shared_payment_granted_token_object) |

| Endpoints | Change | Resources |
| --- | --- | --- |
| `retrieve` | Added | [SharedPayment.GrantedToken](/api/shared-payment/granted-token/object?api-version=2026-04-22.preview#shared_payment_granted_token_object) |
| `create`, `revoke` | Added | [SharedPayment.GrantedToken](/api/shared-payment/granted-token/object?api-version=2026-04-22.preview#shared_payment_granted_token_object) |

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `shared_payment_granted_token` | Added | [ConfirmationToken.testHelpers#create.payment_method_data](/api/confirmation_tokens/test_create?api-version=2026-04-22.preview#test_create-payment_method_data), [PaymentIntent#confirm.payment_method_data](/api/payment_intents/confirm?api-version=2026-04-22.preview#confirm_payment_intent-payment_method_data), [PaymentIntent#create.payment_method_data](/api/payment_intents/create?api-version=2026-04-22.preview#create_payment_intent-payment_method_data), [PaymentIntent#update.payment_method_data](/api/payment_intents/update?api-version=2026-04-22.preview#update_payment_intent-payment_method_data), [PaymentMethod](/api/payment_methods/object?api-version=2026-04-22.preview#payment_method_object), [SetupIntent#confirm.payment_method_data](/api/setup_intents/confirm?api-version=2026-04-22.preview#confirm_setup_intent-payment_method_data), [SetupIntent#create.payment_method_data](/api/setup_intents/create?api-version=2026-04-22.preview#create_setup_intent-payment_method_data), [SetupIntent#update.payment_method_data](/api/setup_intents/update?api-version=2026-04-22.preview#update_setup_intent-payment_method_data) |

#### Ruby

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [SharedPayment::GrantedToken](/api/shared-payment/granted-token/object?api-version=2026-04-22.preview#shared_payment_granted_token_object) |

| Methods | Change | Resources |
| --- | --- | --- |
| `retrieve` | Added | [SharedPayment::GrantedToken](/api/shared-payment/granted-token/object?api-version=2026-04-22.preview#shared_payment_granted_token_object) |
| `create`, `revoke` | Added | [SharedPayment::GrantedToken](/api/shared-payment/granted-token/object?api-version=2026-04-22.preview#shared_payment_granted_token_object) |

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `shared_payment_granted_token` | Added | [ConfirmationTokenCreateParams::PaymentMethodDatum](/api/confirmation_tokens/test_create?api-version=2026-04-22.preview#test_create-payment_method_data), [PaymentIntentConfirmParams::PaymentMethodDatum](/api/payment_intents/confirm?api-version=2026-04-22.preview#confirm_payment_intent-payment_method_data), [PaymentIntentCreateParams::PaymentMethodDatum](/api/payment_intents/create?api-version=2026-04-22.preview#create_payment_intent-payment_method_data), [PaymentIntentUpdateParams::PaymentMethodDatum](/api/payment_intents/update?api-version=2026-04-22.preview#update_payment_intent-payment_method_data), [PaymentMethod](/api/payment_methods/object?api-version=2026-04-22.preview#payment_method_object), [SetupIntentConfirmParams::PaymentMethodDatum](/api/setup_intents/confirm?api-version=2026-04-22.preview#confirm_setup_intent-payment_method_data), [SetupIntentCreateParams::PaymentMethodDatum](/api/setup_intents/create?api-version=2026-04-22.preview#create_setup_intent-payment_method_data), [SetupIntentUpdateParams::PaymentMethodDatum](/api/setup_intents/update?api-version=2026-04-22.preview#update_setup_intent-payment_method_data) |

#### Python

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [shared_payment.GrantedToken](/api/shared-payment/granted-token/object?api-version=2026-04-22.preview#shared_payment_granted_token_object) |

| Methods | Change | Resources |
| --- | --- | --- |
| `retrieve` | Added | [shared_payment.GrantedToken](/api/shared-payment/granted-token/object?api-version=2026-04-22.preview#shared_payment_granted_token_object) |
| `create`, `revoke` | Added | [shared_payment.GrantedToken](/api/shared-payment/granted-token/object?api-version=2026-04-22.preview#shared_payment_granted_token_object) |

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `shared_payment_granted_token` | Added | [ConfirmationTokenCreateParamsPaymentMethodDatum](/api/confirmation_tokens/test_create?api-version=2026-04-22.preview#test_create-payment_method_data), [PaymentIntentConfirmParamsPaymentMethodDatum](/api/payment_intents/confirm?api-version=2026-04-22.preview#confirm_payment_intent-payment_method_data), [PaymentIntentCreateParamsPaymentMethodDatum](/api/payment_intents/create?api-version=2026-04-22.preview#create_payment_intent-payment_method_data), [PaymentIntentModifyParamsPaymentMethodDatum](/api/payment_intents/update?api-version=2026-04-22.preview#update_payment_intent-payment_method_data), [PaymentMethod](/api/payment_methods/object?api-version=2026-04-22.preview#payment_method_object), [SetupIntentConfirmParamsPaymentMethodDatum](/api/setup_intents/confirm?api-version=2026-04-22.preview#confirm_setup_intent-payment_method_data), [SetupIntentCreateParamsPaymentMethodDatum](/api/setup_intents/create?api-version=2026-04-22.preview#create_setup_intent-payment_method_data), [SetupIntentModifyParamsPaymentMethodDatum](/api/setup_intents/update?api-version=2026-04-22.preview#update_setup_intent-payment_method_data) |

#### PHP

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [SharedPayment.GrantedToken](/api/shared-payment/granted-token/object?api-version=2026-04-22.preview#shared_payment_granted_token_object) |

| Methods | Change | Resources |
| --- | --- | --- |
| `retrieve` | Added | [SharedPayment.GrantedToken](/api/shared-payment/granted-token/object?api-version=2026-04-22.preview#shared_payment_granted_token_object) |
| `create`, `revoke` | Added | [SharedPayment.GrantedToken](/api/shared-payment/granted-token/object?api-version=2026-04-22.preview#shared_payment_granted_token_object) |

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `shared_payment_granted_token` | Added | [ConfirmationToken.create().$params.payment_method_datum](/api/confirmation_tokens/test_create?api-version=2026-04-22.preview#test_create-payment_method_data), [PaymentIntent.confirm().$params.payment_method_datum](/api/payment_intents/confirm?api-version=2026-04-22.preview#confirm_payment_intent-payment_method_data), [PaymentIntent.create().$params.payment_method_datum](/api/payment_intents/create?api-version=2026-04-22.preview#create_payment_intent-payment_method_data), [PaymentIntent.update().$params.payment_method_datum](/api/payment_intents/update?api-version=2026-04-22.preview#update_payment_intent-payment_method_data), [PaymentMethod](/api/payment_methods/object?api-version=2026-04-22.preview#payment_method_object), [SetupIntent.confirm().$params.payment_method_datum](/api/setup_intents/confirm?api-version=2026-04-22.preview#confirm_setup_intent-payment_method_data), [SetupIntent.create().$params.payment_method_datum](/api/setup_intents/create?api-version=2026-04-22.preview#create_setup_intent-payment_method_data), [SetupIntent.update().$params.payment_method_datum](/api/setup_intents/update?api-version=2026-04-22.preview#update_setup_intent-payment_method_data) |

#### Java

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [sharedpayment.GrantedToken](/api/shared-payment/granted-token/object?api-version=2026-04-22.preview#shared_payment_granted_token_object) |

| Methods | Change | Resources |
| --- | --- | --- |
| `retrieve` | Added | [sharedpayment.GrantedToken](/api/shared-payment/granted-token/object?api-version=2026-04-22.preview#shared_payment_granted_token_object) |
| `create`, `revoke` | Added | [sharedpayment.GrantedToken](/api/shared-payment/granted-token/object?api-version=2026-04-22.preview#shared_payment_granted_token_object) |

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `sharedPaymentGrantedToken` | Added | [ConfirmationTokenCreateParams.payment_method_data](/api/confirmation_tokens/test_create?api-version=2026-04-22.preview#test_create-payment_method_data), [PaymentIntentConfirmParams.payment_method_data](/api/payment_intents/confirm?api-version=2026-04-22.preview#confirm_payment_intent-payment_method_data), [PaymentIntentCreateParams.payment_method_data](/api/payment_intents/create?api-version=2026-04-22.preview#create_payment_intent-payment_method_data), [PaymentIntentUpdateParams.payment_method_data](/api/payment_intents/update?api-version=2026-04-22.preview#update_payment_intent-payment_method_data), [PaymentMethod](/api/payment_methods/object?api-version=2026-04-22.preview#payment_method_object), [SetupIntentConfirmParams.payment_method_data](/api/setup_intents/confirm?api-version=2026-04-22.preview#confirm_setup_intent-payment_method_data), [SetupIntentCreateParams.payment_method_data](/api/setup_intents/create?api-version=2026-04-22.preview#create_setup_intent-payment_method_data), [SetupIntentUpdateParams.payment_method_data](/api/setup_intents/update?api-version=2026-04-22.preview#update_setup_intent-payment_method_data) |

#### Node.js

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [SharedPayment.GrantedToken](/api/shared-payment/granted-token/object?api-version=2026-04-22.preview#shared_payment_granted_token_object) |

| Methods | Change | Resources |
| --- | --- | --- |
| `retrieve` | Added | [SharedPayment.GrantedToken](/api/shared-payment/granted-token/object?api-version=2026-04-22.preview#shared_payment_granted_token_object) |
| `create`, `revoke` | Added | [SharedPayment.GrantedToken](/api/shared-payment/granted-token/object?api-version=2026-04-22.preview#shared_payment_granted_token_object) |

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `shared_payment_granted_token` | Added | [ConfirmationTokenCreateParams.testHelpers.payment_method_data](/api/confirmation_tokens/test_create?api-version=2026-04-22.preview#test_create-payment_method_data), [PaymentIntentConfirmParams.payment_method_data](/api/payment_intents/confirm?api-version=2026-04-22.preview#confirm_payment_intent-payment_method_data), [PaymentIntentCreateParams.payment_method_data](/api/payment_intents/create?api-version=2026-04-22.preview#create_payment_intent-payment_method_data), [PaymentIntentUpdateParams.payment_method_data](/api/payment_intents/update?api-version=2026-04-22.preview#update_payment_intent-payment_method_data), [PaymentMethod](/api/payment_methods/object?api-version=2026-04-22.preview#payment_method_object), [SetupIntentConfirmParams.payment_method_data](/api/setup_intents/confirm?api-version=2026-04-22.preview#confirm_setup_intent-payment_method_data), [SetupIntentCreateParams.payment_method_data](/api/setup_intents/create?api-version=2026-04-22.preview#create_setup_intent-payment_method_data), [SetupIntentUpdateParams.payment_method_data](/api/setup_intents/update?api-version=2026-04-22.preview#update_setup_intent-payment_method_data) |

#### Go

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [SharedPaymentGrantedToken](/api/shared-payment/granted-token/object?api-version=2026-04-22.preview#shared_payment_granted_token_object) |

| Methods | Change | Resources |
| --- | --- | --- |
| `Get` | Added | [SharedPaymentGrantedToken](/api/shared-payment/granted-token/object?api-version=2026-04-22.preview#shared_payment_granted_token_object) |
| `New`, `Revoke` | Added | [SharedPaymentGrantedToken](/api/shared-payment/granted-token/object?api-version=2026-04-22.preview#shared_payment_granted_token_object) |

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `SharedPaymentGrantedToken` | Added | [ConfirmationTokenPaymentMethodDataParams](/api/confirmation_tokens/test_create?api-version=2026-04-22.preview#test_create-payment_method_data), [PaymentIntentConfirmPaymentMethodDataParams](/api/payment_intents/confirm?api-version=2026-04-22.preview#confirm_payment_intent-payment_method_data), [PaymentIntentPaymentMethodDataParams](/api/payment_intents/create?api-version=2026-04-22.preview#create_payment_intent-payment_method_data), [PaymentMethod](/api/payment_methods/object?api-version=2026-04-22.preview#payment_method_object), [SetupIntentConfirmPaymentMethodDataParams](/api/setup_intents/confirm?api-version=2026-04-22.preview#confirm_setup_intent-payment_method_data), [SetupIntentPaymentMethodDataParams](/api/setup_intents/create?api-version=2026-04-22.preview#create_setup_intent-payment_method_data) |

#### .NET

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [SharedPayment.GrantedToken](/api/shared-payment/granted-token/object?api-version=2026-04-22.preview#shared_payment_granted_token_object) |

| Methods | Change | Resources |
| --- | --- | --- |
| `Get` | Added | [SharedPayment.GrantedToken](/api/shared-payment/granted-token/object?api-version=2026-04-22.preview#shared_payment_granted_token_object) |
| `Create`, `Revoke` | Added | [SharedPayment.GrantedToken](/api/shared-payment/granted-token/object?api-version=2026-04-22.preview#shared_payment_granted_token_object) |

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `SharedPaymentGrantedToken` | Added | [ConfirmationTokenPaymentMethodDataOptions](/api/confirmation_tokens/test_create?api-version=2026-04-22.preview#test_create-payment_method_data), [PaymentIntentPaymentMethodDataOptions](/api/payment_intents/create?api-version=2026-04-22.preview#create_payment_intent-payment_method_data), [PaymentMethod](/api/payment_methods/object?api-version=2026-04-22.preview#payment_method_object), [SetupIntentPaymentMethodDataOptions](/api/setup_intents/create?api-version=2026-04-22.preview#create_setup_intent-payment_method_data) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2026-04-22.preview`
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

- [Adds the SharedPaymentIssuedToken resource to allow agents to give sellers scoped access to a customer’s credentials](https://docs.stripe.com/changelog/dahlia/2026-04-22/shared-payment-issued-token.md)
- [Adds the Orchestrated Commerce Agreements API to manage relationships for agentic commerce integrations](https://docs.stripe.com/changelog/dahlia/2026-04-22/orchestrated-commerce-agreements-api.md)
