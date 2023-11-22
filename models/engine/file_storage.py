#!/usr/bin/python3
"""
'''python class for our Filestorage class'''

class FileStorage:
    ''' this class handles serialization and deserialization of data structures and vice versere
    '''
    
    self.__file_path = "file.json"# The path to the json file
    self.__objects = {}# empty dictionary 

    def all(self):
        '''Returns the dictionary __object'''
        return FileStorage.__object

    def new(self, obj):
        '''sets in __objects the obj with key <obj Class name>.id'''
        key = f"{type(obj).__name__}.id"
        FileStorage.__objects[key] = obj

    def save(self):
        '''serializes __objects to the JSON file path
        '''
        with open(FileStorage.file.path, "w", encoding="utf-8") as f:
            for key, value in FileStorage.__objects.items():
                FileStorage.__objects[key] = obj.to_dict()

                json.dump(FileStorage.__object, file)
    def reload(self):
        '''deserializes the json file to "__objects
        '''
        if not os.path.isfile(FileStorage.__file_path):
            return 
        with open(FileStorage.__file_path) as f:
          obj_dict = json.load(f)
          json.dump(FileStorage.__object, file)
