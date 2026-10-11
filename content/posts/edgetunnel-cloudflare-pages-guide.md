---
title: "Edgetunnel Cloudflare Pages Guide"
date: 2026-10-11
description: "Technical guide and open-source project."
tags: ["GitHub", "Projects", "OpenSource"]
draft: false
---

> 🔗 **Source Repository:** [https://github.com/itexpatchina/edgetunnel-cloudflare-pages-guide](https://github.com/itexpatchina/edgetunnel-cloudflare-pages-guide)

---
title: "Setting Up EdgeTunnel on Cloudflare Pages: Complete Bilingual Guide | Cloudflare Pages 部署 EdgeTunnel 完整双语指南"
date: 2026-10-10
description: "A complete bilingual guide on forking cmliu/edgetunnel to your GitHub account (itexpatchina), deploying on Cloudflare Pages, binding custom domains, and optimizing clean IPs. | 基于 cmliu/edgetunnel 开源项目的 Cloudflare Pages 部署与优选 IP 进阶指南。"
tags: ["Cloudflare", "EdgeTunnel", "DevOps", "Networking", "Serverless"]
draft: false
---


# 🚀 Cloudflare Pages 部署 EdgeTunnel 完整双语实战指南

> 🔗 **Original Open-Source Project / 原开源项目:** [cmliu/edgetunnel](https://github.com/cmliu/edgetunnel)

**EdgeTunnel** is a lightweight, serverless WebSocket routing gateway engineered to run directly inside Cloudflare Workers & Cloudflare Pages.

---

## 📋 Pre-requisites / 准备工作

Before starting, ensure you have:
1. **A Cloudflare Account** (Free tier is fully sufficient).
2. **A Custom Domain Name** added and active on Cloudflare DNS.
3. **A Generated UUID** (Version 4 UUID) to secure your tunnel.

> Generate a UUID on Linux/macOS: `uuidgen`

---

## 🛠 Step 1: Fork or Clone `cmliu/edgetunnel` to Your GitHub Account / 第一步：将 `cmliu/edgetunnel` 导入至个人 GitHub 账号 (`itexpatchina`)

1. Fork or Clone the official repository `https://github.com/cmliu/edgetunnel` into your personal GitHub account (`itexpatchina`).
   （在 GitHub 上将官方原仓库 `cmliu/edgetunnel` Fork 或 Clone 到您的个人账号 `itexpatchina` 下，可命名为 `edgetunnel-cloudflare-pages-guide`）。
2. Repository structure:
   ```text
   repository/
   ├── worker.js        # Core WebSocket worker script
   ├── index.html       # Landing page UI
   └── README.md        # Deployment tutorial
   ```

---

## ☁️ Step 2: Deploy to Cloudflare Pages / 第二步：部署至 Cloudflare Pages

1. Log into your Cloudflare Dashboard.
2. Navigate to Workers & Pages -> Create Application -> Pages.
3. Connect to Git and choose `edgetunnel-cloudflare-pages-guide`.
4. Configure deployment settings:
   * Project Name: `my-edgetunnel`
   * Production Branch: `main`
   * Framework Preset: `None`
   * Build Output Directory: `/`
5. Click Save and Deploy.

---

## 🔐 Step 3: Configure Environment Variables / 第三步：配置环境变量

In Pages project settings (Settings -> Environment Variables):

| Variable Name | Description |
| :--- | :--- |
| `UUID` | Your secure authentication UUID string |
| `PROXY_IP` | Optional fallback proxy IP endpoint |

---

## 🌐 Step 4: Bind Custom Domain & Optimize Clean IPs / 第四步：绑定自定义域名与优选 IP 加速

1. In Cloudflare Pages project dashboard, click Custom Domains.
2. Add your designated subdomain (e.g. `tunnel.example.com`).
3. Cloudflare automatically provisions SSL/TLS certificate.

---

## Step 5: Connection Parameters

Configure your client application with:

* Protocol: WebSocket
* Address / Server: `tunnel.example.com`
* Port: 443
* UUID: Your configured UUID
* Transport / Protocol: ws (WebSocket)
* Host / Header: `tunnel.example.com`
* TLS: Enabled

---

## Step 6: Route & Latency Optimization

1. Locate low-latency Cloudflare edge IP endpoints.
2. Set client Server Address to the optimized IP while keeping Host and SNI set to `tunnel.example.com`.

---

## Verification & Testing

1. Connect to the WebSocket endpoint.
2. Query network status in terminal.
3. Confirm that the returned IP belongs to Cloudflare global ASN.

---

## Summary

Deploying EdgeTunnel on Cloudflare Pages gives you a resilient, zero-maintenance serverless network endpoint hosted on Cloudflare edge network at zero cost.
