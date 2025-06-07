# 挑战杯问答

## 指导问题

> 所有的回答都要通俗易懂， 具体不用大道理。
> 添加学生日常实验过程，凸显正式性。

### 为什么做一个智能汽车加密的芯片？动机

#### answer strategy

- 高度，通俗
- 目前车企信息缺陷，具案例

#### answer

- **10 米外"隔空开车门"**：Pwn2Own 2025，研究员利用 TPMS 漏洞 CVE-2025-2082 远程解锁并点火 Tesla Model 3。
- **一夜召回 110 万辆**：2025-06，福特后视摄像头固件死机，官方迅速 OTA 召回
- **漏洞与召回"双激增"**：2024 年新增 422 个汽车 CVE，61 % 属高危；同年 OTA 召回 406 万辆，同比增长 246 %，软件即风险。

### 这个芯片怎么做出来？可行性

#### answer strategy

- 三步走
  - 市场调研
  - 怎么去设计制造规划
  - 目前做到第几个阶段

#### answer

先市场调研：对比 Infineon AURIX HSM 与 Rambus RT-640，功耗和成本仍偏高，低端 ECU 缺轻量安全芯片。再设计规划：选 28 nm 成熟工艺，SMIC 将晶圆价降至 1500 美元，成本可控；构建轻量分组加密IP核心，按 ISO 26262 ASIL-B 做安全验证。当前进度：算法与 RTL 已冻结，覆盖率 90%，正备 28 nm 测试流片.

### 公司为什么选择你的产品，优势在哪？

#### answer strategy

- 技术好 说了技术指标是不行，需要通俗易懂
- 举例子，找现实中发生的安全事件，

#### answer

黑客真能"隔空控车"：今年 CVE-2025-2082 让研究员在停车场外就解锁并点火 Tesla Model 3；早在 2015 年，Jeep 因娱乐系统漏洞被远程关发动机，结果召回 140 万辆；Ford 又因后视摄像头软件故障一次性召回 110 万辆车。每次召回都是数亿美元级别的代价。

我们的芯片把"车内对话"全部加密，相当于给每条总线报文贴上一次性封条：非法指令进不了车、假固件刷不进 ECU。它只占 x mm²、微瓦级功耗，成本不到传统 HSM 的三分之一，却能让主机厂省下动辄百万辆的召回风险——这就是他们选择我们的理由。

### 市面上的安全芯片，为什么使用你的，安全在哪里？

#### answer strategy

- 我们正在汇总材料到国家安全部门送检
- 我们团队成员都为第一作者，公开发表SCI论文，已经在国际密码同行中得到初步肯定

#### answer

Jeep远程被黑导致140万辆召回，车企因漏洞付出亿美元代价。市面 AURIX HSM、Rambus RT-640 虽安全，但功耗与成本高，对中低端 ECU 不友好。我们的芯片面积 x mm²、微瓦级功耗，侧信道与故障注入双重加固，并准备送国家商用密码产品认证，确保合规。核心算法于学生第一作者发表于 SCI 期刊，多篇论文获同行引用，安全性获学术与产业双认可。

### 你的产品定价多少，同类多少？

#### answer strategy

- 依据ppt数据，推测合理值，给出一个范围区间

#### answer

按 ≥10 万颗量产计算，本芯片单价 **0.8 – 1.2 美元**；小批量试产（1 万颗）亦控制在 1.5 美元以内。可比方案：Microchip TA100 10 k 价约 **1.5 美元**，仅是安全元件；集成 HSM 的 NXP S32K344 MCU 小批量 **14 – 16 美元**，且功耗更高。凭 x mm² 面积与微瓦功耗，我们把成本压到竞品的 1/2–1/10，在保持车规安全的同时，更适配大规模 ECU。

### 成果展示

#### answer strategy

- 我们是一代原型机

## Papera QA

**Attack path** for the automotive security

- wireless commnication
  - esim
- Harware sercurity module
  - TPM (trusted platform module

### exmple

- [tesla hackers on defcon 23](https://www.cnet.com/roadshow/news/tesla-hackers-explain-how-they-did-it-at-def-con-23/)
  - one way is physical disassemble, then to internal Car network contrl the onboard **infotainment** system, the control the full car. here need constantly to get the _token_ from the Tesla's servers.
- [based on physical link CAN ubs](https://www.freecodecamp.org/news/hacking-cars-a-guide-tutorial-on-how-to-hack-a-car-5eafcfbbb7ec)
  - CAN bus is the internal network of the car, which is used to communicate between different components. e.g. to change the RPM table number, remotely controlled the steering, braking, acceleration, or to change the speed limit.
- [BWN i3 attack by tencent keen 2018 ](https://keenlab.tencent.com/en/whitepapers/Experimental_Security_Assessment_of_BMW_Cars_by_KeenLab.pdf)
  - Our research findings have proved that it is feasible to gain local and remote access to infotainment, T-Box components and UDS communication above certain speed of selected BMW vehicle modules and been able to gain control of the CAN buses with the execution of arbitrary, unauthorized diagnostic requests of BMW in-car systems remotely
- [keen top confence IEEE S&P 2024](https://keenlab.tencent.com/zh/2023/11/27/2023-SP24-a-Practitioners-Perspective/)
  - We identified 20 key insights from the interview data, ranging from the challenges and gaps in the existing automotive security industry to the limitations and rec ommendations for current regulations.
  - successfully exploited the corresponding attack chains in the newly gateway-segmented IVN, uncovering new automotive attack surfaces that previous research failed to cover, including the in-vehicle browser, official mobile app, backend server, and in-vehicle malware.

### note

- AEC-xx strandard is automotive reliability, not specific to security.
