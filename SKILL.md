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
4. Segment the Chinese script semantically. First classify every candidate as `普通信息条` or `重点 PPT 卡`, then select hooks, steps, tool names, numbers, comparisons, key conclusions, and CTA. Skip filler and sentences already covered by subtitles.
5. Produce a motion table before rendering: `time`, `source text`, `overlay text`, `motion form`, `module`, `strength`, and `do/skip`. Include `visual_asset`, `semantic_role`, `asset_source`, and `asset_motion`: decide which tool logos, meaningful icons, or explanatory diagrams accompany the text. Mark text-only scenes explicitly rather than defaulting the whole video to text cards.
6. For this user's video packaging, plan 15 distinct motion scenes per minute: target = max(1, floor(duration_seconds / 60 * 15 + 0.5)). Use the requested segment duration, or full video duration when no segment is specified. Use real video frames for static review when available.
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

For landscape sources or requested style comparisons, read [references/landscape-workflow.md](references/landscape-workflow.md). When comparing all four styles, use the same four excerpts, source frames, copy, and semantic assets for 16 fair-comparison previews. This comparison stage does not approve a final style or authorize animation.

- The presenter is the subject. Treat graphics as annotations, not a replacement for the person.
- Portrait: keep primary graphics in the top-safe band; reserve the lower subtitle/platform area, normally about 520px on a 1080x1920 canvas.
- Landscape talking head: this user's preferred placement is the **upper-left corner**, across all four styles. Recompose for landscape rather than shrinking or stretching portrait cards. On a 1920x1080 canvas, use x=64, y=64 as an initial anchor, not a guaranteed safe placement. Inspect real frames across cuts and gestures to determine usable width and height; protect the actual presenter, hair, hands, subtitles, and important screen-recording UI. The central 40% and bottom ~230px are initial caution zones, not substitutes for inspecting the footage.
- Landscape ordinary cards should remain concise, with a readable title plus a semantic icon/logo and optional supporting line. Landscape重点 PPT cards may grow downward within the verified upper-left free space, using numbered rows, compact comparisons, or short flows. Start with roughly 480-640px width for ordinary cards and 560-760px for structured cards, but adjust to the actual frame. Keep Chinese titles roughly 40-52px and body text 28-36px at 1920x1080; prefer shorter copy or splitting a structured idea over reducing text to unreadable sizes.
- If upper-left placement collides with the presenter or essential footage, flag the affected shots and show an alternative static placement for approval. Do not silently cover the subject or relocate the entire video package. Keep entrance/exit paths inside the verified safe region as well as the held card.
- For a new landscape source, confirm display orientation including rotation metadata, duration, frame rate, and aspect ratio before planning. Use a matching landscape overlay canvas (normally 1920x1080 for 16:9); retain the source aspect ratio for non-16:9 footage. Preview the graphics over actual landscape frames, not portrait mockups. Preserve the existing density, semantic icons/logos,重点 PPT minimum, preview approval gate, and Desktop delivery rules.
- Never cover eyes, nose, mouth, hair, hands, or existing subtitles.
- Keep all text inside its own panel. Widen or wrap a card before shrinking legibility.
- Use fixed design canvases for complex cards, then scale the whole module. Do not squeeze internal layouts with percentage widths.
- Keep copy short and editable through centralized scene data. Do not duplicate the full spoken sentence in the overlay.

## Semantic Logos, Icons, and Diagrams

The user's standing preference is for visually varied cards, not a sequence made only of text. Apply this to all four styles and both ordinary and重点 PPT tiers. Choose assets during semantic analysis, not as arbitrary decoration after layout.

- Named tools or platforms: use a verified official logo when it helps recognition (for example Claude, NotebookLM, Obsidian, or Feishu). Record the source and keep the logo's proportions and brand identity. Do not invent brand marks or substitute a generic icon while calling it official. If a reliable asset is unavailable, use the tool name with a clearly generic symbol and disclose the fallback in the review table.
- Actions and concrete objects: use recognizable icons such as a pen for writing, footsteps for walking, a calendar for scheduling, or a battery for rest and replenishment. Prefer a coherent library such as Lucide; do not mix unrelated icon families or use emoji as the default final artwork.
- Relationships and structured ideas: use process arrows, branching nodes, comparison diagrams, loops, or a short timeline to communicate the actual relationship. A重点 PPT card should favor a meaningful visual structure over a collection of decorative icons beside paragraphs. Never invent numerical chart data.
- Metaphors may use a small illustration when supported by the speech, such as a plant for growth or a charging battery for restoring energy. Keep metaphor distinct from scientific evidence and do not imply claims the speaker did not make.
- Default to one clear visual focus per ordinary card; structured cards may contain related icons for their content units. Keep text-only cards for moments where typography is the stronger choice. Do not impose an arbitrary icon quota or shrink approved text to make room.
- Match the selected style: Capsule uses friendly colored icon badges and restrained small illustrations; BlockFrame uses bold high-contrast sticker-like symbols; Tech Glass uses coherent thin-line nodes and technical diagrams; Minimal Bar uses simple monochrome icons with restrained accent color. Branded logos retain their identity across styles.
- Show the actual selected assets in static previews before MOV approval. Keep asset references in centralized scene data and project assets, with source/license notes where applicable. Assets must resolve locally for export; missing files are an error, not a silent omission.
- Give meaningful visual elements restrained semantic motion, such as a process connector drawing, a check appearing, or a metaphorical battery filling. Do not make all icons rotate or bounce. All assets and their motion must respect the top safe area, face/hair/hand boundaries, and subtitles.
- Apply this to future projects and explicit revisions. Do not silently regenerate previously approved or delivered videos or publish skill changes to GitHub without a request.

## Animation Rules

- Standing user standard: 60 seconds = 15 motion scenes; 120 seconds = 30. Report actual duration and target count in the motion table before implementation. An explicit task-specific count overrides this default.
- Count one independently timed semantic card/scene as one; its title, labels, entrance and exit do not count separately. Average cadence is four seconds, not a mandatory cut every four seconds. Preserve readable holds and transparent pauses.
- Split meaningful comparisons, examples, questions and steps to meet the target; never invent claims or duplicate filler just to inflate the count. If the script cannot support the target, propose the shortfall before rendering.
- Use two visual tiers when analyzing subtitles:
  - `普通信息条`: one short takeaway, tool name, number, or emphasis phrase. Keep it compact and fast, usually one headline plus one short pill or support line.
  - `重点 PPT 卡`: a genuine content unit with multiple related facts, steps, comparison items, a framework, a list, an example, or a conclusion that benefits from structure. Use a larger card with a clear headline plus 2-5 information units such as numbered rows, mini-cards, a timeline, a before/after split, or a checklist. Do not compress complex content into one tiny label.
- A重点 PPT 卡 must be triggered by semantic structure, not merely by a long subtitle. Qualifying signals include `第一/第二/第三`, `一共/分别/包括`, multiple parallel items, a named framework, a comparison, a sequence, a concrete example, or a conclusion with supporting reasons.
- In the motion table, add `level` (`普通` or `重点 PPT`), `content_units`, and `layout` columns. For each重点 PPT 卡, list the exact on-screen units and how they relate; do not hide unreviewed copy inside animation.
- Keep the user's 15-scenes-per-minute target as a planning baseline, but allow one重点 PPT 卡 to hold a denser semantic block. Count it as one scene and give it a longer readable hold; do not create many tiny cards just to satisfy density.
- Hard planning minimum: at least `ceil(duration_seconds / 30)` `重点 PPT 卡` scenes (60s: 2; 120s: 4; 160.67s: 6; 252.63s: 9). Distribute them across the video rather than clustering them in one section. If the script has fewer than the minimum number of genuinely structured ideas, flag the shortfall before rendering instead of inventing content.
- Review priority is: content hierarchy and legibility first, scene count second. If a complex block needs two linked PPT cards to remain readable, split it explicitly and explain the reason in the storyboard.
- The two-tier content system is style-independent. Keep the same semantic units and wording when switching styles; change only the card geometry, palette, typography treatment, placement, and motion grammar required by the selected visual style.
- Style adaptations for重点 PPT 卡:
  - Capsule: large rounded editorial card with 2-5 candy pills, hard offset shadow, serif-led headline, and staggered pill reveals.
  - BlockFrame: large square workbench card with chunky border, hard shadow, numbered tiles, arrows, and tactile slam/pop entrances.
  - Tech Glass / Workflow HUD: translucent glass panel with structured rows, nodes, progress marks, or a split comparison; keep the face corridor clear.
  - Minimal Bar: larger information panel made from layered translucent bars, thin accent rules, numbered rows, or a compact checklist; keep decoration restrained.
- Apply this standard to future tasks and requested replanning. Do not silently rerender an already delivered video to change its count.

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
