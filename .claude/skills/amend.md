# /amend - File An Accepted Structural Change

Use `/amend <Target>` when a box, interface, adapter, or registry change has been accepted and must be recorded by Archivist.

---

## Read First

1. `world/WORLD.md`
2. the target file being changed
3. `world/merkle/current.md`
4. relevant shared contracts or adapter records
5. existing files in `world/amendments/`

---

## Supported Target Types

- sovereign box clause
- shared interface
- adapter record
- registry record

---

## Steps

1. Confirm the exact accepted change.
2. Confirm the target type.
3. Check whether the change creates a new conflict.
4. Compute the next amendment number.
5. Write `world/amendments/A<NNN>-<Target>-<slug>.md`.
6. Update the target file.
7. Update `world/merkle/current.md`.
8. Report the new root and accepted target.

---

## Special Rule

If the accepted change affects more than one sovereign box, name the owning box and the requesting box in the amendment body so the record preserves both sides of the boundary.
