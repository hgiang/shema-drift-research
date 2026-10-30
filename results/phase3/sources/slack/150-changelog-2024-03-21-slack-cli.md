---
title: "Release: Slack CLI v2.20.1 & v2.20.1"
summary: "Versions 2.20.0 and 2.20.1 of the developer tools for the Slack automations platform have landed!"
url: "https://docs.slack.dev/changelog/2024/03/21/slack-cli"
type: "changelog"
---

Source: https://docs.slack.dev/changelog/2024/03/21/slack-cli

# Release: Slack CLI v2.20.1 & v2.20.1

March 21, 2024

Versions 2.20.0 and 2.20.1 of the developer tools for the Slack automations platform have landed!

*   We've added a new feature for counting datastore items. Refer to [Counting items in a datastore](https://docs.slack.dev/tools/deno-slack-sdk/guides/using-datastores.md#count) for more details.
*   We added a new feature to query named datastores from a flag instead of an expression. For example, instead of:

`$ slack datastore get '{"datastore": "todos", "id": "42"}'`

use:

`$ slack datastore get --datastore tasks '{"id": "42"}'`

*   We now include a remediation message for the `not_authed` error that explains how to log in and authorize the Slack CLI.
*   Users can now request app approval at the workspace level in an Enterprise organization.
*   We now include the error code in event payloads to logstash.
*   We fixed a bug to output a link if opening the URL in a browser fails.
*   We fixed a bug to catch missing hooks from a command; the initialization error is now included in the debug outputs. This allows any command to be run from a project directory without immediately posting an error.
*   We fixed a bug to remove ANSI escape sequences from the debug log outputs for an improved grepping experience.
*   We fixed a bug to verify that deprecated flags are properly substituted.
*   We fixed an issue to make our releases run more smoothly. Nothing to see here!

**Tags:**

*   [Release](https://docs.slack.dev/changelog/tags/release.md)
*   [Slack CLI](https://docs.slack.dev/changelog/tags/slack-cli.md)
