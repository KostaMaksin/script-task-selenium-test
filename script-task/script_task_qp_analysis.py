import subprocess
import os
import time
import shutil
import pandas as pd
import matplotlib
from pathlib import Path

# Prevent GUI issues on macOS
matplotlib.use("Agg")
import matplotlib.pyplot as plt


# ----------------------
# USER CONFIGURATION
# ----------------------

current_file_dir = os.path.dirname(os.path.abspath(__file__))

INPUT_YUV = os.path.join(current_file_dir, "test_data/foreman-cif.yuv")
WIDTH = 352
HEIGHT = 288
OUTPUT_DIR = os.path.join(current_file_dir, "qp_outputs")
RESULT_DIR = os.path.join(current_file_dir, "qp_results")
RESULT_CSV = os.path.join(RESULT_DIR, "qp_results.csv")

QP_VALUES = range(1, 52)


# ----------------------
# CHECK DEPENDENCIES
# ----------------------

if shutil.which("x264") is None:
    raise RuntimeError(
        "x264 encoder not found. Install it with: brew install x264"
    )


# ----------------------
# PREPARE OUTPUT
# ----------------------

os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(RESULT_DIR, exist_ok=True)

results = []


# ----------------------
# RUN ENCODING
# ----------------------

for qp in QP_VALUES:

    output_file = os.path.join(OUTPUT_DIR, f"qp_{qp}.264")

    cmd = [
        "x264",
        "--qp", str(qp),
        "--input-res", f"{WIDTH}x{HEIGHT}",
        "-o", output_file,
        INPUT_YUV
    ]

    print(f"Encoding with QP={qp}")

    start_time = time.time()

    process = subprocess.run(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    end_time = time.time()
    encode_time = end_time - start_time

    if not os.path.exists(output_file):
        print(f"Encoding failed for QP={qp}")
        print(process.stderr)
        continue

    file_size_kb = os.path.getsize(output_file) / 1024

    results.append({
        "QP": qp,
        "FileSize_KB": file_size_kb,
        "EncodeTime_s": encode_time
    })


# ----------------------
# CREATE SPREADSHEET
# ----------------------

df = pd.DataFrame(results)
df.to_csv(RESULT_CSV, index=False)

print(f"\nCSV report created: {RESULT_CSV}")


# ----------------------
# CHART 1: QP vs File Size
# ----------------------

plt.figure()

plt.plot(df["QP"], df["FileSize_KB"], marker="o")

plt.xlabel("QP")
plt.ylabel("File Size (KB)")
plt.title("Effect of QP on Encoded File Size")

plt.grid(True)

plt.savefig(os.path.join(RESULT_DIR, "qp_vs_filesize.png"))


# ----------------------
# CHART 2: QP vs Encoding Time
# ----------------------

plt.figure()

plt.plot(df["QP"], df["EncodeTime_s"], marker="o")

plt.xlabel("QP")
plt.ylabel("Encoding Time (s)")
plt.title("Effect of QP on Encoding Time")

plt.grid(True)

plt.savefig(os.path.join(RESULT_DIR, "qp_vs_time.png"))

print("Charts generated:")
print(" - qp_vs_filesize.png")
print(" - qp_vs_time.png")


# ----------------------
# TERMINAL SUMMARY
# ----------------------

print("\nSummary statistics:")
print(df.describe())