import Zenify
from os import system
#red
system("title " + "Zenify Shell")
print("Zenify - Shell")
while True:
	text = input('Zenify $ ')
	if text.strip() == "": continue
	result, error = Zenify.run('<stdin>', text)

	if error:
		print(error.as_string())
	elif result:
		if len(result.elements) == 1:
			print(repr(result.elements[0]))
		else:
			print(repr(result))
