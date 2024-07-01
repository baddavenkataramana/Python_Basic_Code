def nearest_vowel(c):
    vowels = 'AEIOU'
    distances = {v: abs(ord(c) - ord(v)) for v in vowels}
    return min(distances, key=distances.get)

def replace_and_convert(s):
    upper_count = sum(1 for c in s if c.isupper())
    lower_count = sum(1 for c in s if c.islower())
    
    replaced_string = ''.join(nearest_vowel(c) if c.isupper() else c for c in s)
    
    if upper_count > lower_count:
        return replaced_string.upper()
    elif upper_count < lower_count:
        return replaced_string.lower()
    else:
        return replaced_string.title()

# Sample Input
input_string = "JndHB"
# Sample Output
output_string = replace_and_convert(input_string)
print(output_string)  # Output: INDIA
