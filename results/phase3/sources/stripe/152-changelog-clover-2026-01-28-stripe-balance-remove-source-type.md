# Removes the source type parameter when creating new Stripe balance payment methods

## What’s new

Removes the ability to specify the [source_type](https://docs.stripe.com/api/payment_methods/object.md?api-version=2025-12-15.preview#payment_method_object-stripe_balance-source_type) when creating [Stripe balance](https://docs.stripe.com/api/payment_methods/object.md?api-version=2026-01-28.preview#payment_method_object-stripe_balance) payment methods. `source_type` is now set to null for new Stripe balance payment methods.

## Impact

Previously, the `source_type` parameter was required when creating Stripe balance payment methods. You can no longer specify the `source_type` when creating Stripe balance payment methods—Stripe now returns an error if you include `source_type`.

If your integration creates Stripe balance payment methods, update your code to remove the `source_type` parameter during creation, as well as handle cases where this property is null.

Existing Stripe balance payment methods are not affected by this change.

## Changes

#### REST API

| Fields | Change | From → to |
| --- | --- | --- |
| `Charge.payment_method_details.stripe_balance.source_type`, `ConfirmationToken.payment_method_preview.stripe_balance.source_type`, `PaymentAttemptRecord.payment_method_details.stripe_balance.source_type`, `PaymentMethod.stripe_balance.source_type`, `PaymentRecord.payment_method_details.stripe_balance.source_type` | Changed | `enum('bank_account'|'card'|'fpx') → nullable(enum('bank_account'|'card'|'fpx'))` |

#### Ruby

| Fields | Change | From → to |
| --- | --- | --- |
| `Charge::PaymentMethodDetail::StripeBalance.source_type`, `ConfirmationToken::PaymentMethodPreview::StripeBalance.source_type`, `PaymentAttemptRecord::PaymentMethodDetail::StripeBalance.source_type`, `PaymentMethod::StripeBalance.source_type`, `PaymentRecord::PaymentMethodDetail::StripeBalance.source_type` | Changed | `enum('bank_account'|'card'|'fpx') → nullable(enum('bank_account'|'card'|'fpx'))` |

#### Python

| Fields | Change | From → to |
| --- | --- | --- |
| `Charge.PaymentMethodDetail.StripeBalance.source_type`, `ConfirmationToken.PaymentMethodPreview.StripeBalance.source_type`, `PaymentAttemptRecord.PaymentMethodDetail.StripeBalance.source_type`, `PaymentMethod.StripeBalance.source_type`, `PaymentRecord.PaymentMethodDetail.StripeBalance.source_type` | Changed | `enum('bank_account'|'card'|'fpx') → nullable(enum('bank_account'|'card'|'fpx'))` |

#### PHP

| Fields | Change | From → to |
| --- | --- | --- |
| `Charge.payment_method_details.stripe_balance.source_type`, `ConfirmationToken.payment_method_preview.stripe_balance.source_type`, `PaymentAttemptRecord.payment_method_details.stripe_balance.source_type`, `PaymentMethod.stripe_balance.source_type`, `PaymentRecord.payment_method_details.stripe_balance.source_type` | Changed | `enum('bank_account'|'card'|'fpx') → nullable(enum('bank_account'|'card'|'fpx'))` |

#### Java

This change doesn’t affect the Java SDK.

#### Node.js

| Fields | Change | From → to |
| --- | --- | --- |
| `Charge.payment_method_details.stripe_balance.source_type`, `ConfirmationToken.payment_method_preview.stripe_balance.source_type`, `PaymentAttemptRecord.payment_method_details.stripe_balance.source_type`, `PaymentMethod.stripe_balance.source_type`, `PaymentRecord.payment_method_details.stripe_balance.source_type` | Changed | `enum('bank_account'|'card'|'fpx') → enum('bank_account'|'card'|'fpx') | null` |

#### Go

This change doesn’t affect the Go SDK.

#### .NET

This change doesn’t affect the .NET SDK.

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2026-01-28.preview`
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
