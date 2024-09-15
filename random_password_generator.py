# MIT License
 
# Copyright (c) 2024 Lawi Corp

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import secrets
import string

vi = ["very strong", "strong", "normal", "weak", "all"] # all the valid inputs "vi."

diff_char_dict = {vi[0]: [string.ascii_letters, string.digits, string.punctuation], vi[1]: [string.ascii_letters, string.digits], vi[2]: [string.ascii_letters], vi[3]: [string.ascii_lowercase]} # different password difficulties and their character sets (used characters).

diff_len_dict = {vi[0]: 19, vi[1]: 14, vi[2]: 9, vi[3]: 8} # different password difficulties and their lengths.

def generate_password(length, characters):
    if not characters:
        print("Value Error: Character set not found."); return()

    return ''.join([secrets.choice(characters) for _ in range(length)])

def main():
    strength = input("Specify the desired password strength (Very Strong, Strong, Normal, Weak, All) >>> ").lower()

    if strength not in vi:
        print("Value Error: Input not recognized. Please try again."); main(); return()
    elif strength in vi[:-1]:
        print(generate_password(diff_len_dict[strength], ''.join(diff_char_dict[strength])))
    else:
        for u in range(4):
            strength = list(diff_char_dict.keys())[u]
            print(f"{strength.capitalize()} password: {generate_password(diff_len_dict[strength], ''.join(diff_char_dict[strength]))}")

    main()

if __name__ == "__main__":
    main()
