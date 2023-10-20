import os
import datetime

class DirectoryTraversal:
    def __init__(self, directory):
        self.directory = directory

    def list_files_created_dates(self):
        for root, dirs, files in os.walk(self.directory):
            for file in files:
                file_path = os.path.join(root, file)
                created_date = self.get_file_creation_date(file_path)
                if created_date:
                    print(f"File: {file_path}, Created Date: {created_date}")

    @staticmethod
    def get_file_creation_date(file_path):
        try:
            # Get file modification time
            modification_time = os.path.getmtime(file_path)

            # Convert modification time to a datetime object
            created_date = datetime.datetime.fromtimestamp(modification_time)

            return created_date
        except Exception as e:
            print(f"Error accessing creation date for {file_path}: {str(e)}")
            return None

if __name__ == "__main__":
    directory_to_traverse = "/Users/mo/Documents/workspace"  # Replace with the directory you want to traverse
    if os.path.exists(directory_to_traverse) and os.path.isdir(directory_to_traverse):
        dt = DirectoryTraversal(directory_to_traverse)
        dt.list_files_created_dates()
    else:
        print("The specified directory does not exist or is not a valid directory.")
