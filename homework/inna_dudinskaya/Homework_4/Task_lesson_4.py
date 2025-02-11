my_dict = {'tuple': (1, 2, 3, 4, 5),
           'list': [6, 7, 8, 9, 10],
           'dict': {'one': 'value1', 'two': 'value2',
                    'three': 'value3', 'four': 'value4',
                    'five': 'value5'},
           'set': {'a1', 'a2', 'a3', 'a4', 'a5'}}

print(my_dict['tuple'][-1])

my_dict['list'].append(25)
my_dict['list'].pop(1)

my_dict['dict'] = {'one': 'value1', 'two': 'value2',
                   'three': 'value3', 'four': 'value4',
                   'five': 'value5', 'i am a tuple': 'value6'}

my_dict['dict'] = {'one': 'value1', 'two': 'value2',
                   'three': 'value3', 'four': 'value4',
                   'i am a tuple': 'value6'}

my_dict['set'].add('a6')
my_dict['set'].pop()

print(my_dict)
