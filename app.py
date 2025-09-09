import streamlit as st
import pandas as pd
import model as md

# Constants
M = 2
B = 3

st.title("Linear Function Calculator: y = mx + b")
st.markdown("This app calculates **y = mx + b** over a range of x values.")

# User input for x range
start = st.number_input("Start of x", value=1, step=1)
end = st.number_input("End of x", value=500, step=1)

if start > end:
    st.error("'Start' must be less than or equal to 'End'.")
else:
    try:
        results = md.compute_linear_range(int(start), int(end), m=M, b=B)
        df = pd.DataFrame(results, columns=['x', 'y'])

        st.subheader(f"Using equation: y = {M}x + {B}")
        st.line_chart(df.set_index('x'))
        csv = df.to_csv(index=False)

        # Add download button
        st.download_button(
            label="📥 Download results as CSV",
            data=csv,
            file_name=f'linear_results_m{M}_b{B}_x{int(start)}-{int(end)}.csv',
            mime='text/csv'
        )

    except Exception as e:
        st.error(f"An error occurred: {e}")
