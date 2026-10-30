# Updates card property requirements and adds 3D Secure authentication properties to Payment Records

## What’s new

Updates the [Payment Record](https://docs.stripe.com/api/payment-record/object.md?api-version=2026-03-25.dahlia) object to provide more payments orchestration flexibility by making several card properties optional and adding 3D Secure authentication properties to capture enhanced transaction security data.

Makes the following properties of the [payment_method_details.card](https://docs.stripe.com/api/payment-record/object.md?api-version=2026-03-25.dahlia#payment_record_object-payment_method_details-card) hash optional instead of required:

- [last4](https://docs.stripe.com/api/payment-record/object.md?api-version=2026-03-25.dahlia#payment_record_object-payment_method_details-card-last4): The last 4 digits of the card number
- [brand](https://docs.stripe.com/api/payment-record/object.md?api-version=2026-03-25.dahlia#payment_record_object-payment_method_details-card-brand): The card brand (Visa, Mastercard and so on)
- [exp_month](https://docs.stripe.com/api/payment-record/object.md?api-version=2026-03-25.dahlia#payment_record_object-payment_method_details-card-exp_month): The card’s expiry month
- [exp_year](https://docs.stripe.com/api/payment-record/object.md?api-version=2026-03-25.dahlia#payment_record_object-payment_method_details-card-exp_year): The card’s expiry year
- [moto](https://docs.stripe.com/api/payment-record/object.md?api-version=2026-03-25.dahlia#payment_record_object-payment_method_details-card-moto): Indicates a MOTO (mail order or telephone order) payment
- [funding](https://docs.stripe.com/api/payment-record/object.md?api-version=2026-03-25.dahlia#payment_record_object-payment_method_details-card-funding): The card funding type (such as credit or debit)

Adds the following optional properties to the [payment_method_details.card.three_d_secure](https://docs.stripe.com/api/payment-record/object.md?api-version=2026-03-25.dahlia#payment_record_object-payment_method_details-card-three_d_secure) hash:

- [electronic_commerce_indicator](https://docs.stripe.com/api/payment-record/object.md?api-version=2026-03-25.dahlia#payment_record_object-payment_method_details-card-three_d_secure-electronic_commerce_indicator): The Electronic Commerce Indicator (ECI), a protocol-level field indicating what degree of authentication was performed
- [exemption_indicator](https://docs.stripe.com/api/payment-record/object.md?api-version=2026-03-25.dahlia#payment_record_object-payment_method_details-card-three_d_secure-exemption_indicator): The exemption requested via 3DS and accepted by the issuer at authentication time
- [exemption_indicator_applied](https://docs.stripe.com/api/payment-record/object.md?api-version=2026-03-25.dahlia#payment_record_object-payment_method_details-card-three_d_secure-exemption_indicator_applied): Whether Stripe requested the value of `exemption_indicator` in the transaction

## Impact

Several card properties on the Payment Record object are now optional instead of required. Because these objects can be rendered at various points in the payment lifecycle, not all card fields are guaranteed to be available. This change makes the API more flexible for payments orchestration scenarios, particularly when working with external processors or recording payment attempts without complete card data.

The new `three_d_secure` properties provide useful 3D Secure authentication information that was previously unavailable on the Payment Record. This brings the Payment Record closer to parity with the [Charge](https://docs.stripe.com/api/charges.md?api-version=2026-03-25.dahlia) resource.

## Changes

#### REST API

| Parameters | Change | Resources or endpoints |
| --- | --- | --- |
| `electronic_commerce_indicator`, `exemption_indicator`, `exemption_indicator_applied` | Added | [PaymentAttemptRecord.payment_method_details.card.three_d_secure](/api/payment-attempt-record/object?api-version=2026-03-25.dahlia#payment_attempt_record_object-payment_method_details-card-three_d_secure), [PaymentRecord.payment_method_details.card.three_d_secure](/api/payment-record/object?api-version=2026-03-25.dahlia#payment_record_object-payment_method_details-card-three_d_secure) |

| Fields | Change | From → to |
| --- | --- | --- |
| `PaymentAttemptRecord.payment_method_details.card.brand`, `PaymentRecord.payment_method_details.card.brand` | Changed | `enum → nullable(enum)` |
| `PaymentAttemptRecord.payment_method_details.card.exp_month`, `PaymentRecord.payment_method_details.card.exp_month` | Changed | `longInteger → nullable(longInteger)` |
| `PaymentAttemptRecord.payment_method_details.card.exp_year`, `PaymentRecord.payment_method_details.card.exp_year` | Changed | `longInteger → nullable(longInteger)` |
| `PaymentAttemptRecord.payment_method_details.card.funding`, `PaymentRecord.payment_method_details.card.funding` | Changed | `enum('credit'|'debit'|'prepaid'|'unknown') → nullable(enum('credit'|'debit'|'prepaid'|'unknown'))` |
| `PaymentAttemptRecord.payment_method_details.card.last4`, `PaymentRecord.payment_method_details.card.last4` | Changed | `string → nullable(string)` |
| `PaymentAttemptRecord.payment_method_details.card.moto`, `PaymentRecord.payment_method_details.card.moto` | Changed | `boolean → nullable(boolean)` |

#### Ruby

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `electronic_commerce_indicator`, `exemption_indicator`, `exemption_indicator_applied` | Added | [PaymentAttemptRecord::PaymentMethodDetail::Card::ThreeDSecure](/api/payment-attempt-record/object?api-version=2026-03-25.dahlia#payment_attempt_record_object-payment_method_details-card-three_d_secure), [PaymentRecord::PaymentMethodDetail::Card::ThreeDSecure](/api/payment-record/object?api-version=2026-03-25.dahlia#payment_record_object-payment_method_details-card-three_d_secure) |

| Fields | Change | From → to |
| --- | --- | --- |
| `PaymentAttemptRecord::PaymentMethodDetail::Card.brand`, `PaymentRecord::PaymentMethodDetail::Card.brand` | Changed | `enum → nullable(enum)` |
| `PaymentAttemptRecord::PaymentMethodDetail::Card.exp_month`, `PaymentRecord::PaymentMethodDetail::Card.exp_month` | Changed | `longInteger → nullable(longInteger)` |
| `PaymentAttemptRecord::PaymentMethodDetail::Card.exp_year`, `PaymentRecord::PaymentMethodDetail::Card.exp_year` | Changed | `longInteger → nullable(longInteger)` |
| `PaymentAttemptRecord::PaymentMethodDetail::Card.funding`, `PaymentRecord::PaymentMethodDetail::Card.funding` | Changed | `enum('credit'|'debit'|'prepaid'|'unknown') → nullable(enum('credit'|'debit'|'prepaid'|'unknown'))` |
| `PaymentAttemptRecord::PaymentMethodDetail::Card.last4`, `PaymentRecord::PaymentMethodDetail::Card.last4` | Changed | `string → nullable(string)` |
| `PaymentAttemptRecord::PaymentMethodDetail::Card.moto`, `PaymentRecord::PaymentMethodDetail::Card.moto` | Changed | `boolean → nullable(boolean)` |

#### Python

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `electronic_commerce_indicator`, `exemption_indicator`, `exemption_indicator_applied` | Added | [PaymentAttemptRecord.PaymentMethodDetail.Card.ThreeDSecure](/api/payment-attempt-record/object?api-version=2026-03-25.dahlia#payment_attempt_record_object-payment_method_details-card-three_d_secure), [PaymentRecord.PaymentMethodDetail.Card.ThreeDSecure](/api/payment-record/object?api-version=2026-03-25.dahlia#payment_record_object-payment_method_details-card-three_d_secure) |

| Fields | Change | From → to |
| --- | --- | --- |
| `PaymentAttemptRecord.PaymentMethodDetail.Card.brand`, `PaymentRecord.PaymentMethodDetail.Card.brand` | Changed | `enum → nullable(enum)` |
| `PaymentAttemptRecord.PaymentMethodDetail.Card.exp_month`, `PaymentRecord.PaymentMethodDetail.Card.exp_month` | Changed | `longInteger → nullable(longInteger)` |
| `PaymentAttemptRecord.PaymentMethodDetail.Card.exp_year`, `PaymentRecord.PaymentMethodDetail.Card.exp_year` | Changed | `longInteger → nullable(longInteger)` |
| `PaymentAttemptRecord.PaymentMethodDetail.Card.funding`, `PaymentRecord.PaymentMethodDetail.Card.funding` | Changed | `enum('credit'|'debit'|'prepaid'|'unknown') → nullable(enum('credit'|'debit'|'prepaid'|'unknown'))` |
| `PaymentAttemptRecord.PaymentMethodDetail.Card.last4`, `PaymentRecord.PaymentMethodDetail.Card.last4` | Changed | `string → nullable(string)` |
| `PaymentAttemptRecord.PaymentMethodDetail.Card.moto`, `PaymentRecord.PaymentMethodDetail.Card.moto` | Changed | `boolean → nullable(boolean)` |

#### PHP

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `electronic_commerce_indicator`, `exemption_indicator`, `exemption_indicator_applied` | Added | [PaymentAttemptRecord.payment_method_details.card.three_d_secure](/api/payment-attempt-record/object?api-version=2026-03-25.dahlia#payment_attempt_record_object-payment_method_details-card-three_d_secure), [PaymentRecord.payment_method_details.card.three_d_secure](/api/payment-record/object?api-version=2026-03-25.dahlia#payment_record_object-payment_method_details-card-three_d_secure) |

| Fields | Change | From → to |
| --- | --- | --- |
| `PaymentAttemptRecord.payment_method_details.card.brand`, `PaymentRecord.payment_method_details.card.brand` | Changed | `enum → nullable(enum)` |
| `PaymentAttemptRecord.payment_method_details.card.exp_month`, `PaymentRecord.payment_method_details.card.exp_month` | Changed | `longInteger → nullable(longInteger)` |
| `PaymentAttemptRecord.payment_method_details.card.exp_year`, `PaymentRecord.payment_method_details.card.exp_year` | Changed | `longInteger → nullable(longInteger)` |
| `PaymentAttemptRecord.payment_method_details.card.funding`, `PaymentRecord.payment_method_details.card.funding` | Changed | `enum('credit'|'debit'|'prepaid'|'unknown') → nullable(enum('credit'|'debit'|'prepaid'|'unknown'))` |
| `PaymentAttemptRecord.payment_method_details.card.last4`, `PaymentRecord.payment_method_details.card.last4` | Changed | `string → nullable(string)` |
| `PaymentAttemptRecord.payment_method_details.card.moto`, `PaymentRecord.payment_method_details.card.moto` | Changed | `boolean → nullable(boolean)` |

#### Java

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `electronicCommerceIndicator`, `exemptionIndicator`, `exemptionIndicatorApplied` | Added | [PaymentAttemptRecord.payment_method_details.card.three_d_secure](/api/payment-attempt-record/object?api-version=2026-03-25.dahlia#payment_attempt_record_object-payment_method_details-card-three_d_secure), [PaymentRecord.payment_method_details.card.three_d_secure](/api/payment-record/object?api-version=2026-03-25.dahlia#payment_record_object-payment_method_details-card-three_d_secure) |

#### Node.js

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `electronic_commerce_indicator`, `exemption_indicator`, `exemption_indicator_applied` | Added | [PaymentAttemptRecord.payment_method_details.card.three_d_secure](/api/payment-attempt-record/object?api-version=2026-03-25.dahlia#payment_attempt_record_object-payment_method_details-card-three_d_secure), [PaymentRecord.payment_method_details.card.three_d_secure](/api/payment-record/object?api-version=2026-03-25.dahlia#payment_record_object-payment_method_details-card-three_d_secure) |

| Fields | Change | From → to |
| --- | --- | --- |
| `PaymentAttemptRecord.payment_method_details.card.brand`, `PaymentRecord.payment_method_details.card.brand` | Changed | `enum → enum | null` |
| `PaymentAttemptRecord.payment_method_details.card.exp_month`, `PaymentRecord.payment_method_details.card.exp_month` | Changed | `longInteger → longInteger | null` |
| `PaymentAttemptRecord.payment_method_details.card.exp_year`, `PaymentRecord.payment_method_details.card.exp_year` | Changed | `longInteger → longInteger | null` |
| `PaymentAttemptRecord.payment_method_details.card.funding`, `PaymentRecord.payment_method_details.card.funding` | Changed | `enum('credit'|'debit'|'prepaid'|'unknown') → enum('credit'|'debit'|'prepaid'|'unknown') | null` |
| `PaymentAttemptRecord.payment_method_details.card.last4`, `PaymentRecord.payment_method_details.card.last4` | Changed | `string → string | null` |
| `PaymentAttemptRecord.payment_method_details.card.moto`, `PaymentRecord.payment_method_details.card.moto` | Changed | `boolean → boolean | null` |

#### Go

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `ElectronicCommerceIndicator`, `ExemptionIndicator`, `ExemptionIndicatorApplied` | Added | [PaymentAttemptRecordPaymentMethodDetailsCardThreeDSecure](/api/payment-attempt-record/object?api-version=2026-03-25.dahlia#payment_attempt_record_object-payment_method_details-card-three_d_secure), [PaymentRecordPaymentMethodDetailsCardThreeDSecure](/api/payment-record/object?api-version=2026-03-25.dahlia#payment_record_object-payment_method_details-card-three_d_secure) |

#### .NET

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `ElectronicCommerceIndicator`, `ExemptionIndicator`, `ExemptionIndicatorApplied` | Added | [PaymentAttemptRecord.PaymentMethodDetails.Card.ThreeDSecure](/api/payment-attempt-record/object?api-version=2026-03-25.dahlia#payment_attempt_record_object-payment_method_details-card-three_d_secure), [PaymentRecord.PaymentMethodDetails.Card.ThreeDSecure](/api/payment-record/object?api-version=2026-03-25.dahlia#payment_record_object-payment_method_details-card-three_d_secure) |

| Fields | Change | From → to |
| --- | --- | --- |
| `PaymentAttemptRecord.PaymentMethodDetails.Card.ExpMonth`, `PaymentRecord.PaymentMethodDetails.Card.ExpMonth` | Changed | `longInteger → nullable(longInteger)` |
| `PaymentAttemptRecord.PaymentMethodDetails.Card.ExpYear`, `PaymentRecord.PaymentMethodDetails.Card.ExpYear` | Changed | `longInteger → nullable(longInteger)` |
| `PaymentAttemptRecord.PaymentMethodDetails.Card.Moto`, `PaymentRecord.PaymentMethodDetails.Card.Moto` | Changed | `boolean → nullable(boolean)` |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2026-03-25.dahlia`
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

- [Adds support for the UPI payment method](https://docs.stripe.com/changelog/dahlia/2026-03-25/adds-support-for-the-upi-payment-method.md)
- [Adds payment method-level support for configuring future usage of crypto payment methods in Checkout Sessions](https://docs.stripe.com/changelog/dahlia/2026-03-25/expands-crypto-payment-method-options-for-checkout-sessions.md)
