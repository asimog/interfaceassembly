from __future__ import annotations

import pathlib
import re
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]
WORLD = ROOT / "world"
CLAUSES = WORLD / "clauses"
INTERFACES = WORLD / "interfaces"
ADAPTERS = WORLD / "adapters"
REGISTRIES = WORLD / "registries"
AGENTS = ROOT / "agents"
HUB = ROOT / "hub"


def read_text(path: pathlib.Path) -> str:
    return path.read_text(encoding="utf-8")


def clause_files() -> list[pathlib.Path]:
    return sorted(
        path
        for path in CLAUSES.glob("*.md")
        if path.name != ".gitkeep"
    )


def interface_files() -> list[pathlib.Path]:
    return sorted(
        path
        for path in INTERFACES.glob("*.md")
        if path.name != "README.md"
    )


def adapter_files() -> list[pathlib.Path]:
    return sorted(
        path
        for path in ADAPTERS.glob("*.md")
        if path.name != "README.md"
    )


def extract_required_field(content: str, key: str) -> str:
    match = re.search(rf"^{re.escape(key)}:\s*(.+)$", content, re.MULTILINE)
    if not match:
        raise AssertionError(f"missing frontmatter field: {key}")
    return match.group(1).strip()


def clause_token_from_name(name: str) -> str:
    special_cases = {
        "ArbiterBox": "A1",
        "ArchivistBox": "A1",
        "BlockBuilderBox": "BB1",
        "G0DM0D3Box": "G1",
        "HermesAgentBox": "HA1",
        "InterfaceRegistryBox": "IR1",
        "PublicReadinessBox": "PR1",
        "WorldBuilderBox": "WB1",
    }
    if name in special_cases:
        return special_cases[name]

    stem = name.removesuffix("Box")
    initials = []
    current = ""
    for char in stem:
        if char.isupper() and current:
            initials.append(current)
            current = char
        else:
            current += char
    if current:
        initials.append(current)
    token_stem = "".join(part[0].upper() for part in initials)
    return f"{token_stem}1"


class InterfaceAssemblyRegressionTests(unittest.TestCase):
    def test_public_entrypoints_exist(self) -> None:
        required = [
            ROOT / "README.md",
            ROOT / "LICENSE",
            ROOT / "constitution.md",
            ROOT / "GISTBOOK.md",
            HUB / "README.md",
            HUB / "interface-assembly.md",
            HUB / "public-readiness.md",
            WORLD / "WORLD.md",
            WORLD / "merkle" / "current.md",
            ROOT / "THIRD_PARTY_NOTICES.md",
            ROOT / "third_party_licenses" / "g0dm0d3-upstream.md",
            ROOT / "third_party_licenses" / "hermes-agent.md",
        ]
        for path in required:
            self.assertTrue(path.exists(), f"missing public entrypoint: {path}")

    def test_every_clause_has_required_structure(self) -> None:
        required_headers = ["clause", "version", "signature", "created", "last_amended", "amendment_ref"]
        required_sections = ["**IS:**", "**OWNS:**", "**MAY:**", "**MAY NOT:**", "**CONNECTS TO:**"]
        for path in clause_files():
            content = read_text(path)
            for field in required_headers:
                extract_required_field(content, field)
            for section in required_sections:
                self.assertIn(section, content, f"{path} missing section {section}")

    def test_merkle_root_matches_current_clauses(self) -> None:
        merkle = read_text(WORLD / "merkle" / "current.md")
        root = extract_required_field(merkle, "merkle_root")
        tokens = []
        for path in clause_files():
            content = read_text(path)
            clause_name = extract_required_field(content, "clause")
            version = extract_required_field(content, "version")
            self.assertEqual(version, "1", f"unexpected version handling in {path}")
            tokens.append(clause_token_from_name(clause_name))
        expected = "ia-root-" + "".join(
            token for _, token in sorted(zip([p.stem for p in clause_files()], tokens), key=lambda item: item[0])
        )
        self.assertEqual(root, expected)

    def test_registries_reference_current_world(self) -> None:
        block_registry = read_text(REGISTRIES / "block-registry.md")
        interface_registry = read_text(REGISTRIES / "interface-registry.md")
        adapter_registry = read_text(REGISTRIES / "adapter-registry.md")
        agent_registry = read_text(REGISTRIES / "agent-registry.md")

        for path in clause_files():
            self.assertIn(path.stem, block_registry, f"block registry missing {path.stem}")

        for path in interface_files():
            self.assertIn(path.stem, interface_registry, f"interface registry missing {path.stem}")

        for path in adapter_files():
            self.assertIn(path.stem, adapter_registry, f"adapter registry missing {path.stem}")

        for role in ["Archivist", "Arbiter", "BlockBuilder", "PublicReadiness", "WorldBuilder"]:
            self.assertIn(role, agent_registry, f"agent registry missing {role}")

    def test_first_party_roles_have_hub_cards_and_agent_specs(self) -> None:
        expected_hub_cards = [
            "archivist.md",
            "arbiter.md",
            "block-builder.md",
            "interface-registry.md",
            "public-readiness.md",
            "worldbuilder.md",
        ]
        for filename in expected_hub_cards:
            self.assertTrue((HUB / filename).exists(), f"missing hub card {filename}")

        expected_agent_specs = [
            AGENTS / "archivist" / "README.md",
            AGENTS / "arbiter" / "README.md",
            AGENTS / "blockbuilder" / "README.md",
            AGENTS / "public-readiness" / "README.md",
            AGENTS / "worldbuilder" / "README.md",
        ]
        for path in expected_agent_specs:
            self.assertTrue(path.exists(), f"missing agent spec {path}")

    def test_vendor_release_basics(self) -> None:
        readme = read_text(ROOT / "README.md")
        self.assertNotIn("## License\n\nMIT", readme)
        self.assertIn("AGPL-3.0-or-later", readme)

        license_text = read_text(ROOT / "LICENSE")
        self.assertIn("GNU AFFERO GENERAL PUBLIC LICENSE", license_text)

        notices = read_text(ROOT / "THIRD_PARTY_NOTICES.md")
        self.assertIn("g0dm0d3-upstream", notices)
        self.assertIn("hermes-agent", notices)
        self.assertIn("AGPL-3.0-or-later", notices)

        nested_git_dirs = sorted(ROOT.glob("agents/vendor/**/.git"))
        self.assertEqual(
            nested_git_dirs,
            [],
            "vendored adapters still contain nested .git directories; remove them before public release",
        )


if __name__ == "__main__":
    unittest.main()
