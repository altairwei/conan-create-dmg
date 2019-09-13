import os
from conans import ConanFile, tools

class CreateDmgConan(ConanFile):
    name = "create-dmg"
    version = "1.0.0.5"
    license = "MIT"
    url = "https://github.com/altairwei/conan-create-dmg.git"
    homepage = "https://github.com/andreyvit/create-dmg"
    settings = "os_build"
    description = "A shell script to build fancy DMGs."
    _source_subfolder = "source_subfolder"

    def configure(self):
        if self.settings.os_build != "Macos":
            raise Exception("Only MacOS supported for create-dmg")

    def build(self):
        url = "https://github.com/andreyvit/create-dmg/archive/v%s.zip" % self.version
        tools.get(url)
        os.rename("create-dmg-" + self.version, self._source_subfolder)

    def package(self):
        self.copy("create-dmg", dst="bin", src=self._source_subfolder, keep_path=True)
        self.copy("support/*", dst="bin", src=self._source_subfolder, keep_path=True)

    def package_info(self):
        self.output.info("Using create-dmg %s" % self.version)
        self.env_info.path.append(os.path.join(self.package_folder, "bin"))
