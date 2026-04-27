# Research Roadmap

**Target Output**: Academic paper on Micro-Displaced Dyson Swarm (MDDS) architecture

---

## Phase 0: Foundation

**目标**: 建立研究基础设施和理论框架

- [x] 项目结构搭建
- [x] 核心概念文档化
- [ ] 文献综述（McInnes displaced orbits, Dyson sphere concepts）
- [x] 定义关键参数和符号系统

**产出**: 完整的项目框架，清晰的研究问题定义

---

## Phase 1: Mathematical Modeling (first slice completed; continuing as supporting work)

**目标**: 建立完整的数学模型

### 1.1 轨道动力学 (Orbital Dynamics)

- [x] Displaced orbit 基础方程推导
- [x] low-latitude $\beta$-$\phi$ screening relation
- [x] 一阶扰动灵敏度切片（锥角误差 / $\beta$ 误差 / 小外压扰动）
- [x] 最优锥角附近的解析局部响应
- [x] reduced low-latitude branch 的局部 `r-\phi` 线性化
- [x] standard Sun-line cone-angle low-latitude error check（Appendix A）
- [ ] full ideal-specular Sun-line cone-angle force-law rederivation
- [ ] passive / closed-loop stability closure
- [ ] 更一般的 stability map（超出 reduced low-latitude branch）
- [ ] 多环系统的相互作用

### 1.2 质量预算 (Mass Budget)

- [x] 材料参数数据库
  - 反射膜：Kapton, CP1, 铝化聚酰亚胺
  - 太阳能板：薄膜 PV, 柔性砷化镓
  - 结构支撑：碳纤维桁架
- [x] 系统 $\beta$ 计算模型
- [x] 优化：镜面积/板面积比例
- [x] 结构闭合尺度律初版（boom/tether/fixed-mass scaling）
- [ ] 结构线密度与固定质量项替换为 source-backed engineering values

### 1.3 热力学分析 (Thermal Analysis)

- [x] 反射膜热平衡（低吸收率情况）
- [x] 载荷舱热平衡（吸收-辐射平衡）
- [ ] 解耦架构的热学优势量化

**产出**: 完整的数学模型代码库，参数灵敏度分析

---

## Phase 2: Feasibility Analysis

**目标**: 验证工程可行性

- [x] 设计空间探索（Design Space Exploration）
- [x] 与现有材料技术的对标
- [x] 识别技术瓶颈和研究缺口
- [x] 与传统方案的定量比较
- [x] Flight-heritage 系统差距 benchmark（ACS3 / NEA Scout）
- [x] 固定 bus 质量阈值 benchmark（ACS3 heritage lines）

**产出**: 可行性报告，关键参数范围

---

## Phase 3: Paper Writing (Current Focus)

**目标**: 产出学术论文

### 当前 canonical manuscript 结构

1. **Introduction**
   - topology-and-growth pressure in dense same-shell Keplerian builds
   - prior-art bridge and claim boundary
   - continuum / analytic-screening contribution

2. **Theoretical Framework**
   - force balance and support variables
   - low-latitude optimized branch
   - support continuum
   - synchronization-constrained branch
   - local radial-latitude dynamics

3. **Illustrative Slices of the Low-Latitude Branch**
   - representative latitudes
   - entry-level interpretation
   - screening-level engineering bookkeeping
   - synchronization slice

4. **Discussion**
   - growth path and deployment logic
   - modeling boundaries
   - next-step realism layers

5. **Conclusion**

### 当前写作进度

- [x] canonical manuscript content surface 建立到 `Paper/content/manuscript.md`
- [x] MNRAS template/build wrapper 可生成 PDF
- [x] abstract、正文主干与结论 first draft 已成型
- [x] 关键 figures 已生成并接入 build
- [x] literature review refresh
- [ ] citation tightening
- [ ] arXiv release package / Zenodo 新快照
- [ ] external pre-read / venue decision

**产出**: 可投稿的学术论文

---

## Phase 4: Submission & Iteration

- [ ] 目标期刊/会议选择
- [ ] 同行预审
- [ ] 投稿与修订

---

## Timeline (Tentative)

| Phase | Duration | Target Completion |
|-------|----------|-------------------|
| Phase 0 | 1 week | 2026-03-30 |
| Phase 1 | 3-4 weeks | 2026-04-30 |
| Phase 2 | 2 weeks | 2026-05-15 |
| Phase 3 | 4 weeks | 2026-06-15 |
| Phase 4 | TBD | — |

---

## Success Criteria

1. **理论完备性**: 数学模型自洽，覆盖轨道、热力学、质量预算
2. **工程可信度**: 参数基于真实材料数据，非理想化假设
3. **创新性**: 明确区分于 Dyson Bubble 和传统 Swarm 的贡献
4. **可复现性**: 所有计算代码和数据可追溯
5. **主张边界清晰**: continuum / architecture contribution 与 prior art、supporting evidence、future work 明确分层
