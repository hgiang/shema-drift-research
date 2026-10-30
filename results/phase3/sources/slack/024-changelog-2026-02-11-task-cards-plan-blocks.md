---
title: "Apps can now display thinking steps to users!"
summary: "Display your apps' and agents' actions with three new Block Kit components:"
url: "https://docs.slack.dev/changelog/2026/02/11/task-cards-plan-blocks"
type: "changelog"
---

Source: https://docs.slack.dev/changelog/2026/02/11/task-cards-plan-blocks

# Apps can now display thinking steps to users!

February 11, 2026

Display your apps' and agents' actions with three new Block Kit components:

*   The [`task_card`](https://docs.slack.dev/reference/block-kit/blocks/task-card-block.md) block displays a single task.
*   The [`url source`](https://docs.slack.dev/reference/block-kit/block-elements/url-source-element.md) element displays clickable URL references within a task card.
*   The [`plan`](https://docs.slack.dev/reference/block-kit/blocks/plan-block.md) block displays multiple of those tasks together in a unified view.

How tasks are displayed is set with a new parameter in the text-streaming API methods: `task_display_mode`. Use this to choose whether your app's tasks appear individually or in a comprehensive plan.

Then update the task cards and plan via the new `chunks` parameter. The parameter also supports plain markdown.

Ready to test it out? Check out our guide on [developing AI apps](https://docs.slack.dev/ai/developing-agents.md#streaming), or jump straight to the text-streaming methods' reference pages:

*   [`chat.startStream`](https://docs.slack.dev/reference/methods/chat.startstream.md)
*   [`chat.appendStream`](https://docs.slack.dev/reference/methods/chat.appendstream.md)
*   [`chat.stopStream`](https://docs.slack.dev/reference/methods/chat.stopstream.md)

**Tags:**

*   [New Feature](https://docs.slack.dev/changelog/tags/new-feature.md)
*   [Block Kit](https://docs.slack.dev/changelog/tags/block-kit.md)
