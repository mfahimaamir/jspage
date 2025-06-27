import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
from pivottablejs import pivot_ui
st.header("Drag and Drop Pivot Table with selected data export to Excel")

mdf = pd.DataFrame({"A": ["foo", "foo", "foo", "foo", "foo",
                         "bar", "bar", "bar", "bar"],
                   "B": ["one", "one", "one", "two", "two",
                         "one", "one", "two", "two"],
                   "C": ["small", "large", "large", "small",
                         "small", "large", "small", "small",
                         "large"],
                   "D": [1, 2, 2, 3, 3, 4, 5, 6, 7],
                   "F": ['AA01', 'AAA2', 'AAA2', 'DDD3', 'DDD3', 'FFF4', 'FFF5', 'TTT6', 'RRR7'],
                   "G": ['ADDA01', 'ADDAA2', 'AFFAA2', 'DFFDD3', 'DFFDD3', 'FDDFF4', 'FFFFF5', 'TDDTT6', 'RRR7'],
                   "E": [2, 4, 5, 5, 6, 6, 8, 9, 9]})



t = pivot_ui(mdf)
with open(t.src) as t:
     components.html(t.read(), width=900, height=1000, scrolling=True)


