import os


class Organize:
    refer = {
        "Images": [".jpg", ".png", ".bmp", ".jpeg"],
        "Python Files": [".py", ".pyw"],
        "Documents": [".txt", ".rtf", ".docx", ".doc"],
        "Compressed": [".rar"]
    }

    assign = {
        "Images": [],
        "Python Files": [],
        "Documents": []
    }

    def __init__(self, main_path):
        self.main_path = main_path

    def get_names(self):
        path = self.main_path
        d = self.refer
        fin = self.assign
        print(self.main_path)
        for filename in os.listdir(os.path.abspath(path)):
            base_file, ext = os.path.splitext(filename)
            for x in d.keys():
                if ext in d[x]:
                    print("'" + filename + "'", "belongs in", x, "Folder")
                    fin[x].append(filename)
        print(fin)

    def arrange(self):
        path = self.main_path
        fin = self.assign
        # create Folders
        for x in fin.keys():
            try:
                os.mkdir(path + x)
            except OSError:
                print("Creation of the directory %s failed" % path)

        for y in fin.keys():
            if len(fin[y]) > 0:
                for file in fin[y]:
                    os.rename(path + file, path + y + "\\" + file)


o = Organize(os.path.dirname(os.path.realpath(__file__)) + "\\Test folder\\")

o.get_names()
o.arrange()
