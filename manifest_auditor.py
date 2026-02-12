import yaml
import sys

def audit_manifest(file_path):
    print(f"🛡️ Auditing K8s Manifest: {file_path}")
    
    with open(file_path, 'r') as f:
        # Load all documents in the YAML file
        docs = yaml.load_all(f, Loader=yaml.SafeLoader)
        
        results = []
        for doc in docs:
            if not doc or doc.get('kind') != 'Deployment':
                continue
                
            containers = doc['spec']['template']['spec']['containers']
            for c in containers:
                name = c.get('name')
                sec_ctx = c.get('securityContext', {})
                res_limits = c.get('resources', {}).get('limits', {})

                # Check 1: Privileged Mode
                privileged = sec_ctx.get('privileged', False)
                results.append({"check": f"{name}: No Privileged Mode", "passed": not privileged})

                # Check 2: Resource Limits
                has_limits = "cpu" in res_limits and "memory" in res_limits
                results.append({"check": f"{name}: Resource Limits Defined", "passed": has_limits})

                # Check 3: Run as Non-Root
                non_root = sec_ctx.get('runAsNonRoot', False)
                results.append({"check": f"{name}: Run as Non-Root", "passed": non_root})

    print("\n--- Audit Results ---")
    for r in results:
        status = "✅ PASSED" if r['passed'] else "❌ FAILED"
        print(f"{r['check']} -> {status}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        audit_manifest(sys.argv[1])
