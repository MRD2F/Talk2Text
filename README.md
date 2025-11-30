# 🎧 Audio Transcription Service

A Python application that provides audio transcription using Whisper and
OpenAI models.\
The project is managed with **uv** (Ultrafast Python Package Manager).

------------------------------------------------------------------------

## 🚀 1. Installation

### **1.1. Clone the repository**

``` bash
git clone https://github.com/yourusername/yourrepo.git
cd yourrepo
```

### **1.2. Install uv (if not already installed)**

``` bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

---or via pip---

``` bash
pip install uv
```

### **1.3. Create and sync the environment**

uv uses `pyproject.toml` + `uv.lock` to reproduce the environment:

``` bash
uv sync
```

This automatically:

-   Creates a virtual environment (`.venv`)
-   Installs all dependencies
-   Pins exact versions from `uv.lock`

------------------------------------------------------------------------

## 🎤 2. Project Structure (relevant section)

    src/
     └── app/
         └── convertor/
             └── service/
                 └── transcription_service.py
    data/
     └── inputs/
         └── file.ogg

------------------------------------------------------------------------

## 🏃 3. Running the Transcription Script and Flask API

Run from the **root directory**:

``` bash
PYTHONPATH=src
uv run -m src.app.convertor.service.transcription
```

``` bash
uv run flask --app src.app.main run
```

### Important

Running from the project root ensures that relative paths like
`data/inputs/...` resolve correctly.


## 🧪 5. Running Tests (if applicable)

``` bash
uv run pytest
```

------------------------------------------------------------------------

## 🛠 6. Updating Dependencies

### Add a new package

``` bash
uv add <package-name>
```

### Upgrade all dependencies

``` bash
uv lock --upgrade
uv sync
```

------------------------------------------------------------------------

## ❗ Troubleshooting

### **FileNotFoundError for audio inputs**

Ensure the script is always run from the **project root**.

Correct:

``` bash
uv run src/app/convertor/service/transcription_service.py
```

Incorrect:

``` bash
cd src/app/convertor/service/
uv run transcription_service.py   # ❌ breaks relative paths
```

------------------------------------------------------------------------
