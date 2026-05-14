from vunit import VUnit

vu = VUnit.from_argv(compile_builtins=False)

# Needed for built in vunit functions
vu.add_vhdl_builtins()
vu.add_verification_components()
vu.add_random()

#Add OSVVM library
vu.add_osvvm()

axi_lite = vu.add_library(library_name="axi_lite").add_source_files(pattern="src/axi-lite/**/*.vhd")
register_file = vu.add_library(library_name="register_file").add_source_files(pattern="src/register-file/**/*.vhd")
common = vu.add_library(library_name="common").add_source_files(pattern="src/common/**/*.vhd")
math = vu.add_library(library_name="math").add_source_files(pattern="src/math/**/*.vhd")
#bfm = vu.add_library(library_name="bfm").add_source_files(pattern="src/bfm/**/*.vhd")

# Create library 'lib', add "allow_empty=False" to disable error when no source files can be found.
lib = vu.add_library(library_name="lib")
# Add all files ending in .vhd in current working directory to library
lib.add_source_files("src/**/*.vhd")

# 1. Get all libraries
all_libraries = vu.get_libraries()

# 2. Print each library name
print("Registered Libraries:")
for lib in all_libraries:
    print(f" - {lib.name}")

for lib in vu.get_libraries():
    print(f"Library: {lib.name}")
    for source_file in lib.get_source_files():
        print(f"  - {source_file.name}")

# Run vunit function
vu.main()
