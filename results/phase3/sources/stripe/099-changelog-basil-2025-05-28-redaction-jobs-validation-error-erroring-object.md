# Updated validation errors for redaction jobs to specify affected objects

## What’s new

Validation errors for redaction jobs now include the [id](https://docs.stripe.com/api/privacy/redaction-job-validation-error/object.md?api-version=2025-05-28.basil#privacy_redaction_job_validation_error_object-erroring_object-id) and [object_type](https://docs.stripe.com/api/privacy/redaction-job-validation-error/object.md?api-version=2025-05-28.basil#privacy_redaction_job_validation_error_object-erroring_object-object_type) for affected objects during a redaction job.

## Impact

Previously, this validation error only returned a nullable dictionary. If you’re using the [erroring_object](https://docs.stripe.com/api/privacy/redaction-job-validation-error/object.md?api-version=2025-05-28.basil#privacy_redaction_job_validation_error_object-erroring_object) field, update your integration to expect values on the `id` and `object_type` fields only.

## Changes

#### REST API

| Field | Change | From → to |
| --- | --- | --- |
| `Privacy.RedactionJobValidationError.erroring_object` | Changed | [map(string: string) → RedactionResourceErroringObject](/api/privacy/redaction-job-validation-error/object?api-version=2025-05-28.preview) |

#### Ruby

| Field | Change | From → to |
| --- | --- | --- |
| `Privacy::RedactionJobValidationError.erroring_object` | Changed | [map(string: string) → RedactionResourceErroringObject](/api/privacy/redaction-job-validation-error/object?api-version=2025-05-28.preview) |

#### Python

| Field | Change | From → to |
| --- | --- | --- |
| `Privacy.RedactionJobValidationError.erroring_object` | Changed | [map(string: string) → RedactionResourceErroringObject](/api/privacy/redaction-job-validation-error/object?api-version=2025-05-28.preview) |

#### PHP

| Field | Change | From → to |
| --- | --- | --- |
| `Privacy.RedactionJobValidationError.erroring_object` | Changed | [map(string: string) → RedactionResourceErroringObject](/api/privacy/redaction-job-validation-error/object?api-version=2025-05-28.preview) |

#### Java

| Field | Change | From → to |
| --- | --- | --- |
| `privacy.RedactionJobValidationError.erroringObject` | Changed | [map(string: string) → RedactionResourceErroringObject](/api/privacy/redaction-job-validation-error/object?api-version=2025-05-28.preview) |

#### Node.js

| Field | Change | From → to |
| --- | --- | --- |
| `Privacy.RedactionJobValidationError.erroring_object` | Changed | [map(string: string) → RedactionResourceErroringObject](/api/privacy/redaction-job-validation-error/object?api-version=2025-05-28.preview) |

#### Go

| Field | Change | From → to |
| --- | --- | --- |
| `PrivacyRedactionJobValidationError.ErroringObject` | Changed | [map(string: string) → RedactionResourceErroringObject](/api/privacy/redaction-job-validation-error/object?api-version=2025-05-28.preview) |

#### .NET

| Field | Change | From → to |
| --- | --- | --- |
| `Privacy.RedactionJobValidationError.ErroringObject` | Changed | [map(string: string) → RedactionResourceErroringObject](/api/privacy/redaction-job-validation-error/object?api-version=2025-05-28.preview) |

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
