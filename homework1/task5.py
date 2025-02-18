#Task5 - Lists and Dictionaries
#CS4300 Zachary Donnelly

#creates a list of books and outputs the first 3
def books():
    book_list = ["Stormbreaker by Anthony Horowitz",
    "The Seven Habits of Highly Effective People by Stephen Covey",
    "The Score Takes Care of Itself by Bill Walsh",
    "The Dirt Eaters by Dennis Foon" ,"Dead Simple by Peter James"]
    
    print(book_list[0:3])
    output = book_list[0:3]
    
    return output
    
#creates a list of dictionaries to emulate a student database
def students():
    student_list = [
    {"Name": "Zachary Donnelly", "ID": "123456"},
    {"Name": "Jane Doe", "ID": "000000"},
    {"Name": "John Doe", "ID": "000001"}]
    
    print(student_list)
    output = student_list
    
    return output
#testing that books output is correct
def test_books():
    output = books()
    
    assert isinstance(output, list)
    assert output == ["Stormbreaker by Anthony Horowitz",
    "The Seven Habits of Highly Effective People by Stephen Covey",
    "The Score Takes Care of Itself by Bill Walsh"]
    
#testing the student data    
def test_students():
   output = students()
   
   assert output == [
    {"Name": "Zachary Donnelly", "ID": "123456"},
    {"Name": "Jane Doe", "ID": "000000"},
    {"Name": "John Doe", "ID": "000001"}]