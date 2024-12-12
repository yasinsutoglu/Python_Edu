import requests
import hashlib
import sys
# K-Anonymity: k-anonymity is a property possessed by certain anonymized data. k-anonymity is an
# attempt to solve the problem "Given person-specific field-structured data, produce a release of
# the data with scientific guarantees that the individuals who are the subjects of the data
# cannot be re-identified while the data remain practically useful." A release of data
# is said to have the k-anonymity property if the information for each person contained
# in the release cannot be distinguished from at least k-1 individuals whose information
# also appear in the release. The guarantees provided by k-anonymity are aspirational,
# not mathematical
def request_api_data(query_char):
  url = 'https://api.pwnedpasswords.com/range/' + query_char
  res = requests.get(url)
  if res.status_code != 200:    # 200 means all good!
    raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try again')
  return res

def get_password_leaks_count(hashes, hash_to_check):
  hashes = (line.split(':') for line in hashes.text.splitlines())
  for h, count in hashes:
    if h == hash_to_check:
      return count
  return 0

# HASH Function --> It is simply a function that generates a value of fixed length for eaxh input
# that it gets. (Some Types: SHA-1,SHA-256, MD5 ...)
def pwned_api_check(password):
  sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
  first5_char, tail = sha1password[:5], sha1password[5:]
  response = request_api_data(first5_char)
  # print(response.text)
  return get_password_leaks_count(response, tail)

def main(args):
  for password in args:
    count = pwned_api_check(password)
    if count:
      print(f'{password} was found {count} times... you should probably change your password!')
    else:
      print(f'{password} was NOT found. Carry on!')
  return 'done!'

if __name__ == '__main__':
  sys.exit(main(sys.argv[1:]))
  #sys.exit() make sure the program ends to the command line at last.

'''
this('https://api.pwnedpasswords.com/range/') website takes the first 5 digit of the 'SHA 1 hash'
so we actually generate a SHA 1 hash of our password and then just pass the first five digits of
the hash so we are keeping safe our hash, so that no one can even backtrace the password using 
our hash. and this website list all the hash starting with the 5 digits we have passed, 
and we can then manually check whether our password has been hacked or not
'''