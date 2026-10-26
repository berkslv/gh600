---
name: "teach-me"
description: "Teach study material one section at a time as an exam-ready summary. Use when the user asks to be taught, to summarize a section, chapter, or module for study, or to move to the \"next section\" of course or exam material (local files, a URL, or pasted text)."
---

# Teach me

Turn source material into a sequence of **sections** and teach one per turn as a dense, exam-ready summary. The summary is the only thing the user studies before [`quiz-me`](../quiz-me/SKILL.md) tests them, so every **testable fact** in the section must be in it.

A **testable fact** is anything an examiner could turn into a question: a definition, a contrast between two concepts, a named list (and how many items it has), a mapping (problem → fix, control → purpose), an ordered process, a rule of thumb, a caveat or exception, a worked example.

## Steps

1. **Map the material.** Find the source: files in the working directory, a URL, or text the user pasted. Work out its natural order (an outline, course index, numbered folders, or chapter headings) and split it into sections, each a module, chapter, or similar unit that is about 20–40 minutes of reading. Done when you can name every section in order and say which one comes next: the one the user asked for, or else the first section not yet taught in this conversation.

2. **Read the whole section.** Read every unit or file in it, including intros and summaries. Treat a "knowledge check" or quiz file as a hint about what the authors think matters, and leave its questions out of the summary. Done when every file in the section is read and nothing is skipped or skimmed.

3. **Write the summary.** Layout:
   - Header: `# <Material> · Section N of M: <Title>`, plus one italic line with the section map (all section titles, current one marked) on the first section, and whenever the user seems lost.
   - One numbered `##` heading per unit of the source, in source order.
   - **Tables** for every contrast (A vs. B), mapping (risk → mitigation), or set of items that share attributes.
   - **Counted lists** for named lists, with the count in the label ("Minimum audit trail (6 items)"). Examiners ask "which is NOT one of…".
   - **Bold** the leading term of each fact. Quote verbatim, in italics, the source's key sentences and slogans, because exams reuse the source's exact wording.
   - Keep one short concrete example wherever the source gives one.
   - Put caveats ("only when configured", "requires admin") next to the fact they qualify.

   Write in the user's language. Prefer dense bullets to prose; aim for a page that reads in 5–10 minutes.

   **Use simple English (CEFR B2 level).** The user is not a native speaker, so the explanations must be easy to read:
   - Short sentences, one idea each. Common, everyday words ("use" not "leverage", "show" not "demonstrate", "because" not "owing to").
   - No idioms, slang, or phrasal verbs that a learner may not know ("rule out", "boils down to").
   - Keep the technical terms and product names the exam uses, but explain each new term in plain words the first time it appears.
   - Verbatim quotes from the source stay exactly as written. If a quote is hard to understand, add a short plain-English note after it.

   Done when every testable fact in the section appears in the summary. Check this by going back through each source file and finding where each of its facts landed.

4. **Hand off.** End with one line: say **"question me"** for a hard quiz on this section, or **"next section"** to continue.

## Follow-ups

- "next section": go to step 1 for the next untaught section.
- "question me" / "quiz me": invoke `quiz-me` on the section just taught.
- A question about the content: answer it from the source, then repeat the hand-off line.