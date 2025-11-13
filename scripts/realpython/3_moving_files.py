from pathlib import Path


file_to_move = Path().resolve() / "plain_list.md"
destination = file_to_move.with_suffix(".txt")

# Note that if the destination already exists, then .replace() will overwrite it.
# To avoid possibly overwriting the destination path, you can test whether the destination exists before replacing:
# if not destination.exists():
#     file_to_move.replace(destination)

# However, this does leave the door open for a possible race condition.
# Another process may add a file at the destination path between the execution
# of the if statement and the .replace() method.
# If that’s a concern, then a safer way is to open the destination path for
# exclusive creation then explicitly copy the source data and
# delete the source file afterward. (try clause, below).

# My solution: use .rename() method - on Windows, if target exists, FileExistsError will be raised.


# 1st state - destination dir does not contain 'new_text_file.txt' file.
file_to_move.replace(destination)  # Works.
file_to_move.rename(destination)  # Works.

try:
    with destination.open(mode="xb") as file:
        file.write(file_to_move.read_bytes())
except FileExistsError:
    print(f"File {destination} exists already.")
except FileNotFoundError:
    print(f"File {file_to_move} does not exist.")
    destination.unlink()
else:
    file_to_move.unlink()
finally:
    print("Attempt completed.")


# 2nd state - destination dir contains 'new_text_file.txt' file.
file_to_move.replace(destination)  # Works.
file_to_move.rename(destination)  # Does not work - FileExistsError.

try:
    with destination.open(mode="xb") as file:
        file.write(file_to_move.read_bytes())
except FileExistsError:
    print(f"File {destination} exists already.")
except FileNotFoundError:
    print(f"File {file_to_move} does not exist.")
    destination.unlink()
else:
    file_to_move.unlink()
finally:
    print("Attempt completed.")
