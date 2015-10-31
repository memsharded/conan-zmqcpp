from conans import ConanFile, CMake
import os


class ZMQCppTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    requires = "zmqcpp/4.1.1@memsharded/testing"
    generators = "cmake"

    def build(self):
        cmake = CMake(self.settings)
        self.run('cmake . %s' % cmake.command_line)
        self.run("cmake --build . %s" % cmake.build_config)

    def imports(self):
        self.copy("*.dll", "bin", "bin")

    def test(self):
        server = "bin%sserver" % os.sep
        import subprocess
        pid = subprocess.Popen(server)
        print "Lets launch client for ", server

        os.chdir("bin")
        self.run(".%sclient > null" % os.sep)
        pid.terminate()
