from conans import ConanFile, CMake


class PolarsConan(ConanFile):
    name = "Polars"
    version = "0.4.0"
    url = "https://github.com/polarsorg/polars"
    license = "MIT License"
    description = "A C++ TimeSeries library that aims to mimic pandas Series"
    settings = "os", "compiler", "build_type", "arch"
    options = {
        "shared": [True, False],
        "with_tests": [True, False],
    }
    default_options = "shared=False", "with_tests=False"
    generators = "cmake"
    exports_sources = "*", "!dependencies/*", "!build", "!source"
    requires = "Armadillo/9.200.1", "date/3.0.1"

    def requirements(self):
        if self.options.with_tests:
            self.requires("gtest/1.10.0")

    def build(self):
        cmake = CMake(self)
        cmake.definitions["WITH_TESTS"] = self.options.with_tests
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
