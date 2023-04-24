def create_string_hash_map(astring):
    hash_map = {}
    for word in astring.lower().split():
        if not word[-1]
        if key in dict:
          dict[key]  += 1
        else:
          dict[key] = 1
         """
        hash_map[word] = hash_map.get(word,0)
    return hash_map

def create_string_hash_map_handle_contractions(astring):
    hash_map = {}

    for word in astring.lower().split():
        word = word.split("'")
        print(word)
        while word:
          current_word = word.pop()
          hash_map[current_word] = hash_map.get(current_word,0)+1
    return hash_map