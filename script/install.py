from pathlib import Path
from ruamel.yaml import YAML
from subprocess import run
from semantic_version import Version, SimpleSpec


FILE_PATH = "../mod_list.yml"


# install mods
def main():
    yaml = YAML()
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        data = yaml.load(f)
    mods_dict: dict = data["mods"]
    minecraft_versions = [f.name for f in list(Path("../").glob("*/")) if f.joinpath("pack.toml").exists()]
    for minecraft_version in minecraft_versions:
        path = "../{}".format(minecraft_version)
        for mod in mods_dict:
            condition = SimpleSpec(mods_dict[mod])
            mc_semver = Version(minecraft_version)
            if condition.match(mc_semver):
                run(["../tools/packwiz", "mr", "add", mod, "--yes"], cwd=path)


if __name__ == "__main__":
    main()