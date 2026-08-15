# Core HITL Patterns (Approval Gates, Escalation Ladders, Collaborative Drafting)

Once you move past the abstract autonomy spectrum, you need concrete architectural blueprints to implement oversight without slowing down operations. The five core patterns cover over 90% of production agent workflows, focusing on when and how humans interact with the system.

## 1. The Approval Gate Pattern
The most intuitive and critical pattern for high-stakes workflows.

When to use: Whenever an agent is about to take an irreversible action (an action that cannot be undone without significant cost, risk, or embarrassment)—such as transferring funds, executing database migrations, deleting customer data, or publishing external communications.

### How it works:

The agent completes its reasoning loop and prepares a tool execution payload.

Instead of calling the tool, the workflow pauses and serializes its state.

A notification is dispatched to a review interface with full context (e.g., the exact SQL query, the target database, and the reason for the action).

A human clicks Approve, Reject, or Modify. If approved, execution resumes securely.

[Agent Plans Action] ──► [Save State / Pause] ──► [Review Dashboard]
                                                          │
                                                ┌─────────┴─────────┐
                                              Approve             Reject
                                                │                   │
                                                ▼                   ▼
                                       [Execute Tool Call]    [Halt Workflow]

## 2. The Escalation Ladder Pattern
Not all tasks carry equal risk; therefore, oversight should scale dynamically based on the complexity or impact of the request.

When to use: Customer service tiers, IT operations triage, or automated financial adjustments.

### How it works:

Level 1 (Autonomous): The agent handles low-risk, standard requests independently (e.g., standard password resets or minor billing inquiries).

Level 2 (Automated Triage + Supervisor Review): If a request involves higher thresholds (e.g., a refund request over $500 or anomalous sentiment), the agent attempts a draft resolution but automatically routes it to a junior team lead for quick review.

Level 3 (Human-Only): If the agent detects high risk, regulatory exposure, or extreme user frustration, it bypasses automation entirely and transfers the context directly to a human specialist.

## 3. The Confidence-Based Routing Pattern
Instead of forcing a human to review every single output, the system relies on internal heuristics and confidence metrics to triage work.

When to use: High-volume text classification, information extraction, or multi-turn conversational agents.

### How it works:

The agent evaluates its own output or extracts structured entities and assigns a confidence score (or checks alignment against deterministic constraints).

High Confidence (> 90%): The action proceeds automatically.

Medium/Low Confidence (< 90%): The item is automatically routed to an asynchronous review queue so human operators can focus solely on edge cases and ambiguous data.

## 4. Collaborative Drafting Pattern
For creative, writing, or strategic tasks, forcing a human to judge a binary "Approve/Reject" gate often leads to friction because the raw output may be close, but not quite right.

When to use: Content creation, legal clause generation, code scaffolding, or policy drafting.

How it works: The agent acts as an always-on co-pilot. It generates a detailed draft, positions the human as a meticulous editor, and instantly adapts or re-generates sections based on inline human edits and feedback.

## 5. Audit Trail with Lazy Review Pattern
When high throughput is required and synchronous blocking would ruin the user experience, systems rely on post-action oversight.

When to use: Low-to-moderate risk autonomous actions where speed is paramount.

How it works: The agent executes actions autonomously in real time, logging every intermediate thought step, tool call, and output into a tamper-proof audit trail. Compliance officers or automated sampling scripts periodically review logs or audit a random percentage of actions after the fact.


### Summary Checklist for Choosing a Pattern
Is the action irreversible (money, data deletion)? Use an Approval Gate.

Is the volume high with varying complexity? Use an Escalation Ladder or Confidence-Based Routing.

Is the output subjective or creative? Use Collaborative Drafting.

Is real-time speed critical for low-risk actions? Use an Audit Trail / Lazy Review.