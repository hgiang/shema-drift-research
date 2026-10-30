# Adds a new Smart Disputes management feature to Account Session embedded components

## What’s new

Adds a new boolean [smart_disputes_management](https://docs.stripe.com/api/account_sessions/create.md?api-version=2026-07-29.dahlia#create_account_session-components-disputes_list-features-smart_disputes_management) parameter to the [features](https://docs.stripe.com/api/account_sessions/create.md?api-version=2026-07-29.dahlia#create_account_session-components-disputes_list-features) hash on the following embedded components when you [create an Account Session](https://docs.stripe.com/api/account_sessions/create.md?api-version=2026-07-29.dahlia):

- [disputes_list](https://docs.stripe.com/api/account_sessions/create.md?api-version=2026-07-29.dahlia#create_account_session-components-disputes_list)
- [payment_details](https://docs.stripe.com/api/account_sessions/create.md?api-version=2026-07-29.dahlia#create_account_session-components-payment_details)
- [payment_disputes](https://docs.stripe.com/api/account_sessions/create.md?api-version=2026-07-29.dahlia#create_account_session-components-payment_disputes)
- [payments](https://docs.stripe.com/api/account_sessions/create.md?api-version=2026-07-29.dahlia#create_account_session-components-payments)

The `smart_disputes_management` parameter uses the value of `dispute_management` by default. You can enable `smart_disputes_management` only when [dispute_management](https://docs.stripe.com/api/account_sessions/create.md?api-version=2026-07-29.dahlia#create_account_session-components-disputes_list-features-dispute_management) is also enabled. Setting `smart_disputes_management` to true while `dispute_management` is false returns a `400` error.

## Impact

You can now disable Smart Disputes for each supported embedded component by setting `smart_disputes_management` to `false` in the component’s `features` object. Existing integrations aren’t affected. The parameter defaults to the value of `dispute_management`, so you don’t need to make any changes unless you want to explicitly control this behaviour.

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `smart_disputes_management` | Added | [AccountSession#create.components.disputes_list.features](/api/account_sessions/create?api-version=2026-07-29.dahlia#create_account_session-components-disputes_list-features), [AccountSession#create.components.payment_details.features](/api/account_sessions/create?api-version=2026-07-29.dahlia#create_account_session-components-payment_details-features), [AccountSession#create.components.payment_disputes.features](/api/account_sessions/create?api-version=2026-07-29.dahlia#create_account_session-components-payment_disputes-features), [AccountSession#create.components.payments.features](/api/account_sessions/create?api-version=2026-07-29.dahlia#create_account_session-components-payments-features), [AccountSession.components.disputes_list.features](/api/account_sessions/object?api-version=2026-07-29.dahlia#account_session_object-components-disputes_list-features), [AccountSession.components.payment_details.features](/api/account_sessions/object?api-version=2026-07-29.dahlia#account_session_object-components-payment_details-features), [AccountSession.components.payment_disputes.features](/api/account_sessions/object?api-version=2026-07-29.dahlia#account_session_object-components-payment_disputes-features), [AccountSession.components.payments.features](/api/account_sessions/object?api-version=2026-07-29.dahlia#account_session_object-components-payments-features) |

#### Ruby

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `smart_disputes_management` | Added | [AccountSession::Component::DisputesList::Feature](/api/account_sessions/object?api-version=2026-07-29.dahlia#account_session_object-components-disputes_list-features), [AccountSession::Component::Payment::Feature](/api/account_sessions/object?api-version=2026-07-29.dahlia#account_session_object-components-payments-features), [AccountSession::Component::PaymentDetail::Feature](/api/account_sessions/object?api-version=2026-07-29.dahlia#account_session_object-components-payment_details-features), [AccountSession::Component::PaymentDispute::Feature](/api/account_sessions/object?api-version=2026-07-29.dahlia#account_session_object-components-payment_disputes-features), [AccountSessionCreateParams::Component::DisputesList::Feature](/api/account_sessions/create?api-version=2026-07-29.dahlia#create_account_session-components-disputes_list-features), [AccountSessionCreateParams::Component::Payment::Feature](/api/account_sessions/create?api-version=2026-07-29.dahlia#create_account_session-components-payments-features), [AccountSessionCreateParams::Component::PaymentDetail::Feature](/api/account_sessions/create?api-version=2026-07-29.dahlia#create_account_session-components-payment_details-features), [AccountSessionCreateParams::Component::PaymentDispute::Feature](/api/account_sessions/create?api-version=2026-07-29.dahlia#create_account_session-components-payment_disputes-features) |

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `smart_disputes_management` | Added | [AccountSession.Component.DisputesList.Feature](/api/account_sessions/object?api-version=2026-07-29.dahlia#account_session_object-components-disputes_list-features), [AccountSession.Component.Payment.Feature](/api/account_sessions/object?api-version=2026-07-29.dahlia#account_session_object-components-payments-features), [AccountSession.Component.PaymentDetail.Feature](/api/account_sessions/object?api-version=2026-07-29.dahlia#account_session_object-components-payment_details-features), [AccountSession.Component.PaymentDispute.Feature](/api/account_sessions/object?api-version=2026-07-29.dahlia#account_session_object-components-payment_disputes-features), [AccountSessionCreateParamsComponentDisputesListFeature](/api/account_sessions/create?api-version=2026-07-29.dahlia#create_account_session-components-disputes_list-features), [AccountSessionCreateParamsComponentPaymentDetailFeature](/api/account_sessions/create?api-version=2026-07-29.dahlia#create_account_session-components-payment_details-features), [AccountSessionCreateParamsComponentPaymentDisputeFeature](/api/account_sessions/create?api-version=2026-07-29.dahlia#create_account_session-components-payment_disputes-features), [AccountSessionCreateParamsComponentPaymentFeature](/api/account_sessions/create?api-version=2026-07-29.dahlia#create_account_session-components-payments-features) |

#### PHP

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `smart_disputes_management` | Added | [AccountSession.components.disputes_list.features](/api/account_sessions/object?api-version=2026-07-29.dahlia#account_session_object-components-disputes_list-features), [AccountSession.components.payment_details.features](/api/account_sessions/object?api-version=2026-07-29.dahlia#account_session_object-components-payment_details-features), [AccountSession.components.payment_disputes.features](/api/account_sessions/object?api-version=2026-07-29.dahlia#account_session_object-components-payment_disputes-features), [AccountSession.components.payments.features](/api/account_sessions/object?api-version=2026-07-29.dahlia#account_session_object-components-payments-features), [AccountSession.create().$params.component.disputes_list.feature](/api/account_sessions/create?api-version=2026-07-29.dahlia#create_account_session-components-disputes_list-features), [AccountSession.create().$params.component.payment.feature](/api/account_sessions/create?api-version=2026-07-29.dahlia#create_account_session-components-payments-features), [AccountSession.create().$params.component.payment_detail.feature](/api/account_sessions/create?api-version=2026-07-29.dahlia#create_account_session-components-payment_details-features), [AccountSession.create().$params.component.payment_dispute.feature](/api/account_sessions/create?api-version=2026-07-29.dahlia#create_account_session-components-payment_disputes-features) |

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `smartDisputesManagement` | Added | [AccountSession.components.disputes_list.features](/api/account_sessions/object?api-version=2026-07-29.dahlia#account_session_object-components-disputes_list-features), [AccountSession.components.payment_details.features](/api/account_sessions/object?api-version=2026-07-29.dahlia#account_session_object-components-payment_details-features), [AccountSession.components.payment_disputes.features](/api/account_sessions/object?api-version=2026-07-29.dahlia#account_session_object-components-payment_disputes-features), [AccountSession.components.payments.features](/api/account_sessions/object?api-version=2026-07-29.dahlia#account_session_object-components-payments-features), [AccountSessionCreateParams.components.disputes_list.features](/api/account_sessions/create?api-version=2026-07-29.dahlia#create_account_session-components-disputes_list-features), [AccountSessionCreateParams.components.payment_details.features](/api/account_sessions/create?api-version=2026-07-29.dahlia#create_account_session-components-payment_details-features), [AccountSessionCreateParams.components.payment_disputes.features](/api/account_sessions/create?api-version=2026-07-29.dahlia#create_account_session-components-payment_disputes-features), [AccountSessionCreateParams.components.payments.features](/api/account_sessions/create?api-version=2026-07-29.dahlia#create_account_session-components-payments-features) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `smart_disputes_management` | Added | [AccountSession.components.disputes_list.features](/api/account_sessions/object?api-version=2026-07-29.dahlia#account_session_object-components-disputes_list-features), [AccountSession.components.payment_details.features](/api/account_sessions/object?api-version=2026-07-29.dahlia#account_session_object-components-payment_details-features), [AccountSession.components.payment_disputes.features](/api/account_sessions/object?api-version=2026-07-29.dahlia#account_session_object-components-payment_disputes-features), [AccountSession.components.payments.features](/api/account_sessions/object?api-version=2026-07-29.dahlia#account_session_object-components-payments-features), [AccountSessionCreateParams.components.disputes_list.features](/api/account_sessions/create?api-version=2026-07-29.dahlia#create_account_session-components-disputes_list-features), [AccountSessionCreateParams.components.payment_details.features](/api/account_sessions/create?api-version=2026-07-29.dahlia#create_account_session-components-payment_details-features), [AccountSessionCreateParams.components.payment_disputes.features](/api/account_sessions/create?api-version=2026-07-29.dahlia#create_account_session-components-payment_disputes-features), [AccountSessionCreateParams.components.payments.features](/api/account_sessions/create?api-version=2026-07-29.dahlia#create_account_session-components-payments-features) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `SmartDisputesManagement` | Added | [AccountSessionComponentsDisputesListFeatures](/api/account_sessions/object?api-version=2026-07-29.dahlia#account_session_object-components-disputes_list-features), [AccountSessionComponentsDisputesListFeaturesParams](/api/account_sessions/create?api-version=2026-07-29.dahlia#create_account_session-components-disputes_list-features), [AccountSessionComponentsPaymentDetailsFeatures](/api/account_sessions/object?api-version=2026-07-29.dahlia#account_session_object-components-payment_details-features), [AccountSessionComponentsPaymentDetailsFeaturesParams](/api/account_sessions/create?api-version=2026-07-29.dahlia#create_account_session-components-payment_details-features), [AccountSessionComponentsPaymentDisputesFeatures](/api/account_sessions/object?api-version=2026-07-29.dahlia#account_session_object-components-payment_disputes-features), [AccountSessionComponentsPaymentDisputesFeaturesParams](/api/account_sessions/create?api-version=2026-07-29.dahlia#create_account_session-components-payment_disputes-features), [AccountSessionComponentsPaymentsFeatures](/api/account_sessions/object?api-version=2026-07-29.dahlia#account_session_object-components-payments-features), [AccountSessionComponentsPaymentsFeaturesParams](/api/account_sessions/create?api-version=2026-07-29.dahlia#create_account_session-components-payments-features) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `SmartDisputesManagement` | Added | [AccountSession.Components.DisputesList.Features](/api/account_sessions/object?api-version=2026-07-29.dahlia#account_session_object-components-disputes_list-features), [AccountSession.Components.PaymentDetails.Features](/api/account_sessions/object?api-version=2026-07-29.dahlia#account_session_object-components-payment_details-features), [AccountSession.Components.PaymentDisputes.Features](/api/account_sessions/object?api-version=2026-07-29.dahlia#account_session_object-components-payment_disputes-features), [AccountSession.Components.Payments.Features](/api/account_sessions/object?api-version=2026-07-29.dahlia#account_session_object-components-payments-features), [AccountSessionComponentsDisputesListFeaturesOptions](/api/account_sessions/create?api-version=2026-07-29.dahlia#create_account_session-components-disputes_list-features), [AccountSessionComponentsPaymentDetailsFeaturesOptions](/api/account_sessions/create?api-version=2026-07-29.dahlia#create_account_session-components-payment_details-features), [AccountSessionComponentsPaymentDisputesFeaturesOptions](/api/account_sessions/create?api-version=2026-07-29.dahlia#create_account_session-components-payment_disputes-features), [AccountSessionComponentsPaymentsFeaturesOptions](/api/account_sessions/create?api-version=2026-07-29.dahlia#create_account_session-components-payments-features) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2026-07-29.dahlia`
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

- [Adds the ability to show who initiated a top-up](https://docs.stripe.com/changelog/dahlia/2026-07-29/top-up-initiated-by-property.md)
- [Adds Payment Method support to Top-ups](https://docs.stripe.com/changelog/dahlia/2026-07-29/adds-payment-method-support-to-top-ups.md)
- [Adds new address fields to Accounts v1 for Singapore compliance](https://docs.stripe.com/changelog/dahlia/2026-07-29/accounts-v1-address-fields.md)
- [Adds new address fields to Accounts v2 for Singapore compliance](https://docs.stripe.com/changelog/dahlia/2026-07-29/accounts-v2-address-fields.md)
- [Enables rejecting connected accounts with non-zero balances and controlling whether to pause payouts](https://docs.stripe.com/changelog/dahlia/2026-07-29/reject-connected-accounts-with-non-zero-balances.md)
- [Adds the ability to reverse platform rejections on connected accounts](https://docs.stripe.com/changelog/dahlia/2026-07-29/unreject-connected-account-endpoint.md)
