---
title: "Cloudflarewarp"
date: 2025-07-15
description: "WARP VPN Related Knowledge Share"
tags: ["GitHub", "Projects", "OpenSource"]
draft: false
---

> 🔗 **Source Repository:** [https://github.com/itexpatchina/CloudFlareWARP](https://github.com/itexpatchina/CloudFlareWARP)

> 📘 **中文版本**：如果您在中国大陆，请查看本项目的 [中文说明文档](./README_CN.md)。



This document provides a practical overview of how to use Cloudflare’s free VPN services — WARP and 1.1.1.1 — while operating within mainland China.

<img src="https://one.one.one.one/media/warp-plus.png"/>

## Current Status of the WARP App in China

As of 2025, Cloudflare’s WARP and 1.1.1.1 apps generally do **not** function reliably behind China’s Great Firewall (GFW). In contrast, throughout much of 2023, the apps operated smoothly across iPhones, Android devices, and PCs.

While it’s still possible to download and install the apps — assuming access to a non-China Apple ID or Google Play Store — successfully establishing a WARP connection has become increasingly rare, if not impossible.

Many Chinese tech YouTubers suspect that Cloudflare’s ingress IPs have been blacklisted by the GFW, and this theory holds weight. Cloudflare openly publishes its WARP ingress IP list here:  🔗 [Cloudflare WARP Ingress IPs](https://developers.cloudflare.com/cloudflare-one/connections/connect-devices/warp/deployment/firewall/#warp-ingress-ip)

### WireGuard Protocol IP Ranges (Quoted from Cloudflare on 2025-07-13)

- **IPv4 Range**: `162.159.193.0/24`  
- **IPv6 Range**: `2606:4700:100::/48`  
- **Default Port**: `UDP 2408`  
- **Fallback Ports**:  
  - `UDP 500`  
  - `UDP 1701`  
  - `UDP 4500`

## WireGuard Configuration via Telegram Bot

Since Cloudflare's WARP is fundamentally a WireGuard-based solution, it’s possible to either extract an existing configuration or create a new one — provided it adheres to Cloudflare’s standard settings.

One of the most convenient tools I use personally is the following Telegram bot:

<img width="335" height="442" alt="Telegram Bot Interface" src="https://github.com/user-attachments/assets/789096c1-7ee5-48c2-8995-a9962e4c7e71" />

Simply send the `/generate` command to this bot, and you’ll receive a `wg-config.conf` file — a valid WireGuard configuration that can be imported into the standard WireGuard app (iOS, Android, or Windows).

<img width="450" height="188" alt="Generated WireGuard Config File" src="https://github.com/user-attachments/assets/9be0fe66-215d-4da5-b661-e60c1c4f84ad" />


## Limitations of WireGuard Config Inside China

Below is a sample `wg-config.conf` file generated via the Telegram bot (sensitive keys truncated for privacy):

<img width="412" height="175" alt="Sample WireGuard Configuration" src="https://github.com/user-attachments/assets/85de15ed-373f-4fa6-a220-8a40833430e5" />

While this configuration may appear valid, it typically **will not work inside mainland China** due to how DNS resolution interacts with the Great Firewall (GFW). Specifically:

- The endpoint `engage.cloudflareclient.com:2408` often resolves to a Cloudflare ingress IP close to the user’s geographic location.
- These localized IPs are highly likely to be blacklisted by GFW, resulting in failed connections.
- This same behavior occurs when using the WARP app directly — tapping the "Connect" button simply attempts to resolve and connect to one of those inaccessible ingress IPs.

Therefore, while the bot-generated config file might work in less restricted regions, additional measures are needed for stable connectivity within China.

## Searching for Viable Endpoints

While the default endpoint `engage.cloudflareclient.com:2408` often fails inside mainland China, several Cloudflare ingress IPs (previously listed) may still be accessible.

Chinese tech YouTuber **yonggekkk** shares a helpful set of scripts on GitHub that can scan and identify working endpoint IP–port pairs.  

🔗 GitHub Project: [warp-yg](https://github.com/yonggekkk/warp-yg)  
📦 Windows-only Script Bundle: [Download ZIP](https://github.com/yonggekkk/warp-yg/raw/refs/heads/main/WIN%E7%AB%AFwarp%E8%87%AA%E9%80%89IP-v23.11.15.zip)

> ⚠️ **Security Warning**:  
> Windows Defender may flag parts of this script as suspicious. Use a **dedicated virtual machine (VM)** on the same network as your main workstation to run tests safely.

> 🈶 **Language Note**:  
> The script’s interactive menu is in Chinese, so basic understanding of the language will help navigate it more efficiently.

<img width="260" height="55" alt="Script Running Screenshot" src="https://github.com/user-attachments/assets/9ef05c97-6b29-4f6b-a2a5-705a2fc3fd2b" />


## Using Viable Endpoints in WireGuard

In the previous step, the test script outputs a `result.csv` file containing viable IPv4 endpoint addresses. 

## 📥 Download Previously Tested Files

I’ve uploaded two CSV files — `result1.csv` and `result2.csv` — from earlier test runs using the script bundle. They are available in the root directory of this GitHub repository and can be used as reference samples or for further testing:

- [`result1.csv`](https://github.com/itexpatchina/CloudFlareWARP/raw/main/result1.csv)
- [`result2.csv`](https://github.com/itexpatchina/CloudFlareWARP/raw/main/result2.csv)

You can choose one of the working IP–port pairs to replace the default Cloudflare endpoint `engage.cloudflareclient.com:2408` in your `wg-config.conf` file.

For instance, if `162.159.192.86:1387` is confirmed as functional, simply update the endpoint line: `Endpoint = 162.159.192.86:1387`

<img width="272" height="79" alt="image" src="https://github.com/user-attachments/assets/13171155-679a-4762-8260-5d0676b5d5cc" />


## WireGuard Connection Demo on Windows 11

I'm currently demonstrating WireGuard on a Windows 11 PC:

<img width="549" height="507" alt="image" src="https://github.com/user-attachments/assets/f73528b2-7859-499d-9041-799fda4fac5a" />


Once you click the **Activate** button, the connection will likely succeed. The WireGuard transfer panel will display live traffic stats like:

> `XX KiB received, YY KiB sent`

<img width="553" height="506" alt="WireGuard Transfer Panel" src="https://github.com/user-attachments/assets/ecd2563d-2277-45e1-bdf6-e74e1eee7b91" />

### Connection Verification

- A ping to Google confirms network access:

<img width="625" height="305" alt="Google Ping Success" src="https://github.com/user-attachments/assets/e8be78ed-53b1-43c2-9dd6-f1778897d3ed" />

- According to [whatismyipaddress.com](https://whatismyipaddress.com), the detected IPv4 address still points to mainland China — typically in a Cloudflare datacenter (e.g. Shanghai):

<img width="778" height="470" alt="Cloudflare IP Location in China" src="https://github.com/user-attachments/assets/025d4048-40e9-4675-9003-4dee6c23de43" />

### Access Limitations

Despite a working WireGuard tunnel:

- Major AI platforms remain inaccessible:

<img width="408" height="374" alt="AI Site Blocked" src="https://github.com/user-attachments/assets/a7c09130-8940-462a-bc7d-9581619e819d" />

- Geo-restricted streaming services like Netflix also fail:

<img width="528" height="72" alt="Netflix Access Denied" src="https://github.com/user-attachments/assets/58451dd3-8628-49fb-8c8d-810d8c25d013" />

### Accessible Services

Fortunately, websites typically blocked in mainland China — such as Google, Facebook, YouTube, X (formerly Twitter), and Instagram — become available again with reasonable connection speeds:

<img width="500" height="286" alt="Google Homepage Access Restored" src="https://github.com/user-attachments/assets/deb53908-8a2a-4cd6-a16c-de01fecd2652" />


## Conclusion

Cloudflare WARP, while built on the robust WireGuard protocol, faces significant connectivity challenges within mainland China due to GFW interference. However, with the help of community tools and endpoint scanning scripts, it's still possible to create functional configurations using manually selected IP–port pairs. Although access to geo-restricted services like Netflix and AI platforms remains limited, the workaround enables reliable access to essential global sites such as Google, YouTube, Facebook, and Instagram. This guide provides a hands-on walkthrough—from configuration generation to live testing—and offers practical insights for users seeking partial but meaningful restoration of open internet access.

## ⭐ Support This Project

If you’ve found this guide helpful or insightful, consider giving it a ⭐ star on GitHub! It’s a simple way to show appreciation and helps others discover the project more easily. Starring also lets you keep track of updates and new tips as they’re added.

Together, we can build a more open and informed tech community — one config file at a time.
