# Adds a documented reason for Klarna chargeback losses to Disputes API

## What’s new

Adds the [chargeback_loss_reason_code](https://docs.stripe.com/api/disputes/object.md?api-version=2025-09-30.clover&rds=1&lang=curl#dispute_object-payment_method_details-klarna-chargeback_loss_reason_code) field, which provides a code describing the reason for lost chargeback disputes with Klarna.

## Impact

The `chargeback_loss_reason_code` is included after Klarna closes a dispute. When handling disputes, use this information to identify factors that contributed to a loss. Understanding these reasons allows you to implement targeted strategies to reduce future chargeback losses.

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `chargeback_loss_reason_code` | Added | [Dispute.payment_method_details.klarna](/api/disputes/object?api-version=2025-09-30.clover#dispute_object-payment_method_details-klarna) |

#### Ruby

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `chargeback_loss_reason_code` | Added | [Dispute::PaymentMethodDetail::Klarna](/api/disputes/object?api-version=2025-09-30.clover#dispute_object-payment_method_details-klarna) |

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `chargeback_loss_reason_code` | Added | [Dispute.PaymentMethodDetail.Klarna](/api/disputes/object?api-version=2025-09-30.clover#dispute_object-payment_method_details-klarna) |

#### PHP

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `chargeback_loss_reason_code` | Added | [Dispute.payment_method_details.klarna](/api/disputes/object?api-version=2025-09-30.clover#dispute_object-payment_method_details-klarna) |

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `chargebackLossReasonCode` | Added | [Dispute.payment_method_details.klarna](/api/disputes/object?api-version=2025-09-30.clover#dispute_object-payment_method_details-klarna) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `chargeback_loss_reason_code` | Added | [Dispute.payment_method_details.klarna](/api/disputes/object?api-version=2025-09-30.clover#dispute_object-payment_method_details-klarna) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `ChargebackLossReasonCode` | Added | [DisputePaymentMethodDetailsKlarna](/api/disputes/object?api-version=2025-09-30.clover#dispute_object-payment_method_details-klarna) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `ChargebackLossReasonCode` | Added | [Dispute.PaymentMethodDetails.Klarna](/api/disputes/object?api-version=2025-09-30.clover#dispute_object-payment_method_details-klarna) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2025-09-30.clover`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to [v16.0.0](https://github.com/stripe/stripe-ruby/releases/tag/v16.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to [v13.0.1](https://github.com/stripe/stripe-python/releases/tag/v13.0.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to [v18.0.0](https://github.com/stripe/stripe-php/releases/tag/v18.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to [v30.0.0](https://github.com/stripe/stripe-java/releases/tag/v30.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to [v19.1.0](https://github.com/stripe/stripe-node/releases/tag/v19.1.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to [v83.0.0](https://github.com/stripe/stripe-go/releases/tag/v83.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to [v49.0.0](https://github.com/stripe/stripe-dotnet/releases/tag/v49.0.0)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

## Related changes

- [Changes the set of decline codes used for Alma, Amazon Pay, Billie, Satispay and South Korean payment methods](https://docs.stripe.com/changelog/clover/2025-09-30/lpm-descriptive-decline-codes.md)
- [Adds a processing status to submitted stablecoin payments](https://docs.stripe.com/changelog/clover/2025-09-30/stablecoin-payments-processing-status.md)
- [Adds support for the MB WAY payment method](https://docs.stripe.com/changelog/clover/2025-09-30/mb-way-payments.md)
