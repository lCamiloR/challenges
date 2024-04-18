class InfiniteArray:
    
    main_dict = {}
    default_value = None

    def __str__(self) -> str:
        if self.default_value:
            return '[' + f'{self.default_value},' * 49 + f'{self.default_value}, ...]'
        return [v for v in self.main_dict.values()].__str__()
    
    def get(self, index:int):
        return self.main_dict.get(index, self.default_value)

    def insert(self, value):
        self.main_dict[len(self.main_dict)] = value
        self.default_value = None

    def set_all(self, value):
        self.default_value = value
        self.main_dict = {}


if __name__ == '__main__':
    custom_array = InfiniteArray()
    custom_array.insert("Eduardo")
    print(custom_array.get(0))
    custom_array.insert("Lucas")
    print(custom_array.get(1))
    custom_array.set_all("Mateus")
    print(custom_array)