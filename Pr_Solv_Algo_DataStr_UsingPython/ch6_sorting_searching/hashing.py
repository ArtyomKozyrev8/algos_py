from typing import List, Union, Any


class HashTable:
    def __init__(self, max_elements: int = 11):
        self._n: int = max_elements  # HashTable maximum size
        self._keys: List[Union[int, None]] = [None for _ in range(max_elements)]
        self._values:  List[Union[Any, None]] = [None for _ in range(max_elements)]

    def _hash_function(self, key: int) -> int:
        """Use the function to create key. This is one (the easiest) ways to create such function"""
        return key % self._n

    def _rehash_function(self, old_hash_key: int) -> int:
        """The rehash function is used if the old_key already exists in HashTable"""
        return (old_hash_key + 1) % self._n

    def __len__(self) -> int:
        temp_key_len = [i for i in self._keys if i is not None]
        temp_val_len = [i for i in self._values if i is not None]

        if len(temp_key_len) == len(temp_val_len):
            return len(temp_key_len)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({list(zip(self._keys, self._values))})"

    def _set(self, key: int, value: Any) -> None:
        start_hash_key = self._hash_function(key)
        if self._keys[start_hash_key] is None:
            self._keys[start_hash_key] = key
            self._values[start_hash_key] = value
        else:
            if self._keys[start_hash_key] == key:
                self._values[start_hash_key] = value  # replace old value with a new one value
            else:
                cur_hash_key = self._rehash_function(start_hash_key)
                while self._keys[cur_hash_key] is not None and self._keys[cur_hash_key] != key:
                    cur_hash_key = self._rehash_function(cur_hash_key)
                    if cur_hash_key == start_hash_key:
                        raise IndexError("Too many elements in HashTable")

                if self._keys[cur_hash_key] is None:
                    self._keys[cur_hash_key] = key
                    self._values[cur_hash_key] = value
                else:
                    self._values[cur_hash_key] = value

    def _get(self, key: int) -> Union[Any, None]:
        start_hash_key = self._hash_function(key)
        hash_key = start_hash_key
        while True:
            if self._keys[hash_key] == key:
                return self._values[hash_key]
            if self._keys[hash_key] is None:
                return None  # key does not exist
            hash_key = self._rehash_function(hash_key)
            if hash_key == start_hash_key:
                return None  # key does not exist

    def _delete(self, key: int) -> None:
        start_hash_key = self._hash_function(key)
        hash_key = start_hash_key
        while True:
            if self._keys[hash_key] == key:
                self._keys[hash_key] = None
                self._values[hash_key] = None
                return None
            elif self._keys[hash_key] is None:
                return None  # key does not exist
            else:
                hash_key = self._rehash_function(hash_key)
                if hash_key == start_hash_key:
                    return None  # key does not exist

    def __setitem__(self, key: int, value: Any) -> None:
        self._set(key, value)

    def __getitem__(self, key: int) -> Union[Any, None]:
        return self._get(key)

    def __delitem__(self, key: int) -> None:
        return self._delete(key)

    def __contains__(self, key: int) -> bool:
        if self._get(key) is not None:
            return True
        return False
