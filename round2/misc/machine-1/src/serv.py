#!/usr/bin/env python3 
import os
import subprocess

def run_command(command):
  try:
    result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
    return result
  except subprocess.CalledProcessError as e:
    return e.output

def run() -> None:
  while True:
    user_input = input("$ ")
    if user_input.lower() in ['exit', 'quit']:
      break
    elif ' ' in user_input:
      user_input = user_input.replace(' ', '')

    output = run_command(user_input)
    print(output)

if __name__ == '__main__':
  run() 