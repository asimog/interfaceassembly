# /gistbook — Save the World

When the user runs `/gistbook`, write a gistbook snapshot of the current world state.

The gistbook is the save file. It captures what the world is, what changed, and where it is going.

---

## Steps

### 1. Read everything

Read in this order:
- `world/WORLD.md` — world name and purpose
- All files in `world/clauses/` — every defined box
- The latest file in `world/gistbook/` (if any) — to know what changed since last snapshot
- Recent git log if available — to understand what was built recently

### 2. Determine the version

If a previous snapshot exists, increment its version by 1. If this is the first snapshot, version is 1.

### 3. Determine what changed

Compare the current clause files against what the previous snapshot described. List what is new, what was modified, and what was removed.

If this is the first snapshot, "what changed" is "initial world definition".

### 4. Write the snapshot file

Filename: `world/gistbook/YYYY-MM-DD-<slug>.md`

The slug should be 2-4 words describing the most significant thing that changed or was added, hyphenated. Example: `2026-03-30-added-search-box.md` or `2026-03-30-initial-world.md`.

Use the format from `GISTBOOK.md`.

### 5. Confirm

Tell the user: "Snapshot saved to `world/gistbook/<filename>`. The world is now recoverable from this point."

---

## Snapshot Format

```markdown
---
gistbook: true
world: <WorldName>
snapshot: <ISO 8601 timestamp>
version: <integer>
---

# Gistbook — <WorldName> — <YYYY-MM-DD>

## The World

<One paragraph. What is this world for. Who builds in it. What it is trying to do.>

## What Exists

<One line per clause. Include version. Include one-phrase summary of what it owns.>

- **BoxName** (v1) — owns: field_one, field_two
- **OtherBox** (v1) — owns: field_three, field_four

## What Changed

<Since the last snapshot, what shifted. Be specific. If this is the first snapshot, say "Initial world definition.">

## What Connects

<Key interfaces between boxes. Which boxes talk to which, and what flows between them.>

- BoxA → BoxB: sends X on Y event
- BoxB → BoxC: reads Z through the Q interface

## What Is Next

<The next box that needs to exist, or the next interface that needs to be defined, or the next piece of work inside an existing box.>

## Notes

<Decisions made. Paths not taken. Constraints discovered. Anything the builder wants preserved.>
```

---

## Rules to Follow

- Never delete old snapshots. Write a new file each time.
- The snapshot must stand alone. A reader with no other files should understand the world from the snapshot.
- If the world has not changed since the last snapshot, say so and skip writing a new file: "No structural changes since the last snapshot. Run `/clause` or `/build` first."
- The latest snapshot is the truth. If the code contradicts it, the code needs updating.

---

## After Writing

Offer next steps:
- "Run `/world` to see the full structure."
- "Run `/clause <Name>` to define the next box."
- "Run `/build <request>` to continue building."
