---
title: "Release: Slack CLI v2.13.0"
summary: "Version 2.13.0 of the developer tools for the Slack automations platform has landed!"
url: "https://docs.slack.dev/changelog/2023/11/16/slack-cli"
type: "changelog"
---

Source: https://docs.slack.dev/changelog/2023/11/16/slack-cli

# Release: Slack CLI v2.13.0

November 16, 2023

Version `2.13.0` of the developer tools for the Slack automations platform has landed!

*   We've added an `--all-org-workspace-grants` flag to the `app list` command so you can display all grants instead of only the first three.
*   We've combined `workspace` and `org` language into `team`; as such, we have added a `--team` flag and deprecated the `--workspace` flag. Note that this will not affect the usage of workspace or org when it is necessary to distinguish between them; for example, with the `hermes auth list` and `trigger access` commands.
*   We removed the redirect to the `delete` command when running the `uninstall` command, so you may now only uninstall an app rather than deleting the app entirely along with all of its data.
*   We've updated the CLI installer to align the Deno runtime version with the current version supported by the Slack platform.
*   We've updated all `deno-reverse-string` sample app references to use `deno-started-template` instead.
*   We fixed a bug to create a `usr/local/bin` directory if it is missing when installing the CLI.
*   We updated some confusing language related to breaking changes.
*   We fixed a bug that caused an error when any property setting flags were provided along with the `--trigger-def` flag.
*   We fixed a bug where descriptions and selected template URLs might be mismatched from the displayed list of samples.

**Tags:**

*   [Release](https://docs.slack.dev/changelog/tags/release.md)
*   [Slack CLI](https://docs.slack.dev/changelog/tags/slack-cli.md)
