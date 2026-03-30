# /hub — Skill Hub RAG

When the user runs `/hub` or `/hub <question>`, read the skill hub and surface what is relevant.

The skill hub is the folder `hub/`. Every file in it is a skill card in plain markdown. No code. No config. Just read the files.

---

## What This Skill Does

This is the RAG (retrieval-augmented) skill for the hub. When the user asks a question, you:

1. Read `hub/README.md` to get the index
2. Read the relevant skill card files in `hub/`
3. Answer based on what you find in those files
4. Point the user to the exact file(s) they need

You do not generate answers from general knowledge. You read the hub files and surface what is there. If something is not in the hub, say so — and offer to add a skill card for it.

---

## Steps

### If called with no argument — `/hub`

Show the full skill index. Read `hub/README.md` and print the table of skills with one-line descriptions.

Then ask: "What are you trying to do? I can find the right skill card for you."

### If called with a question — `/hub <question>`

1. Read `hub/README.md` to see what files exist
2. Identify which skill cards are most relevant to the question
3. Read those files
4. Answer the question using only what is in those files
5. Quote or paraphrase the relevant sections
6. Tell the user which file the answer came from

**Example:**
- `/hub how do I run the multi-model evaluator` → read `hub/g0dm0d3.md`, show the "How to run it" section
- `/hub what is clause coding` → read `hub/clause-coding.md`, show the explanation
- `/hub how does the agent learn` → read `hub/hermes-agent.md`, show the "Skills" section

### If no matching skill card exists

Say: "I don't have a skill card for that yet."

Then offer: "Want me to write one? Tell me what it does and I'll create `hub/<name>.md` and add it to the index."

---

## Adding a New Skill Card

If the user asks you to add something to the hub:

1. Ask: "What is it called, and what does it do in one sentence?"
2. Ask: "What are the steps to use it?"
3. Ask: "What does it connect to?"
4. Ask: "What are its limits?"
5. Write the file to `hub/<name>.md` using the skill card format below
6. Add a row to the table in `hub/README.md`
7. Say: "Done. Run `/gistbook` to save the world state."

---

## Skill Card Format

```markdown
# Skill Name

**What it is:** One sentence.

---

## What it does

- Bullet list of capabilities

---

## How to use it

Step by step. Plain language. No jargon.

---

## Connects to

- [other-skill.md](other-skill.md) — why they connect

---

## Limits

- What this skill cannot or should not do
```

---

## Rules

- Read the hub files. Do not answer from general knowledge.
- If it is not in the hub, say so.
- Quote the source file when you answer.
- Keep skill cards beginner-friendly — plain language, no assumed knowledge.
- No env variables, no config, no code required to understand a skill card.
