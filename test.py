import io

import pandas as pd
pd.set_option('display.expand_frame_repr', False)
csv_in = """Country/Region 1/22/2020 1/23/2020 1/25/2020 1/26/2020 1/27/2020
"Afghanistan" 0 0 0 0 5
"Albania" 0 55 0 0 0
"Algeria" 0 0 0 0 3
"Andorra" 0 0 2 66 0
"Angola" 1 0 0 0 0
"Antigua and Barbuda" 0 0 0 0 0
"""

#org_df = pd.read_csv(io.StringIO(csv_in), sep=' ', index_col=["Country/Region"])                                                                           

org_df = pd.read_csv(io.StringIO(csv_in), sep=' ', index_col=False)

print(org_df)

org_df_t = org_df

print(org_df_t)

melt_df = org_df.melt(id_vars = 'Country/Region', var_name='state', value_name='value')

print(melt_df)
