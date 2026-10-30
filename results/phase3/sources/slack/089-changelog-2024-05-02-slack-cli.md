---
title: "Release: Slack CLI v2.23.0"
summary: "Version 2.23.0 of the developer tools for the Slack automations platform is here!"
url: "https://docs.slack.dev/changelog/2024/05/02/slack-cli"
type: "changelog"
---

Source: https://docs.slack.dev/changelog/2024/05/02/slack-cli

# Release: Slack CLI v2.23.0

May 2, 2024

Version `2.23.0` of the developer tools for the Slack automations platform is here!

*   We now prompt you to log in again if your auth is expired or invalid. This applies to all commands where you need to select an app.
*   We now automatically set the `SLACK_API_URL` environment variable to the preferred API host used in the auth process.
*   We fixed some bugs to reduce the chances of returning errors when checking the operating system, project configs, project tooling, and project dependencies when running the `slack doctor` command.
*   We now display a more informative message when you attempt to delete or uninstall an app from a project that has no apps.

**Tags:**

*   [Release](https://docs.slack.dev/changelog/tags/release.md)
*   [Slack CLI](https://docs.slack.dev/changelog/tags/slack-cli.md)
