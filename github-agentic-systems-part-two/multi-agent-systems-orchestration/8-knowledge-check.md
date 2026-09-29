---
title: Knowledge check - Training | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/training/modules/multi-agent-systems-orchestration/8-knowledge-check
description: Test your understanding of multi-agent coordination, GitHub-native controls, workflow isolation, and deployment governance.
---

# Knowledge Check

Completed

- 5 minutes

1.
What is the most effective coordination primitive for multi-agent work in GitHub?

Private agent-to-agent messaging

Pull requests and surrounding artifacts (checks, reviews, history)

A shared spreadsheet

A single long-running workflow without branches

2.
Which configuration helps prevent repeated overlapping workflow runs when a PR is updated frequently?

Larger runners

Concurrency with cancel-in-progress

Removing required checks

Disabling PR triggers

3.
What is the best GitHub-native mechanism to route review for sensitive paths touched by agent pull requests?

Asking reviewers in chat

CODEOWNERS (with required reviews policy)

Adding more labels

Squashing commits

4.
Which is an example of a coordination failure rather than an individual agent failure?

A single unit test fails once

Two agent pull requests repeatedly conflict because they change the same files

A reviewer requests changes

A workflow run finishes successfully

5.
What is a safe pattern for high-risk actions like production deployments?

Auto-deploy after tests pass

Use environments with required reviewers so jobs pause for approval

Allow direct pushes to main

Disable workflow approvals