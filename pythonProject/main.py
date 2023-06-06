# This is a sample Python script.
import torch


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    x = torch.tensor([1.0, 2.0, 3.0, 4.0], requires_grad=True)
    y = 2 * x
    z = y.view(2, 2)
    print(z)
    v = torch.tensor([[1.0, 0.1], [0.01, 0.001]], dtype=torch.float)
    z.backward(v)
    print(z)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
