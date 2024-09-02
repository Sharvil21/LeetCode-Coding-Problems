#First solution
import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    return orders.groupby('customer_number')['order_number'].count().sort_values(ascending=False).head(1).reset_index()[['customer_number']]

#Second Solution Using .mode() method:
import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    return orders['customer_number'].mode().to_frame()

