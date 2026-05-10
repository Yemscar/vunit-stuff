library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL; -- Recommended library for arithmetic

library vunit_lib;
context vunit_lib.vunit_context;

library work;
use work.counter;

entity tb_example is
  generic (runner_cfg : string);
end entity;

architecture tb of tb_example is

signal clk, reset : STD_LOGIC;
signal count : std_logic_vector(3 downto 0);

begin

  main : process
  begin
    test_runner_setup(runner, runner_cfg);
    report "Hello world!";

    reset <= '1';
    wait for 20 ns;
  check_equal(count, 0, "Reset was not correct");
    reset <='0';
    wait for 1 ps;

    wait for 100 ns;

    test_runner_cleanup(runner); -- Simulation ends here
  end process;


  clk_proc : process
  begin
    clk <= '1';
    wait for 10 ns;
    clk <= '0';
    wait for 10 ns;
  end process;

  dut : entity work.counter(Behavioral) 
  port map (
        clk => clk,  
        reset => reset,
        count => count
	   );

  test_runner_watchdog(runner, 1 ms);

end architecture;
