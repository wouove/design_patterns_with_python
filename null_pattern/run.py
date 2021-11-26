from my_object_factory import MyObjectFactory

my_obj = MyObjectFactory.create_object('my_other_class')
my_obj.do_something('something')
# if my_obj is not None:
#     my_obj.do_something('something')
# else:
#     print('Not doing anything')
    