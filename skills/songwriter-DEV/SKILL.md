---
name: songwriter-DEV
version: 2.0
description: DEVELOPMENT VERSION - Outputs hierarchical style boxes AND Suno-compatible lyrics boxes with experimental formatting. Does NOT output traditional Style Blocks (Genre/Vocal/Tags). Includes negative styles when applicable. Each section is in a markdown code block for easy copy-paste.
---

# Songwriter-DEV: Hierarchical Style + Lyrics Box Generator

## Core Principle

**THIS SKILL OUTPUTS THREE SEPARATE MARKDOWN CODE BLOCKS:**

1. **Hierarchical Style Box** (DEV format, under 1000 chars)
2. **Lyrics Box** (Suno-compatible with tags)
3. **Negative Styles** (comma-separated list)

Each section is in its own **markdown code block** for easy copy-paste.

**DOES NOT OUTPUT:**
- Traditional Style Block (`Genre: "..."`, `Vocal: "..."`, `Tags: "..."`)

---

## Output Structure

Every response must contain these THREE MARKDOWN CODE BLOCKS:

````markdown
```
=== HIERARCHICAL STYLE BOX ===
[Your hierarchical YAML-style box under 1000 chars]
```

```
=== LYRICS BOX ===
[Instruments: ...]
[Session Drummer: ...]

[Verse 1 | ...]
lyric line 1
lyric line 2

[Chorus | ...]
lyric line 1
lyric line 2
```

```
=== NEGATIVE STYLES ===
[comma-separated list when applicable]
```
````

---

## Hierarchical Style Box Rules

### Character Limit: 1000 MAXIMUM
Every hierarchical style box MUST be under 1000 characters total.

### Condensation Rules (MANDATORY)
1. **Remove articles**: `the digital bass` → `digital bass`
2. **Use commas**: `icy with guttural` → `icy,guttural`
3. **Use slashes**: `glassy over rumbling` → `glassy/rumbling`
4. **Abbreviate**: `experimental` → `exp`, `reverb` → `verb`, `compression` → `comp`
5. **Shorten signatures**: `4/4 with 7/8` → `4/4+7/8`
6. **Combine terms**: `vulnerable emotional depth` → `vulnerable,existential`

### Format
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

## Lyrics Box Rules

### Required Tags
1. **`[Instruments: ...]`** - MUST be first tag in lyrics box
2. **`[Session Drummer: ...]`** - MUST be second tag in lyrics box

### Tag Formatting
- Use square brackets for ALL meta tags: `[Verse 1 | Vocal: ... | Mood: ...]`
- Separate categories with pipes: `[Section | Category1: Value | Category2: Value]`
- Max 2-3 categories per section tag
- Parentheses for ad-libs/vocalizations: `(oh yeah)`, `(woah)`

### Section Structure
- Always include: Intro, Verse, Chorus, Bridge, Outro (as applicable)
- Use consistent section naming: `[Intro]`, `[Verse 1]`, `[Chorus]`, `[Bridge]`, `[Outro]`
- Add meta tags to sections: `[Verse 1 | Vocal: Gritty | Energy: High]`

### Drum Tags
- **Session Drummer** must include:
  - Kit composition (kick, snare, toms, cymbals)
  - Groove style (natural, mechanical, swung, etc.)
  - Techniques (ghost notes, flams, etc.)
- Example: `[Session Drummer: Full kit with 22" kick, 14" snare, 12/13/16" toms | Groove: Natural swing, ghost notes]`

---

## Negative Styles Rules

### When to Include
- Always include if user specifies conflicting genres
- Include by default for most requests
- Use common exclusions: `drum machine, electronic drums, synthetic percussion, plastic drums`

### Format
- Comma-separated list
- No line breaks
- Max 5-7 items

### Common Negative Styles by Genre
| **Genre** | **Negative Styles** |
|-----------|---------------------|
| Rock/Metal | Jazz, Country, Acoustic Folk, drum machine, electronic drums, synthetic percussion, plastic drums |
| Electronic | Acoustic Folk, Bluegrass, Country, drum circle, hand percussion |
| Hip-Hop | Polka, Classical, Opera, acoustic guitar, live orchestra |
| Pop | Death Metal, Black Metal, Noise, extreme distortion |
| Classical | Trap, EDM, Dubstep, autotune, 808 bass |

---

## Complete Output Examples

### Example 1: Metallica-Style Song

**User Input:**
```
song in style of metallica, you write the lyrics
```

**songwriter-DEV Output:**
````markdown
```
=== HIERARCHICAL STYLE BOX ===
foundation:
  bass: downtuned dist,palm-muted
  guitars: thrash riffing,harmonized leads
  synths: N/A
  drums: double bass,aggressive fills
  style: thrash metal,heavy,progressive
  processing: hi-gain,compressed,tape-sat
  contrast: melody/aggression
  tempo: 160-180
  meter: 4/4,complex

lead_vocals:
  register: baritone E2-G4
  character: raspy,powerful,gritty
  phrasing: rhythmic,shouted,precise
  emotion: anger,defiance,rebellion
  irony: N/A
  delivery: commanding,urgent
  effects: minimal,raw

atmosphere:
  mood: aggressive,intense,dark
  texture: raw,heavy,abrasive
  space: in-your-face,close
  dynamics: compressed,high-energy
```

```
=== LYRICS BOX ===
[Instruments: downtuned distorted bass; high-gain electric guitars with harmonized leads; double bass drum kit with aggressive fills; no synthesizers]
[Session Drummer: Full acoustic kit with 22" kick, 14" snare, 12/13/16" toms, 20" ride, 18" crash | Groove: Aggressive thrash, double bass patterns, complex fills, ghost notes on snare]

[Intro | Tech: Palm-muted power chords | Energy: Building]
E|-----------------|
B|-----------------|
G|--9--7--5--4----|

[Verse 1 | Vocal: Raspy shout | Mood: Defiant]
The hammer strikes at the break of dawn
Forge of justice burning bright
Chains will break and the walls come down
We stand and fight for what is right

[Pre-Chorus | Energy: High | Vocal: Gritty]
No more silence, no more lies
The fire burns in our eyes

[Chorus | Energy: Maximum | Vocal: Powerful]
SO THE BELL TOLLS FOR YOU!
AND THE ECHOES RING SO TRUE!
NO ONE CAN STOP THE STORM!
WE WILL WEATHER AND REFORM!

[Verse 2 | Vocal: Raspy | Tech: Harmonized guitar leads]
The law of the jungle, the rule of the gun
Innocent blood on their hands
But the tide will turn when the battle's begun
We'll take back our stolen lands

[Bridge | Tech: Drum fill cascade | Mood: Intense]
[Guitar Solo: Shredding, harmonized, with whammy bar]

[Final Chorus | Energy: Maximum | Vocal: Layered]
SO THE BELL TOLLS FOR YOU! (tolls for you!)
AND THE ECHOES RING SO TRUE! (ring so true!)
NO ONE CAN STOP THE STORM! (can stop the storm!)
WE WILL WEATHER AND REFORM! (and reform!)

[Outro | Tech: Fade out with feedback | Vocal: Fade]
The bell tolls...
```

```
=== NEGATIVE STYLES ===
Jazz, Country, Acoustic Folk, Smooth R&B, drum machine, electronic drums, synthetic percussion, plastic drums
```
````

---

### Example 2: Radiohead-Style Song

**User Input:**
```
Create a Radiohead-style song about urban alienation
```

**songwriter-DEV Output:**
````markdown
```
=== HIERARCHICAL STYLE BOX ===
foundation:
  bass: analog synth,octave-down
  guitars: clean/art rock,unusual tunings
  synths: atmospheric,modular
  drums: acoustic,complex polyrhythms
  style: alt rock,art rock,exp
  processing: tape sat,delay,verb
  contrast: organic/electronic
  tempo: 90-110
  meter: 4/4,5/4,7/8

lead_vocals:
  register: tenor C3-G4
  character: fragile,ethereal
  phrasing: sparse,breathy
  emotion: melancholic,anxious
  irony: warmth/cold
  delivery: intimate,detached
  effects: plate verb,delay

atmosphere:
  mood: introspective,alienated
  texture: layered,textural
  space: vast,echoing
  dynamics: wide,dynamic
```

```
=== LYRICS BOX ===
[Instruments: analog bass synth with octave down; clean electric guitar with unusual tunings; atmospheric modular synths; acoustic drum kit with complex polyrhythms; processed vocals with delay and reverb]
[Session Drummer: Full acoustic kit with 22" kick, 14" snare, 12/13/16" toms | Groove: Complex polyrhythms, odd time signatures (5/4, 7/8), ghost notes, brushed snare, electronic-acoustic hybrid]

[Intro | Tech: Atmospheric synth pads, reversed cymbals | Mood: Ethereal]
The city hums in 5/4 time
A rhythm I can't find

[Verse 1 | Vocal: Whispered | Mood: Melancholic]
The subway cars are empty
But full of ghosts
Each seat holds a memory
I try not to notice

[Chorus | Tech: Full kit with electronic processing | Energy: Building]
I walk these streets
But they don't know me
Urban alienation
In perfect time

[Verse 2 | Tech: Complex polyrhythms | Vocal: Fragile]
The WiFi signal fades at 3 AM
A digital ghost in the machine
My shadow has better reception
Than this heart you can't reach

[Bridge | Tech: Drum breakdown, time signature change | Mix: Break]
[No vocals - instrumental only]

[Final Chorus | Energy: Maximum | Vocal: Layered]
I walk these streets (walk these streets)
But they don't know me (don't know me)
Urban alienation (alienation)
In perfect time (perfect time)

[Outro | Tech: Synth pad sustain | Vocal: Fade]
The city hums...
```

```
=== NEGATIVE STYLES ===
Country, Trap, Reggaeton, drum machine, electronic drums, synthetic percussion, plastic drums
```
````

---

## Research File Integration

### When User References Artist Style
1. Check for `research/[artist].md` in suno-music-researcher skill directory
2. If exists, extract data and use it to inform both hierarchical box AND lyrics box
3. If doesn't exist, generate based on style description

### Data Extraction from Research Files

| **Research Section** | **Hierarchical Box** | **Lyrics Box** |
|----------------------|---------------------|----------------|
| Section 3: Instrumentation | `foundation.*` fields | `[Instruments: ...]` tag |
| Section 6: Vocal Style | `lead_vocals.*` fields | Vocal tags in sections |
| Section 2: Tempo/Rhythm | `foundation.tempo`, `foundation.meter` | Tech tags for rhythm |
| Section 5: Mood | `atmosphere.mood` | Mood tags in sections |
| Section 12: Suno Songwriter | N/A | Direct use of Session Drummer and Tech tags |

---

## Generation Workflow

### Step 1: Parse Input
- Identify if user provided lyrics, style, or both
- Check for artist references that might have research files
- Extract all style preferences and constraints

### Step 2: Generate Hierarchical Style Box
- Create foundation, lead_vocals, and atmosphere sections
- Apply condensation rules to stay under 1000 characters
- Count characters and verify limit

### Step 3: Generate Lyrics Box
- Create `[Instruments: ...]` tag from foundation fields
- Create `[Session Drummer: ...]` tag from foundation.drums and research data
- Structure lyrics into sections (Intro, Verse, Chorus, etc.)
- Add section-level meta tags (Vocal, Mood, Tech, Energy, etc.)
- Include user's lyrics if provided, or generate new ones
- Add ad-libs in parentheses where appropriate

### Step 4: Generate Negative Styles
- Identify conflicting genres based on style
- Add common exclusions (drum machine, etc.)
- Format as comma-separated list

### Step 5: Output All Three Code Blocks
- Each section in its own markdown code block
- Section header: `=== SECTION NAME ===`
- Verify hierarchical box is under 1000 characters

---

## Lyrics Generation Rules

### If User Provides Lyrics
- Preserve user's exact lyrics
- Add structure tags around them
- Add appropriate meta tags based on style
- Ensure proper section breaks (Intro, Verse, Chorus, etc.)

### If User Doesn't Provide Lyrics
- Generate lyrics that match:
  - The hierarchical style box mood and themes
  - The requested genre conventions
  - The vocal character and delivery style
- Use appropriate language and imagery
- Maintain proper syllable flow (6-12 syllables per line)

### Lyrics Quality Checks
- [ ] Preserves user's exact words if provided
- [ ] Matches the style and mood from hierarchical box
- [ ] Proper section structure (Intro, Verse, Chorus, Bridge, Outro)
- [ ] Appropriate meta tags for each section
- [ ] 6-12 syllables per line for singability
- [ ] No forced rhymes that sacrifice meaning
- [ ] Natural speech rhythm when read aloud

---

## Drum Tag Guidelines

### Kit Composition
Always specify:
- Kick drum size (e.g., 22", 24")
- Snare drum size (e.g., 14")
- Tom sizes if relevant (e.g., 12/13/16")
- Cymbals (ride, crash, hi-hats, etc.)

### Groove Characteristics
Specify:
- Time feel (swung, straight, shuffled)
- Dynamic range (soft, loud, dynamic)
- Techniques (ghost notes, flams, rim shots, brushes)
- Fill complexity (simple, complex, frequent)

### Examples by Genre
| **Genre** | **Session Drummer Tag** |
|-----------|------------------------|
| Rock | `[Session Drummer: Full kit with 22" kick, 14" snare, 12/13/16" toms | Groove: Natural swing, dynamic hits, ghost notes]` |
| Metal | `[Session Drummer: Full kit with 24" kick, 14" snare, 12/13/16" toms | Groove: Aggressive, double bass, complex fills, ghost notes]` |
| Jazz | `[Session Drummer: Jazz kit with brushed snare, ride cymbal focus | Groove: Soft brushes, swung, hi-hat with foot]` |
| Electronic | `[Session Drummer: Electronic kit with sampled acoustic hits | Groove: Quantized, punchy, consistent]` |

---

## Version System

**CURRENT VERSION:** 2.0

---

## Important Notes

1. **ALWAYS OUTPUT THREE MARKDOWN CODE BLOCKS** in order: Hierarchical Style Box, Lyrics Box, Negative Styles
2. **Each section in its own ``` block** for easy copy-paste
3. **Hierarchical box MUST be under 1000 characters**
4. **Lyrics Box MUST include** `[Instruments: ...]` and `[Session Drummer: ...]` tags
5. **DO NOT OUTPUT** traditional Style Block (Genre/Vocal/Tags)
6. **NO PROPER NOUNS** in generated content (except in research file references)
7. **Use research files** when available for accurate instrument/drum details
8. **Preserve user lyrics** exactly if provided
9. **Negative Styles** should be included for most requests

---

## Quality Checks Before Output

- [ ] Hierarchical style box is complete and under 1000 chars
- [ ] Lyrics box includes [Instruments: ...] tag
- [ ] Lyrics box includes [Session Drummer: ...] tag
- [ ] Lyrics have proper section structure
- [ ] Section tags include appropriate meta categories
- [ ] Negative styles are included when applicable
- [ ] No traditional Style Block output
- [ ] No proper nouns in generated content
- [ ] Character count verified for hierarchical box
- [ ] Each section is in its own markdown code block
