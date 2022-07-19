class FileOperations():
        def readFromFile(self):
            txt_file_given = str(input("Enter the file for Lexical Analysis: "))
            
            try:
                with open(txt_file_given , encoding="utf8") as f:
                    text = f.readline()
                f.close()
                return text
                
            except FileNotFoundError as e:
                 print("File was not fond.\nError message: {}".format(str(e)))

        def writeToFile(self,tokens):
            with open("tokenized_text.txt", "w+", encoding = "utf8") as f:
                for sentance in tokens:
                    f.write(str(sentance) + "\n")
            f.close()         
            print("Created tokenized text successfully.")
    
