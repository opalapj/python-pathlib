import datetime
from pathlib import Path


print(Path())
print(Path().absolute())
print(Path.cwd())
print(Path.home())
print(Path(__file__))


# classmethod Path.cwd()
# Return a new path object representing the current directory (as returned by os.getcwd()):
path = Path.cwd()


# classmethod Path.home()
# Return a new path object representing the user’s home directory (as returned by os.path.expanduser() with ~ construct).
# If the home directory can’t be resolved, RuntimeError is raised.
path = Path.home()


# 3 ways to create path from segments:
Path.home().joinpath("rest")
Path.home() / "rest"
Path(Path.home(), "rest")

Path("C:/Windows").joinpath("/Program Files")
Path("C:/Windows") / "/Program Files"
Path("C:/Windows", "/Program Files")


# The string representation of a path is the raw filesystem path itself (in native form, e.g. with backslashes under Windows),
# which you can pass to any function taking a file path as a string:
str(Path.cwd())


# Accessing individual parts
Path(__file__).parts


# A string representing the drive letter or name, if any:
Path(__file__).drive


# A string representing the (local or global) root, if any:
Path(__file__).root


# The concatenation of the drive and root:
Path(__file__).anchor


# An immutable sequence providing access to the logical ancestors of the path:
Path().parents[0]  # Invalid for relative paths.
Path(__file__).parents[0]
Path(__file__).parents[1]
Path(__file__).parents[5]


# A string representing the final path component, excluding the drive and root, if any:
Path(__file__).name
Path("C:/Windows").name
Path("C:").name


# The file extension of the final component, if any:
Path("my/library/setup.py").suffix
Path("my/library.tar.gz").suffix
Path("my/library").suffix


# A list of the path’s file extensions:
Path("my/library/setup.py").suffixes
Path("my/library.tar.gz").suffixes
Path("my/library").suffixes


# The final path component, without its suffix:
Path("my/library.tar.gz").stem
Path("my/library.tar").stem
Path("my/library").stem


# Represent the path as a file URI. ValueError is raised if the path isn’t absolute.
Path().as_uri()
Path(__file__).as_uri()


# Return whether the path is absolute or not. A path is considered absolute if it has both a root and (if the flavour allows) a drive:
Path().is_absolute()
Path(__file__).is_absolute()


# Return whether this path is relative to the other path.
Path(__file__).is_relative_to(Path(__file__).parent.parent)
Path(__file__).is_relative_to(Path(r"C:/Program Files"))


# PurePath.is_reserved()
# With PureWindowsPath, return True if the path is considered reserved under Windows, False otherwise.
Path("nul").is_reserved()


# PurePath.match(pattern, *, case_sensitive=None)
# The pattern may be another path object; this speeds up matching the same pattern against multiple files:
Path(__file__).match("*.py")
Path(__file__).match("python-pathlib/*.py")
Path(__file__).match("python-pathlib/*/*.py")


# Path.glob(pattern, *, case_sensitive=None)
list(Path("D:/Dane/opalapi/data/programming/github").glob("python-pathlib/*.py"))
list(Path("D:/Dane/opalapi/data/programming/github").glob("python-pathlib/*/*.py"))
list(Path("D:/Dane/opalapi/data/programming/github").glob("python-pathlib/**/*.py"))


# Path.relative_to(other, walk_up=False)
# Compute a version of this path relative to the path represented by other. If it’s impossible, ValueError is raised:
Path(__file__).relative_to(Path().absolute())
Path(__file__).relative_to(Path().absolute().parent)
Path(__file__).relative_to(Path().absolute().parent.parent)

Path().absolute().relative_to(Path(__file__), walk_up=True)
Path().absolute().parent.relative_to(Path(__file__), walk_up=True)
Path().absolute().parent.parent.relative_to(Path(__file__), walk_up=True)


# PurePath.with_name(name)
Path(__file__).with_name("new_name.txt")


# PurePath.with_stem(stem)
Path(__file__).with_stem("new_name")


# PurePath.with_suffix(suffix)
Path(__file__).with_suffix(".txt")


# Path.stat(*, follow_symlinks=True)
stat = Path(__file__).stat()
datetime.datetime.fromtimestamp(stat.st_mtime).strftime("%A, %d. %B %Y %H:%M")


# Path.exists(*, follow_symlinks=True)
Path(__file__).exists()
Path(__file__).with_stem("new").exists()


# Path.is_dir()
Path(__file__).is_dir()
Path().is_dir()


# Path.is_file()
Path(__file__).is_file()
Path().is_file()


# Path.is_mount()
# On Windows, a mount point is considered to be a drive letter root (e.g. c:/), a UNC share (e.g. //server/share), or a mounted filesystem directory.
Path("C:/Windows").is_mount()  # False
Path("C://").is_mount()  # True
Path("//orlen.pl/Office/DR").is_mount()  # False
Path("//orlen.pl/Office").is_mount()  # True


# Path.iterdir()
# When the path points to a directory, yield path objects of the directory contents:
list(Path(__file__).iterdir())
list(Path().iterdir())


# Path.walk(top_down=True, on_error=None, follow_symlinks=False)
for dir, subdirs, files in Path().walk():
    print(f"Walked dir: {dir}")
    print("Subdirs:")
    for subdir in subdirs:
        print(dir / subdir)
    print("Files:")
    for file in files:
        print(dir / file)


# Path.open(mode='r', buffering=-1, encoding=None, errors=None, newline=None)
with Path("data/extra.py").open(encoding="utf-8") as src:
    content = src.read()
    print(content)


# Path.rename(target)
# On Windows, if target exists, FileExistsError will be raised.
Path("data/extra.py").rename(
    "data/super.py"
)  # On Windows, if target exists, FileExistsError will be raised.
Path("data/extra.py").rename("data/amazing.py")
Path("data/super.py").rename("data/extra.py")
Path("data/extra.py").rename(
    "amazing.py"
)  # Which is equal to moving file from one directory to another.
Path("amazing.py").rename("data/extra.py")


# Path.replace(target)
# If target points to an existing file or empty directory, it will be unconditionally replaced.
Path("data/extra.py").replace(
    "data/super.py"
)  # On Windows, if target exists, FileExistsError will be raised.


# Path.absolute()
# Make the path absolute, without normalization or resolving symlinks. Returns a new path object:
Path().absolute()
Path(
    ".."
).absolute()  # WindowsPath('D:/Dane/opalapi/data/programming/study/python/my/pathlib_/..')


# Path.resolve(strict=False)
# Make the path absolute, resolving any symlinks. A new path object is returned:
Path().resolve()
Path("..").resolve()  # WindowsPath('D:/Dane/opalapi/data/programming/study/python/my')


# Path.mkdir(mode=0o777, parents=False, exist_ok=False)
Path("data/new_dir").mkdir()
Path("data/new_dir/next_level").mkdir()
Path("data/new_dir/next_level").mkdir(parents=True)
Path("data/new_dir/next_level").mkdir(parents=True, exist_ok=True)


# Path.rmdir()
# Remove this directory. The directory must be empty.
Path("data/new_dir").rmdir()
for dir, subdirs, files in Path("data/new_dir").walk(top_down=False):
    # print(repr(dir))
    dir.rmdir()
Path(
    "data/example"
).rmdir()  # OSError: [WinError 145] Katalog nie jest pusty: 'example'


# Path.touch(mode=0o666, exist_ok=True)
# Create a file at this given path.
Path("data/new_file.py").touch()


# Path.unlink(missing_ok=False)
# Remove this file or symbolic link.
Path("data/new_file.py").unlink()


# Path.write_text(data, encoding=None, errors=None, newline=None)
# Open the file pointed to in text mode, write data to it, and close the file.
Path("data/new_text_file.txt").write_text("cześć i czołem")
Path("data/new_text_file.txt").write_text("cześć i czołem", encoding="utf-8")


# Path.read_text()
Path("data/new_text_file.txt").read_text()
Path("data/new_text_file.txt").read_text(encoding="utf-8")


# Path.write_bytes(data)
# Open the file pointed to in bytes mode, write data to it, and close the file.
# Path('new_binary_file').write_bytes(b'cześć i czołem')  # SyntaxError: bytes can only contain ASCII literal characters.
Path("data/new_binary_file").write_bytes(bytes("cześć i czołem", "utf-8"))


# Path.read_bytes()
content = Path("data/new_binary_file").read_bytes()
content.decode()
str(content, "utf-8")
