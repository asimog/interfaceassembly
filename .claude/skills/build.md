# /build - Build Inside The World

Use `/build <request>` when the user wants implementation work inside an already-accepted boundary.

If the request creates a new component, new repo, new feature family, or new boundary, route it to `/block-builder` first.

---

## Read First

1. `world/WORLD.md`
2. all files in `world/clauses/`
3. relevant files in `world/interfaces/`
4. relevant files in `world/adapters/`
5. latest gistbook snapshot

---

## Steps

1. Restate the request in one sentence.
2. Name the owning box.
3. Verify the box already exists.
4. Check whether the request changes a shared contract or another box's OWNS.
5. If yes, stop and route through `/conflict`, `/amend`, or `/block-builder`.
6. If no, build inside the owning box only.
7. Report:
   - what was built
   - which box owns it
   - whether any shared interface or adapter changed

---

## Boundary Rules

- Do not invent a new box during `/build`.
- Do not modify another box without its owner participating.
- Do not treat a vendored tool as a state owner.
- Do not copy shared contract language into multiple boxes if it belongs in `world/interfaces/`.

---

## Subagent Rule

If delegation is needed, each subagent is scoped to one existing box only.

If the work crosses boxes, use `/block-builder` so the BlockBuilder workflow can classify and coordinate the change.
