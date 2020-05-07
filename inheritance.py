def name(first_name):
    name_1 = "My first name is " + str(first_name)
    return name_1
    
def another_name(name):
    name_2 = "My second name is "+ str(name)
    return name_2

def allnames():
    first_name = "Jane"
    second_name = "Janet"
    information = name(first_name) + " and " + another_name(second_name)
    return information

print(allnames())

#class master(readme, file1) - develop(framework, data)

class Master:
    def __init__(self,readme):
        self.readme = readme
        self.file1 = []
    
    def new_file(self, data):
        self.file1.append(data)
        return self.file1

    def get_files(self):
        return self.file1


class Develop(Master):
    def __init__(self, readme, framework,data):
        super().__init__(self, readme)
        self.framework = framework
        self.data = data 


den = Master(readme="life")
github = Develop(framework = "new", data="one", readme="take it")
github.new_file("too many files")
github.new_file("Hello World")
print(github.get_files())