from Utility import File_reader
from ChartCreator import ChartCreator
from Futoshiki.Futoshiki import *
from TableCreator import TableCreator


def solve_all_backward():
    size = '4'
    futoshiki_backward(File_reader.get_rows_file(path, title, size, ''), 'BACKWARD 4x4')

    size = '5'
    futoshiki_backward(File_reader.get_rows_file(path, title, size, ''), 'BACKWARD 5x5')

    size = '6'
    futoshiki_backward(File_reader.get_rows_file(path, title, size, ''), 'BACKWARD 6x6')


def count_all_backward():
    size = '4'
    futoshiki_backward_count(File_reader.get_rows_file(path, title, size, ''), 'BACKWARD 4x4')

    size = '5'
    futoshiki_backward_count(File_reader.get_rows_file(path, title, size, ''), 'BACKWARD 5x5')

    size = '6'
    futoshiki_backward_count(File_reader.get_rows_file(path, title, size, ''), 'BACKWARD 6x6')


def solve_all_forward():
    size = '4'
    futoshiki_forward(File_reader.get_rows_file(path, title, size, ''), 'FORWARD 4x4')

    size = '5'
    futoshiki_forward(File_reader.get_rows_file(path, title, size, ''), 'FORWARD 5x5')

    size = '6'
    futoshiki_forward(File_reader.get_rows_file(path, title, size, ''), 'FORWARD 6x6')


def count_all_forward():
    size = '4'
    futoshiki_forward_count(File_reader.get_rows_file(path, title, size, ''), 'FORWARD 4x4')

    size = '5'
    futoshiki_forward_count(File_reader.get_rows_file(path, title, size, ''), 'FORWARD 5x5')

    size = '6'
    futoshiki_forward_count(File_reader.get_rows_file(path, title, size, ''), 'FORWARD 6x6')


def data_backtrack():
    size = '4'
    futoshiki_backtrack_data(File_reader.get_rows_file(path, title, size, ''), 'BACKWARD 4x4')

    size = '5'
    futoshiki_backtrack_data(File_reader.get_rows_file(path, title, size, ''), 'BACKWARD 5x5')

    size = '6'
    futoshiki_backtrack_data(File_reader.get_rows_file(path, title, size, ''), 'BACKWARD 6x6')


def data_forward():
    size = '4'
    futoshiki_forward_data(File_reader.get_rows_file(path, title, size, ''), 'FORWARD 4x4')

    size = '5'
    futoshiki_forward_data(File_reader.get_rows_file(path, title, size, ''), 'FORWARD 5x5')

    size = '6'
    futoshiki_forward_data(File_reader.get_rows_file(path, title, size, ''), 'FORWARD 6x6')


def compare4x4():
    size = '4'
    backtrack_data = futoshiki_backtrack_data(File_reader.get_rows_file(path, title, size, ''), 'BACKWARD 4x4')
    forward_data = futoshiki_forward_data(File_reader.get_rows_file(path, title, size, ''), 'FORWARD 4x4')
    ChartCreator.create_nodes_chart(backtrack_data, forward_data, '4x4')
    ChartCreator.create_time_chart(backtrack_data, forward_data, '4x4')
    TableCreator.create_nodes_table(backtrack_data, forward_data, '4x4')
    TableCreator.create_time_table(backtrack_data, forward_data, '4x4')


def compare5x5():
    size = '5'
    backtrack_data = futoshiki_backtrack_data(File_reader.get_rows_file(path, title, size, ''), 'BACKWARD 5x5')
    forward_data = futoshiki_forward_data(File_reader.get_rows_file(path, title, size, ''), 'FORWARD 5x5')
    ChartCreator.create_nodes_chart(backtrack_data, forward_data, '5x5')
    ChartCreator.create_time_chart(backtrack_data, forward_data, '5x5')
    TableCreator.create_nodes_table(backtrack_data, forward_data, '5x5')
    TableCreator.create_time_table(backtrack_data, forward_data, '5x5')


def compare6x6():
    size = '6'
    backtrack_data = futoshiki_backtrack_data(File_reader.get_rows_file(path, title, size, ''), 'BACKWARD 6x6')
    forward_data = futoshiki_forward_data(File_reader.get_rows_file(path, title, size, ''), 'FORWARD 6x6')
    ChartCreator.create_nodes_chart(backtrack_data, forward_data, '6x6')
    ChartCreator.create_time_chart(backtrack_data, forward_data, '6x6')
    TableCreator.create_nodes_table(backtrack_data, forward_data, '6x6')
    TableCreator.create_time_table(backtrack_data, forward_data, '6x6')
