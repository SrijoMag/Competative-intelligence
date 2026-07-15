import subprocess
import os
import sys
import time

BASE = os.path.dirname(os.path.abspath(__file__))

print("="*70)
print("        WEEK 6 STRATEGIC RECOMMENDATION ENGINE")
print("="*70)

start = time.time()


def run(script):

    path = os.path.join(BASE, script)

    print(f"\nRunning {script}...\n")

    result = subprocess.run(
        [sys.executable, path]
    )

    if result.returncode != 0:
        print(f"{script} Failed.")
        exit()

    print(f"{script} Completed Successfully.")


run("recommendation_engine.py")
run("visualization.py")
run("executive_report.py")

end = time.time()

print("\n")
print("="*70)
print("Week 6 Completed Successfully")
print("="*70)

print(f"Execution Time : {round(end-start,2)} seconds")