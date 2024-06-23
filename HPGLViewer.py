import sys
import matplotlib.pyplot as plt
import matplotlib.transforms as transforms
import re

def read_hpgl(file_path):
    with open(file_path, 'r') as file:
        return file.read().replace('\n', '')

def parse_hpgl(data):
    commands = re.findall(r'[A-Z]{2}[^;]*;', data)
    return [command.strip() for command in commands]

def plot_hpgl(commands):
    x, y = [], []
    max_y = 0  
    pen_down = False
    text_size = (0.400, 0.700)  
    fig, ax = plt.subplots()
    current_color = 'b'
    transform = transforms.Affine2D()  # 初始化变换

    #
    for command in commands:
        coords = re.findall(r'\d+', command[2:])
        y_coords = list(map(int, coords[1::2]))
        if y_coords:
            max_y = max(max_y, max(y_coords))

   
    for command in commands:
        cmd_type = command[:2]
        params = command[2:].strip(';')

        if cmd_type == 'PU':
            if pen_down and x and y:
                ax.plot(x, [max_y - yi for yi in y], color=current_color, transform=transform + ax.transData)
            x, y = [], []
            pen_down = False
        elif cmd_type == 'PD':
            pen_down = True

        if cmd_type in ['PU', 'PD']:
            coords = re.findall(r'\d+', params)
            if coords:
                x.extend(map(int, coords[0::2]))
                y.extend(map(int, coords[1::2]))
        elif cmd_type == 'IN':
            ax.clear()
        elif cmd_type == 'SP':
            current_color = 'b' if params.strip() == '1' else 'r'
        elif cmd_type == 'SI':
            text_size = tuple(map(float, params.split(',')))
        elif cmd_type == 'LB':
            label = params.split('\x04')[0]
            if x and y:
                ax.text(x[-1], max_y - y[-1], label, fontsize=10 * text_size[1], verticalalignment='bottom', transform=transform + ax.transData)
        elif cmd_type == 'RO':
            angle = int(params)
            transform.rotate_deg(-angle)

    if pen_down and x and y:
        ax.plot(x, [max_y - yi for yi in y], color=current_color, transform=transform + ax.transData)

    ax.set_aspect('equal')
    plt.gca().invert_yaxis()
    plt.show()

def main():
    if len(sys.argv) != 2:
        print("Usage: python hpglview.py <hpgl_file>")
        return

    file_path = sys.argv[1]
    data = read_hpgl(file_path)
    commands = parse_hpgl(data)
    plot_hpgl(commands)

if __name__ == "__main__":
    main()
