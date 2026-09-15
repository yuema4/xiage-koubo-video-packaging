---
name: xiage-koubo-video-packaging
description: Create reviewable static storyboards and animated video overlays from Chinese scripts, SRT subtitles, or talking-head videos, with an explicit choice among Capsule, BlockFrame, Tech Glass, and Minimal Bar styles. Use for Xiaohongshu video packaging, HyperFrames motion design, and transparent overlay production.
---

# Xiage Koubo Video Packaging

Use this skill for the complete video-visual workflow: turn a script or subtitle track into a concise visual plan, let the user review the text and stills, then build the approved design into HyperFrames animation or a transparent overlay.

## Non-Negotiable Workflow

1. Read the workspace `CLAUDE.md` or `AGENTS.md` before creating files.
2. Inspect the source video, SRT, or script and identify orientation, duration, existing burned-in subtitles, and the presenter's face boundary.
3. If no style is named, stop and present the four style options in [references/style-options.md](references/style-options.md). Do not silently choose one.
4. Segment the Chinese script semantically. Select only hooks, steps, tool names, numbers, comparisons, key conclusions, and CTA. Skip filler and sentences already covered by subtitles.
5. Produce a motion table before rendering: `time`, `source text`, `overlay text`, `motion form`, `module`, `strength`, and `do/skip`.
6. Generate about 20 static PPT-like frames for a long script, or fewer when the script is short. Use real video frames when a source video exists.
7. Save the stills and a contact sheet to the Desktop for review. Stop and ask for approval or revisions.
8. After approval, use the same scene data and layout for animation. Never turn approved stills into motionless stickers: every card needs entrance, hold, internal staging where useful, and exit.
9. Validate layout, face safety, subtitle safety, typography, and output dimensions. For transparent overlays, validate real alpha before delivery.

## Style Gate

The user may choose by number or name. Preserve the choice for the current task:

- `1` Capsule 胶囊风
- `2` BlockFrame 新粗野主义
- `3` Tech Glass / Workflow HUD 科技风
- `4` Minimal Bar 信息条风

Read only the selected style's section in [references/style-options.md](references/style-options.md). A later request such as “继续 Capsule” carries the style forward; a new unrelated task with no style starts at the selection gate again.

## Output Modes

- **Script-to-video:** default to horizontal `1920x1080`, 30fps, no audio, unless the user specifies another format. Use HyperFrames and copy the final video to Desktop.
- **Talking-head overlay:** create a transparent `MOV`, normally ProRes 4444 at 30fps, matching portrait `1080x1920` or landscape `1920x1080`. Put it above the source video in Jianying/CapCut, aligned from `00:00`.
- **Preview-only:** deliver static PNGs and a contact sheet; do not create MOV/MP4 until the user approves.

## Composition Rules

- The presenter is the subject. Treat graphics as annotations, not a replacement for the person.
- Portrait: keep primary graphics in the top-safe band; reserve the lower subtitle/platform area, normally about 520px on a 1080x1920 canvas.
- Landscape talking head: reserve the central 40% face corridor and the lower subtitle band, normally about 230px on a 1920x1080 canvas. Use side and corner zones.
- Never cover eyes, nose, mouth, hair, hands, or existing subtitles.
- Keep all text inside its own panel. Widen or wrap a card before shrinking legibility.
- Use fixed design canvases for complex cards, then scale the whole module. Do not squeeze internal layouts with percentage widths.
- Keep copy short and editable through centralized scene data. Do not duplicate the full spoken sentence in the overlay.

## Animation Rules

- Strong: opening hook, numbered steps, primary workflow, key conclusion, CTA.
- Medium: tool pills, process arrows, comparisons, parameter controls, retry/swap states.
- Light: small metadata, status labels, secondary notes.
- Prefer deterministic timeline-driven motion: slide/pop in, stagger internal elements, hold, then crisp slide or mask exit. Solid card wrappers must not fade into translucent ghosts; designed glass panels may retain their fixed opacity.

## Verification

- Run the project's check/lint command before rendering.
- Inspect representative stills and the final exit frames over the real video.
- Confirm no overflow, clipping, title/body collisions, face coverage, or subtitle overlap.
- For transparent MOV, confirm transparent-only frames have zero alpha and animated frames contain visible alpha. Do not use `avconvert` to rewrite an alpha MOV.
- If the source project is 4K and the overlay is 1080p, tell the user to scale the overlay to `200%` in the editor.

## User Communication

Use Chinese and report the user-visible outcome first: what is ready, where it is saved, which style is active, and what approval is needed next. Explain technical choices only when they affect how the user reviews, imports, or edits the result.
