# GH-600: Developing in Agentic AI Systems - Comprehensive Study Guide (STUDY.en.md)

This guide provides a comprehensive, highly structured study reference covering the complete curriculum of **Microsoft & GitHub Course GH-600T00-A: Developing in Agentic AI Systems** and preparation for the **GitHub Certified: Agentic AI Developer** certification exam.

---

## 📌 TABLE OF CONTENTS

1. [Module 1: Foundations of Agentic AI in GitHub](#module-1-foundations-of-agentic-ai-in-github)
   - Assistant vs. Agent Distinction
   - The Plan → Act → Evaluate Lifecycle
   - GitHub as System of Record and Control Plane
   - Responsibility Model and the Contributor Model
   - Core Anti-Patterns and Risks
2. [Module 2: Designing Agent Architecture and SDLC Integration](#module-2-designing-agent-architecture-and-sdlc-integration)
   - Mapping Agent Responsibilities to SDLC Stages
   - Task Contracts: Inputs, Outputs, and Enforceable Success Criteria
   - Plan-First vs. Plan + Execution Workflows
   - Pull Request-Based Governance and Templates
   - Reliable Workflow Engineering ($GITHUB_OUTPUT, Contexts, Event Gating)
   - Operational Boundaries and Hook-Based Guardrails
3. [Module 3: Tooling, MCP, and Agent Execution Environments](#module-3-tooling-mcp-and-agent-execution-environments)
   - Model Context Protocol (MCP) Architecture and Components
   - Local vs. Remote MCP Servers (HTTP)
   - MCP Registry v0.1 Specification & Azure API Center Integration
   - MCP Allow Lists (Allow All vs. Registry Only)
   - Execution Context Boundaries (Repository Scope, Branch Isolation, Permissions)
   - GitHub Agentic Workflows (`gh-aw` & Continuous AI)
   - Custom Agents (`.github/agents/*.agent.md`)
4. [Module 4: Multi-Agent Systems and Orchestration](#module-4-multi-agent-systems-and-orchestration)
   - Responsibility Mapping and Scope Boundaries
   - Sequential vs. Parallel (Fan-Out / Fan-In with `needs`) Orchestration
   - Workflow-Level Concurrency Controls
   - Copilot Agent Modes & Parallelism Capabilities (Cloud vs. CLI vs. Local)
   - Conflict Detection, Merge Validation, and Escalation Thresholds
   - Subagents and Handoffs Syntax
   - Live Session Monitoring and Failure Recovery
5. [Module 5: Agent Memory, State, and Evaluation](#module-5-agent-memory-state-and-evaluation)
   - The Memory Hierarchy: Short-Term, Long-Term, and External Memory
   - Pull Requests as the Primary State Anchor
   - Context Drift Detection and Re-Anchoring
   - Log and Artifact Retention Policies (Default 90 Days, Public vs. Private)
   - Evaluation Signals, Quality Gates, and Security Signals
   - Root Cause Failure Classification
6. [Module 6: Governance, Guardrails, and Operations](#module-6-governance-guardrails-and-operations)
   - Risk-Based Autonomy Model (Low, Medium, High, Critical)
   - Least-Privilege GITHUB_TOKEN Patterns
   - CODEOWNERS Routing and Environment Approval Gates
   - PreToolUse Hook Schemas and Command Blocking
   - Defense-in-Depth Guardrail Workflows (Bot PR Review Requirements)
   - Operational Governance Cadences (Weekly, Monthly, Quarterly)
   - Core Governance Anti-Patterns

---

## MODULE 1: FOUNDATIONS OF AGENTIC AI IN GITHUB

### 1.1 Assistant vs. Agent Distinction

Understanding the operational differences between an assistant and an agent is fundamental to designing agentic systems in GitHub:

| Dimension | AI Assistant | Agentic AI (Agent) |
| :--- | :--- | :--- |
| **Operational Posture** | **Reactive:** Waits for user prompts, generates suggestions/explanations, and returns control to the user. | **Goal-Driven:** Interprets high-level goals, formulates intermediate plans, uses tools, and takes action across workflows. |
| **Action Authority** | Suggestions and code snippets only; does not directly modify repositories or invoke durable state changes. | Uses platform tools (APIs, workflows, git commands) to create durable outcomes (branches, commits, PRs). |
| **Feedback Handling** | Dependent on subsequent user input to adjust or correct code. | Evaluates system feedback signals (test failures, linter errors, scan alerts) and iterates autonomously until success criteria are met. |
| **GitHub Presence** | Sits in chat/editor panels; user manually applies snippets. | Enters the SDLC as a contributor via branches, commits, PRs, workflow executions, and review comments. |

### 1.2 The Plan → Act → Evaluate Lifecycle

Agentic systems do not execute a single prompt and terminate. They operate in a continuous, inspectable feedback loop:

```
    ┌──────────────────────────┐
    │          PLAN            │  <── Interprets goal, scopes files,
    └─────────────┬────────────┘      defines success criteria & rollback
                  │
                  ▼
    ┌──────────────────────────┐
    │          ACT             │  <── Creates branch, commits changes,
    └─────────────┬────────────┘      opens pull request (bounded scope)
                  │
                  ▼
    ┌──────────────────────────┐
    │        EVALUATE          │  <── CI status checks, SARIF scans,
    └─────────────┬────────────┘      CODEOWNERS reviews, policy gates
                  │
                  └── (If failed) ──> Re-plans and iterates (or escalates)
```

1. **Plan:** The agent interprets the task and produces a structured, inspectable approach. Rather than hiding reasoning in internal states, high-quality agents expose plans in PR descriptions, issues, or plan artifacts.
2. **Act:** The agent carries out execution within bounded surfaces—specifically isolated git branches, commits, and pull requests, never directly targeting the default branch.
3. **Evaluate:** Outcomes are assessed using **objective system signals**, never the agent's internal confidence. Signals include CI test runs, SARIF code scanning reports, secret scanning alerts, and reviewer feedback. If signals fail, the agent iterates or escalates to human oversight.

### 1.3 GitHub as System of Record and Control Plane

GitHub serves two complementary functions in agentic architectures:

- **System of Record (Historical Truth & Auditability):**
  - Stores repositories, branches, and immutable commit histories.
  - Retains issues and discussions to record context, user intent, and problem specifications.
  - Maintains pull requests as state aggregators of commits, conversations, and decisions.
  - Captures CI workflow runs, execution logs, and uploaded artifacts as durable evidence for post-hoc forensic review.
- **Control Plane (Policy Enforcement & Guardrails):**
  - **Pull Requests:** Mandates that changes are proposed and validated before entering protected branches.
  - **Rulesets & Branch Protection:** Restricts direct pushes, prevents force pushes/deletion, and enforces merge requirements.
  - **Required Status Checks:** Converts automated evaluation (build, test, lint, security scans) into enforceable merge gates.
  - **CODEOWNERS:** Automatically routes high-impact file changes to verified human domain experts.
  - **Environments:** Restricts secret access and pauses execution pending human approval before production deployments.

### 1.4 Responsibility Model and the Contributor Model

- **Responsibility Does Not Shift:** While agents perform execution, **humans remain strictly accountable** for outcomes. The team that configures permissions, approves task specifications, and merges PRs owns the production outcome.
- **The Contributor Model:**
  - Evaluates agent work using standard engineering criteria rather than novel "AI standards."
  - Avoids **Excessive Suspicion** (rejecting sound changes simply because AI authored them).
  - Avoids **Excessive Trust** (merging code without scrutiny simply because automation/CI passed).
  - **Practical Review Rubric:**
    - *Intent:* Is the goal clear and linked to an issue?
    - *Scope:* Are file changes strictly confined to the agreed plan?
    - *Evidence:* Did required status checks and security scans pass?
    - *Ownership:* Did CODEOWNERS review sensitive components?
    - *Rollback:* Is a clear escalation/revert path recorded for high-risk changes?

### 1.5 Core Anti-Patterns and Risks

| Anti-Pattern | Manifestation in GitHub | Architectural Mitigation |
| :--- | :--- | :--- |
| **Planless Execution** | PR contains a diff without an explicit, structured plan or rationale. | Require plan section in `.github/pull_request_template.md`; enforce via Plan Gate required status check. |
| **Over-Permissioned Agents** | Workflows or CLI agents run with broad write tokens (`write-all`) or unneeded secrets. | Enforce least-privilege `GITHUB_TOKEN`; scope secrets using environments with required reviewers. |
| **Hidden Reasoning** | Diff is present, but decision trail, assumptions, and execution logs are omitted. | Require plan artifacts, link workflow runs, and record decision points in PR comments/artifacts. |
| **Blind Trust in Automation** | "CI passed, ship it" mindset without validating real intent or subtle side-effects. | Combine automated checks with CODEOWNERS, mandatory reviews, and risk-based manual approval gates. |

---

## MODULE 2: DESIGNING AGENT ARCHITECTURE AND SDLC INTEGRATION

### 2.1 Mapping Agent Responsibilities to SDLC Stages

Agents should never operate across the entire SDLC without architectural constraints. Teams scope agents to specific stages where GitHub provides natural control surfaces:

| SDLC Stage | Typical Agent Responsibility | Primary GitHub Control Surface |
| :--- | :--- | :--- |
| **Planning** | Draft scope, break down steps, identify risks and success criteria. | GitHub Issues, PR descriptions, Agents interface. |
| **Implementation** | Create branch, apply targeted changes, open/update PR. | Dedicated Branch, Commits, Pull Request. |
| **Validation** | Run tests, attach scan outputs, iterate on failures. | Workflow runs, status checks, uploaded artifacts. |
| **Deployment** | Strictly restricted; agent prepares manifests but cannot unilaterally deploy. | GitHub Environments, Deployment Approvals. |

> **Fundamental Design Boundary:** *Agents propose; humans and policy accept.*

### 2.2 Task Contracts: Inputs, Outputs, and Success Criteria

Every structured agent task must define an explicit three-part contract:
1. **Inputs:** Contextual requirements (Issue links, security alerts), permitted path boundaries (`src/**`), and explicit constraints (no changes to `infra/` or `.github/workflows/`).
2. **Outputs:** Durable repository artifacts: an inspectable plan, bounded commits on a dedicated branch, and a pull request linked to workflow runs.
3. **Success Criteria:** Enforceable, goal-aligned conditions.
   - *Tip:* "CI passed" is necessary but often insufficient. Success criteria must reflect problem resolution (e.g., "vulnerable package upgraded AND CodeQL SARIF scan reports 0 alerts" rather than merely "unit tests compiled").

### 2.3 Plan-First vs. Plan + Execution Workflows

| Characteristic | Option A: Plan-First Pull Request | Option B: Plan + Execution Pull Request |
| :--- | :--- | :--- |
| **Mechanism** | Agent opens a PR containing **only the structured plan** (zero code diff). Code is written only after humans review and approve the plan. | Agent opens a PR containing both the structured plan (in description) and initial code commits simultaneously. |
| **Validation Timing** | Human validation occurs **before** any code changes enter the branch. | Validation occurs **before merge**, but code diffs exist during proposal. |
| **Risk Profile** | **Minimizes blast radius:** Eliminates wasted review effort and early code contamination in high-risk domains. | **Higher velocity:** Introduces potential noise/misalignment during proposal, but guarded by merge gates. |
| **Ideal Use Cases** | High-risk environments: `.github/workflows/`, infrastructure as code (`infra/`), authentication/crypto modules, production configs. | Low-to-medium risk tasks: routine refactors, documentation updates, standard bug fixes with comprehensive test coverage. |

### 2.4 Pull Request Governance & Plan Gate Workflow

To transform a policy expectation ("always provide a plan") into an unbypassable technical guarantee, implement a **Plan Gate** workflow and enforce it as a Required Status Check:

```yaml
# File: .github/workflows/plan-gate.yml
name: Plan Gate

on:
  pull_request:
    branches: [ main ]

jobs:
  require-plan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Verify plan artifact presence
        run: |
          if [ ! -f ".github/pull_request_template.md" ]; then
            echo "Error: Plan documentation is missing from this pull request."
            exit 1
          fi
          echo "Plan artifact verified."
```

### 2.5 Reliable Workflow Engineering

#### Data Passing: Step Outputs vs. Job Outputs vs. Environment Variables

- **Step Outputs:** Pass data sequentially between steps within the *same* job using `$GITHUB_OUTPUT`.
- **Job Outputs:** Pass structured data across *different* jobs via explicit `outputs:` definitions and `needs:` dependencies.
- **Environment Variables (`env`):** Used for runtime tool configuration, not as data-passing contracts.

```yaml
jobs:
  plan:
    runs-on: ubuntu-latest
    outputs:
      plan_payload: ${{ steps.generate_plan.outputs.plan }}
    steps:
      - id: generate_plan
        run: echo "plan=Refactor authentication token validation" >> "$GITHUB_OUTPUT"

  implement:
    needs: plan
    runs-on: ubuntu-latest
    steps:
      - name: Consume plan
        run: echo "Executing plan: ${{ needs.plan.outputs.plan_payload }}"
```

#### GitHub Contexts Disambiguation

- `github.*`: Event metadata and runtime context (`github.event_name`, `github.ref`, `github.actor`, `github.workflow`).
- `vars.*`: Centrally managed, non-sensitive configuration variables configured at repository or organization level.
- `env.*`: Step-level or job-level environment variables defined in the YAML file.

#### Defensive Event Gating

Workflows with multiple triggers (`pull_request`, `workflow_dispatch`, `schedule`) must use defensive job-level conditions to prevent PR-specific operations from failing in non-PR executions:

```yaml
jobs:
  pr-tasks:
    # Defensive gate: executes only when triggered by a true PR event
    if: github.event_name == 'pull_request'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm test
```

---

## MODULE 3: TOOLING, MCP, AND AGENT EXECUTION ENVIRONMENTS

### 3.1 Model Context Protocol (MCP) Architecture

Model Context Protocol (MCP) is an open standard that allows AI agents to interface with external tools, APIs, and databases via a unified protocol:
- **Client (Agent):** Discovers tools, sends structured execution requests, and processes structured responses.
- **MCP Server:** Exposes available capabilities, translates client commands, and communicates with underlying systems.

#### Local vs. Remote MCP Servers

| Attribute | Local MCP Server | Remote MCP Server (HTTP) |
| :--- | :--- | :--- |
| **Runtime Location** | Runs directly on the developer's workstation or runner (`http://localhost:3000`). | Hosted externally on network infrastructure (`https://api.githubcopilot.com/mcp/`). |
| **Primary Strength** | Direct access to local filesystems, custom internal binaries, and debugging tools. | Standardized setup across distributed teams; centralized updates and auth. |
| **Authentication** | Runs in local developer context; typically no external auth tokens required. | Requires token/OAuth handshake during setup. |
| **Enterprise Support** | GitHub Enterprise Server (GHES) & GitHub Enterprise Cloud (GHEC). | GitHub Enterprise Cloud (GHEC) including data residency environments. |

### 3.2 MCP Registry v0.1 Specification & Azure API Center

An **MCP Registry** provides a centralized catalog for discovering approved MCP servers.

#### Mandatory HTTPS Endpoints (v0.1 Spec):
- `GET /v0.1/servers`
- `GET /v0.1/servers/{serverName}/versions/latest`
- `GET /v0.1/servers/{serverName}/versions/{version}`

#### Mandatory CORS Headers:
- `Access-Control-Allow-Origin: *`
- `Access-Control-Allow-Methods: GET, OPTIONS`
- `Access-Control-Allow-Headers: Authorization, Content-Type`

#### Azure API Center Integration Rules:
- Azure API Center can serve as an enterprise managed MCP Registry.
- **Configuration Rule:** Enter the **base URL only** in the GitHub Copilot policy settings (do NOT append `/v0.1/servers`).
- Enable **anonymous access** on the API Center endpoint so Copilot can fetch the catalog without authentication blockers.

### 3.3 MCP Allow Lists

Configured at the Organization or Enterprise level under **Copilot → Policies → MCP**:
- **Allow all:** Developers can install and connect any MCP server without restrictions.
- **Registry only:** Developers are strictly limited to servers listed in the configured registry.
  - *Critical Constraint:* Under "Registry only", even local servers (`http://localhost:...`) must be explicitly declared in the registry catalog, and their server IDs must match exactly!

### 3.4 Execution Context Boundaries

1. **Repository Scope:** The agent is confined to the target repository. It cannot traverse to other repositories unless explicitly provisioned.
2. **Branch Isolation:** Autonomous agents do not write to protected branches (`main`). They create dedicated branches (`copilot/*`, `agent/*`) and submit Pull Requests.
3. **Workflow Boundaries:** Agents run inside containerized GitHub Actions runner environments, isolating execution from local machines.
4. **Permission Scoping:** Governed by `GITHUB_TOKEN` scopes or granular GitHub App permissions.

### 3.5 GitHub Agentic Workflows (`gh-aw` & Continuous AI)

GitHub Agentic Workflows represent repository automation driven by natural language intent rather than rigid procedural YAML:
- **Two-Part Anatomy:**
  - **YAML Frontmatter (Guardrails):** Defines triggers (`on`), least-privilege `permissions:`, tool allowlists (`tools:`), and `safe-outputs:`.
  - **Markdown Body (Intent):** Expresses the high-level objective in plain English (e.g., triage open issues, draft changelog).
- **Compilation:** The `.md` workflow is compiled into an immutable **lock file** executed by GitHub Actions.
- **Security Protections:**
  - Read-only tokens by default.
  - **Safe-outputs:** The agent cannot directly modify issues or code; it outputs structured proposals that a separate, permission-gated step validates and applies.
  - **Zero secrets** inside the agent's LLM process.
  - Network isolation with allowlisted outbound destinations and threat detection scanning.

### 3.6 Custom Agents (`.github/agents/*.agent.md`)

Repository-scoped custom agents specify focused responsibilities:

```markdown
---
applyTo:
  - '**/*.js'
  - 'src/auth/**'
tools:
  - read_file
  - search_files
---
You are a specialized security reviewer analyzing authentication code paths...
```
- `applyTo`: Constrains the agent's view to specific directory globs.
- `tools`: Restricts capability to safe, read-only tools.
- *Boundary Note:* Custom agents define focus and toolsets, but do **not** govern branch creation or PR merging. Execution orchestration is enforced by the surrounding runner or platform.

---

## MODULE 4: MULTI-AGENT SYSTEMS AND ORCHESTRATION

### 4.1 Responsibility Mapping and Scope Boundaries

When multiple agents run in the same codebase, uncontrolled overlap leads to thrashing and merge conflicts. Architectural boundaries must restrict what each agent can alter:

```
  ┌─────────────────────────────────────────────────────────────┐
  │                      REPOSITORY SCOPE                       │
  ├──────────────────────────────┬──────────────────────────────┤
  │ Dependency Agent             │ Refactoring Agent            │
  │ • package.json               │ • src/**/*.ts                │
  │ • package-lock.json          │ • Excludes manifests & lock  │
  ├──────────────────────────────┼──────────────────────────────┤
  │ Security Agent (Reviewer)    │ Documentation Agent          │
  │ • Read-only analysis         │ • docs/**/*.md               │
  │ • SARIF uploads & reporting  │ • README.md                  │
  └──────────────────────────────┴──────────────────────────────┘
```

### 4.2 Sequential vs. Parallel Orchestration Patterns

#### 1. Sequential Orchestration (`workflow_run`)
Used when one agent's output must be verified before another agent begins:

```yaml
# File: .github/workflows/security-validation.yml
name: Security Validation
on:
  workflow_run:
    workflows: ["CI Validation"]
    types: [completed]

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - run: echo "Running secondary security validation following successful CI..."
```

#### 2. Parallel Fan-Out / Fan-In Orchestration (`needs`)
Tested heavily in the GH-600 exam. Coordinates multiple independent analysis agents in parallel, then synthesizes their findings in a single merger job:

```yaml
name: Multi-Agent Fan-Out Fan-In
on:
  workflow_dispatch:

jobs:
  spec_analyzer:
    runs-on: ubuntu-latest
    steps:
      - run: ./executors/spec_analyzer.sh

  risk_reviewer:
    runs-on: ubuntu-latest
    steps:
      - run: ./executors/risk_reviewer.sh

  plan_merger:
    runs-on: ubuntu-latest
    needs: [spec_analyzer, risk_reviewer] # Fan-In: Waits for BOTH upstream jobs
    steps:
      - name: Synthesize merged plan
        run: ./executors/plan_merger.sh
```

### 4.3 Workflow-Level Concurrency Controls

When agents push iterative updates to PR branches, concurrent workflow runs collide and waste resources.

```yaml
concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true
```

- **Why `${{ github.workflow }}-${{ github.ref }}`?** Isolates concurrency to the specific workflow *and* specific branch.
- **Why NOT just `${{ github.ref }}`?** Using only `github.ref` creates a global branch lock, blocking unrelated CI workflows from executing concurrently.
- `cancel-in-progress: true`: Automatically cancels stale, in-flight runs when a new commit is pushed.

### 4.4 Copilot Agent Modes & Parallelism Capabilities

| Agent Mode | Supports Concurrent Parallel Sessions? |
| :--- | :--- |
| **Copilot Cloud** | **Yes** (Multiple cloud sessions can run in parallel across tasks) |
| **Copilot CLI** | **Yes** (Terminal processes can run concurrently across tasks) |
| **Copilot Local (IDE)** | **No** (Serial execution only; operates on one active task at a time) |

### 4.5 Conflict Detection, Arbitration, and Escalation

- **The "First Merge Wins" Anti-Pattern:** Allowing whichever PR merges first to dictate repository state leads to semantic instability.
- **Merge Validation Check:** Proactively detect conflicts inside the PR prior to human review:
  ```bash
  git fetch origin main
  git merge --no-commit origin/main
  ```
- **Escalation Threshold Rule:** If a PR encounters merge conflicts or identical test failures **twice (2 times)** consecutively after automated rebase attempts, automated retries must immediately halt and escalate to a human reviewer with a summary report.

### 4.6 Subagents and Handoffs Syntax

Configured in the parent agent frontmatter (`planner.agent.md`):

```yaml
---
agents: [implementer, code-review]
handoffs:
  - label: Start Implementation
    agent: implementer
    send: true
    model: GPT-5.2
  - label: Run Review
    agent: code-review
    prompt: Review the code changes made in the previous step.
---
```
- `disable-model-invocation: true`: Prevents this agent from being invoked as a subagent by other agents.
- `user-invocable: false`: Hides the agent from end-user selection in chat/UI interfaces.
- **Ruleset Bypass Actor:** When repository rulesets enforce signed commits, the Copilot agent (which cannot cryptographically sign commits) is blocked. Administrators resolve this by adding **"GitHub Copilot" as a Bypass Actor** for that specific ruleset on automation branches.

### 4.7 Live Session Monitoring

Inspect stalled or running agent tasks in real time using the GitHub CLI:

```bash
gh agent-task view --log --follow
```

---

## MODULE 5: AGENT MEMORY, STATE, AND EVALUATION

### 5.1 The Memory Hierarchy

```
  ┌─────────────────────────────────────────────────────────────┐
  │ SHORT-TERM MEMORY (Working Context)                        │
  │ • In-session prompts, active turn context, temporary tokens │
  │ • Ephemeral: Lost when session terminates                   │
  └──────────────────────────────┬──────────────────────────────┘
                                 │
  ┌──────────────────────────────▼──────────────────────────────┐
  │ LONG-TERM MEMORY (Curated Knowledge)                       │
  │ • Reusable instructions, architectural rules, skills       │
  │ • Stable: Maintained across sessions and users             │
  └──────────────────────────────┬──────────────────────────────┘
                                 │
  ┌──────────────────────────────▼──────────────────────────────┐
  │ EXTERNAL MEMORY (Durable Source of Truth)                  │
  │ • Requirements & Acceptance Criteria ──> Issues            │
  │ • Progress, Decisions & Plan Evolution ──> Pull Requests   │
  │ • Evidence, Logs & Test Results ──> Workflow Artifacts     │
  └─────────────────────────────────────────────────────────────┘
```

### 5.2 Pull Requests as State Anchors

Pull requests serve as the central aggregation point for agent state. When switching between environments (IDE → CLI → Cloud), agents should not rely on fragile session history; they re-anchor to the PR:
1. Fetch PR description and linked Issue acceptance criteria.
2. Inspect commit history to identify already completed steps.
3. Review status checks to determine validation progress.
4. Continue execution from the latest commit SHA.

### 5.3 Context Drift Detection and Remediation

- **Definition:** Occurs when an agent's incremental changes diverge from the original requirements, violate previous architectural decisions, or introduce out-of-scope edits.
- **Detection:**
  - PR diff introduces files not declared in the plan or issue.
  - Required checks fail due to regression in previously settled areas.
  - Commits contradict earlier PR comments or decisions.
- **Remediation:**
  - Re-anchor the agent to the primary Issue and PR description.
  - Revert out-of-scope commits.
  - If drift is severe, apply the **Reset Rule**: update or close the PR and restart with explicit boundary constraints.

### 5.4 Log and Artifact Retention Policies

- **Default Retention:** GitHub Actions workflow logs and uploaded artifacts are retained for **90 days** by default, after which they are permanently deleted.
- **Configurability:**
  - **Public Repositories:** Configurable between **1 and 90 days**.
  - **Private Repositories:** Can be extended up to **400 days** for audit/compliance.
- **Permanent Deletion:** Deleted artifacts cannot be restored.
- **Audit Verification:** To detect whether an artifact was manually or programmatically deleted, query the GitHub Organization Audit Log for:
  ```text
  action:artifact.destroy
  ```

### 5.5 Evaluation Signals and Failure Classification

#### Quality Gates & Security Signals:
- Code scanning (SARIF uploads via CodeQL or third-party analyzers).
- Secret scanning alerts and push protection events.
- Required status checks enforced via branch protection or rulesets.

#### Root Cause Failure Categories:
1. **Reasoning Errors:** Incorrect assumptions, faulty business logic, or failure to respect acceptance criteria. (*Fix: Refine prompt instructions and repo guidelines*).
2. **Tool Misuse:** Passing invalid CLI flags, misconfiguring workflow triggers, or referencing non-existent scripts. (*Fix: Constrain tool arguments and update execution templates*).
3. **Context Issues:** Operating on stale branch tips, missing prior decisions, or conflicting requirements across artifacts. (*Fix: Rebase onto main, re-anchor to issue acceptance criteria*).

---

## MODULE 6: GOVERNANCE, GUARDRAILS, AND OPERATIONS

### 6.1 Risk-Based Autonomy Model

Autonomy must be dynamically bounded based on the reversibility and potential blast radius of the action:

| Risk Tier | Representative Actions | Recommended Control & Autonomy Level |
| :--- | :--- | :--- |
| **Low** | Documentation (`docs/`), formatting, typo fixes | **Full Automation:** Automated merge via GitHub Auto-Merge after required status checks pass. |
| **Medium** | Application code (`src/`), routine dependency upgrades | **PR + Required Checks:** Mandatory CI validation and at least one human peer review. |
| **High** | Workflow changes (`.github/workflows/`), infrastructure (`infra/`) | **CODEOWNERS + Strict Review:** Mandatory approval from specialized owners; strict ruleset blocks. |
| **Critical** | Production deployment, access to production secrets | **Environment Approval Gate:** Agent can only stage changes; execution is strictly human-authorized. |

### 6.2 Least-Privilege GITHUB_TOKEN Design

Always set default permissions to read-only at the workflow root, elevating write permissions solely for specific jobs that require them:

```yaml
permissions:
  contents: read

jobs:
  analyze:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm run lint

  publish_pr:
    runs-on: ubuntu-latest
    permissions:
      contents: write
      pull-requests: write
    steps:
      - uses: actions/checkout@v4
      - run: gh pr create --title "[agent] Update dependencies" --body "Plan details..."
```

### 6.3 PreToolUse Hook Schemas & Command Blocking

For local or CLI agents, use repository-scoped hook configurations (`.github/hooks/`) to enforce deterministic deny rules before execution:

```json
{
  "hook": "preToolUse",
  "tools": ["shell(bash)"],
  "rules": [
    { "match": "sudo", "permissionDecision": "deny" },
    { "match": "rm -rf /", "permissionDecision": "deny" },
    { "match": "curl .*\\|\\s*bash", "permissionDecision": "deny" }
  ]
}
```

#### CLI Scoped Tool Flag:
When running read-only inspection tasks via Copilot CLI, strictly scope tool access to Git commands:
```bash
copilot -p "Summarize the last 10 commits and highlight breaking changes." --allow-tool 'shell(git)'
```

### 6.4 Defense-in-Depth: Enforcing Human Approvals on Bot PRs

To prevent bot PRs from being automatically approved and merged by other automated accounts, use a guardrail workflow:

```yaml
name: Agent Guardrails
on:
  pull_request:
    branches: [main]

permissions:
  contents: read

jobs:
  enforce-human-approval:
    runs-on: ubuntu-latest
    steps:
      - name: Verify human review
        uses: actions/github-script@v7
        with:
          script: |
            const reviews = await github.rest.pulls.listReviews({
              owner: context.repo.owner,
              repo: context.repo.repo,
              pull_number: context.payload.pull_request.number
            });

            const approvedByHuman = reviews.data.some(r =>
              r.state === "APPROVED" &&
              r.user &&
              r.user.type === "User" &&
              r.user.login !== "github-copilot[bot]"
            );

            if (!approvedByHuman) {
              core.setFailed("A verified human approval is required before this PR can merge.");
            }
```

### 6.5 Operational Governance Cadence

| Cadence | Operational Focus & Checklist |
| :--- | :--- |
| **Weekly** | Review failed agent workflow runs, flaky checks, and repeated policy blocks. |
| **Monthly** | Audit `GITHUB_TOKEN` permission scopes, secret exposures, and environment boundary settings. |
| **Quarterly** | Full audit of repository rulesets, CODEOWNERS mapping validity, environment approvers, and artifact retention settings. |

### 6.6 Core Governance Anti-Patterns Checklist

1. **Unbounded Autonomy:** Allowing agents to deploy to production without environment approval gates.
2. **Excess Permissions:** Assigning `write-all` tokens to workflows that only perform static code analysis.
3. **Missing Audit Trail:** Storing execution results in ephemeral console logs rather than uploading durable artifacts (`actions/upload-artifact@v4`).
4. **Bypass Paths:** Leaving protected branches vulnerable to direct pushes by not enforcing rulesets.
5. **Rubber-Stamping:** Approvers approving PRs solely because automated checks passed, without inspecting plan fidelity or code quality.

---
*This document summarizes all modules of the GH-600 curriculum for comprehensive preparation for the GitHub Certified: Agentic AI Developer exam.*
