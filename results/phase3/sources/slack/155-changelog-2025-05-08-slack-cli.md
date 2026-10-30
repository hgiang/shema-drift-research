---
title: "Release: Slack CLI v3.1.0"
summary: "Version 3.1.0 of the developer tools for the Slack platform has sprouted!"
url: "https://docs.slack.dev/changelog/2025/05/08/slack-cli"
type: "changelog"
---

Source: https://docs.slack.dev/changelog/2025/05/08/slack-cli

# Release: Slack CLI v3.1.0

May 8, 2025

Version `3.1.0` of the developer tools for the Slack platform has sprouted!

*   We've updated the `slack app link` command to work with apps that have a `local` manifest source.
*   We've updated the `slack feedback` command to display a prompt for Slack CLI feedback: now you can ask questions, submit issues, or suggest features for the Slack CLI through GitHub Issues.
*   Related to the above update, the `slack feedback --name platform-improvements` command has been replaced with `slack feedback --name slack-platform`. You can continue to use the `--name platform-improvements` flag until the next major version release.
*   We updated the `slack feedback` command error message to account for a missing `--name <id>` flag and to clarify that the name is specified as a flag. You should now see: _Please provide a `--name` flag or remove the `--no-prompt` flag_.
*   We fixed a bug with a rare edge case that caused the Slack CLI to hang without exiting the process. Now, the Slack CLI will exit with the correct error code and allow sub-processes to clean up.

**Tags:**

*   [Release](https://docs.slack.dev/changelog/tags/release.md)
*   [Slack CLI](https://docs.slack.dev/changelog/tags/slack-cli.md)
