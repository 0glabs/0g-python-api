# 0G-PYTHON-API
Quick and dirty python API to access 0g's decentralized data storage system. This is provided without warranty, and is intended solely for research/protopying. For production-ready use, please refrence the Go or command-line tools.

https://docs.0g.ai/0g-doc/docs/0g-storage/access-storage-through-cli (CLI Tool docs)
https://docs.0g.ai/0g-doc/docs/0g-storage/sdk (Go SDK docs)

## Methods: 
***Upload*** 
```Upload(file_path, indexer, private_key, url="", contract="0xbD2C3F0E65eDF5582141C35969d66e34629cC768", tags="0x", expected_replica=1, finality_required=True, skip_tx=False, task_size=10, fee=0) -> tuple(status_message, merkle_root)```
Uploads a file to the 0G chain, returns a tuple with the status_message, merkle_root.  
If successful, status_message is "Success" and merkle_root contains the Merkle hash.
If failed, status_message contains error details and merkle_root is None.

```Download(filename, root) -> (filename, status_message).```
Downloads a the file specified by "root" from the 0G data storage system, saves to filename given. Returns a tuple containing (filename, status_message).
If successful, status_message is "Success".
If failed, status_message contains error details.

## Example:
The file `example.py` has some example usage. For feature requests, bugs, and reports, please file an issue on this repository.

## Install
Install using the command ```pip install git+https://github.com/0glabs/zerog_python_api.git#egg=zerog_python_api```
