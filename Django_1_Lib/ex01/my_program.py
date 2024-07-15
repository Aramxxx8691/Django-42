import sys
sys.path.insert(0, 'local_lib')
from path import Path

def main():
    dir_path = Path('my_folder')
    file_path = dir_path / 'my_file.txt'
    dir_path.mkdir_p()
    file_content = "Hello, this is a test file!"
    file_path.write_text(file_content)
    read_content = file_path.read_text()
    print("🔰 File content🔰:", read_content)

if __name__ == "__main__":
    main()
