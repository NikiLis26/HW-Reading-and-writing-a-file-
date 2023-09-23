import os

def count_lines(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return len(f.readlines())


folder_path = "Здание 3. Файлы"
file_list = [f for f in os.listdir(folder_path) if f.endswith('.txt')]


file_list.sort(key=lambda x: count_lines(os.path.join(folder_path, x)))

with open("output.txt", 'w', encoding='utf-8') as outfile:
    for filename in file_list:
        line_count = count_lines(os.path.join(folder_path, filename))
        outfile.write(f'{filename}\n{line_count}\n')
        with open(os.path.join(folder_path, filename), 'r', encoding='utf-8') as infile:
            outfile.writelines(infile.readlines())
        outfile.write('\n')
