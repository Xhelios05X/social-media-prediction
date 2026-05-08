import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

FILENAME = "../Teen_Mental_Health_Dataset.csv"

def data_preprocessing(filename = FILENAME) -> object:
    data = np.genfromtxt(fname=FILENAME, delimiter=",", dtype=None, skip_header=1, encoding='utf-8')
    
    """
    data binarization
    female == 0
    male == 1
    """
    gender_encoded = np.where(data['f1'] == 'female', 1, 0)

    """
    social ineraction encoding
    low == 0
    medium == 1
    high == 2 
    """
    interaction_encoded = np.zeros(data.shape[0])
    interaction_encoded[data['f8'] == 'medium'] = 1
    interaction_encoded[data['f8'] == 'high'] = 2


    """
    create new array to data encoding
    is_instagram == 1/0 (True/False)
    is_tiktok == 1/0 (True/False)
    is_both = = 1/0 (True/False)
    """
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

    test_size = 0.5
    random_state = 2

    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

    scaler = MinMaxScaler()
    X_normalized = scaler.fit_transform(x_train)
    


if __name__ == "__main__":
    
    main()