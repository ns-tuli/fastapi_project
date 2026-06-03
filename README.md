# fastapi_project

## Setup

Create a Python virtual environment

```powershell
python -m venv myenv
```

Activate the environment:

```powershell
myenv\Scripts\Activate.ps1
```

Install the dependencies from `requirements.txt`:

```powershell
pip install -r requirements.txt
```

## Run

After activating the virtual environment and installing requirements, start the app with:

```powershell
uvicorn src.main:app --reload
```
