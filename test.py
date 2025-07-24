import torch

torch.hub.download_url_to_file("https://example.com", "/tmp/unsafe", hash_prefix=None)
