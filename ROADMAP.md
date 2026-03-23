# Research Roadmap

**Target Output**: Academic paper on Micro-Displaced Dyson Swarm (MDDS) architecture

---

## Phase 0: Foundation (Current)

**目标**: 建立研究基础设施和理论框架

- [ ] 项目结构搭建
- [ ] 核心概念文档化
- [ ] 文献综述（McInnes displaced orbits, Dyson sphere concepts）
- [ ] 定义关键参数和符号系统

**产出**: 完整的项目框架，清晰的研究问题定义

---

## Phase 1: Mathematical Modeling

**目标**: 建立完整的数学模型

### 1.1 轨道动力学 (Orbital Dynamics)

- [ ] Displaced orbit 基础方程推导
- [ ] $\beta$-$\phi$ 关系的精确表达式
- [ ] 轨道稳定性分析（线性化扰动）
- [ ] 多环系统的相互作用

### 1.2 质量预算 (Mass Budget)

- [ ] 材料参数数据库
  - 反射膜：Kapton, CP1, 铝化聚酰亚胺
  - 太阳能板：薄膜 PV, 柔性砷化镓
  - 结构支撑：碳纤维桁架
- [ ] 系统 $\beta$ 计算模型
- [ ] 优化：镜面积/板面积比例

### 1.3 热力学分析 (Thermal Analysis)

- [ ] 反射膜热平衡（低吸收率情况）
- [ ] 载荷舱热平衡（吸收-辐射平衡）
- [ ] 解耦架构的热学优势量化

**产出**: 完整的数学模型代码库，参数灵敏度分析

---

## Phase 2: Feasibility Analysis

**目标**: 验证工程可行性

- [ ] 设计空间探索（Design Space Exploration）
- [ ] 与现有材料技术的对标
- [ ] 识别技术瓶颈和研究缺口
- [ ] 与传统方案的定量比较

**产出**: 可行性报告，关键参数范围

---

## Phase 3: Paper Writing

**目标**: 产出学术论文

### 论文结构（暂定）

1. **Introduction**
   - Keplerian deadlock problem
   - Limitations of existing solutions
   - Our contribution

2. **Theoretical Framework**
   - Displaced orbit theory (McInnes)
   - Lightness number and critical density

3. **Micro-Displacement Strategy**
   - Why small $\beta$ is sufficient
   - Decoupled architecture design

4. **Mathematical Model**
   - Orbital dynamics equations
   - Stability analysis

5. **Engineering Feasibility**
   - Mass budget with real materials
   - Thermal analysis
   - Comparison with alternatives

6. **Discussion**
   - Scalability
   - Technology readiness
   - Future work

7. **Conclusion**

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
