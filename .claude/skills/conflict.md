# /conflict - Log A Boundary Contradiction

Use `/conflict <description>` when two boxes, interfaces, or adapters contradict each other.

---

## Read First

1. `world/WORLD.md`
2. all involved clause files
3. relevant interface records
4. relevant adapter records
5. prior conflicts for the same boundary

---

## What Counts As A Conflict

- OWNS overlap
- MAY versus MAY NOT collision
- shared contract mismatch
- one block changing another block without owner participation
- adapter overreach into sovereign state
- public-release gate disagreement about what is publishable

---

## Steps

1. Name the exact boundary contradiction.
2. Name the requesting side and the owning side.
3. Read the shared contract, if one exists.
4. Evaluate the minimum coherent resolution.
5. Write a conflict record in `agents/arbiter/conflicts/`.
6. If recurring, write a decision in `agents/arbiter/decisions/`.
7. Route the accepted result to Archivist through `/amend`.

---

## Hard Rule

No cross-box change is valid unless the owning block agent is part of the record.
