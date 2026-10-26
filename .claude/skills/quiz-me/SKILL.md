---
name: "quiz-me"
description: "Quiz the user with hard, exam-style multiple-choice questions on a section of study material, then grade their answers with explanations. Use when the user says \"question me\", \"quiz me\", or \"test me\", or asks for practice or exam questions on content just taught or given."
---

# Quiz me

Write a hard multiple-choice **exam** on one section, wait for the answers, then grade them. The default difficulty is **4/5**: answerable only by someone who studied the material closely, never by common sense or general knowledge. The user can set a different level.

## Steps

1. **Pin the section.** Use the section most recently taught by [`teach-me`](../teach-me/SKILL.md) in this conversation, or the one the user names. Re-read its source files; the source is the answer key, and the summary is only a guide to it. Done when the source for this section is in context.

2. **Inventory the testable facts.** List, privately, every definition, contrast, named list (with its count), mapping, process, rule, and caveat in the section, grouped by unit. Done when every unit of the section has entries.

3. **Write the exam.** Write 12–15 questions with coverage across every unit, weighted toward the facts most likely to be confused with each other. Make each question hard in one of these ways:
   - **Scenario**: a realistic situation where the user has to classify it or pick the next step. The answer comes from applying a rule, not from recognizing words.
   - **Near-miss distractors**: the wrong options are true statements from a *neighbouring* part of the same material (the mitigation for a different risk, the property of a different concept). This is the main source of difficulty.
   - **Exceptions**: "Which is NOT one of the N items…", or an option that is right except for a missing caveat.
   - **Select TWO**: two correct answers among five options. Use these in about a quarter of the questions.
   - **Misconception challenge**: present a plausible claim the source contradicts and ask why the source disagrees.
   - **Twin concepts**: tell apart two concepts the source defines close together.

   **Use simple English (CEFR B2 level)** in questions, options, and grading. The user is not a native speaker. The question must be hard because of the *content*, never because of the language: use short sentences and common words, avoid idioms and rare phrasal verbs, and keep the exam's technical terms. Don't add trick wording or double negatives; put words like NOT in capitals.

   Every question has exactly one defensible answer (or exactly two for select-TWO) that you can trace to a specific line of the source. Vary the position of the correct letter. Done when every unit is covered and every answer is backed by the source.

4. **Present.** Header: `# <Section title> Quiz (Difficulty N/5)`, then one line with the answer format: `` `1-B, 2-A,C, ...` ``. Number the questions in bold, give options as `- A. …`, and mark multi-select with *(Select TWO)*. Never show an answer next to its question, and give no hints in the question text.

   After the last question, invite the answers. Then put the **answer key at the very end** of the message, so the user can solve every question before they see it:
   - First a warning line: `⚠️ Answer key below. Don't scroll down until you finish.`
   - Then a `---` separator, followed by several empty lines made with `&nbsp;`, and another `---` separator, so the key is not visible while the user reads the questions.
   - Then `## Answer key` with one compact line: `1-B, 2-A,C, 3-D, ...`. No explanations here; they come in step 5.

5. **Grade** when the answers arrive. Write everything in the same simple B2 English as the questions.
   - Score line: `# Results: X / N (P%)`.
   - A table: `Q | Yours | Correct | ✅/❌`. A select-TWO question with only one right option counts as a miss.
   - **One correction block per miss** (a half-right answer is a miss too), in question order:
     - `### Q<n> ❌`, then the **full question again**: the stem and every option, word for word. Mark the user's choice with `← yours` and the correct option(s) with `✅`, so the user can re-read the question with the answer in place.
     - **Why**: the correct answer, quoting the source line that decides it. Then say why the user's choice fails, and name the neighbouring concept that distractor belongs to. If the user's answer is defensible, say so plainly and name the cue in the question that separates the two answers.
   - **Study material** after the correction blocks. Build it from the wrong answers, never from the whole section: this is a focused re-teach of only what the user got wrong. Write one `##` block for each concept the misses touched. Merge misses that share a concept (for example, two misses that both mix up neighbouring lists) into one block. Each block contains:
     - **The full source material** for that concept: the complete list with its count, the full mapping, or the full process, copied faithfully. The user needs the whole list, not only the items in the question.
     - **The neighbour it was confused with**, side by side in one table, with the overlapping items marked (for example, an item that appears in both lists).
     - **The source's key sentences**, quoted verbatim in italics.
     - **One memory hook**: a trick, a contrast rule, or a mnemonic that tells the twins apart.
     - **One self-check line**: a short new question with its answer hidden behind `<details><summary>Answer</summary>…</details>`.

     Done when every missed fact appears in a study block together with its full list and the neighbour it was confused with.
   - **Takeaway**: one or two lines on the pattern in the misses. If a fact was also missed in an earlier round of this conversation, say so.
   - End with the options: **"next section"** (back to `teach-me`) or **"question me again"** (a fresh exam on the same section with new scenarios that put more weight on the facts missed this time, without reusing any earlier question).