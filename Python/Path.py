import site

lib_paths = site.getsitepackages()
print("Python library paths:")
for path in lib_paths:
    print(path)
