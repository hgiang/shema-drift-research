---
title: "Release: Slack CLI v2.2.0"
summary: "Version 2.2.0 of the developer tools for our beta Slack platform has landed!"
url: "https://docs.slack.dev/changelog/2023/05/04/slack-cli"
type: "changelog"
---

Source: https://docs.slack.dev/changelog/2023/05/04/slack-cli

# Release: Slack CLI v2.2.0

May 4, 2023

Version `2.2.0` of the developer tools for our beta Slack platform has landed!

*   The `trigger info` command now also shows who has permissions to run the trigger.
*   We added the `--no-color` flag, which removes all ANSI sequences for color as well as emojis, giving you plain text output from the CLI that's perfect for piping to a text file.
*   The `datastore query` command now supports a `cursor` argument to help you paginate your results the way you want.
*   Trigger operations will now let you know when an invalid trigger file is being ignored.
*   We improved error reporting and some help text.

**Tags:**

*   [Release](https://docs.slack.dev/changelog/tags/release.md)
*   [Slack CLI](https://docs.slack.dev/changelog/tags/slack-cli.md)
