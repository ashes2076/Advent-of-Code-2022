import numpy as np
import pandas as pd

small_program = """noop
addx 3
addx -5
""".split("\n")

with open('Day10\Input_Day10.txt') as f:
    test_data = f.read().split("\n")

def run_signal(program):
    cycles = 1
    x = 1
    cycle_series = [0]
    x_series = [0]
    program_series = ['']

    for line in program:
        cycle_series.append(cycles)
        x_series.append(x)
        program_series.append(line)
        tokens = line.split(" ")
        if tokens[0] == "noop":
            cycles += 1
        elif tokens[0] == "addx":
            cycles += 1
            cycle_series.append(cycles)
            x_series.append(x)
            program_series.append("")
            cycles += 1
            v = int(tokens[1])
            x += v

    
    signal_strength = np.multiply(x_series, cycle_series)
    df = pd.DataFrame({
        "cycle": cycle_series,
        "x": x_series,
        "signal_strength": signal_strength,
        "program": program_series
    })
    return df

run_signal(small_program)

def get_pixel(cycle, x):
    cycle = (((cycle-1) % 40)+1)
    if abs((x+1) - cycle) < 2:
        return "#"
    else:
        return "."

def plot_screen(program):
    df = run_signal(program)
    df['pixel'] = [get_pixel(*item) for item in zip(df['cycle'], df['x'])]
    rows = len(df) // 40
    screen = df["pixel"].to_numpy()[1: 40 * (len(df) // 40)+1].reshape((-1,40))
    print("\n".join([''.join(line) for line in screen]))
    return df
                     
plot_screen(test_data)
