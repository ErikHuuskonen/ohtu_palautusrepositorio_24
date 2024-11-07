class Project:
    def __init__(self, name, description, dependencies, dev_dependencies, license_dev, authors):
        self.name = name
        self.description = description
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies
        self.license = license_dev
        self.authors = authors

    def _stringify_dependencies(self, dependencies):
        return ", ".join(dependencies) if len(dependencies) > 0 else "-"

    def __str__(self):
            result = f"Name: {self.name}\nDescription: {self.description}\n"
            if self.license:
                result += f"License: {self.license}\n"
            if self.authors:
                result += "\nAuthors:\n" + "\n".join(f"- {author}" for author in self.authors) + "\n"
            result += "\nDependencies:\n" + "\n".join(f"- {dep}" for dep in self.dependencies) + "\n"
            result += "\nDevelopment dependencies:\n" + "\n".join(f"- {dev_dep}" for dev_dep in self.dev_dependencies) + "\n"
            return result