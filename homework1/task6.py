#task6 - File Handling and Metaprogramming
#CS4300 Zachary Donnelly

#counts the amount of words in a file, takes the file name as input and through line splitting, returns the amount of words within the file
def file_count(file):
    num_words = 0
    
    with open(file, 'r') as file:
    
        input = file.read()
        split = input.split()
    
        num_words += len(split)
    
    return num_words


#using metaprogramming to create test names and verify the file_count function output
def meta_test_case(name):
    def test_file_count():
        expected_output = 127
        output = file_count(name)
        
        assert output == expected_output
        
        
    return test_file_count
        
       
#can be used to generate test cases for multiple files
file_name = ["task6_read_me.txt"]

#generating test cases for all files
for files in file_name:
    test = meta_test_case(files)
    