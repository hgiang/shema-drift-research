---
title: "Release: Slack CLI v2.6.0"
summary: "Version 2.6.0 of the developer tools for the Slack automations platform has arrived!"
url: "https://docs.slack.dev/changelog/2023/07/27/slack-cli"
type: "changelog"
---

Source: https://docs.slack.dev/changelog/2023/07/27/slack-cli

# Release: Slack CLI v2.6.0

July 27, 2023

Version `2.6.0` of the developer tools for the Slack automations platform has arrived!

*   The `.github` directory will no longer be included in new projects created from one of our [sample apps](https://github.com/slack-samples).
*   The `slack app list` command now returns `Status: Installed` instead of `Status: Unknown` for an installed app.
*   When using the CLI in a non-interactive environment, such as in a CI pipeline, selection prompts will error and suggest a flag alternative to use instead of hanging indefinitely.
*   Trigger generation prompts will be automatically skipped when using `slack run` or `slack deploy` in a non-interactive environment, regardless of how many triggers might exist.
*   We've clarified admin approval requirements when installing to a workspace that has [Admin-Approved Apps](https://docs.slack.dev/tools/deno-slack-sdk/guides/controlling-permissions-for-admins.md) enabled.
*   Socket connections are now gracefully closed when ending a `slack run` session.
*   Improved typeahead suggestions for the `type` field of `functions` and `datastores` were made in the Deno Slack SDK.

**Tags:**

*   [Release](https://docs.slack.dev/changelog/tags/release.md)
*   [Slack CLI](https://docs.slack.dev/changelog/tags/slack-cli.md)
