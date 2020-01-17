
from conans import ConanFile

class Meta(ConanFile):
  name = "nano"
  settings = "os", "arch", "compiler"
  version = "1.0"

  requires = (
    "ffmpeg/1.0",
  )

  default_options = {"ffmpeg:variation": "nano"}
