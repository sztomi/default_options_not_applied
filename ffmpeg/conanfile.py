from conans import ConanFile


class FfmpegConan(ConanFile):
    name = "ffmpeg"
    version = "1.0"
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Ffmpeg here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")
    settings = "os", "compiler", "build_type", "arch"
    options = {"variation": ["standard", "nano"]}
    default_options = {"variation": "standard"}
    generators = "cmake"

    def requirements(self):
        variation = str(self.options.variation)
        print(f"(requirements) variation = {variation}")

    def source(self):
        variation = str(self.options.variation)
        print(f"(source) variation = {variation}")

    def build(self):
        variation = str(self.options.variation)
        print(f"(build) variation = {variation}")
        self.run("touch libavcodec.so")

    def package(self):
        variation = str(self.options.variation)
        print(f"(package) variation = {variation}")
        self.copy("*.so", dst="lib")

    def package_info(self):
        self.cpp_info.libs = ["ffmpeg"]
