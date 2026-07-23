import kagglehub

path_garbagecollector = kagglehub.dataset_download(
    "asdasdasasdas/garbage-classification"
    )

path_tacotrash = kagglehub.dataset_download(
    "kneroma/tacotrashdataset"
    )

path_trashnet = kagglehub.dataset_download(
    "feyzazkefe/trashnet"
    )

print("Path to dataset files:", path_trashnet)
print("Path to dataset files:", path_garbagecollector)
print("Path to dataset files:", path_tacotrash)