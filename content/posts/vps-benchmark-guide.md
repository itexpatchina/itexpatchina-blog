---
title: "Vps Benchmark Guide"
date: 2026-10-12
description: "Technical guide and open-source project."
tags: ["GitHub", "Projects", "OpenSource"]
draft: false
---

> 🔗 **Source Repository:** [https://github.com/itexpatchina/vps-benchmark-guide](https://github.com/itexpatchina/vps-benchmark-guide)

---
title: "Linux VPS Benchmarking Masterclass: YABS, bench.sh, and GoECS (融合怪) Comparison | Linux VPS 性能与线路测评实战指南"
date: 2026-10-12
description: "A comprehensive bilingual guide to evaluating Linux VPS compute, random fio disk I/O, iperf3 network throughput, and triple-network Asia routing using open-source scripts. | 基于 YABS、bench.sh 与 GoECS (融合怪) 的 Linux 服务器性能与网络线路全方位测评指南。"
tags: ["VPS", "Benchmarking", "YABS", "GoECS", "Linux", "Networking", "DevOps", "Bilingual"]
draft: false
---


# 🚀 Linux VPS 性能与线路测评实战指南：YABS、bench.sh 与 GoECS (融合怪) 全景解析

When renting a Linux Virtual Private Server (VPS) from cloud providers, on-paper hardware specifications rarely tell the whole story [163]. Shared vCPU "noisy neighbor" contention, throttled random disk I/O, burstable bandwidth caps, and non-optimized ISP routing can severely degrade real-world application performance [163]. 

To evaluate whether a host meets your technical standards before deploying production workloads, automated open-source benchmarking scripts allow you to measure CPU compute, disk read/write IOPS, network throughput, and IP quality [164, 167].

在向云服务商租用 Linux 虚拟专用服务器 (VPS) 时，账面上的硬件参数往往无法反映真实性能 [163]。共享 vCPU 资源争抢、被限制的随机磁盘读写 (IOPS)、峰值带宽限制以及非优化的网络回程线路，都可能导致实际应用体验大幅打折 [163]。

为了在部署生产业务前全面评估服务器性能，自动化开源测评脚本可以帮助我们精准量化 CPU 计算能力、磁盘随机读写性能、网络吞吐量以及 IP 风险等级 [164, 167]。

---

## 📊 Overview & Suite Comparison / 工具概览与对比

| Feature / 测评维度 | **YABS (`yabs.sh`)** [85, 167] | **`bench.sh`** [1, 167] | **GoECS / Fusion Monster (融合怪)** [99, 167] |
| :--- | :--- | :--- | :--- |
| **Primary Focus / 核心关注** | Hardware compute, random fio disk I/O, iperf3 network / 硬件性能、随机 IOPS、全局带宽 [85, 91] | Quick hardware summary & sequential `dd` write speed / 基础配置速查与磁盘顺序写入 [1, 165] | Full audit: triple-network routing, IP risk score, unlocks / 全能测评：三网回程线路、IP 风险、流媒体解锁 [99, 167] |
| **CPU Benchmark / CPU 测评** | Geekbench 6 (default), GB4, GB5, GB7 [86, 88] | None (Lists CPU model & frequency only) / 无（仅展示型号与主频） [1] | Sysbench (default), Geekbench, or WinSAT [99, 110] |
| **Disk I/O Test / 磁盘测试** | `fio` (Random 4k, 64k, 512k, 1m 50/50 R/W) [88, 91] | `dd` (Sequential 1 GB write) [165] | `fio` and `dd` combined / `fio` 与 `dd` 结合 [99, 126] |
| **Network Test / 网络测试** | `iperf3` (8 parallel threads to global nodes) [87, 91] | Speedtest.net CLI nodes [1, 165] | Multi-region Speedtest nodes & 3-network ping / 节点测速与三网 Ping [99, 129] |
| **Routing Traces / 路由追踪** | None / 无 | None / 无 | NextTrace / NT3 (CN2 GIA, CUG 9929, CMI) [99] |
| **IP Quality & Unlocks / IP 质检与解锁** | None / 无 | None / 无 | 15+ IP risk databases, fraud score, Netflix/ChatGPT unlocks [99, 123] |
| **Privilege Needed / 运行权限** | Unprivileged / Non-root 均可 [85] | Non-root [1] | Non-root (Go version) or Root (Shell version) [99, 105] |

---

## 🛠️ 1. YABS (Yet Another Bench Script)

Created by Mason Rowe (`masonr/yet-another-bench-script`), **YABS** is the global benchmark standard across hosting communities like LowEndTalk and Hetzner [85, 94]. It automates performance testing for three critical server bottlenecks without requiring elevated root privileges or pre-installed dependencies [85].

由 Mason Rowe 开发的 **YABS** 是 LowEndTalk、Hetzner 等全球主机社区中最受欢迎的性能测试工具之一 [85, 94]。它无需 Root 权限或预装依赖，即可自动化评估服务器的三项关键性能瓶颈 [85]。

```bash
# Standard YABS execution command / 标准 YABS 一键运行命令
curl -sL yabs.sh | bash
```
*(Or via `wget` / 或通过 `wget` 运行)*:
```bash
wget -qO- yabs.sh | bash
```

### 🔬 What YABS Tests / YABS 测试项目：
1. **`fio` Random Disk Performance / `fio` 磁盘随机读写性能:** Conducts four random read/write disk tests using 4k, 64k, 512k, and 1m block sizes with a 50/50 read/write split [91]. This simulates real-world database and web application IOPS rather than ideal sequential speeds [91].
   （使用 4k、64k、512k 和 1m 块大小进行四项随机读写测试，按 50% 读 / 50% 写比例模拟真实的数据库和 Web 应用 IOPS 负载 [91]。）
2. **`iperf3` Network Throughput / `iperf3` 网络吞吐量:** Tests upload and download speeds across 8 parallel TCP streams to multiple enterprise bandwidth locations (Clouvider, Scaleway, etc.) [87, 91].
   （使用 8 个并行 TCP 数据流向全球多家企业级节点测试上行与下行带宽速度 [87, 91]。）
3. **Geekbench CPU Scores / Geekbench 处理器得分:** Measures single-core and multi-core integer, floating-point, and cryptographic processing capabilities, generating a shareable Geekbench URL [91].
   （量化单核与多核整数、浮点及加密计算性能，并生成可直接分享的 Geekbench 报告链接 [91]。）

### ⚙️ Useful YABS Execution Flags / 常用 YABS 运行参数：

```bash
# Run YABS with specific flags / 带参数运行 YABS
curl -sL yabs.sh | bash -s -- -flags
```

| Flag / 参数 | Function / 功能 | Use Case / 使用场景 |
| :--- | :--- | :--- |
| **`-r`** | Reduces `iperf3` test locations [88] | Prevents exhausting bandwidth caps on NAT/budget VPS / 减少测速节点以节省流量 [87, 88] |
| **`-i`** | Disables `iperf3` network testing completely [88] | Saves bandwidth when only evaluating CPU/Disk / 跳过网络测试仅测 CPU 与磁盘 [88] |
| **`-f` / `-d`** | Disables `fio` disk testing [88] | Prevents excessive disk write wear / 跳过磁盘 `fio` 读写测试 [88] |
| **`-g`** | Disables Geekbench CPU testing [88] | Speeds up execution on low-RAM servers / 跳过 Geekbench 以加速小内存 VPS 跑分 [88] |
| **`-7`** | Runs Geekbench 7 instead of Geekbench 6 [86, 88] | Evaluating newer CPU architectures / 使用最新的 Geekbench 7 跑分 [86, 88] |
| **`-j` / `-w`** | Outputs JSON or writes to a file [88] | Automating benchmark collection & API reporting / 导出 JSON 数据用于自动化分析 [88] |

---

## ⚡ 2. `bench.sh`

Created by Teddysun, **`bench.sh`** is the classic, hyper-lightweight benchmark script designed for rapid server health checks [1, 165].

由 Teddysun 编写的 **`bench.sh`** 是一款极轻量级的经典脚本，专为快速查看服务器基础硬件信息和网络状况而设计 [1, 165]。

```bash
# Execute bench.sh / 运行 bench.sh 脚本
wget -qO- bench.sh | bash
# Or via curl / 或通过 curl 运行
curl -Lso- bench.sh | bash
```

### 🔬 What `bench.sh` Tests / `bench.sh` 测试项目：
* **System Specs Audit / 系统基础架构审计:** Quickly parses CPU model, physical/virtual core count, processor frequency, total RAM/Swap, distribution distro, and Linux kernel version [1, 93].
  （快速列出 CPU 型号、核心数、主频、RAM/Swap 内存大小、系统发行版及 Linux 内核版本 [1, 93]。）
* **Sequential Write Speed (`dd`) / 顺序写入速度:** Measures disk write speeds using sequential 1 GB `dd` buffer flushes [165].
  （使用 1GB 顺序 `dd` 缓存刷新测试磁盘的峰值写入速度 [165]。）
* **Speedtest.net Throughput / 带宽测速:** Downloads test payloads from global Speedtest.net edge servers [1, 165].

---

## 🐲 3. GoECS / VPS Fusion Monster (VPS 融合怪)

Maintained by `spiritLHLS` and `oneclickvirt`, **GoECS (VPS Fusion Monster / 融合怪)** is the most exhaustive benchmarking suite available for cross-border hosting, ISP route tracing, and streaming unlock validation [98, 99]. 

The modern Go-based edition (`goecs`) runs as a compiled binary with **zero external dependencies**, DoH/DoT encrypted DNS fallbacks, and multi-threaded execution [98, 99].

由 `spiritLHLS` 与 `oneclickvirt` 维护的 **GoECS (VPS 融合怪)** 是目前功能最全的 Linux 服务器综合测评工具 [98, 99]。全新的 Go 语言重构版 (`goecs`) 实现了**零第三方环境依赖**，支持 DoH/DoT 加密 DNS 备用解析以及多线程并发检测 [98, 99, 104]。

```bash
# One-click GoECS install & execution (English) / 一键安装与运行命令（英文界面）
export noninteractive=true && curl -L https://raw.githubusercontent.com/oneclickvirt/ecs/master/goecs.sh -o goecs.sh && chmod +x goecs.sh && ./goecs.sh install && goecs -l=en

# One-click GoECS execution (Chinese) / 一键安装与运行命令（中文界面）
export noninteractive=true && curl -L https://raw.githubusercontent.com/oneclickvirt/ecs/master/goecs.sh -o goecs.sh && chmod +x goecs.sh && ./goecs.sh install && goecs -l=zh
```

### 🔬 What GoECS Tests / GoECS 核心功能：
1. **Triple-Network Routing Traces (三网回程 & 路由追踪):** Uses built-in `nt3` (NextTrace) to trace return routing paths across China Telecom (CN2 GIA / 163), China Unicom (CUG 9929 / 4837), and China Mobile (CMI) back to major mainland nodes (Beijing, Shanghai, Guangzhou, Chengdu) [99].
   （基于内置 `nt3` / NextTrace 引擎，测试电信 (CN2 GIA/163)、联通 (CUG 9929/4837) 与移动 (CMI) 回程路由及三网延迟 [99]。）
2. **IP Quality & Security Risk Audit / IP 质量与欺诈风险审查:** Queries 15+ fraud/security databases (Scamalytics, IPinfo, AbuseIPDB, MaxMind) to classify IP type (Datacenter vs. Residential) and measure IP risk scores. Tests outbound port 25 for mail server viability [99, 123].
   （并发查询 15+ 权威 IP 数据库，检测 IP 类型（数据中心机房 IP 或原生住宅 IP）、欺诈风险得分及 Outbound 25 端口邮件连通性 [99, 123]。）
3. **Streaming & AI Platform Unlocks / 流媒体与 AI 平台解锁测试:** Tests whether the VPS IP is allowed or blocked by major media and AI platforms, including Netflix, Disney+, ChatGPT, YouTube Premium, Spotify, and Steam [99, 127].
   （自动检测 Netflix、Disney+、ChatGPT、YouTube Premium、Spotify 及 Steam 等平台的解锁状态 [99, 127]。）
4. **Flexible CPU & Disk Testing / 灵活的计算与存储测试:** Uses `sysbench` by default for lightweight, network-independent CPU testing across any architecture, with optional toggles for Geekbench or `fio` [99, 110].
   （默认使用无网络依赖的 `sysbench` 进行轻量 CPU 跑分，也可自由切换为 Geekbench 或 `fio` 模式 [99, 110]。）

---

## 🎯 Decision Matrix & Summary / 总结与选型建议

* **Use YABS (`yabs.sh`) / 推荐使用 YABS：** When you want an industry-standard, unprivileged performance audit of raw CPU compute power and database-grade random 4k/64k disk IOPS [85, 91].
  （适合评估 CPU 算力和数据库级的 4k/64k 随机磁盘 IOPS [85, 91]。）
* **Use `bench.sh` / 推荐使用 `bench.sh`：** When you need a 10-second basic hardware summary and disk check before installing lightweight applications [1, 165].
  （适合在安装轻量应用前进行 10 秒快速硬件概览 [1, 165]。）
* **Use GoECS (`goecs`) / 推荐使用 GoECS (融合怪)：** When evaluating VPS providers for cross-border networking, routing quality (CN2/CMI/CUG), IP cleanliness, or streaming media unlocks [98, 99, 167].
  （适合全面评估跨国网络质量、三网回程线路 (CN2/CMI/CUG)、IP 欺诈得分及流媒体/AI 解锁状态 [98, 99, 167]。）
