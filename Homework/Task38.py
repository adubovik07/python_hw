# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, 
# и Вы должны реализовать функционал для изменения и удаления данных

# Показывает информацию в файле

base = dict()

n = "book.txt"

def edit_data(n):
    with open(n, "r") as data:
        tel_book = data.read()
        print(tel_book)
    print("")

index_delete_data = int(input("Введите номер строки для редактирования: ")) - 1
tel_book_lines = n.split("\n")
edit_tel_book_lines = tel_book_lines[index_delete_data]
elements = edit_tel_book_lines.split(" | ")
fio = input("Введите ФИО: ")
phone = input("Введите номер телефона: ")
num = elements[0]
if len(fio) == 0:
    fio = elements[1]
if len(phone) == 0:
    phone = elements[2]
edited_line = f"{num} | {fio} | {phone}"
tel_book_lines[index_delete_data] = edited_line
print(f"Запись — {edit_tel_book_lines}, изменена на — {edited_line}\n")
with open(n, "w") as f:
    f.write("\n".join(tel_book_lines))

def write_contacts(n):
    with open(n, "a") as file:
        file.write("\n" + input(f"Введите данные контакта: "))
        return file


def read_contacts(n):
    contacts = []
    with open(n, "r") as file:
        for line in file:
            name, surname, phone = line. strip().split(",")
            contact = {
                "name" : name,
                "surname" : surname,
                "phone" : phone
            }
            print (name, surname, phone)
            contacts.append(contact)
    return(contacts)


a = int(input("1 - ввод новой записи, 2 - вывод контактов \n"))
if a == 1:
    add_contacts = write_contacts(n)
elif a == 2:
    contacts = read_contacts(n)
elif a == 3:
    edit = edit_data(n)
else:
    print("Такой функции нет")
