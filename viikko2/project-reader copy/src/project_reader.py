from urllib import request
from project import Project
import tomlkit  # lisää tämä kirjaston käyttöä varten

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # Tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        print("TOML Content:\n", content)  # Debug: tulostetaan tiedoston sisältö

        # Deserialisoi TOML-tiedosto ja muunnetaan se Pythonin tietorakenteeksi
        toml_data = tomlkit.parse(content)
        print("Parsed Data:\n", toml_data)  # Debug: tulostetaan parsittu data

        # Poimi tarvittavat tiedot
        name = toml_data["tool"]["poetry"]["name"]
        description = toml_data["tool"]["poetry"].get("description", "No description")
        license_info = toml_data["tool"]["poetry"].get("license", "No license")

        # Muodosta riippuvuuslistat
        dependencies = list(toml_data["tool"]["poetry"]["dependencies"].keys())
        dev_dependencies = list(toml_data["tool"]["poetry"]["dev-dependencies"].keys())

        # Hanki kirjoittajien tiedot, jos olemassa
        authors = toml_data["tool"]["poetry"].get("authors", [])

        # Luo ja palauta Project-olio
        return Project(name, description, license_info, authors, dependencies, dev_dependencies)
