# Expands action coverage in Activity Logs

## What’s new

Adds new action types, action groups, action details, actor information and related request and object information to the [Activity Logs API](https://docs.stripe.com/api/v2/iam/activity-logs.md?api-version=2026-09-30.preview).

The [action_groups](https://docs.stripe.com/api/v2/iam/activity-logs/list.md?api-version=2026-09-30.preview#v2_list_activity_logs-action_groups) parameter now supports  `sso`, `scim`, `user_profile`, `account_security`, `authentication`, `payout` and `issuing`. You can use this parameter to filter results to only include activity logs for the specified action group types.

Adds 50 [type](https://docs.stripe.com/api/v2/iam/activity-logs/object.md?api-version=2026-09-30.preview#v2_activity_log_object-type) enum values under these newly added action groups.

The [details](https://docs.stripe.com/api/v2/iam/activity-logs/object.md?api-version=2026-09-30.preview#v2_activity_log_object-details) property now returns action-specific fields for additional action groups: SSO, SCIM, user profile, account security and authentication, including SSO enforcement levels, SCIM group and membership changes, user profile values, anomaly detection settings and the authentication challenge type.

Adds a `stripe_action` value to the [actor.type](https://docs.stripe.com/api/v2/iam/activity-logs/object.md?api-version=2026-09-30.preview#v2_activity_log_object-actor-type) enum. This is used when a Stripe system or support performs the action.

Adds a [related_object](https://docs.stripe.com/api/v2/iam/activity-logs/object.md?api-version=2026-09-30.preview#v2_activity_log_object-related_object) property for the object related to an activity log entry. It contains the object’s ID and type, such as `bank_account`, `card`, `blockchain_address`, `issuing.card`, `issuing.cardholder`, `issuing.dispute`, or `balance_transfer`. You can use the Stripe API or Dashboard to retrieve details about the related object.

Adds a [request](https://docs.stripe.com/api/v2/iam/activity-logs/object.md?api-version=2026-09-30.preview#v2_activity_log_object-request) property for the API request that instigated the action. This contains the ID of the API request.

## Impact

You can now track and filter a broader set of security, authentication, payout and Issuing actions in Activity Logs. Use the action-specific details, actor, related object and API request ID to investigate changes and provide more context to security information and event management (SIEM) and audit workflows. To learn more, see [Activity Logs](https://docs.stripe.com/activity-logs.md).

## Changes

#### REST API

| Parameters | Change | Resources or endpoints |
| --- | --- | --- |
| `related_object`, `request` | Added | [V2.Iam.ActivityLog](/api/v2/iam/activity-logs/object?api-version=2026-09-30.preview#v2_activity_log_object) |
| `account_security`, `authentication`, `scim`, `sso`, `user_profile` | Added | [V2.Iam.ActivityLog.details](/api/v2/iam/activity-logs/object?api-version=2026-09-30.preview#v2_activity_log_object-details) |

| Values | Change | Enums |
| --- | --- | --- |
| `stripe_action` | Added | [V2.Iam.ActivityLog.actor.type](/api/v2/iam/activity-logs/object?api-version=2026-09-30.preview#v2_activity_log_object-actor-type) |
| `account_security`, `authentication`, `issuing`, `payout`, `scim`, `sso`, `user_profile` | Added | [V2.Iam.ActivityLog.details.type](/api/v2/iam/activity-logs/object?api-version=2026-09-30.preview#v2_activity_log_object-details-type), [V2.Iam.ActivityLog#list.action_groups](/api/v2/iam/activity-logs/list?api-version=2026-09-30.preview#v2_list_activity_logs-action_groups) |
| `anomaly_detection_settings_updated`, `issuing_activated`, `issuing_balance_transfer_created`, `issuing_card_created`, `issuing_card_sensitive_details_viewed`, `issuing_card_updated`, `issuing_cardholder_created`, `issuing_cardholder_updated`, `issuing_dispute_created`, `issuing_dispute_submitted`, `issuing_dispute_updated`, `manual_payouts_disabled`, `manual_payouts_enabled`, `payout_destination_added`, `payout_destination_removed`, `payout_destination_updated`, `payout_schedule_edits_disabled`, `payout_schedule_edits_enabled`, `scim_group_deleted`, `scim_group_member_added`, `scim_group_member_removed`, `scim_group_roles_updated`, `scim_group_updated`, `sso_domain_verified`, `sso_settings_created`, `sso_settings_deleted`, `sso_settings_updated`, `two_step_authentication_mandate_disabled`, `two_step_authentication_mandate_enabled`, `user_auth_challenge_failed`, `user_email_changed`, `user_email_verified`, `user_express_phone_number_changed`, `user_google_account_connected`, `user_google_account_disconnected`, `user_passkey_added`, `user_passkey_removed`, `user_passkey_updated`, `user_passkey_upgraded`, `user_password_changed`, `user_password_initialized`, `user_password_reset_failed`, `user_password_reset_requested`, `user_password_reset_succeeded`, `user_two_step_authentication_backup_code_used`, `user_two_step_authentication_method_added`, `user_two_step_authentication_method_removed`, `user_two_step_authentication_method_reset`, `user_two_step_authentication_method_updated`, `user_two_step_authentication_reset_requested` | Added | [V2.Iam.ActivityLog.type](/api/v2/iam/activity-logs/object?api-version=2026-09-30.preview#v2_activity_log_object-type), [V2.Iam.ActivityLog#list.actions](/api/v2/iam/activity-logs/list?api-version=2026-09-30.preview#v2_list_activity_logs-actions) |

#### Ruby

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `related_object`, `request` | Added | [V2::Iam::ActivityLog](/api/v2/iam/activity-logs/object?api-version=2026-09-30.preview#v2_activity_log_object) |
| `account_security`, `authentication`, `scim`, `sso`, `user_profile` | Added | [V2::Iam::ActivityLog::Detail](/api/v2/iam/activity-logs/object?api-version=2026-09-30.preview#v2_activity_log_object-details) |

#### Python

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `related_object`, `request` | Added | [V2.Iam.ActivityLog](/api/v2/iam/activity-logs/object?api-version=2026-09-30.preview#v2_activity_log_object) |
| `account_security`, `authentication`, `scim`, `sso`, `user_profile` | Added | [V2.Iam.ActivityLog.Detail](/api/v2/iam/activity-logs/object?api-version=2026-09-30.preview#v2_activity_log_object-details) |

| Values | Change | Enums |
| --- | --- | --- |
| `stripe_action` | Added | [V2.Iam.ActivityLog.Actor.type](/api/v2/iam/activity-logs/object?api-version=2026-09-30.preview#v2_activity_log_object-actor-type) |
| `account_security`, `authentication`, `issuing`, `payout`, `scim`, `sso`, `user_profile` | Added | [V2.Iam.ActivityLog.Detail.type](/api/v2/iam/activity-logs/object?api-version=2026-09-30.preview#v2_activity_log_object-details-type), [v2.iam.ActivityLogListParams.action_groups](/api/v2/iam/activity-logs/list?api-version=2026-09-30.preview#v2_list_activity_logs-action_groups) |
| `anomaly_detection_settings_updated`, `issuing_activated`, `issuing_balance_transfer_created`, `issuing_card_created`, `issuing_card_sensitive_details_viewed`, `issuing_card_updated`, `issuing_cardholder_created`, `issuing_cardholder_updated`, `issuing_dispute_created`, `issuing_dispute_submitted`, `issuing_dispute_updated`, `manual_payouts_disabled`, `manual_payouts_enabled`, `payout_destination_added`, `payout_destination_removed`, `payout_destination_updated`, `payout_schedule_edits_disabled`, `payout_schedule_edits_enabled`, `scim_group_deleted`, `scim_group_member_added`, `scim_group_member_removed`, `scim_group_roles_updated`, `scim_group_updated`, `sso_domain_verified`, `sso_settings_created`, `sso_settings_deleted`, `sso_settings_updated`, `two_step_authentication_mandate_disabled`, `two_step_authentication_mandate_enabled`, `user_auth_challenge_failed`, `user_email_changed`, `user_email_verified`, `user_express_phone_number_changed`, `user_google_account_connected`, `user_google_account_disconnected`, `user_passkey_added`, `user_passkey_removed`, `user_passkey_updated`, `user_passkey_upgraded`, `user_password_changed`, `user_password_initialized`, `user_password_reset_failed`, `user_password_reset_requested`, `user_password_reset_succeeded`, `user_two_step_authentication_backup_code_used`, `user_two_step_authentication_method_added`, `user_two_step_authentication_method_removed`, `user_two_step_authentication_method_reset`, `user_two_step_authentication_method_updated`, `user_two_step_authentication_reset_requested` | Added | [V2.Iam.ActivityLog.type](/api/v2/iam/activity-logs/object?api-version=2026-09-30.preview#v2_activity_log_object-type), [v2.iam.ActivityLogListParams.actions](/api/v2/iam/activity-logs/list?api-version=2026-09-30.preview#v2_list_activity_logs-actions) |

#### PHP

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `related_object`, `request` | Added | [V2.Iam.ActivityLog](/api/v2/iam/activity-logs/object?api-version=2026-09-30.preview#v2_activity_log_object) |
| `account_security`, `authentication`, `scim`, `sso`, `user_profile` | Added | [V2.Iam.ActivityLog.details](/api/v2/iam/activity-logs/object?api-version=2026-09-30.preview#v2_activity_log_object-details) |

| Values | Change | Enums |
| --- | --- | --- |
| `stripe_action` | Added | [V2.Iam.ActivityLog.actor.type](/api/v2/iam/activity-logs/object?api-version=2026-09-30.preview#v2_activity_log_object-actor-type) |
| `account_security`, `authentication`, `issuing`, `payout`, `scim`, `sso`, `user_profile` | Added | [V2.Iam.ActivityLog.details.type](/api/v2/iam/activity-logs/object?api-version=2026-09-30.preview#v2_activity_log_object-details-type) |
| `anomaly_detection_settings_updated`, `issuing_activated`, `issuing_balance_transfer_created`, `issuing_card_created`, `issuing_card_sensitive_details_viewed`, `issuing_card_updated`, `issuing_cardholder_created`, `issuing_cardholder_updated`, `issuing_dispute_created`, `issuing_dispute_submitted`, `issuing_dispute_updated`, `manual_payouts_disabled`, `manual_payouts_enabled`, `payout_destination_added`, `payout_destination_removed`, `payout_destination_updated`, `payout_schedule_edits_disabled`, `payout_schedule_edits_enabled`, `scim_group_deleted`, `scim_group_member_added`, `scim_group_member_removed`, `scim_group_roles_updated`, `scim_group_updated`, `sso_domain_verified`, `sso_settings_created`, `sso_settings_deleted`, `sso_settings_updated`, `two_step_authentication_mandate_disabled`, `two_step_authentication_mandate_enabled`, `user_auth_challenge_failed`, `user_email_changed`, `user_email_verified`, `user_express_phone_number_changed`, `user_google_account_connected`, `user_google_account_disconnected`, `user_passkey_added`, `user_passkey_removed`, `user_passkey_updated`, `user_passkey_upgraded`, `user_password_changed`, `user_password_initialized`, `user_password_reset_failed`, `user_password_reset_requested`, `user_password_reset_succeeded`, `user_two_step_authentication_backup_code_used`, `user_two_step_authentication_method_added`, `user_two_step_authentication_method_removed`, `user_two_step_authentication_method_reset`, `user_two_step_authentication_method_updated`, `user_two_step_authentication_reset_requested` | Added | [V2.Iam.ActivityLog.type](/api/v2/iam/activity-logs/object?api-version=2026-09-30.preview#v2_activity_log_object-type) |

#### Java

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `relatedObject`, `request` | Added | [v2.iam.ActivityLog](/api/v2/iam/activity-logs/object?api-version=2026-09-30.preview#v2_activity_log_object) |
| `accountSecurity`, `authentication`, `scim`, `sso`, `userProfile` | Added | [v2.iam.ActivityLog.details](/api/v2/iam/activity-logs/object?api-version=2026-09-30.preview#v2_activity_log_object-details) |

| Values | Change | Enums |
| --- | --- | --- |
| `account_security`, `authentication`, `issuing`, `payout`, `scim`, `sso`, `user_profile` | Added | [v2.iam.ActivityLogListParams.actionGroups](/api/v2/iam/activity-logs/list?api-version=2026-09-30.preview#v2_list_activity_logs-actionGroups) |
| `anomaly_detection_settings_updated`, `issuing_activated`, `issuing_balance_transfer_created`, `issuing_card_created`, `issuing_card_sensitive_details_viewed`, `issuing_card_updated`, `issuing_cardholder_created`, `issuing_cardholder_updated`, `issuing_dispute_created`, `issuing_dispute_submitted`, `issuing_dispute_updated`, `manual_payouts_disabled`, `manual_payouts_enabled`, `payout_destination_added`, `payout_destination_removed`, `payout_destination_updated`, `payout_schedule_edits_disabled`, `payout_schedule_edits_enabled`, `scim_group_deleted`, `scim_group_member_added`, `scim_group_member_removed`, `scim_group_roles_updated`, `scim_group_updated`, `sso_domain_verified`, `sso_settings_created`, `sso_settings_deleted`, `sso_settings_updated`, `two_step_authentication_mandate_disabled`, `two_step_authentication_mandate_enabled`, `user_auth_challenge_failed`, `user_email_changed`, `user_email_verified`, `user_express_phone_number_changed`, `user_google_account_connected`, `user_google_account_disconnected`, `user_passkey_added`, `user_passkey_removed`, `user_passkey_updated`, `user_passkey_upgraded`, `user_password_changed`, `user_password_initialized`, `user_password_reset_failed`, `user_password_reset_requested`, `user_password_reset_succeeded`, `user_two_step_authentication_backup_code_used`, `user_two_step_authentication_method_added`, `user_two_step_authentication_method_removed`, `user_two_step_authentication_method_reset`, `user_two_step_authentication_method_updated`, `user_two_step_authentication_reset_requested` | Added | [v2.iam.ActivityLogListParams.actions](/api/v2/iam/activity-logs/list?api-version=2026-09-30.preview#v2_list_activity_logs-actions) |

#### Node.js

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `related_object`, `request` | Added | [V2.Iam.ActivityLog](/api/v2/iam/activity-logs/object?api-version=2026-09-30.preview#v2_activity_log_object) |
| `account_security`, `authentication`, `scim`, `sso`, `user_profile` | Added | [V2.Iam.ActivityLog.details](/api/v2/iam/activity-logs/object?api-version=2026-09-30.preview#v2_activity_log_object-details) |

| Values | Change | Enums |
| --- | --- | --- |
| `stripe_action` | Added | [V2.Iam.ActivityLog.actor.type](/api/v2/iam/activity-logs/object?api-version=2026-09-30.preview#v2_activity_log_object-actor-type) |
| `account_security`, `authentication`, `issuing`, `payout`, `scim`, `sso`, `user_profile` | Added | [V2.Iam.ActivityLog.details.type](/api/v2/iam/activity-logs/object?api-version=2026-09-30.preview#v2_activity_log_object-details-type), [V2.Iam.ActivityLogListParams.action_groups](/api/v2/iam/activity-logs/list?api-version=2026-09-30.preview#v2_list_activity_logs-action_groups) |
| `anomaly_detection_settings_updated`, `issuing_activated`, `issuing_balance_transfer_created`, `issuing_card_created`, `issuing_card_sensitive_details_viewed`, `issuing_card_updated`, `issuing_cardholder_created`, `issuing_cardholder_updated`, `issuing_dispute_created`, `issuing_dispute_submitted`, `issuing_dispute_updated`, `manual_payouts_disabled`, `manual_payouts_enabled`, `payout_destination_added`, `payout_destination_removed`, `payout_destination_updated`, `payout_schedule_edits_disabled`, `payout_schedule_edits_enabled`, `scim_group_deleted`, `scim_group_member_added`, `scim_group_member_removed`, `scim_group_roles_updated`, `scim_group_updated`, `sso_domain_verified`, `sso_settings_created`, `sso_settings_deleted`, `sso_settings_updated`, `two_step_authentication_mandate_disabled`, `two_step_authentication_mandate_enabled`, `user_auth_challenge_failed`, `user_email_changed`, `user_email_verified`, `user_express_phone_number_changed`, `user_google_account_connected`, `user_google_account_disconnected`, `user_passkey_added`, `user_passkey_removed`, `user_passkey_updated`, `user_passkey_upgraded`, `user_password_changed`, `user_password_initialized`, `user_password_reset_failed`, `user_password_reset_requested`, `user_password_reset_succeeded`, `user_two_step_authentication_backup_code_used`, `user_two_step_authentication_method_added`, `user_two_step_authentication_method_removed`, `user_two_step_authentication_method_reset`, `user_two_step_authentication_method_updated`, `user_two_step_authentication_reset_requested` | Added | [V2.Iam.ActivityLog.type](/api/v2/iam/activity-logs/object?api-version=2026-09-30.preview#v2_activity_log_object-type), [V2.Iam.ActivityLogListParams.actions](/api/v2/iam/activity-logs/list?api-version=2026-09-30.preview#v2_list_activity_logs-actions) |

#### Go

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `RelatedObject`, `Request` | Added | [V2IamActivityLog](/api/v2/iam/activity-logs/object?api-version=2026-09-30.preview#v2_activity_log_object) |
| `AccountSecurity`, `Authentication`, `Scim`, `Sso`, `UserProfile` | Added | [V2IamActivityLogDetails](/api/v2/iam/activity-logs/object?api-version=2026-09-30.preview#v2_activity_log_object-details) |

| Values | Change | Enums |
| --- | --- | --- |
| `stripe_action` | Added | [V2IamActivityLogActor.Type](/api/v2/iam/activity-logs/object?api-version=2026-09-30.preview#v2_activity_log_object-actor-Type) |
| `account_security`, `authentication`, `issuing`, `payout`, `scim`, `sso`, `user_profile` | Added | [V2IamActivityLogDetails.Type](/api/v2/iam/activity-logs/object?api-version=2026-09-30.preview#v2_activity_log_object-details-Type) |
| `anomaly_detection_settings_updated`, `issuing_activated`, `issuing_balance_transfer_created`, `issuing_card_created`, `issuing_card_sensitive_details_viewed`, `issuing_card_updated`, `issuing_cardholder_created`, `issuing_cardholder_updated`, `issuing_dispute_created`, `issuing_dispute_submitted`, `issuing_dispute_updated`, `manual_payouts_disabled`, `manual_payouts_enabled`, `payout_destination_added`, `payout_destination_removed`, `payout_destination_updated`, `payout_schedule_edits_disabled`, `payout_schedule_edits_enabled`, `scim_group_deleted`, `scim_group_member_added`, `scim_group_member_removed`, `scim_group_roles_updated`, `scim_group_updated`, `sso_domain_verified`, `sso_settings_created`, `sso_settings_deleted`, `sso_settings_updated`, `two_step_authentication_mandate_disabled`, `two_step_authentication_mandate_enabled`, `user_auth_challenge_failed`, `user_email_changed`, `user_email_verified`, `user_express_phone_number_changed`, `user_google_account_connected`, `user_google_account_disconnected`, `user_passkey_added`, `user_passkey_removed`, `user_passkey_updated`, `user_passkey_upgraded`, `user_password_changed`, `user_password_initialized`, `user_password_reset_failed`, `user_password_reset_requested`, `user_password_reset_succeeded`, `user_two_step_authentication_backup_code_used`, `user_two_step_authentication_method_added`, `user_two_step_authentication_method_removed`, `user_two_step_authentication_method_reset`, `user_two_step_authentication_method_updated`, `user_two_step_authentication_reset_requested` | Added | [V2IamActivityLog.Type](/api/v2/iam/activity-logs/object?api-version=2026-09-30.preview#v2_activity_log_object-Type) |

#### .NET

| Parameters | Change | Resources or methods |
| --- | --- | --- |
| `RelatedObject`, `Request` | Added | [V2.Iam.ActivityLog](/api/v2/iam/activity-logs/object?api-version=2026-09-30.preview#v2_activity_log_object) |
| `AccountSecurity`, `Authentication`, `Scim`, `Sso`, `UserProfile` | Added | [V2.Iam.ActivityLog.Details](/api/v2/iam/activity-logs/object?api-version=2026-09-30.preview#v2_activity_log_object-details) |

## Upgrade

#### REST API

1. [View your current API version](https://docs.stripe.com/workbench/guides.md#view-api-versions) in Workbench.
2. If you use an SDK, upgrade to the corresponding SDK version for this API version.
   - If you don’t use an SDK, update your [API requests](https://docs.stripe.com/api-versions.md#how-versions-are-specified-in-requests) to include `Stripe-Version: 2026-09-30.preview`
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
