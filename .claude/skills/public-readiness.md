# /public-readiness - Release Gate

Use `/public-readiness` before publishing this repo as a public-facing skill or hub.

---

## Read First

1. `README.md`
2. `constitution.md`
3. `world/WORLD.md`
4. all clauses
5. all interfaces
6. all adapters
7. all registries
8. latest gistbook snapshot
9. `world/merkle/current.md`

---

## Checks

1. Can a new reader understand the lifecycle from markdown alone?
2. Are all sovereign boxes defined?
3. Are shared contracts visible?
4. Are external repos and tools visible as adapters?
5. Do the registries match the actual world?
6. Is the merkle state internally consistent?
7. Are there unresolved blockers that make public use misleading?

---

## Output

Write a report to `agents/public-readiness/reports/` with:

- status
- blockers
- caveats
- recommendation
