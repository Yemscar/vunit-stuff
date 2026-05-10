library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL; -- Recommended library for arithmetic

entity counter is
    Port ( 
        clk    : in  STD_LOGIC;      -- Clock input
        reset  : in  STD_LOGIC;      -- Asynchronous reset (active high)
        count  : out STD_LOGIC_VECTOR(3 downto 0) -- 4-bit output
    );
end counter;

architecture Behavioral of counter is
    -- Internal signal to hold the count value
    -- Using 'unsigned' allows us to perform math directly (+1)
    signal count_reg : unsigned(3 downto 0) := (others => '0');
begin

    process(clk, reset)
    begin
        -- Asynchronous reset: happens immediately when reset is '1'
        if reset = '1' then
            count_reg <= (others => '0');
        
        -- Trigger on the rising edge of the clock
        elsif rising_edge(clk) then
            count_reg <= count_reg + 1;
        end if;
    end process;

    -- Assign the internal register to the output port
    -- Cast unsigned back to std_logic_vector
    count <= std_logic_vector(count_reg);

end Behavioral;
