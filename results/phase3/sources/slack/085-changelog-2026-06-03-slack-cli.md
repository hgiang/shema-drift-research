---
title: "Release: Slack CLI v4.2.0"
summary: "Version 4.2.0 of the Slack CLI has arrived!"
url: "https://docs.slack.dev/changelog/2026/06/03/slack-cli"
type: "changelog"
---

Source: https://docs.slack.dev/changelog/2026/06/03/slack-cli

# Release: Slack CLI v4.2.0

June 3, 2026

Version `4.2.0` of the Slack CLI has arrived!

*   The `slack api` command can now send unauthenticated requests when no token is available or when `--no-auth` is specified.
*   The `slack api` command no longer triggers a background update check when invoked with arguments (e.g., `slack api chat.postMessage`).
*   Any `Y/N` select prompts now display as vertical selection, similar to the `slack create` command.
*   We've disabled upgrade notifications for the `slack manifest` and `slack manifest info` command. The command returns JSON that may be used for scripting, and the notifications interfere with parsing the response output.

**Tags:**

*   [Release](https://docs.slack.dev/changelog/tags/release.md)
*   [Slack CLI](https://docs.slack.dev/changelog/tags/slack-cli.md)
