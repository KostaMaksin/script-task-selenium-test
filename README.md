# Please note before proceeding

In your editor, here VS Code is used, open as folder only the 
individual folder of each task, not the repo root as this might 
cause trouble with paths, modules and running the tests.

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

    script-task-selenium-test/
    │
    ├── script-task/
    │    ├── test_data
    │    ├── qp_outputs
    │    ├── qp_results
    │    ├── venv
    │    ├── ChatGPT_transcript.txt
    │    ├── requirements.txt
    │    └── script_task_qp_analysis.py

------------------------------------------------------------------------

# Requirements

-   Python **3.8+**
-   x264 video encoder
-   Python dependencies listed in:

```{=html}
requirements.txt
```
    
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
python script_task_qp_analysis.py
```

Windows:

    python script_task_qp_analysis.py

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

# JPEGmini UI Automation Tests

Selenium + Python UI automation solution for the JPEGmini **Compress Videos** flow, implemented with the **Page Object Model (POM)**.

## Covered flow

1. Open the JPEGmini homepage
2. Click **Compress Videos**
3. Upload a video file
4. Wait for compression to finish
5. Assert on the UI that the output size is smaller than the original size, and print the reduction
6. Click **Download the video**
7. Wait for the file to download
8. Compare the downloaded file size against the original file size

## Project structure

```text
selenium-test/
├── downloads/
├── pages/
│   ├── __init__.py
│   ├── base_page.py
│   ├── compress_page.py
│   └── home_page.py
├── test_data/
│   └── file_example_MP4_640_3MG.mp4
├── tests/
│   ├── __init__.py
│   └── test_video_compression.py
├── utils/
│   ├── __init__.py
│   ├── driver_factory.py
│   └── file_utils.py
├── pytest.ini
└── requirements.txt
```

## Requirements

- Python 3.11 or 3.12 recommended
- Google Chrome installed
- Internet connection
- A test video in `test_data/file_example_MP4_640_3MG.mp4`

## Installation

### macOS

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Run the test:

```bash
pytest -s -v
```

### Windows

Create and activate a virtual environment:

```powershell
python -m venv venv
venv\Scripts\activate
```

Install dependencies:

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Run the test:

```powershell
pytest -s -v
```

## Notes

- `-s` shows printed debug information such as UI sizes and final file sizes.
- Downloads are saved to the local `downloads/` folder.
- Temporary Chrome files like `.crdownload` and hidden temp files are ignored by the download wait logic.
- The framework uses Selenium Manager, so no separate ChromeDriver installation is required.

## How the framework is structured

### Page Object Model rules followed

- `pages/` contains only page locators and UI actions
- `tests/` contains assertions and test flow
- `utils/` contains reusable support code such as driver setup and file handling

### Main page objects

- `HomePage` opens the site and clicks the **Compress Videos** entry point
- `CompressPage` uploads the file, reads UI size values, waits for compression, and downloads the optimized file

## Test data

Place your input video here:

```text
test_data/file_example_MP4_640_3MG.mp4
```

Use a video that has not already been optimized.

## Known practical note

During debugging, directly opening `https://jpegmini.com/compress-videos` can help isolate upload behavior. For the final flow, the test uses the homepage and clicks **Compress Videos** to match the assignment.

## Expected output

When the test runs successfully, it prints values similar to:

```text
Original UI size: 2.9 MB
Output UI size: 0.9 MB
UI reduction bytes: ...
UI reduction percent: 68.97%
Original size bytes: ...
Downloaded size bytes: ...
```

## Troubleshooting

### VS Code shows missing imports even though packages are installed

Make sure VS Code is using the interpreter from your project virtual environment.

### `ModuleNotFoundError: No module named 'pages'`

Ensure these files exist:

```text
pages/__init__.py
tests/__init__.py
utils/__init__.py
```

Also run pytest from the project root.

### Chrome opens but the test fails before interaction

Check that:
- Chrome is installed
- your video file exists at `test_data/file_example_MP4_640_3MG.mp4`
- the page locators still match the current site HTML

## Dependencies

Example `requirements.txt`:

```text
selenium
pytest
```

------------------------------------------------------------------------

# License

MIT License


