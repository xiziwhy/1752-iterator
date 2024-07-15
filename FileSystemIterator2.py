import os

class filesystemiterator:
    def __init__(self, root, only_files, only_dirs, pattern):
        """
        Initialize the object
        :param root: root directory
        :param only_files: iterate only over files
        :param only_dirs: iterate only over directories
        :param pattern: iterate only over items in the file system containing the pattern in the name
        """
        self.root = root
        self.only_files = only_files
        self.only_dirs = only_dirs
        self.pattern = pattern
        self.filesystem_generator = self._generate_items()

    def _generate_items(self):
        for root, dirs, files in os.walk(self.root):
            for name in files:
                if not self.only_dirs and (not self.only_files or self.only_files and os.path.isfile(os.path.join(root, name))) and (self.pattern is None or self.pattern in name):
                    yield os.path.join(root, name)
            for name in dirs:
                if not self.only_files and (not self.only_dirs or self.only_dirs and os.path.isdir(os.path.join(root, name))) and (self.pattern is None or self.pattern in name):
                    yield os.path.join(root, name)

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.filesystem_generator)