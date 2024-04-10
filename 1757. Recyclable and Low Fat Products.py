import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    products_df = pd.DataFrame(products)
    
    result_df = products_df[(products_df['low_fats'] == 'Y') & (products_df['recyclable'] == 'Y')]
    result_df = result_df[['product_id']]

    return result_df

