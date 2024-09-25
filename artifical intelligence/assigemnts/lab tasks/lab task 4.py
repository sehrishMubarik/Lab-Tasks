class LuhnValidator:
    def __init__(self, card_number):
        self.card_number = card_number
    
    def validate(self):
        card_number = [int(x) for x in str(self.card_number)]  
        checksum = 0

        card_number.reverse()

        for i, num in enumerate(card_number):
            if i % 2 == 1:  
                num *= 2
                if num > 9:  
                    num -= 9
            checksum += num

        return checksum % 10 == 0 


card_validator = LuhnValidator(4532015112830366)
is_valid = card_validator.validate()
print(f"Card number is valid: {is_valid}")


class PunctuationRemover:
    def __init__(self, text):
        self.text = text

    def remove_punctuation(self):
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        result = ''

        for char in self.text:
            if char not in punctuations:
                result += char 

        return result


text = "Hello, world! How's it going?"
punctuation_remover = PunctuationRemover(text)
cleaned_text = punctuation_remover.remove_punctuation()
print(f"Original: {text}")
print(f"Without punctuation: {cleaned_text}")


class WordSorter:
    def __init__(self, text):
        self.text = text

    def sort_words(self):
        words = self.text.split() 
        n = len(words)

        for i in range(n):
            for j in range(0, n - i - 1):
                if words[j].lower() > words[j + 1].lower():  
                    words[j], words[j + 1] = words[j + 1], words[j]  

        return ' '.join(words)

text = "Sorting these words in alphabetical order"
word_sorter = WordSorter(text)
sorted_text = word_sorter.sort_words()
print(f"Original: {text}")
print(f"Sorted: {sorted_text}")
