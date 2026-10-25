# 夏哥口播视频包装 / Xiage Koubo Video Packaging

[English](README.md) | [简体中文](README.zh-CN.md)

![Xiage Koubo Video Packaging](assets/banner.svg)

## 项目说明（中文）

夏哥口播视频包装是一个 Codex Skill，把**口播视频、SRT字幕或脚本**转化成可审核的动效方案、静态预览，以及最终可叠加到剪映等编辑器里的透明底视频。它同时支持竖屏和横屏，不只是生成几张装饰性文字卡。

**核心能力**

- 四种可选风格：Capsule胶囊风、BlockFrame新粗野主义、Tech Glass科技风、Minimal Bar信息条风。
- 横屏默认放在左上方，竖屏优先上方安全区；按实拍镜头避开人物、头发、手势和字幕。
- 按语义配相关工具Logo、动作图标和流程/对比图。没有核实的Logo时明确使用通用图标，不伪造品牌标志。
- 每分钟约15组动效，至少2组重点PPT卡；长视频按时长计算，重点卡计入总数。
- 比较四种风格时，用同样4段内容各做4张，共16张，方便选出适合本条视频的风格。

**工作流**

检查视频与字幕 → 确定风格或生成四风格对比 → 语义分割与动效表 → 静态实拍预览审核 → 制作动画 → 验证透明通道与遮挡 → 桌面交付。

文案、位置和风格未经审核，不直接制作最终视频。透明MOV通常为ProRes4444、无音轨，从00:00对齐原视频；旧版本保留。

**怎么使用**

```text
用夏哥口播Skill处理这个文件夹里的视频和字幕。
这是横屏视频，卡片放在左上方，注意不要挡住人和字幕。
先选4段内容，四种风格每种各做4张让我比较。
选好风格后，生成带语义图标和重点PPT卡的全量静态预览。
等我审核后再制作透明MOV，保存到桌面。
```

[查看完整中文文档](README.zh-CN.md) · [查看16张横屏示例](assets/landscape/README.md) · [阅读完整工作流](references/landscape-workflow.md)

## Project Overview (English)

Turn talking-head footage, SRT subtitles, or scripts into a semantic motion plan, reviewable static composites, and an approved animation or transparent video overlay. Both portrait and landscape are supported; landscape cards default to the upper-left, subject to actual footage safety checks.

Choose from Capsule, BlockFrame, Tech Glass, and Minimal Bar. Add verified tool logos, semantic icons, and explanatory diagrams rather than relying solely on text. Plan about 15 scenes per minute, including at least two structured PPT cards per minute, with duration-based rounding.

**Workflow:** inspect footage and subtitles → choose or compare styles → segment meaning and plan motion → approve real-frame static previews → animate → validate alpha and placement → deliver to Desktop without overwriting prior versions.

For a style comparison, use the same four excerpts across all four styles: 16 previews. Final animation waits for approval. See the English guide below for installation, usage, requirements, and examples.

A Codex skill that turns Chinese scripts, SRT subtitles, and talking-head videos into reviewable video packaging systems.

It helps Codex do more than generate a few decorative cards. The skill defines a repeatable production loop: understand the source, segment the content, choose a visual language, produce static frames for review, then turn the approved direction into HyperFrames animation or a transparent overlay.

## Why This Skill

Most video motion work fails in one of two places:

- The animation starts before the on-screen copy and sequence are approved.
- The graphics are visually strong but cover the presenter, the existing subtitles, or the meaning of the shot.

This skill puts the review gate before production and keeps the presenter at the center of the layout.

## Four Visual Styles

![Four video packaging styles](assets/style-overview.png)

| Style | Character | Best for |
| --- | --- | --- |
| `1` Capsule 胶囊风 | Cream paper, rounded capsules, candy colors, editorial display type | Creator education, AI tools, personal workflows |
| `2` BlockFrame 新粗野主义 | Thick black borders, hard shadows, saturated poster blocks | Strong opinions, hot topics, high-energy listicles |
| `3` Tech Glass / Workflow HUD | Dark glass panels, process nodes, cyan and orange signals | AI agents, automation, software, product demos |
| `4` Minimal Bar 信息条风 | Restrained translucent bars and compact labels | Talking-head tutorials and interviews where the person stays dominant |

### Capsule

![Capsule style](assets/style-capsule.png)

### BlockFrame

![BlockFrame style](assets/style-blockframe.png)

### Tech Glass

![Tech Glass style](assets/style-tech-glass.png)

### Minimal Bar

![Minimal Bar style](assets/style-minimal-bar.png)

## Workflow

```text
Script / SRT / video
        |
        v
Inspect orientation, duration, subtitles, and face boundary
        |
        v
Choose one of four visual styles
        |
        v
Semantic segmentation and motion table
        |
        v
Duration-based static frames for review (about 15 scenes/minute)
        |
        v
User approves or requests revisions
        |
        v
HyperFrames animation or transparent MOV overlay
```

The skill does not silently choose a style. If a new task does not specify one, it presents the four options and waits.

## Landscape, Icons, and Structured Cards

Landscape talking-head graphics default to the **upper-left**, with placement checked against the actual presenter, gestures, subtitles, and screen content. Layouts are recomposed for landscape, not simply scaled down from portrait cards.

- Plan about 15 distinct scenes per minute, including at least `ceil(duration_seconds / 30)` structured PPT cards.
- Pair tool names with verified logos when available; use semantic icons for actions and diagrams for relationships. Generic icons are never presented as official logos.
- When comparing styles, reuse four excerpts across all four styles: **16 real-video composites**, with identical copy and source frames.
- Review static copy and layout first; animate only after approval. Deliver a transparent MOV on the Desktop, preserving previous versions.

![Landscape comparison: three-part workspace](assets/landscape/comparison-02.jpg)

[Browse all 16 landscape examples and close-ups](assets/landscape/README.md) · [Detailed bilingual workflow](references/landscape-workflow.md)

```text
Use xiage-koubo-video-packaging with this landscape video and SRT.
Place cards in the upper-left, keeping the presenter and subtitles clear.
First compare four excerpts in each of the four styles (16 previews).
After I choose, create the full motion table and static previews with
semantic icons, verified logos where relevant, and structured PPT cards.
Wait for approval before exporting the transparent MOV.
```

## Example Storyboard

The static review phase can produce a full visual sequence before any MOV is rendered.

![Tech Glass storyboard](assets/tech-glass-storyboard.png)

## What It Produces

- A semantic motion table with time ranges, overlay copy, motion form, position, and strength.
- A set of still frames sized for the target platform.
- A contact sheet for fast review.
- HyperFrames animated `MP4` output for script-led videos.
- A transparent `ProRes 4444` MOV for placement above an existing talking-head edit.
- Alpha, layout, face-safety, and subtitle-safety checks before delivery.

## Install

Clone the repository and copy the skill folder into your Codex skills directory:

```bash
git clone https://github.com/yuema4/xiage-koubo-video-packaging.git
mkdir -p ~/.codex/skills
cp -R xiage-koubo-video-packaging ~/.codex/skills/
```

The skill is loaded from:

```text
~/.codex/skills/xiage-koubo-video-packaging/SKILL.md
```

## Use It in Codex

Start with a script or a talking-head video. If the style is not specified, the skill asks you to choose one.

Chinese example:

```text
用 xiage-koubo-video-packaging，
把这段脚本做成竖屏口播视频包装。
先让我选风格，再按时长做语义分割、动效表和静态预览。
我审核后再生成透明底 MOV。
```

English example:

```text
Use xiage-koubo-video-packaging.
Turn this script into a portrait video package.
Let me choose the style first, then create the semantic motion table
and duration-based static previews. Render the alpha MOV only after approval.
```

## Repository Structure

```text
xiage-koubo-video-packaging/
|-- SKILL.md
|-- README.md
|-- README.zh-CN.md
|-- LICENSE
|-- agents/
|   `-- openai.yaml
|-- assets/
|   |-- banner.svg
|   |-- style-overview.png
|   |-- style-capsule.png
|   |-- style-blockframe.png
|   |-- style-tech-glass.png
|   |-- style-minimal-bar.png
|   `-- tech-glass-storyboard.png
|-- references/
|   `-- style-options.md
`-- scripts/
    `-- build_readme_assets.py
```

## Requirements

- Codex with local skill support.
- HyperFrames for animated video output.
- FFmpeg with ProRes support for transparent MOV delivery.
- A source video and SRT when overlaying an existing talking-head edit.

## Scope

This skill focuses on Chinese talking-head and creator-education videos. It is especially useful for Xiaohongshu, WeChat Channels, Bilibili, YouTube tutorials, AI workflow videos, and product explainers.

## License

[MIT](LICENSE) for the skill code and documentation. See [landscape asset notes](assets/landscape/README.md#asset-notes--素材说明) for creator imagery and third-party icon attribution.
