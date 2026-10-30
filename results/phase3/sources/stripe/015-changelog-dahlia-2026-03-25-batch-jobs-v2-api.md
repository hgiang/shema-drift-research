# Adds support for running API operations in batches

## What’s new

Adds the ability to create, process, and track large asynchronous batches of API operations using the new [Batch Jobs v2 API](https://docs.stripe.com/api/v2/core/batch-jobs.md?api-version=2026-03-25.preview).

## Impact

You can now create batches of API calls to run asynchronously. That helps you handle large-scale operations efficiently and process bulk operations like creating multiple customers, migrating subscriptions, or updating large datasets.

The Batch Jobs API has built-in error handling and progress tracking through webhook events. For more detail about working with it and the resources it supports, see [Batch jobs](https://docs.stripe.com/api/v2/core/batch-jobs.md?api-version=2026-03-25.preview).

## Changes

#### REST API

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [V2.Core.BatchJob](/api/v2/core/batch-jobs?api-version=2026-03-25.preview) |

| Endpoints | Change | Resource |
| --- | --- | --- |
| `cancel`, `create`, `retrieve` | Added | [V2.Core.BatchJob](/api/v2/core/batch-jobs/cancel?api-version=2026-03-25.preview) |

|  | Change | Event type |
| --- | --- | --- |
| `V2CoreBatchJobBatchFailedEvent`, `V2CoreBatchJobCanceledEvent`, `V2CoreBatchJobCompletedEvent`, `V2CoreBatchJobCreatedEvent`, `V2CoreBatchJobReadyForUploadEvent`, `V2CoreBatchJobTimeoutEvent`, `V2CoreBatchJobUpdatedEvent`, `V2CoreBatchJobUploadTimeoutEvent`, `V2CoreBatchJobValidatingEvent`, `V2CoreBatchJobValidationFailedEvent` | Added | `V2.Core.BatchJob` |

#### Ruby

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [V2::Core::BatchJob](/api/v2/core/batch-jobs?api-version=2026-03-25.preview) |

| Methods | Change | Resource |
| --- | --- | --- |
| `cancel`, `create`, `retrieve` | Added | [V2::Core::BatchJob](/api/v2/core/batch-jobs/cancel?api-version=2026-03-25.preview) |

|  | Change | Event type |
| --- | --- | --- |
| `V2CoreBatchJobBatchFailedEvent`, `V2CoreBatchJobCanceledEvent`, `V2CoreBatchJobCompletedEvent`, `V2CoreBatchJobCreatedEvent`, `V2CoreBatchJobReadyForUploadEvent`, `V2CoreBatchJobTimeoutEvent`, `V2CoreBatchJobUpdatedEvent`, `V2CoreBatchJobUploadTimeoutEvent`, `V2CoreBatchJobValidatingEvent`, `V2CoreBatchJobValidationFailedEvent` | Added | `V2::Core::BatchJob` |

#### Python

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [v2.core.BatchJob](/api/v2/core/batch-jobs?api-version=2026-03-25.preview) |

| Methods | Change | Resource |
| --- | --- | --- |
| `cancel`, `create`, `retrieve` | Added | [v2.core.BatchJob](/api/v2/core/batch-jobs/cancel?api-version=2026-03-25.preview) |

|  | Change | Event type |
| --- | --- | --- |
| `V2CoreBatchJobBatchFailedEvent`, `V2CoreBatchJobCanceledEvent`, `V2CoreBatchJobCompletedEvent`, `V2CoreBatchJobCreatedEvent`, `V2CoreBatchJobReadyForUploadEvent`, `V2CoreBatchJobTimeoutEvent`, `V2CoreBatchJobUpdatedEvent`, `V2CoreBatchJobUploadTimeoutEvent`, `V2CoreBatchJobValidatingEvent`, `V2CoreBatchJobValidationFailedEvent` | Added | `v2.core.BatchJob` |

#### PHP

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [V2.Core.BatchJob](/api/v2/core/batch-jobs?api-version=2026-03-25.preview) |

| Methods | Change | Resource |
| --- | --- | --- |
| `cancel`, `create`, `retrieve` | Added | [V2.Core.BatchJob](/api/v2/core/batch-jobs/cancel?api-version=2026-03-25.preview) |

|  | Change | Event type |
| --- | --- | --- |
| `V2CoreBatchJobBatchFailedEvent`, `V2CoreBatchJobCanceledEvent`, `V2CoreBatchJobCompletedEvent`, `V2CoreBatchJobCreatedEvent`, `V2CoreBatchJobReadyForUploadEvent`, `V2CoreBatchJobTimeoutEvent`, `V2CoreBatchJobUpdatedEvent`, `V2CoreBatchJobUploadTimeoutEvent`, `V2CoreBatchJobValidatingEvent`, `V2CoreBatchJobValidationFailedEvent` | Added | `V2.Core.BatchJob` |

#### Java

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [v2.core.BatchJob](/api/v2/core/batch-jobs?api-version=2026-03-25.preview) |

| Methods | Change | Resource |
| --- | --- | --- |
| `cancel`, `create`, `retrieve` | Added | [v2.core.BatchJob](/api/v2/core/batch-jobs/cancel?api-version=2026-03-25.preview) |

|  | Change | Event type |
| --- | --- | --- |
| `V2CoreBatchJobBatchFailedEvent`, `V2CoreBatchJobCanceledEvent`, `V2CoreBatchJobCompletedEvent`, `V2CoreBatchJobCreatedEvent`, `V2CoreBatchJobReadyForUploadEvent`, `V2CoreBatchJobTimeoutEvent`, `V2CoreBatchJobUpdatedEvent`, `V2CoreBatchJobUploadTimeoutEvent`, `V2CoreBatchJobValidatingEvent`, `V2CoreBatchJobValidationFailedEvent` | Added | `v2.core.BatchJob` |

#### Node.js

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [V2.Core.BatchJob](/api/v2/core/batch-jobs?api-version=2026-03-25.preview) |

| Methods | Change | Resource |
| --- | --- | --- |
| `cancel`, `create`, `retrieve` | Added | [V2.Core.BatchJob](/api/v2/core/batch-jobs/cancel?api-version=2026-03-25.preview) |

|  | Change | Event type |
| --- | --- | --- |
| `V2CoreBatchJobBatchFailedEvent`, `V2CoreBatchJobCanceledEvent`, `V2CoreBatchJobCompletedEvent`, `V2CoreBatchJobCreatedEvent`, `V2CoreBatchJobReadyForUploadEvent`, `V2CoreBatchJobTimeoutEvent`, `V2CoreBatchJobUpdatedEvent`, `V2CoreBatchJobUploadTimeoutEvent`, `V2CoreBatchJobValidatingEvent`, `V2CoreBatchJobValidationFailedEvent` | Added | `V2.Core.BatchJob` |

#### Go

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [V2CoreBatchJob](/api/v2/core/batch-jobs?api-version=2026-03-25.preview) |

| Methods | Change | Resource |
| --- | --- | --- |
| `Cancel`, `Get`, `New` | Added | [V2CoreBatchJob](/api/v2/core/batch-jobs/cancel?api-version=2026-03-25.preview) |

|  | Change | Event type |
| --- | --- | --- |
| `V2CoreBatchJobBatchFailedEvent`, `V2CoreBatchJobCanceledEvent`, `V2CoreBatchJobCompletedEvent`, `V2CoreBatchJobCreatedEvent`, `V2CoreBatchJobReadyForUploadEvent`, `V2CoreBatchJobTimeoutEvent`, `V2CoreBatchJobUpdatedEvent`, `V2CoreBatchJobUploadTimeoutEvent`, `V2CoreBatchJobValidatingEvent`, `V2CoreBatchJobValidationFailedEvent` | Added | `V2CoreBatchJob` |

#### .NET

|  | Change | Resource |
| --- | --- | --- |
|  | Added | [V2.Core.BatchJob](/api/v2/core/batch-jobs?api-version=2026-03-25.preview) |

| Methods | Change | Resource |
| --- | --- | --- |
| `Cancel`, `Create`, `Get` | Added | [V2.Core.BatchJob](/api/v2/core/batch-jobs/cancel?api-version=2026-03-25.preview) |

|  | Change | Event type |
| --- | --- | --- |
| `V2CoreBatchJobBatchFailedEvent`, `V2CoreBatchJobCanceledEvent`, `V2CoreBatchJobCompletedEvent`, `V2CoreBatchJobCreatedEvent`, `V2CoreBatchJobReadyForUploadEvent`, `V2CoreBatchJobTimeoutEvent`, `V2CoreBatchJobUpdatedEvent`, `V2CoreBatchJobUploadTimeoutEvent`, `V2CoreBatchJobValidatingEvent`, `V2CoreBatchJobValidationFailedEvent` | Added | `V2.Core.BatchJob` |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2026-03-25.preview`
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
