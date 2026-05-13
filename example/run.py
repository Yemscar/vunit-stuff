from vunit import VUnit

vu = VUnit.from_argv(compile_builtins=False)

# Needed for built in vunit functions
vu.add_vhdl_builtins()
vu.add_verification_components()
vu.add_random()

#Add OSVVM library
vu.add_osvvm()

# Allow -gui flag to open a waveform viewer.
#vu.set_sim_option("ghdl.viewer_args", ["--save", "my_signals.gtkw"], all_empty=False, overwrite=True)

common = vu.add_library(library_name="common").add_source_files(pattern="src/hdl-modules/modules/common/**/*.vhd")

math = vu.add_library(library_name="math").add_source_files(pattern="src/hdl-modules/modules/math/**/*.vhd")

resync = vu.add_library(library_name="resync").add_source_files(pattern="src/hdl-modules/modules/resync/**/*.vhd")

axi = vu.add_library(library_name="axi").add_source_files(pattern="src/hdl-modules/modules/axi/**/*.vhd")

axi_lite = vu.add_library(library_name="axi_lite").add_source_files(pattern="src/hdl-modules/modules/axi_lite/**/*.vhd")

bfm = vu.add_library(library_name="bfm").add_source_files(pattern="src/hdl-modules/modules/bfm/**/*.vhd")

fifo = vu.add_library(library_name="fifo").add_source_files(pattern="src/hdl-modules/modules/fifo/**/*.vhd")

register_file = vu.add_library(library_name="register_file").add_source_files(pattern="src/hdl-modules/modules/register_file/**/*.vhd")

secureip = vu.add_library(library_name="secureip").add_source_files(pattern="/opt/2025.2/Vivado/data/vhdl/src/unisims/secureip/**/*.vhd")

unisim = vu.add_library(library_name="unisim").add_source_files(pattern="/opt/2025.2/Vivado/data/vhdl/src/unisims/**/*.vhd")

# Create library 'lib', add "allow_empty=False" to disable error when no source files can be found.
lib = vu.add_library(library_name="lib")
# Add all files ending in .vhd in current working directory to library
lib.add_source_files("src/**/*.vhd")
vu.get_libraries('*')

#lib.get_test_benches(allow_empty=True)

# Run vunit function
vu.main()
