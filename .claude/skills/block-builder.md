# /block-builder - Intake And Scope New Work

Use `/block-builder <request>` when the user is adding a new component, repo, feature family, or boundary.

---

## Read First

1. `README.md`
2. `world/WORLD.md`
3. all clauses
4. relevant interfaces
5. relevant adapters
6. latest gistbook snapshot

---

## Steps

1. Restate the request.
2. Classify the request as:
   - box
   - shared interface
   - adapter
   - sidecar
   - reference only
3. Write or update a proposal in `world/proposals/`.
4. If it is a box, define the scoped role and create or update the clause.
5. If it is a shared contract, place it in `world/interfaces/`.
6. If it is an external repo or tool, create an adapter record in `world/adapters/`.
7. Write a scoped report in `agents/blockbuilder/reports/`.
8. Route accepted structural changes through `/amend`.
9. Route contradictions through `/conflict`.

---

## Hard Rule

If another block must change, involve the owning block and route the disagreement through Arbiter.
