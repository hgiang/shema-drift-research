# Adds support for WeChat Pay and Affirm on Terminal

## What’s new

Adds support for Terminal when using WeChat Pay and Affirm Charge by including additional fields on the `payment_method_details`. You can also specify a `return_url` for non-card payments in Terminal server-driven integrations.

## Impact

Lets you collect WeChat Pay and Affirm payments in-person on Terminal smart readers. Learn more about [additional payment methods](https://docs.stripe.com/terminal/payments/additional-payment-methods.md) on Terminal.

## Changes

#### REST API

| Parameters | Change | Resources or endpoints |
| --- | --- | --- |
| `location`, `reader` | Added | [Charge.payment_method_details.affirm](/api/charges/object?api-version=2025-05-28.preview#charge_object-payment_method_details-affirm), [Charge.payment_method_details.wechat_pay](/api/charges/object?api-version=2025-05-28.preview#charge_object-payment_method_details-wechat_pay), [PaymentAttemptRecord.payment_method_details.affirm](/api/payment-attempt-record/object?api-version=2025-05-28.preview#payment_attempt_record_object-payment_method_details-affirm), [PaymentAttemptRecord.payment_method_details.wechat_pay](/api/payment-attempt-record/object?api-version=2025-05-28.preview#payment_attempt_record_object-payment_method_details-wechat_pay), [PaymentRecord.payment_method_details.affirm](/api/payment-record/object?api-version=2025-05-28.preview#payment_record_object-payment_method_details-affirm), [PaymentRecord.payment_method_details.wechat_pay](/api/payment-record/object?api-version=2025-05-28.preview#payment_record_object-payment_method_details-wechat_pay) |
| `confirm_config` | Added | [Terminal.Reader#confirm_payment_intent](/api/terminal/readers/confirm_payment_intent?api-version=2025-05-28.preview), [Terminal.Reader.action.confirm_payment_intent](/api/terminal/readers/object?api-version=2025-05-28.preview#terminal_reader_object-action-confirm_payment_intent) |
| `return_url` | Added | [Terminal.Reader#process_payment_intent.process_config](/api/terminal/readers/process_payment_intent?api-version=2025-05-28.preview#process_payment_intent-process_config), [Terminal.Reader.action.process_payment_intent.process_config](/api/terminal/readers/object?api-version=2025-05-28.preview#terminal_reader_object-action-process_payment_intent-process_config) |

#### Ruby

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `location`, `reader` | Added | [Charge::PaymentMethodDetail::Affirm](/api/charges/object?api-version=2025-05-28.preview#charge_object-payment_method_details-affirm), [Charge::PaymentMethodDetail::WechatPay](/api/charges/object?api-version=2025-05-28.preview#charge_object-payment_method_details-wechat_pay), [PaymentAttemptRecord::PaymentMethodDetail::Affirm](/api/payment-attempt-record/object?api-version=2025-05-28.preview#payment_attempt_record_object-payment_method_details-affirm), [PaymentAttemptRecord::PaymentMethodDetail::WechatPay](/api/payment-attempt-record/object?api-version=2025-05-28.preview#payment_attempt_record_object-payment_method_details-wechat_pay), [PaymentRecord::PaymentMethodDetail::Affirm](/api/payment-record/object?api-version=2025-05-28.preview#payment_record_object-payment_method_details-affirm), [PaymentRecord::PaymentMethodDetail::WechatPay](/api/payment-record/object?api-version=2025-05-28.preview#payment_record_object-payment_method_details-wechat_pay) |
| `confirm_config` | Added | [Terminal::Reader::Action::ConfirmPaymentIntent](/api/terminal/readers/object?api-version=2025-05-28.preview#terminal_reader_object-action-confirm_payment_intent), [Terminal::Reader::ConfirmPaymentIntentParams](/api/terminal/readers/confirm_payment_intent?api-version=2025-05-28.preview) |
| `return_url` | Added | [Terminal::Reader::Action::ProcessPaymentIntent::ProcessConfig](/api/terminal/readers/object?api-version=2025-05-28.preview#terminal_reader_object-action-process_payment_intent-process_config), [Terminal::Reader::ProcessPaymentIntentParams::ProcessConfig](/api/terminal/readers/process_payment_intent?api-version=2025-05-28.preview#process_payment_intent-process_config) |

#### Python

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `location`, `reader` | Added | [Charge.PaymentMethodDetail.Affirm](/api/charges/object?api-version=2025-05-28.preview#charge_object-payment_method_details-affirm), [Charge.PaymentMethodDetail.WechatPay](/api/charges/object?api-version=2025-05-28.preview#charge_object-payment_method_details-wechat_pay), [PaymentAttemptRecord.PaymentMethodDetail.Affirm](/api/payment-attempt-record/object?api-version=2025-05-28.preview#payment_attempt_record_object-payment_method_details-affirm), [PaymentAttemptRecord.PaymentMethodDetail.WechatPay](/api/payment-attempt-record/object?api-version=2025-05-28.preview#payment_attempt_record_object-payment_method_details-wechat_pay), [PaymentRecord.PaymentMethodDetail.Affirm](/api/payment-record/object?api-version=2025-05-28.preview#payment_record_object-payment_method_details-affirm), [PaymentRecord.PaymentMethodDetail.WechatPay](/api/payment-record/object?api-version=2025-05-28.preview#payment_record_object-payment_method_details-wechat_pay) |
| `confirm_config` | Added | [Terminal.Reader.Action.ConfirmPaymentIntent](/api/terminal/readers/object?api-version=2025-05-28.preview#terminal_reader_object-action-confirm_payment_intent), [terminal.Reader.ConfirmPaymentIntentParams](/api/terminal/readers/confirm_payment_intent?api-version=2025-05-28.preview) |
| `return_url` | Added | [Terminal.Reader.Action.ProcessPaymentIntent.ProcessConfig](/api/terminal/readers/object?api-version=2025-05-28.preview#terminal_reader_object-action-process_payment_intent-process_config), [terminal.Reader.ProcessPaymentIntentParamsProcessConfig](/api/terminal/readers/process_payment_intent?api-version=2025-05-28.preview#process_payment_intent-process_config) |

#### PHP

This change doesn’t affect the PHP SDK.

#### Java

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `location`, `reader` | Added | [Charge.payment_method_details.affirm](/api/charges/object?api-version=2025-05-28.preview#charge_object-payment_method_details-affirm), [Charge.payment_method_details.wechat_pay](/api/charges/object?api-version=2025-05-28.preview#charge_object-payment_method_details-wechat_pay), [PaymentAttemptRecord.payment_method_details.affirm](/api/payment-attempt-record/object?api-version=2025-05-28.preview#payment_attempt_record_object-payment_method_details-affirm), [PaymentAttemptRecord.payment_method_details.wechat_pay](/api/payment-attempt-record/object?api-version=2025-05-28.preview#payment_attempt_record_object-payment_method_details-wechat_pay), [PaymentRecord.payment_method_details.affirm](/api/payment-record/object?api-version=2025-05-28.preview#payment_record_object-payment_method_details-affirm), [PaymentRecord.payment_method_details.wechat_pay](/api/payment-record/object?api-version=2025-05-28.preview#payment_record_object-payment_method_details-wechat_pay) |
| `confirmConfig` | Added | [terminal.Reader.action.confirm_payment_intent](/api/terminal/readers/object?api-version=2025-05-28.preview#terminal_reader_object-action-confirm_payment_intent), [terminal.ReaderConfirmPaymentIntentParams](/api/terminal/readers/confirm_payment_intent?api-version=2025-05-28.preview) |
| `returnUrl` | Added | [terminal.Reader.action.process_payment_intent.process_config](/api/terminal/readers/object?api-version=2025-05-28.preview#terminal_reader_object-action-process_payment_intent-process_config), [terminal.ReaderProcessPaymentIntentParams.process_config](/api/terminal/readers/process_payment_intent?api-version=2025-05-28.preview#process_payment_intent-process_config) |

#### Node.js

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `location`, `reader` | Added | [Charge.payment_method_details.affirm](/api/charges/object?api-version=2025-05-28.preview#charge_object-payment_method_details-affirm), [Charge.payment_method_details.wechat_pay](/api/charges/object?api-version=2025-05-28.preview#charge_object-payment_method_details-wechat_pay), [PaymentAttemptRecord.payment_method_details.affirm](/api/payment-attempt-record/object?api-version=2025-05-28.preview#payment_attempt_record_object-payment_method_details-affirm), [PaymentAttemptRecord.payment_method_details.wechat_pay](/api/payment-attempt-record/object?api-version=2025-05-28.preview#payment_attempt_record_object-payment_method_details-wechat_pay), [PaymentRecord.payment_method_details.affirm](/api/payment-record/object?api-version=2025-05-28.preview#payment_record_object-payment_method_details-affirm), [PaymentRecord.payment_method_details.wechat_pay](/api/payment-record/object?api-version=2025-05-28.preview#payment_record_object-payment_method_details-wechat_pay) |
| `confirm_config` | Added | [Terminal.Reader.action.confirm_payment_intent](/api/terminal/readers/object?api-version=2025-05-28.preview#terminal_reader_object-action-confirm_payment_intent), [Terminal.ReaderConfirmPaymentIntentParams](/api/terminal/readers/confirm_payment_intent?api-version=2025-05-28.preview) |
| `return_url` | Added | [Terminal.Reader.action.process_payment_intent.process_config](/api/terminal/readers/object?api-version=2025-05-28.preview#terminal_reader_object-action-process_payment_intent-process_config), [Terminal.ReaderProcessPaymentIntentParams.process_config](/api/terminal/readers/process_payment_intent?api-version=2025-05-28.preview#process_payment_intent-process_config) |

#### Go

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `Location`, `Reader` | Added | [ChargePaymentMethodDetailsAffirm](/api/charges/object?api-version=2025-05-28.preview#charge_object-payment_method_details-affirm), [ChargePaymentMethodDetailsWechatPay](/api/charges/object?api-version=2025-05-28.preview#charge_object-payment_method_details-wechat_pay), [PaymentAttemptRecordPaymentMethodDetailsAffirm](/api/payment-attempt-record/object?api-version=2025-05-28.preview#payment_attempt_record_object-payment_method_details-affirm), [PaymentAttemptRecordPaymentMethodDetailsWechatPay](/api/payment-attempt-record/object?api-version=2025-05-28.preview#payment_attempt_record_object-payment_method_details-wechat_pay), [PaymentRecordPaymentMethodDetailsAffirm](/api/payment-record/object?api-version=2025-05-28.preview#payment_record_object-payment_method_details-affirm), [PaymentRecordPaymentMethodDetailsWechatPay](/api/payment-record/object?api-version=2025-05-28.preview#payment_record_object-payment_method_details-wechat_pay) |
| `ConfirmConfig` | Added | [TerminalReaderActionConfirmPaymentIntent](/api/terminal/readers/object?api-version=2025-05-28.preview#terminal_reader_object-action-confirm_payment_intent), [TerminalReaderConfirmPaymentIntentParams](/api/terminal/readers/confirm_payment_intent?api-version=2025-05-28.preview) |
| `ReturnURL` | Added | [TerminalReaderActionProcessPaymentIntentProcessConfig](/api/terminal/readers/object?api-version=2025-05-28.preview#terminal_reader_object-action-process_payment_intent-process_config), [TerminalReaderProcessPaymentIntentProcessConfigParams](/api/terminal/readers/process_payment_intent?api-version=2025-05-28.preview#process_payment_intent-process_config) |

#### .NET

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `Location`, `Reader` | Added | [Charge.PaymentMethodDetails.Affirm](/api/charges/object?api-version=2025-05-28.preview#charge_object-payment_method_details-affirm), [Charge.PaymentMethodDetails.WechatPay](/api/charges/object?api-version=2025-05-28.preview#charge_object-payment_method_details-wechat_pay), [PaymentAttemptRecord.PaymentMethodDetails.Affirm](/api/payment-attempt-record/object?api-version=2025-05-28.preview#payment_attempt_record_object-payment_method_details-affirm), [PaymentAttemptRecord.PaymentMethodDetails.WechatPay](/api/payment-attempt-record/object?api-version=2025-05-28.preview#payment_attempt_record_object-payment_method_details-wechat_pay), [PaymentRecord.PaymentMethodDetails.Affirm](/api/payment-record/object?api-version=2025-05-28.preview#payment_record_object-payment_method_details-affirm), [PaymentRecord.PaymentMethodDetails.WechatPay](/api/payment-record/object?api-version=2025-05-28.preview#payment_record_object-payment_method_details-wechat_pay) |
| `ConfirmConfig` | Added | [Terminal.Reader.Action.ConfirmPaymentIntent](/api/terminal/readers/object?api-version=2025-05-28.preview#terminal_reader_object-action-confirm_payment_intent), [Terminal.ReaderConfirmPaymentIntentOptions](/api/terminal/readers/confirm_payment_intent?api-version=2025-05-28.preview) |
| `ReturnUrl` | Added | [Terminal.Reader.Action.ProcessPaymentIntent.ProcessConfig](/api/terminal/readers/object?api-version=2025-05-28.preview#terminal_reader_object-action-process_payment_intent-process_config), [TerminalReaderProcessConfigOptions](/api/terminal/readers/process_payment_intent?api-version=2025-05-28.preview#process_payment_intent-process_config) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2025-05-28.preview`
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Ruby

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Ruby SDK to [v15.3.0-beta.1](https://github.com/stripe/stripe-ruby/releases/tag/v15.3.0-beta.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Python

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Python SDK to [v12.3.0b1](https://github.com/stripe/stripe-python/releases/tag/v12.3.0b1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### PHP

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your PHP SDK to [v17.4.0-beta.2](https://github.com/stripe/stripe-php/releases/tag/v17.4.0-beta.2)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Java

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Java SDK to [v29.3.0-beta.1](https://github.com/stripe/stripe-java/releases/tag/v29.3.0-beta.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Node.js

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Node SDK to [v18.3.0-beta.1](https://github.com/stripe/stripe-node/releases/tag/v18.3.0-beta.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### Go

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your Go SDK to [v82.3.0-beta.1](https://github.com/stripe/stripe-go/releases/tag/v82.3.0-beta.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).

#### .NET

1. [View your current API version](https://docs.stripe.com/upgrades.md#view-your-api-version-and-the-latest-available-upgrade-in-workbench) in Workbench.
2. Upgrade your .NET SDK to [v48.3.0-beta.1](https://github.com/stripe/stripe-dotnet/releases/tag/v48.3.0-beta.1)
3. Upgrade the API version used for [webhook endpoints](https://docs.stripe.com/webhooks/versioning.md).
4. [Test your integration](https://docs.stripe.com/testing.md) against the new version.
5. If you use Connect, [test your Connect integration](https://docs.stripe.com/connect/testing.md).
6. In Workbench, [perform the upgrade](https://docs.stripe.com/upgrades.md#perform-the-upgrade). You can [roll back the version](https://docs.stripe.com/upgrades.md#roll-back-your-api-version) for 72 hours.

Learn more about [Stripe API upgrades](https://docs.stripe.com/upgrades.md).
