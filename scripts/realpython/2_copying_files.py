from pathlib import Path


file_to_copy = Path().resolve() / "plain_list.md"
copy_ = file_to_copy.with_stem("_".join((file_to_copy.stem, "copy")))
copy_.write_bytes(file_to_copy.read_bytes())
