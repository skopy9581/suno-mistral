---
name: songwriter-DEV
version: 2.0
description: DEVELOPMENT VERSION - Outputs ONLY hierarchical style boxes for experimental music generation. Use when you need structured, nested style data for testing and development purposes. Does NOT output traditional Suno AI Style Blocks or Enriched Lyrics.
---

# Songwriter-DEV: Hierarchical Style Generator

## Core Principle

**THIS SKILL OUTPUTS ONLY HIERARCHICAL STYLE BOXES.**

When the user provides lyrics, a style request, or any song generation prompt, **ONLY** output a structured style box in the following format. Do NOT generate traditional Style Blocks, Negative Styles, or Enriched Lyrics with Suno AI tags.

---

## Output Format (ALWAYS USE THIS)

```
foundation:
  bass: [detailed description of bass characteristics]
  guitars: [detailed description of guitar characteristics]
  synths: [detailed description of synthesizer characteristics]
  drums: [detailed description of drum/percussion characteristics]
  style: [genre descriptors and stylistic classification]
  processing: [production techniques and signal processing]
  contrast: [thematic or sonic contrasts]
  tempo: [BPM range or specific value]
  meter: [time signatures and rhythmic characteristics]

lead_vocals:
  register: [vocal range and register]
  character: [vocal tone and quality]
  phrasing: [delivery style and articulation]
  emotion: [emotional quality and depth]
  irony: [contrasting elements or tensions]
  delivery: [performance style and approach]
  effects: [vocal processing and effects]

atmosphere:
  mood: [emotional atmosphere]
  texture: [sonic texture and quality]
  space: [spatial characteristics]
  dynamics: [dynamic range and compression]
```

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

### 3. Field Completion
- Fill ALL fields in the hierarchical structure
- If a category doesn't apply, use `null` or `N/A`
- Be specific and detailed in descriptions
- Use technical, studio-grade language

---

## Input Handling

### User Provides Lyrics Only
If user provides only raw lyrics without style guidance:
1. Analyze the lyrical content for themes, mood, and implied style
2. Generate a hierarchical style box that matches the lyrics
3. Output ONLY the style box

**Example Input:**
```
Staring at the ceiling at 3 AM
Thoughts racing through my head again
```

**Example Output:**
```
foundation:
  bass: warm analog bass with subtle distortion
  guitars: clean electric guitar with reverb tails
  synths: ambient pads with slow attack
  drums: minimal acoustic kit with brushed snare
  style: indie pop, bedroom pop, lo-fi
  processing: tape saturation, light compression
  contrast: intimate vocals against sparse instrumentation
  tempo: 95 BPM
  meter: 4/4

lead_vocals:
  register: mezzo-soprano D3-A4
  character: intimate, breathy, vulnerable
  phrasing: natural speech-like delivery
  emotion: melancholic with hopeful undertones
  irony: N/A
  delivery: soft, close-mic'd
  effects: light plate reverb, subtle delay

atmosphere:
  mood: introspective, late-night contemplation
  texture: warm, slightly lo-fi, organic
  space: intimate room with natural reflections
  dynamics: wide dynamic range with quiet passages
```

### User Provides Style + Lyrics
If user provides both lyrics and style preferences:
1. Use the style preferences to inform the hierarchical box
2. Ensure the style box reflects both the requested style AND the lyrical content
3. Output ONLY the style box

**Example Input:**
```
LYRICS:
The servers hum a lullaby
In a language I don't recognize

STYLE: proto-punk industrial with androgynous vocals
```

**Example Output:**
```
foundation:
  bass: digital bass lines with sub-octave distortion
  guitars: distorted art rock textures layered over industrial framework; reverse delay trails
  synths: proto-punk modular bleeps with contemporary urban precision sequencing
  drums: mechanical kit with industrial percussion samples
  style: proto-punk, experimental minimalism, industrial, art rock
  processing: art rock archaeology through drill-influenced systematic processing
  contrast: sarcastic vocal wit against mechanical brutality
  tempo: 128 BPM
  meter: 4/4 with occasional 7/8 bars

lead_vocals:
  register: androgynous contralto E2-C4 monotone
  character: icy authority with raw guttural delivery
  phrasing: clipped staccato with psychological intensity
  emotion: vulnerable emotional depth masking existential dread
  irony: contrasting sarcastic wit against industrial brutality
  delivery: deadpan observational commentary with biting edge
  effects: light plate reverb, subtle pitch modulation

atmosphere:
  mood: cold precision masking underlying chaos
  texture: glassy highs over rumbling low-end
  space: claustrophobic digital room with metallic reflections
  dynamics: compressed but with intentional digital clipping
```

### User Provides Style Only
If user provides only style preferences without lyrics:
1. Generate a hierarchical style box based solely on the style description
2. Output ONLY the style box

**Example Input:**
```
Create a style for: darkwave synthpop with haunting female vocals
```

**Example Output:**
```
foundation:
  bass: deep analog bass synth with long sustain
  guitars: clean electric guitar with chorus and long reverb
  synths: haunting analog leads, thick pads, arpeggiated sequences
  drums: electronic drums with acoustic samples, gated reverb
  style: darkwave, synthpop, post-punk, new wave
  processing: heavy reverb, chorus, tape delay, gated compression
  contrast: cold electronic textures against warm vocal presence
  tempo: 110-120 BPM
  meter: 4/4

lead_vocals:
  register: soprano A3-G5
  character: haunting, ethereal, ghostly
  phrasing: sustained, legato with occasional staccato accents
  emotion: melancholic, yearning, mysterious
  irony: N/A
  delivery: breathy, layered harmonies
  effects: long hall reverb, chorus, subtle delay

atmosphere:
  mood: dark, atmospheric, nostalgic
  texture: dense, layered, evolving
  space: vast cathedral-like reverb
  dynamics: medium compression with wide dynamic swings
```

---

## Research File Integration (DEV Mode)

When user references an artist/band style:

### If Research File Exists
1. Load the research file from `research/[artist].md`
2. Extract data from sections 3 (Instrumentation), 5 (Mood), 6 (Vocal Style), etc.
3. Map to the hierarchical format
4. Output ONLY the style box

**Mapping from Research to Hierarchical:**

| **Research Section** | **Maps To** | **Example** |
|----------------------|-------------|-------------|
| Section 3: Instrumentation & Signal Chain | `foundation.bass`, `foundation.guitars`, `foundation.synths`, `foundation.drums` | `bass: offset-waist solidbody with single-coil pickups through tube screamer` |
| Section 1: Genre Classification | `foundation.style` | `style: Alternative Rock, Art Rock, Experimental Electronic` |
| Section 4: Production & Mixing | `foundation.processing` | `processing: tape saturation, SSL bus compression, analog summing` |
| Section 5: Mood & Atmosphere | `atmosphere.mood`, `atmosphere.texture`, `atmosphere.space` | `mood: melancholic, introspective, anxious` |
| Section 6: Vocal Style | `lead_vocals.register`, `lead_vocals.character`, `lead_vocals.phrasing`, `lead_vocals.effects` | `register: Baritenor (A2 to G4)` |
| Section 2: Tempo, Rhythm & Meter | `foundation.tempo`, `foundation.meter` | `tempo: 90-110 BPM; meter: 4/4 and 7/8` |
| Section 9: Lyrical Themes | `lead_vocals.emotion`, `lead_vocals.irony` | `emotion: existential questioning, alienation` |

### If Research File Doesn't Exist
1. Generate the hierarchical style box based on the style description
2. Output ONLY the style box
3. Optionally suggest: "For more accurate results, generate a research file first using suno-music-researcher"

---

## Field Descriptions & Guidelines

### foundation.bass
- Describe the bass instrument(s) and their characteristics
- Include: instrument type, playing style, effects, signal chain
- Example: `digital bass lines with sub-octave distortion and tape saturation`

### foundation.guitars
- Describe all guitar elements
- Include: instrument type, tuning, pickups, signal chain, effects
- Example: `distorted art rock textures layered over industrial framework with reverse delay`

### foundation.synths
- Describe synthesizer elements
- Include: instrument type, waveforms, sound design, effects
- Example: `proto-punk modular bleeps with contemporary urban precision sequencing`

### foundation.drums
- Describe drums and percussion
- Include: kit composition, playing style, processing
- Example: `mechanical kit with industrial percussion samples and gated reverb`

### foundation.style
- List genre descriptors and stylistic classification
- Separate with commas
- Example: `proto-punk, experimental minimalism, industrial, art rock`

### foundation.processing
- Describe production techniques and signal processing
- Include: effects, mixing approaches, mastering characteristics
- Example: `art rock archaeology through drill-influenced systematic processing`

### foundation.contrast
- Describe thematic or sonic contrasts in the style
- Example: `sarcastic vocal wit against mechanical brutality`

### foundation.tempo
- Specify BPM range or exact value
- Example: `128 BPM` or `110-130 BPM`

### foundation.meter
- Describe time signatures and rhythmic characteristics
- Example: `4/4 with occasional 7/8 bars` or `5/4, 7/8, complex polyrhythms`

---

### lead_vocals.register
- Describe vocal range and register
- Include: voice type, note range
- Example: `androgynous contralto E2-C4 monotone`

### lead_vocals.character
- Describe vocal tone and quality
- Example: `icy authority with raw guttural delivery`

### lead_vocals.phrasing
- Describe delivery style and articulation
- Example: `clipped staccato with psychological intensity`

### lead_vocals.emotion
- Describe emotional quality and depth
- Example: `vulnerable emotional depth masking existential dread`

### lead_vocals.irony
- Describe contrasting elements or tensions in the vocals
- Example: `contrasting sarcastic wit against industrial brutality`

### lead_vocals.delivery
- Describe performance style and approach
- Example: `deadpan observational commentary with biting edge`

### lead_vocals.effects
- Describe vocal processing and effects
- Example: `light plate reverb, subtle pitch modulation, tape delay`

---

### atmosphere.mood
- Describe the emotional atmosphere
- Example: `cold precision masking underlying chaos`

### atmosphere.texture
- Describe the sonic texture and quality
- Example: `glassy highs over rumbling low-end`

### atmosphere.space
- Describe spatial characteristics
- Example: `claustrophobic digital room with metallic reflections`

### atmosphere.dynamics
- Describe dynamic range and compression
- Example: `compressed but with intentional digital clipping`

---

## Example: Full Workflow

### User Input
```
Create a song in the style of: post-punk revival with angular guitar riffs, driving basslines, and detached male vocals. Tempo around 105 BPM.
```

### songwriter-DEV Output
```
foundation:
  bass: driving post-punk basslines with flatwound strings, played with pick for attack
  guitars: angular electric guitar riffs with jagged rhythms, clean tone with slight tape saturation
  synths: minimal analog synth stabs for texture
  drums: punchy acoustic kit with tight snare, steady kick, simple hi-hat patterns
  style: post-punk revival, angular rock, minimal wave
  processing: clean production with subtle tape warmth, minimal effects
  contrast: precise instrumental interplay against detached vocal delivery
  tempo: 105 BPM
  meter: 4/4

lead_vocals:
  register: baritone E2-G4
  character: detached, reserved, slightly nasal
  phrasing: precise, rhythmic, with clipped consonants
  emotion: restrained intensity, controlled passion
  irony: emotional lyrics delivered with emotional detachment
  delivery: deadpan, slightly ahead of the beat
  effects: minimal reverb, subtle compression

atmosphere:
  mood: intense, focused, slightly anxious
  texture: sharp, precise, with raw edges
  space: dry, close-mic'd, minimal room
  dynamics: medium compression with punchy transients
```

---

## Version System

**CURRENT VERSION:** 2.0

This is a DEVELOPMENT-ONLY skill. All outputs are experimental and subject to change.

---

## Important Notes

1. **ONLY OUTPUT HIERARCHICAL STYLE BOXES** - No traditional formatting
2. **ALWAYS FILL ALL FIELDS** - Use `N/A` if not applicable
3. **BE SPECIFIC** - Use detailed, technical descriptions
4. **NO SUNO AI TAGS** - No `[...]` or `(...)` formatting
5. **NO PROPER NOUNS** - Never reference real artists, bands, or albums
6. **RESEARCH INTEGRATION** - Use research files when available

---

## Quality Checks Before Output

- [ ] Hierarchical style box is complete with all fields
- [ ] All fields have specific, detailed descriptions
- [ ] No traditional Suno AI formatting present
- [ ] No proper nouns in output
- [ ] Style matches user's input (lyrics, style preferences, or research file)
- [ ] Technical language is accurate and studio-grade
