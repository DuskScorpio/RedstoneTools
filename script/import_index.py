from pathlib import Path
from ruamel.yaml import YAML

import re


FILE_PATH = "../mod_list.yml"

def main():
    index_dir = Path("../.index")
    if not index_dir.exists() or not index_dir.is_dir():
        return

    files = [f.name for f in index_dir.iterdir() if f.is_file()]
    mod_ids = [f.replace(".pw.toml", "") for f in files if re.match(".*\\.pw\\.toml", f)]
    yaml = YAML()
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        data = yaml.load(f)

    try:
        mods = dict(data["mods"]).copy()
    except TypeError:
        data = {"mods": {}}
        mods = dict(data["mods"]).copy()

    for mod_id in mod_ids:
        mods.setdefault(mod_id, "*")
    data["mods"] = dict(sorted(mods.items()))
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        yaml.dump(data, f)


if __name__ == "__main__":
    main()