from urllib import request
from project import Project
import tomlkit


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        toml_data = tomlkit.parse(content)

        # Haetaan tarvittavat tiedot TOML-datasta
        name = toml_data["tool"]["poetry"]["name"]
        description = toml_data["tool"]["poetry"]["description"]
        dependencies = list(toml_data["tool"]["poetry"]["dependencies"].keys())
        license_dev = toml_data["tool"]["poetry"].get("license", "No license specified")
        authors = toml_data["tool"]["poetry"].get("authors", [])
        # Tarkistetaan, löytyykö 'dev-dependencies' 'group.dev.dependencies' -kohdasta
        dev_dependencies = list(toml_data["tool"]["poetry"].get("group", {}).get("dev", {}).get("dependencies", {}).keys())

        # Muodosta Project-olio ja palauta se
        return Project(name, description, dependencies, dev_dependencies, license_dev, authors)
