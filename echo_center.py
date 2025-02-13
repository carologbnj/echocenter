import os
import zipfile
import argparse

class EchoCenter:
    def __init__(self, directory, archive_name):
        self.directory = directory
        self.archive_name = archive_name

    def compress_directory(self):
        """Compresses the specified directory into a zip file."""
        try:
            with zipfile.ZipFile(self.archive_name, 'w', zipfile.ZIP_DEFLATED) as archive:
                for foldername, subfolders, filenames in os.walk(self.directory):
                    for filename in filenames:
                        file_path = os.path.join(foldername, filename)
                        archive.write(file_path, os.path.relpath(file_path, self.directory))
            print(f"Directory '{self.directory}' has been successfully compressed into '{self.archive_name}'.")
        except Exception as e:
            print(f"An error occurred while compressing the directory: {e}")

def main():
    parser = argparse.ArgumentParser(description='Archive and compress files to save space and improve load times.')
    parser.add_argument('directory', type=str, help='The directory to archive and compress.')
    parser.add_argument('archive_name', type=str, help='The name of the output archive file.')

    args = parser.parse_args()

    echo_center = EchoCenter(args.directory, args.archive_name)
    echo_center.compress_directory()

if __name__ == '__main__':
    main()