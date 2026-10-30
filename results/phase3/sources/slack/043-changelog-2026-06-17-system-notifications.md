---
title: "System notifications now delivered by \"Slack\" instead of Slackbot"
summary: "'Slack"
url: "https://docs.slack.dev/changelog/2026/06/17/system-notifications"
type: "changelog"
---

Source: https://docs.slack.dev/changelog/2026/06/17/system-notifications

# System notifications now delivered by "Slack" instead of Slackbot

June 17, 2026

Slack system notifications (such as channel membership changes, User Group updates, Slack Connect alerts, and retention policy notices) are now delivered from the "Slack" system user (`USLACK`) instead of Slackbot.

## What's changing {#whats-changing}

Previously, system-generated notifications were sent as direct messages from Slackbot. Now that Slackbot is the home for AI conversations in Slack, we want to separate notification delivery for clarity. These notifications are now sent from the new "Slack" system user, `USLACK`. Existing historical Slackbot system notifications will be backfilled and moved to the new "Slack" DM as well.

Note: User-authored messages sent directly to Slackbot (e.g., messages you typed into the Slackbot conversation) are not affected by this change.

## What this means for developers {#what-this-means-for-developers}

If your app or integration:

*   Filters incoming messages or events by Slackbot's user ID,
*   Checks the username field for "Slackbot" to identify system notifications, or
*   Uses the `chat.postMessage` API method or related API methods and expects system notifications to route through Slackbot

then you should update your integration to handle the new "Slack" system user (`USLACK`) instead.

No action required if your integration does not reference Slackbot's user ID or username in its logic.

**Tags:**

*   [Announcement](https://docs.slack.dev/changelog/tags/announcement.md)
*   [Breaking change](https://docs.slack.dev/changelog/tags/breaking-change.md)
