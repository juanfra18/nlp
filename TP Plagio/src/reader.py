import textract

def file_reader(path):
    return str(textract.process(path).decode("utf-8"))
