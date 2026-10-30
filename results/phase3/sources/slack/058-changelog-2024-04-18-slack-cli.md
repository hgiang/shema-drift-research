---
title: "Release: Slack CLI v2.22.0"
summary: "Version 2.22.0 of the developer tools for the Slack automations platform is here!"
url: "https://docs.slack.dev/changelog/2024/04/18/slack-cli"
type: "changelog"
---

Source: https://docs.slack.dev/changelog/2024/04/18/slack-cli

# Release: Slack CLI v2.22.0

April 18, 2024

Version `2.22.0` of the developer tools for the Slack automations platform is here!

*   We fixed a bug to prevent project paths including spaces from being separated into multiple arguments when deploying an app.
*   We now cease defaulting to the deno runtime, and log unsupported runtimes.
*   We fixed a bug that was causing a `team_access_not_granted` error when redeploying an app.
*   We fixed a bug to handle an empty `outgoing_domains` attribute within an app's manifest.
*   We fixed a bug to remove extra spaces from error messages when creating a new project using `slack create`.

**Tags:**

*   [Release](https://docs.slack.dev/changelog/tags/release.md)
*   [Slack CLI](https://docs.slack.dev/changelog/tags/slack-cli.md)
