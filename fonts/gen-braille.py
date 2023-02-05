#!/usr/bin/python3

def show_char(i):
    bit = [ '--', '--', '--', '--', '--', '--', '--', '--' ]

    for n in range(8):
        if i & (1 << n):
            bit[n] = '##'

    print('%')
    print(f'// Character {256 + i}')
    print('Bitmap: -------- \\')
    print(f'        -{bit[0]}--{bit[3]}- \\')
    print(f'        -{bit[0]}--{bit[3]}- \\')
    print('        -------- \\')
    print('        -------- \\')
    print(f'        -{bit[1]}--{bit[4]}- \\')
    print(f'        -{bit[1]}--{bit[4]}- \\')
    print('        -------- \\')
    print('        -------- \\')
    print(f'        -{bit[2]}--{bit[5]}- \\')
    print(f'        -{bit[2]}--{bit[5]}- \\')
    print('        -------- \\')
    print('        -------- \\')
    print(f'        -{bit[6]}--{bit[7]}- \\')
    print(f'        -{bit[6]}--{bit[7]}- \\')
    print('        --------')
    print('Unicode: [{:08x}];'.format(0x2800 + i))


if __name__ == '__main__':
    for i in range(256):
        show_char(i)

