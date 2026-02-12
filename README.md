# 🛡️ Kube-Guardian  
## AI-Powered Kubernetes Security Auditor

**Kube-Guardian** is an agentic security framework designed to bridge the gap between AI-generated Kubernetes manifests and production-grade security standards.

Built as part of the **GitHub Copilot CLI Challenge**, it leverages the reasoning capabilities of GitHub Copilot CLI to generate Kubernetes manifests, which are then instantly audited by a custom Python-based security engine.

---

## 🚀 The Mission

In modern **DevOps**, speed often comes at the cost of security.

Developers increasingly rely on AI tools to generate Kubernetes YAML files — but these manifests may include risky defaults such as:

- Privileged containers  
- Missing CPU/Memory resource limits  
- Root-level execution  

### 🔐 Kube-Guardian enforces a **"Trust but Verify"** workflow:

1. **AI Reasoning**  
   Use GitHub Copilot CLI to generate manifests from high-level security scenarios.

2. **Automated Auditing**  
   Instantly scan the generated YAML files for critical vulnerabilities.

3. **Audit Reporting**  
   Provide clear, production-ready validation:
   - ✅ **PASSED**
   - ❌ **FAILED**

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| **AI Engine** | GitHub Copilot CLI (`gh copilot`) |
| **Core Logic** | Python 3.13 |
| **YAML Parsing** | PyYAML |
| **Terminal Environment** | Git Bash (Windows) |

---

## 📋 Security Scenarios

The project includes a `guardian_library.json` file containing predefined security archetypes:

### 🔹 `web_app_secure`
- Hardened Nginx deployment  
- Non-root execution  
- Resource limits enforced  

### 🔹 `database_risky`
- High-performance database scenario  
- May trigger warnings:
  - Privileged mode  
  - `hostPath` usage  

---

## 🚦 Security Checks

Every generated manifest is validated against three critical production gates:

### 1️⃣ Privileged Mode Check  
Ensures:
```yaml
privileged: false
```
Prevents container escape vulnerabilities.

---

### 2️⃣ Resource Limits Check  
Verifies CPU and memory limits are defined:
```yaml
resources:
  limits:
    cpu: "500m"
    memory: "512Mi"
```
Prevents resource exhaustion and DoS risks.

---

### 3️⃣ Run as Non-Root Check  
Ensures containers do not execute with root privileges:
```yaml
securityContext:
  runAsNonRoot: true
```

---

## 💻 Usage

### 🔹 Step 1: Generate a Manifest

```bash
python kube_guardian.py web_app_secure
```

### 🔹 Step 2: Audit the Generated Manifest

```bash
python manifest_auditor.py nginx-deployment.yaml
```

---

## 📊 Proof of Concept

### ✅ Secure Path (Nginx)

When generating a secure manifest:

- Resource limits are correctly defined  
- Non-root execution is enforced  
- No privileged mode enabled  

**Result:**
```
nginx: No Privileged Mode → ✅ PASSED
```

---

### ❌ Risky Path (Postgres)

When generating a high-performance database manifest with `hostPath`:

- Privileged mode may be enabled  
- Security best practices violated  

**Result:**
```
postgres: No Privileged Mode → ❌ FAILED
```

---

## 🏗️ Architecture Insight

Kube-Guardian demonstrates how AI can act as a **Reasoning Engine** inside a controlled programmatic wrapper.

By handling Copilot CLI’s interactive syntax (e.g., `-i "suggest -p ..."`), the framework creates a seamless and secure bridge between:

- 🧠 Developer Intent  
- ⚙️ AI Manifest Generation  
- 🔒 Automated Security Enforcement  
- ☁️ Production-Ready Kubernetes Deployment  

---

## 🎯 Why Kube-Guardian?

✔ Bridges AI velocity with production security  
✔ Enforces Kubernetes best practices automatically  
✔ Demonstrates agentic AI workflow in DevSecOps  
✔ Ready-to-extend for enterprise policy enforcement  

---

### 👨‍💻 Built for DevSecOps Engineers Who Believe:

> “Speed is good. Secure speed is better.”

