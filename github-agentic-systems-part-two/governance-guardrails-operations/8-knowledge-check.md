---
title: Knowledge Check - Training | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/training/modules/governance-guardrails-operations/8-knowledge-check
description: Verify your knowledge of governance, guardrails, and operations.
---

# Knowledge check

Completed

- 5 minutes

1.
What is the best way to allow a terminal agent to perform a low-risk, read-only task like summarizing recent commits without granting broad capabilities?

Allow all tools so the agent never prompts for approval

Scope tool access to only what is required for read-only Git inspection

Grant write access by default and rely on audits afterward

Deny all shell access and require manual copy/paste of commit history

2.
Which GitHub-native control is most effective for requiring explicit approval before production workflows access production secrets?

A PR template that asks for review

A repository README policy statement

A protected environment with required reviewers

A label applied by the agent

3.
What is the recommended least-privilege pattern for GITHUB\_TOKEN permissions in agent-driven workflows?

Set write permissions globally so any job can push if needed

Default to read-only and elevate permissions only for the job that performs write operations

Disable permissions entirely and store a PAT in the repository

Grant all permissions during business hours only

4.
Which configuration helps prevent overlapping production deployments and cancels in-progress deployments when a newer run starts?

Using larger runners

Adding more approvals

Concurrency with a shared group and cancel-in-progress

Disabling workflow\_dispatch

5.
What is the best GitHub-native mechanism to route required review for sensitive paths like .github/workflows/ and infra/?

Asking reviewers in chat

CODEOWNERS (with required reviews policy)

Adding labels and milestones

Squashing commits before merge