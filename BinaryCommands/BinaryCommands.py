from Utility import File_reader
from Binary.Binary import *
from ChartCreator import ChartCreator
from TableCreator import TableCreator


def solve_all_backward():
    size = '6'
    binary_backward(File_reader.get_rows_file(path, title, size, '2'), 'BACKWARD 6x6 lista')

    binary_backward(File_reader.get_rows_file(path, title, size, ''), 'BACKWARD 6x6')

    size = '8'
    binary_backward(File_reader.get_rows_file(path, title, size, ''), 'BACKWARD 8x8')

    size = '10'
    binary_backward(File_reader.get_rows_file(path, title, size, ''), 'BACKWARD 10x10')


def count_all_backward():
    size = '6'
    binary_backward_count(File_reader.get_rows_file(path, title, size, '2'), 'BACKWARD 6x6 lista')

    binary_backward_count(File_reader.get_rows_file(path, title, size, ''), 'BACKWARD 6x6')

    size = '8'
    binary_backward_count(File_reader.get_rows_file(path, title, size, ''), 'BACKWARD 8x8')

    size = '10'
    binary_backward_count(File_reader.get_rows_file(path, title, size, ''), 'BACKWARD 10x10')


def solve_8x8():
    size = '8'
    binary_backward(File_reader.get_rows_file(path, title, size, ''), 'BACKWARD 8x8')


def solve_all_forward():
    size = '6'
    binary_forward(File_reader.get_rows_file(path, title, size, '2'), 'FORWARD 6x6 lista')

    binary_forward(File_reader.get_rows_file(path, title, size, ''), 'FORWARD 6x6')

    size = '8'
    binary_forward(File_reader.get_rows_file(path, title, size, ''), 'FORWARD 8x8')

    size = '10'
    binary_forward(File_reader.get_rows_file(path, title, size, ''), 'FORWARD 10x10')


def count_all_forward():
    size = '6'
    binary_forward_count(File_reader.get_rows_file(path, title, size, '2'), 'FORWARD 6x6 lista')

    binary_forward_count(File_reader.get_rows_file(path, title, size, ''), 'FORWARD 6x6')

    size = '8'
    binary_forward_count(File_reader.get_rows_file(path, title, size, ''), 'FORWARD 8x8')

    size = '10'
    binary_forward_count(File_reader.get_rows_file(path, title, size, ''), 'FORWARD 10x10')


def data_backtrack():
    size = '6'
    binary_backtrack_data(File_reader.get_rows_file(path, title, size, '2'), 'BACKWARD 6x6 lista')

    binary_backtrack_data(File_reader.get_rows_file(path, title, size, ''), 'BACKWARD 6x6')

    size = '8'
    binary_backtrack_data(File_reader.get_rows_file(path, title, size, ''), 'BACKWARD 8x8')

    size = '10'
    binary_backtrack_data(File_reader.get_rows_file(path, title, size, ''), 'BACKWARD 10x10')


def data_forward():
    size = '6'
    binary_forward_data(File_reader.get_rows_file(path, title, size, '2'), 'FORWARD 6x6 lista')

    binary_forward_data(File_reader.get_rows_file(path, title, size, ''), 'FORWARD 6x6')

    size = '8'
    binary_forward_data(File_reader.get_rows_file(path, title, size, ''), 'FORWARD 8x8')

    size = '10'
    binary_forward_data(File_reader.get_rows_file(path, title, size, ''), 'FORWARD 10x10')


def compare_6x6_fromlist():
    size = '6'
    backtrack_data = binary_backtrack_data(File_reader.get_rows_file(path, title, size, '2'), 'BACKWARD 6x6 lista')
    forward_data = binary_forward_data(File_reader.get_rows_file(path, title, size, '2'), 'FORWARD 6x6 lista')
    ChartCreator.create_nodes_chart(backtrack_data, forward_data, '6x6 lista')
    ChartCreator.create_time_chart(backtrack_data, forward_data, '6x6 lista')
    TableCreator.create_nodes_table(backtrack_data, forward_data, '6x6 lista')
    TableCreator.create_time_table(backtrack_data, forward_data, '6x6 lista')

def compare_6x6():
    size = '6'
    backtrack_data = binary_backtrack_data(File_reader.get_rows_file(path, title, size, ''), 'BACKWARD 6x6')
    forward_data = binary_forward_data(File_reader.get_rows_file(path, title, size, ''), 'FORWARD 6x6')
    ChartCreator.create_nodes_chart(backtrack_data, forward_data, '6x6')
    ChartCreator.create_time_chart(backtrack_data, forward_data, '6x6')
    TableCreator.create_nodes_table(backtrack_data, forward_data, '6x6')
    TableCreator.create_time_table(backtrack_data, forward_data, '6x6')

def compare_8x8():
    size = '8'
    backtrack_data = binary_backtrack_data(File_reader.get_rows_file(path, title, size, ''), 'BACKWARD 8x8')
    forward_data = binary_forward_data(File_reader.get_rows_file(path, title, size, ''), 'FORWARD 8x8')
    ChartCreator.create_nodes_chart(backtrack_data, forward_data, '8x8')
    ChartCreator.create_time_chart(backtrack_data, forward_data, '8x8')
    TableCreator.create_nodes_table(backtrack_data, forward_data, '8x8')
    TableCreator.create_time_table(backtrack_data, forward_data, '8x8')

def compare_10x10():
    size = '10'
    backtrack_data = binary_backtrack_data(File_reader.get_rows_file(path, title, size, ''), 'BACKWARD 10x10')
    forward_data = binary_forward_data(File_reader.get_rows_file(path, title, size, ''), 'FORWARD 10x10')
    ChartCreator.create_nodes_chart(backtrack_data, forward_data, '10x10')
    ChartCreator.create_time_chart(backtrack_data, forward_data, '10x10')
    TableCreator.create_nodes_table(backtrack_data, forward_data, '10x10')
    TableCreator.create_time_table(backtrack_data, forward_data, '10x10')