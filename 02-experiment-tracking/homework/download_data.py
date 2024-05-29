import urllib.request

# List of URLs to download
urls = [
    "https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2023-01.parquet",
    "https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2023-02.parquet",
    "https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2023-03.parquet"
]

# Directory to save the files
save_directory = "data/"

# Function to download a single file
def download_file(url, save_directory):
    file_name = url.split("/")[-1]
    file_path = f"{save_directory}/{file_name}"
    urllib.request.urlretrieve(url, file_path)
    print(f"File downloaded and saved as {file_path}")

# Loop through each URL and download the file
for url in urls:
    download_file(url, save_directory)
