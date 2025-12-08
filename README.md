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
source .env
uv run -m src.app.convertor.service.transcription
```

``` bash
uv run flask --app src.app.main run --debug
```

### Important

Running from the project root ensures that relative paths like
`data/inputs/...` resolve correctly.

The .env file contains the python path (PYTHONPATH):

``` bash
export PYTHONPATH=$(pwd)/src
```
 Which ensures the project root is in the PYTHONPATH, so  python can find the project modules. For this project "src"  should be treated as the root of the package.

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

## 🚀   Docker


1. Create an image from the Dockerfile

``` bash
docker build -t myflaskapp .
```
2. Create, start and attach a Docker Container

``` bash
docker run -t myflaskapp .
```

3. To access Flask from localhost

Flask must listen on all interfaces, not just localhost, or it will be unreachable from your machine. The local cmd

``` bash
CMD ["uv", "run", "flask", "--app", "src.app.main", "run"] ❌ Required change: Add host
CMD ["uv", "run", "flask", "--app", "src.app.main", "run", "--host=0.0.0.0", "--port=5000"]

```

Then run the container, and access Flask using Port Binding
``` bash
docker run --rm -p <host_port>:<conteiner_port> myflaskapp

docker run --rm -p 5001:5000 myflaskapp
``` 

Now in the local browser we can access our running flask application at:

[text](http://localhost:5004/)

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

## 🚀   Run with docker-compose

``` bash
1 - docker-compose up --force-recreate --build -d (only first time)
2-  docker exec -it talk2text  bash
3 - uv run flask --app src.app.main run --debug
```
