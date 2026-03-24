# Mathematical Models

本目录包含 MDDS (Micro-Displaced Dyson Swarm) 项目的数学模型。

高层理论主线的详细文字推导见
`Paper/drafts/high_level_derivation.md`。本文件更偏“符号与模型接口”，而不是完整叙述。

---

## Symbol Definitions (Canonical)

此处是项目范围内符号的**单一权威定义**。论文、代码、文档均应引用此处。

### Physical Constants

| Symbol | Name | Value | Unit |
|--------|------|-------|------|
| $c$ | Speed of light | $2.998 \times 10^8$ | m/s |
| $G$ | Gravitational constant | $6.674 \times 10^{-11}$ | m³/(kg·s²) |
| $L_\odot$ | Solar luminosity | $3.828 \times 10^{26}$ | W |
| $M_\odot$ | Solar mass | $1.989 \times 10^{30}$ | kg |
| $\text{AU}$ | Astronomical unit | $1.496 \times 10^{11}$ | m |

### Derived Constants

| Symbol | Name | Expression | Value | Unit |
|--------|------|------------|-------|------|
| $\sigma^*$ | Critical areal density | $\frac{L_\odot}{2\pi c G M_\odot}$ | 1.53 | g/m² |
| $P_0$ | Solar radiation pressure at 1 AU | $\frac{L_\odot}{4\pi c \cdot \text{AU}^2}$ | $4.56 \times 10^{-6}$ | Pa |

### System Parameters

| Symbol | Name | Definition | Typical Range | Unit |
|--------|------|------------|---------------|------|
| $\beta$ | Lightness number | $F_{\text{rad}}/F_{\text{grav}} = \sigma^*/\sigma$ | 0.04–0.25 | — |
| $\sigma$ | System areal density | $m_{\text{total}}/A_{\text{reflector}}$ | 5–150 | g/m² |
| $\phi$ | Displacement angle | Ring latitude above/below the ecliptic | 0.25°–5° | deg |
| $\alpha$ | Sail cone angle | Angle between Sun-line and sail normal | 35.26° optimal on low-$\beta$ branch | deg |
| $\nu$ | Orbital-rate ratio | $\omega/\sqrt{\mu/r^3}$ | 0–1 | — |
| $\lambda$ | PV fill factor | $A_p/A_r$ | 0–1 for shell-area comparisons | — |

### Geometry

| Symbol | Name | Definition |
|--------|------|------------|
| $A_r$ | Reflector area | Total reflective sail area |
| $A_p$ | Payload area | PV active area |
| $d$ | Vertical displacement | $r \sin\phi$ |

### Mass Components

| Symbol | Name | Notes |
|--------|------|-------|
| $m_{\text{total}}$ | Total system mass | $m_r + m_p + m_s$ |
| $m_r$ | Reflector mass | Sail membrane or subsystem |
| $m_p$ | Payload mass | PV cells and payload hardware |
| $m_s$ | Structure mass | Booms, tethers, deployment and control hardware |
| $\sigma_r$ | Reflector areal density | $m_r / A_r$ |
| $\sigma_p$ | PV areal density | $m_p / A_p$ |

---

## Model Modules

### 1. Orbital Dynamics (`orbital/`)

位移轨道的动力学模型，采用理想镜面反射帆的精确受力平衡。

**Core equations**:

对固定半径 $r$、固定位移角 $\phi$ 的圆形轨道，定义 $\nu = \omega/\sqrt{\mu/r^3}$，则

$$\beta \cos^3\alpha = \cos\phi(1-\nu^2)$$
$$\beta \cos^2\alpha \sin\alpha = \sin\phi$$

在低-$\beta$ 最优分支上：

$$\alpha_{\text{opt}} = \arctan\left(\frac{1}{\sqrt{2}}\right) \approx 35.26^\circ$$
$$\beta_{\min} = \frac{3\sqrt{3}}{2}\sin\phi$$
$$\nu^2 = 1 - \sqrt{2}\tan\phi$$

这意味着 1 AU, $\phi = 1^\circ$ 时：

$$\beta_{\min} \approx 0.0453,\qquad \sigma_{\max} \approx 33.8\ \text{g/m}^2$$

**Files**:
- `displaced_orbit.py` — 精确位移轨道方程、最优锥角、受力分析
- `stability.py` — 一阶扰动灵敏度、等效外压扰动、漂移时间估计

在最优锥角附近，还可以写出局部闭式响应：

$$\frac{\Delta a_z}{a_{z,0}} \approx \varepsilon_\beta - 3\delta^2$$
$$\frac{\Delta a_r}{a_{r,0}} \approx \varepsilon_\beta - \frac{3}{\sqrt{2}}\delta$$

其中 $\delta$ 以弧度计、$\varepsilon_\beta$ 为分数形式的 beta 误差。
这说明轴向残差对小姿态误差只有二阶敏感，而径向残差是一阶敏感。

### 2. Mass Budget (`mass_budget/`)

质量预算和系统 $\beta$ / 利用率计算。

**Core equations**:

系统面密度:
$$\sigma_{\text{sys}} = \sigma_r + \lambda \sigma_p + \sigma_{\text{extra}}$$

系统光压参数:
$$\beta_{\text{sys}} = \frac{\sigma^*}{\sigma_{\text{sys}}}$$

给定目标角度 $\phi$ 的最大填充因子:
$$\lambda_{\max}(\phi) = \frac{\sigma_{\max}(\phi) - \sigma_r - \sigma_{\text{extra}}}{\sigma_p}$$

其中 $\sigma_{\max}(\phi) = \sigma^*/\beta_{\min}(\phi)$。

电能利用率定义:
$$\eta_{\text{abs}} = \lambda \eta_{\text{pv}}$$

若与采用同一 PV 技术、但满壳面均可发电的 Dyson Swarm 比较，则

$$U_{\text{Dyson, rel}} = \lambda$$

若再把显式结构尺度律接入，并反过来要求达到目标 $\lambda$，则最小节点功率来自：

$$P_{\min}(\phi,\lambda) = A_p S \eta_{\text{pv}} = \lambda A_r^{\min}(\phi,\lambda) S \eta_{\text{pv}}$$

其中 $A_r^{\min}$ 由

$$\sigma_r + \lambda \sigma_p + \sigma_{\text{structure}}(A_r) \le \sigma_{\max}(\phi)$$

隐式确定。

**Files**:
- `materials.py` — 源有据的材料数据库
- `calculator.py` — 质量预算、角度极限、利用率 trade study，以及目标 fill factor 的最小功率求解

### 3. Thermal Analysis (`thermal/`)

热平衡分析。

**Core equation**:

$$\alpha S A_{\text{proj}} = \epsilon \sigma_{\text{SB}} T^4 A_{\text{rad}}$$

**Files**:
- `equilibrium.py` — 反射膜 / 载荷舱稳态温度计算

### 4. Controlled Comparisons (`comparison/`)

与 Dyson Swarm / Dyson Ring 做理想化上限比较的基准模块。

**Controlled-variable assumptions**:

- 同一恒星、同一轨道半径
- 不考虑材料老化、热退化、维护、控制损耗
- 只比较几何截获与理想光伏转换

**Core equations**:

壳面上理想集能面积为 $A_c$ 时：
$$P = \eta \frac{L_\odot}{4\pi r^2} A_c$$

理想 Dyson Swarm 上限（覆盖率 $f$）：
$$P_{\text{swarm}} = \eta f L_\odot,\qquad 0 \le f \le 1$$

理想 Dyson Ring 上限（球带半角 $\psi$）：
$$P_{\text{ring}} = \eta \sin\psi \, L_\odot$$

同壳面占用前提下，MDDS 相对理想 Swarm 的比值为：
$$\frac{P_{\text{MDDS}}}{P_{\text{swarm}}} = \min(1,\lambda)\frac{\eta_{\text{MDDS}}}{\eta_{\text{swarm}}}$$

若两边使用同代 PV，则该比值退化为 $\min(1,\lambda)$，因此 MDDS 不会在纯能量上超越同条件的理想 Swarm。

### 5. Structural Scaling (`structural/`)

显式节点结构模型，用几何尺度律替代抽象的 `extra_areal_density` 参数。

当前模型假设：

- 方形反射器
- `cross` 或 `perimeter` 两种 boom 拓扑
- 载荷舱由四根角点 tether 悬挂在反射器下方
- 线性构件质量按 g/m 输入
- 固定载荷舱 / 姿控 / 部署硬件质量按 kg 输入

结构材料库现在同时包含：

- exploratory placeholder 线密度（便于快速扫参数）
- source-backed 线密度条目，例如：
  - `acs3_composite_boom_2023`
  - `dyneema_1p25mm_usspars`
  - `dyneema_2mm_usspars`

结构额外面密度写成：

$$\sigma_{\text{structure}}(A_r) = \frac{1000\,m_{\text{structure}}(A_r)}{A_r}$$

因此当节点做大时，固定质量项被摊薄；当节点很小且目标角度很大时，结构质量会主导整个面密度预算。

**Files**:
- `structural/geometry.py` — 几何尺度律结构模型

---

## Usage

```python
from models.orbital import DisplacedOrbit
from models.mass_budget import (
    SystemBudget,
    max_fill_factor_for_angle,
    max_fixed_mass_for_angle_power_fill_factor,
    minimum_power_for_fill_factor_with_structure,
)
from models.comparison import required_efficiency_ratio_to_match_swarm
from models.thermal import payload_temperature
from models.structural import NodeStructure

# Exact displaced-orbit solution at 1 AU and 1 degree
orbit = DisplacedOrbit(r_au=1.0, phi_deg=1.0)
params = orbit.get_params()

# Best-case 1 degree fill factor with current materials
summary = max_fill_factor_for_angle(
    phi_deg=1.0,
    reflector_material="cp1_subsystem_nasa_2009",
    pv_material="ultralight_tandem_2021",
)

# A node that uses half of the reflector footprint as PV area
budget = SystemBudget.from_fill_factor(
    reflector_material="cp1_subsystem_nasa_2009",
    pv_material="ultralight_tandem_2021",
    fill_factor=0.5,
)

# Thermal snapshot for the payload
payload_k = payload_temperature(distance_au=1.0, pv_efficiency=0.274)

# Pure controlled-variable comparison to an ideal Dyson Swarm
eta_ratio_needed = required_efficiency_ratio_to_match_swarm(
    budget.relative_dyson_utilization()
)

# Minimum node power needed to hold 10% of an ideal same-efficiency Swarm at 1 deg
threshold = minimum_power_for_fill_factor_with_structure(
    phi_deg=1.0,
    target_fill_factor=0.10,
    structure_model=NodeStructure(topology="cross", fixed_mass_kg=0.5, line_mass_margin_factor=1.1),
)

# Maximum fixed bus mass allowed once angle, power, and utilization are fixed
allowance = max_fixed_mass_for_angle_power_fill_factor(
    phi_deg=1.0,
    pv_power_required_w=10000.0,
    target_fill_factor=0.10,
    structure_model=NodeStructure(
        topology="cross",
        boom_material="acs3_composite_boom_2023",
        tether_material="dyneema_1p25mm_usspars",
        fixed_mass_kg=8.3,
        line_mass_margin_factor=1.0,
    ),
)
```

---

## Validation

每个模型需通过以下验证:

1. **单位分析** — 所有方程量纲正确
2. **极限情况**
   - $\phi \to 0$: 退化为开普勒轨道
   - $\lambda \to 0$: 退化为纯反射帆极限
   - $\beta \to 1$: 接近全光压悬浮边界
3. **数值回归** — 1° 参考环结果保持：
   - $\beta_{\min} \approx 0.04534$
   - $\alpha_{\text{opt}} \approx 35.264^\circ$
   - $\sigma_{\max} \approx 33.76$ g/m²
