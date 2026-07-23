import kagglehub

path_garbage_collector = kagglehub.dataset_download(
    "asdasdasasdas/garbage-classification"
    )

path_trashnet = kagglehub.dataset_download(
    "feyzazkefe/trashnet"
    )

path_taco = kagglehub.dataset_download(
    "kneroma/tacotrashdataset"
    )


print("Path to dataset files:", path_garbage_collector)
print("Path to dataset files:", path_trashnet)
print("Path to dataset files:", path_taco)