#task1 - Hello World
#CS4300 - Zachary Donnelly

#returns "Hello, World!" to the screen
def task():
    return "Hello, World!"

#tests the task to verify the output is correct
def test_task1():
	output = task()
	assert output == "Hello, World!"