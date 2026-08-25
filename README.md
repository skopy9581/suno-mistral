# Suno Songwriter & Album Concept Designer

A suite of Vibe Code skills specialized for AI music creation, heavily optimized for Suno AI prompts.

## Included Skills

### 1. Suno Songwriter
Specialized in formatting and enriching lyrics with technical Suno AI tags (`[Verse]`, `(ad-libs)`, etc.). It preserves your lyrics while adding proper meta tags and structural elements for high-quality music generation.
- **Location**: `skills/suno-songwriter/SKILL.md`

### 2. Album Concept Designer
A creative director for building complex conceptual albums. It handles world-building, storyline, character profiles, and narrative tracklists. It generates an "Album Bible" and track specifications.
- **Location**: `skills/album-concept-designer/SKILL.md`

### 3. Suno Music Researcher
A studio-grade music research specialist. Provides deeply detailed technical breakdowns of musical styles, instrumentation, production techniques, and sonic characteristics.
- **Location**: `skills/suno-music-researcher/SKILL.md`

## Installation

### For Vibe Code

Simply reference the skills directory when setting up your Vibe Code environment:

```
Skills Directory: /path/to/suno-mistral/skills
```

Or copy individual SKILL.md files to your Vibe Code skills folder.

## Usage

### Suno Music Researcher
Use when you need comprehensive musical analysis to inform your album design or track creation.

**Example Input:**
```
Analyze 90s alternative rock style
```

**Output:** Complete 12-section technical profile with studio-grade instrumentation details.

### Album Concept Designer
Use when you want to build a cohesive album story, define characters, set the musical style, create a tracklist, or generate an Album Bible.

**Example Input:**
```
Let's create a concept album about urban alienation
```

**Output:** Interactive workflow guiding you through concept, world-building, characters, narrative arc, and musical identity.

### Suno Songwriter
Use when you have raw lyrics or need to finalize a song prompt with proper Suno AI formatting.

**Example Input:**
```
LYRICS:
Staring at the ceiling at 3 AM
Thoughts racing through my head again

STYLE:
Indie pop, emotional, female vocals, 95 BPM, melancholic but hopeful
```

**Output:** Formatted Style Block + Enriched Lyrics with meta tags ready for Suno AI.

## Workflow Integration

The three skills work together seamlessly:

1. **Suno Music Researcher** → Generates detailed musical profiles
2. **Album Concept Designer** → Uses research to create Album Bible with track specifications
3. **Suno Songwriter** → Formats final lyrics with proper Suno AI tags

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
