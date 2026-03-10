# x264 QP Feature Analysis

Python automation script for analyzing the **QP (Quantization
Parameter)** feature of the x264 encoder.

The script runs the encoder using **QP values from 1 to 51** on an
uncompressed `.yuv` video and generates reports demonstrating how QP
affects compression efficiency.

Results are exported as:

-   📊 **CSV spreadsheet**
-   📈 **Charts**
-   📁 Encoded `.264` bitstreams for each QP value

------------------------------------------------------------------------

# What This Project Demonstrates

This project shows how **encoder parameters affect compression
behavior**.

The generated reports illustrate:

-   QP vs **encoded file size**
-   QP vs **encoding time**

Typical behavior:

    Lower QP  → Higher quality → Larger file size
    Higher QP → Lower quality → Smaller file size

------------------------------------------------------------------------

# Project Structure

    x264-qp-analysis/
    │
    ├── qp_analysis.py
    ├── foreman-cif.yuv
    ├── requirements.txt
    ├── README.md
    │
    ├── qp_outputs/
    │   ├── qp_1.264
    │   ├── qp_2.264
    │   └── ...
    │
    ├── qp_results.csv
    ├── qp_vs_filesize.png
    └── qp_vs_time.png

------------------------------------------------------------------------

# Requirements

-   Python **3.8+**
-   x264 video encoder
-   Python dependencies listed in:

```{=html}
<!-- -->
```
    requirements.txt

Supported platforms:

-   macOS
-   Windows

------------------------------------------------------------------------

# Installing x264

## macOS

Install using Homebrew:

``` bash
brew install x264
```

Verify installation:

``` bash
x264 --version
```

------------------------------------------------------------------------

## Windows

1.  Download a prebuilt binary from a trusted source.
2.  Extract the archive.
3.  Add the folder containing `x264.exe` to your **PATH** environment
    variable.

Verify installation:

    x264 --version

------------------------------------------------------------------------

# Setting Up Python Virtual Environment

Using a virtual environment keeps project dependencies isolated.

------------------------------------------------------------------------

## macOS / Linux

### Create virtual environment

``` bash
python3 -m venv venv
```

### Activate environment

``` bash
source venv/bin/activate
```

Your terminal should now show:

    (venv)

### Install project dependencies

``` bash
pip install -r requirements.txt
```

------------------------------------------------------------------------

## Windows

### Create virtual environment

    python -m venv venv

### Activate environment

Command Prompt:

    venv\Scripts\activate

PowerShell:

    venv\Scripts\Activate.ps1

After activation you should see:

    (venv)

### Install project dependencies

    pip install -r requirements.txt

------------------------------------------------------------------------

# Input Video

The script requires an **uncompressed YUV video file**.

Example:

    foreman-cif.yuv

Resolution must match the value defined in the script:

    352x288

------------------------------------------------------------------------

# Running the Analysis

Run the script from the project directory while the virtual environment
is active.

macOS / Linux:

``` bash
python qp_analysis.py
```

Windows:

    python qp_analysis.py

------------------------------------------------------------------------

# What the Script Does

The script automatically:

1.  Runs the encoder with **QP values from 1 to 51**
2.  Generates encoded `.264` files
3.  Measures encoding metrics
4.  Creates charts and reports

------------------------------------------------------------------------

# Generated Reports

### CSV Report

    qp_results.csv

Example output:

  QP   FileSize_KB   EncodeTime_s
  ---- ------------- --------------
  1    12500         1.42
  10   6400          1.31
  25   2300          1.18
  40   900           1.05
  51   450           0.98

------------------------------------------------------------------------

### Chart: QP vs File Size

    qp_vs_filesize.png

Illustrates how compression changes with QP.

Expected trend:

    QP ↑  →  File Size ↓

------------------------------------------------------------------------

### Chart: QP vs Encoding Time

    qp_vs_time.png

Shows how the quantization parameter influences encoding runtime.

------------------------------------------------------------------------

# Example x264 Command Used

For each QP value the script executes:

    x264 --qp <value> --input-res 352x288 -o qp_<value>.264 foreman-cif.yuv

Example:

    x264 --qp 25 --input-res 352x288 -o qp_25.264 foreman-cif.yuv

------------------------------------------------------------------------

# Deactivating the Virtual Environment

When you finish working:

    deactivate

------------------------------------------------------------------------

# Possible Future Improvements

Potential extensions of this project:

-   PSNR analysis
-   SSIM quality metrics
-   Rate--distortion (RD) curves
-   Bitrate extraction from encoder logs
-   Parallel encoding
-   Excel report generation
-   Command line arguments for input file and resolution

------------------------------------------------------------------------

# License

MIT License
