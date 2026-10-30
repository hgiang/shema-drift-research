---
title: "Release: Slack CLI v3.13.0"
summary: "Version 3.13.0 of the developer tools for the Slack platform has arrived!"
url: "https://docs.slack.dev/changelog/2026/02/19/slack-cli"
type: "changelog"
---

Source: https://docs.slack.dev/changelog/2026/02/19/slack-cli

# Release: Slack CLI v3.13.0

February 19, 2026

Version `3.13.0` of the developer tools for the Slack platform has arrived!

*   When running the `slack create` command with the `agent` argument, a list of agentic apps are now highlighted for selection. If you want to name your app "agent" and not create an agentic app, you can use the `--name` flag instead to explicitly set your app name. Refer to the [`slack create`](https://docs.slack.dev/tools/slack-cli/reference/commands/slack_create.md) command for more details.
*   When running the `slack create` command, the available templates are now shown without requiring an immediate selection when using the `--list` flag. Refer to the [`slack create`](https://docs.slack.dev/tools/slack-cli/reference/commands/slack_create.md) command for more details.
*   The `slack deploy` command now references the latest online documentation, with a suggestion to run a development app using the `slack run` command if a `deploy` hook script doesn't exist. Refer to our [hooks](https://docs.slack.dev/tools/slack-cli/reference/hooks.md#deploy) documentation for more details.
*   We now prompt you to log in if no prior authentications are detected when running any command that requires credentials, rather than exiting with an error.

**Tags:**

*   [Release](https://docs.slack.dev/changelog/tags/release.md)
*   [Slack CLI](https://docs.slack.dev/changelog/tags/slack-cli.md)
