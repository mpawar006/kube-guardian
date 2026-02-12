import subprocess
import json
import sys

def generate_manifest(scenario_key):
    with open('guardian_library.json', 'r') as f:
        library = json.load(f)
    
    prompt = library['scenarios'].get(scenario_key)
    if not prompt:
        print("Scenario not found.")
        return

    print(f"🤖 Kube-Guardian is reasoning: {scenario_key}")
    
    # The CLI now requires the 'suggest' command to be passed as a string
    # We use single quotes for the outer string and double quotes for the inner prompt
    cmd = f'gh copilot -i "suggest -p \'{prompt}\'"'
    
    try:
        subprocess.run(cmd, shell=True)
    except Exception as e:
        print(f"❌ Execution Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        generate_manifest(sys.argv[1])
    else:
        print("Usage: python kube_guardian.py <scenario_key>")
