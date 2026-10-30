---
title: "Release: Slack CLI v3.5.0"
summary: "Version 3.5.0 of the developer tools for the Slack platform is here!"
url: "https://docs.slack.dev/changelog/2025/07/03/slack-cli"
type: "changelog"
---

Source: https://docs.slack.dev/changelog/2025/07/03/slack-cli

# Release: Slack CLI v3.5.0

July 3, 2025

Version `3.5.0` of the developer tools for the Slack platform is here!

*   The Bolt for JavaScript and Bolt for Python sample apps referenced in the documentation are now included in prompts of the `slack samples` command, and can be filtered using the `--language` flag.
*   Samples can now be created with a provided app name using the `slack samples` command with the provided app name.
*   We fixed a bug where the `slack run` command exited with an error if activity logs failed to stream. Now, retries are attempted for those missed logs.

**Tags:**

*   [Release](https://docs.slack.dev/changelog/tags/release.md)
*   [Slack CLI](https://docs.slack.dev/changelog/tags/slack-cli.md)
