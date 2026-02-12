🛡️ Kube-Guardian: AI-Powered Kubernetes Security Auditor
* **Kube-Guardian** is an agentic framework designed to bridge the gap between AI-driven manifest generation and production-grade security standards.
Built as part of the **GitHub Copilot CLI Challenge,** it uses the reasoning capabilities of the Copilot CLI to generate manifests which are then
instantly audited by a custom Python security engine.

🚀 The Mission
In modern **DevOps,** velocity often comes at the cost of security. Developers use AI to quickly generate Kubernetes YAML, but these manifests can
sometimes include "risky" defaults like privileged mode or missing resource limits.

**Kube-Guardian** solves this by enforcing a "Trust but Verify" workflow:

  1. **AI Reasoning:** Use the GitHub Copilot CLI to generate manifests based on high-level security scenarios.

  2. **Automated Auditing:** Instantly scan the generated YAML for critical security vulnerabilities.

  3. **Audit Reporting:** Provide clear ✅ **PASSED** or ❌ **FAILED** status for every deployment.

🛠️ Tech Stack
*  **AI Engine:** GitHub Copilot CLI (gh copilot)

*  **Core Logic:** Python 3.13

*  **Parsing:** PyYAML

*  **Terminal:** Git Bash on Windows

📋 Security Scenarios

The tool includes a guardian_library.json with pre-defined security archetypes:

* **web_app_secure:** Hardened Nginx deployment with non-root users and resource limits.

* **database_risky:** High-performance database requirements that often trigger security warnings (privileged mode, hostPath).

🚦 Security Checks

Every manifest is audited against three critical production gates:

* **Privileged Mode:** Ensures privileged: false to prevent container escapes.

* **Resource Limits:** Verifies CPU and Memory limits are defined to prevent DoS.

* **Run as Non-Root:** Ensures the container does not execute with root privileges.

💻 Usage

 **1. Generate a Manifest**
   Ask the AI to reason through a security scenario:
```text
python kube_guardian.py web_app_secure
```
 **2. Audit the Result**
   Run the guardian auditor against the generated YAML:
```text
python manifest_auditor.py nginx-deployment.yaml
```

📊 Proof of Concept

✅ **The Secure Path (Nginx)**

When generating a "Secure" manifest, the AI correctly identifies the need for resource limits and non-root execution.
**Result:** nginx: No Privileged Mode -> ✅ PASSED

❌ **The Risky Path (Postgres)**

When prompted for a high-performance DB requiring hostPath, the auditor correctly flags the resulting security vulnerabilities.
**Result:** postgres: No Privileged Mode -> ❌ FAILED

🏗️ Architecture Insight

This project demonstrates the power of using AI as a **Reasoning Engine** within a programmatic wrapper.
By handling the CLI's interactive syntax hurdles (like the -i "suggest -p ..." wrapper), Kube-Guardian
provides a seamless, secure bridge between a developer's intent and a safe cloud environment.
