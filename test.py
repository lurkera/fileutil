import fileutil as fu
from pathlib import Path

pth = r'D:\Documents\Desktop\ll'
pth = Path(pth)

result = fu.union_in_path_to_sheets(pth / 'rrr.xlsx', pth, file_type=['.*'])
print(result)

