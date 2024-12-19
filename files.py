"""
примеры работы с текстовыми файлами
"""
with open("models.txt","w") as f:
    f.write("hello\n")
    f.write("ФИО\n")
    f.write("чем увлекается\n")
    f.write("возраст\n")


with open("models.txt","r") as f:
    result = f.readline()
    result1 = f.readline()
    result2 = f.readline()
    print(f"############################################\n {result}\n ############################################\n {result1}\n ############################################\n {result2}\n ############################################\n")


