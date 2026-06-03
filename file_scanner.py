import os #gives access to operating system features.
import hashlib #provides cryptographic hashing functions
import json #Used to store and read structured data (dictionary format)
from datetime import datetime

BASELINE_FILE = "baseline_hashes.json"


# ---------------- HASH FUNCTION ----------------
def get_file_hash(file_path):
    sha256 = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            while chunk := f.read(8192):
                sha256.update(chunk)
        return sha256.hexdigest()
    except Exception:
        return None


# ---------------- SCAN DIRECTORY ----------------
def scan_directory(target_folder):
    file_hashes = {}

    for root, _, files in os.walk(target_folder):
        for name in files:
            path = os.path.join(root, name)
            file_hash = get_file_hash(path)
            if file_hash:
                file_hashes[path] = file_hash

    return file_hashes


# ---------------- SAVE BASELINE ----------------
def save_baseline(data):
    with open(BASELINE_FILE, "w") as f:
        json.dump(data, f, indent=4)


# ---------------- LOAD BASELINE ----------------
def load_baseline():
    if not os.path.exists(BASELINE_FILE):
        return None

    with open(BASELINE_FILE, "r") as f:
        return json.load(f)


# ---------------- COMPARE STATES ----------------
def compare(baseline, current):
    baseline_files = set(baseline.keys())
    current_files = set(current.keys())

    added = current_files - baseline_files
    deleted = baseline_files - current_files
    common = baseline_files & current_files

    modified = [
        f for f in common if baseline[f] != current[f]
    ]

    return added, deleted, modified


# ---------------- REPORT ----------------
def report_changes(added, deleted, modified):
    print("\n===== FILE INTEGRITY REPORT =====")
    print("Time:", datetime.now())
    print("----------------------------------")

    if added:
        print("\n🟢 Added Files:")
        for f in added:
            print(" +", f)

    if deleted:
        print("\n🔴 Deleted Files:")
        for f in deleted:
            print(" -", f)

    if modified:
        print("\n🟠 Modified Files:")
        for f in modified:
            print(" *", f)

    if not (added or deleted or modified):
        print("\n✅ No changes detected. System is clean.")


# ---------------- MAIN ----------------
def main():
    folder = input("Enter folder path to monitor: ").strip()

    current_snapshot = scan_directory(folder)
    baseline = load_baseline()

    # First run → create baseline
    if baseline is None:
        save_baseline(current_snapshot)
        print("\nBaseline created. Run again to detect changes.")
        return

    added, deleted, modified = compare(baseline, current_snapshot)
    report_changes(added, deleted, modified)

    # Update baseline after scan
    save_baseline(current_snapshot)


if __name__ == "__main__":
    main()