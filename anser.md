# 挑战杯问答

## 指导问题

> 所有的回答都要通俗易懂， 具体不用大道理。
> 添加学生日常实验过程，凸显正式性。

### 为什么做一个智能汽车加密的芯片？动机

#### answer strategy

- 高度，通俗
- 目前车企信息缺陷，具案例

#### answer

- **10 米外“隔空开车门”**：Pwn2Own 2025，研究员利用 TPMS 漏洞 CVE-2025-2082 远程解锁并点火 Tesla Model 3。([gbhackers.com][1])
- **一夜召回 110 万辆**：2025-06，福特后视摄像头固件死机，官方迅速 OTA 召回 ([finance.sina.com.cn][2])
- **漏洞与召回“双激增”**：2024 年新增 422 个汽车 CVE，61 % 属高危；同年 OTA 召回 406 万辆，同比增长 246 %，软件即风险。([esmchina.com][3], [stdaily.com][4])

[1]: https://gbhackers.com/tesla-model-3-vcsec-vulnerability/?utm_source=chatgpt.com "Tesla Model 3 VCSEC Vulnerability Lets Hackers Run Arbitrary Code"
[2]: https://finance.sina.com.cn/stock/usstock/c/2025-06-02/doc-ineyszpt7410781.shtml?cre=tianyi&loc=32&mod=pchp&r=0&rfunc=18&tj=cxvertical_pc_hp&tr=12&utm_source=chatgpt.com "福特因后视摄像头故障召回110万辆汽车 - 新浪财经"
[3]: https://www.esmchina.com/news/13050.html?utm_source=chatgpt.com "高危漏洞占比超六成：汽车供应链成网络攻击“重灾区” - 国际电子商情"
[4]: https://www.stdaily.com/web/gdxw/2025-03/05/content_305228.html?utm_source=chatgpt.com "两部门：加强智能网联汽车召回及软件在线升级管理 - 科技日报"

### 这个芯片怎么做出来？可行性

#### answer strategy

- 三步走
  - 市场调研
  - 怎么去设计制造规划
  - 目前做到第几个阶段

### 公司为什么选择你的产品，优势在哪？

- 技术好 说了技术指标 不行
- 举例子，找现实中发生的安全事件，

### 市面上的安全芯片，为什么使用你的，安全在哪里？

- 我们正在汇总材料到国家安全部门送检
- 我们团队成员都为第一作者，公开发表SCI论文，已经在国际密码同行中得到初步肯定

### 你的产品定价多少，同类多少？

- 依据ppt数据，推测合理值，给出一个范围区间

### 成果展示

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
