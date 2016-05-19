from conans import ConanFile


class ZMQCPPConan(ConanFile):
    name = "zmqcpp"
    version = "4.1.1"
    url = "https://github.com/memsharded/conan-zmqcpp.git"
    requires = "ZMQ/4.1.1@memsharded/stable"
    exports = "zmq.hpp"

    def package(self):
        self.copy_headers("*.hpp")
