---
title: Module assessment - Training | Microsoft Learn
canonicalUrl: https://learn.microsoft.com/en-us/training/modules/agent-tooling-mcp-execution-environments/6-knowledge-check
description: Verify your knowledge of tool selection, MCP, and safe agent execution.
---

# Module assessment

Completed

- 5 minutes

1.
Where do agents execute tasks when working with GitHub repositories?

Directly on the developer's local machine.

Within workflows powered by GitHub Actions.

Inside the GitHub web interface without workflows.

On external servers without using GitHub workflows.

2.
How are agent-generated code changes isolated before review?

By committing directly to the default branch.

By creating and working within a separate branch.

By storing changes in a temporary external system.

By applying changes only after deployment.

3.
What determines what an agent can do during workflow execution?

The number of contributors in the repository.

Workflow permissions and the GITHUB\_TOKEN scope.

The size of the repository.

The number of workflow runs completed.

4.
What is the purpose of a pull request in agent workflows?

To automatically merge agent changes into the default branch.

To provide a place to review and validate changes before merging.

To bypass workflow execution.

To execute code changes immediately without checks.

5.
How can workflows be triggered after an agent updates code?

Only manually by a repository administrator.

Through events such as push or pull request.

Only when a repository is forked.

Only when code is downloaded locally.

6.
What is the role of an MCP server?

To replace GitHub workflows.

To expose tools and services that agents can use.

To store repository code.

To execute workflows instead of GitHub Actions.

7.
What controls which MCP servers an agent can use?

Repository size limits.

Registries and allow lists.

Workflow execution time limits.

The number of commits in the repository.

8.
Why are environment protections used in GitHub workflows?

To increase workflow execution speed.

To require approvals and protect sensitive operations.

To automatically merge pull requests.

To disable workflows on certain branches.

9.
What is the effect of using least-privilege permissions in workflows?

It gives agents full access to all resources.

It limits actions to only what is required.

It prevents workflows from running.

It automatically approves pull requests.

10.
How are agent actions kept visible and reviewable?

By hiding logs and restricting access.

Through workflow logs and pull request review.

By executing actions outside GitHub.

By skipping validation steps.