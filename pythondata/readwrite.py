with open('name.txt', 'r') as f:
	my_name = f.read()

greeting = "Hello, my name is "  + my_name +  " . "

with open('hello.txt', 'w') as f:
	f.write(greeting)