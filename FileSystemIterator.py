import os
import fnmatch


class FileSystemIterator:
        def __iter__(self):
		return self

	def __next__(self):
		if self.index >= len(self.files):
			raise StopIteration
		item = self.files[self.index]
		self.index += 1
		return item

	def __init__(self, root, only_files=False, only_dirs=False, pattern=None):
		self.root = root
		self.only_files = only_files
		self.only_dirs = only_dirs
		self.pattern = pattern

		self.files = []
		self.find_files()
		self.index = 0

	def find_files(self):
		for root, dirs, files in os.walk(self.root):
			if self.only_files:
				if self.pattern:
					self.files.extend([os.path.join(root, file) for file in files if fnmatch.fnmatch(file, self.pattern)])
				else:
					self.files.extend([os.path.join(root, file) for file in files])
			
			elif self.only_dirs:
				self.files.extend([os.path.join(root, dir) for dir in dirs])
			else:
				if self.pattern:
					self.files.extend([os.path.join(root, name) for name in dirs + files if fnmatch.fnmatch(name, self.pattern)])
				else:
					self.files.extend([os.path.join(root, name) for name in dirs + files])
		self.index = 0

	