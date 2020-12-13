import pandas as pd


csv_file = pd.read_csv('Resources/cities.csv')
cities_df = pd.DataFrame(csv_file)

csv_file.to_html('table.html', classes=['table', 'table-hover', 'thead-dark'])