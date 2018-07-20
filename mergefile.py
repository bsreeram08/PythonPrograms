from datetime import datetime
with open("file1.txt","r") as file1:
    with open("file2.txt","r") as file2:
        with open("file3.txt","r") as file3:
            with open(datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")+".txt", 'w') as newfile:
                    newfile.write(file1.readline())
                    newfile.write("\n")
                    newfile.write(file2.readline())
                    newfile.write("\n")
                    newfile.write(file3.readline())
                    newfile.write("\n")
                    print(newfile)
