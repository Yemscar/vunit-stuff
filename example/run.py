from vunit import VUnit

# Create VUnit instance by parsing command line arguments
vu = VUnit.from_argv()

# Optionally add VUnit's builtin HDL utilities for checking, logging, communication...
# See http://vunit.github.io/hdl_libraries.html.
vu.add_vhdl_builtins()
# or
# vu.add_verilog_builtins()

vu.set_sim_option("ghdl.viewer_args", ["--save", "my_signals.gtkw"], all_empty=False, overwrite=True)

# Create library 'lib'
lib = vu.add_library("lib")

# Add all files ending in .vhd in current working directory to library
lib.add_source_files("*.vhd")

#lib.get_test_benches(allow_empty=True)

# Run vunit function
vu.main()
