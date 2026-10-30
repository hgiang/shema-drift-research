---
title: "Release: Slack CLI v3.2.0"
summary: "Version 3.2.0 of the developer tools for the Slack platform is here!"
url: "https://docs.slack.dev/changelog/2025/05/22/slack-cli"
type: "changelog"
---

Source: https://docs.slack.dev/changelog/2025/05/22/slack-cli

# Release: Slack CLI v3.2.0

May 22, 2025

Version `3.2.0` of the developer tools for the Slack platform is here!

*   We now display the manifest source as human-friendly output: `project (local)` and `app settings (remote)`. You'll see these changes in the `slack create`, `slack init`, and `slack app link <id>` commands, for example.
*   The link between your project code and the configurations within app settings can now be accessed by running the `slack app settings` command. Bolt developers with a remote manifest source managed within app settings may find this useful for discovering new features or making updates.
*   We fixed a bug: The example `slack app link` and `slack app list` commands shown when running the `slack app --help` command now use the entire command in order to prevent potential aliasing errors.
*   We fixed a bug to improve the console output to handle string values for versions.

**Tags:**

*   [Release](https://docs.slack.dev/changelog/tags/release.md)
*   [Slack CLI](https://docs.slack.dev/changelog/tags/slack-cli.md)
