from conans import ConanFile


class CPPZMQConan(ConanFile):
    name = "cppzmq"
    version = "4.2.0"
    sha1 = "6c9103433f978e2c190c806a98c53f5cee4744f9"  # For 4.2.0
    url = "https://github.com/memsharded/conan-zmqcpp.git"
    requires = "libzmq/4.2.0@memsharded/stable"
    source_dir = "cppzmq"

    def source(self):
        self.run_command("git clone https://github.com/zeromq/cppzmq.git")
        self.run_command("git checkout -b %s.x %s" % (self.version, self.sha1), self.source_dir)

    def run_command(self, cmd, cwd=None):
        self.output.info(cmd)
        self.run(cmd, True, cwd)

    def package(self):
        self.copy("*.hpp", dst="include", src="%s" % self.source_dir)

    def package_info(self):
        self.cpp_info.libdirs = []
