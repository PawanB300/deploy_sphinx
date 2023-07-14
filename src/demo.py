class A:

    def __init__(self, name, age) -> None:
        """
        :params Str name: Name of author
        :params Int age: Age of author
        """
        self.name = name 
        self.age = age

    def print_info(self):

        """
        :returns Print all the info it has about author
        """

        print(self.name, self.age)