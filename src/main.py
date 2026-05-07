import numpy as np

FILENAME = "../Teen_Mental_Health_Dataset.csv"

def data_preprocessing(filename = FILENAME) -> object:
    data = np.genfromtxt(fname=FILENAME, delimiter=",", dtype=None, skip_header=1, encoding='utf-8')
    
    gender_encoded = np.where(data['f1'] == 'female', 1, 0)

    interaction_encoded = np.zeros(data.shape[0])
    interaction_encoded[data['f8'] == 'medium'] = 1
    interaction_encoded[data['f8'] == 'high'] = 2

    is_instagram = np.where(data['f3'] == 'Instagram', 1, 0)
    is_tiktok = np.where(data['f3'] == 'TikTok', 1, 0)
    is_both = np.where(data['f3'] == 'Both', 1, 0)
    
    X = np.column_stack((
    data['f0'],
    gender_encoded,
    data['f2'],
    is_instagram,
    is_tiktok,
    is_both,
    data['f4'],
    data['f5'],
    data['f6'],
    data['f7'],
    interaction_encoded,
    data['f9'],
    data['f10'],
    data['f11'] 
    )).astype(float)

    y = data['f12'].astype(int)

    return X, y


def main() -> None:
    X, y = data_preprocessing()
    


if __name__ == "__main__":
    
    main()