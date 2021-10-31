subject_id = '2301170'
subject = 'Python'
days = ['M', 'W', 'F']
data = {'First': [1, 2, 3], True: 8, -2.5: (4, '5'), (0, 'k'): False,
        'last': {}, subject_id: subject, 'class': days}

for key in data.keys():
    print(key)