import pandas as pd

def account_summary(users: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    balances = transactions.groupby('account')['amount'].sum().reset_index()
    balances.columns = ['account', 'balance']
    
    high_balance_accounts = balances[balances['balance'] > 10000]
    
    result = pd.merge(high_balance_accounts, users, on='account', how='inner')
    
    result = result[['name', 'balance']]
    
    return result

