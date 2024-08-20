from zerog_python_api import upload, download
import os

# Constants
TESTNET_SK = ""
CONTRACT_ADDRESS = "0xbD2C3F0E65eDF5582141C35969d66e34629cC768"
RPC_URL = "https://evmrpc-test-us.0g.ai"
INDEXER_URL = "https://rpc-storage-testnet-turbo.0g.ai"

def upload_file(file_path: str) -> tuple[str, str]:
    """
    Upload a single file using the 0G Storage Client API.

    Args:
    file_path (str): The full path to the file to be uploaded.

    Returns:
    tuple: (file_path, status_message)
           If successful, status_message is "Success".
           If failed, status_message contains error details.
    """
    try:
        result = upload(
            file_path=file_path,
            tags="0x",  # Default tag
            url=RPC_URL,
            indexer=INDEXER_URL,
            contract=CONTRACT_ADDRESS,
            private_key=TESTNET_SK,
            expected_replica=1,
            finality_required=True,
            skip_tx=False,
            task_size=10,
            fee=0  # Let it be computed automatically
        )
        # print(f"LOW_LEVEL={result}")
        return result
    except Exception as e:
        return file_path, f"Error: {str(e)}"

# Example usage
if __name__ == "__main__":
    file_to_upload = "example.txt"
    merkle_root, status = upload_file(file_to_upload)
    while (status != "Success"):
        merkle_root, status = upload_file(file_to_upload)
        if status == "Success":
            print(f"File '{file_to_upload}' uploaded successfully!")
            break
        else:
            print(f"Upload failed: {status}")
    download_location = "down.txt"
    # print(f"MERKLE_ROOT={merkle_root}, STATUS = {status}")
    # (file_path, status) = download(download_location, merkle_root)
    # if status == "Success":
    #     print(f"File '{download_location}' uploaded successfully!")
    # else:
    #     print(f"Upload failed: {status}")