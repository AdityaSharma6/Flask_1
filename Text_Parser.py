class Text_Text_Extraction():
    def __init__(self, file_name):
        self.file_name = file_name
    
    def text_extraction(self):
        with open(self.file_name) as data:
            contents = data.readlines()
            #print(contents)

            counter = 0
            while counter in range(len(contents)):
                if (contents[counter] == "\n"):
                    contents.pop(counter)
                    continue
                contents[counter] = contents[counter][:-1]
                counter += 1
                
            
        text = " ".join(contents)
        #print(text)
        return text

    def execute(self):
        self.text_extraction()