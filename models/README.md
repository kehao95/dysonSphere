# Mathematical Models

本目录包含 MDDS (Micro-Displaced Dyson Swarm) 项目的数学模型。

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
| $\beta$ | Lightness number | $F_{\text{rad}}/F_{\text{grav}} = \sigma^*/\sigma$ | 0.01–0.05 | — |
| $\sigma$ | System areal density | $m_{\text{total}}/A_{\text{reflector}}$ | 30–150 | g/m² |
| $\phi$ | Displacement angle | Angle above/below orbital plane | 1°–5° | deg |
| $r$ | Orbital radius | Distance from Sun | 0.5–2 | AU |
| $\theta$ | Sail tilt angle | Reflector angle to radial direction | varies | deg |

### Geometry

| Symbol | Name | Definition |
|--------|------|------------|
| $A_r$ | Reflector area | Total reflective surface area |
| $A_p$ | Payload area | PV cell active area |
| $d$ | Vertical displacement | $r \sin\phi$ |

### Mass Components

| Symbol | Name | Notes |
|--------|------|-------|
| $m_{\text{total}}$ | Total system mass | $m_r + m_p + m_s$ |
| $m_r$ | Reflector mass | Thin film + coating |
| $m_p$ | Payload mass | PV cells + electronics + structure |
| $m_s$ | Structural mass | Booms, tethers, deployment mechanisms |
| $\sigma_r$ | Reflector areal density | $m_r / A_r$ |
| $\sigma_p$ | Payload areal density | $m_p / A_p$ |

---

## Model Modules

### 1. Orbital Dynamics (`orbital/`)

位移轨道的动力学模型。

**Core equations**:

力平衡条件（极坐标，轴对称）:

径向: $F_{\text{grav}} \cos\phi - F_{\text{cent}} - F_{\text{rad}} \cos\theta \cos\phi = 0$

轴向: $F_{\text{grav}} \sin\phi - F_{\text{rad}} \sin\theta = 0$

其中:
- $F_{\text{grav}} = \frac{G M_\odot m}{r^2}$
- $F_{\text{cent}} = m \omega^2 r \cos\phi$ (轨道离心力)
- $F_{\text{rad}} = 2 P_{\text{rad}} A_r \cos\theta$ (光压力)

**Files**:
- `displaced_orbit.py` — 位移轨道方程求解
- `stability.py` — 线性稳定性分析

### 2. Mass Budget (`mass_budget/`)

质量预算和系统 $\beta$ 计算。

**Core equations**:

系统面密度:
$$\sigma_{\text{sys}} = \frac{m_{\text{total}}}{A_r} = \sigma_r + \frac{m_p + m_s}{A_r}$$

系统 $\beta$:
$$\beta_{\text{sys}} = \frac{\sigma^*}{\sigma_{\text{sys}}}$$

给定目标 $\beta$，最大载荷密度:
$$\frac{m_p + m_s}{A_r} \leq \frac{\sigma^*}{\beta_{\text{target}}} - \sigma_r$$

**Files**:
- `materials.py` — 材料数据库
- `calculator.py` — $\beta$ 和质量预算计算器

### 3. Thermal Analysis (`thermal/`)

热平衡分析。

**Core equations**:

稳态能量平衡:
$$\alpha S A_{\text{proj}} = \epsilon \sigma_{\text{SB}} T^4 A_{\text{rad}}$$

其中:
- $\alpha$ = 吸收率
- $\epsilon$ = 发射率
- $S$ = 太阳辐照度 (~1361 W/m² at 1 AU)
- $\sigma_{\text{SB}}$ = Stefan-Boltzmann 常数

**Files**:
- `equilibrium.py` — 热平衡温度计算

---

## Usage

```python
from models.orbital import DisplacedOrbit
from models.mass_budget import SystemBudget
from models.thermal import ThermalEquilibrium

# 计算位移轨道参数
orbit = DisplacedOrbit(r=1.0, phi_deg=1.0)  # 1 AU, 1° displacement
beta_required = orbit.required_beta()

# 质量预算
budget = SystemBudget(
    reflector_density=1.4,  # g/m²
    payload_mass=10.0,      # kg
    reflector_area=1000.0   # m²
)
beta_achieved = budget.system_beta()

# 热分析
thermal = ThermalEquilibrium(
    distance_au=1.0,
    absorptivity=0.05,
    emissivity=0.9
)
T_eq = thermal.equilibrium_temperature()
```

---

## Validation

每个模型需通过以下验证:

1. **单位分析** — 所有方程量纲正确
2. **极限情况** — 
   - $\phi \to 0$: 退化为开普勒轨道
   - $\beta \to 1$: 接近完全悬浮
   - $r \to \infty$: 光压趋于零
3. **文献对标** — 与 McInnes (1999) 结果一致
