# Adds Account Signals, Account Evaluations and Account Activity APIs in public preview

## What’s new

Introduces the following v2 APIs in public preview:

- [Account Evaluation](https://docs.stripe.com/api/v2/signals/account-evaluations.md?api-version=2026-08-26.preview): Request evaluations for the `user_account_sharing` and `user_multi_accounting` [requested_signals](https://docs.stripe.com/api/v2/signals/account-evaluations/object.md?api-version=2026-08-26.preview#v2_signals_account_evaluation_object-requested_signals) types. This API sends the `v2.signals.account_evaluation.complete` event when all pending evaluation signals finish processing so you can use the risk signal result to direct your decision.
- [Account Activity](https://docs.stripe.com/api/v2/signals/account-activities.md?api-version=2026-08-26.preview): Create account activity events, such as login and registration attempts, to use in requesting evaluations, then report the outcome to Stripe to reconcile your risk-signal based decisions and improve future evaluations. You can create, retrieve and delete recorded activities.
- [Account Signal](https://docs.stripe.com/api/v2/signals/account-signals.md?api-version=2026-08-26.preview): List and retrieve individual risk signals generated for accounts.

## Impact

You can now send account activity data, such as login and registration attempts, to Stripe’s Signals APIs and request on-demand evaluations about whether your accounts might be engaged in account sharing or multi-accounting. Stripe returns a risk score to help you manage your abuse prevention strategy. You can also report the action you take based on the risk evaluation results and look up individual past signals.

## Changes

#### REST API

|  | Change | Resources |
| --- | --- | --- |
|  | Added | [V2.Signals.AccountActivity](/api/v2/signals/account-activities/object?api-version=2026-08-26.preview#v2_signals_account_activity_object), [V2.Signals.AccountEvaluation](/api/v2/signals/account-evaluations/object?api-version=2026-08-26.preview#v2_signals_account_evaluation_object), [V2.Signals.AccountSignal](/api/v2/signals/account-signals/object?api-version=2026-08-26.preview#v2_account_signal_object) |

| Endpoints | Change | Resources |
| --- | --- | --- |
| `list`, `retrieve` | Added | [V2.Signals.AccountSignal](/api/v2/signals/account-signals/object?api-version=2026-08-26.preview#v2_account_signal_object) |
| `create`, `retrieve` | Added | [V2.Signals.AccountEvaluation](/api/v2/signals/account-evaluations/object?api-version=2026-08-26.preview#v2_signals_account_evaluation_object) |
| `create`, `delete`, `retrieve` | Added | [V2.Signals.AccountActivity](/api/v2/signals/account-activities/object?api-version=2026-08-26.preview#v2_signals_account_activity_object) |

|  | Change | Event type |
| --- | --- | --- |
| `V2SignalsAccountEvaluationCompleteEvent` | Added | `V2.Signals.AccountEvaluation` |

#### Ruby

|  | Change | Resources |
| --- | --- | --- |
|  | Added | [V2::Signals::AccountActivity](/api/v2/signals/account-activities/object?api-version=2026-08-26.preview#v2_signals_account_activity_object), [V2::Signals::AccountEvaluation](/api/v2/signals/account-evaluations/object?api-version=2026-08-26.preview#v2_signals_account_evaluation_object), [V2::Signals::AccountSignal](/api/v2/signals/account-signals/object?api-version=2026-08-26.preview#v2_account_signal_object) |

| Methods | Change | Resources |
| --- | --- | --- |
| `list`, `retrieve` | Added | [V2::Signals::AccountSignal](/api/v2/signals/account-signals/object?api-version=2026-08-26.preview#v2_account_signal_object) |
| `create`, `retrieve` | Added | [V2::Signals::AccountEvaluation](/api/v2/signals/account-evaluations/object?api-version=2026-08-26.preview#v2_signals_account_evaluation_object) |
| `create`, `delete`, `retrieve` | Added | [V2::Signals::AccountActivity](/api/v2/signals/account-activities/object?api-version=2026-08-26.preview#v2_signals_account_activity_object) |

|  | Change | Event type |
| --- | --- | --- |
| `V2SignalsAccountEvaluationCompleteEvent` | Added | `V2::Signals::AccountEvaluation` |

#### Python

|  | Change | Resources |
| --- | --- | --- |
|  | Added | [v2.signals.AccountActivity](/api/v2/signals/account-activities/object?api-version=2026-08-26.preview#v2_signals_account_activity_object), [v2.signals.AccountEvaluation](/api/v2/signals/account-evaluations/object?api-version=2026-08-26.preview#v2_signals_account_evaluation_object), [v2.signals.AccountSignal](/api/v2/signals/account-signals/object?api-version=2026-08-26.preview#v2_account_signal_object) |

| Methods | Change | Resources |
| --- | --- | --- |
| `list`, `retrieve` | Added | [v2.signals.AccountSignal](/api/v2/signals/account-signals/object?api-version=2026-08-26.preview#v2_account_signal_object) |
| `create`, `retrieve` | Added | [v2.signals.AccountEvaluation](/api/v2/signals/account-evaluations/object?api-version=2026-08-26.preview#v2_signals_account_evaluation_object) |
| `create`, `delete`, `retrieve` | Added | [v2.signals.AccountActivity](/api/v2/signals/account-activities/object?api-version=2026-08-26.preview#v2_signals_account_activity_object) |

|  | Change | Event type |
| --- | --- | --- |
| `V2SignalsAccountEvaluationCompleteEvent` | Added | `v2.signals.AccountEvaluation` |

#### PHP

|  | Change | Resources |
| --- | --- | --- |
|  | Added | [V2.Signals.AccountActivity](/api/v2/signals/account-activities/object?api-version=2026-08-26.preview#v2_signals_account_activity_object), [V2.Signals.AccountEvaluation](/api/v2/signals/account-evaluations/object?api-version=2026-08-26.preview#v2_signals_account_evaluation_object), [V2.Signals.AccountSignal](/api/v2/signals/account-signals/object?api-version=2026-08-26.preview#v2_account_signal_object) |

| Methods | Change | Resources |
| --- | --- | --- |
| `all`, `retrieve` | Added | [V2.Signals.AccountSignal](/api/v2/signals/account-signals/object?api-version=2026-08-26.preview#v2_account_signal_object) |
| `create`, `retrieve` | Added | [V2.Signals.AccountEvaluation](/api/v2/signals/account-evaluations/object?api-version=2026-08-26.preview#v2_signals_account_evaluation_object) |
| `create`, `delete`, `retrieve` | Added | [V2.Signals.AccountActivity](/api/v2/signals/account-activities/object?api-version=2026-08-26.preview#v2_signals_account_activity_object) |

|  | Change | Event type |
| --- | --- | --- |
| `V2SignalsAccountEvaluationCompleteEvent` | Added | `V2.Signals.AccountEvaluation` |

#### Java

|  | Change | Resources |
| --- | --- | --- |
|  | Added | [v2.signals.AccountActivity](/api/v2/signals/account-activities/object?api-version=2026-08-26.preview#v2_signals_account_activity_object), [v2.signals.AccountEvaluation](/api/v2/signals/account-evaluations/object?api-version=2026-08-26.preview#v2_signals_account_evaluation_object), [v2.signals.AccountSignal](/api/v2/signals/account-signals/object?api-version=2026-08-26.preview#v2_account_signal_object) |

| Methods | Change | Resources |
| --- | --- | --- |
| `list`, `retrieve` | Added | [v2.signals.AccountSignal](/api/v2/signals/account-signals/object?api-version=2026-08-26.preview#v2_account_signal_object) |
| `create`, `retrieve` | Added | [v2.signals.AccountEvaluation](/api/v2/signals/account-evaluations/object?api-version=2026-08-26.preview#v2_signals_account_evaluation_object) |
| `create`, `delete`, `retrieve` | Added | [v2.signals.AccountActivity](/api/v2/signals/account-activities/object?api-version=2026-08-26.preview#v2_signals_account_activity_object) |

|  | Change | Event type |
| --- | --- | --- |
| `V2SignalsAccountEvaluationCompleteEvent` | Added | `v2.signals.AccountEvaluation` |

#### Node.js

|  | Change | Resources |
| --- | --- | --- |
|  | Added | [V2.Signals.AccountActivity](/api/v2/signals/account-activities/object?api-version=2026-08-26.preview#v2_signals_account_activity_object), [V2.Signals.AccountEvaluation](/api/v2/signals/account-evaluations/object?api-version=2026-08-26.preview#v2_signals_account_evaluation_object), [V2.Signals.AccountSignal](/api/v2/signals/account-signals/object?api-version=2026-08-26.preview#v2_account_signal_object) |

| Methods | Change | Resources |
| --- | --- | --- |
| `list`, `retrieve` | Added | [V2.Signals.AccountSignal](/api/v2/signals/account-signals/object?api-version=2026-08-26.preview#v2_account_signal_object) |
| `create`, `retrieve` | Added | [V2.Signals.AccountEvaluation](/api/v2/signals/account-evaluations/object?api-version=2026-08-26.preview#v2_signals_account_evaluation_object) |
| `create`, `del`, `retrieve` | Added | [V2.Signals.AccountActivity](/api/v2/signals/account-activities/object?api-version=2026-08-26.preview#v2_signals_account_activity_object) |

|  | Change | Event type |
| --- | --- | --- |
| `V2SignalsAccountEvaluationCompleteEvent` | Added | `V2.Signals.AccountEvaluation` |

#### Go

|  | Change | Resources |
| --- | --- | --- |
|  | Added | [V2SignalsAccountActivity](/api/v2/signals/account-activities/object?api-version=2026-08-26.preview#v2_signals_account_activity_object), [V2SignalsAccountEvaluation](/api/v2/signals/account-evaluations/object?api-version=2026-08-26.preview#v2_signals_account_evaluation_object), [V2SignalsAccountSignal](/api/v2/signals/account-signals/object?api-version=2026-08-26.preview#v2_account_signal_object) |

| Methods | Change | Resources |
| --- | --- | --- |
| `Get`, `List` | Added | [V2SignalsAccountSignal](/api/v2/signals/account-signals/object?api-version=2026-08-26.preview#v2_account_signal_object) |
| `Get`, `New` | Added | [V2SignalsAccountEvaluation](/api/v2/signals/account-evaluations/object?api-version=2026-08-26.preview#v2_signals_account_evaluation_object) |
| `Del`, `Get`, `New` | Added | [V2SignalsAccountActivity](/api/v2/signals/account-activities/object?api-version=2026-08-26.preview#v2_signals_account_activity_object) |

|  | Change | Event type |
| --- | --- | --- |
| `V2SignalsAccountEvaluationCompleteEvent` | Added | `V2SignalsAccountEvaluation` |

#### .NET

|  | Change | Resources |
| --- | --- | --- |
|  | Added | [V2.Signals.AccountActivity](/api/v2/signals/account-activities/object?api-version=2026-08-26.preview#v2_signals_account_activity_object), [V2.Signals.AccountEvaluation](/api/v2/signals/account-evaluations/object?api-version=2026-08-26.preview#v2_signals_account_evaluation_object), [V2.Signals.AccountSignal](/api/v2/signals/account-signals/object?api-version=2026-08-26.preview#v2_account_signal_object) |

| Methods | Change | Resources |
| --- | --- | --- |
| `Get`, `List` | Added | [V2.Signals.AccountSignal](/api/v2/signals/account-signals/object?api-version=2026-08-26.preview#v2_account_signal_object) |
| `Create`, `Get` | Added | [V2.Signals.AccountEvaluation](/api/v2/signals/account-evaluations/object?api-version=2026-08-26.preview#v2_signals_account_evaluation_object) |
| `Create`, `Delete`, `Get` | Added | [V2.Signals.AccountActivity](/api/v2/signals/account-activities/object?api-version=2026-08-26.preview#v2_signals_account_activity_object) |

|  | Change | Event type |
| --- | --- | --- |
| `V2SignalsAccountEvaluationCompleteEvent` | Added | `V2.Signals.AccountEvaluation` |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2026-08-26.preview`
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

- [Redirects new Connect platforms away from unsupported integration patterns](https://docs.stripe.com/changelog/dahlia/2026-08-26/2026-08-17-blocks-unsupported-integration-patterns.md)
- [Adds control over Stripe user authentication to Payment Method Settings](https://docs.stripe.com/changelog/dahlia/2026-08-26/payment-method-settings-disable-stripe-user-authentication.md)
