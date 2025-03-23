import os

def write_directory_structure(startpath, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        for root, dirs, files in os.walk(startpath):
            # Определяем уровень вложенности
            level = root.replace(startpath, '').count(os.sep)
            indent = ' ' * 4 * level
            f.write(f"{indent}[DIR] {os.path.basename(root)}\n")
            for file in files:
                f.write(f"{indent}    {file}\n")

# Замените путь на путь к вашей папке
start_directory = 'C:/Users/Пользователь/Documents/GitHub/mysite/myproject'
output_file = 'directory_structure.txt'

write_directory_structure(start_directory, output_file)
