---
title: "Removing the Slack CLI deno command"
summary: "We previously mentioned that we had deprecated the deno command and removed its listing from the help command. We have now removed the deno command completely. Developers who were depending on this command should now use the deno executable directly."
url: "https://docs.slack.dev/changelog/2025/02/27/slack-cli"
type: "changelog"
---

Source: https://docs.slack.dev/changelog/2025/02/27/slack-cli

# Removing the Slack CLI deno command

February 27, 2025

We [previously](https://docs.slack.dev/changelog/2023/12/14/slack-cli.md) mentioned that we had deprecated the `deno` command and removed its listing from the `help` command. We have now removed the `deno` command completely. Developers who were depending on this command should now use the deno executable directly.

We've also removed support for the deprecated, pre-release Deno Slack SDK versions that used `slack.yaml` and `project.ts` files. The Run-on-Slack platform no longer supports the `slack.yaml` file format, and no production projects should be affected. The `project.ts` file was deprecated by the Deno Slack SDK in favor of `manifest.ts` and `manifest.json` files.

**Tags:**

*   [Slack CLI](https://docs.slack.dev/changelog/tags/slack-cli.md)
*   [Breaking change](https://docs.slack.dev/changelog/tags/breaking-change.md)
