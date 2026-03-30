# /world — Show the Current World

When the user runs `/world`, read the full world structure and present it clearly.

---

## Steps

1. **Read `world/WORLD.md`.** Get the world name and purpose.

2. **Read all clause files in `world/clauses/`.** Collect every defined box.

3. **Read the latest gistbook snapshot** in `world/gistbook/` if any exists (sort by filename, take the last one).

4. **Present the world** in this order:

---

## Output Format

```
# World: <WorldName>

<One sentence about what this world is.>

## Boxes

<For each clause, one block:>

### <BoxName> (v<version>)
IS: <the IS line>
OWNS: <the OWNS fields>
CONNECTS TO: <the other boxes and what flows>

## Connections Map

<A simple text diagram or list showing which boxes connect to which.>
BoxA ──► BoxB   (what flows)
BoxB ──► BoxC   (what flows)

## Status

<From the latest gistbook snapshot: what is working, what changed recently, what is next.>
<If no gistbook exists, say "No snapshot yet. Run /gistbook to save the current state.">
```

---

## If the World Is Empty

If `world/WORLD.md` has not been filled in or no clauses exist yet, say:

"The world has not been named yet. Start with:
1. Edit `world/WORLD.md` — give your world a name and one sentence.
2. Run `/clause <BoxName>` to define your first box."

---

## After Showing

Offer next steps:
- "Run `/clause <Name>` to add a new box."
- "Run `/build <request>` to build something inside the current structure."
- "Run `/gistbook` to save a snapshot of the world as it is now."
