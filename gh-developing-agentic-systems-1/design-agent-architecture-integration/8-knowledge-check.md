---
title: Knowledge check - Training | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/training/modules/design-agent-architecture-integration/8-knowledge-check
description: Test your understanding of agent architecture, governance controls, and SDLC integration in GitHub.
---

# Knowledge Check

Completed

- 5 minutes

1.
What is the most reliable way to prevent planless execution from being merged?

Ask the agent to be careful.

Require a plan template only.

Make a plan check a required status check and require pull request reviews.

Allow direct pushes but require tests.

2.
Which GitHub feature most directly routes reviews based on changed file paths?

Issues

CODEOWNERS

Actions artifacts

Releases

3.
In a plan-act-evaluate architecture, where should evaluation evidence primarily live?

Only inside the agent's private logs

In PR comments only

In GitHub-native artifacts like workflow runs, checks, and uploaded artifacts

In a separate external document

4.
Which design best expresses risk-based autonomy for production deployments?

Let the agent deploy after tests pass

Use GitHub Environments with required reviewers for production

Allow direct pushes to main

Disable workflow approvals

5.
Which is an architectural anti-pattern in agent design?

Clear success criteria

Required checks

Mixed planning and execution with no inspectable plan

Uploading artifacts