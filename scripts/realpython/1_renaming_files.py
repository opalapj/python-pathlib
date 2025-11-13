from pathlib import Path


file_to_rename = Path().resolve() / "plain_list.md"
renamed_file = file_to_rename.with_suffix(".txt")

# 1st state - dir contains only .md file.
file_to_rename.replace(renamed_file)  # Works.
file_to_rename.rename(renamed_file)  # Works.

# 2nd state - dir contains both .md & .txt files.
file_to_rename.replace(renamed_file)  # Works.
file_to_rename.rename(renamed_file)  # Does not work - FileExistsError.
