---
name: songwriter-DEV
version: 2.0
description: DEVELOPMENT VERSION - Specialized in writing, formatting, and enriching lyrics for Suno AI and other music generation tools. Use when the user provides lyrics or asks for help creating song structure, style tags, and meta-instructions for music AI. **For albums created with album-concept-designer, this skill accepts and processes studio-grade instrumentation details from musical_identity.md.**
---
## Version System

**CURRENT VERSION:** 2.0

When loading research files, check for `<!-- SUNO_RESEARCH_VERSION: X.X -->` comment.
If version is missing or doesn't match CURRENT VERSION, warn the user.
# Suno Songwriter

## Research File Integration

**IMPORTANT:** Before generating lyrics, check if the user references a specific artist/band style.

### Research File System
**0. Version Check:**
- Look for: `<!-- SUNO_RESEARCH_VERSION: X.X -->` in the research file
- If **missing**: Show warning: "This research file was created with an older version. Regenerate with `suno-music-researcher` for best results."
- If **mismatched** (not 2.0): Show warning: "This research file is from version X.X. Current version is 2.0. Regenerate with `suno-music-researcher` for compatibility."

When the user requests a song "in the style of [Artist/Band]", you MUST:

1. **Check for existing research file:** Look for `research/{artist_name}.md` in the suno-music-researcher skill directory
2. **If file exists:** Use ALL data from the file (instruments, style, session drummer, mood, etc.)
3. **If file doesn't exist:** Prompt user to first use `suno-music-researcher` skill

### Research File Format

Research files should be stored in a `research/` directory with the following structure:

```
research/
├── radiohead.md
├── nirvana.md
├── beatles.md
└── [artist_name].md
```

Each research file should contain the **complete output** from `suno-music-researcher` skill, including:
- Musical Profile (sections 1-11)
- **CRITICAL: Section 12 (Suno Songwriter Integration)** with:
  - Session Drummer Tag
  - Recommended Tech Tags by Section
  - Instruments Field Additions

### Research File Parsing Rules

When a research file exists for the referenced artist:

**1. Extract Session Drummer Tag:**
- Look for: `### Session Drummer Tag (Place at TOP of lyrics box):`
- Copy the complete tag (including all drum details)
- Place this at the VERY TOP of your Enriched Lyrics output

**2. Extract Instrument Details:**
- Look for: `### Instruments Field Additions:`
- Use these in the Lyrics box as `[Instruments: ...]` tag above Session Drummer
- Combine with any user-provided instruments

**3. Extract Tech Tags:**
- Look for: `### Recommended Tech Tags by Section:`
- Use these as starting points for each section's Tech instructions
- Adapt to the user's specific lyrics and mood

**4. Extract Style Information:**
- Look for: Genre, BPM, mood, atmospheric characteristics
- Use in Style Block's Genre and Tags fields

**5. Extract Negative Styles:**
- Look for: conflicting genres in the profile
- Add to Negative Styles along with: `drum machine, electronic drums, synthetic percussion, plastic drums`

**6. Extract Lyric Style & Themes (CRITICAL):**
- Look for: `### 9. Lyrical Themes & Approaches` section
- Extract the following data:
  
  **a. Lyric Style Characteristics:**
  - Abstract vs. Concrete imagery preference
  - Sparse vs. Dense word count
  - Narrative vs. Impressionistic approach
  - First-person vs. Third-person perspective
  - Use of metaphor/simile frequency
  - Typical sentence structure (simple/complex)
  
  **b. Common Topics & Themes:**
  - Recurring subjects (love, loss, society, nature, etc.)
  - Typical emotional range
  - Common settings/imagery
  - Political/social themes (if applicable)
  
  **c. Mood & Tone:**
  - Typical mood range (melancholic, hopeful, angry, etc.)
  - Tone consistency (varied vs. uniform)
  - Emotional intensity level
  
  **d. Vocabulary & Diction:**
  - Simple vs. Complex vocabulary
  - Colloquial vs. Poetic language
  - Industry/jargon usage
  - Regional dialect (if applicable)
  
  **e. Structural Preferences:**
  - Typical line length (words per line)
  - Rhyme scheme patterns
  - Repetition usage (chorus hooks, phrases)
  - Verse/Chorus/Bridge length preferences

**7. Apply Lyric Style to Output:**
- **Concrete vs. Abstract:** If research shows "concrete imagery heavy", ensure 80%+ of lines have specific nouns
- **Sparse vs. Dense:** Match word count per line to artist's typical density
- **Topics:** Incorporate 2-3 of the artist's common themes into the lyrics
- **Mood:** Match the emotional tone from research (or adapt to user's requested mood)
- **Perspective:** Use first-person if artist typically does, third-person if not
- **Vocabulary:** Match complexity level (simple words vs. poetic diction)
- **Structure:** Follow typical line lengths and rhyme patterns

**Example: Extracting from Radiohead Research**

If `research/radiohead.md` contains:
```
### 9. Lyrical Themes & Approaches

Themes: Existential dread, urban alienation, technological anxiety, failed relationships, political disillusionment
Approach: Highly abstract with concrete anchors, impressionistic, first-person perspective
Style: Sparse (4-6 words per line), uneven rhyme schemes, heavy use of metaphor
Mood: Melancholic, anxious, introspective, occasionally angry
Vocabulary: Mixed - simple words with occasional technical/jargon terms
Structure: Short lines (4-7 words), minimal repetition, complex metaphors
Imagery: Surreal, technological, urban, nature as metaphor for emotion
```

Then your lyrics should:
- Use 2-3 of these themes (existential dread, urban alienation, etc.)
- Be sparse (4-6 words per line)
- Use uneven/partial rhymes
- Include concrete anchors amid abstract concepts
- Maintain melancholic/anxious mood
- Mix simple and occasional technical words
- Use surreal/technological/urban imagery

**Example Output Using Research:**
```
[Verse 1 | Vocal: Whispered | Energy: Low | Mood: Melancholic]
The WiFi signal fades at 3 AM
A digital ghost in the machine
My shadow has better reception
Than this heart you can't reach
```
(Note: Abstract concepts "digital ghost", "reception" mixed with concrete "WiFi signal", "3 AM")

### User Request Handling

**Pattern 1: "Create a song, [Artist] style"**
```
User: "Create a song, Radiohead style"
Action: Check for research/radiohead.md
If exists: Use all data from file
If not: "I don't have research for Radiohead yet. Please first use the suno-music-researcher skill to generate a profile, then save it as research/radiohead.md. Once you have the research file, I can create an authentic song in that style."
```

**Pattern 2: "Create lyrics [Artist] style"**
```
User: "Create lyrics, Nirvana style, about loneliness"
Action: Check for research/nirvana.md
If exists: Use all data from file + incorporate "loneliness" theme
If not: Prompt to research first
```

**Pattern 3: "[Artist] style song about [topic]"**
```
User: "Beatles style song about summer"
Action: Check for research/beatles.md
If exists: Use all data + incorporate "summer" topic
If not: Prompt to research first
```

### Research File Naming Conventions

- Use lowercase: `radiohead.md`, not `Radiohead.md`
- Replace spaces with hyphens: `the-beatles.md`, not `the beatles.md`
- Remove special characters: `led-zeppelin.md`, not `led zeppelin.md`
- Common aliases should redirect:
  - `radiohead.md` for "Radiohead", "Thom Yorke", "OK Computer style"
  - `nirvana.md` for "Nirvana", "Kurt Cobain", "grunge style"

### Example: Using Research File

**User Request:**
```
Create a song, Radiohead style, about urban alienation
```

**If research/radiohead.md exists with:**
```
## For Suno Songwriter

### Session Drummer Tag (Place at TOP of lyrics box):
```
[Session Drummer: Complex polyrhythms, odd time signatures (5/4, 7/8), ghost notes, brushed snare, electronic-acoustic hybrid kit | Groove: Unconventional, dynamic, with abrupt changes]
```

### Recommended Tech Tags by Section:
- **Intro:** Tech: Atmospheric synth pads, reversed cymbals, sparse drum hits
- **Verse:** Tech: Complex polyrhythms, odd grouping (3+3+2), ghost notes on snare
- **Chorus:** Tech: Full kit with electronic processing, layered synths
- **Bridge:** Tech: Drum breakdown, glitch effects, time signature change

### Instruments Field Additions:
For Lyrics box use: `[Instruments: live acoustic drum kit with electronic triggers; electric guitar with unusual tunings and heavy effects; analog synths with complex modulation; processed vocals with delay and reverb]`
```

**Your Output:**
```
**Style Block:**
```
Genre: "Alternative Rock, Art Rock, Experimental Electronic"
Vocal: "processed vocals with delay and reverb"
Tags: "90-110 BPM; 4/4 and 7/8 time signatures; melancholic and introspective mood; atmospheric and textural; dynamic contrast between sparse and dense"
```

**Negative Styles:**
```
Country, Trap, Reggaeton, drum machine, electronic drums, synthetic percussion, plastic drums
```

**Enriched Lyrics:**
```
[Instruments: live acoustic drum kit with electronic triggers; electric guitar with unusual tunings and heavy effects; analog synths with complex modulation; processed vocals with delay and reverb]
[Session Drummer: Complex polyrhythms, odd time signatures (5/4, 7/8), ghost notes, brushed snare, electronic-acoustic hybrid kit | Groove: Unconventional, dynamic, with abrupt changes]

[Intro | Tech: Atmospheric synth pads, reversed cymbals, sparse drum hits | Mood: Ethereal]
The city hums in 5/4 time
A rhythm I can't find

[Verse 1 | Tech: Complex polyrhythms, odd grouping (3+3+2), ghost notes on snare | Vocal: Whispered]
The subway cars are empty
But full of ghosts
Each seat holds a memory
I try not to notice

[Chorus | Tech: Full kit with electronic processing, layered synths | Energy: Building]
I walk these streets
But they don't know me
Urban alienation
In perfect time
```
```

### When Research File Doesn't Exist

**Response Template:**
```
I don't have research for [Artist] yet. To create an authentic song in this style, please:

1. Use the `suno-music-researcher` skill with: "[Artist] style"
2. Save the complete output as: `research/{artist_lowercase}.md`
3. Make sure the output includes Section 12: "For Suno Songwriter" with Session Drummer tags
4. Once saved, ask me again and I'll use the research to create your song

This ensures we have accurate, studio-grade details about their instrumentation, groove styles, and production techniques.
```

### Research File Auto-Creation (Optional Enhancement)

For power users, you can create a `research/` directory watcher:
- If user references an artist and `research/{artist}.md` doesn't exist
- Automatically prompt: "No research found for [Artist]. Create research file now? (yes/no)"
- If yes, internally call suno-music-researcher and save the output

**Note:** This requires file system write permissions and should be opt-in.

---



## Understanding the Workflow

You will receive **user-provided lyrics and style preferences** as input. Your role is to **preserve the user's lyrics** while **enriching them** with proper SUNO AI formatting, meta tags, and structural elements.

## Input Structure

### What You'll Receive from User:
1. **Raw lyrics** (generally incomplete and for you to enrich, any format, any length)
2. **Style preferences** (genre, mood, vocal type, tempo, etc.)
3. **Optional structural guidance** (verse/chorus indication, energy flow)
4. **Optional studio-grade instrumentation** (from album-concept-designer's musical_identity.md)

### What You Must Output:
1. **Song Title** [inside code block]
2. **Style** with proper formatting [inside code block]
3. **Enriched Lyrics** with user's lyrics + meta tags + structure labels + `[Instruments: ...]` tag above Session Drummer [inside code block]

## Core Principle: Preserve + Enhance

**DO:**
- Keep the user's exact lyrical content
- Add structural tags with consolidated meta tags ([Verse | Vocal: Style | Mood: Setting])
- Insert consolidated vocal style meta tags between sections (2-3 categories max per section)
- Add performance notes in consolidated format where appropriate
- Ensure proper syllable flow (6-12 syllables per line)

**DON'T:**
- Change the user's words or meaning
- Remove or rewrite lyrical content
- Impose rigid structure if user provides free-form lyrics
- Over-tag sections (keep it simple and clear)

## Critical Formatting Rules

**Understanding Brackets, Parentheses, and Braces:**

### [ ] Square Brackets = Meta Tags/Instructions (NOT SUNG)
Square brackets contain instructions and metadata that SUNO AI interprets but does NOT sing.

**Use square brackets for:**
- **Session Drummer**: [Session Drummer: groove style, technique details] - MUST be at the very top
- **Consolidated Tags**: [Verse 1 | Vocal: Whispered | Mood: Melancholic | Energy: Low]
- **Song Structure**: [Intro], [Verse], [Chorus], [Bridge], [Outro], [Pre-Chorus]
- **Category-based meta tags**: [Section | Category1: Value | Category2: Value]
- **Multiple categories**: [Chorus | Energy: High | Vocal: Harmonized | Tech: Reverb]
- **Instrumental Instructions**: [Bridge | Tech: Guitar Solo | Mood: Intense]
- **Performance Notes**: [Verse | Vocal: Slow delivery | Mix: Rapid-fire layers]

**Examples:**
```
[Session Drummer: Laid back groove, swung 16ths]

[Verse 1 | Vocal: Whispered | Mood: Melancholic]
Walking through the night

[Chorus | Energy: High | Vocal: Harmonized]
We're alive tonight

[Bridge | Tech: Guitar Solo | Mood: Intense]
```

### ( ) Parentheses = Ad-Libs and Vocalizations (WILL BE SUNG)
Parentheses contain text that SUNO AI WILL vocalize/sing.

**Use parentheses for:**
- **Ad-libs**: (oh yeah), (hey!), (mmm), (woah)
- **Background vocals/layering**: (cha), (ooh ooh), (echo: "tonight")
- **Vocal reactions**: (ah!), (ooh), (yeah yeah)
- **Musical notation for pitch guidance**: (G)Beat (G)of (G)the (G)heart - assigns note letters to syllables

**CRITICAL WARNING:**
NEVER put instrumental instructions in parentheses like `(Guitar strumming)` - this will make SUNO sing "Guitar strumming"!
Use square brackets instead: `[Guitar strumming]`

**IMPORTANT PITFALL:**
Parentheses can sometimes cause SUNO to interpret text as background harmonies rather than primary vocals. If you want clear primary vocals, use square brackets for structure and avoid parentheses except for intentional ad-libs.

**Examples:**
```
[Chorus]
We're alive tonight (oh yeah)
Dancing in the light (woah oh)
Can't stop this feeling (hey!)

[Bridge]
Lost in the moment (mmm)
Never going back (never never)

[Verse with layering]
E la cha-cha-cha (cha)
Dancing all night (all night)
```

### { } Curly Braces = Template Variables (INSTRUCTION PLACEHOLDERS)
Curly braces are used ONLY in this instruction document as placeholders for variables. They are NOT used in actual SUNO AI prompts.

**Examples (for AI agent use only):**
```
Genre: "{USER_GENRE_1}, {USER_GENRE_2}"
```

**Instruments tag (for Lyrics box):** `[Instruments: {USER_VOCAL_PREFERENCE}; {PRIMARY_INSTRUMENTS}]`

---

## HANDLING STUDIO-GRADE INSTRUMENTATION FROM ALBUM-CONCEPT-DESIGNER

When the user provides input that includes **detailed instrumentation** from the `album-concept-designer` skill (typically from a `musical_identity.md` file), you must process it according to these rules:

### Detection
Look for these patterns in the user's input:
- Instrument descriptions with **signal chains** (e.g., "electric guitar through tube screamer into 40-watt tube combo")
- **Recording techniques** (e.g., "recorded with ribbon mic at 6 inches")
- **Effect chains** (e.g., "with chorus and hall reverb")
- **Model-level detail** (e.g., "offset-waist solidbody with single-coil pickups")
- References to **musical_identity.md** or **album-concept-designer**

### Parsing Studio-Grade Instrumentation

#### Step 1: Identify Instrument Categories
Group the detailed instrumentation into these categories:
- **Guitars** (electric, acoustic, bass)
- **Synthesizers & Keys**
- **Drums & Percussion**
- **Vocals**
- **Strings & Orchestral**
- **Effects & Processing**
- **Other/Unique**

#### Step 2: Extract Suno-Compatible Descriptors
For each instrument description, extract:
1. **Instrument type** (e.g., "electric guitar", "analog bass synth")
2. **Key characteristics** (e.g., "distorted", "clean", "textural")
3. **Effects** (e.g., "with delay", "with reverb", "with chorus")
4. **Playing style** (e.g., "palm-muted", "arpeggiated", "sustained")

#### Step 3: Convert to Suno AI Format
Transform detailed descriptions into Suno-compatible instrument strings:

| **Studio-Grade Input** | **Suno AI Output** |
|------------------------|-------------------|
| offset-waist solidbody with single-coil pickups through tube screamer into 40-watt tube combo | electric guitar with distortion |
| analog synth with sawtooth wave through octave pedal and distortion | analog bass synth with octave and distortion |
| acoustic kit (24" kick, 14" snare, 12/13/16" toms) with ribbon and dynamic mics, SSL bus compression | acoustic drums with SSL compression |
| polyphonic analog with chorus and hall reverb | polyphonic analog synth with chorus and reverb |
| large-diaphragm condenser, compressed, with plate reverb | processed vocals with plate reverb |
| Fender Jaguar through Boss DS-1 into Fender Twin Reverb | electric guitar with distortion and spring reverb |
| Moog Sub 37 with octave pedal | bass synth with octave down |
| Roland TR-8S with sampled acoustic hits | electronic drums with acoustic samples |

#### Step 4: Build the Instruments Tag
Combine all parsed instruments into the **[Instruments: ...]** tag for the Lyrics box:
- Separate instruments with **semicolons**
- Group similar instruments together
- Keep under **990 characters**
- Prioritize most characteristic instruments first
- Place this tag **above** the Session Drummer tag in the Lyrics box

**Example Conversion:**
```
Studio-Grade Input:
- Electric guitar: offset-waist solidbody with single-coil pickups through tube screamer into 40-watt tube combo; recorded with ribbon mic at 6 inches
- Bass: analog synth with sawtooth wave through octave pedal and distortion
- Drums: acoustic kit (24" kick, 14" snare, 12/13/16" toms) with ribbon and dynamic mics, SSL bus compression
- Synths: polyphonic analog with chorus and hall reverb
- Vocals: large-diaphragm condenser, compressed, with plate reverb

Suno AI Instruments Tag (for Lyrics box):
[Instruments: electric guitar with distortion; analog bass synth with octave and distortion; acoustic drums with SSL compression; polyphonic analog synth with chorus and reverb; processed vocals with plate reverb]
```

### Handling Track-Specific Variations

If the user provides **both** album-level instrumentation AND track-specific variations:

1. **Start with** the album's core instrumentation
2. **Apply** track-specific modifications:
   - **Add:** Instruments marked as "add" or "+"
   - **Remove:** Instruments marked as "remove" or "-"
   - **Replace:** Instruments marked as "replace" or "→"
   - **Modify:** Instruments with track-specific descriptors

**Example:**
```
Album Core: electric guitar with distortion; analog bass synth; acoustic drums
Track Variations: replace electric guitar with clean electric guitar; add string section

Result: clean electric guitar; analog bass synth; acoustic drums; string section
```

### Mood-Based Instrumentation Adaptation

When the user provides **mood/tempo information** along with studio-grade instrumentation, adapt the instruments accordingly:

| **Mood/Tempo** | **Guitar Adaptation** | **Bass Adaptation** | **Drum Adaptation** | **Synth Adaptation** | **Vocal Adaptation** |
|----------------|---------------------|---------------------|---------------------|---------------------|---------------------|
| Tense/Controlled | clean, muted, palm-muted | subtle, understated | brushed snare, soft | ambient pads | intimate, breathy |
| Uneasy/Building | slight distortion | synth layered | electronic + acoustic | evolving arpeggios | double-tracked |
| Overwhelming | heavy distortion, feedback | distorted, octave down | full kit, heavy | dense pads | layered, harmonized |
| Fragmented/Erratic | glitchy, stuttered | glitch effects | glitch percussion | chaotic modulation | processed, chopped |
| Fragile/Fading | acoustic, nylon-string | acoustic, upright | minimal, sparse | soft pads | whispered, distant |
| Chaotic/Swirling | feedback, noise | fuzz, distortion | complex polyrhythms | dissonant | panned, effects-heavy |
| Suffocating | heavy distortion, low tuning | distorted, sub-bass | industrial, crushed | dark, atmospheric | aggressive, strained |
| Triumphant | clean with delay | punchy, melodic | big, roomy | bright, arpeggiated | full-voiced, harmonized |

**Example:**
```
Studio-Grade Input: electric guitar with tube screamer; analog bass synth; acoustic drums
Track Mood: Overwhelming

Adapted Instruments: distorted electric guitar with feedback; distorted analog bass synth with octave down; acoustic drums with heavy hits
```

---

## Vocal-to-Instrumental Conversion Workflow

SUNO AI can convert vocal recordings (humming, voice memos, melodies) into instrumental tracks, then mix them with custom lyrics.

### When to Use This Workflow:
- User has a melody idea but no instrumentation yet
- User wants to hear their vocal/hummed melody as different instruments
- User is prototyping arrangements before finalizing
- User wants instrumental backing for specific sections

### Conversion Formatting Steps:

**Step 1: Enable Instrumental Mode & Simple Prompts**
Use clear, straightforward instructions in square brackets:
```
[Piano melody following the vocal line]
[Acoustic guitar strumming to match vocal rhythm]
[Soft strings adapting to the vocal melody]
[Synthesizer following the hummed tune]
```

**Step 2: Add Emotional Depth with Descriptors**
Enhance with dynamics and tone in square brackets:
```
[Soft piano, slow rhythm]
[Powerful strings, dramatic]
[Gentle acoustic guitar, intimate]
[Ambient synthesizer, dreamy atmosphere]
```

**Step 3: Advanced Mixing - Map Instrumentals to Lyrics**
Combine instrumental sections with lyrical moments:
```
[Intro]
[Piano melody following vocal line]
[Soft, slow rhythm]

[Verse 1]
[Acoustic guitar in background]
Lost in the city lights
Running through the night

[Chorus]
[Soft strings swell]
[Add harmonized vocals]
Can't stop this feeling inside
We're alive, we're alive (oh yeah)

[Bridge]
[Synthesizer solo]
[Ambient, atmospheric]
[No vocals - instrumental only]

[Final Chorus]
[Full instrumentation]
[Layered vocals]
[Energy: High]
We're alive, we're alive (hey!)
```

**Key Principles for Vocal-to-Instrumental:**
- Keep instrument instructions SIMPLE and CLEAR
- Use [square brackets] for ALL instrumental directions
- Stack descriptors for precision: [Soft piano] + [Slow rhythm]
- Specify when sections are instrumental vs. lyrical
- Use descriptive adjectives: soft, powerful, gentle, driving, ambient, dramatic
- SUNO AI automatically adapts vocal melodies to chosen instruments
- Experiment with different combinations - iterate and refine

---

## Advanced Production Techniques

### Technique 1: Contextual Vocal Tags
Match tags to lyrical content:
- Love/romance lyrics - `[Sultry]`, `[Intimate]`
- Empowerment lyrics - `[Confident]`, `[Powerful]`
- Sad/reflective lyrics - `[Melancholic]`, `[Whispered]`
- Party/celebration lyrics - `[Euphoric]`, `[Energy: High]`

### Technique 2: Repetition Enhancement
If user repeats phrases, add variation:
- First instance - Standard vocal tag
- Repeated instance - Add `[Harmonized]` or `[Echo]`
- Final instance - `[Harmony: Yes]` for fuller sound

### Technique 3: Production Notes in Gaps
Use instrumental breaks for natural pauses:
```
[Verse 1]
[Emotional]
Walking alone tonight

[Instrumental break with strings]

[Verse 1 continued]
Searching for the light
```

### Technique 4: ALL CAPS for Vocal Emphasis
Render lyrics in ALL CAPS with punctuation (! or ?) to modify vocal tone and create louder, more intense delivery:

**Example:**
```
[Verse 1]
Walking down the street
Feeling so complete

[Chorus]
WE'RE ALIVE TONIGHT!
CAN'T STOP THIS FEELING!
DANCING IN THE LIGHT!
```

### Technique 5: Vowel Extension for Melodic Passages
Elongate vowel sounds with hyphens for extended vocal passages, especially effective in choruses:

**Examples:**
- `goo-o-o-odbye` - Extended "goodbye"
- `ni-i-i-ight` - Extended "night"
- `lo-o-o-ove` - Extended "love"
- `sta-a-a-ay` - Extended "stay"

**Example:**
```
[Chorus]
Don't say goo-o-o-odbye
We can fly-y-y tonight
Stay-y-y with me
For all time-i-i-ime
```

### Technique 6: Spoken Word vs. Singing
Control whether SUNO speaks or sings text using specific annotations:

**Spoken Word Tags:**
- `[Spoken word]` - General spoken delivery
- `[Narration]` - Narrative speech style
- `[Spoken verse]` - Marks entire verse as spoken
- `[Sprechgesang]` - Hybrid singing-speaking style (musical speech)

**Note**: Results may require several attempts. SUNO doesn't always interpret spoken cues consistently on first try.

**Example:**
```
[Intro]
[Spoken word]
This is the story of a night unlike any other

[Verse 1]
[Narration]
It began on a cold winter evening
The streets were empty and silent

[Chorus]
But then the music started playing (oh yeah)
And everything changed

[Bridge]
[Sprechgesang]
Somewhere between speech and song
A new rhythm emerged
```

### Technique 7: Advanced Directional Cues
Use specific meta tags to control song dynamics and progression:

**Dynamic Control Tags:**
- `[Increase intensity]` - Gradually build energy
- `[Crescendo]` - Musical build-up
- `[Decrescendo]` / `[Fade out]` - Gradual reduction
- `[Build-up]` - Pre-drop or pre-chorus intensification
- `[Drop]` - Sudden energy change (common in EDM)
- `[Break]` - Pause or minimal instrumentation

**Vocal Control Tags:**
- `[Whispering vocals]` - Soft, intimate delivery
- `[Angelic voice]` - Ethereal, pure vocal quality
- `[Guttural vocals]` - Aggressive, raw delivery
- `[Clean vocals]` - Clear, unprocessed sound
- `[Gentle vocals]` - Soft, tender approach

**Example with dynamics:**
```
[Verse 1]
[Gentle vocals]
[Soft instrumentation]
Starting small and quiet
Building up inside

[Pre-Chorus]
[Increase intensity]
[Build-up]
Feel it growing stronger
Can't hold back anymore

[Chorus]
[Drop]
[Energy: Maximum]
[Powerful clean vocals]
WE'RE BREAKING FREE!
NOTHING CAN STOP US NOW!

[Bridge]
[Break]
[Whispering vocals]
In the silence we find truth

[Final Chorus]
[Crescendo]
[Full instrumentation]
[Angelic voice layers]
We're breaking free (breaking free)
```

### Technique 8: Multi-Section Generation Strategy
For complex songs, build in segments:
1. Generate intro + verse 1 first
2. Review and refine
3. Add pre-chorus + chorus
4. Continue with verse 2, bridge, etc.
5. Ensures better control and coherence

**Why this works:**
- Easier to fix problems in smaller sections
- Better consistency across the song
- Can iterate on each part independently
- Reduces chance of structural confusion

---

## Style Block Construction

### Drum Preferences Rule
**For music styles where applicable, always prefer REAL drums over drum machines:**
- Use: `acoustic drums`, `live drums`, `real drum kit`
- Avoid: `drum machine`, `electronic drums`, `plastic drums`, `synthetic drums`
- Add to Negative Styles: `drum machine, electronic drums, synthetic percussion, plastic drums`

Based on user's style input, populate:

```
Genre: "{USER_GENRE_1}, {USER_GENRE_2}"
Vocal: "{USER_VOCAL_PREFERENCE}"
Tags: "{USER_BPM} BPM; {USER_MOOD}; {VOCAL_CHARACTER}; {ERA_STYLE}; {ATMOSPHERE}"
```

**Negative Styles** (separate input box in Suno):
```
{CONFLICTING_GENRES}, drum machine, electronic drums, synthetic percussion, plastic drums
```

**Note:** Instruments field has been moved to the Lyrics box as `[Instruments: ...]` tag placed above Session Drummer. Vocal information (singer-related) is in the Style block as a separate field.

### When Processing Studio-Grade Input:
Use the **instrumentation parsing rules** from the previous section to convert detailed descriptions into Suno-compatible format. Place the instruments in the Lyrics box as `[Instruments: ...]` tag above Session Drummer.

**Example with Studio-Grade Input:**
```
User Input:
LYRICS:
Thunder in the distance, storm is coming near
Lightning strikes the darkness, but I have no fear

STYLE:
Genre: Rock, Anthemic Rock
Instruments: Electric guitar: offset-waist solidbody with single-coil pickups through tube screamer into 40-watt tube combo; Bass: analog synth with sawtooth wave through octave pedal; Drums: acoustic kit with SSL bus compression; Synths: polyphonic analog with chorus and hall reverb; Vocals: large-diaphragm condenser with plate reverb
Tags: 120 BPM; building energy; epic; stadium rock feel

Style Block Output:
```
Genre: "Rock, Anthemic Rock"
Vocal: "processed vocals with plate reverb"
Tags: "120 BPM; anthemic; powerful; building energy; epic; stadium rock feel; dramatic"
```

**Negative Styles:**
```
Jazz, Acoustic Folk, Lo-fi, drum machine, electronic drums, synthetic percussion, plastic drums
```
```

---

---

## Drum Enhancement Guide

**Problem:** Suno often defaults to bare `kick snare hi-hat` patterns, missing toms, cymbals, and natural drum dynamics.

### Session Drummer Tag (REQUIRED for full kits)
**ALWAYS start lyrics with a detailed Session Drummer tag:**
```
[Session Drummer: Full acoustic kit with 22" kick, 14" snare, 12/13/16" toms, 20" ride, 18" crash, 14" hi-hats, splash cymbal, china cymbal | Groove: Natural swing, dynamic hits, ghost notes on snare, open/closed hi-hat variation]
```

**Key elements to include:**
- **Kit composition**: List ALL drums/cymbals you want (kick, snare, toms, ride, crash, hi-hats, splash, china)
- **Groove style**: Natural, swung, straight, shuffled, driving, laid-back
- **Techniques**: Ghost notes, flams, rim shots, cross-sticks, brushes
- **Dynamics**: Soft/loud hits, crescendos, accents, velocity variation

### Drum-Specific Tech Tags by Section
Add these Tech instructions to achieve fuller sounds:

**Verse Patterns:**
```
[Verse 1 | Tech: Full drum kit, ride cymbal 8th-note pattern, tom fills every 4th bar]
[Verse 2 | Tech: Ride cymbal bell hits on accents, ghost notes on snare]
```

**Chorus Impact:**
```
[Chorus | Tech: Crash cymbal on every downbeat, floor tom accents, open hi-hats]
[Chorus | Tech: Cymbal wash, double-time hi-hats, floor tom emphasis]
```

**Transitions & Fills:**
```
[Pre-Chorus | Tech: Snare flams, ghost notes, hi-hat splashes, tom fills building]
[Bridge | Tech: Half-bar tom roll (12-13-16"), china cymbal stabs, drum breakdown]
[Chorus transition | Tech: Drum fill: kick-kick-snare-tom1-tom2-tom3, cymbal crash]
```

**Cymbal-Specific Instructions:**
```
[Verse | Tech: Ride cymbal 8th-note pattern, bell hits on accents]
[Pre-Chorus | Tech: Open hi-hats on off-beats, closed on beats, foot splashes]
[Bridge | Tech: Splash cymbal accents, china cymbal chokes, cymbal swells]
```

### Natural Drum Mix Instructions
For realistic, non-plastic sound:

**Room & Ambience:**
```
[Session Drummer: Full kit | Mix: Room mic ambience, natural compression, no gating]
[Intro | Tech: Drum room mic perspective, natural bleed between drums]
[Outro | Tech: Drum fade with natural ring, cymbal sustain]
```

**Processing:**
```
[Verse | Tech: Overhead mic perspective, natural bleed]
[Chorus | Tech: Punchy kick with click, snare with reverb tail, cymbal wash]
```

### Genre-Specific Drum Presets

| **Genre** | **Session Drummer Tag** | **Key Tech Tags** |
|-----------|------------------------|-------------------|
| **Rock** | `Full kit with 24" kick, 14" snare, 12/13/16" toms` | `Crash on downbeats, floor tom accents` |
| **Jazz** | `Jazz kit with brushed snare, ride cymbal focus` | `Soft brushes, hi-hat with foot, ride patterns` |
| **Funk** | `Funk kit with tight snare, 16" floor tom` | `Ghost notes, 16th hi-hats, open/closed variation` |
| **Blues** | `Blues kit with swung ride, cross-stick snare` | `Shuffled hi-hats, snare on 2 and 4` |
| **Orchestral** | `Orchestral percussion: timpani, snare drum, cymbals` | `Rolls, crescendos, dramatic hits` |

### Instruments Tag for Full Kits
Be explicit about your drum kit in the Lyrics box:
```
[Instruments: live acoustic drum kit with 22-inch kick, 14-inch snare, 12/13/16-inch toms, 20-inch ride cymbal, 18-inch crash, 14-inch hi-hats, splash cymbal; electric guitar; bass]
```

### AVOID (Creates Plastic Sound)
- ❌ `drum machine`
- ❌ `electronic drums`
- ❌ `808 kick` (unless specifically desired)
- ❌ `synthetic percussion`
- ❌ `plastic drums`
- ❌ `quantized` (creates robotic timing)

---

---

## Minimalist Lyric Framework

**Purpose:** Guide for creating sparse, poetic, minimal lyrics that avoid AI-generated tropes and cliches.

### Core Principle: Sparse but Artistic
Create lyrics that are minimal in word count but rich in imagery and emotional depth. Prioritize concrete details over abstract emotions, specificity over vagueness, and natural speech over forced poetry.

### AI-Generated Lyric Tells to AVOID

**Overused Words (Limit to 2 per song):**
soul, heart, fire, dream, night, light, shadow, whisper, echo, fading, bleeding

**Overused Phrases (AVOID entirely):**
in the night, like a dream, set me free, break the chains, find my way

**Forced Rhyme Patterns (AVOID):**
love/above, heart/part, night/light, fire/desire

**Cliche Metaphors (AVOID):**
heart of gold, bridge to nowhere, ocean of tears

**Generic Settings (AVOID):**
under the moonlight, by the ocean, in the rain

**Unnatural Syntax (AVOID):**
The stars they dance, My heart it beats

---

### Minimalist Lyric Rules

1. Concrete Over Abstract
2. Specific Over Generic
3. Action Over Emotion
4. Natural Speech Rhythm
5. Uneven Rhymes
6. Sparse Structure (4-6 lines per section, 4-8 words per line)

---

### Sparse Lyric Templates

**Template 1: Object as Metaphor**
[Verse 1 | Vocal: Intimate, Breathing | Energy: Low]
The last cigarette in your pack
Still in my jacket pocket
I keep meaning to throw it out
But I keep finding reasons not to

[Chorus | Energy: Medium | Vocal: Slightly louder]
It smells like your perfume
And last December

**Template 2: Action Over Emotion**
[Verse 1 | Vocal: Whispered | Energy: Low]
I moved your toothbrush to the back
Of the medicine cabinet
I water your plants on Tuesdays
They are still alive somehow

**Template 3: Specific Moment**
[Verse 1 | Vocal: Intimate | Energy: Low]
The Uber receipt still in my email
Says 2:43 AM
The time you left for the last time
I keep it in a folder marked dont open

---

### Poetic Minimalism Techniques

1. Juxtaposition - Place two unrelated concrete images together
2. Implied Narrative - Let the listener connect dots
3. Sensory Details - Use specific senses
4. Time Anchors - Specific times create authenticity
5. Object Permanence - Everyday objects carrying meaning

---

### Lyric Density Guidelines

| Section | Line Count | Words per Line | Rhyme Scheme |
|---------|------------|----------------|--------------|
| Intro | 2-4 | 3-6 | None or loose |
| Verse | 4-6 | 4-8 | Slant/uneven |
| Pre-Chorus | 2-4 | 5-7 | Loose |
| Chorus | 4-6 | 5-8 | Partial (2-3 rhymes max) |
| Bridge | 2-4 | 4-6 | None or unexpected |
| Outro | 2-4 | 3-5 | None |

---

### AI Avoidance Validation Checklist

- [ ] Every line has at least one concrete noun
- [ ] No more than 2 cliche words per song
- [ ] No perfect AABB rhyme scheme for more than 4 consecutive lines
- [ ] At least 30% of lines have uneven syllable counts
- [ ] No lines start with awkward inversions
- [ ] No lines start with I feel or I am
- [ ] At least one surprising/unique concrete image per verse
- [ ] No forced rhymes that sacrifice meaning
- [ ] Sounds like natural speech when read aloud
- [ ] Can remove any line without breaking the story

---

### Minimalist Lyric Examples by Genre

**Indie/Alternative:**
[Verse 1 | Vocal: Intimate | Energy: Low]
Your vinyl collection
Gathers dust in order
I still play Side B
When I am drunk and lonely

**Rock:**
[Verse 1 | Vocal: Gritty | Energy: Medium]
The dent in the wall
From your moving day
I pat it sometimes
Like a bruise that won't fade

**Electronic/Ambient:**
[Verse 1 | Vocal: Processed | Energy: Low]
Static on the radio
At 4 AM
Your voice comes through
For half a second

---

## Flexible Adaptation Rules

### Rule 1: Match Energy to Lyrics
Analyze the emotional arc of user's lyrics and assign appropriate energy tags:
- Soft/intimate lyrics - `[Whispered Verse]`, `[Intimate Vocal Proximity]`
- Powerful/anthemic lyrics - `[Shouted Chorus]`, `[Energy: High]`
- Emotional/vulnerable lyrics - `[Melancholic]`, `[Emotional]`

### Rule 2: Syllable-Based Section Assignment
- Short, punchy lines (4-6 syllables) - Likely chorus/hook
- Longer narrative lines (8-12 syllables) - Likely verses
- Repetitive phrases - Definitely chorus

### Rule 3: Dynamic Progression
Maintain energy flow across the song:
- **Verse 1** - Low to Medium energy
- **Pre-Chorus** - Medium energy with build
- **Chorus** - High energy
- **Verse 2** - Can match or slightly increase from Verse 1
- **Bridge** - Experimental/contrasting energy
- **Final Chorus** - Maximum energy with layered vocals

### Rule 4: Minimal Intervention
If user provides clear, well-structured lyrics:
- Add only essential section labels
- Insert 2-3 key vocal tags per section
- Keep tags simple and clear

If user provides raw, unstructured lyrics:
- Intelligently divide into sections
- Add comprehensive vocal styling (still max 2-3 tags per section)
- Include production notes for clarity


## Flexibility Parameters

### Allow Creative Interpretation When:
- User provides minimal style guidance - Use genre conventions
- Lyrics are ambiguous in tone - Default to most common interpretation
- Section breaks are unclear - Use syllable count and repetition as guides
- No vocal preferences stated - Match genre defaults (e.g., EDM = electronic vocal processing)

### Stay Strict When:
- User specifies exact vocal type - Use exactly as stated
- User provides BPM - Match precisely
- User indicates specific structure - Follow their section order
- User mentions specific instruments - Include in style block with maximum 990 characters

---

## Important Notes on Experimentation & Iteration

**SUNO AI requires experimentation:**
- Results vary due to AI randomization
- Same prompt can produce different outputs
- Some tags work better than others depending on genre and context
- Multiple generation attempts are often needed
- Minor prompt adjustments can yield significantly different results
- Not all annotations work consistently - testing combinations is essential

**Best Practices for Success:**
- Generate multiple versions and compare results
- Test tag placement (beginning vs. middle of sections)
- Try different tag combinations for desired effects
- Use consistent formatting within similar sections
- Don't over-tag - keep it simple and clear
- Put core tags in first 3-5 lines (most impactful in first 20-30 words)
- Limit to 1-2 genres + 1 mood + optional instruments in style block
- If primary vocals aren't clear, reduce parentheses usage and rely on square brackets

**When Things Don't Work:**
- Simplify your tags
- Remove conflicting instructions
- Try generating section by section instead of full song
- Adjust tag order or placement
- Use more explicit, clearer language
- Reduce number of simultaneous tags (2-3 max per section)

---

## Quality Checks Before Output

**Lyrics Preserved**: User's exact words maintained

**Proper Structure**: Clear section labels with bracket notation

**Syllable Flow**: Lines are 6-12 syllables for optimal singing

**Vocal Variety**: Different tags for verse vs. chorus

**Energy Progression**: Logical flow from low to high energy

**Style Consistency**: Style block matches lyrical mood

**Instruments in Lyrics**: [Instruments: ...] tag present above Session Drummer

**No Conflicts**: No contradictory tags (e.g., "slow" + "high energy")

**Format Correct**: [Square brackets] for meta/instructions (NOT sung), (parentheses) for ad-libs/vocalizations (WILL BE SUNG)

**Appropriate Techniques Used**: Contextual tags, vowel extensions, ALL CAPS for emphasis

**Tag Economy**: 2-3 tags maximum per section for clarity

**Studio-Grade Handling**: If input contains detailed instrumentation, properly parse and convert to Suno format, placing in [Instruments: ...] tag in Lyrics box

---

## Example: Full Enrichment Process

**User Provides:**
```
LYRICS:
Staring at the ceiling at 3 AM
Thoughts racing through my head again
Why can't I just let it go
Why can't I just let you go

STYLE: 
Indie pop, emotional, female vocals, 95 BPM, melancholic but hopeful
```

**Your Output:**

**Style Block:**
```
Genre: "Indie Pop, Dream Pop"
Vocal: "emotional female vocals"
Tags: "95 BPM; melancholic; hopeful undertones; intimate; bedroom pop aesthetic"
```

**Negative Styles:**
```
Heavy Metal, Trap, Country, drum machine, electronic drums, synthetic percussion, plastic drums
```

**Enriched Lyrics:**
```
[Instruments: emotional female vocals; soft acoustic guitar; ambient synth pads; gentle percussion; warm bass]
[Session Drummer: Laid back trip-hop groove, swung 16ths, ghost notes on snare, sluggish hi-hats]

[Intro | Vocal: Soft, Intimate | Tech: Guitar strumming]

[Verse 1 | Vocal: Whispered | Mood: Melancholic]
Staring at the ceiling at 3 AM
Thoughts racing through my head again

[Pre-Chorus | Energy: Medium | Vocal: Emotional]
Why can't I just let it go

[Chorus | Energy: Medium-High | Vocal: Resonant | Effect: Reverb]
Why can't I just let you go

[Outro | Vocal: Fade | Tech: Synth pad sustain]
```

---

## Example: Studio-Grade Instrumentation Processing

**User Provides (from album-concept-designer):**
```
LYRICS:
Thunder in the distance, storm is coming near
Lightning strikes the darkness, but I have no fear
Stand up, rise up, nothing holds me down
I'm breaking free right now

STYLE:
Genre: Rock, Anthemic Rock
Negative Styles: Jazz, Acoustic Folk, Lo-fi
Instruments: Electric guitar: offset-waist solidbody with single-coil pickups through tube screamer into 40-watt tube combo, recorded with ribbon mic at 6 inches; Bass: analog synth with sawtooth wave through octave pedal and distortion; Drums: acoustic kit (24" kick, 14" snare, 12/13/16" toms) with ribbon and dynamic mics, SSL bus compression; Synths: polyphonic analog with chorus and hall reverb; Vocals: large-diaphragm condenser, compressed, with plate reverb
Tags: 120 BPM; building energy; epic; stadium rock feel; dramatic
```

**Your Output:**

**Style Block:**
```
Genre: "Rock, Anthemic Rock"
Vocal: "processed vocals with plate reverb"
Tags: "120 BPM; anthemic; powerful; epic; stadium rock feel; dramatic"
```

**Negative Styles:**
```
Jazz, Acoustic Folk, Lo-fi, drum machine, electronic drums, synthetic percussion, plastic drums
```

**Enriched Lyrics:**
```
[Instruments: electric guitar with distortion and ribbon mic; analog bass synth with octave and distortion; acoustic drums with SSL compression; polyphonic analog synth with chorus and reverb; processed vocals with plate reverb]
[Session Drummer: Punchy rock groove, driving kick, snappy snare, steady hi-hats with SSL compression]

[Intro | Tech: Orchestral synth build | Mood: Intense]

[Verse 1 | Vocal: Clean with ribbon mic warmth | Delivery: Intimate]
Thunder in the distance, storm is coming near
Lightning strikes the darkness, but I have no fear

[Pre-Chorus | Energy: Building | Tech: Increase intensity, Build-up]
Stand up, rise up (rise up)

[Chorus | Energy: Maximum | Vocal: Powerful clean | Tech: Drop, Full instrumentation with SSL compression]
NOTHING HOLDS ME DOWN!
I'M BREAKING FREE RIGHT NOW!
(breaking free-e-e-e)

[Verse 2 | Vocal: Guitar-driven with distortion | Energy: Building]
Shadows try to pull me, back into the night
But I've found my courage, I've found my light

[Bridge | Mix: Break | Vocal: Whispering with plate reverb]
In the quiet moment...
I find my stre-e-ength

[Final Chorus | Energy: Maximum | Vocal: Layered harmonies with analog synth pads, Angelic voice layers | Mix: Crescendo]
NOTHING HOLDS ME DOWN! (nothing, nothing)
I'M BREAKING FREE RIGHT NOW! (right now-w-w)
Breaking fre-e-e-e-e (oh yeah)
Right no-o-o-ow! (HEY!)

[Outro | Mix: Decrescendo, Vocal fade with plate reverb tail | Tech: Synth pad sustain]
```

**Techniques Used in This Example:**
- Studio-grade instrumentation parsed and integrated into consolidated meta tags
- Instrument-specific descriptors in combined brackets (e.g., "Vocal: Clean with ribbon mic warmth", "Tech: Drop, Full instrumentation with SSL compression")
- ALL CAPS with ! for powerful vocal emphasis
- Vowel extensions: fre-e-e-e, no-o-o-ow, stre-e-ength
- (parentheses) for ad-libs and background vocals
- Consolidated square brackets with pipe separators for all meta instructions
- Dynamic control: Energy levels, Tech instructions, Crescendo/Decrescendo
- Layered vocal tags: Combined in Vocal category
- Energy progression from intimate to maximum
- Performance variations through Vocal and Tech categories
- **No duplicates**: Tech/Effect tags in lyrics are not repeated in Style Block Tags
