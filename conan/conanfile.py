from conans import ConanFile, CMake, tools


class PolarsConan(ConanFile):
    name = "Polars"
    version = "0.1.0"
    url = "https://github.com/polarsorg/polars"
    license = "MIT License"
    description = "A C++ TimeSeries library that aims to mimic pandas Series"
    settings = "cppstd", "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"
    exports_sources = "../*", "!dependencies/*", "!build"
    requires = "Armadillo/9.200.1", "date/2.4.1"

    def build(self):
        cmake = CMake(self)
        cmake.definitions["WITH_TESTS"] = "OFF"
        cmake.definitions["BUILD_WITH_CONAN"] = "ON"
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", src="src/cpp")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.dylib*", dst="lib", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["polars_cpp"]
