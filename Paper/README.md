# Paper: Micro-Displaced Dyson Swarm

**Working Title**: Orbital Dynamics and Engineering Feasibility of Micro-Displaced Dyson Swarm Nodes using Decoupled Solar Sail Architectures

---

## Paper Control Plane

此文档是论文写作的控制中心。

### Current Status

**Stage**: Outline Development

| Section | Status | Notes |
|---------|--------|-------|
| Abstract | 🟡 Draft | 见 README.md |
| 1. Introduction | 🔴 Not started | |
| 2. Theoretical Framework | 🔴 Not started | McInnes displaced orbits |
| 3. Core Innovation | 🔴 Not started | 解耦架构、微位移策略 |
| 4. Mathematical Model | 🔴 Not started | 依赖 `models/` |
| 5. Feasibility Analysis | 🔴 Not started | 依赖 Phase 2 |
| 6. Discussion | 🔴 Not started | |
| 7. Conclusion | 🔴 Not started | |

---

## Outline

### 1. Introduction

**目标**: 建立问题的重要性和现有方案的不足

1.1 The Dyson Swarm Concept
- 戴森球作为 Type II 文明标志
- 戴森群（Swarm）vs 戴森壳（Shell）vs 戴森泡（Bubble）

1.2 The Keplerian Deadlock
- 所有开普勒轨道必须过质心 → 大圆轨迹
- 同高度多节点必然产生轨道交点
- 碰撞风险与 Kessler 灾难

1.3 Limitations of Existing Approaches
- Co-orbital phase separation: 微扰不稳定
- Nested rings: 遮挡与热串扰
- Full levitation (Dyson Bubble): 材料不可行

1.4 Our Contribution
- 微位移策略：小 $\beta$ 实现大分离
- 解耦架构：打破反射-吸收死结

### 2. Theoretical Framework: Displaced Orbits

**目标**: 建立理论基础

2.1 Solar Radiation Pressure
- 光压基本原理
- 临界面密度 $\sigma^*$

2.2 Lightness Number $\beta$
$$\beta = \frac{F_{\text{rad}}}{F_{\text{grav}}} = \frac{\sigma^*}{\sigma}$$

2.3 Non-Keplerian Displaced Orbits (McInnes)
- 圆形位移轨道方程
- $\beta$-$\phi$ 关系

2.4 Stability Considerations
- 径向稳定性
- 轴向稳定性

### 3. Core Innovation: Micro-Displacement with Decoupled Architecture

**目标**: 阐述核心创新

3.1 Why Full Levitation Fails
- $\beta \ge 1$ 要求 $\sigma < 1.53$ g/m²
- 无法携带有意义的载荷

3.2 The Micro-Displacement Insight
- 小角度 $\phi \sim 1°$ 只需 $\beta \sim 0.017$
- 1 AU 处物理分离达数百万公里
- 完全消除轨道交点

3.3 Decoupled Architecture
- 推力模块（反射）与载荷模块（吸收）分离
- 热力学解耦
- 系统 $\beta$ 计算

### 4. Mathematical Model

**目标**: 提供定量分析

4.1 Orbital Dynamics
- 位移轨道精确方程
- 多环配置

4.2 Mass Budget Model
- 材料参数
- 最优面积比

4.3 Thermal Model
- 反射膜热平衡
- 载荷舱热平衡

### 5. Engineering Feasibility

**目标**: 验证可行性

5.1 Design Space Exploration
- 参数灵敏度分析
- 可行设计窗口

5.2 Material Requirements
- 与现有技术对标
- 近期 vs 远期材料

5.3 Comparison with Alternatives
- vs 传统戴森群
- vs 戴森泡
- 定量优势

### 6. Discussion

6.1 Scalability
- 从单环到全球覆盖

6.2 Practical Considerations
- 部署策略
- 维护与冗余

6.3 Limitations and Future Work

### 7. Conclusion

---

## Directory Structure

```
Paper/
├── README.md           # This file (control plane)
├── drafts/             # Working drafts
│   └── outline.md      # Detailed outline
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
| Fig 1 | Keplerian deadlock illustration | 🔴 |
| Fig 2 | Micro-displaced parallel rings concept | 🔴 |
| Fig 3 | Decoupled architecture schematic | 🔴 |
| Fig 4 | $\beta$-$\phi$ relationship curve | 🔴 |
| Fig 5 | Design space / feasibility region | 🔴 |
| Fig 6 | Mass budget breakdown | 🔴 |

---

## Target Venues (TBD)

- *Acta Astronautica*
- *Journal of Spacecraft and Rockets*
- *Advances in Space Research*
- *arXiv* (astro-ph.EP or astro-ph.IM)

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
