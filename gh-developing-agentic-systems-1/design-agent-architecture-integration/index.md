---
title: Designing Agent Architecture and SDLC Integration - Training | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/training/modules/design-agent-architecture-integration/
description: Illustration showing how agentic systems use GitHub workflows such as branches, pull requests, checks, and repository rules to safely build and maintain software.
---

# Designing Agent Architecture and SDLC Integration - Training | Microsoft Learn

![](/en-us/training/achievements/generic-badge.svg)

# Designing Agent Architecture and SDLC Integration

- Module
- 9 Units

 Intermediate 

 DevOps Engineer 

 Administrator 

 Developer 

 Solution Architect 

 GitHub 

Learn how agentic systems use GitHub workflows to build software safely.

## Learning objectives

By the end of this module, you will be able to:

- Map agent responsibilities to SDLC stages and define architectural boundaries
- Define structured agent tasks using inputs, outputs, and success criteria
- Separate planning, reasoning, and execution to create inspectable and reliable workflows
- Implement pull request-based governance using templates, checks, CODEOWNERS, rules, and environments
- Design reliable workflows using outputs, contexts, triggers, and cross-job handoffs
- Operate agent systems safely using observability, tool governance, secrets boundaries, hooks, and reliability patterns

## Prerequisites

Before getting started, you should have:

- A GitHub account and familiarity with repositories, branches, and pull requests
- Basic experience with GitHub Actions workflows and status checks
- A general understanding of the software development lifecycle (SDLC) (planning, implementation, validation, deployment)
- Awareness of repository governance concepts, such as required reviews, CODEOWNERS, and branch protection

Some enforcement controls (for example, rulesets/branch protection and required checks) require repository or organization administrator permissions to configure.

This module focuses on repository-level architecture (pull requests, checks, and rules). In practice, agent systems also include environment-level controls such as network access restrictions. For example, GitHub Copilot cloud agent uses a configurable firewall to limit external access. These controls define what the agent can access at runtime, while PR-based governance defines what changes are accepted.

For more information, see: [Customize the agent firewall for Copilot cloud agent.](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/customize-the-agent-firewall)

- [Introduction](1-introduction)min
- [Map agent responsibilities to the SDLC](2-agent-responsibilities)min
- [Define inputs, outputs, and success criteria](3-inputs-outputs-success-criteria)min
- [Separate planning, reasoning, and execution](4-plan-reason-execution)min
- [Examples of implementing PR governance with templates, checks, CODEOWNERS, rules, and environment gates](5-pull-request-governance-controls)min
- [Build reliable workflows - outputs, contexts, triggers, and cross-job handoffs](6-reliable-workflows)min
- [Control and operate agents - observability, tools, MCP, secrets, hooks, and reliability](7-agent-operations-controls)min
- [Knowledge Check](8-knowledge-check)min
- [Summary](9-summary)min

Take the module assessment

 Module Assessment Results

Assess your understanding of this module. Sign in and answer all questions correctly to earn a pass designation on your profile.