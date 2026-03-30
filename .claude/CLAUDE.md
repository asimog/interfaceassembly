# Interface Assembly - Claude Overlay

Read before acting:

- [`README.md`](../README.md)
- [`constitution.md`](../constitution.md)
- [`world/WORLD.md`](../world/WORLD.md)
- all clause files in [`world/clauses/`](../world/clauses/)
- shared contracts in [`world/interfaces/`](../world/interfaces/)
- adapter records in [`world/adapters/`](../world/adapters/)
- the current merkle state in [`world/merkle/current.md`](../world/merkle/current.md)
- the hub in [`hub/README.md`](../hub/README.md)

---

## Named Roles

- `Archivist`
- `Arbiter`
- `WorldBuilder`
- `BlockBuilder`
- `PublicReadiness`

Hermes and G0DM0D3 are tools used by the named roles.

---

## Operating Rules

1. Read the world first.
2. Do not silently expand a box.
3. Shared contracts belong in `world/interfaces/` once they stop being local.
4. External repos and tools enter through `world/adapters/`.
5. Cross-box changes require the requesting block and the owning block.
6. Arbiter resolves contradictions.
7. WorldBuilder ratifies role and boundary shape.
8. Archivist records accepted structure.
9. PublicReadiness runs before public release.

---

## Repo Skills

| Skill | File | What it does |
|-------|------|--------------|
| `/clause <Name>` | `skills/clause.md` | define or revise a sovereign box |
| `/build <request>` | `skills/build.md` | build inside existing boundaries |
| `/block-builder <request>` | `skills/block-builder.md` | intake and scope a new block, repo, or feature |
| `/amend <Target>` | `skills/amend.md` | file accepted structural changes |
| `/conflict <desc>` | `skills/conflict.md` | log a boundary contradiction |
| `/oversee` | `skills/oversee.md` | run the WorldBuilder review |
| `/public-readiness` | `skills/public-readiness.md` | run the public release gate |
| `/gistbook` | `skills/gistbook.md` | write a world snapshot |
| `/hub <question>` | `skills/hub.md` | search the public skill cards |
