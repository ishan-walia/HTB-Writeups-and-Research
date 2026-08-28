import os
path="test.txt"
if os.path.isfile(path):
  print("file found")
elif os.path.isdir(path):
  print("Directory found")
else:
  print("Not found")
