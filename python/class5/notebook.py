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
		fout = open(self.filename, 'w')
		for note in self.notes:
			fout.write(str(note))
			fout.write('\n')
		fout.close()

if __name__ == '__main__':
	notebook = Notebook('notebook.txt')
	notebook.add_note('Drink  lot of water', 'health')
	notebook.add_note('Exercise regularly', 'health')
	notebook.add_note('Do not talk to strangers', 'safety')
	notebook.add_note('Always say "thank you"', 'social')

	notebook.save()
	print(notebook)
