# Landscape talking-head workflow / 横屏口播工作流

## 中文

1. **检查素材**：读取视频显示尺寸、旋转信息、时长、帧率和SRT。重复中英文轨只按目标语言分段。抽查开头、切镜、手势和主体移动，记录人物、字幕及重要屏幕内容的安全边界。
2. **选择风格**：提供Capsule、BlockFrame、Tech Glass、Minimal Bar。用户要求比较时，选择相同的4段口播，每种风格各做4张，共16张；使用相同截图、文案、语义图标，不通过更换内容影响比较。
3. **语义规划**：区分普通信息条与重点PPT卡。按每分钟15组规划，目标数为round(时长秒数/4)；重点卡至少ceil(时长秒数/30)组，计入总数。结构不足时说明，不为凑数编造内容。
4. **配视觉元素**：品牌工具优先使用核实的官方Logo；动作配语义图标，关系配流程或对比图。没有可信Logo时使用工具名称与通用图标，并明确不是官方Logo。图示不是为了装饰而堆叠。
5. **横屏排版**：默认左上。16:9使用1920x1080设计画布，x=64、y=64仅作起点。普通卡通常宽480–640px，重点卡560–760px，均需服从实拍空位。中文标题约40–52px、正文28–36px。不能直接缩小竖屏卡，也不能为了塞内容无限缩小文字。
6. **静态审核**：先给动效表，再生成叠加原视频的静态图、卡片特写和总览。表中列出时间、原话、文案、级别、内容单元、布局、图示含义、素材来源和动效计划。用户确认文字、大小、位置与风格后才开始最终动画。
7. **动画制作**：复用审核版数据、布局与素材；制作进入、层次展开、停留和退出。流程图分步出现，图标动效与含义一致，避免统一无意义弹跳。出入路径也不能遮挡人物。
8. **检查交付**：检查完整解码、时长、透明通道、文字溢出和切镜附近遮挡；不要把静态抽样通过说成全程遮挡验证。透明MOV通常ProRes4444、无音轨、从00:00对齐；帧率与时长明确记录。保存桌面，新版本不覆盖旧版。

上方或左侧并不天然安全。如果左上有脸、手势或演示内容，先展示替代布局再确认，不擅自遮住主体。4K源视频配1080p动效时，只有编辑器未自动适配才设200%缩放。

## English

1. Inspect displayed orientation, rotation metadata, duration, frame rate, subtitles, cuts, gestures, and essential screen content. Ignore duplicate subtitle-language tracks when planning one language.
2. Ask for a style. For a requested four-style comparison, reuse four semantic excerpts and identical source frames/copy/icons across all styles: 16 previews total.
3. Plan approximately 15 distinct scenes per minute and at least two structured PPT cards per minute, rounded up for the minimum. Structured cards count toward the total; do not fabricate content to reach a quota.
4. Choose verified brand logos, semantic icons, and explanatory diagrams during segmentation. Explicitly label generic-symbol fallbacks; do not invent logos or data.
5. Recompose for landscape, preferably upper-left. For 1920x1080, start near (64,64), with roughly 480-640px ordinary cards or 560-760px structured panels. Actual footage determines the safe bounds. Keep text readable; do not shrink portrait layouts wholesale.
6. Review the motion table, real-frame composites, card close-ups, and contact sheets before animation. Record copy, content units, visual role, source, layout, and intended motion.
7. Animate the approved assets and geometry with entrance, staged internal elements, hold, and exit. Keep movement within the safe area.
8. Validate decoding, alpha, duration, layout, and representative transitions. State sampling limits accurately. Deliver a full-canvas transparent ProRes4444 MOV, normally without audio, aligned at zero; preserve previous versions. For 4K footage, apply 200% scaling only if the editor has not already fitted the 1080p overlay.

## Examples

See [all 16 published previews](../assets/landscape/README.md). These are static design examples, not evidence that every moment of the source video is occlusion-free.
