---
title: "Release: Slack CLI v2.18.0"
summary: "Version 2.18.0 of the developer tools for the Slack automations platform has joined the party!"
url: "https://docs.slack.dev/changelog/2024/02/22/slack-cli"
type: "changelog"
---

Source: https://docs.slack.dev/changelog/2024/02/22/slack-cli

# Release: Slack CLI v2.18.0

February 22, 2024

Version 2.18.0 of the developer tools for the Slack automations platform has joined the party!

*   The minimum supported PowerShell version as of this release is `v6.0`. If you attempt to use an older version of PowerShell, you may encounter errors reading the Slack Configuration file (`slack.json`) or running the `get hooks` hook.
*   We've added the ability to put, get, and delete items in bulk in a datastore. Refer to [Create or replace items with `put` and `bulkPut`](https://docs.slack.dev/tools/deno-slack-sdk/guides/adding-items-to-a-datastore.md), [Retrieve items with `get` and `bulkGet`](https://docs.slack.dev/tools/deno-slack-sdk/guides/retrieving-items-from-a-datastore.md), and [Delete items with `delete` and `bulkDelete`](https://docs.slack.dev/tools/deno-slack-sdk/guides/deleting-items-from-a-datastore.md), respectively.
*   We've added the ability to import to and export from datastores. Refer to [Datastore commands](https://docs.slack.dev/tools/slack-cli/reference/commands/slack_datastore.md) for more details.
*   We've added a warning when creating an app from a sample app when the sample app may not have come from a trusted source.
*   You can disable this warning temporarily by running the `slack create` command with the `--force` flag.
*   You can disable this warning permanently by either selecting _don't ask again_ when prompted, or by setting the `trust_unknown_sources` property in your `config.json` file.
*   We've fixed an issue so can now use **CTRL-C** to unhide your cursor when a spinner displays after running `slack deploy`.
*   We've enhanced some error messages and we've improved highlighting matching for help commands.

**Tags:**

*   [Release](https://docs.slack.dev/changelog/tags/release.md)
*   [Slack CLI](https://docs.slack.dev/changelog/tags/slack-cli.md)
