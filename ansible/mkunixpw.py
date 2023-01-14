#!/usr/bin/env python3

import crypt;
import getpass;

if __name__ == '__main__':
  password = getpass.getpass();

  if (password == getpass.getpass('Confirm: ')):
    print(crypt.crypt(password));
