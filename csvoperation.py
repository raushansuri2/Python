datalist = []

while True:
    user_action = input('Type add, edit, show, complete or exit: ')
    user_action = user_action.strip();

    match user_action:
        case 'add':
            todo = input('enter the any data: ') + "\n"
            file = open('data.txt', 'r');
            data = file.readlines()
            data.append(todo)
            file = open('data.txt','w');
            file.writelines(data)
        case 'show':
            file = open('data.txt', 'r');
            datalist = file.readlines()
            file.close();
            #datalist_new = [item.strip('\n') for item in datalist] #list comprehension
            for index, item in enumerate(datalist):
                item = item.strip('\n')
                row = f"{index} - ({item})"
                print(row)
        case 'exit':
            break
        case 'edit':
            print('dd')

