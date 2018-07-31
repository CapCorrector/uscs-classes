import pickle

from note import Note

class Notebook:
	def __init__(self, filename):
		self.notes = []
		self.filename = filename

	def __str__(self):
		result = ''
		for index, note in enumerate(self.notes, start = 1):
			result += str(index) + '. ' + str(note) + '\n'
		return result

	def add_note(self, content, category):
		self.notes.append(Note(content, category))
	
	def save(self):
		fout = open(self.filename, 'wb')
		pickle.dump(self.notes, fout)
		fout.close()

	def load(self):
		fin = open(self.filename, 'rb')
		self.notes = pickle.load(fin)
		fin.close()

if __name__ == '__main__':
	notebook = Notebook('notebook.dat')
#	notebook.add_note('Drink  lot of water', 'health')
#	notebook.add_note('Exercise regularly', 'health')
#	notebook.add_note('Do not talk to strangers', 'safety')
#	notebook.add_note('Always say "thank you"', 'social')

#	notebook.save()
	notebook.load()
	print(notebook)
