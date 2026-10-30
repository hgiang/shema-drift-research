---
title: "Release: Slack CLI v2.7.0"
summary: "Version 2.7.0 of the developer tools for the Slack automations platform has arrived!"
url: "https://docs.slack.dev/changelog/2023/08/10/slack-cli"
type: "changelog"
---

Source: https://docs.slack.dev/changelog/2023/08/10/slack-cli

# Release: Slack CLI v2.7.0

August 10, 2023

Version `2.7.0` of the developer tools for the Slack automations platform has arrived!

*   We've added a [`slack trigger list --type=<string>`](https://docs.slack.dev/tools/slack-cli/reference/commands/slack_trigger_list.md) flag to only list triggers of a specific type: For example, `slack trigger list --type=shortcut`. We've also supported flag values for `--type=<string>` are `all`, `shortcut`, `event`, `webhook`, `scheduled`, and `external`.
*   We've added flags to provide values for many interactive prompts. Learn more about the flags available by adding `--help` to any command. For example, `slack external-auth add-secret --provider github --secret my-secret-value`.
*   We've updated the `slack app list` command to improve displaying apps you are not authenticated to access. For example, local apps now display a `(local)` label and install status is now shown as `Status: Unknown`.
*   We removed an incorrect timestamp found in the Slack debug log file.
*   The Deno Slack SDK v2.2.0 now displays an error in your editor when you accidentally register duplicate primary keys for `workflow`, `function`, `datastore`, `customType`, `event` or `provider`. This helps prevent unexpected behavior at runtime.

**Tags:**

*   [Release](https://docs.slack.dev/changelog/tags/release.md)
*   [Slack CLI](https://docs.slack.dev/changelog/tags/slack-cli.md)
