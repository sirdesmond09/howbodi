file = 'n.txt'

with open(file) as file_object: 
    lines = file_object.readlines() 
    
    for line in lines: 
        j = line.strip('\n').rsplit('\t')
        print(j[0], j[1])
        print(f'\n{j[-1]}')

        # PersonalHealthQuestion.objects.create(question = j[1])

# PersonalHealthQuestion.objects.create(test = test_id, question = j[1], not_at_all = 0, a_little_bit = 1, moderately = 2, quite_a_bit = 3, extremely = 4)

# AddictionQuestion.objects.create(test = test_id, question = j[1], yes = 1, no = 0)