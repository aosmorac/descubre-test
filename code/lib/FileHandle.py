class FileHandle:

	def __init__(self, arg):
		super(ClassName, self).__init__()
		self.arg = arg

	def saveFile(name, text):
		f = open(name,"w+");
		f.write(text);
		f.close;
		return 1;