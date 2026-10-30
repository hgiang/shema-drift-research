---
title: "Release: Slack CLI v2.5.0"
summary: "Version 2.5.0 of the developer tools for the Slack automations platform is hot off the press!"
url: "https://docs.slack.dev/changelog/2023/06/29/slack-cli"
type: "changelog"
---

Source: https://docs.slack.dev/changelog/2023/06/29/slack-cli

# Release: Slack CLI v2.5.0

June 29, 2023

Version `2.5.0` of the developer tools for the Slack automations platform is hot off the press!

*   We've added a confirmation message if you decide not to delete an app when using the `slack app delete` command.
*   We added a `--hide-triggers` flag to the `slack run` and `slack deploy` commands to prevent retrieving and displaying application triggers.
*   We added a warning to listed trigger info that Slack Connect channels do not support event triggers.
*   We added app collaborators to listed trigger info.
*   We added support to limit paginated results with the `trigger list --limit <n>` command.
*   We added a prompt for whether you would like to include/exclude app collaborators into the named entities list if you set your trigger's ACL to `named_entities`. The `include-app-collaborators` flag will allow you to skip this prompt.
*   We updated the `slack activity` command to support datastore event and error logs. For more information, refer to [logging](https://docs.slack.dev/tools/deno-slack-sdk/guides/logging-function-and-app-behavior.md).
*   When the `--token` flag is set, background checks for updates will now be automatically disabled.
*   We added support to fall back to a `curl` install of `deno` if `deno upgrade` should fail.
*   The `slack logout` command now accepts the `--workspace` flag.
*   We removed the `--show-triggers` flag from the `slack run` command, as the command now displays all of your app's triggers and their types.

**Tags:**

*   [Release](https://docs.slack.dev/changelog/tags/release.md)
*   [Slack CLI](https://docs.slack.dev/changelog/tags/slack-cli.md)
