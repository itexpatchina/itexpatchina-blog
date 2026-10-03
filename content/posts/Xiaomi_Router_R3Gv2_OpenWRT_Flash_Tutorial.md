---
title: "Xiaomi Router R3Gv2 Openwrt Flash Tutorial"
date: 2025-09-19
description: "Tutorial about how to flash OpenWRT into a Xiaomi R3Gv2 router"
tags: ["GitHub", "Projects", "OpenSource"]
draft: false
---

> 🔗 **Source Repository:** [https://github.com/itexpatchina/Xiaomi_Router_R3Gv2_OpenWRT_Flash_Tutorial](https://github.com/itexpatchina/Xiaomi_Router_R3Gv2_OpenWRT_Flash_Tutorial)

This guide walks you through flashing the Xiaomi Mi Router 3G v2 (R3Gv2) with OpenWRT using the [OpenWRT Invasion](https://github.com/acecilia/OpenWRTInvasion) exploit. 

This method enables SSH access on stock firmware without soldering or serial access.

> ⚠️ Use at your own risk. This process may void your warranty and carries a small risk of bricking your device. Proceed only if you're comfortable with CLI tools and network troubleshooting.
> Per my personal experience, Xiaomi R3Gv2 router actually ACCEPT a Xiaomi 4A OpenWRt firmware version, which will the version that'll be demo'ed below.

---

## 📦 Requirements

- Xiaomi Mi Router 3G v2 (R3Gv2) running stock firmware - this is actually very accessible through 2nd hand market such as Xianyu 咸鱼 at around 30 RMB per unit
- A Linux machine and in my case Ubuntu 24.04 LTS desktop edition
- Ethernet cable (recommended for stability)
- [OpenWRT Invasion](https://github.com/acecilia/OpenWRTInvasion) cloned locally
- OpenWRT firmware image for R3Gv2: [openwrt-23.05.2-ramips-mt7621-xiaomi_mi-router-4a-gigabit-squashfs-sysupgrade.bin](https://downloads.openwrt.org/releases/23.05.2/targets/ramips/mt7621/openwrt-23.05.2-ramips-mt7621-xiaomi_mi-router-4a-gigabit-squashfs-sysupgrade.bin)

---

## 🛠️ Step-by-Step Instructions

### 1. Connect to the Router

- Reset the router to factory settings.
- Connect your PC to the router via Ethernet or Wi-Fi.
- Access the router's web UI at `http://192.168.31.1` and log in.

### 2. Clone OpenWRT Invasion

```bash
git clone https://github.com/acecilia/OpenWRTInvasion.git
cd OpenWRTInvasion
pip3 install -r requirements.txt
```

### 3. Run the Exploit
```bash
python3 remote_command_execution_vulnerability.py
```


## 💾 Flash OpenWRT Firmware into R3Gv2

### 1. Telnet to Exploited Router Backend

```bash
telnet root@192.168.31.1
```
login and passward are both: root


### 2. Use Below Commands to Flash it

```bash
cd /tmp/
wget http://downloads.openwrt.org/releases/23.05.2/targets/ramips/mt7621/openwrt-23.05.2-ramips-mt7621-xiaomi_mi-router-4a-gigabit-squashfs-sysupgrade.bin
mtd -e OS1 -r write openwrt-23.05.2-ramips-mt7621-xiaomi_mi-router-4a-gigabit-squashfs-sysupgrade.bin OS1
```

### 3. Reboot the Router

Use http://192.168.1.1 to access the newly flashed OpenWRT router backend with default username root wiht no initial password.
