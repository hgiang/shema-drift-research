---
title: "Release: Multiple Node Slack SDK package updates"
summary: "Our collection of Node Slack SDK packages have received new major versions."
url: "https://docs.slack.dev/changelog/2026/07/14/node-slack-sdk-release"
type: "changelog"
---

Source: https://docs.slack.dev/changelog/2026/07/14/node-slack-sdk-release

# Release: Multiple Node Slack SDK package updates

July 14, 2026

Our collection of Node Slack SDK packages have received new major versions.

All packages now require **Node.js 20 or later**. This is the only breaking change for the following packages:

*   The `cli-hooks` package has been updated to v2.
*   The `cli-test` package has been updated to v4.
*   The `logger` package has been updated to v5.
*   The `oauth` package has been updated to v4.
*   The `types` package has been updated to v3.

Three packages have more substantial breaking changes:

*   The `socket-mode` package has been updated to v3. See the guide on [migrating @slack/socket-mode from v2 to v3](https://docs.slack.dev/tools/node-slack-sdk/migration/socket-mode/migrating-socket-mode-package-to-v3.md) for handling breaking changes.
*   The `web-api` package has been updated to v8. See the guide on [migrating @slack/web-api from v7 to v8](https://docs.slack.dev/tools/node-slack-sdk/migration/web-api/migrating-web-api-package-to-v8.md) for handling breaking changes.
*   The `webhook` package has been updated to v8. See the guide on [migrating @slack/webhook from v7 to v8](https://docs.slack.dev/tools/node-slack-sdk/migration/webhook/migrating-webhook-package-to-v8.md) for handling breaking changes.

Most of the changes in those batch of updates fall under the theme of HTTP transport improvements, such as migrating from axios to the native Fetch API.

**Tags:**

*   [Release](https://docs.slack.dev/changelog/tags/release.md)
*   [Node Slack SDK](https://docs.slack.dev/changelog/tags/node-slack-sdk.md)
