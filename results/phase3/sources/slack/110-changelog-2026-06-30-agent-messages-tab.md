---
title: "Introducing the Agent messaging experience"
summary: "Agents now support a new messaging experience, set by your app manifest:"
url: "https://docs.slack.dev/changelog/2026/06/30/agent-messages-tab"
type: "changelog"
---

Source: https://docs.slack.dev/changelog/2026/06/30/agent-messages-tab

# Introducing the Agent messaging experience

June 30, 2026

Agents now support a new messaging experience, set by your [app manifest](https://docs.slack.dev/reference/app-manifest.md#features):

*   **Agent messaging experience** (`agent_view`): agent conversations now look & feel the same as a regular direct message. Gone is the history tab and new chat button. Instead, all of your conversations appear in the standard message tab and your agent can respond in-thread.
*   **Assistant messaging experience** (`assistant_view`): agent conversations happen in separate Chat and History tabs.

New apps can only use the Agent messaging experience. Apps that already use the Assistant messaging experience can continue to use it for now, but `assistant_view` will eventually be deprecated, and we'll ask existing apps to migrate to `agent_view`.

The Agent messaging experience changes the following:

*   **Knowing when a user opens a DM**: rely on the [`app_home_opened`](https://docs.slack.dev/reference/events/app_home_opened.md) event to know when a user has actively opened a DM with your app. The [`assistant_thread_started`](https://docs.slack.dev/reference/events/assistant_thread_started.md) event no longer indicates this. See [Migrating to the Agent messaging experience](https://docs.slack.dev/ai/migrating-to-agent-messaging.md) for details.
*   **Suggested prompts**: [suggested prompts](https://docs.slack.dev/reference/methods/assistant.threads.setsuggestedprompts.md) now live at the top of the Messages tab instead of within threads, and the `thread_ts` argument is no longer required when `agent_view` is enabled.
*   **Continuing a conversation**: after a user sends a new message, calling the [`assistant.threads.setStatus`](https://docs.slack.dev/reference/methods/assistant.threads.setstatus.md) API method on that thread automatically opens the thread to keep the conversation going.

The [Slack CLI v4.4.0](https://github.com/slackapi/slack-cli/releases/tag/v4.4.0), [Python SDK v3.43.0](https://pypi.org/project/slack-sdk/3.43.0/) with [Bolt Python v1.29.0](https://github.com/slackapi/bolt-python/releases/tag/v1.29.0), and [@slack/web-api@7.18.0](https://github.com/slackapi/node-slack-sdk/releases/tag/@slack/web-api@7.18.0) (for the Node Slack SDK) are required to access the Agent View feature.

Already have an app using the Assistant messaging experience? Follow the [migration checklist](https://docs.slack.dev/ai/migrating-to-agent-messaging.md) to move to the Agent messaging experience. Read more in the guide to [developing agents](https://docs.slack.dev/ai/developing-agents.md).

**Tags:**

*   [Announcement](https://docs.slack.dev/changelog/tags/announcement.md)
