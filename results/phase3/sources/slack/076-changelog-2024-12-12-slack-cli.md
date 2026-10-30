---
title: "Release: Slack CLI v2.32.0"
summary: "Version 2.32.0 of the developer tools for the Slack automations platform is here!"
url: "https://docs.slack.dev/changelog/2024/12/12/slack-cli"
type: "changelog"
---

Source: https://docs.slack.dev/changelog/2024/12/12/slack-cli

# Release: Slack CLI v2.32.0

December 12, 2024

Version `2.32.0` of the developer tools for the Slack automations platform is here!

*   We improved detection of [Deno](https://docs.slack.dev/tools/deno-slack-sdk/guides/installing-deno.md) projects and added test coverage to the Deno runtime for a smoother experience.
*   We improved the formatting of output when running `slack env` commands. We also added error messaging to these commands when the app being referenced is not an app created using the Deno Slack SDK.
*   The `slack env remove` command now exits without erroring when there are no environment variables to remove.
*   We enhanced text styling for easier reading.
*   We improved some internal processes that allow us to keep our documentation fresh and up-to-date.
*   We improved the error messaging of our `slack datastore` commands.
*   We updated our documentation and errors displayed when using `slack external-auth` subcommands with Bolt apps.
*   We now raise errors that may impact the validation of selected authentications.
*   We now hide blank `source` errors that may have caused confusion; they have been replaced with more helpful messaging.

**Tags:**

*   [Release](https://docs.slack.dev/changelog/tags/release.md)
*   [Slack CLI](https://docs.slack.dev/changelog/tags/slack-cli.md)
