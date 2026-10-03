---
title: "About IT Expat China | 关于本站"
date: 2026-10-03
draft: false
description: "Behind the GFW: Homelabs, self-hosting, proxy routing, and digital sovereignty."
---

## 👋 Welcome to IT Expat China

**IT Expat China** is a technical knowledge base and lab journal dedicated to navigating the unique technical challenges of operating IT infrastructure, homelabs, and self-hosted services from behind the Great Firewall (GFW).

---

### 🛡️ Privacy & Anonymity Statement

Due to the sensitive nature of network research, circumvention technologies, and operating within restrictive regulatory environments, **this site operates under total anonymity**. 

* No real names, employer information, or identifiable personal telemetry are published.
* All IP addresses, server credentials, and domain identifiers in tutorials are sanitized or anonymized.
* All hosted services and build pipelines utilize zero-trust tunneling and privacy-preserving infrastructure.

---

### 🔬 Core Focus Areas & Homelab Stack

This blog documents real-world experiments, network engineering workarounds, and infrastructure setups across several key domains:

#### 1. Homelab Architecture & Virtualization
* **Hypervisors:** Dual-node VMware ESXi clusters running isolated virtual machines and containers.
* **Storage & Backups:** Self-hosted Network Attached Storage (fnNAS / ZFS) with offsite encrypted backups.
* **Media & Game Hosting:** Self-hosted Jellyfin, Plex, and optimized Minecraft servers running on lightweight Linux instances.

#### 2. Cross-Border Networking & GFW Workarounds
* **Proxy Frameworks:** VLESS + REALITY protocols, 3X-UI management panels, and Xray core integrations.
* **Encrypted Tunnels:** Multi-gateway WireGuard VPN topologies, Cloudflare WARP, and authenticated Squid proxy chaining.
* **Smart Routing:** Policy-based routing with sing-box, DNS-over-HTTPS (DoH), and custom split-tunneling.

#### 3. Edge Gateways & Cloud Infrastructure
* **Cloud Infrastructure:** Multi-cloud deployments across low-latency Hong Kong, Tokyo, and Singapore VPS providers (CN2 GIA, CMI routes).
* **Reverse Proxies & Tunnels:** Cloudflare Tunnels (`cloudflared`) exposing internal web services without opening public ports.
* **Automated CI/CD:** Serverless static site generation with Hugo, GitHub Actions, and Cloudflare Pages.

---

### 💬 Contact & Community

If you share a passion for self-hosting, network engineering, privacy, or building resilient homelab setups behind restrictive networks, feel free to explore the repository or connect via public open-source channels.

> *"Knowledge belongs to everyone — no matter where in the world you happen to connect from."*

<br>
<hr>
<br>

## 👋 欢迎来到 IT Expat China

**IT Expat China** 是一个技术知识库与实验日志，专注于记录在防火长城（GFW）网络环境下搭建与运维 IT 基础设施、Homelab 自建服务及网络工程的实践经验。

---

### 🛡️ 隐私与匿名声明

鉴于网络工程研究、代理路由技术以及在特定网络监管环境下的敏感性，**本站坚持完全匿名运行**。

* 本站绝不发布任何真实姓名、工作单位或可识别个人身份的信息。
* 所有教程与文章中的 IP 地址、服务器凭据及域名标识均经过脱敏与匿名化处理。
* 所有自建服务与构建流水线均采用零信任隧道（Zero-Trust Tunnels）及隐私保护型基础设施。

---

### 🔬 核心关注领域与 Homelab 架构

本博客记录了跨多个技术领域的真实实验、网络优化方案与架构配置：

#### 1. Homelab 架构与虚拟化
* **虚拟化平台：** 双节点 VMware ESXi 集群，运行隔离的虚拟机与 Docker 容器。
* **存储与备份：** 自建网络附加存储（fnNAS / ZFS），配置异地加密备份。
* **媒体与游戏服务：** 轻量级 Linux 实例上运行的 Jellyfin、Plex 媒体服务器及 Fabric 优化版 Minecraft 游戏服务器。

#### 2. 跨境网络与 GFW 优化
* **代理协议栈：** VLESS + REALITY 协议、3X-UI 可视化面板及 Xray 核心集成。
* **加密隧道：** 多网关 WireGuard VPN 拓扑、Cloudflare WARP 及带鉴权的 Squid 代理链。
* **分流路由：** 基于 sing-box 的智能分流、DNS-over-HTTPS (DoH) 及自定义 Split-Tunneling 规则。

#### 3. 边缘网关与云端架构
* **云端基础设施：** 跨香港、东京、新加坡等低延迟 VPS 节点的多云部署（精选 CN2 GIA、CMI 优化线路）。
* **反向代理与隧道：** 利用 Cloudflare Tunnels (`cloudflared`) 安全内网穿透，无需暴露公网端口。
* **自动化 CI/CD：** 基于 Hugo、GitHub Actions 与 Cloudflare Pages 的无服务器静态网站部署。

---

### 💬 交流与社区

如果您同样对自建服务、网络工程、隐私保护以及突破限制性网络构建坚韧的 Homelab 架构感兴趣，欢迎浏览本站文章或通过开源社区共同探讨。

> *“知识属于每个人 —— 无论你身在何处，从哪里连接。”*
