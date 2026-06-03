PowerShell instructions to run the Python helper scripts

1) Open PowerShell in the project root (`C:\Root\Projects\RickMaxwell23`).

2) (Optional) Allow running the activation script for this session:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
```

3) Activate the project's virtual environment (if you have one):

```powershell
& .\.venv\Scripts\Activate.ps1
# or if you don't have a venv, use the system python: py -3
```

4) Run the helper script:

```powershell
python .\scripts\inspect_images.py
# or
py -3 .\scripts\inspect_images.py
```

If PowerShell complains about syntax when pasting multiline Python code, don't paste Python into PowerShell; save it into a `.py` file and run it with `python` as shown above.
