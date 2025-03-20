import kaggle

# Download the dataset
kaggle.api.authenticate()
kaggle.api.dataset_download_files('shreyanshverma27/online-sales-dataset-popular-marketplace-data', path='data/', unzip=True)