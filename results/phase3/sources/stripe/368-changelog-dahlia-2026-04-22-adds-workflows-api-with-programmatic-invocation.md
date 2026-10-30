# Adds programmatic invocation of Stripe Workflows

## What’s new

This change adds new APIs to work with [Stripe Workflows](https://docs.stripe.com/workflows.md). You can now [list](https://docs.stripe.com/api/v2/extend/workflows/list.md?api-version=2026-04-22.preview), [retrieve](https://docs.stripe.com/api/v2/extend/workflows/retrieve.md?api-version=2026-04-22.preview) and programmatically [invoke](https://docs.stripe.com/api/v2/extend/workflow-runs/invoke-workflow.md?api-version=2026-04-22.preview) workflows created through the Dashboard. Previously, workflows could only be triggered by [Stripe events](https://docs.stripe.com/events/how-events-work.md).

This change also adds methods to [list](https://docs.stripe.com/api/v2/extend/workflow-runs/list.md?api-version=2026-04-22.preview) and [retrieve](https://docs.stripe.com/api/v2/extend/workflow-runs/retrieve.md?api-version=2026-04-22.preview) [workflow runs](https://docs.stripe.com/api/v2/extend/workflow-runs.md?api-version=2026-04-22.preview), including [events](https://docs.stripe.com/api/v2/extend/workflow-runs/event-types.md?api-version=2026-04-22.preview) emitted during a workflow run’s lifecycle.

## Impact

You can now integrate workflow execution into your application’s logic, enabling use cases such as:

- Starting workflows in response to user actions within your application
- Triggering workflows as part of batch processing operations
- Triggering workflows in response to the success or failure of other workflows

You can now monitor workflow runs from within your own application. Subscribe to workflow run lifecycle events to be notified or take actions in response to the status of workflow runs.

## Changes

#### REST API

|  | Change | Resources |
| --- | --- | --- |
|  | Added | [V2.Extend.Workflow](/api/v2/extend/workflows/object?api-version=2026-04-22.preview#v2_workflow_object), [V2.Extend.WorkflowRun](/api/v2/extend/workflow-runs/object?api-version=2026-04-22.preview#v2_workflow_run_object) |

| Endpoints | Change | Resources |
| --- | --- | --- |
| `list`, `retrieve` | Added | [V2.Extend.WorkflowRun](/api/v2/extend/workflow-runs/object?api-version=2026-04-22.preview#v2_workflow_run_object) |
| `invoke`, `list`, `retrieve` | Added | [V2.Extend.Workflow](/api/v2/extend/workflows/object?api-version=2026-04-22.preview#v2_workflow_object) |

|  | Change | Event type |
| --- | --- | --- |
| `V2ExtendWorkflowRunFailedEvent`, `V2ExtendWorkflowRunStartedEvent`, `V2ExtendWorkflowRunSucceededEvent` | Added | `V2.Extend.WorkflowRun` |

#### Ruby

|  | Change | Resources |
| --- | --- | --- |
|  | Added | [V2::Extend::Workflow](/api/v2/extend/workflows/object?api-version=2026-04-22.preview#v2_workflow_object), [V2::Extend::WorkflowRun](/api/v2/extend/workflow-runs/object?api-version=2026-04-22.preview#v2_workflow_run_object) |

| Methods | Change | Resources |
| --- | --- | --- |
| `list`, `retrieve` | Added | [V2::Extend::WorkflowRun](/api/v2/extend/workflow-runs/object?api-version=2026-04-22.preview#v2_workflow_run_object) |
| `invoke`, `list`, `retrieve` | Added | [V2::Extend::Workflow](/api/v2/extend/workflows/object?api-version=2026-04-22.preview#v2_workflow_object) |

|  | Change | Event type |
| --- | --- | --- |
| `V2ExtendWorkflowRunFailedEvent`, `V2ExtendWorkflowRunStartedEvent`, `V2ExtendWorkflowRunSucceededEvent` | Added | `V2::Extend::WorkflowRun` |

#### Python

|  | Change | Resources |
| --- | --- | --- |
|  | Added | [v2.extend.Workflow](/api/v2/extend/workflows/object?api-version=2026-04-22.preview#v2_workflow_object), [v2.extend.WorkflowRun](/api/v2/extend/workflow-runs/object?api-version=2026-04-22.preview#v2_workflow_run_object) |

| Methods | Change | Resources |
| --- | --- | --- |
| `list`, `retrieve` | Added | [v2.extend.WorkflowRun](/api/v2/extend/workflow-runs/object?api-version=2026-04-22.preview#v2_workflow_run_object) |
| `invoke`, `list`, `retrieve` | Added | [v2.extend.Workflow](/api/v2/extend/workflows/object?api-version=2026-04-22.preview#v2_workflow_object) |

|  | Change | Event type |
| --- | --- | --- |
| `V2ExtendWorkflowRunFailedEvent`, `V2ExtendWorkflowRunStartedEvent`, `V2ExtendWorkflowRunSucceededEvent` | Added | `v2.extend.WorkflowRun` |

#### PHP

|  | Change | Resources |
| --- | --- | --- |
|  | Added | [V2.Extend.Workflow](/api/v2/extend/workflows/object?api-version=2026-04-22.preview#v2_workflow_object), [V2.Extend.WorkflowRun](/api/v2/extend/workflow-runs/object?api-version=2026-04-22.preview#v2_workflow_run_object) |

| Methods | Change | Resources |
| --- | --- | --- |
| `all`, `retrieve` | Added | [V2.Extend.WorkflowRun](/api/v2/extend/workflow-runs/object?api-version=2026-04-22.preview#v2_workflow_run_object) |
| `all`, `invoke`, `retrieve` | Added | [V2.Extend.Workflow](/api/v2/extend/workflows/object?api-version=2026-04-22.preview#v2_workflow_object) |

|  | Change | Event type |
| --- | --- | --- |
| `V2ExtendWorkflowRunFailedEvent`, `V2ExtendWorkflowRunStartedEvent`, `V2ExtendWorkflowRunSucceededEvent` | Added | `V2.Extend.WorkflowRun` |

#### Java

|  | Change | Resources |
| --- | --- | --- |
|  | Added | [v2.extend.Workflow](/api/v2/extend/workflows/object?api-version=2026-04-22.preview#v2_workflow_object), [v2.extend.WorkflowRun](/api/v2/extend/workflow-runs/object?api-version=2026-04-22.preview#v2_workflow_run_object) |

| Methods | Change | Resources |
| --- | --- | --- |
| `list`, `retrieve` | Added | [v2.extend.WorkflowRun](/api/v2/extend/workflow-runs/object?api-version=2026-04-22.preview#v2_workflow_run_object) |
| `invoke`, `list`, `retrieve` | Added | [v2.extend.Workflow](/api/v2/extend/workflows/object?api-version=2026-04-22.preview#v2_workflow_object) |

|  | Change | Event type |
| --- | --- | --- |
| `V2ExtendWorkflowRunFailedEvent`, `V2ExtendWorkflowRunStartedEvent`, `V2ExtendWorkflowRunSucceededEvent` | Added | `v2.extend.WorkflowRun` |

#### Node.js

|  | Change | Resources |
| --- | --- | --- |
|  | Added | [V2.Extend.Workflow](/api/v2/extend/workflows/object?api-version=2026-04-22.preview#v2_workflow_object), [V2.Extend.WorkflowRun](/api/v2/extend/workflow-runs/object?api-version=2026-04-22.preview#v2_workflow_run_object) |

| Methods | Change | Resources |
| --- | --- | --- |
| `list`, `retrieve` | Added | [V2.Extend.WorkflowRun](/api/v2/extend/workflow-runs/object?api-version=2026-04-22.preview#v2_workflow_run_object) |
| `invoke`, `list`, `retrieve` | Added | [V2.Extend.Workflow](/api/v2/extend/workflows/object?api-version=2026-04-22.preview#v2_workflow_object) |

|  | Change | Event type |
| --- | --- | --- |
| `V2ExtendWorkflowRunFailedEvent`, `V2ExtendWorkflowRunStartedEvent`, `V2ExtendWorkflowRunSucceededEvent` | Added | `V2.Extend.WorkflowRun` |

#### Go

|  | Change | Resources |
| --- | --- | --- |
|  | Added | [V2ExtendWorkflow](/api/v2/extend/workflows/object?api-version=2026-04-22.preview#v2_workflow_object), [V2ExtendWorkflowRun](/api/v2/extend/workflow-runs/object?api-version=2026-04-22.preview#v2_workflow_run_object) |

| Methods | Change | Resources |
| --- | --- | --- |
| `Get`, `List` | Added | [V2ExtendWorkflowRun](/api/v2/extend/workflow-runs/object?api-version=2026-04-22.preview#v2_workflow_run_object) |
| `Get`, `Invoke`, `List` | Added | [V2ExtendWorkflow](/api/v2/extend/workflows/object?api-version=2026-04-22.preview#v2_workflow_object) |

|  | Change | Event type |
| --- | --- | --- |
| `V2ExtendWorkflowRunFailedEvent`, `V2ExtendWorkflowRunStartedEvent`, `V2ExtendWorkflowRunSucceededEvent` | Added | `V2ExtendWorkflowRun` |

#### .NET

|  | Change | Resources |
| --- | --- | --- |
|  | Added | [V2.Extend.Workflow](/api/v2/extend/workflows/object?api-version=2026-04-22.preview#v2_workflow_object), [V2.Extend.WorkflowRun](/api/v2/extend/workflow-runs/object?api-version=2026-04-22.preview#v2_workflow_run_object) |

| Methods | Change | Resources |
| --- | --- | --- |
| `Get`, `List` | Added | [V2.Extend.WorkflowRun](/api/v2/extend/workflow-runs/object?api-version=2026-04-22.preview#v2_workflow_run_object) |
| `Get`, `Invoke`, `List` | Added | [V2.Extend.Workflow](/api/v2/extend/workflows/object?api-version=2026-04-22.preview#v2_workflow_object) |

|  | Change | Event type |
| --- | --- | --- |
| `V2ExtendWorkflowRunFailedEvent`, `V2ExtendWorkflowRunStartedEvent`, `V2ExtendWorkflowRunSucceededEvent` | Added | `V2.Extend.WorkflowRun` |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2026-04-22.preview`
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
