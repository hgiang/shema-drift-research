---
title: "Release: Slack CLI v4.0.0 and v4.0.1"
summary: "Version 4.0.0 of the developer tools for the Slack platform has arrived with lots of goodies for you!"
url: "https://docs.slack.dev/changelog/2026/04/10/slack-cli"
type: "changelog"
---

Source: https://docs.slack.dev/changelog/2026/04/10/slack-cli

# Release: Slack CLI v4.0.0 and v4.0.1

April 10, 2026

Version `4.0.0` of the developer tools for the Slack platform has arrived with lots of goodies for you!

This version ties together iterative improvements, with special focus on agent development. The Slack CLI can now quickly scaffold an AI agent using the `slack create agent` command and our collection of agent sample apps. Features such as local manifest management, environment variable management, and file watching with live reloading come together to streamline the agent development experience.

## New features {#new-features}

### Creating apps and agents {#creating-apps-and-agents}

*   The AI Agent templates now include an IT support agent available with the `slack create agent` command.
    *   Use `slack create agent` to choose one the new AI Agent templates:
        *   Starter Agent:
            *   Supports Bolt for JavaScript and Bolt for Python
            *   Available in the Claude Agent SDK, OpenAI Agents SDK, and Pydantic AI framework
        *   IT Support Agent:
            *   Supports Bolt for JavaScript and Bolt for Python
            *   Available in the Claude Agent SDK, OpenAI Agents SDK, and Pydantic AI framework
    *   Slack MCP Server is built-in to all of the AI Agent templates.
*   The Slack CLI installer now ends with a recommendation to run the `slack create agent` command.
*   The `slack create` command now separates selections into categories of templates for frameworks to better align with the options displayed.

### Managing environment variables {#managing-environment-variables}

*   Environment variables saved to `.env` files are now loaded into the process before hook scripts run. This improves the `slack run` command, as additional dependencies are no longer required to load environment variables into the runtime context. Other commands such as the `slack deploy` command and the `slack manifest` command also benefit, as the underlying hooks can be more expressive in customizations, and can also be configured for custom environments.
*   The `slack env list` command now lists the environment variables available from `.env` files for apps that aren't run on Slack infrastructure.
*   The `slack env set` command can now add and update environment variables in `.env` files for apps that aren't built or run on Slack infrastructure, making configuring and iterating on a Bolt app from the command line faster.
*   The `slack env unset` command now removes environment variables from `.env` files for apps that aren't built or run on Slack infrastructure.
*   The `slack env` commands were aliased to `env set` and `env unset` to match more common shell conventions. (These commands were previously recommended as `add` and `remove`, which became confusing when existing variables were updated.) Refer to the [`slack env`](https://docs.slack.dev/tools/slack-cli/reference/commands/slack_env.md) command docs for more details.

### Finding docs programmatically {#finding-docs-programmatically}

*   We've added a `slack docs search` subcommand, which can output search results using plain text, json, or your preferred browser. Refer to the [`slack docs`](https://docs.slack.dev/tools/slack-cli/reference/commands/slack_docs.md) command docs for more details.

## Developing an app {#developing-an-app}

*   We've added file watch and live reload support to `slack run`. This allows your Slack apps to immediately reflect changes to files by you or your agent-related development tools (Claude Code, Codex, etc.).
*   It's easier to start an HTTP OAuth Server or app with a custom path, as the `slack run` command now accepts an optional argument for the app entry point. For example: `$ slack run ./src/app_oauth.py`.
*   We updated the `slack run` command for Enterprise Organizations so that "All workspaces" is always shown as the first option when prompted to choose whether to grant to all workspaces or a specific workspace.
*   When a command runs using the verbose flag (`--verbose`) and makes an HTTP request, the output now includes the HTTP Header's User-Agent. For example: `HTTP Request User-Agent: slack-cli/v3.15.0 (os: darwin)`.

## Python project improvements {#python-project-improvements}

*   The `slack create` and `slack init` commands now create a Python Virtual Environment (`.venv`) when it doesn't exist.
*   The `slack create` and `slack init` commands now install your project dependencies from `pyproject.toml` and `requirements.txt` after activating your Python virtual environment.
*   All `slack` commands now activate your Python virtual environment, when it exists. For example, this means `slack run` will activate your `.venv` before starting your app's server.

## Bolt Framework agent improvements {#bolt-framework-agent-improvements}

*   [Bolt for JavaScript 4.7.0](https://github.com/slackapi/bolt-js/releases/tag/%40slack%2Fbolt%404.7.0) and [Bolt for Python 1.28.0](https://github.com/slackapi/bolt-python/releases/tag/v1.28.0) support a collection of new agent-related UI features.
*   Event listener handlers now provide utilities to display your agent's thinking status, streaming text, display suggested prompts, and more.
*   The Slack MCP Server now works with Bolt Frameworks.
*   Popular agent frameworks such as Claude Agent SDK, OpenAI Agents SDK, Pydantic, and Vercel now work with Bolt.

## Prompt look and feel {#prompt-look-and-feel}

*   We've refreshed our interactive prompt style with [Charm's Huh](https://github.com/charmbracelet/huh) package.
*   Interactive prompts now support light-mode and dark-mode.

## Bug fixes {#bug-fixes}

*   We fixed a `pyproject.toml` error that was displayed by the `slack create` and `slack init` commands. The error occurred when creating a Bolt Python project that includes `pyproject.toml`, but doesn't define a `[project]` section or `dependencies` array. Now, a warning is displayed in `--verbose` mode, as this is a valid `pyproject.toml` format.
*   We fixed a bug: environment variable values set for hook commands are no longer surrounded with double quotes.
*   We fixed a bug with the Windows installer. The installer now suggests providing an optional alias as a separate step from downloading the installer if earlier overwrites were avoided but still caused the installation to fail.
*   We fixed a bug: errors will appear sooner in CI and scripting setups if either interactive input or a confirmation is requested, rather than waiting for a timeout.
*   We fixed a bug: The sections of `slack env` command outputs are now titled to match the command itself, and are grouped under one section for each command.

## But wait, there's more! {#but-wait-theres-more}

In version `4.0.1` of the developer tools, we've fixed the `slack create agent` command so that it shows prompts for the app template, Bolt Framework, and then Agent Framework. This adds more templates to the options, including Bolt for JavaScript and Bolt for Python implementations of the Starter Agent and Support Agent templates.

**Tags:**

*   [Release](https://docs.slack.dev/changelog/tags/release.md)
*   [Slack CLI](https://docs.slack.dev/changelog/tags/slack-cli.md)
