---
title: "Release: Slack CLI v2.4.0"
summary: "Version 2.4.0 of the developer tools for the Slack automations platform is now available!"
url: "https://docs.slack.dev/changelog/2023/06/15/slack-cli"
type: "changelog"
---

Source: https://docs.slack.dev/changelog/2023/06/15/slack-cli

# Release: Slack CLI v2.4.0

June 15, 2023

Version `2.4.0` of the developer tools for the Slack automations platform is now available!

*   We updated the Linux/macOS installation script to support a CLI version param, `-v`.
*   We added a `-d` flag to bypass Deno installation in the Linux/macOS installation script.
*   We updated the Windows installation script to include Alias, Version, SkipDeno, and SkipGit flags.
*   We now suggest Windows users open a new terminal after installation to add the Slack CLI to the user's environment PATH.
*   We bumped minimum required Deno version to `1.31.1`.
*   We replaced the `workspace` command with a new [`app`](https://docs.slack.dev/tools/slack-cli/reference/commands/slack_app.md) command.
*   We made the `config-dir` global flag visible.
*   We deprecated auth login's `auth` flag in favor of [`token`](https://docs.slack.dev/tools/slack-cli/reference/commands/slack_auth_login.md).
*   We updated `app list` command to display installation status.

**Tags:**

*   [Release](https://docs.slack.dev/changelog/tags/release.md)
*   [Slack CLI](https://docs.slack.dev/changelog/tags/slack-cli.md)
