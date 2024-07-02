from json import load, dump

class FileManager:
    def load_data(self, filename):
        # reads the contents of the `filename` file and returns the text
        with open(filename, "r") as file:    
            return file.read()

    def save_data(self, filename, data):
        # writes the contents of `data` to the file `filename`
        with open(filename, "w") as file:
            file.write(data)

    def read_json(self, json_file_path):
        # reads the contents of a file whose path is stored in the `json_file_path` variable 
        # and returns a list of dictionaries
        with open(json_file_path, "r") as file:
            return load(file)
        
    def write_json(self, list_of_dicts, json_file_path):
        # writes a list of dictionaries from list_of_dicts to the `json_file_path` file
        with open(json_file_path, "w") as file:
            dump(list_of_dicts, file, indent="\t")

    def add_to_json(self, data, json_file_path):
        # gets the dictionary in the data variable and adds it to the JSON `json_file_path`
        data_json = self.read_json(json_file_path)
        data_json.append(data)
        self.write_json(data_json, json_file_path)

