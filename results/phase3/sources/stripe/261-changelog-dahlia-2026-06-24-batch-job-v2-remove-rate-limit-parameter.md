# Removes the rate limit parameter from the Batch Job v2 object

## What’s new

Removes the [maximum_rps](https://docs.stripe.com/api/v2/core/batch-jobs/object.md?api-version=2026-05-27.preview#v2_batch_job_object-maximum_rps) parameter from the [Batch Job v2](https://docs.stripe.com/api/v2/core/batch-jobs/object.md?api-version=2026-06-24.preview) object and the [create Batch Job v2](https://docs.stripe.com/api/v2/core/batch-jobs/create.md?api-version=2026-06-24.preview) endpoint. Previously, you could use `maximum_rps` to set a per-second request rate limit when creating a batch job. We now manage batch job throughput automatically.

## Why is this a breaking change?

If your integration passes `maximum_rps` when creating a Batch Job v2, you must remove that parameter from your request. Requests that include `maximum_rps` return an error after this change takes effect.

## Impact

You no longer need to configure a rate limit when creating a Batch Job v2. We now manage throughput automatically, giving you consistent performance without any per-request configuration. Before upgrading to this API version, remove `maximum_rps` from any create Batch Job v2 requests.

## Changes

#### REST API

| Parameter | Change | Resources or endpoints |
| --- | --- | --- |
| `maximum_rps` | Removed | [V2.Core.BatchJob](/api/v2/core/batch-jobs/object?api-version=2026-06-24.preview#v2_batch_job_object), [V2.Core.BatchJob#create](/api/v2/core/batch-jobs/create?api-version=2026-06-24.preview#v2_create_batch_jobs) |

#### Ruby

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `maximum_rps` | Removed | [V2::Core::BatchJob](/api/v2/core/batch-jobs/object?api-version=2026-06-24.preview#v2_batch_job_object), [V2::Core::BatchJobCreateParams](/api/v2/core/batch-jobs/create?api-version=2026-06-24.preview#v2_create_batch_jobs) |

#### Python

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `maximum_rps` | Removed | [V2.Core.BatchJob](/api/v2/core/batch-jobs/object?api-version=2026-06-24.preview#v2_batch_job_object), [v2.core.BatchJobCreateParams](/api/v2/core/batch-jobs/create?api-version=2026-06-24.preview#v2_create_batch_jobs) |

#### PHP

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `maximum_rps` | Removed | [V2.Core.BatchJob](/api/v2/core/batch-jobs/object?api-version=2026-06-24.preview#v2_batch_job_object), [V2\Core\BatchJob.create().$params](/api/v2/core/batch-jobs/create?api-version=2026-06-24.preview#v2_create_batch_jobs) |

#### Java

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `maximumRps` | Removed | [v2.core.BatchJob](/api/v2/core/batch-jobs/object?api-version=2026-06-24.preview#v2_batch_job_object), [v2.core.BatchJobCreateParams](/api/v2/core/batch-jobs/create?api-version=2026-06-24.preview#v2_create_batch_jobs) |

#### Node.js

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `maximum_rps` | Removed | [V2.Core.BatchJob](/api/v2/core/batch-jobs/object?api-version=2026-06-24.preview#v2_batch_job_object), [V2.Core.BatchJobCreateParams](/api/v2/core/batch-jobs/create?api-version=2026-06-24.preview#v2_create_batch_jobs) |

#### Go

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `MaximumRps` | Removed | [V2CoreBatchJob](/api/v2/core/batch-jobs/object?api-version=2026-06-24.preview#v2_batch_job_object), [V2CoreBatchJobParams](/api/v2/core/batch-jobs/create?api-version=2026-06-24.preview#v2_create_batch_jobs) |

#### .NET

| Parameter | Change | Resources or methods |
| --- | --- | --- |
| `MaximumRps` | Removed | [V2.Core.BatchJob](/api/v2/core/batch-jobs/object?api-version=2026-06-24.preview#v2_batch_job_object), [V2.Core.BatchJobCreateOptions](/api/v2/core/batch-jobs/create?api-version=2026-06-24.preview#v2_create_batch_jobs) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2026-06-24.preview`
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
