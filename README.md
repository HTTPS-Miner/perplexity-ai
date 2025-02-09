### English Version - README.md

# Selenium Browser Automation for perplexity.ai

## Overview

This project automates interactions with perplexity-ai on the [perplexity.ai](https://perplexity.ai/) website using **selenium** and **Firefox**. The script allows you to send text input from a file, receive the response from ChatGPT, and save it to an output file — all without manually opening a browser.

https://github.com/user-attachments/assets/98b8be66-8835-4a26-a008-10367a0e8ec1

## Requirements

**Tested in Python 3.11.2 on linux**

To get started, you'll need to install the following Python packages:

```
pip install selenium beautifulsoup4 markdownify
```

## Workflow

1. **Input File**: Create a file called `prompt.txt` and write your message to ChatGPT.
2. **Output File**: The response from ChatGPT will be saved in the `response_to_markdown/output.md` file.

## Software Support

- Crossplatform - Windows, Linux

## Purpose

The primary goal of this tool is to streamline and automate interactions with perplexity-ai, making it faster and more efficient.

## Installation and Usage

### Terminal Commands

1. Clone the repository:
   ```shell
   git clone https://github.com/HTTPS-Miner/perplexity-ai
   cd perplexity-ai
   ```

2. Create a virtual environment:
   ```shell
   python3 -m venv myenv
   source myenv/bin/activate
   ```

3. Install the required dependencies:
   ```shell
   pip install selenium beautifulsoup4 markdownify
   ```

4. Create a `prompt.txt` file in the current directory and write the message you want to send to ChatGPT.

5. To run the tool:
   ```shell
   python3 main.py
   ```

If you want to avoid opening the browser window, simply uncomment line 13 in main.py to perform the operation without opening the browser.

## For Windows

```
py -m venv myenv
myenv\Scripts\activate.bat
```

Update Firefox path:

Open main.py and modify line 11 to set the correct path for Firefox:
Example:

```
options.binary_location = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
```