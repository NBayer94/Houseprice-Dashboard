import streamlit as st
import matplotlib.pyplot as plt
import DataLoader

st.set_page_config(layout='wide', page_title='House Price Dashboard')

plt.style.use(style='dark_background')
plt.rcParams["image.cmap"]  = 'viridis'

df = DataLoader.load_data()
num_cols = df.select_dtypes(include=['int64', 'float64']).columns.to_list()
cat_cols = df.select_dtypes(include=['object']).columns.to_list()

st.header('House Price Dashboard')
st.write('This dashboard provides information about the house price dataset.')

################
#   Sidebar   #
###############
with st.sidebar:
    st.header('Plot Settings')
    st.write('Select attributes and plot types.')
    # Form to collect desired settings
    with st.form('cols'):
        #First Plot
        attr_1 = st.selectbox('First attribute:', num_cols, 0)
        plot_type_1 = st.radio('First plot type:', ['Histogram', 'Scatter'])
        st.write('\n')
        # Second Plot
        attr_2 = st.selectbox('Second attribute', num_cols, 1)
        plot_type_2 = st.radio('Second plot type:', ['Histogram', 'Scatter'])
        st.write('\n')
        # Grouping var
        attr_3 = st.selectbox('Grouping attribute', cat_cols)
        # Submit button
        submitted = st.form_submit_button("Submit")

# First Plot
with st.container():
    col1, col2 = st.columns(2)
    if plot_type_1 == 'Histogram':
        col1.subheader(f'Distribution {attr_1}')
    else:  
        col1.subheader(f'SalePrice vs. {attr_1}')
    col2.subheader('Data')

    # Plot 1
    with col1:
        fig_1 = plt.figure()
        for val in df[attr_3].unique():
            if plot_type_1 == 'Histogram':
                plt.hist(df.loc[df[attr_3] == val , attr_1], 'auto', label=val, alpha=0.7)
            else:
                plt.scatter(df.loc[df[attr_3] == val , attr_1], df.loc[df[attr_3] == val, 'SalePrice'], label=val)

        plt.legend(title=attr_3)
        left, right = plt.gca().get_xlim()
        left = float(left)
        right = float(right)
        plot_container = st.container()
        slider_1 = st.slider('Adjust x-axis', left, right, (left, right))
        plt.xlim(slider_1[0], slider_1[1])
        plot_container.pyplot(fig_1)

    # Data
    with col2:
        st.dataframe(df[[attr_1, attr_3, 'SalePrice']], height=500)

# Second plot
with st.container():
    col1, col2 = st.columns(2)
    if plot_type_1 == 'Histogram':
        col1.subheader(f'Distribution {attr_2}')
    else:  
        col1.subheader(f'SalePrice vs. {attr_2}')
    col2.subheader('Data')

    with col1:
        fig = plt.figure()
        for val in df[attr_3].unique():
            if plot_type_2 == 'Histogram':
                plt.hist(df.loc[df[attr_3] == val , attr_2], 'auto', label=val, alpha=0.7)
            else:
                plt.scatter(df.loc[df[attr_3] == val, attr_2], df.loc[df[attr_3] == val, 'SalePrice'], label=val)
        plt.legend(title=attr_3)
        left, right = plt.gca().get_xlim()
        left = float(left)
        right = float(right)
        plot_container = st.container()
        slider_2 = st.slider('Adjust x-axis', left, right, (left, right))
        plt.xlim(slider_2[0], slider_2[1])
        plot_container.pyplot(fig)

    with col2:
        st.dataframe(df[[attr_2, attr_3, 'SalePrice']], height=500)