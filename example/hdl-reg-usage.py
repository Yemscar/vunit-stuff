from pathlib import Path

from hdl_registers.generator.vhdl.register_package import VhdlRegisterPackageGenerator
from hdl_registers.parser.toml import from_toml


this_dir = Path(__file__).parent

register_list = from_toml(name="caesar", toml_file=this_dir / "toml-example.toml")
VhdlRegisterPackageGenerator(register_list=register_list, output_folder=this_dir).create_if_needed()
