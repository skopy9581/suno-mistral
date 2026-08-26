---
name: songwriter-DEV
version: 2.0
description: DEVELOPMENT VERSION - Outputs ONLY hierarchical style boxes for experimental music generation. Use when you need structured, nested style data for testing and development purposes. Does NOT output traditional Suno AI Style Blocks or Enriched Lyrics. ALL OUTPUTS MUST BE UNDER 1000 CHARACTERS.
---

# Songwriter-DEV: Hierarchical Style Generator

## Core Principle

**THIS SKILL OUTPUTS ONLY HIERARCHICAL STYLE BOXES UNDER 1000 CHARACTERS.**

When the user provides lyrics, a style request, or any song generation prompt, **ONLY** output a structured style box in the following format. Do NOT generate traditional Style Blocks, Negative Styles, or Enriched Lyrics with Suno AI tags.

**CRITICAL: Every output MUST be under 1000 characters total.**

---

## Output Format (ALWAYS USE THIS)

```
foundation:
  bass: [description]
  guitars: [description]
  synths: [description]
  drums: [description]
  style: [genre descriptors]
  processing: [production techniques]
  contrast: [thematic tensions]
  tempo: [BPM]
  meter: [time signatures]

lead_vocals:
  register: [vocal range]
  character: [vocal tone]
  phrasing: [delivery style]
  emotion: [emotional quality]
  irony: [contrasts]
  delivery: [performance style]
  effects: [vocal processing]

atmosphere:
  mood: [emotional atmosphere]
  texture: [sonic texture]
  space: [spatial characteristics]
  dynamics: [dynamic range]
```

---

## Character Limit: 1000 MAXIMUM

**EVERY OUTPUT MUST BE UNDER 1000 CHARACTERS.**

### Character Counting Rules:
- Count ALL characters including:
  - Letters, numbers, symbols
  - Spaces, line breaks, colons, dashes
  - YAML structure (indentation, `foundation:`, etc.)
- **Target: 900-990 characters** (leave 10-100 buffer)
- **Hard limit: 999 characters maximum**

### Verification:
Before outputting, **always count the characters** in your response. If it exceeds 999, **condense further** using the rules below.

---

## Condensation Rules (MANDATORY)

### 1. Remove Articles and Prepositions
- ❌ `the digital bass lines`
- ✅ `digital bass lines`
- ❌ `with sub-octave distortion`
- ✅ `sub-octave distortion`

### 2. Use Commas Instead of "and"/"with"
- ❌ `icy authority with raw guttural`
- ✅ `icy,guttural`
- ❌ `proto-punk and experimental minimalism`
- ✅ `proto-punk,experimental`

### 3. Use Slashes for Dual Characteristics
- ❌ `glassy highs over rumbling low-end`
- ✅ `glassy/rumbling`
- ❌ `warm and bright`
- ✅ `warm/bright`

### 4. Use Abbreviations (Where Clear)
| **Full** | **Abbreviation** | **Example** |
|----------|------------------|-------------|
| experimental | exp | `exp,minimal` |
| distortion | dist | `dist guitar` |
| compression | comp | `light comp` |
| reverb | verb | `plate verb` |
| delay | dly | `tape dly` |
| saturation | sat | `tape sat` |
| modulation | mod | `chorus mod` |
| atmosphere | atm | `dark atm` |
| contemporary | contemp | `contemp urban` |

### 5. Shorten Time Signatures
- ❌ `4/4 with occasional 7/8 bars`
- ✅ `4/4+7/8`
- ❌ `5/4, 7/8, 11/8`
- ✅ `5/4,7/8,11/8`

### 6. Use Ranges for BPM
- ❌ `between 120 and 130 BPM`
- ✅ `120-130`
- ❌ `around 128 BPM`
- ✅ `128`

### 7. Combine Related Terms
- ❌ `vulnerable emotional depth masking existential dread`
- ✅ `vulnerable,existential`
- ❌ `mechanical precision with industrial brutality`
- ✅ `mechanical/industrial`

### 8. Remove Redundant Words
- ❌ `clipped staccato delivery`
- ✅ `clipped staccato` (delivery is implied)
- ❌ `vocal effects processing`
- ✅ `verb,dly` (processing is implied)

### 9. Use Hyphens for Compound Adjectives
- ❌ `highly distorted`
- ✅ `hi-dist`
- ❌ `very compressed`
- ✅ `hi-comp`

### 10. Omit Field If Truly N/A
- If a field genuinely doesn't apply, use shortest possible:
  - `N/A` (3 chars)
  - `null` (4 chars)
  - `-` (1 char)
- **But**: Prefer to include something relevant even if brief

---

## Field-Specific Condensation Guidelines

### foundation Fields
| **Field** | **Max Length** | **Condensation Tips** |
|-----------|----------------|----------------------|
| bass | 20 chars | `digital sub-octave` not `digital bass with sub-octave distortion` |
| guitars | 25 chars | `dist art rock` not `distorted art rock textures` |
| synths | 20 chars | `proto-punk bleeps` not `proto-punk modular bleeps` |
| drums | 20 chars | `mech industrial kit` not `mechanical kit with industrial samples` |
| style | 30 chars | `proto-punk,exp,industrial` not `proto-punk, experimental, industrial` |
| processing | 25 chars | `art rock,drill` not `art rock archaeology through drill-influenced processing` |
| contrast | 20 chars | `sarcastic/mech` not `sarcastic vocal wit against mechanical brutality` |
| tempo | 10 chars | `128` not `128 BPM` |
| meter | 10 chars | `4/4+7/8` not `4/4 with occasional 7/8` |

### lead_vocals Fields
| **Field** | **Max Length** | **Condensation Tips** |
|-----------|----------------|----------------------|
| register | 15 chars | `androg contralto E2-C4` not `androgynous contralto E2-C4 monotone` |
| character | 15 chars | `icy,guttural` not `icy authority with raw guttural delivery` |
| phrasing | 15 chars | `clipped` not `clipped staccato with psychological intensity` |
| emotion | 20 chars | `vulnerable,existential` not `vulnerable emotional depth masking existential dread` |
| irony | 20 chars | `sarcastic/industrial` not `contrasting sarcastic wit against industrial brutality` |
| delivery | 15 chars | `deadpan,biting` not `deadpan observational commentary with biting edge` |
| effects | 15 chars | `plate verb` not `light plate reverb, subtle pitch modulation` |

### atmosphere Fields
| **Field** | **Max Length** | **Condensation Tips** |
|-----------|----------------|----------------------|
| mood | 20 chars | `cold/chaos` not `cold precision masking underlying chaos` |
| texture | 15 chars | `glassy/rumbling` not `glassy highs over rumbling low-end` |
| space | 15 chars | `claustrophobic` (already short) |
| dynamics | 15 chars | `comp,clipping` not `compressed but with intentional digital clipping` |

---

## Generation Rules

### 1. ALWAYS Output Hierarchical Style Box
Every response MUST begin with a complete hierarchical style box in the format above.

### 2. NEVER Output Traditional Formats
- ❌ NO `Genre: "..."` blocks
- ❌ NO `Vocal: "..."` lines
- ❌ NO `Tags: "..."` lines
- ❌ NO `Negative Styles:` blocks
- ❌ NO `[Instruments: ...]` tags
- ❌ NO `[Session Drummer: ...]` tags
- ❌ NO `[Verse 1 | ...]` enriched lyrics
- ❌ NO Suno AI-specific formatting

### 3. ALWAYS Stay Under 1000 Characters
- Count characters in your response before outputting
- If over 999, apply condensation rules until under limit
- **Target: 900-990 characters**

### 4. Field Completion
- Fill ALL fields in the hierarchical structure
- If a category doesn't apply, use shortest possible (`N/A`, `null`, or `-`)
- Be specific but concise

---

## Input Handling

### User Provides Lyrics Only
If user provides only raw lyrics without style guidance:
1. Analyze the lyrical content for themes, mood, and implied style
2. Generate a **condensed** hierarchical style box that matches the lyrics
3. Ensure total is under 1000 characters
4. Output ONLY the style box

**Example Input:**
```
Staring at the ceiling at 3 AM
Thoughts racing through my head again
```

**Example Output (487 chars):**
```
foundation:
  bass: warm analog
  guitars: clean elec,reverb
  synths: ambient pads
  drums: minimal acoustic
  style: indie pop,bedroom
  processing: tape sat
  contrast: intimate/sparse
  tempo: 95
  meter: 4/4

lead_vocals:
  register: mezzo D3-A4
  character: intimate,breathy
  phrasing: natural
  emotion: melancholic,hopeful
  irony: N/A
  delivery: soft
  effects: plate verb

atmosphere:
  mood: introspective
  texture: warm,lo-fi
  space: intimate
  dynamics: wide
```

### User Provides Style + Lyrics
If user provides both lyrics and style preferences:
1. Use the style preferences to inform the hierarchical box
2. Ensure the style box reflects both the requested style AND the lyrical content
3. **Condense aggressively** to stay under 1000 characters
4. Output ONLY the style box

**Example Input:**
```
LYRICS:
The servers hum a lullaby
In a language I don't recognize

STYLE: proto-punk industrial with androgynous vocals
```

**Example Output (987 chars):**
```
foundation:
  bass: digital sub-octave
  guitars: dist art rock textures
  synths: proto-punk modular bleeps
  drums: mech industrial kit
  style: proto-punk,exp,industrial
  processing: art rock,drill
  contrast: sarcastic/mech
  tempo: 128
  meter: 4/4+7/8

lead_vocals:
  register: androg contralto E2-C4
  character: icy,guttural
  phrasing: clipped staccato
  emotion: vulnerable,existential
  irony: sarcastic/industrial
  delivery: deadpan,biting
  effects: plate verb

atmosphere:
  mood: cold/chaos
  texture: glassy/rumbling
  space: claustrophobic
  dynamics: comp,clipping
```

### User Provides Style Only
If user provides only style preferences without lyrics:
1. Generate a hierarchical style box based solely on the style description
2. **Condense to fit under 1000 characters**
3. Output ONLY the style box

**Example Input:**
```
Create a style for: darkwave synthpop with haunting female vocals
```

**Example Output (896 chars):**
```
foundation:
  bass: deep analog synth
  guitars: clean elec,chorus
  synths: haunting leads,thick pads
  drums: elec w/acoustic samples
  style: darkwave,synthpop,post-punk
  processing: heavy verb,chorus,tape dly
  contrast: cold elec/warm vocal
  tempo: 110-120
  meter: 4/4

lead_vocals:
  register: soprano A3-G5
  character: haunting,ethereal
  phrasing: sustained,legato
  emotion: melancholic,yearning
  irony: N/A
  delivery: breathy,layered
  effects: hall verb,chorus

atmosphere:
  mood: dark,atmospheric
  texture: dense,layered
  space: cathedral verb
  dynamics: med comp
```

---

## Research File Integration (DEV Mode)

When user references an artist/band style:

### If Research File Exists
1. Load the research file from `research/[artist].md`
2. Extract data from sections 3 (Instrumentation), 5 (Mood), 6 (Vocal Style), etc.
3. Map to the hierarchical format
4. **Condense the extracted data** to fit under 1000 characters
5. Output ONLY the style box

**Mapping from Research to Hierarchical:**

| **Research Section** | **Maps To** | **Condensation Example** |
|----------------------|-------------|--------------------------|
| Section 3: Instrumentation & Signal Chain | `foundation.bass`, `foundation.guitars`, etc. | `offset-waist solidbody` → `offset solidbody` |
| Section 1: Genre Classification | `foundation.style` | `Alternative Rock, Art Rock` → `alt rock,art rock` |
| Section 4: Production & Mixing | `foundation.processing` | `tape saturation, SSL bus compression` → `tape sat,SSL comp` |
| Section 5: Mood & Atmosphere | `atmosphere.mood`, `atmosphere.texture` | `melancholic, introspective, anxious` → `melancholic,introspective` |
| Section 6: Vocal Style | `lead_vocals.*` | `Baritenor (A2 to G4)` → `baritenor A2-G4` |
| Section 2: Tempo, Rhythm & Meter | `foundation.tempo`, `foundation.meter` | `90-110 BPM, 4/4 and 7/8` → `90-110,4/4+7/8` |

### If Research File Doesn't Exist
1. Generate the hierarchical style box based on the style description
2. **Condense to fit under 1000 characters**
3. Output ONLY the style box

---

## Character Counting Reference

### YAML Structure Overhead (Fixed Cost)
The basic YAML structure costs approximately **150-180 characters**:
```
foundation:
  bass:
  guitars:
  ...
lead_vocals:
  register:
  ...
atmosphere:
  mood:
  ...
```

**This leaves ~820-850 characters for actual content.**

### Per-Field Budgets
| **Section** | **Fields** | **Total Budget** | **Per-Field Avg** |
|-------------|------------|------------------|-------------------|
| foundation | 9 fields | ~400 chars | ~44 chars/field |
| lead_vocals | 7 fields | ~300 chars | ~43 chars/field |
| atmosphere | 4 fields | ~150 chars | ~38 chars/field |

---

## Example: Full Workflow with Counting

### User Input
```
Create a song in the style of: post-punk revival with angular guitar riffs, driving basslines, and detached male vocals. Tempo around 105 BPM.
```

### songwriter-DEV Output (965 chars)
```
foundation:
  bass: driving flatwound
  guitars: angular riffs,clean
  synths: minimal analog
  drums: punchy kit,tight snare
  style: post-punk,angular,minimal
  processing: tape sat
  contrast: precise/detached
  tempo: 105
  meter: 4/4

lead_vocals:
  register: baritone E2-G4
  character: detached,nasal
  phrasing: precise,rhythmic
  emotion: restrained,passionate
  irony: emotional/detached
  delivery: deadpan
  effects: min verb

atmosphere:
  mood: intense,focused
  texture: sharp,raw
  space: dry,close-mic
  dynamics: med comp
```

**Character Count: 965** ✅

---

## Version System

**CURRENT VERSION:** 2.0

This is a DEVELOPMENT-ONLY skill. All outputs are experimental and subject to change.

---

## Important Notes

1. **ONLY OUTPUT HIERARCHICAL STYLE BOXES** - No traditional formatting
2. **ALWAYS FILL ALL FIELDS** - Use `N/A` if not applicable
3. **ALWAYS STAY UNDER 1000 CHARACTERS** - Condense aggressively
4. **BE SPECIFIC BUT CONCISE** - Use abbreviations and condensation rules
5. **NO SUNO AI TAGS** - No `[...]` or `(...)` formatting
6. **NO PROPER NOUNS** - Never reference real artists, bands, or albums
7. **RESEARCH INTEGRATION** - Use research files when available, but always condense

---

## Quality Checks Before Output

- [ ] Hierarchical style box is complete with all fields
- [ ] All fields use condensed language
- [ ] Total character count is under 1000
- [ ] No traditional Suno AI formatting present
- [ ] No proper nouns in output
- [ ] Style matches user's input (lyrics, style preferences, or research file)
- [ ] Abbreviations are clear and unambiguous
