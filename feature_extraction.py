from urllib.parse import urlparse

def extract_features(url):
    features = []

    features.append(len(url))                     # URL length
    features.append(url.count('.'))               # dot count
    features.append(url.count('-'))               # hyphen count
    features.append(url.count('@'))               # @ symbol
    features.append(url.count('?'))               # ?
    features.append(url.count('%'))               # %
    features.append(url.count('='))               # =
    features.append(len(urlparse(url).netloc))    # domain length
    features.append(1 if url.startswith("https") else 0)  # HTTPS

    return features
