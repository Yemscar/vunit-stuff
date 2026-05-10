ibrary ieee;
use ieee.std_logic_1164.all;

-- Import the VUnit context for access to 'run', 'check', etc.
library vunit_lib;
context vunit_lib.vunit_context;

entity tb_example is
  generic (runner_cfg : string); -- Mandatory VUnit generic
end entity;

architecture sim of tb_example is
begin
  -- Main test runner process
  main : process
  begin
    test_runner_setup(runner, runner_cfg);

    -- Loop to allow the Python runner to execute individual test cases
    while test_suite loop
      
      if run("Test_Addition") then
        -- Your test logic here
        check_equal(1 + 1, 2, "Simple math should work");
        
      elsif run("Test_Subtraction") then
        -- Another independent test case
        check_equal(5 - 3, 2, "Subtraction test");
        
      end if;
      
    end loop;

    test_runner_cleanup(runner);
  end process;

  dut :
  
end architecture;
