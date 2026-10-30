---
title: "Release: Slack CLI v2.3.0"
summary: "Version 2.3.0 of the developer tools for the Slack automations platform has arrived!"
url: "https://docs.slack.dev/changelog/2023/06/01/slack-cli"
type: "changelog"
---

Source: https://docs.slack.dev/changelog/2023/06/01/slack-cli

# Release: Slack CLI v2.3.0

June 1, 2023

Version `2.3.0` of the developer tools for the Slack automations platform has arrived!

*   The `external-auth remove` command now allows you to select a token for deletion.
*   The new `external-auth select-auth` command allows you to select a unique auth for each of the workflows in an app. This command is mandatory when using new coded workflows that have a step containing `credentialSource DEVELOPER`; that is, every time a coded workflow is created, this command must be called after the `external-auth add` command.
*   The `slack auth token` and `slack auth revoke` commands allow you to manage service tokens.
*   The `slack auth token` command allows you to get the `slackauthticket` and copy and paste it into your workspace to exchange for the service token. The service token will not be saved to your `credentials.json` file; instead, it is presented in the prompt for you to copy and paste to your CI/CD pipelines. Once you obtained a service token, you can use the `slack login --auth <your-service-token>` command to authorize your Slack CLI. The service token will not conflict with your regular authentication token; you can continue using your regular authentication token within the Slack CLI while using the service token for your CI/CD pipelines.
*   The new global `--token <token>` flag allows you to pass the service token used by requests requiring authentication. For example, to install an app, use: `slack install --token <your-service-token>`. To create a trigger, use: `slack trigger create --token <your-service-token> --app deployed --trigger-def triggers/trigger_def_file.ts`. To deploy an app, use: `slack deploy --token <your-service-token>`
*   We added support for a global `--experiment [name,name,...]` flag.

**Tags:**

*   [Release](https://docs.slack.dev/changelog/tags/release.md)
*   [Slack CLI](https://docs.slack.dev/changelog/tags/slack-cli.md)
