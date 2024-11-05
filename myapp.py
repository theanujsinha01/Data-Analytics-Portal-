# import libraries
import pandas as pd
import plotly.express as px
import streamlit as st

# page tittle and page icon
st.set_page_config(
    page_title= 'Data Analytics Portal',
    page_icon='📈'
)

#Tittle
st.title(':rainbow[Data Analytics Portal]')
# subHeader and divider
st.subheader(':gray[Explore Data with ease.]', divider='rainbow')

#File upload
file = st.file_uploader('Drop csv or excel file', type=['csv','xlsx'])

if(file != None):
    if(file.name.endswith('csv')):
        data = pd.read_csv(file)
    else:
        data = pd.read_excel(file)

    st.dataframe(data)
    st.info('File is Successfully Uploaded')

    st.subheader(':rainbow[Basic information of the dataset]',divider='rainbow')

    # Multiples Tabs
    tab1, tab2, tab3, tab4 = st.tabs(['Summary','Top & Bottom Rows','Data Types','Columns'])

    with tab1:
        st.write(f'There are {data.shape[0]} rows in dataset and {data.shape[1]} columns in dataset')
        st.subheader(':gray[Statistical Summary of the  Dataset]')
        st.dataframe(data.describe())

    with tab2:
        st.subheader(':gray[Top Rows]')
        topRows = st.slider('Number of rows you want',1,data.shape[0], key='1')  
        st.dataframe(data.head(topRows)) 


        st.subheader(':gray[Bottom Rows]')
        topRows = st.slider('Number of rows you want',1,data.shape[0], key='2')  
        st.dataframe(data.tail(topRows))

    with tab3:
        st.subheader(':gray[Data types of column]')
        st.dataframe(data.dtypes)    
    
    with tab4:
        st.subheader(':gray[Column Names in Dataset]')
        st.dataframe(data.columns)
    st.subheader(':rainbow[Column Values To Count]',divider='rainbow')
    with st.expander('Value Count'):
        col1, col2 = st.columns(2)
        with col1:
            column = st.selectbox('Choose Colmn name', options=(data.columns))
        with col2:
            toprows = st.number_input('Top rows', min_value=1,step=1)
        
        count = st.button('Count')
        if(count == True):
            result = data[column].value_counts().reset_index().head(toprows)
            st.dataframe(result)
            st.subheader('Visualization',divider='rainbow')
            fig = px.bar(data_frame=result, x = column, y='count',text='count',template='plotly_white')
            st.plotly_chart(fig)

            fig = px.line(data_frame=result, x = column, y='count',text='count',template='plotly_white')
            st.plotly_chart(fig)

            fig = px.pie(data_frame=result, names= column, values='count',template='plotly_white')
            st.plotly_chart(fig)

    st.subheader(':rainbow[Groupby : Simplify your data ananlysis]',divider='rainbow')
    st.write('The groupby lets you summarize data by specific catogories and groups')  
    with st.expander('Group By your columns'):
        col1,col2,col3 = st.columns(3)
        with col1:
            groupby_cols =st.multiselect('Choose your columns to groupby',options=list(data.columns))
        with col2:
            operation_col = st.selectbox('Choose  columns to for operation',options=list(data.columns))
        with col3:
            operation = st.selectbox('Choose operation',options=['sum','max','min','mean','median','count'])
        if(groupby_cols):
            result = data.groupby(groupby_cols).agg(
            newcol =(operation_col,operation)
            ).reset_index()
            st.dataframe(result)

            st.subheader(':gray[Data Visualization]',divider='gray')
            graphs = st.selectbox('Choose your graphs',options=['line','bar','pie','sunburst','scatter'])
            if(graphs == 'line'):
                x_axis =st.selectbox('Choose X axis',options=list(result.columns))
                y_axis =st.selectbox('Choose Y axis',options=list(result.columns))
                color = st.selectbox('Color Information',options=[None]+list(result.columns))
                fig = px.line(data_frame=result, x=x_axis, y=y_axis,color=color, markers='o')
                st.plotly_chart(fig)
            elif(graphs == 'bar'):
                x_axis =st.selectbox('Choose X axis',options=list(result.columns))
                y_axis =st.selectbox('Choose Y axis',options=list(result.columns))
                color = st.selectbox('Color Information',options=[None]+list(result.columns))
                facet_col = st.selectbox('Column Information',options=[None]+list(result.columns), key='123')
                fig = px.bar(data_frame=result, x=x_axis, y=y_axis,color=color, facet_col=facet_col,barmode='group')
                st.plotly_chart(fig)
            elif(graphs == 'scatter'):
                x_axis =st.selectbox('Choose X axis',options=list(result.columns))
                y_axis =st.selectbox('Choose Y axis',options=list(result.columns))
                color = st.selectbox('Color Information',options=[None]+list(result.columns))
                size = st.selectbox('Size Column',options=[None]+list(result.columns))
                fig = px.scatter(data_frame=result, x=x_axis, y=y_axis,color=color, size=size)
                st.plotly_chart(fig)
            elif(graphs == 'pie'):
                values =st.selectbox('Choose Numerical Values',options=list(result.columns))
                names =st.selectbox('Choose Labels',options=list(result.columns))
                fig = px.pie(data_frame=result, values=values,names=names )
                st.plotly_chart(fig)
            elif(graphs == 'sunburst'):
                path = st.multiselect('Choose your Path',options=list(result.columns))
                fig = px.sunburst(data_frame=result, path=path, values='newcol')
                st.plotly_chart(fig)
        