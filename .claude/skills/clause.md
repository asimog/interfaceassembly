# /clause - Define Or Revise A Sovereign Box

Use `/clause <Name>` when the work has already been classified as a sovereign box.

If classification is unclear, use `/block-builder` first.

---

## Read First

1. `world/WORLD.md`
2. all files in `world/clauses/`
3. relevant files in `world/interfaces/`
4. `world/registries/block-registry.md`
5. latest gistbook snapshot

---

## Steps

1. Confirm the box name and one-sentence purpose.
2. Check that the work is truly a sovereign box and not a shared interface or adapter.
3. Check OWNS overlap against existing clauses.
4. Draft the clause with full frontmatter:

```markdown
---
clause: BoxName
version: 1
signature: BoxName-v1-YYYYMMDD
created: YYYY-MM-DD
last_amended: YYYY-MM-DD
amendment_ref: BoxName-A1 | none
---
```

5. Fill:
   - IS
   - OWNS
   - MAY
   - MAY NOT
   - CONNECTS TO
6. Update `world/WORLD.md` and `world/registries/block-registry.md`.
7. If the clause is being accepted now, route the structural record through Archivist with `/amend`.

---

## Hard Rules

- One clause, one purpose.
- MAY NOT is required.
- OWNS must be specific and exclusive.
- CONNECTS TO must name real boxes or shared interfaces.
- A new clause should not bypass Archivist if it is being accepted into the world.
