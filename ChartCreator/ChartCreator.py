from typing import List
import matplotlib.pyplot as plt


def create_nodes_chart(backtrack_data: List[tuple[float, int, int]], forward_data: List[tuple[float, int, int]], title: str):
    backtrack_x = []
    backtrack_y = []
    for item in backtrack_data:
        backtrack_x.append(item[2])
        backtrack_y.append(item[1])

    forward_x = []
    forward_y = []
    for item in forward_data:
        forward_x.append(item[2])
        forward_y.append(item[1])

    plt.plot(backtrack_x, backtrack_y, label='backtrack', alpha=0.8, linewidth= 3, color='#25D5F7')
    plt.plot(forward_x, forward_y, label='forward', alpha=0.6, linewidth= 3, color='#F7780C')

    plt.legend(loc="upper left")

    plt.title(title)
    plt.xlabel("Number of found solutions")
    plt.ylabel("Nodes Visits")

    plt.show()


def create_time_chart(backtrack_data: List[tuple[float, int, int]], forward_data: List[tuple[float, int, int]], title: str):
    backtrack_x = []
    backtrack_y = []
    for item in backtrack_data:
        backtrack_x.append(item[2])
        backtrack_y.append(item[0])

    forward_x = []
    forward_y = []
    for item in forward_data:
        forward_x.append(item[2])
        forward_y.append(item[0])

    plt.plot(backtrack_x, backtrack_y, label='backtrack', alpha=0.8, linewidth= 3, color='#25D5F7')
    plt.plot(forward_x, forward_y, label='forward', alpha=0.6, linewidth= 3, color='#F7780C')

    plt.legend(loc="upper left")

    plt.title(title)
    plt.xlabel("Number of found solutions")
    plt.ylabel("Time [s]")

    plt.show()
