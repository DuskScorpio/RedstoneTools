## Setting up (VS Code)

1. Run `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` in PowerShell as Admin
2. `Ctrl+Shift+P` > `Python: Create Environment` > `venv` in VS Code to setup virtual environment
3. Run `pip install -r script/requirements.txt` to install prerequisites

## Importing mod index

1. Place `.index` folder in the project root `RedstoneTools/`
2. Run `import_index.py` from `script/`
3. `mod_list.yml` will be generated in `RedstoneTools/`

## Installing mods

1. Create folders for each game version in project root
2. Run `../tools/packwiz init` within each version folder
3. Run `install.py` from `script/`
4. Removing mods from `mod_list.yml` will remove the mods from the version folders when `install.py` runs

## Testing modpack

1. Follow instructions from [this video](https://www.bilibili.com/video/BV1YQhyz5EHf) or [this guide](https://docs.yw-games.top/posts/tutorial/modpack/packwiz.html)
2. Run `../tools/packwiz server` within game version folder, e.g. `RedstoneTools/1.21.11`
