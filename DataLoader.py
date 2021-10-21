import pandas as pd
import streamlit as st

@st.cache
def load_data():
    """
    Loads house price data
    :return:
    """
    df = pd.read_csv('Data/train.csv')
    df.drop(columns=['Id'], inplace=True)

    train_numeric = df.select_dtypes(['int64', 'float64'])
    train_cat = df.select_dtypes(['object'])

    # Drop low correlation cols
    corr = train_numeric.corr()
    low_corr_cols = train_numeric.corr()['SalePrice'].sort_values().index[:12]
    df.drop(columns=low_corr_cols, inplace=True)

    # Drop sparse cols
    sparse_cols = train_cat.isna().sum().sort_values(ascending=False).index[:10]
    sparse_cols = sparse_cols.drop(labels=['FireplaceQu', 'GarageFinish', 'GarageType'])
    df.drop(columns=sparse_cols, inplace=True)

    # Some other cols to drop
    cols_to_drop = ['ExterCond', 'RoofMatl', 'BldgType', 'Condition1', 'LandSlope', 'Utilities', 'Condition2', 'Street',
                    'Heating', 'Functional']
    df.drop(columns=cols_to_drop, inplace=True)

    return df
