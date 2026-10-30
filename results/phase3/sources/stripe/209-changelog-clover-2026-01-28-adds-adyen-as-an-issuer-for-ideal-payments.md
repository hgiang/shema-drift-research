# Adds Adyen as an issuer for iDEAL payments

## What’s new

Adds [Adyen](https://www.adyen.com/) to the list of supported issuers for [iDEAL payments](https://docs.stripe.com/payments/ideal.md). Your customers can now select Adyen from the list of available banks when making iDEAL payments through your integration.

## Impact

If you accept iDEAL payments, customers who bank with Adyen can now use their Adyen account to complete payments. No changes are required to your existing iDEAL integration. Adyen automatically appears as an available option in the bank selection interface for customers in the Netherlands.

## Changes

#### REST API

| Values | Change | Enums |
| --- | --- | --- |
| `adyen` | Added | [Charge.payment_method_details.ideal](/api/charges/object?api-version=2026-01-28.clover#charge_object-payment_method_details-ideal-bank), [ConfirmationToken.testHelpers#create.payment_method_data.ideal](/api/charges/object?api-version=2026-01-28.clover#charge_object-payment_method_data-ideal-bank), [ConfirmationToken.payment_method_preview.ideal](/api/charges/object?api-version=2026-01-28.clover#charge_object-payment_method_preview-ideal-bank), [PaymentAttemptRecord.payment_method_details.ideal](/api/charges/object?api-version=2026-01-28.clover#charge_object-payment_method_details-ideal-bank), [PaymentIntent#create.payment_method_data.ideal](/api/charges/object?api-version=2026-01-28.clover#charge_object-payment_method_data-ideal-bank), [PaymentIntent#update.payment_method_data.ideal](/api/charges/object?api-version=2026-01-28.clover#charge_object-payment_method_data-ideal-bank), [PaymentIntent#confirm.payment_method_data.ideal](/api/charges/object?api-version=2026-01-28.clover#charge_object-payment_method_data-ideal-bank), [PaymentMethod#create.ideal](/api/charges/object?api-version=2026-01-28.clover#charge_object-ideal-bank), [PaymentMethod.ideal](/api/charges/object?api-version=2026-01-28.clover#charge_object-ideal-bank), [PaymentRecord.payment_method_details.ideal](/api/charges/object?api-version=2026-01-28.clover#charge_object-payment_method_details-ideal-bank), [SetupAttempt.payment_method_details.ideal](/api/charges/object?api-version=2026-01-28.clover#charge_object-payment_method_details-ideal-bank), [SetupIntent#create.payment_method_data.ideal](/api/charges/object?api-version=2026-01-28.clover#charge_object-payment_method_data-ideal-bank), [SetupIntent#update.payment_method_data.ideal](/api/charges/object?api-version=2026-01-28.clover#charge_object-payment_method_data-ideal-bank), [SetupIntent#confirm.payment_method_data.ideal](/api/charges/object?api-version=2026-01-28.clover#charge_object-payment_method_data-ideal-bank) |
| `ADYBNL2A` | Added | [Charge.payment_method_details.ideal](/api/charges/object?api-version=2026-01-28.clover#charge_object-payment_method_details-ideal-bic), [ConfirmationToken.payment_method_preview.ideal](/api/charges/object?api-version=2026-01-28.clover#charge_object-payment_method_preview-ideal-bic), [PaymentAttemptRecord.payment_method_details.ideal](/api/charges/object?api-version=2026-01-28.clover#charge_object-payment_method_details-ideal-bic), [PaymentMethod.ideal](/api/charges/object?api-version=2026-01-28.clover#charge_object-ideal-bic), [PaymentRecord.payment_method_details.ideal](/api/charges/object?api-version=2026-01-28.clover#charge_object-payment_method_details-ideal-bic), [SetupAttempt.payment_method_details.ideal](/api/charges/object?api-version=2026-01-28.clover#charge_object-payment_method_details-ideal-bic) |

#### Ruby

This change doesn’t affect the Ruby SDK.

#### Python

| Values | Change | Enums |
| --- | --- | --- |
| `adyen` | Added | [Charge.PaymentMethodDetail.Ideal](/api/charges/object?api-version=2026-01-28.clover#charge_object-payment_method_details-ideal-bank), [ConfirmationTokenCreateParamsPaymentMethodDatumIdeal](/api/charges/object?api-version=2026-01-28.clover#charge_object-payment_method_data-ideal-bank), [ConfirmationToken.PaymentMethodPreview.Ideal](/api/charges/object?api-version=2026-01-28.clover#charge_object-payment_method_preview-ideal-bank), [PaymentAttemptRecord.PaymentMethodDetail.Ideal](/api/charges/object?api-version=2026-01-28.clover#charge_object-payment_method_details-ideal-bank), [PaymentIntentCreateParamsPaymentMethodDatumIdeal](/api/charges/object?api-version=2026-01-28.clover#charge_object-payment_method_data-ideal-bank), [PaymentIntentModifyParamsPaymentMethodDatumIdeal](/api/charges/object?api-version=2026-01-28.clover#charge_object-payment_method_data-ideal-bank), [PaymentIntentConfirmParamsPaymentMethodDatumIdeal](/api/charges/object?api-version=2026-01-28.clover#charge_object-payment_method_data-ideal-bank), [PaymentMethodCreateParamsIdeal](/api/charges/object?api-version=2026-01-28.clover#charge_object-ideal-bank), [PaymentMethod.Ideal](/api/charges/object?api-version=2026-01-28.clover#charge_object-ideal-bank), [PaymentRecord.PaymentMethodDetail.Ideal](/api/charges/object?api-version=2026-01-28.clover#charge_object-payment_method_details-ideal-bank), [SetupAttempt.PaymentMethodDetail.Ideal](/api/charges/object?api-version=2026-01-28.clover#charge_object-payment_method_details-ideal-bank), [SetupIntentCreateParamsPaymentMethodDatumIdeal](/api/charges/object?api-version=2026-01-28.clover#charge_object-payment_method_data-ideal-bank), [SetupIntentModifyParamsPaymentMethodDatumIdeal](/api/charges/object?api-version=2026-01-28.clover#charge_object-payment_method_data-ideal-bank), [SetupIntentConfirmParamsPaymentMethodDatumIdeal](/api/charges/object?api-version=2026-01-28.clover#charge_object-payment_method_data-ideal-bank) |
| `ADYBNL2A` | Added | [Charge.PaymentMethodDetail.Ideal](/api/charges/object?api-version=2026-01-28.clover#charge_object-payment_method_details-ideal-bic), [ConfirmationToken.PaymentMethodPreview.Ideal](/api/charges/object?api-version=2026-01-28.clover#charge_object-payment_method_preview-ideal-bic), [PaymentAttemptRecord.PaymentMethodDetail.Ideal](/api/charges/object?api-version=2026-01-28.clover#charge_object-payment_method_details-ideal-bic), [PaymentMethod.Ideal](/api/charges/object?api-version=2026-01-28.clover#charge_object-ideal-bic), [PaymentRecord.PaymentMethodDetail.Ideal](/api/charges/object?api-version=2026-01-28.clover#charge_object-payment_method_details-ideal-bic), [SetupAttempt.PaymentMethodDetail.Ideal](/api/charges/object?api-version=2026-01-28.clover#charge_object-payment_method_details-ideal-bic) |

#### PHP

| Values | Change | Enums |
| --- | --- | --- |
| `adyen` | Added | [Charge.payment_method_details.ideal](/api/charges/object?api-version=2026-01-28.clover#charge_object-payment_method_details-ideal-bank), [ConfirmationToken.payment_method_preview.ideal](/api/charges/object?api-version=2026-01-28.clover#charge_object-payment_method_preview-ideal-bank), [PaymentAttemptRecord.payment_method_details.ideal](/api/charges/object?api-version=2026-01-28.clover#charge_object-payment_method_details-ideal-bank), [PaymentMethod.ideal](/api/charges/object?api-version=2026-01-28.clover#charge_object-ideal-bank), [PaymentRecord.payment_method_details.ideal](/api/charges/object?api-version=2026-01-28.clover#charge_object-payment_method_details-ideal-bank), [SetupAttempt.payment_method_details.ideal](/api/charges/object?api-version=2026-01-28.clover#charge_object-payment_method_details-ideal-bank) |
| `ADYBNL2A` | Added | [Charge.payment_method_details.ideal](/api/charges/object?api-version=2026-01-28.clover#charge_object-payment_method_details-ideal-bic), [ConfirmationToken.payment_method_preview.ideal](/api/charges/object?api-version=2026-01-28.clover#charge_object-payment_method_preview-ideal-bic), [PaymentAttemptRecord.payment_method_details.ideal](/api/charges/object?api-version=2026-01-28.clover#charge_object-payment_method_details-ideal-bic), [PaymentMethod.ideal](/api/charges/object?api-version=2026-01-28.clover#charge_object-ideal-bic), [PaymentRecord.payment_method_details.ideal](/api/charges/object?api-version=2026-01-28.clover#charge_object-payment_method_details-ideal-bic), [SetupAttempt.payment_method_details.ideal](/api/charges/object?api-version=2026-01-28.clover#charge_object-payment_method_details-ideal-bic) |

#### Java

| Value | Change | Enums |
| --- | --- | --- |
| `adyen` | Added | [ConfirmationTokenCreateParams.payment_method_data.ideal](/api/confirmation_tokens/test_create?api-version=2026-01-28.clover#create_confirmation_token-payment_method_data-ideal-bank), [PaymentIntentCreateParams.payment_method_data.ideal](/api/confirmation_tokens/test_create?api-version=2026-01-28.clover#create_confirmation_token-payment_method_data-ideal-bank), [PaymentIntentUpdateParams.payment_method_data.ideal](/api/confirmation_tokens/test_create?api-version=2026-01-28.clover#create_confirmation_token-payment_method_data-ideal-bank), [PaymentIntentConfirmParams.payment_method_data.ideal](/api/confirmation_tokens/test_create?api-version=2026-01-28.clover#create_confirmation_token-payment_method_data-ideal-bank), [PaymentMethodCreateParams.ideal](/api/confirmation_tokens/test_create?api-version=2026-01-28.clover#create_confirmation_token-ideal-bank), [SetupIntentCreateParams.payment_method_data.ideal](/api/confirmation_tokens/test_create?api-version=2026-01-28.clover#create_confirmation_token-payment_method_data-ideal-bank), [SetupIntentUpdateParams.payment_method_data.ideal](/api/confirmation_tokens/test_create?api-version=2026-01-28.clover#create_confirmation_token-payment_method_data-ideal-bank), [SetupIntentConfirmParams.payment_method_data.ideal](/api/confirmation_tokens/test_create?api-version=2026-01-28.clover#create_confirmation_token-payment_method_data-ideal-bank) |

#### Node.js

| Values | Change | Enums |
| --- | --- | --- |
| `adyen` | Added | [Charge.payment_method_details.ideal](/api/charges/object?api-version=2026-01-28.clover#charge_object-payment_method_details-ideal-bank), [ConfirmationTokenCreateParams.testHelpers.payment_method_data.ideal](/api/charges/object?api-version=2026-01-28.clover#charge_object-payment_method_data-ideal-bank), [ConfirmationToken.payment_method_preview.ideal](/api/charges/object?api-version=2026-01-28.clover#charge_object-payment_method_preview-ideal-bank), [PaymentAttemptRecord.payment_method_details.ideal](/api/charges/object?api-version=2026-01-28.clover#charge_object-payment_method_details-ideal-bank), [PaymentIntentCreateParams.payment_method_data.ideal](/api/charges/object?api-version=2026-01-28.clover#charge_object-payment_method_data-ideal-bank), [PaymentIntentUpdateParams.payment_method_data.ideal](/api/charges/object?api-version=2026-01-28.clover#charge_object-payment_method_data-ideal-bank), [PaymentIntentConfirmParams.payment_method_data.ideal](/api/charges/object?api-version=2026-01-28.clover#charge_object-payment_method_data-ideal-bank), [PaymentMethodCreateParams.ideal](/api/charges/object?api-version=2026-01-28.clover#charge_object-ideal-bank), [PaymentMethod.ideal](/api/charges/object?api-version=2026-01-28.clover#charge_object-ideal-bank), [PaymentRecord.payment_method_details.ideal](/api/charges/object?api-version=2026-01-28.clover#charge_object-payment_method_details-ideal-bank), [SetupAttempt.payment_method_details.ideal](/api/charges/object?api-version=2026-01-28.clover#charge_object-payment_method_details-ideal-bank), [SetupIntentCreateParams.payment_method_data.ideal](/api/charges/object?api-version=2026-01-28.clover#charge_object-payment_method_data-ideal-bank), [SetupIntentUpdateParams.payment_method_data.ideal](/api/charges/object?api-version=2026-01-28.clover#charge_object-payment_method_data-ideal-bank), [SetupIntentConfirmParams.payment_method_data.ideal](/api/charges/object?api-version=2026-01-28.clover#charge_object-payment_method_data-ideal-bank) |
| `ADYBNL2A` | Added | [Charge.payment_method_details.ideal](/api/charges/object?api-version=2026-01-28.clover#charge_object-payment_method_details-ideal-bic), [ConfirmationToken.payment_method_preview.ideal](/api/charges/object?api-version=2026-01-28.clover#charge_object-payment_method_preview-ideal-bic), [PaymentAttemptRecord.payment_method_details.ideal](/api/charges/object?api-version=2026-01-28.clover#charge_object-payment_method_details-ideal-bic), [PaymentMethod.ideal](/api/charges/object?api-version=2026-01-28.clover#charge_object-ideal-bic), [PaymentRecord.payment_method_details.ideal](/api/charges/object?api-version=2026-01-28.clover#charge_object-payment_method_details-ideal-bic), [SetupAttempt.payment_method_details.ideal](/api/charges/object?api-version=2026-01-28.clover#charge_object-payment_method_details-ideal-bic) |

#### Go

| Values | Change | Enums |
| --- | --- | --- |
| `adyen` | Added | [ConfirmationTokenPaymentMethodPreviewIdeal](/api/confirmation_tokens/object?api-version=2026-01-28.clover#confirmation_token_object-payment_method_preview-ideal-Bank), [PaymentAttemptRecordPaymentMethodDetailsIdeal](/api/confirmation_tokens/object?api-version=2026-01-28.clover#confirmation_token_object-payment_method_details-ideal-Bank), [PaymentRecordPaymentMethodDetailsIdeal](/api/confirmation_tokens/object?api-version=2026-01-28.clover#confirmation_token_object-payment_method_details-ideal-Bank) |
| `ADYBNL2A` | Added | [ConfirmationTokenPaymentMethodPreviewIdeal](/api/confirmation_tokens/object?api-version=2026-01-28.clover#confirmation_token_object-payment_method_preview-ideal-BIC), [PaymentAttemptRecordPaymentMethodDetailsIdeal](/api/confirmation_tokens/object?api-version=2026-01-28.clover#confirmation_token_object-payment_method_details-ideal-BIC), [PaymentRecordPaymentMethodDetailsIdeal](/api/confirmation_tokens/object?api-version=2026-01-28.clover#confirmation_token_object-payment_method_details-ideal-BIC) |

#### .NET

This change doesn’t affect the .NET SDK.

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2026-01-28.clover`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to [v18.2.0](https://github.com/stripe/stripe-ruby/releases/tag/v18.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to [v14.2.0](https://github.com/stripe/stripe-python/releases/tag/v14.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to [v19.2.0](https://github.com/stripe/stripe-php/releases/tag/v19.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to [v31.2.0](https://github.com/stripe/stripe-java/releases/tag/v31.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to [v20.2.0](https://github.com/stripe/stripe-node/releases/tag/v20.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to [v84.2.0](https://github.com/stripe/stripe-go/releases/tag/v84.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to [v50.2.0](https://github.com/stripe/stripe-dotnet/releases/tag/v50.2.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

## Related changes

- [Adds support for 3D Secure versions 2.3.0 and 2.3.1](https://docs.stripe.com/changelog/clover/2026-01-28/3d-secure-version-support.md)
- [Adds the ability to monitor reserve activity on Balance Transactions and reconcile Risk Reserved balance changes](https://docs.stripe.com/changelog/clover/2026-01-28/monitor-reserve-activity-on-balance-transactions.md)
- [Adds the ability to opt out of strict arithmetic validation for Payment Line Items](https://docs.stripe.com/changelog/clover/2026-01-28/loosen-arithmetic-validation-for-payment-line-items.md)
- [Adds adjustable quantity to the line items response](https://docs.stripe.com/changelog/clover/2026-01-28/line-items-adjustable-quantity.md)
