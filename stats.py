def get_num_words(string):
    num_words = string.split()

    return len(num_words)

def get_unique_character_count(string):
    unique_character_count = {}

    for letter in string:
        if letter.lower() not in unique_character_count:
            unique_character_count[letter.lower()] = 1
        else:
            unique_character_count[letter.lower()] += 1
    return unique_character_count


def get_sorted_list(dictionary):
    final_list = []
    sorted_list = sorted(dictionary.values(), reverse=True)
    
    for sortedKey in sorted_list:
        for key, value in dictionary.items():
            if (f"{key}: {sortedKey}") in final_list:
                pass
            elif key.isalpha() and value == sortedKey:
                final_list.append(f"{key}: {sortedKey}")
            else:
                pass
    return final_list