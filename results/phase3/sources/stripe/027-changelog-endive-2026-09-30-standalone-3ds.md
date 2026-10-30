# Adds the Standalone 3D Secure API

## What’s new

Adds the [Standalone 3D Secure API](https://docs.stripe.com/payments/3d-secure/standalone-3d-secure.md), which lets you authenticate a card using 3D Secure independently of a Stripe payment. This enables you to incorporate Stripe’s 3D Secure authentication into a payment flow that you manage separately.

Use [3DS Authentications](https://docs.stripe.com/api/three-d-secure/authentication/object.md?api-version=2026-09-30.endive) to:

- [Create](https://docs.stripe.com/api/three-d-secure/authentication/create.md?api-version=2026-09-30.endive) an authentication.
- [Submit](https://docs.stripe.com/api/three-d-secure/authentication/submit.md?api-version=2026-09-30.endive) a created authentication.
- [Retrieve](https://docs.stripe.com/api/three-d-secure/authentication/retrieve.md?api-version=2026-09-30.endive) an authentication’s status and results.
- [List](https://docs.stripe.com/api/three-d-secure/authentication/list.md?api-version=2026-09-30.endive) your authentications.
- [Cancel](https://docs.stripe.com/api/three-d-secure/authentication/cancel.md?api-version=2026-09-30.endive) a pending authentication.

You can use the authentication result in your own payment flow. To learn how 3D Secure works and when to use it, see [3D Secure authentication](https://docs.stripe.com/payments/3d-secure.md).

## Impact

You can now perform 3D Secure authentication without creating or processing the corresponding payment on Stripe. This lets you add 3D Secure to payment flows where you manage payment creation and processing separately, while controlling when authentication begins and how to proceed with the payment in your own system.

## Changes

#### REST API

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [ThreeDSecure.Authentication](/api/three-d-secure/authentication/object?api-version=2026-09-30.endive#three_d_secure_authentication_object) |

| Endpoints | Change | Resource |
| --- | --- | --- |
| `cancel`, `create`, `list`, `retrieve`, `submit` | Added | [ThreeDSecure.Authentication](/api/three-d-secure/authentication/object?api-version=2026-09-30.endive#three_d_secure_authentication_object) |

#### Ruby

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [ThreeDSecure::Authentication](/api/three-d-secure/authentication/object?api-version=2026-09-30.endive#three_d_secure_authentication_object) |

| Methods | Change | Resource |
| --- | --- | --- |
| `cancel`, `create`, `list`, `retrieve`, `submit` | Added | [ThreeDSecure::Authentication](/api/three-d-secure/authentication/object?api-version=2026-09-30.endive#three_d_secure_authentication_object) |

#### Python

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [three_d_secure.Authentication](/api/three-d-secure/authentication/object?api-version=2026-09-30.endive#three_d_secure_authentication_object) |

| Methods | Change | Resource |
| --- | --- | --- |
| `cancel`, `create`, `list`, `retrieve`, `submit` | Added | [three_d_secure.Authentication](/api/three-d-secure/authentication/object?api-version=2026-09-30.endive#three_d_secure_authentication_object) |

#### PHP

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [ThreeDSecure.Authentication](/api/three-d-secure/authentication/object?api-version=2026-09-30.endive#three_d_secure_authentication_object) |

| Methods | Change | Resource |
| --- | --- | --- |
| `all`, `cancel`, `create`, `retrieve`, `submit` | Added | [ThreeDSecure.Authentication](/api/three-d-secure/authentication/object?api-version=2026-09-30.endive#three_d_secure_authentication_object) |

#### Java

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [threedsecure.Authentication](/api/three-d-secure/authentication/object?api-version=2026-09-30.endive#three_d_secure_authentication_object) |

| Methods | Change | Resource |
| --- | --- | --- |
| `cancel`, `create`, `list`, `retrieve`, `submit` | Added | [threedsecure.Authentication](/api/three-d-secure/authentication/object?api-version=2026-09-30.endive#three_d_secure_authentication_object) |

#### Node.js

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [ThreeDSecure.Authentication](/api/three-d-secure/authentication/object?api-version=2026-09-30.endive#three_d_secure_authentication_object) |

| Methods | Change | Resource |
| --- | --- | --- |
| `cancel`, `create`, `list`, `retrieve`, `submit` | Added | [ThreeDSecure.Authentication](/api/three-d-secure/authentication/object?api-version=2026-09-30.endive#three_d_secure_authentication_object) |

#### Go

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [ThreeDSecureAuthentication](/api/three-d-secure/authentication/object?api-version=2026-09-30.endive#three_d_secure_authentication_object) |

| Methods | Change | Resource |
| --- | --- | --- |
| `Cancel`, `Get`, `List`, `New`, `Submit` | Added | [ThreeDSecureAuthentication](/api/three-d-secure/authentication/object?api-version=2026-09-30.endive#three_d_secure_authentication_object) |

#### .NET

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [ThreeDSecure.Authentication](/api/three-d-secure/authentication/object?api-version=2026-09-30.endive#three_d_secure_authentication_object) |

| Methods | Change | Resource |
| --- | --- | --- |
| `Cancel`, `Create`, `Get`, `List`, `Submit` | Added | [ThreeDSecure.Authentication](/api/three-d-secure/authentication/object?api-version=2026-09-30.endive#three_d_secure_authentication_object) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2026-09-30.endive`
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

- [Removes the payment method types parameter from Checkout Sessions](https://docs.stripe.com/changelog/endive/2026-09-30/remove-payment-method-types-checkout-sessions.md)
- [Adds support for Data Share Only for 3D Secure authentication](https://docs.stripe.com/changelog/endive/2026-09-30/data-share-only.md)
- [Makes Payment Evaluation signal scores nullable](https://docs.stripe.com/changelog/endive/2026-09-30/payment-evaluations-nullable-score.md)
- [Removes PayTo-specific fields from Payment Methods](https://docs.stripe.com/changelog/endive/2026-09-30/removed-payto-fields.md)
- [Removes the payment method types parameter from Payment Intents and Setup Intents](https://docs.stripe.com/changelog/endive/2026-09-30/removes-the-payment-method-types-parameter-from-payment-intents-and-setup-intents.md)
- [Returns specific decline codes for BLIK payment failures](https://docs.stripe.com/changelog/endive/2026-09-30/blik-granular-decline-codes.md)
- [Deprecates the payment request button](https://docs.stripe.com/changelog/endive/2026-09-30/deprecate-payment-request-button.md)
- [Shows pending-authorization UI for MB WAY, Bizum, and BLIK with stripe.handleNextAction](https://docs.stripe.com/changelog/endive/2026-09-30/handle-next-action-mb-way-bizum-ui.md)
- [Removes support for the payment method types option in Elements](https://docs.stripe.com/changelog/endive/2026-09-30/remove-elements-deferred-intent-payment-method-types.md)
- [Saves Bancontact payment details for future off-session payments in Checkout](https://docs.stripe.com/changelog/endive/2026-09-30/bancontact-off-session-payments-checkout.md)
- [Adds support for SeQura payments](https://docs.stripe.com/changelog/endive/2026-09-30/sequra-payments.md)
- [Adds card-present payment methods to allowed payment method types](https://docs.stripe.com/changelog/endive/2026-09-30/card-present-and-interac-present-enum-values-for-allowed-payment-method-types.md)
- [Adds Link funding source group details on Payment Records](https://docs.stripe.com/changelog/endive/2026-09-30/link-funding-source-group-payment-records.md)
- [Adds early fraud warnings and fraudulent dispute signals for Payment Evaluations](https://docs.stripe.com/changelog/endive/2026-09-30/new-radar-signals-for-payment-evaluations.md)
- [Adds the ability to report cancelled payments](https://docs.stripe.com/changelog/endive/2026-09-30/reporting-canceled-payments.md)
- [Adds support for expanding the mandate on card payment method details](https://docs.stripe.com/changelog/endive/2026-09-30/expand-mandate-on-card-payments-details.md)
- [Adds the Payment Record property to the Payment Intent object](https://docs.stripe.com/changelog/endive/2026-09-30/payment-records-on-payment-intents.md)
- [Adds Link wallet details to Payment Records for card payments](https://docs.stripe.com/changelog/endive/2026-09-30/adds-link-wallet-details-to-payment-records-for-card-payments.md)
- [Adds 3D Secure versions 2.3.0 and 2.3.1 to Payment Records](https://docs.stripe.com/changelog/endive/2026-09-30/3d-secure-payment-records.md)
- [Adds support for BLIK recurring off-session payments](https://docs.stripe.com/changelog/endive/2026-09-30/blik-recurring-off-session-payments.md)
- [Adds PayPay support for one-time online payments in Japan](https://docs.stripe.com/changelog/endive/2026-09-30/paypay-payments-japan.md)
- [Exposes the network response electronic commerce indicator on card charges](https://docs.stripe.com/changelog/endive/2026-09-30/view-network-response-eci-on-card-charges.md)
- [Adds payment method type information for failed payments](https://docs.stripe.com/changelog/endive/2026-09-30/payment-method-type-payment-failures.md)
- [Adds MoMo payment method details to Payment Records](https://docs.stripe.com/changelog/endive/2026-09-30/adds-momo-payment-method-details-to-payment-records.md)
