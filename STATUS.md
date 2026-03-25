# Project Status

**Last Updated**: 2026-03-25

## Current Phase

**Phase 1: Mathematical Modeling (first slice completed)**

已完成第一轮可复现建模、材料代入和典型工况分析。

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
- [ ] 文献综述（继续扩展）

## Active Work

| Area | Status | Owner | Notes |
|------|--------|-------|-------|
| 轨道动力学模型 | 🟢 First pass complete | Codex | 精确理想帆方程已实现，1° 参考环受力、一阶扰动灵敏度与最优点局部解析稳定性已计算 |
| 质量预算计算 | 🟢 First pass complete | Codex | 已引入 source-backed 材料并完成 angle/utilization trade study |
| 热力学分析 | 🟡 Initial model complete | Codex | 1 AU 温度快照已跑通，仍需更细的系统热耦合 |
| 理想基准对比 | 🟢 First pass complete | Codex | 已完成与理想 Swarm / Ring 的纯上限比较 |
| 结构闭合 | 🟡 First scaling slice | Codex | 显式 boom/tether 几何模型已接入，并已补充 heritage gap 与 fixed-bus-budget 两组系统级 benchmark |
| 论文大纲 | 🟡 In progress | Codex | 已增加定量结果草稿，现已覆盖 orbit/mass/benchmark/stability/design-map 五块结果 |

## Key Decisions

| Date | Decision | Rationale |
|------|----------|-----------|
| 2026-03-23 | 采用精确理想帆受力模型替代 $\beta \approx \sin\phi$ 近似 | 对 1° 环，精确结果为 $\beta_{\min} \approx 0.0453$，明显更严格 |
| 2026-03-23 | 采用微位移策略而非完全悬浮 | 即便用精确模型，1° 环仍远低于 $\beta \ge 1$ 的全悬浮门槛 |
| 2026-03-23 | 解耦推力/载荷模块 | 打破"反射-吸收"热力学死结 |
| 2026-03-23 | 论文范围收束为“理论框架 + 低纬示例” | 避免论文滑向未完成的重系统工程研究，主贡献保持为框架建立 |
| 2026-03-24 | 当前版本先定位 arXiv 发布，JBIS 作为后续更匹配的正式期刊方向 | 现阶段 manuscript 更像 framework-first / advanced concepts paper；先以 arXiv 固化叙事与引用，再视拓扑指标或非理想修正补强后评估 JBIS |
| 2026-03-25 | 在 novelty posture 中显式吸收 McInnes 2026 | 最新 prior art 已明确指出 Dyson swarm 可借 displaced NKO parallel stacking 缓解碰撞；当前贡献因此进一步收束为 bridge development、continuum framing 与 analytic criterion |

## Blockers

- 商业柔性 CIGS 模块面密度过高；若坚持 1° 以上位移，必须依赖更轻的薄膜 PV。
- 结构质量目前仍按最优/上界方式处理，下一步需把 tether/avionics/control margin 显式纳入。
- 在纯控制变量比较下，MDDS 不会在同效率条件下超过理想 Swarm / Ring；论文叙事必须把优势定位到轨道管理而非纯能量上限。
- 结构闭合初版显示节点粒度本身是关键变量：小功率节点会被固定结构质量严重惩罚。
- design map 进一步表明，多度数位移与高相对利用率不能同时轻易成立：对当前 `CP1 + ultralight tandem` 组合，2° 时 25% 理想同效率 Swarm 比值已不可达。
- flight-heritage benchmark 表明，当前真正的系统瓶颈已经不只是 sail membrane，而是整船 bus / deployment / control overhead；这要求后续结构闭合必须显式建模系统级固定质量。
- fixed-bus-budget 结果进一步表明，在给定 angle / power / utilization 时，允许的固定系统质量会迅速收紧到几公斤甚至亚公斤量级；这已经是明确的系统级 miniaturization 门槛。

## Next Milestone

**M2: Manuscript Framing and Low-Latitude Main Text** — 将论文正文收束为 `\beta_{\min}(\phi)` / `\sigma_{\max}(\phi)` 框架、`0.5^\circ`/`1^\circ`/`2^\circ` 示例与同步分支说明，把更深的结构/控制/稳定性分析降到 supporting work。

---

See [ROADMAP.md](./ROADMAP.md) for full timeline.
