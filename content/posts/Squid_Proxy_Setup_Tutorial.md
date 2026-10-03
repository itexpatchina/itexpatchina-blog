---
title: "Squid Proxy Setup Tutorial"
date: 2025-10-20
description: "How I set up my squid proxy server"
tags: ["GitHub", "Projects", "OpenSource"]
draft: false
---

> 🔗 **Source Repository:** [https://github.com/itexpatchina/Squid_Proxy_Setup_Tutorial](https://github.com/itexpatchina/Squid_Proxy_Setup_Tutorial)

# 🛠️ 1st Step: Install Squid Proxy

Here’s how to install **Squid** on your system, depending on your Linux distribution:

---

### 🐧 For Debian/Ubuntu
```bash
sudo apt update
sudo apt install squid
```

- Configuration file: `/etc/squid/squid.conf`
- Service control:
  ```bash
  sudo systemctl start squid
  sudo systemctl enable squid
  sudo systemctl status squid
  ```

---

### 🔴 For CentOS/RHEL/Fedora
```bash
sudo yum install squid
```
Or on newer Fedora/RHEL:
```bash
sudo dnf install squid
```

- Configuration file: `/etc/squid/squid.conf`
- Service control:
  ```bash
  sudo systemctl start squid
  sudo systemctl enable squid
  sudo systemctl status squid
  ```

---

### 🧪 For Arch Linux
```bash
sudo pacman -S squid
```

- Configuration file: `/etc/squid/squid.conf`
- Service control:
  ```bash
  sudo systemctl start squid
  sudo systemctl enable squid
  sudo systemctl status squid
  ```

---

### 🔍 Verify Installation
After installation, check the version and test the config:
```bash
squid -v
squid -k parse
```


# 🛠️ 2nd Step: Install `htpasswd` 

#### On **Debian/Ubuntu**:
```bash
sudo apt update
sudo apt install apache2-utils
```

#### On **CentOS/RHEL/Fedora**:
```bash
sudo yum install httpd-tools
```

#### On **Arch Linux**:
```bash
sudo pacman -S apache
```

---

### ✅ Once Installed

You can create or update your password file like this:
```bash
htpasswd -c /etc/squid/htpasswd your_username
```
- `-c` creates a new file (omit it when adding more users).
- You’ll be prompted to enter a password.

---

You can add a 2nd user by omitting the ’-c‘ option  

```bash
htpasswd /etc/squid/htpasswd your_2nd_username
```
- You’ll be prompted to enter a password again.

---

# 🛠️ 3rd Step: Prepare `local.conf` file in /etc/squid/conf.d/ folder

---

### ✅ Content `local.conf` for Squid

```conf
# Listen on port 8080
http_port 8080

# Cache configuration
cache_dir ufs /var/spool/squid 100 16 256

# Authentication setup
auth_param basic program /usr/lib/squid/basic_ncsa_auth /etc/squid/htpasswd
auth_param basic realm "LAN Proxy Access"
auth_param basic credentialsttl 2 hours
auth_param basic casesensitive off

# ACL definitions
acl localnet src 192.168.0.0/24         # Internal LAN
acl all_ips src all                     # All IPs
acl authenticated proxy_auth REQUIRED   # Authenticated users

# Access rules
http_access allow localnet              # Allow LAN without auth
http_access allow authenticated         # Allow authenticated users
http_access deny all                    # Deny everything else
```

### ✅ Verify Auentication is Functioning

You can use below command

```bash
/usr/lib/squid/basic_ncsa_auth /etc/squid/htpasswd
```

And then you type in the "username password" as input to verify successful autentication when it returns 'OK'.

# 🛠️ 4th Step: Reboot Squid Service and Make Sure that Port 3128 and 8080 are Exposed


To reboot the Squid service and ensure that ports **3128** and **8080** are exposed and listening properly, follow these steps:

---

### 🔁 1. Reboot the Squid Service

Use `systemctl` to restart Squid:

```bash
sudo systemctl restart squid
```

Then verify its status:

```bash
sudo systemctl status squid
```

You should see `active (running)` in green.

---

### 🔓 2. Open Firewall Ports 

If you use `ufw` (Ubuntu):

```bash
sudo ufw allow 3128/tcp
sudo ufw allow 8080/tcp
```

For `firewalld` (CentOS/Fedora):

```bash
sudo firewall-cmd --add-port=3128/tcp --permanent
sudo firewall-cmd --add-port=8080/tcp --permanent
sudo firewall-cmd --reload
```
