# Displays Amazon Pay dispute type on Disputes

## What’s new

Adds the Amazon Pay `dispute_type` to the `Dispute.payment_method_details` field.

## Impact

This change helps you understand the details of Amazon Pay disputes directly from [Disputes](https://docs.stripe.com/api/disputes.md?api-version=2024-09-30.acacia).

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `amazon_pay` | Added | [Dispute.payment_method_details](/api/disputes/object?api-version=2024-09-30.acacia#dispute_object-payment_method_details) |

| Value | Change | Enum |
| --- | --- | --- |
| `amazon_pay` | Added | [Dispute.payment_method_details.type](/api/disputes/object?api-version=2024-09-30.acacia#dispute_object-payment_method_details-type) |

#### Ruby

This change doesn’t affect the Ruby SDK.

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `amazon_pay` | Added | [stripe.Dispute.PaymentMethodDetails](/api/disputes/object?api-version=2024-09-30.acacia#dispute_object-payment_method_details) |

| Value | Change | Enum |
| --- | --- | --- |
| `amazon_pay` | Added | [stripe.Dispute.PaymentMethodDetails.type](/api/disputes/object?api-version=2024-09-30.acacia#dispute_object-payment_method_details-type) |

#### PHP

This change doesn’t affect the PHP SDK.

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `amazon_pay` | Added | [Dispute.payment_method_details](/api/disputes/object?api-version=2024-09-30.acacia#dispute_object-payment_method_details) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `amazon_pay` | Added | [Dispute.payment_method_details](/api/disputes/object?api-version=2024-09-30.acacia#dispute_object-payment_method_details) |

| Value | Change | Enum |
| --- | --- | --- |
| `amazon_pay` | Added | [Dispute.payment_method_details.type](/api/disputes/object?api-version=2024-09-30.acacia#dispute_object-payment_method_details-type) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `AmazonPay` | Added | [DisputePaymentMethodDetails](/api/disputes/object?api-version=2024-09-30.acacia#dispute_object-payment_method_details) |

| Value | Change | Enum |
| --- | --- | --- |
| `amazon_pay` | Added | [DisputePaymentMethodDetailsType](/api/disputes/object?api-version=2024-09-30.acacia#dispute_object-payment_method_details-type) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `AmazonPay` | Added | [DisputePaymentMethodDetails](/api/disputes/object?api-version=2024-09-30.acacia#dispute_object-payment_method_details) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2024-09-30.acacia`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to [v13.0.0](https://github.com/stripe/stripe-ruby/releases/tag/v13.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to [v11.0.0](https://github.com/stripe/stripe-python/releases/tag/v11.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to [v16.0.0](https://github.com/stripe/stripe-php/releases/tag/v16.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to [v27.0.0](https://github.com/stripe/stripe-java/releases/tag/v27.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to [v17.0.0](https://github.com/stripe/stripe-node/releases/tag/v17.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to [v80.0.0](https://github.com/stripe/stripe-go/releases/tag/v80.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to [v46.0.0](https://github.com/stripe/stripe-dotnet/releases/tag/v46.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

## Related changes

- [Adds option to retrieve CVC tokens on Confirmation Tokens](https://docs.stripe.com/changelog/acacia/2024-09-30/support-payment-method-options-confirmation.md)
- [Adds customer ID to payment method preview on a confirmation token](https://docs.stripe.com/changelog/acacia/2024-09-30/support-customer-payment-method-preview.md)
- [Adds support for identifying the unique payer for the BLIK payment method](https://docs.stripe.com/changelog/acacia/2024-09-30/buyer-id-blik.md)
- [Adds support for Affirm transaction IDs](https://docs.stripe.com/changelog/acacia/2024-09-30/affirm-transaction-id-dashboard.md)
- [Adds support for in-person payment methods, including Interac cards](https://docs.stripe.com/changelog/acacia/2024-09-30/card-interac-present-support.md)
- [Displays `authorization_code` for Charges](https://docs.stripe.com/changelog/acacia/2024-09-30/displays-authorization-code-for-charges.md)
- [Adds wallet details for `card_present` Charges and Payment Methods](https://docs.stripe.com/changelog/acacia/2024-09-30/adds-offline-details-card-present-paymentmethods.md)
- [Adds country field for Charges that use Klarna](https://docs.stripe.com/changelog/acacia/2024-09-30/charges-klarna-payer-details-country.md)
