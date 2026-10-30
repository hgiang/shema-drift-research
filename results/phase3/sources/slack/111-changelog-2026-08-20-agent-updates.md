---
title: "The next wave of Agent messaging experience"
summary: "We're rolling out a wave of updates to agents on Slack, along with an important heads-up about the road ahead for the Assistant messaging experience."
url: "https://docs.slack.dev/changelog/2026/08/20/agent-updates"
type: "changelog"
---

Source: https://docs.slack.dev/changelog/2026/08/20/agent-updates

# The next wave of Agent messaging experience

August 20, 2026

We're rolling out a wave of updates to agents on Slack, along with an important heads-up about the road ahead for the Assistant messaging experience.

## Agent updates and the deprecation of assistant_view {#agent-updates-and-the-deprecation-of-assistant_view}

The Assistant messaging experience (`assistant_view`) will be deprecated in **February 2027**. The assistant-related methods that power it are being replaced by a new set of API methods: the **Agent Sessions API**. Agent sessions let users manage their conversations with your agent in one place, with a status, a title, and a stop button. The [`agents.sessions.setStatus`](https://docs.slack.dev/reference/methods/agents.sessions.setstatus.md) and [`agents.sessions.rename`](https://docs.slack.dev/reference/methods/agents.sessions.rename.md) API methods replace the `assistant.threads.setStatus` and `assistant.threads.setTitle` API methods, respectively. For now, your existing calls keep working through a compatibility bridge. See the [Agent sessions](https://docs.slack.dev/ai/agent-sessions.md) guide to get started.

The Agent messaging experience (`agent_view`) is already available, and we recommend moving to it now. If your app still uses `assistant_view`, follow the [migration guide](https://docs.slack.dev/ai/migrating-to-agent-messaging.md) to move to the new experience. Read more in the guide to [developing agents](https://docs.slack.dev/ai/developing-agents.md).

## What's new for agents {#whats-new-for-agents}

Alongside this announcement, we're releasing a set of improvements to the agent experience:

*   **Upgraded Tools tab**: a newly renamed and revamped **Agents & Tools** tab helps users find popular agents with a new landing page.
*   **Improved thread experience**: including multi-agent stacking, thread naming, a revamped thinking UI, and a native stop button for agent streams. When a user stops your agent, your app receives an [`agent_session_stopped`](https://docs.slack.dev/reference/events/agent_session_stopped.md) event.
*   **Plan and Task card block updates**: UI refinements to the [plan](https://docs.slack.dev/reference/block-kit/blocks/plan-block.md) and [task card](https://docs.slack.dev/reference/block-kit/blocks/task-card-block.md) blocks agents use to show their work.
*   **Marketplace data in the About tab**: an agent's Marketplace data now appears in its About tab.
*   **Agent sessions in the sidebar**: A new sidebar with pin / archive / unread and live updates.

**Tags:**

*   [Announcement](https://docs.slack.dev/changelog/tags/announcement.md)
*   [Deprecation](https://docs.slack.dev/changelog/tags/deprecation.md)
