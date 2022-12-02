# 35. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
def get_list_from_file(file_name):
    with open(file_name) as f:
        lst = f.read()
    print(lst)
    k = str(lst.split(" + "))
    # k = str(k)
    k = k.replace("'", "").replace("[", "").replace("]", "").replace(", ", " ").replace(" - ", " -").replace(" = 0", "")
    k = k.split(" ")
    out = {}
    for i in k:
        if "x2" in i:
            out["x2"] = int(i.replace("*", "").replace("x2", ""))
            continue
        if "x" in i:
            out["x"] = int(i.replace("*", "").replace("x", ""))
            continue
        else:
            out["num"] = int(i)
    return out


f1 = get_list_from_file("f_file.txt")
f2 = get_list_from_file("s_file.txt")
x2 = f1.get("x2", 0) + f2.get("x2", 0)
x = f1.get("x", 0) + f2.get("x", 0)
num = f1.get("num", 0) + f2.get("num", 0)
with open("out_resul.txt", "w") as file:
    file.write(f"{x2}*x2 {'+' if x > 0 else ''} {x}*x {'+' if num > 0 else ''} {num} = 0")
get_list_from_file("out_resul.txt")  # Добавлено для вывода в консоль
