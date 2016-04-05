# functional style
# def my_fancy_attribute_getter(self):
#     attr_and_values = ((attr, getattr(self, attr)) for attr in dir(self) if not attr.startswith("__"))
#     return [(attr, value) for attr, value in attr_and_values if not callable(value)]

# imperative style
# def my_fancy_attribute_getter(self):
#     result = []
#     for attr in dir(self):
#         if not attr.startswith("__"):
#             value = getattr(self, attr)
#             if not callable(value):
#                 result.append((attr, value))
#     return result
#     #print(result)

def my_even_fancier_attribute_getter(self):
    return [(attr, value) for attr, value in self.__dict__.items() if not callable(value)]



#print(my_fancy_attribute_getter())
print(my_even_fancier_attribute_getter())