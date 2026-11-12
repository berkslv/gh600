# GitHub Certified: Agentic AI Developer (GH-600) - Mock Exam (EXAM.en.md)

This is a **full-length mock exam** written at real-exam difficulty for **Course GH-600T00-A: Developing in Agentic AI Systems** and the **GitHub Certified: Agentic AI Developer** certification. All of the questions are new. None of them repeat `QUESTIONS.en.md`.

**How to take it like the real exam**

- **60 questions**. Allow **100 minutes** and do not pause the clock.
- Aim for a score of **42/60 (70%)** or higher. This is only a rough guide to readiness and is not the official cut score.
- Cover each answer block before you read the question, and write down your answer before you uncover it.
- Formats: single choice, multiple choice ("select two/three"), code and YAML analysis, ordering, Yes/No statement series, and a case study at the end (Q55–Q60).
- An answer key with a domain breakdown is at the bottom so you can find weak areas.

| Domain | Questions |
| :--- | :--- |
| D1 – Foundations of agentic AI in GitHub | Q1–Q8 |
| D2 – Agent architecture & SDLC integration | Q9–Q18 |
| D3 – Tooling, MCP & execution environments | Q19–Q30 |
| D4 – Multi-agent systems & orchestration | Q31–Q40 |
| D5 – Memory, state & evaluation | Q41–Q48 |
| D6 – Governance, guardrails & operations | Q49–Q54 |
| Case study – Contoso Payments (mixed) | Q55–Q60 |

---

## Domain 1 – Foundations of Agentic AI in GitHub

### Question 1 (Multiple Choice - Select Two)
An architect is explaining to leadership how GitHub serves as both a **System of Record** and a **Control Plane** for agent work.

Which **two** capabilities belong to the **Control Plane** role, not to the System of Record role? (Each correct answer presents a complete solution.)

A) A required status check prevents a pull request from merging until the test workflow succeeds  
B) Commit history preserves which identity changed which lines and when  
C) A deployment job targeting the `production` environment pauses until a designated reviewer approves it  
D) An issue retains the original problem statement and acceptance criteria  
E) Uploaded workflow artifacts keep test reports available for later forensic review  

> **Correct Answer:** **A and C**  
> **Explanation:** The Control Plane **enforces** policy before something happens. Required status checks, rulesets, CODEOWNERS enforcement and environment approvals are all control-plane functions. B, D and E **record** what happened (lineage, intent, evidence), which is the System of Record role.

---

### Question 2 (Single Choice - Anti-Pattern Identification)
An agent opens a pull request with a small, well-bounded diff. The PR description includes a short "Plan" section listing three steps. During review, an engineer notices that the agent removed a retry wrapper around an HTTP client. Nothing in the PR explains why: no assumptions, no linked workflow runs, and no decision notes. All checks are green.

Which anti-pattern does this **most precisely** describe?

A) Planless execution  
B) Over-permissioned agent  
C) Hidden reasoning  
D) Context drift  

> **Correct Answer:** **C**  
> **Explanation:** A plan exists, so this is not *planless execution*. The diff is bounded, so it is not *drift*. What is missing is the **decision trail**: the assumptions, the rationale and the linked evidence. That is *hidden reasoning*. The mitigation is to require plan artifacts and linked workflow runs, and to record decision points in PR comments or artifacts.

---

### Question 3 (Single Choice - Contributor Model Rubric)
The linked issue for an agent-authored PR says: *"Fix session timeout calculation in `src/auth/session.ts`."* The diff modifies `src/auth/session.ts` **and** `.github/workflows/deploy.yml`. Checks pass and the plan section only mentions the session fix.

Which dimension of the practical review rubric is **primarily** violated?

A) Intent  
B) Scope  
C) Evidence  
D) Rollback  

> **Correct Answer:** **B**  
> **Explanation:** Intent is clear because the change is linked to an issue, and evidence exists because checks passed. The problem is that file changes are **not confined to the agreed plan**, which is a scope violation. Because the extra change touches `.github/workflows/`, it is also high-risk and should trigger CODEOWNERS routing.

---

### Question 4 (Single Choice - Responsibility Model)
A platform team writes: *"Because the agent made the change, accountability for defects in agent PRs belongs to whoever maintains the agent's prompt."*

Which statement correctly reflects the GH-600 responsibility model?

A) The statement is correct; prompt maintainers own all agent outcomes.  
B) Accountability is shared between the GitHub App identity and the reviewer.  
C) Responsibility does not move with execution; the humans who define the task, scope permissions, configure controls and approve or merge remain accountable for the outcome.  
D) Accountability transfers to the agent once required checks pass, because the system validated it.  

> **Correct Answer:** **C**  
> **Explanation:** Agents carry out the work but **do not carry responsibility**. The human team that defined the task, granted permissions, configured governance and merged the change owns the outcome.

---

### Question 5 (Single Choice - Lifecycle)
During the **Plan** phase of Plan → Act → Evaluate, which output is **most** important for making the agent's work governable?

A) A private chain-of-thought stored in the model provider's logs  
B) A confidence score the agent will later use to approve its own work  
C) A commit on `main` that reserves the file paths the agent intends to change  
D) An inspectable plan, visible in the issue or PR, that states scope, steps, success criteria and a rollback or escalation approach  

> **Correct Answer:** **D**  
> **Explanation:** A good Plan phase exposes intent in GitHub, in the issue, the PR description or a plan artifact, so humans can check intent **before** the impact lands. Hidden reasoning (A), direct writes to `main` (C) and self-assessed confidence (B) all go against the model.

---

### Question 6 (Single Choice - Assistant vs Agent)
Which behavior shows **agentic** feedback handling rather than assistant behavior?

A) The tool reads a failed lint check on its own PR, pushes a corrective commit to the same branch, and waits for the check to rerun.  
B) After a developer pastes a failing test log into chat, the tool explains the failure.  
C) The tool generates a code completion when the developer types a function signature.  
D) The tool summarizes a PR diff when a reviewer clicks a button.  

> **Correct Answer:** **A**  
> **Explanation:** Agents **consume system feedback signals** (failed checks, scan alerts) and iterate on their own toward success criteria, producing durable artifacts as they go. B, C and D are reactive assistant behaviors that wait for a human prompt.

---

### Question 7 (Single Choice - "Agents propose; humans and policy accept")
A team wants an agent to help with releases without breaking the principle *"agents propose; humans and policy accept."*

Which design satisfies this principle?

A) The agent receives production deployment credentials as a repository secret and deploys after CI passes.  
B) The agent deploys to production, and a human reviews the deployment log the following morning.  
C) The agent merges its own PR when CODEOWNERS have not responded within 24 hours.  
D) The agent updates release manifests in a PR; after merge, a deploy job targeting a `production` environment with required reviewers waits for human approval.  

> **Correct Answer:** **D**  
> **Explanation:** The agent **prepares** the change. Humans and policy (the PR review, then the environment approval gate) **authorize** the deployment. Every other option gives the agent unilateral execution authority over a critical action.

---

### Question 8 (Single Choice - Mitigating Blind Trust)
An engineering manager notices reviewers approving agent PRs with the comment "CI green, LGTM" within seconds of the PR opening.

Which mitigation **best** addresses the underlying risk?

A) Add `continue-on-error: true` to slow tests so CI finishes faster  
B) Remove human review for agent PRs, since reviewers add no value  
C) Pair automated checks with CODEOWNERS routing, required reviews, evidence sections in the PR, and smaller scoped PRs so reviewers can actually verify intent  
D) Require the agent to state a higher confidence score in the PR description  

> **Correct Answer:** **C**  
> **Explanation:** "CI passed, ship it" is *blind trust in automation*, and the approval pattern described is *rubber-stamping*. Both are fixed by giving reviewers better evidence and context (evidence sections, CODEOWNERS routing, small PRs) and by enforcing review, not by removing it or relying on self-reported confidence.

---

## Domain 2 – Agent Architecture & SDLC Integration

### Question 9 (Single Choice - Workflow Choice)
An agent is assigned two tasks:

1. Rewrite the IAM role definitions in `infra/iam/`
2. Fix typos across `docs/`

Which workflow assignment is **most** appropriate?

A) Plan + execution PR for both, because GitHub merge gates make both equally safe  
B) Plan-first PR for both, to keep the process uniform  
C) Plan-first PR for the IAM change; plan + execution PR for the docs change  
D) Plan + execution PR for the IAM change; plan-first PR for the docs change  

> **Correct Answer:** **C**  
> **Explanation:** Plan-first is preferred when changes are **high-risk or hard to reverse** (infrastructure, auth, workflows, production), because intent is validated before any code exists. Low-risk, easily reversible work such as docs typos benefits from the faster plan + execution model, which is still guarded by merge gates.

---

### Question 10 (Single Choice - Enforcing Planning Boundaries)
A team's planning agent has the instruction *"Do NOT modify any files during planning."* Last week it still edited a configuration file during a planning run.

Which change turns this guidance into **enforcement**?

A) Restrict the planning agent to read-only tools and use an explicit handoff to a separate implementation agent after the plan is approved  
B) Repeat the instruction in uppercase in three places in the agent file  
C) Add a README note telling reviewers to watch for planning-phase edits  
D) Increase the model's temperature so it explores more alternatives before acting  

> **Correct Answer:** **A**  
> **Explanation:** The course is explicit: *"Treat 'instructions not to edit' as guidance; treat tool allowlists and gates as enforcement."* A capability boundary (read-only tools) plus a deliberate handoff to an implementation agent makes editing during planning impossible, not just discouraged.

---

### Question 11 (Single Choice - Workflow Data Passing)
Review this workflow:

```yaml
jobs:
  plan:
    runs-on: ubuntu-latest
    outputs:
      plan: ${{ steps.gen.outputs.plan }}
    steps:
      - id: gen
        run: echo "plan=upgrade lodash to 4.17.21" >> "$GITHUB_OUTPUT"

  implement:
    runs-on: ubuntu-latest
    steps:
      - run: echo "Executing: ${{ needs.plan.outputs.plan }}"
```

The `implement` job starts at the same time as `plan`, and it never receives the plan value.

What is the **minimal** fix?

A) Replace `$GITHUB_OUTPUT` with `$GITHUB_ENV` in the `gen` step  
B) Move the `outputs:` block from the `plan` job into the `implement` job  
C) Add `needs: plan` to the `implement` job  
D) Reference `${{ steps.gen.outputs.plan }}` directly in the `implement` job  

> **Correct Answer:** **C**  
> **Explanation:** Job outputs only cross job boundaries through a `needs:` dependency. `needs:` also orders the jobs, so `implement` waits for `plan`. Without it, the jobs run in parallel and the `needs` context has nothing in it. Step outputs (D) are only visible inside the same job, and `$GITHUB_ENV` (A) does not cross jobs.

---

### Question 12 (Single Choice - Contexts)
A platform team wants one non-secret value, the name of the approved base branch for agent work, to be **centrally managed at the organization level** and reused by many repositories' workflows.

Which context should workflows read it from?

A) `github.*`  
B) `env.*`  
C) `vars.*`  
D) `secrets.*`  

> **Correct Answer:** **C**  
> **Explanation:** `vars.*` holds **centrally managed, non-sensitive configuration variables** set at the repository, organization or environment level. `github.*` is event and runtime metadata, `env.*` is defined in the YAML itself, and `secrets.*` is for sensitive values.

---

### Question 13 (Multiple Choice - Select Three: PR Template)
A team is designing `.github/pull_request_template.md` for agent PRs, following the course's plan template.

Which **three** fields belong in the **Plan (required)** section? (Each correct answer presents part of the solution.)

A) Scope (paths/files)  
B) Model temperature and token budget  
C) Success criteria (verifiable)  
D) Rollback / escalation plan  
E) Personal access token used by the agent  
F) Number of lines of code changed  

> **Correct Answer:** **A, C and D**  
> **Explanation:** The plan template contains **Goal, Scope (paths/files), Steps, Success criteria (verifiable), Risks + mitigations, and Rollback/escalation plan**, followed by Evidence and Review checklist sections. Model parameters and diff size are not plan fields. Tokens must **never** appear in repository content.

---

### Question 14 (Single Choice - Success Criteria)
An agent is assigned *"Resolve code scanning alert #212 (SQL injection) in `orders/repository.py`."*

Which success criterion is the **best** enforceable, goal-aligned definition?

A) "Unit tests pass."  
B) "The agent reports high confidence that the fix is correct."  
C) "The CodeQL analysis on the PR shows alert #212 as fixed, no new code scanning alerts are introduced, and required checks pass."  
D) "The PR is opened within 30 minutes."  

> **Correct Answer:** **C**  
> **Explanation:** Success criteria must show that the **problem is actually solved**, not just superficial signals. "Tests pass" is necessary but not sufficient. The criterion has to tie back to the original signal, the scanning alert, and still keep the standard checks.

---

### Question 15 (Single Choice - CODEOWNERS Ordering)
Review this CODEOWNERS file:

```text
/security/          @security-team
/.github/workflows/ @platform-team
/infra/             @platform-team
*                   @core-team
```

An agent PR modifies only `.github/workflows/ci.yml`. The ruleset on `main` requires review from Code Owners.

Whose approval satisfies the Code Owner requirement?

A) `@core-team`, because `*` matches every file  
B) `@platform-team`, because the more specific matching pattern for that path takes precedence  
C) Both `@core-team` and `@platform-team` must approve  
D) Any repository collaborator with write access  

> **Correct Answer:** **A**  
> **Explanation (exam trap):** CODEOWNERS uses **last matching pattern wins**, not "most specific wins." Here `*` is the **final line**, so it is the last pattern that matches every file, and it overrides the specific rules above it. The effective owner of `.github/workflows/ci.yml` is therefore `@core-team`, and `@platform-team` is never required. The fix is to put the `*` default at the **top** of the file so the specific high-risk paths below it take precedence. A misordered CODEOWNERS file silently removes specialist review from high-risk paths. Treat it as governance drift.

---

### Question 16 (Single Choice - Rollback-Safe Deployment)
An agent prepares a sensitive configuration rollout. Which practice makes the rollout **rollback-safe**?

A) Deploy whatever is "latest on the `release` branch" at the moment the job runs  
B) Re-run the deployment job until it succeeds  
C) Deploy from the agent's local working copy to avoid network delays  
D) Deploy from an explicit reference (a specific commit SHA or tag) recorded in the PR and workflow run  

> **Correct Answer:** **D**  
> **Explanation:** Operating on **explicit references (commit/tag)**, not "latest on a branch," makes a deployment reproducible and easy to revert. It also ties the evidence to a specific code state.

---

### Question 17 (Multiple Choice - Select Three: Agent Profile Controls)
Agent profile configuration provides three kinds of control. Match the course's terms.

Which **three** pairings are correct? (Each correct answer presents part of the solution.)

A) Capability boundary → which tools the agent is allowed to use (prefer allowlists)  
B) Capability boundary → which branches the agent may push to  
C) Visibility boundary → whether the agent is user-selectable in the interactive UI  
D) Delegation boundary → which subagents can be invoked and how handoffs occur  
E) Delegation boundary → which GitHub teams can approve the agent's PRs  

> **Correct Answer:** **A, C and D**  
> **Explanation:** Agent profiles control **capability** (tools), **visibility** (for example `user-invocable`) and **delegation** (`agents` / `handoffs`). Branch behavior and PR approvals are enforced by the execution context and repository rules, **not** by the agent profile.

---

### Question 18 (Single Choice - Evidence Traceability)
An auditor asks: *"Which run produced this `test-results` artifact, and against which code state?"* The team cannot answer.

Which design principle was **not** applied?

A) Evidence should be traceable to a specific workflow run and a specific commit  
B) Evidence should be committed back into the repository tree  
C) Evidence should be stored only in console logs  
D) Evidence should be regenerated on demand during audits  

> **Correct Answer:** **A**  
> **Explanation:** The course's naming and metadata principle: **evidence must be traceable to a specific workflow run and commit**. Upload artifacts where they are produced, link them in the PR's Evidence section, and include run and commit identifiers. Committing generated files (B) and relying on console logs (C) are anti-patterns.

---

## Domain 3 – Tooling, MCP & Execution Environments

### Question 19 (Single Choice - MCP Roles)
Which mapping correctly describes the three MCP governance building blocks?

A) Server = decides which tools are permitted; Registry = exposes tools; Allow list = makes servers discoverable  
B) Server = exposes tools; Registry = makes servers discoverable and trustable; Allow list = decides which servers are permitted  
C) Server = stores credentials; Registry = executes tools; Allow list = logs tool calls  
D) Server = makes servers discoverable; Registry = enforces policy; Allow list = exposes tools  

> **Correct Answer:** **B**  
> **Explanation:** **MCP server** exposes tools. **Registry** makes servers discoverable and trustable. **Allow list** decides which servers are permitted. Together these make MCP both scalable and governable.

---

### Question 20 (Single Choice - Registry Spec)
A team builds a custom MCP registry implementation for its enterprise. Which endpoint is **not** among the HTTPS endpoints required by the MCP registry v0.1 specification for GitHub Copilot?

A) `GET /v0.1/servers`  
B) `GET /v0.1/servers/{serverName}/versions/latest`  
C) `GET /v0.1/servers/{serverName}/versions/{version}`  
D) `POST /v0.1/servers/{serverName}/install`  

> **Correct Answer:** **D**  
> **Explanation:** The three required endpoints are all **read-only GETs**: list servers, get the latest version, and get a specific version. That is also why the required CORS methods are only `GET, OPTIONS`.

---

### Question 21 (Single Choice - CORS Troubleshooting)
A self-hosted registry returns valid JSON from `GET /v0.1/servers`, but Copilot clients cannot load the catalog. The response headers are:

```text
Access-Control-Allow-Origin: https://github.com
Access-Control-Allow-Methods: GET
Access-Control-Allow-Headers: Content-Type
```

Which change set brings the registry into compliance?

A) Set `Access-Control-Allow-Origin: *`, `Access-Control-Allow-Methods: GET, OPTIONS`, and `Access-Control-Allow-Headers: Authorization, Content-Type`  
B) Add `Access-Control-Allow-Credentials: true` only  
C) Set `Access-Control-Allow-Methods: GET, POST, PUT, DELETE`  
D) Remove all CORS headers so the browser falls back to defaults  

> **Correct Answer:** **A**  
> **Explanation:** All three required headers are wrong here. The spec requires origin `*`, methods `GET, OPTIONS`, and headers `Authorization, Content-Type`.

---

### Question 22 (Single Choice - Platform Support)
A regulated customer runs **GitHub Enterprise Server (GHES)** and wants to use the GitHub MCP server in supported IDEs.

Which configuration is supported?

A) Remote only, via `https://api.githubcopilot.com/mcp/`  
B) MCP is not available on any GitHub Enterprise offering  
C) Both local and remote, identical to GitHub Enterprise Cloud with data residency  
D) Local MCP server configuration  

> **Correct Answer:** **D**  
> **Explanation:** **GHES supports local** MCP server configuration. **GHEC with data residency supports both local and remote.** For most users the remote option is the recommended setup where it is available.

---

### Question 23 (Single Choice - Allow List Policy Effect)
An organization owner switches **Restrict MCP access to registry servers** from *Allow all* to *Registry only*. A developer's MCP server, which worked yesterday and is **not** in the registry, stops loading.

When did the policy take effect, and what is the fix?

A) It applies immediately to all developers; add the server to the registry, with an exactly matching server ID, or keep using approved servers only.  
B) It takes effect after the next Copilot seat renewal; wait for renewal.  
C) It only applies to remote servers; the developer should convert the server to `localhost`.  
D) It only applies to new repositories; move work to an older repository.  

> **Correct Answer:** **A**  
> **Explanation:** Once a policy is selected it **applies immediately to all developers**. Under *Registry only*, **every** server, local ones included, must be listed in the registry with an **exactly matching server ID**. Converting to localhost (C) does not help.

---

### Question 24 (Ordering - Remote MCP Setup in VS Code)
Put the steps for adding the GitHub remote MCP server as an agent tool in VS Code in the correct order:

1. Click **Add MCP server**
2. Open Copilot Chat and switch to **Agent mode**
3. Select **HTTP** as the server type and enter `https://api.githubcopilot.com/mcp/`
4. Click **Authenticate** and sign in to GitHub, then save
5. Click the **Tools** icon, then **Configure tools**
6. Choose the scope (current workspace or all workspaces)

A) 2 → 5 → 1 → 3 → 6 → 4  
B) 5 → 2 → 3 → 1 → 4 → 6  
C) 2 → 1 → 5 → 6 → 3 → 4  
D) 1 → 3 → 2 → 5 → 4 → 6  

> **Correct Answer:** **A**  
> **Explanation:** Agent mode → Tools → Configure tools → Add MCP server → HTTP + URL (a name is generated automatically) → choose scope → Authenticate → Save.

---

### Question 25 (Single Choice - MCP Operational Risk)
A developer opens a PR that changes a custom agent's tool configuration from three specific GitHub MCP tools to the wildcard for the whole server.

How should this change be treated?

A) As a cosmetic change that needs no review  
B) As acceptable as long as the agent's instructions say "use tools responsibly"  
C) As a low-risk change, because the MCP server is maintained by GitHub  
D) As a governance-sensitive, high-risk change, reviewed like adding a high-risk dependency, because it increases blast radius; prefer a narrow tool subset  

> **Correct Answer:** **D**  
> **Explanation:** **Namespace control** prefers a narrow tool subset over broad wildcards. Adding or expanding MCP tools increases blast radius and **should be reviewed like a high-risk dependency**. Changes to tool allowlists are governance-sensitive.

---

### Question 26 (Single Choice - Secret Boundaries)
A team assumes the Copilot agent's runtime will automatically have access to the `NPM_TOKEN` repository secret that their CI workflows use. Installs of a private package fail during agent sessions.

Which principle explains this?

A) The agent's runtime environment has its own secret boundary; do not assume it inherits repository CI secrets. Secrets must be injected at runtime only to the components that need them  
B) Secrets are only available on Fridays for change-freeze compliance  
C) The token should be pasted into `.github/copilot-instructions.md` so the agent can read it  
D) Secrets are only available when the workflow uses `permissions: write-all`  

> **Correct Answer:** **A**  
> **Explanation:** This is a direct course principle. Secrets must **never** be placed in instruction files, committed config or plain-text YAML (C). Permissions scopes (D) control the `GITHUB_TOKEN`, not secret visibility.

---

### Question 27 (Single Choice - Agentic Workflow Safe Outputs)
Review this GitHub Agentic Workflow frontmatter:

```yaml
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
```

The daily report issue is created successfully, even though `permissions` grants only **read** access to issues. How?

A) The `github` tool silently upgrades the token to write access  
B) Scheduled workflows always run with `write-all` permissions  
C) The agent writes a structured proposal; a separate, permission-gated safe-output step validates it and creates the issue, applying the title prefix and labels  
D) The issue is created by the developer who last edited the workflow, using their personal token  

> **Correct Answer:** **C**  
> **Explanation:** In agentic workflows the agent runs **read-only** with **zero secrets**. It **proposes** actions, and a separate gated step decides what is allowed and applies it, after threat detection has scanned the proposed output. This separation between "reasoning" and "writing" is the core defense-in-depth design.

---

### Question 28 (Single Choice - GITHUB_TOKEN Trigger Behavior)
An agent workflow pushes a fix commit to a PR branch using the default `GITHUB_TOKEN`. The team expects the `on: push` CI workflow to run on that commit, but it does not.

What is the **most likely** explanation, and the associated design caution?

A) The runner was out of disk space; increase the runner size.  
B) Most events caused by the `GITHUB_TOKEN` do not trigger new workflow runs, which prevents recursive loops; switching to a GitHub App token or PAT can trigger runs but must be designed carefully to avoid recursive automation.  
C) `on: push` never runs for PR branches; use `on: schedule` instead.  
D) The commit message was missing a `[ci run]` tag.  

> **Correct Answer:** **B**  
> **Explanation:** Actions performed with the `GITHUB_TOKEN` generally **do not trigger extra workflow runs**, by design, to prevent unintended loops. GitHub App tokens and PATs can trigger runs, but that power needs guardrails such as bounded retries and concurrency controls.

---

### Question 29 (Single Choice - Custom Agent Boundaries)
A team creates `.github/agents/docs-writer.agent.md` with `applyTo: ['docs/**']` and `tools: [read_file, edit_file]`. They want this agent to **always** work on a branch named `agent/docs/<ticket>` and never push to `main`.

Where must the branch behavior be enforced?

A) By adding `branch: agent/docs/*` to the agent file's frontmatter  
B) By the Markdown instructions in the agent body  
C) By the `applyTo` glob, which also restricts branches  
D) By the execution context (the cloud agent platform or the CI workflow that runs the agent) together with rulesets that block direct pushes to `main`  

> **Correct Answer:** **D**  
> **Explanation:** Custom agents define **focus (`applyTo`), tools and behavior**. They do **not** define branch creation, PR behavior or execution isolation. *"Branch-based scope is always enforced by the execution context, not the custom agent itself,"* backed by rulesets on protected branches.

---

### Question 30 (Single Choice - Workflow-Invoked Agent)
A team runs a custom agent from CI:

```yaml
- name: Security review
  env:
    COPILOT_GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
  run: |
    npx @github/copilot-cli \
      --agent security-reviewer \
      -p "Review this code for vulnerabilities" \
      --no-ask-user
```

Which statement about this configuration is **correct**?

A) `--agent security-reviewer` selects the custom agent defined in `.github/agents/security-reviewer.agent.md`, and the workflow (trigger, runner, permissions) becomes the execution boundary.  
B) `--no-ask-user` grants the agent permission to merge its own PR.  
C) The agent inherits the permissions of the repository administrator who created the workflow.  
D) `COPILOT_GITHUB_TOKEN` must contain a PAT with `admin:org` scope.  

> **Correct Answer:** **A**  
> **Explanation:** The workflow is the controlled execution path: a defined trigger, runner, repository context, and **only the permissions granted to the workflow**. `--no-ask-user` only makes the run non-interactive and grants no extra authority.

---

## Domain 4 – Multi-Agent Systems & Orchestration

### Question 31 (Single Choice - Sequential Orchestration Trap)
A security validation workflow is meant to run **only after CI succeeds**:

```yaml
name: Security Validation
on:
  workflow_run:
    workflows: ["CI Validation"]
    types: [completed]

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - run: ./scripts/security-validate.sh
```

Reviewers notice it also runs after **failed** CI runs. What is the fix?

A) Change `types: [completed]` to `types: [success]`  
B) Add `if: github.event.workflow_run.conclusion == 'success'` to the `validate` job  
C) Add `needs: CI Validation` to the `validate` job  
D) Replace `workflow_run` with `pull_request`  

> **Correct Answer:** **B**  
> **Explanation:** `workflow_run` with `types: [completed]` fires when the upstream workflow **finishes, whatever its result**. Gate on `github.event.workflow_run.conclusion == 'success'`. `success` is not a valid activity type (A), and `needs` only works between jobs in the **same** workflow (C).

---

### Question 32 (Single Choice - Parallelism Precondition)
A documentation agent (`docs/**`) and a refactoring agent (`src/**/*.ts`) should run at the same time. A third agent, for dependency updates, edits `package.json` **and** occasionally `src/config.ts`.

Which statement is **correct**?

A) The docs and refactoring agents can run in parallel because their paths are isolated; the dependency agent overlaps with the refactoring agent's scope and should either be re-scoped or sequenced.  
B) All three can safely run in parallel because each opens its own PR.  
C) Parallel orchestration is never appropriate in GitHub.  
D) Only the dependency agent should run in parallel because it touches manifests.  

> **Correct Answer:** **A**  
> **Explanation:** *"The core design requirement for parallel orchestration is isolation: if agents can collide on the same files, parallelism will increase instability rather than throughput."* Separate PRs alone do not remove overlap.

---

### Question 33 (Single Choice - Conflict Types)
Two agent PRs merge cleanly into `main` one after the other. Agent A renamed a config key in `config/defaults.yaml`. Agent B added new code that reads the **old** key name. There are no textual conflicts, but the application fails at startup.

What kind of conflict is this?

A) Textual merge conflict  
B) Semantic conflict  
C) Policy conflict  
D) Duplicate effort  

> **Correct Answer:** **B**  
> **Explanation:** A **semantic conflict** is a *clean merge* with *broken combined behavior*. Mitigations include merge validation checks against the latest `main`, requiring branches to be up to date before merging, and arbitration rules rather than "first merge wins."

---

### Question 34 (Single Choice - Coordination Failure Modes)
Over a weekend, an agent's PR shows 37 workflow runs. Each run fails, the agent pushes a small tweak, and the same check fails again with the same failure signature. Nobody was notified.

Which failure mode is this, and which control was missing?

A) Partial execution; missing artifact uploads  
B) Stalled workflow; missing environment approval  
C) Flapping (repeated runs without convergence); missing bounded retries and an escalation threshold (escalate after the same check fails twice)  
D) Conflicting outputs; missing CODEOWNERS  

> **Correct Answer:** **C**  
> **Explanation:** Repeated reruns with no convergence is **flapping**. The safe iteration policy says that if the **same required check fails twice**, automated iteration stops and the issue is escalated to a human with a summary.

---

### Question 35 (Multiple Choice - Select Three: Escalation Report)
An agent has hit its escalation threshold. According to the safe iteration policy, which **three** items should the escalation to a human reviewer contain? (Each correct answer presents part of the solution.)

A) What failed  
B) The agent's total token consumption for the session  
C) What was attempted  
D) What evidence exists (links to runs and artifacts)  
E) The agent's self-reported confidence score  
F) A request to enable auto-merge  

> **Correct Answer:** **A, C and D**  
> **Explanation:** The escalation includes **what failed, what was attempted, what evidence exists, and the suggested next step**. Token usage, confidence scores and auto-merge requests are not part of an actionable escalation.

---

### Question 36 (Single Choice - Subagent Failure)
A `planner.agent.md` contains:

```yaml
---
agents: [implementer, code-review]
handoffs:
  - label: Start Implementation
    agent: implementer
    send: true
---
```

The **Start Implementation** handoff fails every time. `implementer.agent.md` contains:

```yaml
---
name: implementer
disable-model-invocation: true
user-invocable: true
---
```

What is the cause?

A) `send: true` is not a valid handoff property  
B) Handoffs only resolve by filename, never by the `name:` attribute  
C) `user-invocable: true` hides the agent from orchestration  
D) `disable-model-invocation: true` prevents the implementer from being invoked as a subagent by another agent  

> **Correct Answer:** **D**  
> **Explanation:** `disable-model-invocation: true` means **the agent cannot be invoked as a subagent**, which breaks orchestration. `user-invocable` only controls whether users can pick it in the UI. `send: true` auto-submits the handoff prompt. Handoffs resolve by the `name:` attribute **or** a matching filename.

---

### Question 37 (Single Choice - Copilot Modes)
A developer wants to work on **three independent issues at the same time** using Copilot agents. They currently use the local agent in the IDE.

What should they do?

A) Open three IDE windows; local mode runs sessions in parallel  
B) Parallel agent sessions are not supported in any mode  
C) Use `strategy.matrix` in the IDE settings to parallelize local sessions  
D) Use Copilot cloud agent sessions or Copilot CLI processes, both of which support parallel sessions across tasks; local mode runs serially, one task at a time  

> **Correct Answer:** **D**  
> **Explanation:** **Cloud: yes. CLI: yes. Local: no (serial only).**

---

### Question 38 (Single Choice - Artifact-Based Coordination)
A design proposal has a "triage agent" send its findings directly to a "fix agent" through an in-memory message channel that no one can inspect.

Which alternative pattern does the course recommend?

A) Give both agents `write-all` permissions so they can coordinate faster  
B) Run the first agent with restricted permissions, have it produce a structured output (plan or report) as a workflow artifact, then use a controlled step that applies only the operations the workflow allows  
C) Store the messages in the agent's short-term memory  
D) Have the agents comment on each other's commits using a shared PAT  

> **Correct Answer:** **B**  
> **Explanation:** *"Direct agent-to-agent communication is often less reliable than shared, reviewable artifacts."* Artifact-based coordination creates an explicit boundary between **reasoning** and **writing** and leaves evidence that reviewers can inspect.

---

### Question 39 (Multiple Choice - Select Two: Attribution Conventions)
An organization runs dependency, security and refactor agents in the same repository. Reviewers cannot tell which agent produced which PR.

Which **two** conventions from the course improve attribution? (Each correct answer presents part of the solution.)

A) PR titles such as `[agent: dependency] Update axios to 1.7.4`  
B) Using one shared branch named `agents` for all agent work  
C) Labels such as `agent: dependency`, `agent: security`, `agent: refactor`, plus dedicated branches like `agent/security/<ticket>`  
D) Squashing all agent PRs into a single weekly PR  
E) Removing PR descriptions to reduce noise  

> **Correct Answer:** **A and C**  
> **Explanation:** Consistent titles, labels and dedicated branches (`agent/<role>/<ticket>`) make every change attributable. Shared branches (B) and batching (D) cause interleaved commits and ambiguous ownership.

---

### Question 40 (Single Choice - Matrix vs Concurrency)
An engineer proposes using `strategy.matrix` to stop two agent sessions from triggering overlapping runs of the same workflow on the same PR branch.

Why is this the wrong tool?

A) `strategy.matrix` controls parallelism **within** a single run, not overlap **across** runs triggered by different events or sessions; use workflow-level `concurrency` with `group: ${{ github.workflow }}-${{ github.ref }}` and `cancel-in-progress: true`  
B) `strategy.matrix` is deprecated  
C) `strategy.matrix` only works with self-hosted runners  
D) `strategy.matrix` cancels every run except the first one  

> **Correct Answer:** **A**  
> **Explanation:** Matrix strategies expand jobs **inside one run**. Preventing collisions between runs on the same branch is the job of workflow-level `concurrency`, scoped per workflow **and** per ref so unrelated workflows are not blocked.

---

## Domain 5 – Memory, State & Evaluation

### Question 41 (Single Choice - Source of Truth Mapping)
Which mapping matches the course's single-source-of-truth model?

A) Requirements → PR comments; Decisions → chat history; Validation rules → workflow logs; Results → issues  
B) Requirements → Issue; Decisions → Pull request or documentation; Validation rules → Repository instructions; Results → Workflow logs and artifacts  
C) Requirements → Commit messages; Decisions → Labels; Validation rules → README; Results → Releases  
D) Requirements → Agent short-term memory; Decisions → Long-term memory; Validation rules → Prompts; Results → Console output  

> **Correct Answer:** **B**  
> **Explanation:** Each type of information has **one** clear home. Duplicating it elsewhere creates conflicting context.

---

### Question 42 (Single Choice - Conflicting vs Stale Context)
A product manager pastes updated acceptance criteria into three different Copilot Chat prompts across the week but never updates the linked issue. The agent's output alternates between the old and new behavior.

What is the problem, and the correct remediation?

A) Stale context; rebase the branch onto `main`  
B) Tool misuse; restrict the agent's tools  
C) Conflicting context; update the original source (the issue or PR) instead of redefining criteria in prompts, keeping one source of truth  
D) Reasoning error; switch to a larger model  

> **Correct Answer:** **C**  
> **Explanation:** **Conflicting context** is the same information existing in several places with different values. The fix is to *"Update the original source instead of creating new copies."* Stale context is outdated information, for example a PR that is behind its base branch.

---

### Question 43 (Single Choice - Cross-Tool Continuity)
A developer starts a task in the IDE, continues in Copilot CLI, and finishes with a cloud agent. What is the course-recommended way to share state across these surfaces?

A) Export the IDE chat transcript and paste it into each new tool  
B) Copy the acceptance criteria into each tool's local config file  
C) Store progress in the agent's long-term memory only  
D) Use durable references such as the PR number, branch name, commit SHAs, workflow run links, and issue/PR URLs, so every environment retrieves the same state from GitHub  

> **Correct Answer:** **D**  
> **Explanation:** State is shared through **durable references, not copied context**. Every surface can read the same repository data, so continuity does not depend on moving session history around.

---

### Question 44 (Single Choice - Reset Rules)
Halfway through an agent PR, the team abandons a REST-based approach and chooses an event-driven design. The PR description, commits and earlier comments all assume REST.

What should happen according to the reset rules?

A) Keep working in the same PR and let the agent infer the change from new commits  
B) Clearly document the new direction, then rewrite the PR description or close and recreate the PR, so incorrect assumptions are not carried over  
C) Delete all workflow artifacts so the old context disappears  
D) Increase the agent's short-term memory window  

> **Correct Answer:** **B**  
> **Explanation:** Reset rules apply when **a new implementation approach is chosen**, requirements change significantly, or assumptions are no longer valid. Rewrite or recreate the PR and record the new direction before continuing.

---

### Question 45 (Single Choice - Root Cause Classification)
An agent's PR fails CI because its workflow edit calls `./scripts/run-integration.sh`, a script that does not exist in the repository. The application logic in the PR is otherwise correct.

How should this failure be classified, and which improvement area applies?

A) Reasoning error → clarify acceptance criteria in the issue  
B) Tool misuse → adjust tool configuration and execution templates (workflow files, allowed commands and scripts)  
C) Context issue → rebase onto `main`  
D) Semantic conflict → add a merge validation check  

> **Correct Answer:** **B**  
> **Explanation:** Referencing non-existent scripts, using wrong commands and misconfiguring workflows are all **tool misuse**. The improvement lever is **tool configuration** (workflows, templates, constrained arguments). Reasoning errors map to prompts and instructions. Context issues map to memory and state.

---

### Question 46 (Single Choice - Root Cause Classification II)
An agent re-implements a caching layer that the team **explicitly rejected** two weeks earlier. The rejection was recorded in a comment on a *different*, closed PR and never written to the issue or the repository docs.

Which root cause category fits **best**?

A) Reasoning error  
B) Tool misuse  
C) Context issue (missing prior decisions)  
D) Flapping  

> **Correct Answer:** **C**  
> **Explanation:** The agent was missing a **prior decision** because it was not stored in the source of truth. That is a context issue. The fix is in memory and state: record decisions in the active issue, PR or docs.

---

### Question 47 (Multiple Choice - Select Two: Retention)
A compliance team defines these requirements for workflow evidence:

- Private repository `payments-core`: keep artifacts for **one year**.
- Public repository `sdk-samples`: keep artifacts for **180 days**.

Which **two** statements are correct? (Each correct answer presents part of the solution.)

A) `payments-core` can be configured with a 365-day retention, because private repositories support up to 400 days  
B) `sdk-samples` can be configured with a 180-day retention  
C) Public repositories are configurable only between 1 and 90 days, so 180 days must be met some other way (for example, exporting evidence to a separate archive)  
D) Default retention is 30 days for every repository  
E) Deleted artifacts can be restored from the Actions tab within 400 days  

> **Correct Answer:** **A and C**  
> **Explanation:** The default is **90 days**. Public repositories allow **1–90 days**. Private repositories can extend to **400 days**. Deleted artifacts **cannot be restored**.

---

### Question 48 (Multiple Choice - Select Three: Security Signals)
A team wants agent PRs evaluated against **security** quality gates before merge. Which **three** GitHub capabilities from the course should be part of evaluation? (Each correct answer presents part of the solution.)

A) Code scanning (for example, CodeQL with SARIF results)  
B) Dependency review checks  
C) Secret scanning and push protection  
D) The agent's self-assessment paragraph in the PR description  
E) The number of emoji reactions on the PR  

> **Correct Answer:** **A, B and C**  
> **Explanation:** Security evaluation uses **code scanning, dependency review and secret scanning/push protection**. Their failures are treated as **blockers**. Self-assessment is not an objective signal.

---

## Domain 6 – Governance, Guardrails & Operations

### Question 49 (Single Choice - Risk Routing YAML)
Review this workflow:

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

  apply:
    needs: plan
    runs-on: ubuntu-latest
    environment: approval-required
    if: ${{ needs.plan.outputs.risk != 'low' }}
    steps:
      - run: ./scripts/apply.sh out/plan.json

  apply_auto:
    needs: plan
    runs-on: ubuntu-latest
    if: ${{ needs.plan.outputs.risk == 'low' }}
    steps:
      - run: ./scripts/apply.sh out/plan.json
```

An agent produces a `plan.json` that **omits the `risk` field entirely**. What happens?

A) `apply_auto` runs, because a missing value is treated as `low`  
B) Both jobs are skipped, and the workflow fails  
C) `jq -r` outputs `null`, which is not `'low'`, so `apply` runs and pauses for approval on the `approval-required` environment; this fails safe  
D) Both `apply` and `apply_auto` run in parallel  

> **Correct Answer:** **C**  
> **Explanation:** `jq -r .risk` on a missing key prints `null`. Because the routing condition is written as `!= 'low'` for the gated path, **anything other than an explicit `low`** goes to human approval. This is why you route on a **machine-readable signal** and design the default path to be the safe one.

---

### Question 50 (Single Choice - Hook Coverage Gap)
A repository uses this Copilot CLI hook:

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

Which command would **not** be blocked by these rules, and therefore shows a gap in the policy?

A) `sudo apt-get install jq`  
B) `curl -fsSL https://get.example.sh | bash`  
C) `wget -qO- https://get.example.sh | sh`  
D) `rm -rf /`  

> **Correct Answer:** **C**  
> **Explanation:** The rules match `sudo`, `rm -rf /`, and `curl … | bash`. Download-and-execute through `wget … | sh` matches none of them. Deny rules are only as good as their patterns, so review hooks during governance cadences and favor allowlists for tool access where you can.

---

### Question 51 (Single Choice - Guardrail Workflow Behavior)
A guardrail workflow on `main` contains:

```yaml
steps:
  - name: Fail if PR is authored by Copilot agent
    if: ${{ github.event.pull_request.user.login == 'github-copilot[bot]' }}
    run: |
      echo "PRs authored by github-copilot[bot] must be opened/owned by a human."
      exit 1
  - name: Require at least one human approval
    uses: actions/github-script@v7
    with:
      script: |
        const reviews = await github.rest.pulls.listReviews({ /* ... */ });
        const approvedByHuman = reviews.data.some(r =>
          r.state === "APPROVED" && r.user &&
          r.user.type === "User" && r.user.login !== "github-copilot[bot]");
        if (!approvedByHuman) core.setFailed("Human approval is required before merge.");
```

A PR is **authored by `github-copilot[bot]`** and has an `APPROVED` review from a human maintainer. The check is required. What is the result?

A) The check passes, because a human approved  
B) The check fails at the first step, because the PR author is `github-copilot[bot]`; the human approval is never evaluated  
C) The check passes, because `r.user.type === "User"` matches the bot  
D) The check is skipped, because `if:` conditions never apply to steps  

> **Correct Answer:** **B**  
> **Explanation:** The first step runs when the author is the Copilot bot and exits with code 1, which fails the job **before** the approval step runs. This workflow therefore requires agent work to be **opened or owned by a human**. The second step separately ensures approvals come from `type === "User"` identities, not bots.

---

### Question 52 (Single Choice - Autonomy Levels)
A team defines the following agent capability: *"The agent may create branches and pull requests, but cannot merge or deploy."*

Which autonomy level is this?

A) Read-only autonomy  
B) Propose-only autonomy  
C) Execute with guardrails  
D) Human-authorized execution  

> **Correct Answer:** **B**  
> **Explanation:** **Read-only**: inspect and recommend. **Propose-only**: branches and PRs, no merge or deploy. **Execute with guardrails**: run pre-approved workflows such as tests, builds and staging deploys. **Human-authorized execution**: high-impact actions only after human approval.

---

### Question 53 (Multiple Choice - Select Three: Governance Drift)
During a quarterly audit, which **three** findings are examples of **governance drift**? (Each correct answer presents part of the solution.)

A) A required check was renamed in the workflow, and the ruleset no longer enforces the new name  
B) "Require review from Code Owners" was turned off "temporarily" six months ago  
C) CODEOWNERS still lists a team that was disbanded last year  
D) Workflow logs older than 90 days were deleted automatically under the default retention policy  
E) A PR template includes a Rollback section  

> **Correct Answer:** **A, B and C**  
> **Explanation:** Drift is controls quietly degrading: checks renamed or removed, review requirements relaxed, CODEOWNERS outdated, permissions expanding, secrets moved to broader scopes. D is expected, configured behavior. E is a good practice.

---

### Question 54 (Single Choice - Recovery Strategy)
A dependency agent's PR fails because **secret scanning push protection** blocked a commit that contained what looks like a cloud access key. The agent's automation is set to retry failed pushes up to three times.

What is the correct response?

A) Let the agent retry three times; push protection sometimes produces transient errors  
B) Bypass push protection for the agent's identity to keep velocity  
C) Stop retrying and investigate the security failure; security failures are investigated, not repeatedly retried  
D) Increase the retry limit to ten  

> **Correct Answer:** **C**  
> **Explanation:** Bounded retries are for **transient** failures. A security block is a signal that needs a human. The recovery strategy is explicit: *"Investigate security failures instead of repeatedly retrying."*

---

## Case Study – Contoso Payments (Q55–Q60)

> **Read the case study, then answer Questions 55–60.** You may refer back to it.
>
> **Background.** Contoso Payments runs a monorepo, `contoso/payments`, on GitHub Enterprise Cloud. It contains:
>
> - `src/` – application services (TypeScript)
> - `docs/` – developer documentation
> - `infra/` – Terraform for production networking and IAM
> - `.github/workflows/` – CI and deployment workflows
>
> **Current state.**
>
> - Copilot cloud agent is enabled for the repository. Developers also use Copilot CLI locally.
> - The org MCP policy is *Allow all*. Developers have installed 14 different MCP servers, including an unvetted community server that can run SQL against any database URL.
> - All workflows declare `permissions: write-all` at the top level.
> - A `deploy.yml` workflow deploys to production on every push to `main` using a `PROD_DEPLOY_KEY` **repository** secret.
> - CODEOWNERS has a single line: `* @payments-devs`.
> - Agent PRs often contain only a diff, with no plan and no evidence links.
> - Last month an agent PR changed `infra/iam/roles.tf`, was approved within two minutes by a teammate, and caused a production access outage.
>
> **Requirements.**
>
> 1. Only security-approved MCP servers may be used, including local servers.
> 2. No agent-initiated action may reach production without explicit approval from the SRE team, and production credentials must not be available to other jobs.
> 3. Changes to `infra/` and `.github/workflows/` must be reviewed by `@platform-team`.
> 4. Low-risk docs changes should merge without waiting for human review once checks pass.
> 5. Workflows must follow least privilege.
> 6. Every agent PR must carry a plan, and merging without one must be technically impossible.

### Question 55 (Single Choice - Case Study: MCP)
Which configuration meets **Requirement 1**?

A) Keep *Allow all* and publish a wiki page listing approved servers  
B) Configure an MCP registry that contains only approved servers (including any local servers, with exactly matching IDs), enter its URL in Copilot policy settings, and set **Restrict MCP access to registry servers** to *Registry only*  
C) Add a `preToolUse` hook that logs which MCP server was called  
D) Disable MCP servers in Copilot entirely and allow only local servers  

> **Correct Answer:** **B**  
> **Explanation:** Documentation (A) and logging (C) do not enforce anything. *Registry only* plus a curated registry is the enforcement mechanism, and under it local servers must also be listed with exact IDs. D blocks all MCP use and contradicts the goal of allowing approved servers.

---

### Question 56 (Single Choice - Case Study: Production Gate)
Which change to `deploy.yml` and the repository settings **best** meets **Requirement 2**?

A) Add `if: github.actor != 'github-copilot[bot]'` to the deploy job  
B) Add `continue-on-error: false` to the deploy step  
C) Rename `PROD_DEPLOY_KEY` to something less obvious  
D) Create a `production` environment with the SRE team as required reviewers, move `PROD_DEPLOY_KEY` from repository secrets to that environment's secrets, and set `environment: production` on the deploy job  

> **Correct Answer:** **D**  
> **Explanation:** Environments **require reviewers before the job continues** and **restrict secrets** to jobs that target that environment. Moving the key out of repository scope keeps it from other jobs. A is easy to get around: a human pushing an agent's merged change still deploys without approval. C is obscurity, not security.

---

### Question 57 (Single Choice - Case Study: CODEOWNERS)
Which CODEOWNERS file, combined with **"Require review from Code Owners"** in the `main` ruleset, meets **Requirement 3**?

A)
```text
/infra/             @platform-team
/.github/workflows/ @platform-team
*                   @payments-devs
```
B)
```text
*                   @payments-devs
/infra/             @platform-team
/.github/workflows/ @platform-team
```
C)
```text
*                   @payments-devs @platform-team
```
D)
```text
/infra/             @payments-devs
/.github/workflows/ @payments-devs
```

> **Correct Answer:** **B**  
> **Explanation:** CODEOWNERS uses **last matching pattern wins**. In A, the trailing `*` overrides the specific rules (the same trap as Q15), so `@payments-devs` alone could approve infra changes. B puts the catch-all first and the specific high-risk paths after it. C lets *either* team satisfy the rule for every path. D routes to the wrong team.

---

### Question 58 (Single Choice - Case Study: Least Privilege)
A CI workflow in the repository has two jobs: `lint-and-test`, which only reads code, and `comment-results`, which posts a summary comment on the PR. Which permission design meets **Requirement 5**?

A) Keep `permissions: write-all` at the top level, since the comment needs write access  
B) Top level `permissions: pull-requests: write, contents: write`; nothing at job level  
C) Top level `permissions: contents: read`; on `comment-results` only, add `pull-requests: write`  
D) `permissions: {}` at the top level, and `write-all` on `lint-and-test`  

> **Correct Answer:** **C**  
> **Explanation:** Use a read-only default at the workflow level and **elevate only on the job that needs it**. `pull-requests: write` counts as an elevated capability and belongs only on the job that writes PR context.

---

### Question 59 (Single Choice - Case Study: Plan Enforcement)
Which approach meets **Requirement 6** ("merging without a plan must be technically impossible")?

A) Add the plan section to the PR template **and** create a Plan Gate workflow that fails when the plan is missing, then mark it as a **required status check** in the `main` ruleset  
B) Add a plan section to `.github/pull_request_template.md` and ask reviewers to check it  
C) Add a sentence to `.github/copilot-instructions.md` telling agents to always write a plan  
D) Add a `postToolUse` hook that logs whether a plan was written  

> **Correct Answer:** **A**  
> **Explanation:** A template creates *consistency*, but only a **required status check** turns *"include a plan"* into a **system guarantee**. Instructions (C) are guidance, and logging hooks (D) observe without preventing anything. This applies the "controls in docs only" anti-pattern lesson.

---

### Question 60 (Yes/No Statement Series - Case Study: Outage Review)
Consider last month's `infra/iam/roles.tf` outage. For each statement, decide **Yes** (true) or **No** (false).

1. A plan-first PR would have been the more appropriate workflow for this change.
2. Under the course's risk model, this change should have been eligible for auto-merge once CI passed.
3. The two-minute approval is an example of the rubber-stamping anti-pattern.
4. Accountability for the outage lies with the agent, because it authored the change.

A) Yes, No, Yes, No  
B) Yes, Yes, Yes, No  
C) No, No, Yes, Yes  
D) Yes, No, No, No  

> **Correct Answer:** **A**  
> **Explanation:**  
> 1. **Yes.** `infra/` is high-risk and hard to reverse, which is the textbook case for plan-first.  
> 2. **No.** Infra changes are **High** risk and need CODEOWNERS plus explicit approvals and stronger checks. Auto-merge is for **Low** risk only (Requirement 4: docs).  
> 3. **Yes.** An approval that is just a click to unblock is rubber-stamping. The mitigation is better evidence, CODEOWNERS routing and smaller PRs.  
> 4. **No.** Responsibility does not move with execution. The humans who scoped, approved and merged the change are accountable.

---

## Answer Key

| Q | Ans | Q | Ans | Q | Ans | Q | Ans | Q | Ans | Q | Ans |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 1 | A, C | 11 | C | 21 | A | 31 | B | 41 | B | 51 | B |
| 2 | C | 12 | C | 22 | D | 32 | A | 42 | C | 52 | B |
| 3 | B | 13 | A, C, D | 23 | A | 33 | B | 43 | D | 53 | A, B, C |
| 4 | C | 14 | C | 24 | A | 34 | C | 44 | B | 54 | C |
| 5 | D | 15 | A | 25 | D | 35 | A, C, D | 45 | B | 55 | B |
| 6 | A | 16 | D | 26 | A | 36 | D | 46 | C | 56 | D |
| 7 | D | 17 | A, C, D | 27 | C | 37 | D | 47 | A, C | 57 | B |
| 8 | C | 18 | A | 28 | B | 38 | B | 48 | A, B, C | 58 | C |
| 9 | C | 19 | B | 29 | D | 39 | A, C | 49 | C | 59 | A |
| 10 | A | 20 | D | 30 | A | 40 | A | 50 | C | 60 | A |

**Scoring:** 1 point per question. Multi-select questions score only if every selection is correct.

| Domain | Questions | Your score |
| :--- | :--- | :--- |
| D1 Foundations | Q1–Q8 | __ / 8 |
| D2 Architecture & SDLC | Q9–Q18 | __ / 10 |
| D3 Tooling, MCP & Execution | Q19–Q30 | __ / 12 |
| D4 Multi-Agent Orchestration | Q31–Q40 | __ / 10 |
| D5 Memory, State & Evaluation | Q41–Q48 | __ / 8 |
| D6 Governance & Operations | Q49–Q54 | __ / 6 |
| Case Study | Q55–Q60 | __ / 6 |
| **Total** | | **__ / 60** |

**If you scored below 70% in a domain,** re-read that module in `STUDY.en.md` and then retake only that domain's questions a day later.

---
*End of Mock Exam.*
