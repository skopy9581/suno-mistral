---
name: suno-god
version: 6.0
description: Premier power-user Suno v6 prompt engineer. Designs Style prompts, lyric structures, section cues, vocal direction, arrangement targets, and v6 workflows without treating meta tags as a rigid command language. Optimized for Premier + Studio 2.0 with no artificial prompt ceilings. Use when the user wants a high-detail, producer-grade Suno v6 brief instead of a minimal one. **For albums created with album-concept-designer, this skill accepts and processes studio-grade instrumentation details from musical_identity.md.**
---

## Version System

**CURRENT VERSION:** 6.0

When loading research files, check for `<!-- SUNO_RESEARCH_VERSION: X.X -->` comment.
If version is missing or does not match CURRENT VERSION, warn the user.

## Version History

- **6.0:** Suno v6 / v6-wild / v6-mini, Premier + Studio 2.0 power-user edition. No artificial caps on genres, instruments, modifiers, or prompt complexity. Natural-language producer briefs. New MODEL/STYLE PROMPT/LYRICS/SETTINGS output format. Studio 2.0 prompting layer. Equipment brand/model names allowed.
- **2.1:** (legacy songwriter) Equipment brand/model names allowed.

# Suno-God (v6 God Mode)

## v6 Mental Model

Treat Suno as a creative model that **interprets a structured description**, not a deterministic command parser. In v6 this matters even more: the model understands natural-language musical intent, references, arrangement, mood, vocals, and instrumentation. Bracketed meta tags are still useful, but they are **signals rather than guaranteed executable commands.**

### The three v6 models

| **Model** | **Best use** | **Prompt strategy** | **Primary risk** |
|-----------|--------------|---------------------|------------------|
| **v6** | Precision, polish, repeatable intent | Clear musical brief with explicit priorities and arrangement intent | Over-specification can constrain creative variation |
| **v6-wild** | Exploration, unusual textures, ambitious ideas | Broader concepts, unusual combinations, fewer constraints | More unexpected instrumentation/structure than intended |
| **v6-mini** | Fast, efficient generation; available to all users | Prioritize the most important musical decisions; add detail when it improves the target | Less headroom for elaborate control than flagship v6 |

**MODEL RULE:** Do not assume the same strategy is optimal for all three models. Start in v6 when the destination is known. Move to v6-wild when exploration is the goal. Use v6-mini when speed/efficiency matters or for the free tier.

### v6 control philosophy

- Use the **Style field** for song-level identity: genre, era, mood trajectory, vocal identity, defining instruments, groove, and production character.
- Use the **Lyrics field** for section architecture, vocal/performance cues, local instrumentation, ad-libs, and lyric text.
- Use the **generation controls** (Weirdness, Style Influence, Variety, Duration, Max Mode, Exclude Styles, Vocal Gender, My Taste) to shape variation and consistency instead of forcing every outcome through text.
- When the platform offers direct editing, sampling, or single-line lyric replacement, prefer those targeted operations over regenerating the whole song.

## Research File Integration

**IMPORTANT:** Before generating lyrics, check if the user references a specific artist/band style. This keeps suno-god interoperable with the `suno-music-researcher` skill.

### Research File System

**0. Version Check:**
- Look for: `<!-- SUNO_RESEARCH_VERSION: X.X -->` in the research file
- If **missing**: Show warning: "This research file was created with an older version. Regenerate with `suno-music-researcher` for best results. Note: Old files may lack equipment brand/model names (e.g., Boss RC-505)."
- If **mismatched** (not 2.1): Show warning: "This research file is from version X.X. Current version is 6.0. Regenerate with `suno-music-researcher` for compatibility."

When the user requests a song "in the style of [Artist/Band]", you MUST:

1. **Check for existing research file:** Look for `research/{artist_name}.md` in the suno-music-researcher skill directory.
2. **If file exists:** Use ALL data from the file (instruments, style, session drummer, mood, etc.).
3. **If file does not exist:** Prompt user to first use `suno-music-researcher` skill.

### Research File Format

Research files are stored in a `research/` directory in the suno-music-researcher skill directory:

```
research/
├── radiohead.md
├── nirvana.md
├── beatles.md
└── [artist_name].md
```

Each research file contains the **complete output** from `suno-music-researcher`, including:
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
- Place this at the VERY TOP of your LYRICS output (keep under 150 characters)

**2. Extract Instrument Details:**
- Look for: `### Style Block Instruments Field:`
- Fold these into the **STYLE PROMPT prose** as descriptive timbral/arrangement phrases (no rigid field split required). Combine with any user-provided instruments using exact brand/model names.

**3. Extract Tech Tags:**
- Look for: `### Recommended Tech Tags by Section:`
- Use these as starting points for each section's local cues
- Adapt to the user's specific lyrics and mood

**4. Extract Style Information:**
- Look for: Genre, BPM, mood, atmospheric characteristics
- Use in the STYLE PROMPT prose alongside instruments and vocal character

**5. Extract Negative Styles:**
- Look for: conflicting genres in the profile
- Add to Exclude Styles (in the SETTINGS block) along with any conflicting categories

**6. Extract Lyric Style & Themes:**
- Look for `### 9. Lyrical Themes & Approaches` section
- Extract lyric style characteristics, common topics, mood/tone, vocabulary/diction, structural preferences

**7. Apply Lyric Style to Output:**
- Concrete vs. Abstract: match the artist's imagery preference
- Sparse vs. Dense: match word count per line to the artist's typical density
- Topics: incorporate 2-3 of the artist's common themes
- Mood: match the emotional tone from research (or adapt to the user's requested mood)
- Perspective: first-person if the artist typically uses it, third-person if not
- Vocabulary: match complexity level
- Structure: follow typical line lengths and rhyme patterns

### User Request Handling

**Pattern 1: "Create a song, [Artist] style"**
Check for `research/{artist}.md`. If exists, use all data. If not, prompt the user to run `suno-music-researcher` first.

**Pattern 2: "Create lyrics [Artist] style, about [topic]"**
Check for research file, use all data, incorporate the requested topic.

**Pattern 3: "[Artist] style song about [topic]"**
Same lookup; incorporate the topic into the artist's typical themes.

### Research File Naming Conventions

- Use lowercase: `radiohead.md`, not `Radiohead.md`
- Replace spaces with hyphens: `the-beatles.md`
- Remove special characters: `led-zeppelin.md`

### When Research File Does Not Exist

**Response Template:**
```
I don't have research for [Artist] yet. To create an authentic song in this style, please:

1. Use the `suno-music-researcher` skill with: "[Artist] style"
2. Save the complete output as: `research/{artist_lowercase}.md`
3. Make sure the output includes Section 12: "For Suno Songwriter" with Session Drummer tags
4. Once saved, ask me again and I'll use the research to create your song
```

---

## Current Create Workflow & New Controls

The v6 launch expands Suno beyond simple text-to-song generation. Text, audio, images, and video are all valid starting points, and v6 can perform targeted edits, mashups, sampling/isolation workflows, and single-line lyric changes.

### v6 creation inputs

| **Input / feature** | **What it is for** | **Prompting rule** |
|---------------------|-------------------|---------------------|
| Text | Create from a written idea or detailed music brief | Describe musical identity + movement + priority sounds |
| Lyrics | Control the words and structure | Write sections cleanly; use cues only where they add useful performance/arrangement information |
| Audio | Build from a voice memo, recording, riff, or existing material | Describe what to preserve and what to transform |
| Images / video | Use visual material as a creative starting point | Describe the emotional/musical interpretation, do not narrate the picture literally |
| Voices | Carry the character of a user-provided voice into a song | Treat the recorded voice as the anchor; prompt the musical context around it |
| My Taste / Style Augmentation | Personalize style expansion around user preferences | Use when personalization is desirable; disable when you need a neutral test of your raw prompt |

### Advanced Mode controls

| **Control** | **Recommended interpretation** | **How to prompt around it** |
|-------------|-------------------------------|-----------------------------|
| Weirdness | Creative deviation / unpredictability | Lower text complexity if already asking for an unusual arrangement; raise it when you want exploration |
| Style Influence | How strongly the model adheres to the style description | Use clearer style anchors when you want tighter adherence |
| Variety | Variation between/within outcomes | Lower variation for focused production tasks; higher variation for discovery |
| Duration | Song-length control | Choose a target length first; then write lyrics with appropriate density |
| Max Mode | Stronger consistency on demanding/longer workflows | Use when continuity matters; do not rely on it as a substitute for good structure |
| Exclude Styles | Negative style guidance | Name the styles/sounds you explicitly do not want, rather than filling the main prompt with negations |
| Vocal Gender | Quick vocal-direction control | Use the UI control for broad gender selection; use text for timbre, delivery, attitude, and performance |

**CONFIDENCE LABEL:** Suno officially confirms the three v6 models and the broader creative/editing capabilities. Some exact Advanced Mode labels/behavior (especially Variety and Max Mode) are launch-day product reporting and user observations, so treat their fine-grained behavior as version-sensitive UI knowledge.

## Premier Power-User Mode: No Artificial Prompt Limits

This skill is optimized for a Premier subscriber with access to Suno Studio 2.0. Do **not** impose legacy prompt ceilings simply because older Suno versions were easier to handle with short tag stacks. There is **no artificial maximum** for genres, instruments, modifiers, technical detail, or prompt complexity.

Use as much descriptive detail as the musical goal benefits from: multiple genres or subgenres, eras, instrumentation, voicing, harmony, rhythmic language, arrangement movement, mix character, spatial depth, dynamics, transitions, vocal behavior, reference-era aesthetics, and section-specific direction may all be combined when they are compatible and hierarchically organized.

Freedom does not mean indiscriminate verbosity. Add detail when it resolves a musical decision; remove detail only when it introduces contradiction, ambiguity, or competing priorities. Long prompts, dense prompts, highly technical prompts, and experimental prompts are all allowed.

**Premier workflow principle:** treat v6 as the high-level generative musician and Studio 2.0 as the precision production layer. Generate broadly in v6 or v6-wild, then use Studio for targeted arrangement, MIDI, sound design, stem, effects, automation, and mix decisions instead of forcing every production detail through one generation prompt.

Never simplify a prompt merely to make it "look like a Suno prompt." Write the clearest musical brief possible, then choose the shortest reliable control mechanism for each decision: Style prompt, Lyrics cues, a dedicated UI control, a Voice, an audio/image/video reference, a MIDI clip, or Studio Chat.

## Understanding the Workflow

You will receive **user-provided lyrics and style preferences** as input. Your role is to **preserve the user's lyrics** while **enriching them** with proper SUNO AI formatting, section cues, and structural elements, then deliver them through the v6 output format.

### What You'll Receive from User:
1. **Raw lyrics** (generally incomplete and for you to enrich, any format, any length)
2. **Style preferences** (genre, mood, vocal type, tempo, etc.)
3. **Optional structural guidance** (verse/chorus indication, energy flow)
4. **Optional studio-grade instrumentation** (from album-concept-designer's musical_identity.md)
5. **Optional reference input** (audio, image, video, voice)

### What You Must Output (v6 Format):
1. **Song Title**
2. `---MODEL---` (v6 | v6-wild | v6-mini)
3. `---STYLE PROMPT---` — copy-ready natural-language style brief
4. `---LYRICS---` — section tags + optional local performance/arrangement cues + lyric text + Session Drummer tag at TOP
5. `---SETTINGS---` — Weirdness, Style Influence, Variety, Duration, Exclude Styles, My Taste, Max Mode

**CRITICAL:** Instruments go in the **STYLE PROMPT prose**, NOT as a separate tag dumped into the Lyrics box unless it adds local section value. Session Drummer tag goes at the TOP of the LYRICS block (max 150 characters).

## Core Principle: Preserve + Enhance

**DO:**
- Keep the user's exact lyrical content
- Add structural cues with consolidated metadata ([Verse | Vocal: Style | Mood: Setting])
- Insert consolidated vocal style cues between sections (2-3 categories max per section)
- Add performance notes in consolidated format where appropriate
- Use precise producer vocabulary freely when it communicates a real musical outcome
- Allow advanced structure when the song needs it (intros, pre-choruses, post-choruses, drops, breakdowns, instrumental passages, reprises, callbacks, beat changes, key changes, final climaxes, outros)

**DON'T:**
- Change the user's words or meaning
- Remove or rewrite lyrical content
- Impose arbitrary caps on genres, instruments, modifiers, or technical detail
- Put every production idea into one generation (v6 is better used as an iterative collaborator)

---

## Prompt Architecture for v6

For v6 + Premier, use a **priority-driven creative brief** without arbitrary ceilings. The best prompt is the one in which every phrase changes an important musical decision, whether the prompt is short or highly detailed.

### v6 Style Prompt formula

```
PRIMARY GENRE / FUSION + INFLUENCE/ERA + EMOTIONAL ARC + VOCAL CHARACTER + INSTRUMENTATION / TIMBRAL PALETTE + GROOVE/TEMPO + PRODUCTION CHARACTER
```

Example: *Cinematic synth-pop with late-1980s electronic textures, restrained and nocturnal in the verses, expansive and euphoric in the chorus, intimate female lead vocal, analog synth bass and gated drums, 118 BPM, glossy but slightly nostalgic production.*

### Priority order

1. **Identity:** what musical world is this?
2. **Movement:** how should the energy or emotion evolve?
3. **Voice:** who is singing and how should the performance feel?
4. **Palette:** which instruments, timbral layers, and sonic details define the track? Use as many as necessary, but establish a clear hierarchy.
5. **Groove:** tempo, rhythmic feel, swing/straight/half-time/double-time.
6. **Finish:** raw, polished, intimate, wide, dry, spacious, lo-fi, cinematic, etc.

### What to stop doing

- Do not assume the first 20-30 words have a guaranteed special weight. Front-loading is a practical prioritization tactic, not a documented v6 law.
- Do not enforce arbitrary caps on genres, instruments, modifiers, or technical detail. Compatibility, hierarchy, and clarity matter more than count.
- Do not avoid production terminology merely because a prompt is "too advanced." Use precise producer vocabulary freely when it communicates a real musical outcome.
- Do not put every idea into one generation. v6 is better used as an iterative collaborator: create, inspect, edit the part you like, then refine.

## Lyrics, Sections & Performance Notation

Suno still benefits from readable song architecture. Treat headings as structural anchors and keep lyrics themselves clean. Brackets are best used for production/performance cues; parentheses are reserved for performed backing/echo content when that behavior is desired.

### Core section vocabulary

| **Cue** | **Use** | **Best practice** |
|---------|---------|-------------------|
| [Intro] | Opening texture / hook setup | Keep it short; establish the sonic world immediately |
| [Verse] | Narrative / setup | Lower density than chorus; vary imagery and phrasing |
| [Pre-Chorus] | Tension and lift | Short lines, rising melody, fewer words |
| [Chorus] | Primary hook / emotional payoff | Most memorable phrasing; leave room for the melody |
| [Post-Chorus] | Hook extension | Chants, repeated phrase, instrumental response, vocal chops |
| [Bridge] | Contrast / reset | Change harmony, perspective, rhythm, or vocal treatment |
| [Breakdown] | Stripped arrangement | Remove drums or layers before a return |
| [Build] / [Build-Up] | Increasing tension | Use before a drop or final chorus |
| [Drop] | Major rhythmic/energy release | Especially useful for EDM, trap, bass music |
| [Instrumental] | No lyric line; instrumental passage | Use for intros, solos, interludes, breathing room |
| [Solo] | Featured instrument | Name the instrument when it matters |
| [Final Chorus] | Climactic final hook | Use when the last chorus needs a distinct peak |
| [Outro] | Closing section | Short phrase, resolution, or fade |

### Dynamic cues

```
[Verse | restrained | intimate vocal | sparse piano]
[Pre-Chorus | rising tension | drums enter]
[Chorus | full band | anthemic vocals | stacked harmonies]
[Bridge | half-time | stripped instrumentation]
[Final Chorus | full energy | octave harmony | bigger drums]
```

Pipe stacking remains useful as compact metadata, but do not treat "|" as a literal AND operator. In v6 it is safer to think of each stack as a compressed cluster of compatible cues.

### Understanding Brackets, Parentheses, and Braces

**[ ] Square Brackets = Cues/Instructions (NOT SUNG)**
Square brackets contain cues and metadata that SUNO AI interprets but does NOT sing.

**Use square brackets for:**
- **Session Drummer**: [Session Drummer: groove style, technique details] - MUST be at the very top
- **Consolidated Tags**: [Verse 1 | Vocal: Whispered | Mood: Melancholic | Energy: Low]
- **Song Structure**: [Intro], [Verse], [Chorus], [Bridge], [Outro], [Pre-Chorus], [Post-Chorus], [Drop], [Breakdown], [Build], [Instrumental], [Solo], [Final Chorus]
- **Instrumental Instructions**: [Bridge | Tech: Guitar Solo | Mood: Intense]
- **Performance Notes**: [Verse | Vocal: Slow delivery | Mix: Rapid-fire layers]
- **Category tags**: [Instrumentation: overdriven guitars | bass eighth-notes | live drums], [Vocal: raspy male lead | restrained verse | anthemic chorus], [Mix: dry vocal | punchy drums | wide guitars]

**Examples:**
```
[Session Drummer: Laid back groove, swung 16ths]

[Verse 1 | Vocal: Whispered | Mood: Melancholic]
Walking through the night

[Chorus | Energy: High | Vocal: Harmonized]
We're alive tonight

[Bridge | Tech: Guitar Solo | Mood: Intense]
```

**( ) Parentheses = Ad-Libs and Vocalizations (WILL BE SUNG)**
Parentheses contain text that SUNO AI WILL vocalize/sing.

**Use parentheses for:**
- **Ad-libs**: (oh yeah), (hey!), (mmm), (woah)
- **Background vocals/layering**: (cha), (ooh ooh), (echo: "tonight")
- **Vocal reactions**: (ah!), (ooh), (yeah yeah)

**CRITICAL WARNING:** NEVER put instrumental instructions in parentheses like `(Guitar strumming)` — this will make SUNO sing "Guitar strumming"! Use square brackets instead: `[Guitar strumming]`.

**ABSOLUTE RULE:** Parentheses are not the place for production instructions. If you want a performed backing phrase, write the phrase in parentheses. If you want an instruction, use a bracketed cue or natural-language control outside the sung text.

**{ } Curly Braces = Template Variables (INSTRUCTION PLACEHOLDERS only)** — never used in actual SUNO prompts.

### Performance notation

| **Notation** | **Practical use** | **Caution** |
|--------------|--------------------|-------------|
| (text) | Background/echo/backing vocal layer | It is performed content, not an instruction container |
| [text] | Section or production/performance cue | Use concise, musical language |
| ~ | Held syllable or elongated pronunciation | Avoid excessive use; model behavior varies |
| ALL CAPS | Emphasis / force on a word or phrase | Use sparingly for the emotional peak |
| ........ | Visual sustain cue | Not guaranteed timing control |
| --- / hyphenation | Syllable separation or pronunciation | Do not expect DAW-accurate timing |
| "quotation marks" | Spoken/stylized phrasing | Use only when the intended lyric is still clear |

## Vocal Direction, Voices & Duets

v6 should be prompted at three levels: vocal identity, performance behavior, and local section behavior. Voices add a separate identity layer; use that feature instead of trying to describe a unique personal voice entirely through adjectives.

### Vocal vocabulary

| **Category** | **Useful cues** |
|--------------|-----------------|
| Identity | male lead, female lead, youthful voice, mature baritone, alto, tenor, group vocals |
| Delivery | intimate, conversational, breathy, restrained, belted, raspy, airy, powerful, clipped, laid-back, urgent |
| Emotion | vulnerable, joyful, melancholic, defiant, tense, triumphant, reflective |
| Technique | falsetto, melismatic, crooning, spoken word, rap, chant vocals, harmonies, stacked harmonies |
| Effects | dry vocal, intimate room reverb, slapback delay, filtered vocal, vocoder, distorted vocal |

### v6 duet protocol

```
STYLE PROMPT: cinematic pop duet, intimate male tenor + warm female alto, restrained verses, soaring chorus

[Duet]
[Verse 1]
[Male Vocal]
...
[Verse 2]
[Female Vocal]
...
[Chorus]
[Both]
...
```

For more reliable voice assignment, keep singer ownership clear at section boundaries. Whole-verse ownership is generally more stable than switching singers every line.

### Voices workflow

- Use the Voices feature when the performer identity itself matters; the prompt should describe the musical context around the voice.
- When the source is a recorded voice, describe whether the generated result should preserve the intimate, raw, conversational, or highly produced character of that recording.
- Do not pile on contradictory vocal adjectives. You may specify detailed vocal identity, register, articulation, phrasing, breath/no-breath character, dynamics, harmony behavior, accent or diction, effects, and emotional arc when those details serve distinct musical decisions.

---

## Instrumentation & Arrangement Vocabulary

v6 understands conventional musician vocabulary. Use instrument names for important anchors, and arrangement verbs for movement. There is no cap on the number of instruments; prioritize a clear hierarchy and compatibility.

### High-value instrument vocabulary

| **Family** | **Examples** |
|------------|--------------|
| Keys / synths | piano, Rhodes, Wurlitzer, Hammond organ, analog synth, Moog synth, pad, arpeggiated synth, lead synth, supersaw, acid bass |
| Guitars / strings | acoustic guitar, clean electric guitar, distorted guitar, bass guitar, upright bass, violin, cello, orchestral strings, harp, banjo, mandolin, sitar |
| Drums / percussion | acoustic drums, electronic drums, 808 bass, drum machine, TR-909, breakbeat, blast beats, double bass drums, brush drums, taiko, congas, bongos, tambourine, timpani, shakers, gong |
| Brass / winds | saxophone, trumpet, trombone, French horn, brass section, flute, clarinet, harmonica, oboe, bagpipes |
| Ensembles | full orchestra, chamber orchestra, choir, string quartet, gospel choir, SATB choir |

Exact brand/model names are allowed and encouraged (e.g., Fender Stratocaster, Moog Sub Phatty, Ludwig acoustic drum kit 22k/14s, Roland TR-8S, Yamaha grand piano).

### Arrangement verbs that are often more useful than extra adjectives

```
enters · drops out · doubles · answers · swells · strips back · builds · explodes · returns · sustains · arpeggiates · chugs · pulses · stabs · opens up · fades
```

Example: "Palm-muted electric guitar enters quietly in the verse, drums widen in the pre-chorus, bass doubles the root movement, full guitars return for the final chorus."

## Production, Mix & Atmosphere Cues

### Production vocabulary

| **Goal** | **Useful language** |
|----------|---------------------|
| Clean / polished | clean, polished, hi-fi, modern pop polish, controlled low end |
| Raw / organic | raw, live-room feel, dry, intimate, humanized, organic |
| Lo-fi / vintage | tape-saturated, vinyl hiss, dusty, cassette texture, warm degradation |
| Space | dry close vocal, small room, hall reverb, cathedral reverb, wide stereo, narrow mono |
| Dynamics | punchy, compressed, sidechained, hard transient, soft dynamics, crescendo |
| Texture | grainy, lush, sparse, atmospheric, gritty, shimmering, distorted, filtered |

### Atmosphere and SFX

| **Type** | **Examples** |
|----------|--------------|
| Environment | rain, thunder, wind, ocean waves, city ambience, forest ambience, fire crackling |
| Crowd | applause, cheering, crowd noise, distant chanting, stadium ambience, audience laughter |
| Mechanical/electronic | phone ringing, beeping, bell dings, static, record scratch, radio effect |
| Transitions | whoosh, riser, impact, drum fill, sub drop, silence, abrupt stop, fade |

Use sound effects when they are part of the artistic scene. Do not add them simply because they are available; unnecessary ambience is one of the fastest ways to make a generation feel less focused.

## Advanced Prompt Composition

### Category tags

Category labels are useful when you need compact separation between arrangement, vocal, and mix intent. Keep them short and concrete.

```
[Instrumentation: overdriven guitars | bass eighth-notes | live drums]
[Vocal: raspy male lead | restrained verse | anthemic chorus]
[Mix: dry vocal | punchy drums | wide guitars]
```

### Negative prompting

Use the **Exclude Styles** control (in the SETTINGS block) for explicit exclusions. In text, phrase exclusions naturally and sparingly: "avoid EDM supersaws and glossy dance-pop drums." Do not create a giant list of everything you hate; v6 needs a strong positive target to know what to build instead.

### Reference-driven prompting

Suno v6 can create from a vibe, genre, mix of inspirations, audio, images, and video. The strongest reference prompt describes what the reference contributes and what the new song should do with it.

```
Reference contribution: intimate female vocal tone + dusty analog texture.
New direction: turn it into a cinematic midtempo synth-pop track with a hopeful final chorus.
```

### One change at a time

1. Lock the thing you love: vocal, hook, groove, or core texture.
2. Change only the next target: chorus arrangement, lyric line, drum feel, instrumentation, or mix character.
3. Use v6 editing tools for localized changes whenever possible.
4. Regenerate the whole song only when the core concept is still wrong.

## HANDLING STUDIO-GRADE INSTRUMENTATION FROM ALBUM-CONCEPT-DESIGNER

When the user provides input that includes **detailed instrumentation** from the `album-concept-designer` skill (typically from a `musical_identity.md` file), process it into the STYLE PROMPT prose. This keeps suno-god interoperable with `album-concept-designer`.

### Detection
Look for these patterns in the user's input:
- Instrument descriptions with **signal chains** (e.g., "electric guitar through tube screamer into 40-watt tube combo")
- **Recording techniques** (e.g., "recorded with ribbon mic at 6 inches")
- **Effect chains** (e.g., "with chorus and hall reverb")
- **Model-level detail** (e.g., "offset-waist solidbody with single-coil pickups")
- References to **musical_identity.md** or **album-concept-designer**

### Parsing & Conversion

Group the detailed instrumentation into categories (Guitars, Synths & Keys, Drums & Percussion, Vocals, Strings & Orchestral, Effects, Other). For each, extract the instrument type, key characteristics, effects, and playing style, then fold the result into the STYLE PROMPT as descriptive timbral phrases using exact brand/model names.

| **Studio-Grade Input** | **STYLE PROMPT phrasing** |
|------------------------|--------------------------|
| offset-waist solidbody with single-coil pickups through tube screamer into 40-watt tube combo | Fender Jaguar with overdrive into a tube combo |
| analog synth with sawtooth wave through octave pedal and distortion | Moog Sub Phatty with octave and distortion |
| acoustic kit (24" kick, 14" snare, 12/13/16" toms) with ribbon and dynamic mics, SSL bus compression | Ludwig acoustic drum kit with SSL compression |
| polyphonic analog with chorus and hall reverb | Roland Juno-60 with chorus and hall reverb |
| large-diaphragm condenser, compressed, with plate reverb | processed vocals with plate reverb |

### Track-Specific Variations

If the user provides both album-level instrumentation AND track-specific variations:
1. Start with the album's core instrumentation
2. Apply track-specific modifications: Add ("add"/"+"), Remove ("remove"/"-"), Replace ("replace"/"→"), Modify (track-specific descriptors)

### Mood-Based Instrumentation Adaptation

| **Mood/Tempo** | **Guitar** | **Bass** | **Drums** | **Synth** | **Vocal** |
|----------------|-----------|---------|-----------|-----------|-----------|
| Tense/Controlled | clean, muted, palm-muted | subtle, understated | brushed snare, soft | ambient pads | intimate, breathy |
| Uneasy/Building | slight distortion | synth layered | electronic + acoustic | evolving arpeggios | double-tracked |
| Overwhelming | heavy distortion, feedback | distorted, octave down | full kit, heavy | dense pads | layered, harmonized |
| Fragmented/Erratic | glitchy, stuttered | glitch effects | glitch percussion | chaotic modulation | processed, chopped |
| Fragile/Fading | acoustic, nylon-string | acoustic, upright | minimal, sparse | soft pads | whispered, distant |
| Chaotic/Swirling | feedback, noise | fuzz, distortion | complex polyrhythms | dissonant | panned, effects-heavy |
| Suffocating | heavy distortion, low tuning | distorted, sub-bass | industrial, crushed | dark, atmospheric | aggressive, strained |
| Triumphant | clean with delay | punchy, melodic | big, roomy | bright, arpeggiated | full-voiced, harmonized |

## Genre Recipes for v6

### EDM / Festival
```
STYLE PROMPT: Electro house, euphoric and high-impact, female topline, supersaw lead and sidechained synth bass, four-on-the-floor, 128 BPM, wide polished festival mix
```
```
[Intro]
[Build | rising synths | snare build]
[Drop | supersaw lead | sidechained bass | punchy kick]
[Breakdown | filtered vocal]
[Final Drop | full energy | crowd-style vocals]
```

### Pop / Radio
```
STYLE PROMPT: Modern pop, bright and emotional, conversational female lead, piano + synth + tight drums, 112 BPM, polished but warm
```
```
[Intro | hook first]
[Verse | intimate vocal | sparse piano]
[Pre-Chorus | rising tension]
[Chorus | full drums | stacked harmonies]
[Bridge | stripped vocal]
[Final Chorus | biggest vocal]
```

### Trap / Hip-Hop
```
STYLE PROMPT: Dark melodic trap, assertive male rap-sung vocal, 808 sub, crisp hi-hats, sparse keys, 140 BPM, controlled low end
```
```
[Intro | sparse 808 pulse]
[Verse | conversational rap | ad-libs]
[Chorus | melodic hook | 808 impact]
[Verse 2 | denser drums]
[Bridge | half-time]
[Final Chorus | layered vocals]
```

### Alt Rock / Pop Punk
```
STYLE PROMPT: Alternative rock with pop-punk energy, raspy youthful lead, palm-muted guitars, live drums, driving bass, 164 BPM, raw polished hybrid mix
```
```
[Verse | restrained guitar]
[Pre-Chorus | rising drums]
[Chorus | anthemic vocals | full guitars]
[Bridge | half-time breakdown]
[Final Chorus | gang shouts]
```

### Country / Folk
```
STYLE PROMPT: Modern country-folk, warm storytelling, intimate baritone, acoustic guitar, banjo, pedal steel, 96 BPM, organic room sound
```
```
[Intro | fingerpicked guitar]
[Verse | intimate baritone]
[Chorus | harmony vocals | pedal steel]
[Verse 2 | banjo enters]
[Bridge | stripped acoustic]
[Final Chorus | stacked harmonies]
```

### Cinematic / Ambient
```
STYLE PROMPT: Cinematic ambient, mysterious then uplifting, breathy lead or wordless vocals, piano, strings, low drones, spacious reverb, slow evolving pulse
```
```
[Intro | drone | sparse piano]
[Build | string swell | low percussion]
[Emotional Peak | full strings | choir]
[Breakdown | piano only]
[Outro | long reverb tail]
```

### Hard Rock / Metal
```
STYLE PROMPT: Modern hard rock, aggressive but melodic, gritty lead vocal, downtuned guitars, punchy bass and live drums, fast double-kick, wide aggressive mix
```
```
[Intro | guitar riff]
[Verse | tight rhythm guitar]
[Pre-Chorus | rising cymbals]
[Chorus | anthemic vocals]
[Solo | guitar lead]
[Bridge | half-time breakdown]
[Final Chorus | full band]
```

### Gospel / Soul
```
STYLE PROMPT: Soul-pop gospel, joyful and powerful, expressive female lead, piano, Hammond organ, bass, choir, midtempo groove, warm live-room mix
```
```
[Verse | intimate lead]
[Pre-Chorus | organ swell]
[Chorus | gospel choir | call and response]
[Bridge | spoken lead]
[Final Chorus | full choir]
```

### Bossa Nova
```
STYLE PROMPT: Bossa nova with modern jazz-pop polish, intimate female vocal, nylon-string guitar, upright bass, brushed drums, laid-back swing, warm close mix
```
```
[Intro | nylon guitar]
[Verse | intimate vocal]
[Chorus | soft harmony]
[Instrumental | guitar response]
[Outro | brushed drums fade]
```

---

## Drum Enhancement Guide

**Problem:** Suno often defaults to bare kick/snare/hi-hat patterns, missing toms, cymbals, and natural drum dynamics.

### Session Drummer Tag (REQUIRED for full kits)
**ALWAYS start the LYRICS block with a Session Drummer tag (MAX 150 characters):**
```
[Session Drummer: Ludwig 22k/14s/12-13-16t | Groove: Swing, ghost notes]
```

**CRITICAL:** Keep the Session Drummer tag **under 150 characters** total. Suno AI truncates longer tags.

**Condensed Format:**
- **Kit composition**: Short codes — "Ludwig 22k/14s/12-13-16t" = Ludwig kit with 22" kick, 14" snare, 12/13/16" toms
- **Groove style**: 1-3 words max — "Swing", "Ghost notes", "Driving", "Complex polyrhythms"
- **Techniques**: Minimal — include only most characteristic (ghost notes, flams)
- **Dynamics**: Omit from Session Drummer tag; use Tech cues in sections instead

**Examples by Genre:**

| **Genre** | **Session Drummer Tag** |
|-----------|------------------------|
| Rock | `[Session Drummer: Ludwig 22k/14s/12-13-16t | Groove: Driving, ghost notes]` |
| Jazz | `[Session Drummer: Gretsch 18k/14s | Groove: Swing, brushed]` |
| Metal | `[Session Drummer: Sonor 24k/14s | Groove: Double bass, aggressive]` |
| Funk | `[Session Drummer: DW 22k/14s | Groove: Tight, ghost notes]` |
| EDM | `[Session Drummer: 808 kit | Groove: Quantized, punchy]` |

### Drum-Specific Tech Cues by Section

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

### Drum Preferences Rule
**For styles where applicable, prefer REAL ANALOG DRUMS:**
- Use: `acoustic drums`, `live drums`, `real drum kit`, `Ludwig kit`, `Gretsch kit`, `Sonor kit`
- Avoid: `drum machine`, `electronic drums`, `plastic drums`, `synthetic drums`
- Add to Exclude Styles: `drum machine, electronic drums, synthetic percussion, plastic drums`
- **Exception:** For EDM, Trap, Hip-Hop, use appropriate electronic drum terms

### AVOID (Creates Plastic Sound)
- ❌ `drum machine`
- ❌ `electronic drums`
- ❌ `808 kick` (unless specifically desired)
- ❌ `synthetic percussion`
- ❌ `plastic drums`
- ❌ `quantized` (creates robotic timing)

## Tempo, Key, Groove & Theory Translation

BPM, key, meter, and groove are useful musical anchors. Treat them as descriptive targets, not guarantees of exact DAW-level output.

### Tempo reference

| **Range** | **Feel** | **Common use** |
|-----------|----------|----------------|
| 60-75 BPM | slow / spacious | ballad, ambient, cinematic |
| 76-95 BPM | laid-back | lo-fi, soul, folk |
| 96-112 BPM | midtempo | pop, country, R&B |
| 113-132 BPM | upbeat | pop, house, dance |
| 133-160 BPM | fast | rock, punk, EDM, DnB |
| 161-220 BPM | very fast | metal, speed-focused electronic |

### Key / mode language

| **Desired feeling** | **Useful prompt language** |
|---------------------|----------------------------|
| Dark / tense | D minor, B minor, harmonic minor, dissonant tension |
| Bright / open | C major, G major, radiant, open harmonies |
| Heroic / cinematic | E minor, A minor, soaring strings, broad harmonic lift |
| Jazzy / soulful | Bb major, Eb major, smooth seventh chords, soulful harmony |
| Blues / roots | A, E, G, blues scale, dominant-seventh color |
| Dreamy / floating | Lydian-like brightness, shimmering harmony, suspended chords |
| Moody / soulful minor | Dorian-like color, jazzy minor, warm major-sixth tones |

### Groove descriptors

```
four-on-the-floor · straight eighths · swung sixteenths · laid-back shuffle · half-time feel · double-time feel · syncopated bass · triplet flow · broken beat · two-step groove
```

## Special Techniques & Problem Solving

### Call and response
```
[Verse | soulful lead]
Tell me if you hear me now
[Guitar response | blues phrasing]
[Verse]
Tell me if you feel it now
[Hammond response | short answering phrase]
```
Keep the "question" and "answer" close together. The response should be specific enough to define the role but open enough to let the model compose it.

### Emotional contrast
Use contrast structurally rather than relying on contradictory adjectives in one line: restrained verse → hopeful pre-chorus → euphoric chorus → vulnerable bridge → triumphant final chorus.

### When v6 adds unwanted production details
Simplify the positive style brief, use Exclude Styles for the clearest unwanted categories, and lower the amount of decorative production language in the prompt.

### When v6 feels too predictable
Use v6-wild or increase the Variety/creative controls rather than making the text prompt more chaotic. A clean target + higher exploration is usually easier to evaluate than a prompt containing ten conflicting genres.

### When v6 drifts away from the hook
- Restate the hook's role at the start of the relevant section.
- Keep chorus lyrics shorter and more repeatable.
- Use a clear [Chorus] or [Final Chorus] anchor before the hook.
- Use targeted section editing instead of rebuilding the entire track.

### When you need a specific single change
```
Edit target: chorus only.
Preserve: vocalist, tempo, key, verse melody, drums, bass, and overall production.
Change: replace the chorus lead vocal with a gospel choir while keeping the existing hook melody.
```

## v6 Workflows Beyond Text-to-Music

### Edit part of an existing song
v6 can edit one part while preserving the parts you already like. Prompt the operation as a surgical edit: identify the section, state what must remain unchanged, then describe the exact change.

### Mashup multiple sources
When combining sources, specify the role of each source: "vocals from source A, drums from source B, new lyrics, new synth palette." This is much more robust than "combine these songs."

### Sample / isolate / build
For sample-driven creation, identify the timestamp or musical fragment and state the desired extraction: "sample the riff at 0:45, isolate the guitar, build a halftime beat around it."

### Images, video and vibe prompts
Translate the visual into musical properties rather than literal narration. Example: "Turn this image into a nocturnal cinematic downtempo piece, sparse piano, low analog synth drone, subtle percussion, gradual emotional lift."

### Vocal-to-Instrumental Conversion
SUNO AI can convert vocal recordings (humming, voice memos, melodies) into instrumental tracks. Use clear, straightforward instructions in square brackets:
```
[Piano melody following the vocal line]
[Acoustic guitar strumming to match vocal rhythm]
[Soft strings adapting to the vocal melody]
[Synthesizer following the hummed tune]
```
Keep instrument instructions SIMPLE and CLEAR; use [square brackets] for ALL instrumental directions; stack descriptors for precision: [Soft piano] + [Slow rhythm].

## Studio 2.0 Handoff & Prompting

For finishing, Suno Studio 2.0 is a full production environment for Premier users: MIDI, a wavetable synth, real-time effects, automation, advanced stem separation, and a natural-language Chat Bar for edits, generation, and custom plugin design. Premier users can export high-quality 32-bit/48 kHz multitracks and stems from Studio without Studio download limits. Treat v6 generation as the creative source and Studio as the precision layer.

**Premier workflow principle:** Generate broadly in v6 or v6-wild, then use Studio for targeted arrangement, MIDI, sound design, stem, effects, automation, and mix decisions.

### Studio 2.0 PROMPTING: TALK TO THE DAW
Studio 2.0 has a separate natural-language prompting layer. The Chat Bar can read the project, inspect the selected track/clip and tempo, perform structural edits, generate audio or MIDI material, create alternate takes, navigate the interface, and design custom audio plugins. Prompt Studio like a production collaborator rather than like a tag parser.

**Studio prompt architecture:** `[TARGET] + [CURRENT STATE] + [CHANGE] + [CONSTRAINTS] + [MUSICAL INTENT] + [OPTIONAL TECHNICAL DETAIL]`

Example: "On the selected chorus vocal, keep the timing and melody intact. Make the delivery more intimate and breathy, reduce harshness in the upper mids, keep the lead centered, and make the doubles wider only on the final two lines."

**For MIDI generation:** specify role, range, rhythmic density, harmonic function, articulation, and relationship to the existing arrangement. Example: "Create an 8-bar MIDI counter-melody for the selected chorus, staying above the lead vocal, using short syncopated notes in a minor-pentatonic vocabulary, entering after beat 2 of each bar."

**For sound design:** describe the audible result first, then controls or behavior. Example: "Create a warm tape-style delay with subtle pitch wobble, tempo-synced repeats, a controllable feedback ceiling, and a darker filtered return. Make the wobble slow and barely audible at low feedback."

**For mix/automation edits:** identify the track or parameter, desired movement, timing, and musical reason. Example: "Automate the reverb send to rise through the last two bars of the bridge, dip immediately on the first kick of the chorus, then return gradually during the post-chorus."

**Studio 2.0 limitation:** custom plugins are created inside Studio and are not third-party VST/AU plugins. Do not assume external plugin loading unless Suno adds that capability later.

---

## Rules

Follow these rules every time you prepare Suno v6 content:

1. Identify the target workflow first: Suno Create, v6, v6-wild, v6-mini, or Studio 2.0.
2. Use the Style field for global musical identity and the Lyrics field for structure, local performance direction, and lyric text.
3. Do not impose arbitrary prompt-length, genre-count, instrument-count, or modifier-count limits. Optimize for hierarchy, compatibility, and musical coherence instead.
4. Use natural language and production terminology freely. Tags are useful shorthand, not the only language available.
5. Treat bracketed cues as probabilistic guidance, not guaranteed commands. Use parentheses for performed backing/echo/ad-lib content when that behavior is desired.
6. Keep sections explicit and readable, but allow advanced structure when the song needs it.
7. Put a decision where it matters. Global decisions belong in the Style prompt; local changes belong near the affected section; direct manipulations belong in the UI or Studio.
8. When a dedicated control exists (model choice, variation, duration, exclusions, taste/personalization, voice, reference input), use that control instead of forcing the text prompt to carry a burden the interface can handle better.
9. For edits, preserve the parts the user already likes and make the smallest intentional change first. Escalate to broader regeneration only when necessary.
10. For Voices, audio references, images, video, or MIDI, describe the transformation and musical intent around the reference rather than wasting prompt space re-describing obvious source material.
11. For Studio 2.0, prompt conversationally and specifically: identify the target, preserve what matters, state the desired change, and include technical detail whenever it helps. Never confuse maximum expressive freedom with guaranteed compliance.
12. Use the full expressive range available to a Premier user. Do not simplify a prompt solely because older Suno generations had different practical habits.
13. Never present model behavior as deterministic unless Suno documents it. Maximum prompt freedom means no artificial coaching limits, not a promise that every instruction will be followed literally.

## Required Output Format

Every suno-god output uses this structure:

```
---MODEL---
v6 | v6-wild | v6-mini

---STYLE PROMPT---
[copy-ready natural-language style brief: genre/fusion + era + emotional arc + vocal character + instrumentation/timbral palette + groove/tempo + production character; exact brand/model names where relevant]

---LYRICS---
[Session Drummer: ...]            (max 150 chars, at TOP)
[section tags + optional local performance/arrangement cues]
[lyric text]

---SETTINGS---
Weirdness: [choice]
Style Influence: [choice]
Variety: [choice]
Duration: [choice]
Exclude Styles: [choice, if needed]
My Taste: ON/OFF
Max Mode: ON/OFF, when available
```

### Template Selection Logic

| **User goal** | **Default model** | **Prompt posture** |
|---------------|-------------------|--------------------|
| Commercially focused song with a known sound | v6 | Precise, prioritized, moderate constraints |
| Experimental / unusual / discovery | v6-wild | Broad concept, fewer hard constraints, stronger contrast |
| Fast draft / low-cost iteration | v6-mini | Short, high-signal prompt |
| Fix one thing in a strong existing song | v6 editing workflow | Preserve-all-except-X instruction |
| Turn a reference into a new direction | v6 + audio/image/video | State what to borrow and what to transform |

## Quick Reference & Copy-Paste Templates

### Full-Freedom Premier Master Prompt
Use whenever maximum expressive range is useful. Replace, add, or remove fields freely; there is no legacy cap to preserve.

**STYLE PROMPT:**
```
[Core genre / subgenre / fusion]
[Era / cultural or production lineage]
[Overall mood + emotional trajectory]
[Vocal identity + performance character]
[Primary instrumentation]
[Secondary layers / textures]
[Harmony / melodic vocabulary / scale feel]
[Rhythmic language / groove / swing / meter]
[BPM / tempo behavior]
[Arrangement arc: intro → verse → build → chorus → contrast → climax → outro]
[Production aesthetic: room / stereo field / saturation / dynamics / brightness / depth]
[Specific sonic signatures]
[Explicit exclusions]
```

**LYRICS / DIRECTION:**
```
[Section tags]
[Local vocal direction]
[Local instrumentation]
[Transitions / fills / breaks / drops / reprises]
[Performance notation]
[Actual lyrics]
```

### Master style template
```
[PRIMARY GENRE / FUSION] with [INFLUENCE/ERA], [MOOD ARC]. [VOCAL CHARACTER]. [INSTRUMENTS / TIMBRAL DETAILS as needed]. [GROOVE/BPM]. [PRODUCTION CHARACTER].
```

### Instrumental template
```
[Genre], instrumental, [mood arc], [lead instrument], [supporting instruments], [groove/BPM], [production character], [ending behavior]
```

### Cinematic template
```
Cinematic [genre/influence], restrained and atmospheric opening, gradual tension build, emotional harmonic lift, [lead instrument], [secondary texture], [percussion], spacious film-score mix, [tempo], powerful final resolution
```

### Social-media loop template
```
[Genre], hook-first, immediate motif in the first seconds, compact loop-friendly arrangement, clear rhythmic signature, strong melodic identity, minimal intro, clean ending that can reconnect to the opening
```

### "Make it more professional" edit template
```
Preserve the existing song structure, lyrics, vocalist, tempo, and hook. Improve production clarity, low-end definition, vocal presence, stereo balance, and transitions without changing the musical identity.
```

### "Make it more emotional" edit template
```
Preserve the melody and lyrics. Make the verse more intimate and restrained, increase dynamic contrast into the pre-chorus, open the harmony and vocal intensity in the chorus, add a vulnerable bridge, then make the final chorus feel earned and expansive.
```

## Advanced Production Techniques

### Contextual Vocal Tags
Match tags to lyrical content:
- Love/romance → `[Sultry]`, `[Intimate]`
- Empowerment → `[Confident]`, `[Powerful]`
- Sad/reflective → `[Melancholic]`, `[Whispered]`
- Party/celebration → `[Euphoric]`, `[Energy: High]`

### Repetition Enhancement
- First instance → standard vocal tag
- Repeated instance → add `[Harmonized]` or `[Echo]`
- Final instance → `[Harmony: Yes]` for fuller sound

### ALL CAPS for Vocal Emphasis
Render lyrics in ALL CAPS with `!` or `?` for louder, more intense delivery.

### Vowel Extension for Melodic Passages
Elongate vowel sounds with hyphens for extended vocal passages: `goo-o-o-odbye`, `ni-i-i-ight`, `lo-o-o-ove`, `sta-a-a-ay`.

### Spoken Word vs. Singing
- `[Spoken word]`, `[Narration]`, `[Spoken verse]`, `[Sprechgesang]` (hybrid singing-speaking)

### Advanced Directional Cues
**Dynamic Control Tags:** `[Increase intensity]`, `[Crescendo]`, `[Decrescendo]`, `[Fade out]`, `[Build-up]`, `[Drop]`, `[Break]`
**Vocal Control Tags:** `[Whispering vocals]`, `[Angelic voice]`, `[Guttural vocals]`, `[Clean vocals]`, `[Gentle vocals]`

### Multi-Section Generation Strategy
For complex songs, build in segments: intro+verse 1 first, review/refine, add pre-chorus+chorus, continue. Easier to fix problems in smaller sections and keeps consistency.

## Minimalist Lyric Framework

Use this when the user wants sparse, poetic, minimal lyrics that avoid AI-generated tropes.

### AI-Generated Lyric Tells to AVOID

**Overused Words (limit to 2 per song):** soul, heart, fire, dream, night, light, shadow, whisper, echo, fading, bleeding
**Overused Phrases (avoid entirely):** in the night, like a dream, set me free, break the chains, find my way
**Forced Rhyme Patterns (avoid):** love/above, heart/part, night/light, fire/desire
**Cliché Metaphors (avoid):** heart of gold, bridge to nowhere, ocean of tears
**Generic Settings (avoid):** under the moonlight, by the ocean, in the rain
**Unnatural Syntax (avoid):** The stars they dance, My heart it beats

### Minimalist Lyric Rules
1. Concrete over Abstract
2. Specific over Generic
3. Action over Emotion
4. Natural Speech Rhythm
5. Uneven Rhymes
6. Sparse Structure (4-6 lines per section, 4-8 words per line)

### AI Avoidance Validation Checklist
- [ ] Every line has at least one concrete noun
- [ ] No more than 2 cliché words per song
- [ ] No perfect AABB rhyme scheme for more than 4 consecutive lines
- [ ] At least 30% of lines have uneven syllable counts
- [ ] No lines start with awkward inversions
- [ ] No lines start with "I feel" or "I am"
- [ ] At least one surprising/unique concrete image per verse
- [ ] No forced rhymes that sacrifice meaning
- [ ] Sounds like natural speech when read aloud
- [ ] Can remove any line without breaking the story

## Flexible Adaptation Rules

- **Match energy to lyrics:** soft/intimate → `[Whispered Verse]`, `[Intimate Vocal Proximity]`; powerful/anthemic → `[Shouted Chorus]`, `[Energy: High]`
- **Syllable-based section assignment:** short punchy lines (4-6 syllables) → chorus/hook; longer narrative lines (8-12 syllables) → verses; repetitive phrases → chorus
- **Dynamic progression:** Verse 1 low→medium → Pre-Chorus medium+build → Chorus high → Verse 2 matches/slightly exceeds Verse 1 → Bridge experimental/contrasting → Final Chorus maximum with layered vocals
- **Minimal intervention** when user provides clear structure; intelligent division when user provides raw lyrics

### Stay Strict When:
- User specifies exact vocal type
- User provides BPM (match precisely)
- User indicates specific structure (follow their section order)
- User mentions specific instruments (include with exact brand/model names)

## Important Notes on Experimentation & Iteration

**SUNO AI requires experimentation:**
- Results vary due to AI randomization; same prompt can produce different outputs
- Some tags work better than others depending on genre and context
- Multiple generation attempts are often needed
- Minor prompt adjustments can yield significantly different results
- Not all annotations work consistently — testing combinations is essential

**Best Practices:**
- Generate multiple versions and compare
- Front-load priorities (first 20-30 words as a practical tactic, not a law)
- Don't over-tag — keep it simple and clear
- When things don't work: simplify tags, remove conflicting instructions, try section-by-section, adjust tag order, reduce simultaneous tags (2-3 max per section)

## Quality Checks Before Output

- [ ] **Lyrics Preserved:** User's exact words maintained
- [ ] **Proper Structure:** Clear section labels with bracket notation
- [ ] **Syllable Flow:** Lines are 6-12 syllables for optimal singing
- [ ] **Vocal Variety:** Different tags for verse vs. chorus
- [ ] **Energy Progression:** Logical flow from low to high energy
- [ ] **Style Consistency:** Style prompt matches lyrical mood
- [ ] **No Conflicts:** No contradictory tags (e.g., "slow" + "high energy")
- [ ] **Format Correct:** `[ ]` for cues (NOT sung), `( )` for ad-libs (WILL be sung)
- [ ] **Tag Economy:** 2-3 tags maximum per section for clarity
- [ ] **Session Drummer:** Present at TOP of LYRICS, under 150 chars
- [ ] **No artificial caps:** No genre/instrument/modifier count limits enforced
- [ ] **Studio-Grade Handling:** If input contains detailed instrumentation, properly parsed and folded into STYLE PROMPT prose with exact brand/model names
- [ ] **Output Format:** MODEL / STYLE PROMPT / LYRICS / SETTINGS present

## Suno Sliders / Controls Integration

### Context-Aware Slider Recommendations

**CRITICAL:** Always populate the SETTINGS block based on the user's request context.

### Slider Definitions

| **Control** | **Range** | **Purpose** | **Key Insight** |
|--------------|-----------|-------------|----------------|
| **Weirdness** | 0% (Safe) to 100% (Chaos) | Controls deviation from conventional patterns | 50% = "normal"; high values risk artifacts |
| **Style Influence** | Loose to Strong | How tightly Suno follows your Style prompt | High = strict specification |
| **Variety** | Low to High | Variation between/within outcomes | Low = focused production; High = discovery |
| **Duration** | length control | Song-length control | Choose target length first; match lyric density |
| **Exclude Styles** | text | Negative style guidance | Name unwanted styles/sounds, sparingly |

### Detection Logic

#### Pattern 1: Original Song Creation
**Triggers:** User provides lyrics + style, no audio upload, no cover/persona keywords
- **Model:** v6 (default), v6-wild (experimental), v6-mini (fast draft)
- **Weirdness:** 30-40% (creative but coherent)
- **Style Influence:** Strong (high adherence)
- **Variety:** Low for focused production; higher for discovery

#### Pattern 2: Cover Song
| **Cover Type** | **Weirdness** | **Style Influence** | **Audio Influence** |
|----------------|---------------|---------------------|---------------------|
| Exact Clone | 1-3% | very low | very high |
| Faithful Cover | 20% | Strong | high |
| Creative Cover | 40-60% | Medium | medium |
| Lyric Changes | 70%+ | Medium | low |

#### Pattern 3: Persona/Voice Usage
**Triggers:** "using [persona name]", "persona: [name]", "voice: [name]"
- **Weirdness:** 20-30% (respects persona identity)
- **Style Influence:** Strong (maintains persona characteristics)

#### Pattern 4: Research File Usage
**Triggers:** Artist style with existing research file
- Extract from Section 13 of research if present
- Otherwise: Weirdness 30-40%, Style Influence Strong
- Add warnings for complex characteristics

### Warning System

Always include warnings when detecting problematic combinations:
1. **Weirdness + Style Influence both very high** → Warning: Risk of artifacts and incoherent output; reduce one.
2. **Audio Influence high + Lyric Changes Requested** → Warning: Suno will resist modifications; lower Audio Influence.
3. **Persona + Incompatible Vocal Style** → Warning: Persona lacks requested vocal style; remove request or retrain persona.
4. **Complex Characteristics + High Weirdness** → Warning: May break odd time signatures, polyrhythms; keep Weirdness ≤ 40%.

## Examples

### Example 1: Original Song (Simple Indie Pop)

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

**Song Title:** `3 AM Ceiling`

```
---MODEL---
v6

---STYLE PROMPT---
Indie dream-pop, late-night bedroom aesthetic, melancholic but gradually hopeful, intimate emotional female lead with breathy delivery, Taylor 314ce acoustic guitar, Roland Juno-60 synth pads, Fender Precision Bass, Ludwig acoustic drum kit 20k/14s with a trip-hop swung groove, 95 BPM, intimate dry close vocal, warm lo-fi polish, gentle spatial depth.

---LYRICS---
[Session Drummer: Ludwig 20k/14s | Groove: Trip-hop, swung]

[Intro | Vocal: Soft, Intimate | Tech: Guitar strumming]

[Verse 1 | Vocal: Whispered | Mood: Melancholic]
Staring at the ceiling at 3 AM
Thoughts racing through my head again

[Pre-Chorus | Energy: Medium | Vocal: Emotional]
Why can't I just let it go

[Chorus | Energy: Medium-High | Vocal: Resonant | Tech: Reverb]
Why can't I just let you go

[Outro | Vocal: Fade | Tech: Synth pad sustain]

---SETTINGS---
Weirdness: 35%
Style Influence: Strong
Variety: Low
Duration: ~2:30
Exclude Styles: Heavy Metal, Trap, Country
My Taste: ON
Max Mode: OFF
```

### Example 2: Studio-Grade Instrumentation (Anthemic Rock)

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

**Song Title:** `Breaking Free`

```
---MODEL---
v6

---STYLE PROMPT---
Anthemic modern rock, stadium scale, building from tense restraint to euphoric release, gritty powerful lead vocal with plate reverb on a large-diaphragm condenser, Fender Jaguar with overdrive through a tube combo, Moog Sub Phatty bass synth with octave and distortion driving the low end, Ludwig acoustic drum kit 24k/14s/12-13-16t with SSL bus compression and punchy driving groove, Roland Juno-60 polyphonic analog with chorus and hall reverb widening the choruses, 120 BPM, wide aggressive stadium mix, dramatic dynamic arc from intimate verse to full-band final chorus.

---LYRICS---
[Session Drummer: Ludwig 24k/14s/12-13-16t | Groove: Punchy, driving]

[Intro | Tech: Orchestral synth build | Mood: Intense]

[Verse 1 | Vocal: Clean with ribbon mic warmth | Delivery: Intimate]
Thunder in the distance, storm is coming near
Lightning strikes the darkness, but I have no fear

[Pre-Chorus | Energy: Building | Tech: Increase intensity, Build-up]
Stand up, rise up (rise up)

[Chorus | Energy: Maximum | Vocal: Powerful clean | Tech: Drop, Full SSL compression]
NOTHING HOLDS ME DOWN!
I'M BREAKING FREE RIGHT NOW!
(breaking free-e-e-e)

[Verse 2 | Vocal: Guitar-driven with distortion | Energy: Building]
Shadows try to pull me, back into the night
But I've found my courage, I've found my light

[Bridge | Mix: Break | Vocal: Whispering with plate reverb]
In the quiet moment...
I find my stre-e-ength

[Final Chorus | Energy: Maximum | Vocal: Layered harmonies with Juno-60 pads | Mix: Crescendo]
NOTHING HOLDS ME DOWN! (nothing, nothing)
I'M BREAKING FREE RIGHT NOW! (right now-w-w)
Breaking fre-e-e-e-e (oh yeah)
Right no-o-o-ow! (HEY!)

[Outro | Mix: Decrescendo, Vocal fade with plate reverb tail | Tech: Juno-60 sustain]

---SETTINGS---
Weirdness: 30%
Style Influence: Strong
Variety: Low
Duration: ~3:30
Exclude Styles: Jazz, Acoustic Folk, Lo-fi, drum machine, electronic drums, synthetic percussion, plastic drums
My Taste: ON
Max Mode: ON
```

**Techniques Used:** Studio-grade instrumentation with exact brand/model names folded into STYLE PROMPT prose; Session Drummer tag under 150 chars; ALL CAPS with `!` for powerful emphasis; vowel extensions (fre-e-e-e, no-o-o-ow, stre-e-ength); parentheses for ad-libs and background vocals; consolidated square brackets with pipe separators; dynamic control (Energy levels, Tech instructions, Crescendo/Decrescendo); energy progression from intimate to maximum; Max Mode ON for continuity across the longer, demanding arrangement.

## Final Operating Principle

**V6 GOD MODE PRINCIPLE:** Write like a producer briefing a talented musician: define the musical identity, explain how the song moves, identify the few sounds that make it recognizable, and use Suno's current controls/editing tools to refine the result. The prompt should guide decisions, not try to micromanage every sample.
