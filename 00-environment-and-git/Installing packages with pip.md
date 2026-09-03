# How to install packages with pip

First, we need to ensure we have it downloaded, so we use =

```powershell
python -m pip --version
```

If not, we can enable it by doing = 

```powershell
python -m ensurepip --default-pip
```

We then create an isolated environment =

```powershell
python -m venv venv
```

We activate the isolated environment =

```powershell
venv\Scripts\activate
```

Finally, we install the packages with, here's  an example =

```powershell
pip  install typer python-dateutil rich
```