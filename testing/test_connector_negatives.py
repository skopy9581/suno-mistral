#!/usr/bin/env python3
"""Connector negatives contract tests.

Problem under test: when the Suno MCP connector (`suno_44bb`) is connected,
create/send functions go through `suno_44bb_audio-create` /
`suno_44bb_audio-covers-create`, but the negatives (Exclude Styles / Negative
Styles box) were not sent with them — they must be sent as the separate
`negative_style` field on every create call, never inlined in `style`
(inline dash-negations are read by Suno as the positive word).

Run from the repo root:
    python3 testing/test_connector_negatives.py
"""

import json
import re
import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = REPO_ROOT / "skills"
FIXTURE = Path(__file__).resolve().parent / "fixtures" / "sample_brief.json"

CREATE_CALL_RE = re.compile(r"audio-create|covers-create")
NEGATIVES_BOX_RE = re.compile(r"Negative Styles|Exclude Styles")
INLINE_EXCLUSIONS_MARKER = "[Explicit exclusions]"
NON_BREAKING_HYPHEN = "‑"


def skill_files():
    return sorted(SKILLS_DIR.glob("*/SKILL.md"))


def build_audio_create_call(brief):
    """Reference implementation of the connector send contract.

    Every send defines model and workspace_id, and always carries the
    negatives as their own `negative_style` field.
    """
    return {
        "title": brief["title"],
        "model": brief["model"],
        "style": brief["style"],
        "lyrics": brief["lyrics"],
        "negative_style": brief["exclude_styles"],
        "workspace_id": brief["workspace_id"],
    }


class ConnectorNegativesContractTest(unittest.TestCase):
    def test_skills_present(self):
        files = skill_files()
        self.assertGreaterEqual(len(files), 5, "expected the skills directory to be scanned")

    def test_connector_create_calls_carry_negative_style(self):
        """Any skill that documents a suno_44bb create call must map the
        negatives box onto the `negative_style` parameter in the same file."""
        offenders = []
        for path in skill_files():
            text = path.read_text(encoding="utf-8")
            if "suno_44bb" in text and CREATE_CALL_RE.search(text):
                if "negative_style" not in text:
                    offenders.append(path.parent.name)
        self.assertEqual(offenders, [], f"create-call contract missing negative_style in: {offenders}")

    def test_every_negatives_box_has_a_send_mapping(self):
        """Every skill that emits a Negative Styles / Exclude Styles output box
        must also tell the model to send it as `negative_style` when the
        connector is connected — otherwise negatives are dropped on send."""
        offenders = []
        for path in skill_files():
            text = path.read_text(encoding="utf-8")
            if NEGATIVES_BOX_RE.search(text) and "negative_style" not in text:
                offenders.append(path.parent.name)
        self.assertEqual(offenders, [], f"negatives box without negative_style send mapping in: {offenders}")

    def test_no_inline_exclusions_in_style_templates(self):
        """Style-box templates must not instruct inline negatives: Suno reads a
        dash-prefixed token as the positive word, and the connector contract
        only accepts negatives via the separate `negative_style` field."""
        offenders = []
        for path in skill_files():
            text = path.read_text(encoding="utf-8")
            if INLINE_EXCLUSIONS_MARKER in text:
                offenders.append(f"{path.parent.name}: {INLINE_EXCLUSIONS_MARKER}")
        self.assertEqual(offenders, [], f"inline exclusions in style template: {offenders}")

    def test_simulated_connector_send_includes_negatives(self):
        brief = json.loads(FIXTURE.read_text(encoding="utf-8"))
        call = build_audio_create_call(brief)
        self.assertIn("negative_style", call)
        self.assertEqual(call["negative_style"], brief["exclude_styles"])
        self.assertTrue(call["negative_style"].strip(), "negatives must not be sent empty")
        self.assertNotIn(INLINE_EXCLUSIONS_MARKER, call["style"])
        self.assertNotIn(NON_BREAKING_HYPHEN, call["style"])
        self.assertIn("model", call, "model must be defined on every send")
        self.assertIn("workspace_id", call, "workspace_id must be defined on every send")


if __name__ == "__main__":
    unittest.main(verbosity=2)
