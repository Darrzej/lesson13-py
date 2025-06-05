import numpy as np 
import pandas as pd
print(np.__version__)

df = pd.read_csv('avgIQpercountry.csv')
print(df.info())

print_rows = df.head()

subset = df[['Country', 'Average IQ']]
print(subset)

filtered_df = subset[subset['Average IQ'] < 76]
print(filtered_df)



# array_2d = np.array([[1,2,3,4,5], [6,7,8,9,10]])
# print(array_2d)

# element = array_2d[0,1]
# print(element)

# dimension = array_2d.ndim
# print(dimension)

# size = array_2d.size
# print(size)

# total_sum = np.sum(array_2d)
# print(total_sum)

# sum_columns = np.sum(array_2d, axis=0)
# print(sum_columns)

# sum_rows = np.sum(array_2d, axis = 1)
# print(sum_rows)

# products = ['apple', 'banana', 'orange', 'grape']
# sales = [90,100,110,120]

# sales_series = pd.Series(sales,index=products)
# print(sales_series)

# print(sales_series['grape'])

# total_sales = sales_series.sum()
# print(total_sales)

# best_selling_product = sales_series.idxmax()
# print(f"Best selling produvt is: {best_selling_product}")

# data = {
#     'Name': ['Leon', 'Jon', 'Christopher'],
#     'Age': [69, 1, 100],
#     'City': ['Prizren', 'Gjakove', 'Baghdad']

# }

# df = pd.DataFrame(data)
# print(df)

# df = pd.read_csv('cs.csv')
# df.to_csv('darsej.csv', index = False)
