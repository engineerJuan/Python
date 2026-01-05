from colorama import Fore, Style, init

init(autoreset=True)

def corazon(name):
    name = name.upper()
    name_len = len(name)
    idx = 0
    
    for y in range(20, -20, -1):
        row = ""
        for x in range(-40, 41):
            x0, y0 = x * 0.05, y * 0.1
            
            equation_val = (x0**2 + y0**2 - 1)**3 - x0**2 * y0**3
            
            if equation_val <= 0:
                is_border = False
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = (x + dx) * 0.05, (y + dy) * 0.1
                    neighbor_val = (nx**2 + ny**2 - 1)**3 - nx**2 * ny**3
                    if neighbor_val > 0:
                        is_border = True
                        break
                
                if is_border:
                    row += Fore.BLUE + "♦" + Style.RESET_ALL
                else:
                    row += Fore.RED + name[idx % name_len] + Style.RESET_ALL
                    idx += 1
            else:
                row += " "
        print(row)

if __name__ == "__main__":
    try:
        user_input = input("Nombre: ")
        if not user_input:
            user_input = "LOVE"
        corazon(user_input)
    except KeyboardInterrupt:
        print("\nExiting...")