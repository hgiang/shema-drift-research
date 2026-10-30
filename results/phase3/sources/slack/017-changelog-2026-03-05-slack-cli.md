---
title: "Release: Slack CLI v3.14.0"
summary: "Version 3.14.0 of the developer tools for the Slack platform has landed!"
url: "https://docs.slack.dev/changelog/2026/03/05/slack-cli"
type: "changelog"
---

Source: https://docs.slack.dev/changelog/2026/03/05/slack-cli

# Release: Slack CLI v3.14.0

March 5, 2026

Version `3.14.0` of the developer tools for the Slack platform has landed!

*   The [`slack create`](https://docs.slack.dev/tools/slack-cli/reference/commands/slack_create.md) command now prompts you for a custom app name if the randomly generated default isn't your thing. This prompt appears before scaffolding a new project from a template, and when making new project directories with your custom app name, we now replace spaces with a dash (instead of removing spaces altogether) to make navigation a bit better.
*   The `slack create` command now updates the app name in the `package.json` and `pyproject.toml` project files.
*   We've updated the `slack create` and [`slack init`](https://docs.slack.dev/tools/slack-cli/reference/commands/slack_init.md) commands to support creating a Python virtual environment (.venv) when it doesn't exist, and installing the project's dependencies from the `requirements.txt` and `pyproject.toml` project files.
*   When running Slack CLI commands in a Bolt Python project, the Slack CLI will attempt to automatically activate the Python virtual environment (.venv). This allows commands that use the `slack-cli-hooks` Python package to run safely and successfully, even when the terminal system doesn't have the virtual environment activated.
*   We've added a `--subdir` flag to the `slack create` command for extracting a subdirectory from a template repository as the project root. This supports monorepo-style templates where multiple apps live in subdirectories (e.g., `slack create my-app -t org/monorepo --subdir apps/my-app`).
*   The [`slack docs`](https://docs.slack.dev/tools/slack-cli/reference/commands/slack_docs.md) command opens the slack developer docs site, and you can now use the `--search` flag to open the docs search page with the provided query.
*   We fixed a bug and now avoid infinite loops when searching for the root project `.slack` directory for projects existing on drives other than the `C:` drive on Windows.
*   We fixed a bug and now check whether an installed `git` command exists on Windows.

**Tags:**

*   [Release](https://docs.slack.dev/changelog/tags/release.md)
*   [Slack CLI](https://docs.slack.dev/changelog/tags/slack-cli.md)
