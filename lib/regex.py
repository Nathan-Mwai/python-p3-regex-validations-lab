import re

# NOTE: There are only a few tests included, so multiple solutions will work.
# Feel free to encourage students to find oversights and add tests to this lab!
# \-' checks for apostrophes and hyphens
# \s checks for spaces
#  $ ensures there are no extra characters
#  * checks how many times the words are repeating i.e first name , second name etc

name = r"^[A-Z][A-z\-']*(?:\s[A-Z][A-z\-']*)*$"
name_regex = re.compile(name)

phone_number = r"^\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$"
phone_regex = re.compile(phone_number)

email_address = r"^[A-z][A-z0-9._%+-]+\@[A-z0-9.-]+\.[A-z]{2,}$"
email_regex = re.compile(email_address)
