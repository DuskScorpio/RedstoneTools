from pathlib import Path
from ruamel.yaml import YAML
from utils.constant import *

import re
import os


def main():
    index_dir = Path("../.index")
    if not index_dir.exists() or not index_dir.is_dir():
        return

    files = [f.name for f in index_dir.iterdir() if f.is_file()]
    mod_ids = [f.replace(".pw.toml", "") for f in files if re.match(".*\\.pw\\.toml", f)]
    yaml = YAML()
    yaml.indent(mapping=2, sequence=4, offset=2)
    yaml.preserve_quotes = True
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        data = dict(yaml.load(f))

    enabled_mods: list[dict[str, str]] = data.get(ENABLED, []).copy()
    disabled_mods: list[dict[str, str]] = data.get(DISABLED, []).copy()
    new_mods = []
    for mod_id in sorted(mod_ids):
        enabled_slugs = [i[MR] for i in enabled_mods if MR in i]
        disabled_slug = [i[MR] for i in disabled_mods if MR in i]
        if mod_id not in enabled_slugs and mod_id not in disabled_slug:
            new_mods.append({MR: mod_id})
    data[ENABLED].extend(new_mods)

    if new_mods:
        comment = data[ENABLED]
        comment.yaml_set_comment_before_after_key(enabled_mods.__len__(), "\n======NEW MODS======")

    # save
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        yaml.dump(data, f)


if __name__ == "__main__":
    script_dir = Path(__file__).resolve().parent
    os.chdir(script_dir)
    main()