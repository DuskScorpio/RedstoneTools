from pathlib import Path
from ruamel.yaml import YAML
from ruamel.yaml.comments import CommentedMap

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
        for i in data:
            if data[i] is None:
                data[i] = {}

    mods = data["mods"]
    disable_mods = data["disable_mods"]
    new_mods = {mod: "*" for mod in mod_ids if mod not in mods and mod not in disable_mods}
    data["mods"].update(dict(sorted(new_mods.items())))

    # add comment
    comment = data["mods"]
    if isinstance(comment, CommentedMap) and len(new_mods) != 0:
        comment.yaml_set_comment_before_after_key(list(new_mods)[0], "\n======NEW MODS======")

    # save
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        yaml.dump(data, f)


if __name__ == "__main__":
    main()