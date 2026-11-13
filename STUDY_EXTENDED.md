# GH-600: Developing in Agentic AI Systems - Extended Study Guide (STUDY_EXTENDED.md)

This is a **companion to `STUDY.en.md`**. It only contains material from the course source (`gh-developing-agentic-systems-1/` and `github-agentic-systems-part-two/`) that `STUDY.en.md` leaves out or covers too thinly. Read `STUDY.en.md` first, then this file.

Section numbers follow the module numbering used in `STUDY.en.md`. A "➕" marks a section that extends an existing `STUDY.en.md` section.

---

## 📌 TABLE OF CONTENTS

1. [Module 1 additions: Foundations](#module-1-additions-foundations)
2. [Module 2 additions: Architecture & SDLC integration](#module-2-additions-architecture--sdlc-integration)
3. [Module 3 additions: Tooling, MCP & execution environments](#module-3-additions-tooling-mcp--execution-environments)
4. [Module 4 additions: Multi-agent systems & orchestration](#module-4-additions-multi-agent-systems--orchestration)
5. [Module 5 additions: Memory, state & evaluation](#module-5-additions-memory-state--evaluation)
6. [Module 6 additions: Governance, guardrails & operations](#module-6-additions-governance-guardrails--operations)
7. [Hands-on exercises (what to know)](#hands-on-exercises-what-to-know)
8. [Official knowledge-check questions with answers](#official-knowledge-check-questions-with-answers)
9. [Rapid-fire exam facts](#rapid-fire-exam-facts)

---

## MODULE 1 ADDITIONS: FOUNDATIONS

### ➕ 1.1 Recognizing agent vs. assistant behavior

An AI system is behaving as an **agent** when it can:
- Maintain a goal across multiple steps
- Decide intermediate actions
- Use tools
- Create or modify **durable artifacts** (branch / commits / PR)
- Iterate based on feedback signals

It is behaving as an **assistant** when it produces suggestions or explanations, takes no repository actions, and requires the user to apply each step manually.

> **Exam signal:** The *best indicator* that an AI system is acting as an agent is that **it opens a pull request from a branch it created**. "Suggests code in chat", "summarizes docs" and "explains an error" are assistant behaviors.

An agent **does not replace the workflow; it enters the workflow as a participant**. Agent behavior shows up in GitHub through branches/commits (what changed), PRs (what is proposed and why), workflows/checks (what evidence exists), and reviews (what humans accepted or rejected).

### ➕ 1.2 Lifecycle details

- The lifecycle is a **loop**, not a sequence: plan → act → evaluate repeats until success criteria are met **or the work is handed off to a human**.
- A reviewable plan includes **scope** (what will change), **success criteria** (how you'll know it worked) and a **rollback or escalation path**.
- Evaluation signals: workflow runs/status checks, code review feedback, and security signals (code scanning, including SARIF uploads; secret scanning alerts; dependency alerts; push protection).
- Key lesson: **evaluation is grounded in system signals, not in the agent's confidence.**
- A high-quality system makes every phase visible: **plan is inspectable, action is bounded, evaluation uses objective signals.** If any piece is missing, trust degrades.

### ➕ 1.3 Control plane details

| GitHub control | What it enforces | Why it matters for agents |
| :--- | :--- | :--- |
| Pull requests | Changes are proposed before merging | Makes agent work reviewable |
| **Required reviews** | Approval gate | Prevents unreviewed merges; supports accountability |
| Required status checks | CI evidence before merging | Converts evaluation into enforceable policy |
| CODEOWNERS | Review routing by path | Right experts supervise high-impact changes |
| Rulesets / branch protection | Centralized branch policy | Prevents unsafe merges |
| Environments | Approvals for deployments/secrets | Controls sensitive execution and secret access |

- **Enforcement depends on configuration.** Enabling required checks and rulesets is typically an **admin task**. The supervision model works everywhere, but enforcement only exists when the controls are turned on.
- **GitHub Actions belongs in the control plane.** For agentic systems, "what the agent can do" often reduces to **"what the workflow token and tool credentials can do."**
- **"Approve and run workflows"**: in some agent PR workflows, a human must explicitly approve running workflows. This built-in guardrail stops privileged workflows from running automatically on untrusted changes.

### ➕ 1.4 Accountability and traceability

**Who stays accountable?** The people and teams who:
1. Defined the task
2. Set permissions
3. Chose and configured controls
4. Approved the resulting change

**Traceability trail** in GitHub: PRs and commit history, review comments and approvals, workflow runs and uploaded artifacts, code scanning uploads and alerts, secret scanning alerts and push protection events, and **organization audit log events**.

**Minimum audit trail for an agent contribution (6 items):**
1. A stated goal (issue link or PR description)
2. An inspectable plan (PR plan section or file)
3. A bounded changeset (branch and commits)
4. Automated evidence (workflow run and artifacts)
5. Human judgment (review and approval)
6. A clear outcome (merge, revert or escalation)

**Post-incident questions** (for example, the fix passed CI but caused a regression). Don't only ask whether the agent made a mistake. Ask whether the system made it understandable and preventable:
- Was there a visible plan and scope?
- Were the right reviewers requested, and did they approve?
- Did the checks match the risk of the change?
- Is the audit trail sufficient to reconstruct what happened?

> **Blind trust in automation:** checks only validate what they're designed to detect. A passing build doesn't mean the change is complete, appropriate or low-risk.

### ➕ 1.5 Contributor model: full rubric

`STUDY.en.md` omits the **Policy** item. The full rubric has six items:

| Item | Question |
| :--- | :--- |
| Intent | Clear goal and visible plan? |
| Scope | Changed files aligned with the plan? |
| Evidence | Required checks pass? Logs/artifacts available? |
| Ownership | CODEOWNERS reviewed sensitive areas? |
| **Policy** | Complies with rulesets / branch rules / environments? |
| Fallback | Rollback or escalation clear for high-risk changes? |

**What good looks like.** A well-supervised agent contribution is:
- **Understandable** (clear goal and plan)
- **Bounded** (scoped changeset, least privilege)
- **Reviewable** (right owners, evidence present)
- **Policy-compliant**
- **Reconstructable** (audit trail supports post-hoc analysis)

> **Exam signal:** Under the contributor model, reviewers evaluate **first** whether the change meets the repo's **definition of done** (scope, checks, review, policy). They do *not* start from whether the author is human or AI.

---

## MODULE 2 ADDITIONS: ARCHITECTURE & SDLC INTEGRATION

### Glossary (two terms the exam can contrast)
- **Plan (artifact):** a structured description of intended changes, typically in the PR description. It outlines goal, scope, steps, risks and validation criteria.
- **Planning (agent capability):** the process by which an agent generates or refines a plan. It can start from a GitHub issue or from the Agents interface.

### ➕ 2.1 Architectural boundaries
- Most teams **start by scoping agents to the implementation and validation stages**, where PRs and workflows provide natural control points.
- Three boundary rules:
  1. **Scope early** to reduce blast radius: limit which directories an agent can modify, by policy and ownership.
  2. Treat **workflow and infra changes as higher risk** than application code changes.
  3. **Prefer PR-based work even for automation**, and avoid direct-to-default-branch changes.
- Example: a dependency remediation agent detects a vulnerable dependency, creates a branch, updates the dependency and lockfile, then opens a PR with a plan and expected success signals. **At that point its scoped responsibility is complete.** Acceptance happens through checks, reviews and policy.

### ➕ 2.2 Task contract: full success criteria
Success criteria for a vulnerability-remediation task:
- Required checks pass (build/test/lint)
- The security signal is resolved (the vulnerable version is replaced)
- **Scope matches intent** (no unexpected files changed)
- **A rollback or escalation path is recorded** for higher-risk changes

Constraints in the inputs: no workflow changes without platform review, no secrets introduced, no direct-to-main pushes.

**Failure example to remember:** with vague criteria, the agent "updates the dependency" but **leaves the vulnerable version reachable through a transitive dependency**, or makes broad changes that are hard to validate.

**CI + CodeQL as an enforceable success signal.** Note the `security-events: write` permission:
```yaml
on:
  pull_request:
    branches: [ main ]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm test
  security-analysis:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      security-events: write
    steps:
      - uses: actions/checkout@v4
      - uses: github/codeql-action/init@v3
      - uses: github/codeql-action/analyze@v3
```
This is only enforced once it's configured as a **required check** through rulesets or branch protection.

### ➕ 2.3 Separating planning, execution and validation
| Concern | Where it lives in GitHub |
| :--- | :--- |
| Planning (what and why) | PR description, issue comment, PR template artifact |
| Execution (concrete changes) | Commits on a branch |
| Validation (evidence) | Checks, scans, artifacts, review outcomes |

When planning and execution are mixed, reviewers see only the final diff. They lose the chance to validate intent early, catch misunderstandings and control scope.

- **Key insight:** the choice is **not whether** work is reviewed (it always is). It is **when** code may be generated relative to human validation. Both options use the same GitHub controls.
- Option B's risk exists **during the proposal stage, not after merge**: extra reviewer effort, unnecessary changes, and temporary plan/implementation misalignment.

**Enforcing planning boundaries (4 mechanisms):**
1. **Capability boundary:** planning agents are **read-only**, so they can't modify files during planning.
2. **Explicit transition / handoff** to an implementation agent, and only after plan approval.
3. **Tool gating in orchestrators:** run planning with tools disabled, then enable tools after the plan is accepted.
4. **"Plan mode" workflows:** the interface generates a plan artifact and pauses before applying any changes.

> **Exam signal:** "Instructions not to edit" are **guidance**. **Tool allowlists and gates are enforcement.**

### ➕ 2.4 PR governance details

**Safe flow:** agent creates branch → opens PR with plan → required reviews validate approach → Actions run required checks → all checks pass and approvals complete → merge.

**PR template** (`.github/pull_request_template.md`):
```md
## Plan (required)
- **Goal:**
- **Scope (paths/files):**
- **Steps:**
- **Success criteria (verifiable):**
  - [ ] Required checks pass
  - [ ] Security signals reviewed (as applicable)
- **Risks + mitigations:**
- **Rollback / escalation plan:**
## Evidence
- Workflow run(s):
- Scan results (if applicable):
## Review checklist
- [ ] Plan reviewed and approved
- [ ] Required reviews satisfied
- [ ] Required checks satisfied
```

- A **template alone is not enough.** The most reliable way to stop planless execution from merging is to **make the plan check a required status check AND require PR reviews** (knowledge-check answer).
- GitHub **can require explicit approval before workflows run** on agent-generated changes.
- If an agent can bypass required checks or merge without reviews, that's **a workflow design failure, not a model problem.**
- Key takeaway: *Pull requests aren't just collaboration tools; they are enforcement mechanisms.*

### ➕ 2.5 Risk-based autonomy in the Design module
The Design module's version of the table names the control for each tier:

| Tier | Paths | Autonomy design |
| :--- | :--- | :--- |
| Low | `docs/`, formatting | Merge automated with **GitHub automerge** after required checks (and reviews, if configured) |
| Medium | `src/`, dependency bumps | PR + checks + **at least one review** |
| High | `infra/`, `.github/workflows/` | CODEOWNERS + **multiple reviews** + stricter rulesets |
| Critical | Production deploy settings, secrets | **Environment approvals; agent prepares but can't execute** |

Environment approval: a job targeting an environment that has required reviewers **pauses until approval is granted**.

### 2.6 Operating agents: evidence, tools, MCP, secrets, hooks (NEW)

**Minimum observability set:** a visible plan artifact, PR + commit history, workflow run links for required checks, durable artifacts (logs/reports/traces), and review outcomes/approvals.

- Put links to runs and artifacts in an **"Evidence" section of the PR**.
- **Evidence must be traceable to a specific workflow run AND a specific commit** ("which run produced this artifact, against what code state?").
- **Share evidence across jobs with artifacts:** upload where produced, download where reviewed or deployed. **Don't commit generated files back to the repo.**

**Reliability assumes failure:**
- *Retries:* the agent can update the branch when checks fail.
- *Escalation:* persistent failures are summarized and handed to a human.
- *Rollback readiness:* high-risk changes include rollback notes and scope limits.

**Safe iteration policy:** if a required check fails, the agent may revise the branch and rerun. **If the same required check fails twice, escalate to a human** with:
1. what failed,
2. what was attempted,
3. what evidence exists, and
4. the suggested next step.

This prevents infinite loops.

**Agent profile configuration: three kinds of control**
| Boundary | Controls |
| :--- | :--- |
| **Capability** | Which tools are allowed (prefer allowlists) |
| **Visibility** | Whether the agent is user-selectable in the interactive UI |
| **Delegation** | Which subagents can be invoked and how handoffs occur |

Design guidance:
- Use read-only toolsets for planning and review agents.
- Restrict implementation tools to execution agents.
- **Treat changes to tool allowlists as governance-sensitive.**

**MCP servers: extending tools safely**
- *Transport shape:* remote endpoint vs local process.
- *Authentication:* tokens **injected at runtime via protected secret boundaries**.
- *Namespace control:* **enable a narrow tool subset rather than broad wildcards.**
- Adding or expanding MCP tools **increases blast radius**, so review it like a **high-risk dependency**.

**Secrets**
- Never put secrets in instruction files, committed config files, or workflow YAML in plain text.
- Use protected secret boundaries for runtime injection. Pass secrets only to the components that need them, and scope them by environment.
- Key principle: **"The agent's runtime environment has its own secret boundary; don't assume it automatically inherits repository CI secrets."**

**Hooks**
- Hooks are configuration files stored in the repo (for example under `.github/hooks/`). They run custom commands at specific points during agent execution.
- Simplified form shown in the Design module (the Governance module shows the `preToolUse` rule form found in `STUDY.en.md` §6.3):
  ```json
  {
    "name": "block-high-risk-command",
    "trigger": "pre-tool-use",
    "run": "if [[ \"$TOOL\" == \"delete\" ]]; then echo 'Blocked unsafe command'; exit 1; fi"
  }
  ```

| Hook pattern | Purpose |
| :--- | :--- |
| **Pre-action** | Validate or **block** unsafe actions before execution |
| **Post-action** | **Log** tool usage, outputs and decisions for auditing |
| **Error** | Capture failures and trigger escalation/alerting |

- Hooks are **enforceable control points that operate independently of the model's reasoning**.
- **Rollback-safe pattern:** deploy sensitive configuration from **explicit references (commit SHA / tag)**, not "latest on a branch".
- `permissions: { contents: read, pull-requests: write }` lets automation read code and update PR context (comments, statuses) without broad write access.

---

## MODULE 3 ADDITIONS: TOOLING, MCP & EXECUTION ENVIRONMENTS

### 3.0 How agents interact with GitHub (NEW)

GitHub supports agent work through **three layers**:
1. **GitHub APIs:** read repo state and perform actions
2. **GitHub Actions workflows:** run automation on controlled runners
3. **GitHub Agentic Workflows:** describe higher-level tasks in Markdown, executed by coding agents under guardrails

**APIs**
- They let agents create branches and commits, read repo data, open and update PRs, and trigger workflows.
- **Every API request must be authenticated**, with a **personal access token, a GitHub App token, or the `GITHUB_TOKEN`**. This makes every agent action permission-controlled and auditable.

**How an agent creates a change** (same as a developer, with a separate API operation per step: Git refs, contents, PRs):
1. Select a base branch
2. Create a working branch
3. Modify or create files
4. Commit
5. Open a PR

**Actions as the execution layer:** agents don't execute on your machine. **Copilot cloud agent runs in a GitHub Actions-powered environment**, so workflows are the foundation of agent execution: tests, validation, automation and deployment.

**Traditional vs. agentic workflows**
| Traditional Actions workflow | GitHub Agentic Workflow |
| :--- | :--- |
| Deterministic YAML; every step, trigger and condition explicit | Describe the **desired outcome** in Markdown; guardrails in frontmatter |
| Defines *how* | Agent decides *how* within frontmatter constraints |
| CI/CD | **Extends, does not replace, CI/CD** ("Continuous AI") |

Best suited to **open-ended but bounded** tasks: triage, reporting, documentation maintenance, CI failure analysis and code improvement.

Example agentic workflow (frontmatter = boundaries, Markdown = intent). It is **compiled into a lock file** that Actions executes:
```markdown
---
on:
  schedule: daily
permissions:
  contents: read
  issues: read
  pull-requests: read
safe-outputs:
  create-issue:
    title-prefix: "[repo-status] "
    labels:
      - report
tools:
  github:
---
Daily Repository Status Report
Create a daily report for maintainers. Include recent activity, highlights
and risks, and recommended next steps. Link to relevant issues and PRs.
```
The permissions are read-only. The only write (creating an issue) goes through **safe-outputs**.

**Triggering workflows:** events (push, pull_request), manually (`workflow_dispatch`), or programmatically through the GitHub API. Each run executes jobs in **isolated environments**.

**Agent sessions are observable and interactive.** You can monitor the session log, see what actions the agent takes, give feedback or adjust the task, and review the final PR.

**End-to-end flow (7 steps):**
1. Task assigned (issue, chat or CLI)
2. Agent selects repo and base branch
3. Agent analyzes and plans
4. API operations create branch and commits
5. PR opened
6. Workflows validate or deploy
7. User reviews, approves or requests updates

Result: scoped to a repo, controlled by permissions, executed through workflows, visible and reviewable.

### ➕ 3.1 MCP: the three concepts and setup

| Concept | Role |
| :--- | :--- |
| **MCP server** | **Exposes** tools |
| **Registry** | Makes servers **discoverable and trustable** |
| **Allow list** | Decides which servers are **permitted** |

- The **GitHub MCP server** connects AI clients to repos, issues and PRs.
- **Remote is the recommended setup for most users.** GitHub Enterprise Server supports **local** configuration. GitHub Enterprise Cloud with data residency supports **both**.
- **Add a remote MCP server in VS Code:**
  1. Open Copilot Chat in **Agent mode** → **Tools** icon → **Configure tools** → **Add MCP server**
  2. Choose **HTTP** and enter `https://api.githubcopilot.com/mcp/`
  3. A name is auto-generated. Choose the scope (**current workspace or all workspaces**).
  4. **Authenticate** (sign in to GitHub) and save.
- **Local server:** same flow, but with a local endpoint such as `http://localhost:3000`. Usually no external auth is needed.

### ➕ 3.2 MCP registries
- By default, supported IDEs use the **GitHub MCP Registry**. Developers can switch to a custom registry.
- Registries help when teams want simpler setup, orgs want a standard set of approved servers, or developers need a curated list instead of unmanaged discovery.
- **Three ways to create or host a custom registry:**
  1. Fork and self-host the open-source MCP Registry
  2. Run the open-source registry locally with **Docker**
  3. Build and publish your own implementation that follows the v0.1 spec
  4. (Alternative) Use **Azure API Center** as a managed registry, with anonymous access enabled
- Once configured, the registry becomes the **source of truth for available MCP servers**.

### ➕ 3.3 MCP allow lists: where to configure them
- Allow-list enforcement is applied at **organization and enterprise level** and is **tied to the Copilot seat** that governs the user.
- An org/enterprise can decide whether developers can use MCP servers **at all**, use **any** server, or use **only registry** servers.
- **Enterprise path:** Enterprise → **AI controls** → **MCP** → ensure *MCP servers in Copilot* is **Enabled everywhere** → enter the *MCP Registry URL* → *Restrict MCP access to registry servers*: **Allow all** or **Registry only**
- **Organization path:** Org → **Settings** → **Copilot** → **Policies** → in *Features*, enable *MCP servers in Copilot* → *MCP Registry URL* (optional) → **Allow all** or **Registry only**
- The policy is **applied immediately to all developers**.

**Practical flow:**
1. Org configures the registry
2. Org defines the allow-list policy
3. Developer opens an MCP-capable client
4. Client discovers approved servers
5. Developer enables a server
6. Agent uses its tools

### ➕ 3.4 Execution context: configuration details
- **Execution context** = repository + branch + workflow + permissions. It defines both **visibility and capability**.
- **Enable Copilot cloud agent for a repo:** Repo → **Settings** → *Code & automation* → **Copilot** → **Cloud agent** → enable and save.
- **Base branch:** when delegating from the **Agents page**, you can pick a base branch other than `main`. The agent branches from it.
- **Layered control:** repository scope defines *where* the agent operates. Custom agent config (`applyTo`, `tools`) defines *what* it can access and do inside that boundary.

**What custom agents control vs. don't control:**
| Custom agents DO define | Custom agents do NOT define |
| :--- | :--- |
| Files to focus on (`applyTo`) | Branch creation |
| Actions they can perform (`tools`) | Pull request behavior |
| Behavior (instructions) | Execution isolation |

> Branch-based scope is **always enforced by the execution context**, not by the custom agent. With the cloud agent, the system creates the branch. In CI, the workflow determines the branch.

**Invoking an agent from a workflow** (the workflow becomes the execution boundary):
```yaml
on:
  workflow_dispatch:
  schedule:
    - cron: '0 9 * * *'
permissions:
  contents: read
jobs:
  agent-task:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '18'
      - name: Run custom agent
        env:
          COPILOT_GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          npx @github/copilot-cli \
            --agent security-reviewer \
            -p "Review this code for vulnerabilities" \
            --no-ask-user
```
- `-p`: prompt
- `--agent <name>`: use a custom agent from `.github/agents/`
- `--no-ask-user`: non-interactive (optional)
- `COPILOT_GITHUB_TOKEN`: authentication

**Guardrails in GitHub Agentic Workflows** (defense in depth; the full list):
1. Read-only tokens by default
2. **Safe outputs:** the agent proposes; a separate gated step decides what's allowed
3. **Zero secrets in the agent process**
4. **Sandboxed, containerized execution**
5. **Network isolation with allowlisted outbound access**
6. **Threat detection that scans proposed outputs before any write action**

These target overprivileged agents, **prompt injection**, and unintended repo changes.

### 3.7 Agent execution limits and protections (NEW)

**Platform limits on Copilot cloud agent:**
- Access **only to the repository it works in**
- Changes go on a **separate branch**, never directly on the default branch
- **It doesn't automatically create or merge a PR.** It prepares changes, and *you* decide whether to create the PR, request updates or discard the work.
- Repo/org settings control **which workflows are allowed, which actions can run, and what `GITHUB_TOKEN` may do**

**Execution safeguards:**
| Safeguard | Implementation |
| :--- | :--- |
| **Error handling** | Fail fast (`continue-on-error: false`), log meaningful errors, prevent partial/inconsistent changes |
| **Retries** (transient: network etc.) | Rerun failed steps, retry logic in scripts, design for safe re-execution |
| **Rollbacks** | Built in through branch isolation and PR review; close/discard the PR, or **revert commits** if already merged |
| **Escalation paths** | Required PR review, auto-assigned reviewers, workflow steps that notify maintainers |
| **Traceability** | Workflow logs, commit history, PR discussions; clear commit messages; branch-scoped changes |

```yaml
- name: Run agent task with retry
  run: |
    for i in 1 2 3; do
      npx @github/copilot-cli -p "Run task" && break
      sleep 5
    done
```
The four outcomes: **Resilient · Controlled · Auditable · Human-governed**

**Environment protections:** require approvals before jobs continue, restrict secret access, and control deployment targets.

**Session visibility:** monitor logs, inspect actions, and send follow-up prompts during execution.

> ⚠️ **High-value exam fact: trigger behavior**
> - Actions performed with **`GITHUB_TOKEN` mostly do NOT trigger new workflow runs**. This prevents unintended loops and recursive execution.
> - **GitHub App tokens or PATs CAN trigger extra workflow runs.** That's more flexible, but you must design against **recursive executions / automation loops**.

---

## MODULE 4 ADDITIONS: MULTI-AGENT SYSTEMS & ORCHESTRATION

### ➕ 4.1 Responsibility mapping (5 stages, including Acceptance)
| SDLC stage | Multi-agent responsibility | Reviewable artifact |
| :--- | :--- | :--- |
| Planning | Goal, scope, success criteria, risks | PR plan section or **`PLAN.md`** |
| Implementation | Changes in an isolated branch | Branch + commits + PR |
| Validation | Evidence and results | Actions runs + checks + artifacts |
| **Acceptance** | Policy and human judgment | CODEOWNERS + reviews + required checks |
| Deployment | Gate high-risk execution | Environments + approvals |

**Scope rules:**
- **Dependency agent:** manifests and lockfiles only. It avoids changing application behavior.
- **Refactoring agent:** `src/` only. It does **not** touch manifests, lockfiles or workflows.
- **Security agent:** validates outcomes and produces reports. It may propose changes but does **not** broaden into refactoring unless the task is explicitly a code security fix.
- If agents act as general developers across the whole repo, the result is **repeated collisions, inconsistent review routing and uncontrolled risk**.

Overlap produces **duplicated work, conflicting PRs and unclear ownership**. Assign each agent a narrow role, limit scope **by path and artifact type**, and define **completion signals** verifiable through checks and reviews.

### ➕ 4.2 Orchestration details
- **Typical orchestration triggers:**
  - **schedules** for periodic work (reports, dependency checks)
  - **pull request events** for validation and iteration
  - **workflow completion (`workflow_run`)** when one step must follow another
- **Sequential pipeline example:** dependency agent opens PR → CI validates → security validation runs after CI completes → human approves → merge only when gates are satisfied.
- **Parallel orchestration requires isolation.** It's only appropriate when scope boundaries prevent overlap. If agents can collide on the same files, **parallelism increases instability rather than throughput**.
- The course's fan-in example also adds **job-level concurrency** on the merger job:
  ```yaml
  plan_merger:
    needs: [spec_analyzer, risk_reviewer]
    concurrency:
      group: multiagent-${{ github.ref }}   # no overlapping merge jobs per branch
  ```

**Artifact-based coordination** (preferred over direct "agent-to-agent communication"):
1. Run the agent with **restricted permissions**
2. Produce a **structured output** (plan/report/proposal) as an **artifact**
3. Use a **controlled step** to apply only the operations the workflow allows

This creates an explicit boundary **between "reasoning" and "writing"** and leaves evidence.

```yaml
name: Daily Repo Status Report
on:
  schedule:
    - cron: "0 2 * * *"
permissions:
  contents: read
  issues: write
  pull-requests: read
jobs:
  report:
    runs-on: ubuntu-latest
    steps:
      - run: echo '{ "summary": "Daily status...", "links": [] }' > report.json
      - uses: actions/upload-artifact@v4
        with:
          name: repo-status-report
          path: report.json
      - name: Create issue (controlled output)
        run: echo "Create issue from report.json"
```

- **Hidden orchestration** (coordination outside GitHub, leaving no evidence in PRs or runs) makes failures impossible to diagnose and reduces trust.
- Knowledge-check answer: the most effective coordination primitive is **PRs and their surrounding artifacts (checks, reviews, history)**. Private agent-to-agent messaging is not.

### ➕ 4.3 Execution isolation (4 kinds)
1. **Branch isolation:** a dedicated branch per agent, for example `agent/dependency/<ticket>`, `agent/refactor/<ticket>`, `agent/security/<ticket>`.
2. **Workflow isolation:** a dedicated workflow (or a dedicated job with distinct permissions) per agent, which reduces accidental coupling.
3. **Permission isolation:** for example `contents: read` + `pull-requests: write` for a workflow that updates PR metadata but shouldn't push commits.
4. **Concurrency controls:** see `STUDY.en.md` §4.3.

**Why not job-level or matrix concurrency?**
- **Job-level `concurrency`** applies only *within* a workflow run, not across runs.
- **`strategy.matrix`** controls intra-run parallelism, not parallelism across triggers or agent sessions.

Without isolation you get **interleaved commits, ambiguous ownership and repeated failures**, which makes rollback and auditing much harder. Isolation is "not only about merge conflicts; it's about preventing instability (thrashing)".

### ➕ 4.5 Conflict types and escalation triggers
**Four conflict types:**
| Type | Meaning |
| :--- | :--- |
| Textual merge conflict | Same files/lines changed |
| **Semantic conflict** | **Clean merge, broken combined behavior** |
| Policy conflict | Protected areas require different reviews/approvals |
| Duplicate effort | Two PRs solve the same problem differently |

- A merge validation check only becomes enforceable when it's a **required check**. Then detection no longer depends on reviewers noticing.
- **CODEOWNERS** is the arbitration tool for sensitive paths in multi-agent systems.

**Escalation triggers (any of these):**
- A PR **conflicts twice** after rebase attempts
- Required checks **fail twice with the same failure signature**
- **Two agents propose incompatible fixes to the same alert**

The escalation report says **what conflicted, what was attempted and which options exist**.

Without arbitration, outcomes are decided by **timing rather than correctness** ("first merge wins").

### 4.8 Observability, attribution and handoffs (NEW)
**Practical goal:** every meaningful step leaves a durable trace:
- a PR that links to context and states intent
- checks/runs that produce evidence
- artifacts and logs that explain outcomes
- **clear attribution (titles, labels, owners)**

As the number of agents grows, traceability becomes a primary requirement. Reviewers need to know which agent produced a change, what decision was made, what evidence supports it, and what happened next.

**Attribution conventions:**
- PR title: `[agent: dependency] Update <package> to <version>`
- Labels: `agent: dependency`, `agent: security`, `agent: refactor`
- PR body sections: Plan, Evidence, Risks, Rollback/Escalation

**Post-hoc analysis.** Artifacts are the **primary evidence source even when live logs are incomplete**:
1. Open the workflow run in the **Actions** tab
2. Scroll to the **Artifacts** section at the bottom of the run summary
3. Download the artifact (for example `agent-report`)

If artifacts are missing, search the org audit log for `action:artifact.destroy`. It shows **who** deleted the artifact, **when**, and **which repository**.

**Handoff PR template:**
```md
## Objective
## Plan
## Evidence
- CI run:
- Scan outputs:
- Relevant issue/alert:
## Decisions and handoffs
- Decision:
- Rationale:
- Next owner (if escalation needed):
## Risks and rollback
```

### 4.9 Failure modes and recovery at scale (NEW)
**Multi-agent failures are often *coordination* failures:**
| Failure mode | Symptom |
| :--- | :--- |
| **Partial execution** | PR exists, but evidence or validation is missing |
| **Stalled workflows** | Checks fail repeatedly or approvals never arrive |
| **Conflicting outputs** | PRs compete and block each other |
| **Flapping** | Workflows rerun repeatedly with no convergence |

> Knowledge-check: **two agent PRs that repeatedly conflict because they change the same files** = coordination failure. A single test failing once is not.

**Diagnose with GitHub-native evidence:**
- **PR timelines:** what changed and when
- **Required check results:** what failed and how often
- **Workflow run history:** patterns of failures and cancellations
- **Artifacts:** reports and logs

**Recovery:**
- **Bounded retries:** the agent revises the branch, but only within limits
- **Escalation threshold:** same required check fails twice → stop and escalate with links and a summary
- **Rollback readiness:** small, scoped PRs; revert when risk increases

**Interpreting a policy-blocked action (preToolUse hook output):**
```
Error: Command blocked by policy
Reason: destructive_operation_detected
[agent] Escalating to human review...
```

**Orchestration gotchas:**
- `disable-model-invocation: true` on an agent means it **can't be invoked as a subagent**, which **causes orchestration failures** if a parent tries to hand off to it.
- `handoffs` resolve to subagents **by the `name:` attribute in the agent YAML, or by matching filename**.
- `agents:` lists the subagents allowed. `send: true` auto-submits the handoff prompt. `model:` overrides the model.

**Failure-aware design rules:**
1. Assume failure at every stage
2. Define clear retry limits
3. Escalate when automation can't converge
4. Design changes to be reversible

A system that assumes success produces endless loops, compounding failures, and reactive human intervention.

---

## MODULE 5 ADDITIONS: MEMORY, STATE & EVALUATION

### ➕ 5.1 Memory: what to store where

**Where each kind of information goes:**
| Information | Store it in |
| :--- | :--- |
| Requirements & acceptance criteria | Issue / PR description |
| Plans & decisions | Same places (PR, docs), so work continues without reinterpretation |
| **Repeatable processes** | **Instructions or reusable skills** |

**Scope memory:** store only what affects the outcome (requirements and constraints, decisions affecting implementation, validation/testing approach). **Don't store** temporary intermediate steps or duplicated context. Limiting memory reduces confusion and stale information.

**Single source of truth per information type:**
| Type | Source of truth |
| :--- | :--- |
| Requirements | Issue |
| Decisions | PR or documentation |
| **Validation rules** | **Repository instructions** |
| Results | Workflow logs and artifacts |

- Long-term memory = **curated, summarized or structured** knowledge (key decisions, patterns).
- External memory = **the most reliable source of truth** (knowledge-check answer), because it is persistent and reviewable.

### 5.1b Memory maintenance: expiration, pruning, summarization, reset (NEW)
| Rule | Meaning | GitHub practice |
| :--- | :--- | :--- |
| **Expiration** | Some memory is kept only for a limited time | Logs/artifacts are kept **90 days by default**, configurable at **repo, org or enterprise** level (public 1–90 days; private up to 400) |
| **Pruning** | Remove outdated or unnecessary artifacts | Delete artifacts manually from the **Actions tab**, remove stale runs, avoid large or redundant outputs. **Deleted artifacts can't be restored.** |
| **Summarization** | Reduce detailed history to key points + references | Update the PR description with final decisions, **reference key commits**, **link to runs instead of storing full logs** |
| **Reset rules** | Prevent incorrect carryover | Triggered when requirements change significantly, a new approach is chosen, or assumptions become invalid. **Rewrite the PR description, close and recreate the PR if needed, document the new direction first.** |

### ➕ 5.2 State: capture and resume
**Capturing state as durable artifacts:**
- issue = requirements and acceptance criteria
- PR = tracks implementation
- **commits = incremental progress**
- **workflow runs = validation results**

**The PR as a state anchor should include:**
- the task description
- acceptance criteria or an issue link
- a plan summary
- **updates as work progresses** (update the description when decisions change, and reference commits and runs directly)

**Resume flow (5 steps):**
1. Open the existing PR
2. Review its description and linked issue
3. Check the commits already made
4. Review workflow results under the **"Checks" tab**
5. Continue from the latest state

This avoids repeating completed work.

### ➕ 5.3 Correcting drift (source wording)
- **Detect:**
  - do the PR changes satisfy the acceptance criteria?
  - do commits contradict earlier decisions?
  - are workflow checks **failing or missing**?
- **Correct:**
  - re-read the issue/PR description
  - compare changes with the acceptance criteria
  - update the PR description if needed
  - **re-run workflows or push new commits to trigger validation**

### 5.3b Continuity across tools and environments (NEW)
Work moves between **IDE → CLI → GitHub-hosted environment**. Share state with **durable references, not copied context**:
- **PR numbers and branch names**
- **Commit SHAs**
- **Workflow run links**
- **Issue and PR URLs**

Rules:
- **Never keep critical information only in prompts or chat history.** Write important updates to issues or PRs.
- When switching environments, always **re-anchor to GitHub state**: start in the IDE → open or reference the PR → continue in CLI/automation → validate with workflows → finalize in the PR.

**Conflicting vs. stale context (know the difference):**
| | Conflicting context | Stale context |
| :--- | :--- | :--- |
| **Definition** | Same info exists in multiple places **with different values** | **Outdated** info used during execution |
| **Causes** | Duplicated requirements/decisions; acceptance criteria redefined in several prompts | PR branch behind base; workflow results no longer match the current code; requirements changed but not updated |
| **Prevention** | One source of truth per info type; **update the original, don't create copies** | **Keep the branch up to date with base**; review the latest commits/runs before changing anything; update issues/PRs when requirements change |
| **GitHub enforcement** | – | Required status checks + branch protection that **requires branches to be up to date before merging** |

### ➕ 5.5 Evaluation signals and quality gates
- **Success criteria live in the issue** (written as acceptance criteria) and are referenced in the PR.
- **Configuring required checks:** branch protection → enable **"Require status checks to pass before merging"** → select the specific checks. You can optionally require branches to be **up to date** before merging.
- **Security evaluation** includes:
  - **code scanning**
  - **dependency review**
  - **secret scanning and push protection**
  - **Treat security alerts or failed checks as blockers**
- **Rules and protections:** require at least one approving review, combine reviews with required checks, and prevent direct pushes to protected branches.

**End-to-end evaluation flow (7 steps):**
1. Issue defines the task and criteria
2. Agent creates a branch and PR
3. Workflows run automatically
4. Status checks appear in the PR
5. Required checks must pass
6. Reviewer approves
7. Merge

### ➕ 5.6 Analyzing failures and improving behavior
**Compare intent with results:**
- Intent lives in the **issue (requirements) and PR description (plans/decisions)**.
- Results live in **commits/code and workflow outputs/logs**.

The comparison tells you whether the agent **misinterpreted the task, implemented a wrong solution, or failed during execution/validation**.

**Fix by area:**
| Area | Fixes |
| :--- | :--- |
| **Prompts & instructions** | Clarify acceptance criteria, add constraints, **update repository instruction files** |
| **Memory & state** | Clearer decisions in issues/PRs, remove outdated/conflicting context, keep a single source of truth |
| **Tool configuration** | Update `.github/workflows/`, correct triggers (push, pull_request), verify permissions and required checks |

**Feedback loop:**
1. Run the agent
2. Observe failures through logs and artifacts
3. Identify the root cause
4. Fix prompts / memory / tools
5. Re-run the workflow

Keep every improvement **traceable**: document it in PR updates, reference commits and runs, and keep changes scoped.

> Knowledge-check traps: improving agent behavior means **adjusting prompts, memory structure or workflow configuration**, *not* "rerun without changes". The most useful failure artifacts are **workflow logs, workflow runs and PRs**.

---

## MODULE 6 ADDITIONS: GOVERNANCE, GUARDRAILS & OPERATIONS

### ➕ 6.1 Risk-based autonomy: full model

**Risk depends on three factors:**
1. **Where** the change is applied
2. **How easily it can be reversed**
3. **How quickly it affects users or systems**

**Four autonomy levels:**
| Level | Agent may… |
| :--- | :--- |
| **Read-only** | Inspect, summarize, classify, recommend. No modifications. |
| **Propose-only** | Create branches and PRs. **Can't merge or deploy.** |
| **Execute with guardrails** | Run **pre-approved** workflows (tests, builds, **staging** deploys) within limits |
| **Human-authorized execution** | High-impact actions (prod deploy, workflow changes, secret access) **only after human approval** |

Autonomy isn't one setting. You combine PR rules, environments, workflow permissions and tool access.

- In the Governance module's risk table, **Critical = environment gate + explicit reviewers + audit evidence required**.
- Use **full automation only when failures are reversible.**
- **`.github/workflows/`, `infra/` and `security/` are high-risk by default.** These are "small diff, big consequence" areas.

**Risk-based routing:** the plan's risk rating is a **machine-readable signal** that decides the execution path. **Don't rely on narrative explanations of risk.**
```yaml
jobs:
  plan:
    runs-on: ubuntu-latest
    outputs:
      risk: ${{ steps.read.outputs.risk }}
    steps:
      - uses: actions/download-artifact@v4
        with: { name: plan, path: out }
      - id: read
        run: echo "risk=$(jq -r .risk out/plan.json)" >> "$GITHUB_OUTPUT"
  apply:                       # anything not low → human approval
    needs: plan
    environment: approval-required
    if: ${{ needs.plan.outputs.risk != 'low' }}
    runs-on: ubuntu-latest
    steps:
      - run: ./scripts/apply.sh out/plan.json
  apply_auto:                  # low → automatic
    needs: plan
    if: ${{ needs.plan.outputs.risk == 'low' }}
    runs-on: ubuntu-latest
    steps:
      - run: ./scripts/apply.sh out/plan.json
```

- **For terminal agents (Copilot CLI), tool access is the primary governance boundary.** Allow read-only tools by default and gate write, execution and privileged operations. *Match tool access to consequence: low-risk tasks shouldn't inherit high-risk capabilities.*

**Progressive autonomy** (start strict, relax as reliability is proven):
| Phase | Agent capability |
| :--- | :--- |
| 1 | Open PRs only, can't merge |
| 2 | Merge **low-risk** PRs after checks |
| 3 | Deploy to **staging** automatically |
| 4 | Deploy to **production only through environment approval** |

### 6.2b Enforcement controls (NEW detail)
**Enforcement control set:** rulesets/branch protection, required checks, CODEOWNERS, environments, and guardrail workflows.

**Ruleset / branch protection settings for `main`:**
- PR required to merge
- Required checks must pass
- Required approving reviews (number per risk level)
- **Require CODEOWNERS review** (for sensitive paths)
- Restrict direct pushes
- **Block force pushes and branch deletion**

**Required checks map to governance goals:**
| Check | Goal |
| :--- | :--- |
| Build/unit tests | Quality |
| Security scans | Risk |
| Policy checks for workflow/infra changes | Governance |

> ⚠️ **Treat renaming or removing required checks as high risk: "if checks drift, governance drifts."**
> ⚠️ **If "require CODEOWNERS review" isn't enabled, CODEOWNERS is advisory only.**
> ⚠️ If a workflow accesses **production secrets**, treat it as **critical** risk and gate it.

**Environments:** require reviewers for prod deploys, **restrict production secrets to the production environment only**, and keep a deployment/approval record.

- **Hooks vs. logging:** *use enforceable hooks for blocking. Logging and banners are helpful, but they don't prevent execution.*
- **The guardrail workflow** in the source has an **extra first step** that `STUDY.en.md` omits. It fails outright if the PR **author** is the Copilot bot:
  ```yaml
  - name: Fail if PR is authored by Copilot agent
    if: ${{ github.event.pull_request.user.login == 'github-copilot[bot]' }}
    run: |
      echo "PRs authored by github-copilot[bot] must be opened/owned by a human."
      exit 1
  ```
  Purpose: agent PRs can't merge automatically, **only human approvals count**, and review requirements **can't be satisfied by automation identities**. It's *defense in depth*: you still need branch protection and CODEOWNERS, but this enforces rules that settings alone can't express.

**Layered enforcement model:**
| Layer | Mechanism |
| :--- | :--- |
| **Pre-action** constraints | Permissions |
| **In-action** validation | Checks |
| **Post-action** traceability | Logs, artifacts |

- **"If a control isn't enforced by the platform, treat it as optional."**
- **"Controls in docs only" is an anti-pattern.** If the platform can't enforce it, it will be bypassed. Agents operate at scale and speed, so governance that relies on human behavior alone will fail.

### 6.3b Human-in-the-loop workflows (NEW)
**HITL flow:**
1. Agent creates a PR (**including plan and risk level**)
2. Checks validate
3. CODEOWNERS auto-requested
4. Merge after approvals and checks

**Put humans at decision points (merge, deploy, secret access), not at every step (analysis, formatting, routine checks).**

- Production approvals should be **explicit, auditable and owned by accountable roles**.
- **Prevent overlapping production deployments** (serialize them):
  ```yaml
  concurrency:
    group: production
    cancel-in-progress: true
  ```
  Note the **fixed group name `production`**, unlike the per-branch `${{ github.workflow }}-${{ github.ref }}` used for PR CI.
- **Tool-based approval boundaries:** automate low-risk tools and keep high-risk tools available but approval-gated at the time of use:
  ```bash
  copilot agent run CodeAgent --allow-tool 'read,search'
  ```
  Reading and searching are auto-approved. Edit and execute still prompt for approval.

**Avoid governance fatigue** (keep oversight without slowing everyday work):
- **Require evidence** (tests, scans, artifacts) so review is fast
- **Route reviews via CODEOWNERS** so reviewers have context
- **Keep PRs small and scoped**
- **Require a rollback plan** for high-impact changes

Agents don't carry responsibility for outcomes. Humans provide judgment for decisions that can't be fully validated by automated checks.

### ➕ 6.2 Least privilege: extra rules
- **`pull-requests: write` is an elevated capability.** Grant it only when the workflow must create or update PRs.
- **Only allow write where required, and document why.**
- Additional controls:
  - restrict secrets using **environments**
  - **isolate workflows** so high-risk jobs don't share permissions with low-risk jobs
  - **minimize third-party actions and pin versions**
- *Permissions define the true boundary of agent power*, regardless of intent or instructions. Broad tokens turn small mistakes into large incidents.

### 6.4b Observability as a governance requirement (NEW)
**Every meaningful action must produce:**
- PR + commit history
- Workflow results (**job logs, time, actor**)
- Uploaded artifacts (**plan, test results, execution report**)
- Approval and merge events
- **Environment approval record** (for production)

Without durable evidence you can't debug reliably, investigate incidents, prove compliance, or trust autonomous changes over time.

**Evidence-first workflows:** each critical workflow outputs:
- test results
- scan reports
- **`plan.json`** (machine-readable)
- **`execution-report`** (machine-readable summary)

Artifacts must be **retained long enough for audits and incident response**.

> **"Missing evidence = failure." If a change can't be audited, it shouldn't be merged.**

### ➕ 6.5 Operational governance: the rest of the unit
- **Agent lifecycle:** **deploy → monitor → update → retire**. Both agents and guardrails evolve. Required: **clearly defined ownership, runbooks and regular review cadences**.
- **Governance drift is inevitable.** Causes:
  - checks renamed or removed
  - review requirements relaxed
  - **CODEOWNERS outdated**
  - permissions expanded
  - **secrets moved into broader scopes**

  Treat governance as an ongoing operational responsibility with periodic reviews.
- **Prevent ambiguity before execution.** Before assigning work, define:
  - acceptance criteria
  - **constraints and non-goals**
  - **specific files/paths**
  - validation and rollout expectations

  > **"If a task can't be defined precisely, it shouldn't be executed autonomously."**
- **Recovery strategies:**
  - Retry **transient** failures (bounded retries)
  - **Escalate** after repeated failures
  - **Rollback** quickly using small PRs and safe revert paths
  - **Investigate security failures instead of repeatedly retrying them** ⚠️

### ➕ 6.6 Anti-patterns: why they fail and how to fix them
| Anti-pattern | Example | Why it fails | Mitigation |
| :--- | :--- | :--- | :--- |
| Unbounded autonomy | No approval for prod deploys | Irreversible changes without oversight | Environments + required reviewers + rulesets |
| Excess permissions | Token can write-all and read-all secrets | Small mistake becomes a major incident | Least privilege + env scoping + **job-level** permissions |
| Missing audit trail | No artifacts, only console logs | **Can't prove what happened** | Artifact uploads + **evidence-first** workflows |
| Bypass paths | Direct push to main, disabled checks | Policy can be skipped | Branch protection/rulesets + restrict push |
| Rubber-stamping | Approvals become "click to unblock" | Humans stop reviewing | **Better evidence + CODEOWNERS + smaller PRs** |

---

## HANDS-ON EXERCISES (WHAT TO KNOW)

### Exercise 1: Automate repository updates with GitHub Agentic Workflows (Module 3)
- Install the **`gh aw`** GitHub CLI extension and run the repo setup commands.
- **Commit the setup on a branch → open PR → merge to `main`.** *Agentic workflows run from the configuration on the default branch.*
- Write an agentic workflow **in Markdown** that reads notes plus the GitHub Blog and Changelog, drafts website updates, and **opens a PR** with a summary of sources.
- A good workflow definition states:
  - its **purpose**
  - **which files it may modify**
  - **sources to consult**
  - the **expected output format**
  - the **review process**
- Run it **with the GitHub CLI**. Then verify the PR was created by the workflow, changes are **limited to the intended files**, and the output is suitable for **human review before merge**.
- Designed for **public** repo copies. Private copies may need extra token/policy configuration.

### Exercise 2: Build an AI "dream team" with Copilot CLI custom agents (Module 4)
- Runs in **GitHub Codespaces** with **Copilot CLI**.
- The custom agents in **`.github/agents/`** are `orchestrator.agent.md`, `planner.agent.md`, `designer.agent.md` and `coder.agent.md`:

| Agent | Role |
| :--- | :--- |
| **Orchestrator** | Coordinates the other agents (delegates) |
| **Planner** | Breaks the project into implementation phases |
| **Designer** | Defines visual structure and UX |
| **Coder** | Implements the files |

- Flow:
  1. Ask the Orchestrator to involve the Planner and create a plan
  2. Delegate design to the Designer
  3. Delegate implementation to the Coder
  4. Validate the result
  5. Ask the Orchestrator to **summarize the coordinated handoff**
- Output:
  - `app/index.html`, `app/styles.css`, `app/project-data.json`
  - `.vscode/launch.json`
  - planning and handoff notes in `docs/`
- Don't modify workflow files: they grade the exercise.

---

## OFFICIAL KNOWLEDGE-CHECK QUESTIONS WITH ANSWERS

The source files list options without marking the correct one. The answers below are the clearly correct options, based on the course content.

**Foundations**
1. Best indicator an AI is acting as an agent → **It opens a PR from a branch it created.**
2. Why GitHub is a system of record → **It stores plans, commits, PR discussion and workflow evidence.**
3. Control that requires the right reviewers for sensitive paths → **CODEOWNERS.**
4. Example of hidden reasoning → **A diff with no plan, assumptions or execution context.**
5. What reviewers evaluate first under the contributor model → **Whether the change meets the repo's definition of done (scope, checks, review, policy).**

**Design architecture**
1. Most reliable way to stop planless execution from merging → **Plan check as a required status check + required PR reviews** (not "template only").
2. Feature that routes reviews by changed path → **CODEOWNERS.**
3. Where evaluation evidence should live → **GitHub-native artifacts: workflow runs, checks, uploaded artifacts.**
4. Risk-based autonomy for prod deploys → **Environments with required reviewers.**
5. Architectural anti-pattern → **Mixed planning and execution with no inspectable plan.**

**Tooling / MCP / execution**
1. Where agents execute → **Within workflows powered by GitHub Actions.**
2. How changes are isolated → **A separate branch.**
3. What determines what an agent can do → **Workflow permissions and `GITHUB_TOKEN` scope.**
4. Purpose of a PR → **A place to review and validate before merging.**
5. How workflows trigger after an agent updates code → **Events such as push or pull_request.**
6. Role of an MCP server → **Expose tools and services that agents can use.**
7. What controls which MCP servers can be used → **Registries and allow lists.**
8. Why environment protections → **Require approvals and protect sensitive operations.**
9. Effect of least privilege → **Limits actions to only what is required.**
10. How agent actions stay visible → **Workflow logs and PR review.**

**Multi-agent**
1. Most effective coordination primitive → **PRs and surrounding artifacts (checks, reviews, history).**
2. Preventing overlapping runs on frequent PR updates → **Concurrency with cancel-in-progress.**
3. Routing review for sensitive paths → **CODEOWNERS (with a required-reviews policy).**
4. Coordination failure (vs individual) → **Two agent PRs repeatedly conflicting on the same files.**
5. Safe pattern for prod deploys → **Environments with required reviewers so jobs pause for approval.**

**Memory / state / evaluation**
1. Most reliable source of truth → **External memory in GitHub artifacts (issues, PRs).**
2. Primary role of a PR → **Central place to track progress, decisions and validation results.**
3. Context drift → **Agent's actions no longer align with the original goal or prior decisions.**
4. Ensures validation passes before merge → **Required status checks.**
5. Most useful artifacts for failure analysis → **Workflow logs, workflow runs and PRs.**
6. Improving behavior after failure → **Adjust prompts, memory structure or workflow configuration.**

**Governance**
1. Low-risk read-only CLI task (summarize commits) → **Scope tool access to read-only Git inspection** (`--allow-tool 'shell(git)'`).
2. Explicit approval before prod workflows access prod secrets → **Protected environment with required reviewers.**
3. Least-privilege `GITHUB_TOKEN` pattern → **Read-only default; elevate only for the job that writes.**
4. Prevent overlapping prod deploys and cancel in-progress → **Concurrency with a shared group + cancel-in-progress.**
5. Route review for `.github/workflows/` and `infra/` → **CODEOWNERS (with a required-reviews policy).**

---

## RAPID-FIRE EXAM FACTS

These facts come only from this extension; `STUDY.en.md` doesn't cover them.

- `GITHUB_TOKEN` actions **don't trigger new workflow runs** (loop protection). **PAT / GitHub App tokens can**, which creates a recursion risk.
- Copilot cloud agent **does not auto-create or auto-merge PRs**. A human decides.
- Copilot cloud agent runs in a **GitHub Actions-powered environment** and is **repo-scoped**. Enable it via *Settings → Copilot → Cloud agent*.
- The custom agent `applyTo`/`tools` keys define focus and capability. **Branching, PR behavior and isolation are controlled by the execution context.**
- API authentication options: **PAT, GitHub App token, `GITHUB_TOKEN`**.
- Agentic workflow = **frontmatter (triggers, permissions, tools, safe-outputs) + Markdown intent → compiled lock file**. It **extends**, not replaces, CI/CD.
- Agentic workflow guardrails: read-only token, safe outputs, zero secrets, sandbox/container, **network allowlist**, **threat detection on outputs**.
- Remote MCP is **recommended**. GHES = local only.
- MCP allow lists are **org/enterprise** level, tied to the **Copilot seat**, and take effect **immediately**.
- MCP tool expansion = review it like a **high-risk dependency**. Prefer **narrow tool subsets** over wildcards.
- The agent runtime **does not automatically inherit repo CI secrets**.
- Hooks: **pre-action = block**, **post-action = log**, **error = escalate**. Logging and banners **don't prevent** execution.
- Deploy sensitive configuration from **explicit commit/tag**, not branch head.
- Instructions are *guidance*. **Tool allowlists and gates are *enforcement***.
- Four autonomy levels: **read-only → propose-only → execute with guardrails → human-authorized**.
- Progressive autonomy: **PRs only → merge low-risk → auto staging → prod via environment approval**.
- Risk = **where + reversibility + speed of impact**. Route on a **machine-readable** risk value (`plan.json`), not narrative.
- **Renaming or removing required checks = high risk.** CODEOWNERS without "require CODEOWNERS review" is **advisory**.
- Prod deploy serialization: `concurrency: { group: production, cancel-in-progress: true }`.
- `pull-requests: write` = **elevated**. Pin third-party action versions.
- **Missing evidence = failure.** Evidence must tie to a **specific run + specific commit**.
- Conflict types: **textual, semantic, policy, duplicate effort**.
- Escalate when: **conflict twice after rebase**, **same check fails twice with the same signature**, or **two agents propose incompatible fixes to the same alert**.
- Coordination failure modes: **partial execution, stalled, conflicting outputs, flapping**.
- Job-level concurrency applies **within** a run only. A matrix controls **intra-run** parallelism.
- `disable-model-invocation: true` → can't be a subagent → **orchestration failure** if a parent hands off to it. Handoffs resolve by **`name:` or filename**.
- Memory maintenance: **expiration, pruning, summarization, reset rules**. Deleted artifacts **can't be restored**.
- Share state across tools with **durable references** (PR #, branch, SHA, run link, URL), never chat history.
- **Conflicting** context = same info, different values. **Stale** context = outdated info.
- **Repeatable processes** go into **instructions or skills**. **Validation rules** go into **repository instructions**.
- Security evaluation = **code scanning + dependency review + secret scanning/push protection**, treated as **blockers**.
- **Investigate security failures; don't retry them.**
- "If a task can't be defined precisely, it shouldn't be executed autonomously."
- "Put humans at decision points (merge, deploy, secret access), not at every step."
