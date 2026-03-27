# from pathlib import Path
# p = Path('dummy.py')
# with open('dummy.py', encoding='utf-8') as f:
#     print(f.readlines())
    
# print(p.read_text())
# print(p.read_bytes())


# print(p.write_text('Text file contents'))
# print(p.read_text())


# print(p.write_bytes(b'Text file contents in bytes'))
# print(p.read_bytes())

# p = Path('dum1')
# for child in p.iterdir(): print(child)

# # pa=Path('dum')
# # pa.touch()
# pa1=Path('dum1')
# # pa1.mkdir()
# print(pa1.exists())
# path2=Path('.')
# print(list(path2.glob('*.py')))

# from pathlib import Path
# pat=Path('dum')
# print(pat.exists())
# print(pat.read_text())
# pat.open()
# print(dir(pat))

# f = open("dum1/sxj.txt", "r")

# print(f.fileno())
# f.close()

# f = open("dum1/sxj.txt", "r")
# f.seek(17)
# print(f.readline())


f = open("dum1/sxj.txt", "a")
f.truncate()
f.close()

#open and read the file after the truncate:
f = open("dum1/sxj.txt", "r")
print(f.read())



from pathlib import Path

p=Path(__file__)

p=p.resolve().parents[0]

print(p)

s=p/'home'

x=Path(s)
# x.mkdir()

import os

# Simple rename
print(s)
s=Path(__file__)
print(s)

y='/home/cis/Documents/Vinshul/Coma/Learning/home'
os.renames('swayam/dhamunia/newname','swayam')

# Rename and create missing parent directories if needed
# os.renames("old_dir", "new_parent/new_child/renamed_directory")