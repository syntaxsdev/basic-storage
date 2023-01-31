import json, hashlib, time


#Standalone method
def md5key() -> str:
    return hashlib.md5(str(time.time()).encode()).hexdigest()

class new:
    _storage:dict = {}

    def __init__(self):
        pass
 
    #ADD TO ROOT FOLDER
    def add(self, data, key=None, convert_json=False) -> str:
        '''
        Add data to root folder at the data key
        '''
        key = md5key() if key is None else key
        self._storage[key] = json.dumps(data) if convert_json else data
        return key

    def insert(self, data, key=None, convert_json=False) -> str:
        '''
        Insert data into a list, and create one if needed.
        *Note this overrides any data stored at this root-key if it is not a list.
        '''
        key = md5key() if key is None else key
        if self._storage.get(key) is None or type(self._storage.get(key)) is not list:
            self._storage[key] = []
            self._storage[key].append(json.dumps(data) if convert_json else data)
        else:
            self._storage[key].append(json.dumps(data) if convert_json else data)
        return key

    def get(self, key, from_json=False):
        '''
        Get the data stored at the root folder at the data key
        '''
        return self._storage.get(key) if from_json == False else json.loads(self._storage.get(key))

    def pop(self, key, from_json=False):
        '''
        Pop the data at the root folder at the data key
        '''
        return self._storage.pop(key) if from_json == False else json.loads(self._storage.pop(key))

    def delete(self, key) -> bool:
        '''
        Delete the data at the root folder at the data key
        Can also be used to delete folders.
        '''
        del self._storage[key]
        return True

    def createFolder(self, key=None) -> str:
        '''
        Create a folder, and return a generated key unless specified
        '''
        key = md5key() if key is None else key
        self._storage[key] = {}
        return key

    #ADD DATA TO A FOLDER
    def addf(self, folder_key, data, key=None, convert_json=False) -> str:
        '''
        Add data to a folder given folder_key at the data key
        '''
        key = md5key() if key is None else key
        self._storage[folder_key][key] = data
        return key
    
    def getf(self, folder_key, key, from_json=False):
        '''
       Get data from a folder given folder_key and data key
        '''
        return self._storage[folder_key].get(key) if from_json == False else json.loads(self._storage[folder_key].get(key))

    def insertf(self, folder_key, data, key=None, convert_json=False) -> str:
        '''
        Insert data into a list at a folder at data key, and create one if needed.
        *Note this overrides any data stored at this data key.
        '''
        key = md5key() if key is None else key
        if self._storage[folder_key].get(key) is None or type(self._storage[folder_key].get(key)) is not list:
            self._storage[folder_key][key] = []
            self._storage[folder_key][key].append(json.dumps(data) if convert_json else data)
        else:
            self._storage[folder_key][key].append(json.dumps(data) if convert_json else data)
        return key

    def deletef(self, folder_key, key) -> bool:
        '''
        Delete the data in the folder at the data key
        '''
        del self._storage[folder_key][key]
        return True

    def popf(self, folder_key, key, from_json=False):
        '''
        Pop the data at the folder at the data key
        '''
        return self._storage[folder_key].pop(key) if from_json == False else json.loads(self._storage[folder_key].pop(key))