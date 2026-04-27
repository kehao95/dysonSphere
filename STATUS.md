# Project Status

**Last Updated**: 2026-04-27

## Current Phase

**Phase 3: Manuscript Consolidation and Literature Review Refresh**

建模与可行性分析的第一轮切片已完成。当前重心是把 framework-first manuscript、文献综述、构建产物与控制面吸收到同一现实状态，并收束为可继续发布/送审的稿件基线。

## Recent Progress

- [x] 项目仓库初始化
- [x] 核心概念定义（微位移戴森群、解耦架构）
- [x] 目录结构设计
- [x] 数学模型框架（轨道、质量预算、热平衡初版）
- [x] 第一轮可复现可行性实验
- [x] 理想 Dyson Swarm / Dyson Ring 控制变量 benchmark
- [x] 结构闭合尺度律初版
- [x] 扰动灵敏度一阶切片
- [x] 最优锥角附近的解析局部稳定性结果
- [x] 结构-角度-功率一体化 design map
- [x] Flight-heritage gap benchmark（ACS3 / NEA Scout）
- [x] Fixed bus mass budget threshold（ACS3 heritage lines）
- [x] canonical manuscript build surface 上提到 `Paper/content/manuscript.md`
- [x] 正文已形成可构建 full first draft（Introduction / Framework / Low-latitude slices / Discussion / Conclusion）
- [x] reduced low-latitude support model 的局部 `r-\phi` 线性化已并入正文，并明确收束为 branch-specific boundedness check
- [x] Earth-synchronous illustrative slice 已按 low-latitude optimized branch 的近似 `r_sync=a_\oplus(1-\sqrt{2}\tan\phi)^{1/3}` 修正
- [x] force-model critique 已吸收：正文不再把当前 `\beta_{\min}` 曲线称为 full high-latitude exact ideal-specular branch
- [x] standard Sun-line cone-angle appendix 已并入，用来量化核心 `0.1^\circ`–`1^\circ` 例子相对 reduced screening curve 的小误差与保守性
- [x] 审稿防御精修已吸收：主文 reduced pitch 改名为 `\alpha_{\mathrm{eff}}`，dense same-shell 拓扑动机降调为 design pressure，PV fill-factor 明确为 mass-budget illustration 而非 closed optical-power architecture
- [x] 本地 MNRAS PDF / HTML build 已重新验证通过
- [x] `dr` assisted literature-review refresh 已吸收为 curated prior-art boundary map
- [ ] citation tightening pass（按文献簇逐段收紧正文引用）

## Active Work

| Area | Status | Owner | Notes |
|------|--------|-------|-------|
| 轨道动力学模型 | 🟡 First pass scoped | Codex | 正文主线已收束为 low-latitude support approximation；Appendix A 已补标准 cone-angle 小误差检查，完整 Sun-line cone-angle dynamics/stability rederivation 仍是后续修正项 |
| 质量预算计算 | 🟢 First pass complete | Codex | 已引入 source-backed 材料并完成 angle/utilization trade study |
| 热力学分析 | 🟡 Initial model complete | Codex | 1 AU 温度快照已跑通，仍需更细的系统热耦合 |
| 理想基准对比 | 🟢 First pass complete | Codex | 已完成与理想 Swarm / Ring 的纯上限比较 |
| 结构闭合 | 🟡 Supporting slice complete | Codex | 显式 boom/tether 几何模型已接入，并已补充 heritage gap 与 fixed-bus-budget 两组系统级 benchmark；仍未完成 engineering closure |
| 论文正文 | 🟡 Full first draft | Codex | canonical manuscript 已形成完整主线，当前定位为 theory-grounded framework paper with low-latitude illustrative analysis |
| 文献综述 | 🟡 Refresh absorbed | Codex | `docs/references/literature_review_refresh_20260427.md` 已记录 `dr` 结果、可用 citation clusters 与 rejected/deferred overclaims |
| 构建与发布 | 🟡 In progress | Codex | 本地 build 已验证；Zenodo 新快照、venue decision 与 external pre-read 仍待完成 |

## Key Decisions

| Date | Decision | Rationale |
|------|----------|-----------|
| 2026-03-23 | 采用更严格的低纬理想帆支撑关系替代 $\beta \approx \sin\phi$ 近似 | 对 1° 环，当前 screening relation 给出 $\beta_{\min} \approx 0.0453$，明显更严格 |
| 2026-03-23 | 采用微位移策略而非完全悬浮 | 即便用精确模型，1° 环仍远低于 $\beta \ge 1$ 的全悬浮门槛 |
| 2026-03-23 | 解耦推力/载荷模块 | 打破"反射-吸收"热力学死结 |
| 2026-03-23 | 论文范围收束为“理论框架 + 低纬示例” | 避免论文滑向未完成的重系统工程研究，主贡献保持为框架建立 |
| 2026-03-24 | 当前版本先定位 arXiv 发布，JBIS 作为后续更匹配的正式期刊方向 | 现阶段 manuscript 更像 framework-first / advanced concepts paper；先以 arXiv 固化叙事与引用，再视拓扑指标或非理想修正补强后评估 JBIS |
| 2026-03-25 | 在 novelty posture 中显式吸收 McInnes 2026 | 最新 prior art 已明确指出 Dyson swarm 可借 displaced NKO parallel stacking 缓解碰撞；当前贡献因此进一步收束为 bridge development、continuum framing 与 analytic criterion |
| 2026-04-23 | 将 local `r-\phi` 结果明确定义为 branch-specific dynamics contribution | 避免把本文表述成 displaced-orbit stability 的一般性重做，保持 claim boundary 与 prior art 一致 |
| 2026-04-23 | 论文控制面以 canonical manuscript 的实际结构为准，而不是反向要求正文匹配旧 outline | 减少 control-plane drift，让写作状态、build surface 与稿件现实保持一致 |
| 2026-04-27 | 将 `dr` deep-research 输出作为 triage 吸收到文献综述控制面 | `dr` 输出支持当前 novelty boundary，但包含二手来源和过强架构主张；可用部分已压缩为 citation clusters 和 future-work gaps |
| 2026-04-27 | 将 `\beta_{\min}` 与稳定性表述降格为 low-latitude support approximation | 审稿式检查指出当前 effective support pitch / cone-angle 口径与 full ideal-specular sail force law 可能不一致；正文保留低纬 screening value，但移除 high-latitude endpoint 和 exact-branch claim，并将主文符号改为 `\alpha_{\mathrm{eff}}` |
| 2026-04-27 | 用 Appendix A 锁定低纬 cone-angle 近似误差 | 标准 Sun-line cone-angle 检查显示主文 reduced screening curve 在 `0.1^\circ`、`0.5^\circ`、`1^\circ` 只保守高估所需 `\beta_{\min}` 约 `0.25%`、`1.24%`、`2.48%` |
| 2026-04-27 | 将 PV fill-factor 样例降格为 mass-budget illustration | `54.8 g/m^2` ultralight PV benchmark 已接到 Kim et al. (2021) device-level result；正文明确 support area 不等于 energy-collecting area，样例不构成 optical-power closure |

## Blockers

- 商业柔性 CIGS 模块面密度过高；若坚持 1° 以上位移，必须依赖更轻的薄膜 PV。
- 结构质量目前仍按最优/上界方式处理，下一步需把 tether/avionics/control margin 显式纳入。
- 在纯控制变量比较下，MDDS 不会在同效率条件下超过理想 Swarm / Ring；论文叙事必须把优势定位到轨道管理而非纯能量上限。
- 结构闭合初版显示节点粒度本身是关键变量：小功率节点会被固定结构质量严重惩罚。
- design map 进一步表明，多度数位移与高相对利用率不能同时轻易成立：对当前 `CP1 + ultralight tandem` 组合，2° 时 25% 理想同效率 Swarm 比值已不可达。
- flight-heritage benchmark 表明，当前真正的系统瓶颈已经不只是 sail membrane，而是整船 bus / deployment / control overhead；这要求后续结构闭合必须显式建模系统级固定质量。
- fixed-bus-budget 结果进一步表明，在给定 angle / power / utilization 时，允许的固定系统质量会迅速收紧到几公斤甚至亚公斤量级；这已经是明确的系统级 miniaturization 门槛。
- 本地 working manuscript 已领先于当前公开 Zenodo `v3` 快照；若要对外继续分发，需要先做一次新的 snapshot / release absorption。
- 完整 ideal-specular Sun-line cone-angle dynamics/stability rederivation 尚未完成；当前正文只应按 low-latitude screening framework 对外表述，Appendix A 仅作为核心低纬算例的 conservative error check。

## Next Milestone

**M3: arXiv-Ready Manuscript Freeze** — 完成 citation tightening、重新核验 build/export、并准备新的公开快照或 external pre-read 基线。

---

See [ROADMAP.md](./ROADMAP.md) for full timeline.
