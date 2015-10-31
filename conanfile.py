from conans import ConanFile


class ZMQCPPConan(ConanFile):
    """ ONGOING WORK, tested in Win VS 12 """
    name = "zmqcpp"
    version = "4.1.1"
    url = "https://github.com/memsharded/conan-zmqcpp.git"
    requires = "ZMQ/4.1.1@memsharded/testing"
    exports = "zmq.hpp"

    def package(self):
        self.copy_headers("*.hpp")
