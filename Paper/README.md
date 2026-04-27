# Paper: Micro-Displaced Dyson Swarm

**Working Title**: From Keplerian Swarms to Radiatively Supported Bubbles: A Continuum Framework for Dyson Architectures

---

## Paper Control Plane

此文档是论文写作的控制中心。

### Current Status

**Stage**: Manuscript Consolidation, Literature Review Refresh, and Build Verification

**Latest shift**: after force-model review, the manuscript no longer presents the current `\beta_{\min}` curve as a full high-latitude exact ideal-specular sail branch. It is now explicitly framed as a low-latitude ideal-specular support approximation / screening relation. The old `\nu=0`, `\phi_c`, and `\beta=1.5` endpoint interpretation has been removed from the canonical manuscript; local `r-\phi` dynamics are now described only as bounded response for the same reduced low-latitude model.

**Build state**: the local MNRAS build currently succeeds for both PDF and HTML. The working tree is ahead of the latest public Zenodo snapshot (`v3`), so the next public release should be treated as a new post-`v3` draft rather than a rebuild of the archived version.

**Literature-review state**: `dr` deep-research results have been absorbed into `docs/references/literature_review_refresh_20260427.md`. The usable result is a prior-art boundary map and citation-cluster guide; several stronger `dr` suggestions were explicitly rejected or deferred because they would overclaim the current manuscript.

### Public Draft Record (Zenodo)

Versioned public manuscript snapshots are now archived on Zenodo. Current latest public snapshot: `v3`.

| Version | DOI | Date | Notes |
|---------|-----|------|-------|
| v3 | [10.5281/zenodo.19298178](https://doi.org/10.5281/zenodo.19298178) | 2026-03-28 | 当前最新公开快照 |
| v2 | [10.5281/zenodo.19226004](https://doi.org/10.5281/zenodo.19226004) | 2026-03-25 | 中间公开修订版 |
| v0.1 | [10.5281/zenodo.19224636](https://doi.org/10.5281/zenodo.19224636) | 2026-03-25 | 首个公开快照 |

| Section | Status | Notes |
|---------|--------|-------|
| Abstract | 🟡 Draft in metadata | canonical abstract 位于 `template/metadata.yaml` |
| Introduction | 🟡 Full first draft | canonical source 为 `content/manuscript.md` |
| Theoretical Framework | 🟡 Full first draft | canonical source 为 `content/manuscript.md` |
| Illustrative Low-Latitude Slices | 🟡 Full first draft | canonical source 为 `content/manuscript.md` |
| Discussion | 🟡 Full first draft | canonical source 为 `content/manuscript.md` |
| Conclusion | 🟡 Full first draft | canonical source 为 `content/manuscript.md` |

### Current Writing Surface

- canonical build manuscript 现已上提到 `Paper/content/manuscript.md`
- `Paper/drafts/manuscript_draft.md` 保留为较自由的 prose / note surface，而不是模板内正文源
- abstract 与投稿元数据的 canonical source 为 `Paper/template/metadata.yaml`
- 对外联系草稿现集中保存在 `Paper/drafts/`，包括 `mcinnes_cold_email.md`、`wright_cold_email.md`、`quarta_cold_email.md`、`heiligers_cold_email.md` 与 `friend_forward_packet.md`；各 cold-email draft 现记录公开邮箱、联系理由以及其与 manuscript 的关系
- 核心参考文献 canonical source 为 `Paper/references/bibliography.bib`
- 当前文献综述 refresh surface 为 `docs/references/literature_review_refresh_20260427.md`
- 最小 `main.tex` 已补齐于 `Paper/main.tex`
- 图像生成脚本已落地于 `Paper/figures/generate_figures.py`
- 当前结构已显式分离为：`Paper/content/` 管正文，`Paper/template/` 管唯一保留的 MNRAS build/template 资产，`Paper/output/` 管构建产物

### Canonical Manuscript Structure

当前 canonical manuscript 的实际主结构是：

1. `Introduction`
2. `Theoretical Framework`
3. `Illustrative Slices of the Low-Latitude Branch`
4. `Discussion`
5. `Conclusion`

这意味着 control plane 不应再假设 “Architecture Reframing” 必须作为独立一级标题存在于 canonical manuscript 中。当前正文里，这部分内容主要被吸收到：

- `Introduction` 中的 claim boundary / continuum framing
- `Discussion` 中的 growth path、design language 与 modeling boundary

若后续为投稿或审稿需要重新拆出独立一级节，可以再做结构性回退；在那之前，应以当前 canonical manuscript 的实际组织为准，避免 control-plane drift。

### Paper Positioning

本文定位现已明确收束为：

- **主贡献**：建立 MDDS 的高层理论框架，把问题压缩为 `\beta_{\min}(\phi)`、`\sigma_{\max}(\phi)` 与 `\sigma_{\text{sys}}` 的交点判据。
- **示例验证**：只在低纬区间做轻量但定量的展开，证明该框架不是空的。
- **不做的事**：不把正文写成完整系统工程论文，不在正文里追求 exhaustive 的结构闭合、固定 bus 预算、全面 design map 或控制系统论证。

因此，本文最稳的口径是：

> **A theory-grounded framework paper with low-latitude illustrative feasibility analysis.**

在 recent prior-art review 之后，这个定位进一步收紧为：

- **不是**新的太阳帆轨道家族论文
- **不是**新的 Earth-synchronous displaced-orbit family 论文
- **而是**把已知低纬 DNKO / statite / displaced-orbit 理论，重组为一个面向分层 Dyson Swarm 设计的解析架构判据

更具体地说，当前 manuscript 的主贡献已经收束成三层，而且第一层现在是正文主轴：

- **Continuum 层面**：本文主张 Dyson architectures 更应被理解为一条连续的 support spectrum，而不是完全离散的 shell / swarm / bubble taxonomy。
- **架构层面**：MDDS 是这条连续谱中的低-`\beta` 微位移工作段，提供了一条相对于传统纯开普勒 Dyson Swarm 更易组织的渐进式替代路线，通过光压辅助的纬度分层降低轨道拓扑复杂度，并把问题从固定参数开普勒巨型星座的 intersection management，转写为 layered support geometry。
- **物理层面**：地日环境下存在一个非空的小角度工作区间，在这个区间内，微小角位移已经能带来巨大的离面部署平面，而对应的纯面密度门槛在入口级角度上已接近或进入现有人类轻量航天系统能力范围。

同时，latest prior-art update 现在已经明确指出一个必须写进正文的边界：

- **McInnes 2026 已明确占住桥接命题**：Dyson swarm 的碰撞可原则上通过 displaced non-Keplerian orbit families 来缓解，因为轨道面可以做 parallel stacking，而不是继续保持 mutually inclined 的相交结构。
- 因此，本文**不再把“这座桥是否存在”当作 novelty**；真正保得住的贡献，是把这条已经被点出的桥发展成 `Dyson support continuum + analytic screening criterion + staged-growth architecture language`。

当前写作策略也已相应调整：

- 低纬 `\theta_\oplus / 0.1^\circ / 0.5^\circ / 1^\circ` 例子保留，但只作为 supporting slices
- 正文重心回到 `Dyson support continuum` 这一主张
- 引言与讨论现已把 dense same-shell Keplerian swarm 收束为 `topology-and-growth pressure`，并把 `Walker-like / phase-separated / radial nesting` 方案定位为可缓解或移出同壳情形、但不能消除 dense same-radius multi-plane subset 的底层节点交叉结构
- `β`、`φ`、`ν`、`\sigma_{\max}(\phi)` 被反复用作 continuum 的参数化语言，而不只是局部算例变量
- `low-latitude` 部分的职责被明确限制为：证明该 continuum 中的低-`\beta` 工作段非空，而不是承载全文的主 novelty

当前 safest one-sentence claim 为：

> **The novelty is not the displaced orbit family itself, but the use of the low-latitude displaced branch as a Dyson-swarm architecture screening relation linking latitude, lightness number, and system areal density.**

### Core Results For Main Text

- 主支撑曲线现在明确为 reduced low-latitude screening relation：$\beta_{\min}(\phi)=\frac{3\sqrt3}{2}\sin\phi$，而不是 full high-latitude exact ideal-sail branch。
- 1 AU, $\phi = 1^\circ$ 的低纬支撑近似给出 $\beta_{\min} \approx 0.0453$，比早期启发式 $\sim 0.017$ 更严格。
- 对应总面密度上限约为 $33.8\ \text{g/m}^2$。
- 入口级低纬示例现已明确加入：在 `0.1^\circ` 时，$\beta_{\min} \approx 0.00453$、$\sigma_{\max} \approx 337.4\ \text{g/m}^2$，这说明最靠近 reference orbital plane 的微位移窗口在纯面密度意义上已经相当宽裕。
- 一个更直观的入口级特征角也已纳入正文：取从太阳看地球角半径 $\theta_\oplus \approx 0.00244^\circ$，则有 $\beta_{\min}(\theta_\oplus) \approx 1.11\times 10^{-4}$、$\sigma_{\max}(\theta_\oplus) \approx 13.83\ \text{kg/m}^2$。这说明在纯面密度意义上，MDDS 框架已经进入了一个明显落在人类现有轻量航天系统能力范围内的近入口区间。
- 该点现在不再只是旁注，而是正式并入代表性例子：在 1 AU 上它对应约一个地球半径的法向分离，$z \approx 6{,}371\ \text{km}$；若施加 Earth-synchronous 约束，对应 inward shift 约 `3000 km`。
- 低纬主结果现已收束为 `0.1^\circ`、`0.5^\circ`、`1^\circ` 三个正文代表点：用于展示从“极宽松入口”到“仍有意义但已明显收紧”的低纬窗口；`2^\circ` 保留为对照点，说明窗口会继续快速缩窄。
- 正文现已把标准 ideal-specular cone angle 定义与当前 reduced support pitch 区分开来：当前主文变量已改为 `\alpha_{\mathrm{eff}}`，表示低纬柱坐标支撑近似中的 effective support pitch，不再声称是完整 Sun-line cone-angle force law。
- 新增 Appendix A，用标准 Sun-line cone-angle force law 检查主文低纬 screening curve；在 `0.1^\circ / 0.5^\circ / 1^\circ` 三个核心例子中，主文公式分别只保守高估 $\beta_{\min}$ 约 `0.25% / 1.24% / 2.48%`。
- 正文现已补入 reduced low-latitude model 的一阶局部 `r-\phi` 线性化：在定义 `q=r_0\delta\phi` 与 `y=r_0\cos\phi_0\,\psi` 后，可得到耦合扰动方程与特征二次式 `u^2+[1+\nu^2(1+2\sin^2\phi_0)]u+\nu^2\cos^2\phi_0=0`（其中 `u=\lambda^2/n^2`）。该结果只说明 retained low-latitude domain 中 `r-\phi` 子系统振荡有界，而 along-track phase mode 仍是中性模态。
- McInnes 2026 的 extended-reflector 稳定性结果现在只作为 neighboring idealized models 的 consistency check，不再写成 favorable screen 或稳定上限。
- 当前正文的主建模边界也已明确：主推导采用低纬理想镜面支撑近似，并把 reflector 视为唯一显式承受并利用光压的支撑表面；payload（例如太阳能电池板）造成的额外光压、热再辐射与受力偏移未进入主方程，只在 $\sigma_{\text{sys}}$ 中作为总质量预算处理。正文现在进一步强调 support area 不等于 energy-collecting area，PV fill-factor 只是 mass-budget illustration，不是 closed optical-power architecture。
- `54.8 g/m^2` ultralight PV benchmark 现在明确接到 Kim et al. (2021) device-level flexible InGaP/GaAs tandem-cell result：`27.4%` efficiency 与 `>5000 W/kg` specific power under AM1.5G；正文同时声明它不是 space-qualified module loading，未含 wiring / deployment / interconnect / thermal / radiation margin。
- current prior-art map 已明确表明：Earth-synchronous / period-constrained branch 在现有 DNKO 文献中已有成熟先例，因此正文中只把它当作 framework 内的 illustrative operational variant，不再当作独立 novelty claim。
- McInnes 2026 进一步表明：`Dyson-swarm collision relief -> displaced NKO parallel stacking` 这条主桥本身也已被显式说出，因此正文 novelty posture 现已进一步收紧为 `bridge development` 而不是 `bridge discovery`。
- 高层理论主线现已单独记录：MDDS 可以被统一表述为“纬度支撑曲线 $\beta_{\min}(\phi)$ / $\sigma_{\max}(\phi)$ 与系统面密度 $\sigma_{\text{sys}}$ 的交点问题”，详见 `Paper/drafts/high_level_derivation.md`。
- 更高层的概念定位也已收紧：MDDS 可被解释为连接“平面开普勒 swarm 极限”和“辐射支撑 statite / bubble 端点”的构型连续体，而本文当前严格分析的是其中低纬、低-$\beta$、可工程化的 displaced-orbit 分支。
- 理论框架下的两类自然设计方向也已明确：一类是通过最小化 $\beta$ 来最大化质量裕度的 low-latitude optimized branch，另一类是通过施加外部周期条件来保持运行规则性的 synchronization-constrained branch。
- 渐进部署思想也已纳入主叙事：MDDS 不只是一个最终构型，还可以被表述为一条从 reference orbital plane 附近开始、每一步都可运营、再逐步向更高纬扩张的 Dyson-progressive growth path。

### Supporting Results (Appendix / Future Work)

以下结果保留为 supporting evidence，但不再视为正文主线：

- 理想 Dyson Swarm / Dyson Ring 纯能量 benchmark
- 结构闭合尺度律、design map、fixed bus budget
- ACS3 / NEA Scout flight-heritage gap benchmark
- 扰动灵敏度切片与局部解析稳定性结果
- 更细的 thermal / control / deployment 系统分析
- 结果草稿见 `Paper/drafts/quantitative_findings.md`，可复现实验见 `experiments/runs/20260323_mdds_feasibility/`。
  以及 `experiments/runs/20260323_ideal_architecture_comparison/`。
  以及 `experiments/runs/20260323_structural_closure/`。
  以及 `experiments/runs/20260323_perturbation_sensitivity/`。
  以及 `experiments/runs/20260323_linearized_stability/`。
  以及 `experiments/runs/20260323_structural_design_map/`。
  以及 `experiments/runs/20260323_flight_heritage_gap/`。
  以及 `experiments/runs/20260323_fixed_bus_budget/`。

---

## Outline

### 1. Introduction

**目标**: 先说清楚问题，再说清楚 prior-art boundary 与本文新增内容

1.1 Dyson Swarms as a Topology-and-Growth Problem
- 所有开普勒轨道必须过中心体
- 同半径多倾角轨道天然生成 node-crossing graph
- 问题不只是碰撞，而是 growth path 的几何病理

1.2 The Prior-Art Bridge and Its Boundary
- DNKO / statite / displaced-orbit 理论链已经成熟
- McInnes 2026 已明确指出 Dyson swarm 可借 displaced NKO parallel stacking 缓解碰撞
- 因此本文不能再把“桥是否存在”作为 novelty

1.3 What This Paper Adds
- 把 bridge 发展成 support continuum
- 把架构问题压缩为 `\beta_{\min}(\phi)` / `\sigma_{\max}(\phi)` / `\sigma_{\text{sys}}`
- 把问题从 intersection management 改写为 layered support geometry

1.4 Claim Boundary and Roadmap
- 明确不主张 orbit-family discovery
- 明确不做完整系统工程 closure
- 提前说明后文结构：framework -> architecture consequences -> illustrative slices -> boundaries

### 2. Analytic Support Framework

**目标**: 建立全文真正承重的解析骨架

2.1 Geometry, Kinematics, and Force Balance
- 圆形位移轨道几何
- 轨道支撑与辐射支撑的分解
- 明确 current force model 是 low-latitude support approximation，而不是完整 high-latitude ideal-sail force law

2.2 Payload-Optimized Branch
- 低纬支撑近似下的 optimized effective support pitch `\alpha_{\mathrm{eff,opt}}`
- `\beta_{\min}(\phi)` 与 `\sigma_{\max}(\phi)`
- 把轨道问题转写为 screening criterion

2.3 Dyson Support Continuum
- Keplerian swarm 极限
- low-`\beta` MDDS 工作段
- bubble / statite access threshold 与 low-latitude model validity boundary 的区分

2.4 Synchronization-Constrained Branch
- Earth-synchronous / period-constrained slice
- 作为同一 framework 的 operational variant

2.5 Local Radial-Latitude Dynamics
- reduced low-latitude branch 的 `r / \phi` 线性化
- bounded oscillatory `r-\phi` subspace vs neutral along-track mode within the approximation
- `\delta\beta/\beta \sim \cot\phi\,\delta\phi` 与 `\delta\omega/\omega = -\tfrac32 \delta r/r`

2.6 Scope of the Main-Text Model
- 理想镜面边界
- payload 只作为面密度预算进入

### 3. Architecture Reframing and Design Consequences

**目标**: 在算例之前先把论文真正的主贡献讲清楚

3.1 Architecture Reframing
- novelty 在于 bridge development，不在 bridge discovery
- 从 nodal-intersection management 转向 layered support geometry

3.2 From End-State Taxonomy to Design Space
- shell / swarm / bubble 改写为同一 support space 的不同区域
- growth path 与 transition threshold 变成一等理论对象

3.3 Growth Path and Deployment Logic
- 低纬起步、逐步拓纬的 progressive architecture
- 后续可自然引出 traffic-style metrics

3.4 Observational Implications
- developing Dyson systems 更像 stratified circumstellar disk
- technosignature implication 作为 framework-generated hypothesis

### 4. Low-Latitude Illustrative Analysis

**目标**: 只证明 framework 非空，不承载主 novelty

4.1 Representative Latitudes
- `\theta_\oplus`
- `0.1^\circ`
- `0.5^\circ`
- `1.0^\circ`

4.2 Entry-Level Interpretation
- Earth-angle 作为近入口特征角
- 微小角位移即可换来巨大法向分离

4.3 Order-of-Magnitude Engineering Slices
- 轻量 reflector + PV bookkeeping
- 只做 screening-level 说明

4.4 Synchronization Slice
- 同步约束改变半径
- 不改变 support curve 本身

4.5 What the Slices Show
- 只证明 low-`\beta` window 非空且快速收紧

### 5. Boundaries and Next Steps

**目标**: 把 claim boundary 单独放出来，而不是混在主论证里

5.1 Modeling Boundaries
- 非理想光学
- 稳定性 / 控制闭合

5.2 Deferred Engineering Questions
- 结构闭合
- fixed bus / deployment / control mass
- 更完整 thermal / control / traffic analysis

### 6. Conclusion

---

## Directory Structure

```
Paper/
├── README.md           # This file (control plane)
├── drafts/             # Working drafts
│   ├── outline.md      # Detailed outline
│   ├── high_level_derivation.md  # High-level theoretical derivation
│   ├── mcinnes_cold_email.md     # Cold email draft for arXiv endorsement
│   ├── quantitative_findings.md  # Supporting quantitative notes
│   └── manuscript_draft.md       # Main-text draft in progress
├── figures/            # Diagrams and plots
│   ├── concept/        # Conceptual diagrams
│   └── results/        # Computational results
├── references/         # Source materials
│   └── bibliography.bib
└── main.tex            # Final manuscript (when ready)
```

---

## Key Figures Needed

| Figure | Description | Status |
|--------|-------------|--------|
| Fig 1 | Keplerian deadlock illustration | 🟢 Generated |
| Fig 2 | MDDS local force-balance schematic | 🟢 Generated |
| Fig 3 | Micro-displaced parallel rings concept | 🟢 Generated |
| Fig 4 | $\beta$-$\phi$ / $\sigma_{\max}(\phi)$ low-latitude support curves | 🟢 Generated |
| Fig 5 | Low-latitude illustrative window (`0.1°`, `0.5°`, `1°`) | 🟢 Generated |
| Fig 6 | Earth-synchronous radius shift schematic | 🟢 Generated |
| Deferred | Full support continuum with exact Sun-line cone-angle geometry | 🔴 Needs rederivation before use |

---

## Target Venues

- **Current release target**: *arXiv* (`astro-ph.EP` or `astro-ph.IM`) for the present framework-first version
- **Best-fit journal direction after another strengthening pass**: *JBIS* (*Journal of the British Interplanetary Society*), especially if the paper continues to position itself as an advanced concepts / architecture paper
- **Longer-shot / more conventional alternatives**: *Acta Astronautica*, *Journal of Spacecraft and Rockets*, *Advances in Space Research*

---

## References (Core)

1. Dyson, F. J. (1960). Search for Artificial Stellar Sources of Infrared Radiation.
2. McInnes, C. R. (1999). Solar Sailing: Technology, Dynamics and Mission Applications.
3. McInnes, C. R. & Simmons, J. F. L. (1992). Solar sail halo orbits.
4. Forward, R. L. (1984). Roundtrip Interstellar Travel Using Laser-Pushed Lightsails.

---

## Writing Guidelines

- 使用第一人称复数（we propose, we show）
- 数学符号与 `models/README.md` 保持一致
- 图表需自解释（caption 完整）
- 每个 claim 需有支撑（方程、引用、或计算结果）
