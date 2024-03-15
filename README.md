# Python Script to Rename Files

This Python script renames files within a specified directory by prefixing them with a three-digit sequential number.

## Usage

```
python renban.py [options] path extension
```

### Arguments

- `path`: Directory path where files are located.
- `extension`: File extension to filter files.

## Example

```bash
python renban.py /path/to/directory txt
```

## Notes

- Ensure that the directory path provided exists and contains files with the specified extension.
- The script will rename the files within the directory by adding a three-digit sequential number as a prefix to the original file name.

## Help

For additional help, run the script with the `-h` or `--help` option.

```bash
python renban.py -h
```
