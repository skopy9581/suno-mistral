# Testing Workspace

Test harness for the skill suite, focused on the Suno MCP connector send
contract.

## The problem these tests guard against

When the Suno MCP connector (`suno_44bb`) is connected, every create/send
function goes through `suno_44bb_audio-create` (or `suno_44bb_audio-covers-create`).
The negatives (Exclude Styles / Negative Styles box) must be sent with them as
the separate `negative_style` field on every call. Two failure modes are
tested:

1. **Dropped negatives** — a skill emits a Negative Styles / Exclude Styles
   box but never maps it to `negative_style`, so the send goes out without
   negatives.
2. **Inlined negatives** — a Style-box template instructs exclusions inside the
   Style prompt (e.g. `[Explicit exclusions]`). Suno reads a dash-prefixed
   token as the *positive* word, and the connector only accepts negatives via
   `negative_style`, so inlined negatives both inject the banned genre and
   never reach the exclude field.

## Running

From the repo root (stdlib only, Python 3):

```
python3 testing/test_connector_negatives.py
```

The suite scans every `skills/*/SKILL.md` and asserts:

- any skill documenting a `suno_44bb` create call maps negatives to
  `negative_style` in the same file;
- any skill emitting a Negative Styles / Exclude Styles box also has that
  `negative_style` send mapping;
- no Style-box template contains inline-exclusion markers;
- a simulated connector send built from `fixtures/sample_brief.json` carries
  `negative_style` (plus `model` and `workspace_id`, per the every-send rule)
  and a Style field free of inline negations.
