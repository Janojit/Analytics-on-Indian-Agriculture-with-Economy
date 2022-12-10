import streamlit as st
import numpy as np 
import pandas as pd 
import seaborn as sns
import plotly.express as px 
import plotly.graph_objects as go 
import matplotlib.pyplot as plt 
from chart_studio import plotly as py 
from plotly import tools 
from plotly.subplots import make_subplots as sub

def rice():
    temp = df.groupby(['Year'],as_index = False)['RICE PRODUCTION (1000 tons)'].sum()[['Year','RICE PRODUCTION (1000 tons)']]
    fig = px.line(temp, 'Year', 'RICE PRODUCTION (1000 tons)')
    st.plotly_chart(fig)

    fig = sub(rows=1,cols=2,
                        subplot_titles=('Highest Rice producing districts', 'Least overall Rice producing districts'))


    temp = df.groupby(['Dist Name'],as_index = False)['RICE PRODUCTION (1000 tons)'].sum().sort_values('RICE PRODUCTION (1000 tons)',ascending=False).reset_index()[['Dist Name','RICE PRODUCTION (1000 tons)']]
    temp1 = temp.head()
    trace1 = go.Bar(x= temp1['Dist Name'], y=temp1['RICE PRODUCTION (1000 tons)'])

    temp1=temp.tail()
    trace2 = go.Bar(x= temp1['Dist Name'], y=temp1['RICE PRODUCTION (1000 tons)'])

    fig.append_trace(trace1,1,1)
    fig.append_trace(trace2,1,2)
    st.plotly_chart(fig)
    del temp,temp1

    temp = df.groupby(['State Name'],as_index = False)['RICE PRODUCTION (1000 tons)'].sum()
    fig = plt.figure(figsize=(15,15))
    sns.barplot(df["State Name"],df["RICE PRODUCTION (1000 tons)"])
    plt.xticks(rotation=90)
    st.pyplot(fig)
    fig1 = plt.figure(figsize=(10,15))
    plt.pie(temp['RICE PRODUCTION (1000 tons)'], labels=temp['State Name'], colors=sns.color_palette('bright'), autopct='%.0f%%')
    st.pyplot(fig1)

def wheat():
    temp = df.groupby(['Year'],as_index = False)['WHEAT PRODUCTION (1000 tons)'].sum()[['Year','WHEAT PRODUCTION (1000 tons)']]
    fig = px.line(temp, 'Year', 'WHEAT PRODUCTION (1000 tons)')
    st.plotly_chart(fig)

    fig = sub(rows=1,cols=2,
                        subplot_titles=('Highest Wheat producing districts', 'Least overall Wheat producing districts'))


    temp = df.groupby(['Dist Name'],as_index = False)['WHEAT PRODUCTION (1000 tons)'].sum().sort_values('WHEAT PRODUCTION (1000 tons)',ascending=False).reset_index()[['Dist Name','WHEAT PRODUCTION (1000 tons)']]
    temp1 = temp.head()
    trace1 = go.Bar(x= temp1['Dist Name'], y=temp1['WHEAT PRODUCTION (1000 tons)'])

    temp1=temp.tail()
    trace2 = go.Bar(x= temp1['Dist Name'], y=temp1['WHEAT PRODUCTION (1000 tons)'])

    fig.append_trace(trace1,1,1)
    fig.append_trace(trace2,1,2)
    st.plotly_chart(fig)
    del temp,temp1

    temp = df.groupby(['State Name'],as_index = False)['WHEAT PRODUCTION (1000 tons)'].sum()
    fig = plt.figure(figsize=(15,15))
    sns.barplot(df["State Name"],df["WHEAT PRODUCTION (1000 tons)"])
    plt.xticks(rotation=90)
    st.pyplot(fig)
    fig1 = plt.figure(figsize=(10,15))
    plt.pie(temp['WHEAT PRODUCTION (1000 tons)'], labels=temp['State Name'], colors=sns.color_palette('bright'), autopct='%.0f%%')
    st.pyplot(fig1)

def kharif():
    temp = df.groupby(['Year'],as_index = False)['KHARIF SORGHUM PRODUCTION (1000 tons)'].sum()[['Year','KHARIF SORGHUM PRODUCTION (1000 tons)']]
    fig = px.line(temp, 'Year', 'KHARIF SORGHUM PRODUCTION (1000 tons)')
    st.plotly_chart(fig)

    fig = sub(rows=1,cols=2,
                        subplot_titles=('Highest Kharif Sorghum producing districts', 'Least overall Kharif Sorghum producing districts'))


    temp = df.groupby(['Dist Name'],as_index = False)['KHARIF SORGHUM PRODUCTION (1000 tons)'].sum().sort_values('KHARIF SORGHUM PRODUCTION (1000 tons)',ascending=False).reset_index()[['Dist Name','KHARIF SORGHUM PRODUCTION (1000 tons)']]
    temp1 = temp.head()
    trace1 = go.Bar(x= temp1['Dist Name'], y=temp1['KHARIF SORGHUM PRODUCTION (1000 tons)'])

    temp1=temp.tail()
    trace2 = go.Bar(x= temp1['Dist Name'], y=temp1['KHARIF SORGHUM PRODUCTION (1000 tons)'])

    fig.append_trace(trace1,1,1)
    fig.append_trace(trace2,1,2)
    st.plotly_chart(fig)
    del temp,temp1

    temp = df.groupby(['State Name'],as_index = False)['KHARIF SORGHUM PRODUCTION (1000 tons)'].sum()
    fig = plt.figure(figsize=(15,15))
    sns.barplot(df["State Name"],df["KHARIF SORGHUM PRODUCTION (1000 tons)"])
    plt.xticks(rotation=90)
    st.pyplot(fig)
    fig1 = plt.figure(figsize=(10,15))
    plt.pie(temp['KHARIF SORGHUM PRODUCTION (1000 tons)'], labels=temp['State Name'], colors=sns.color_palette('bright'), autopct='%.0f%%')
    st.pyplot(fig1)

def rabi():
    temp = df.groupby(['Year'],as_index = False)['RABI SORGHUM PRODUCTION (1000 tons)'].sum()[['Year','RABI SORGHUM PRODUCTION (1000 tons)']]
    fig = px.line(temp, 'Year', 'RABI SORGHUM PRODUCTION (1000 tons)')
    st.plotly_chart(fig)

    fig = sub(rows=1,cols=2,
                        subplot_titles=('Highest Rabi Sorghum producing districts', 'Least overall Rabi Sorghum producing districts'))


    temp = df.groupby(['Dist Name'],as_index = False)['RABI SORGHUM PRODUCTION (1000 tons)'].sum().sort_values('RABI SORGHUM PRODUCTION (1000 tons)',ascending=False).reset_index()[['Dist Name','RABI SORGHUM PRODUCTION (1000 tons)']]
    temp1 = temp.head()
    trace1 = go.Bar(x= temp1['Dist Name'], y=temp1['RABI SORGHUM PRODUCTION (1000 tons)'])

    temp1=temp.tail()
    trace2 = go.Bar(x= temp1['Dist Name'], y=temp1['RABI SORGHUM PRODUCTION (1000 tons)'])

    fig.append_trace(trace1,1,1)
    fig.append_trace(trace2,1,2)
    st.plotly_chart(fig)
    del temp,temp1

    temp = df.groupby(['State Name'],as_index = False)['RABI SORGHUM PRODUCTION (1000 tons)'].sum()
    fig = plt.figure(figsize=(15,15))
    sns.barplot(df["State Name"],df["RABI SORGHUM PRODUCTION (1000 tons)"])
    plt.xticks(rotation=90)
    st.pyplot(fig)
    fig1 = plt.figure(figsize=(10,15))
    plt.pie(temp['RABI SORGHUM PRODUCTION (1000 tons)'], labels=temp['State Name'], colors=sns.color_palette('bright'), autopct='%.0f%%')
    st.pyplot(fig1)

def all():
    temp = df.groupby(['Year'],as_index = False)['RICE PRODUCTION (1000 tons)','WHEAT PRODUCTION (1000 tons)','KHARIF SORGHUM PRODUCTION (1000 tons)','RABI SORGHUM PRODUCTION (1000 tons)'].sum()
    fig = px.line(temp,x="Year", y=['RICE PRODUCTION (1000 tons)','WHEAT PRODUCTION (1000 tons)','KHARIF SORGHUM PRODUCTION (1000 tons)','RABI SORGHUM PRODUCTION (1000 tons)'],width=1000,height=400)
    st.plotly_chart(fig)



def q1():
    fig = plt.figure(figsize=(20,15))
    sns.barplot(df1["State Name"],df1["Total Production (1000 tons)"])
    plt.xticks(rotation=90)
    fig1  = plt.figure(figsize=(20,15))
    plt.pie(df1.groupby(['State Name'],as_index = False)['Total Production (1000 tons)'].sum()['Total Production (1000 tons)'], labels=df1.groupby(['State Name'],as_index = False)['Total Production (1000 tons)'].sum()['State Name'], colors=sns.color_palette('bright'), autopct='%.0f%%')
    st.pyplot(fig)
    st.pyplot(fig1)

def q2():
    fig = sub(rows=1,cols=2,
                    subplot_titles=('Highest crop producing districts', 'Least overall crop producing districts'))


    temp = df.groupby(['Dist Name'],as_index = False)['Total Production (1000 tons)'].sum().sort_values('Total Production (1000 tons)',ascending=False).reset_index()[['Dist Name','Total Production (1000 tons)']]
    temp1 = temp.head()
    trace1 = go.Bar(x= temp1['Dist Name'], y=temp1['Total Production (1000 tons)'])

    temp1=temp.tail()
    trace2 = go.Bar(x= temp1['Dist Name'], y=temp1['Total Production (1000 tons)'])

    fig.append_trace(trace1,1,1)
    fig.append_trace(trace2,1,2)
    st.plotly_chart(fig)
    del temp,temp1

def q3():
    fig = plt.figure(figsize=(20,15))
    sns.barplot(df1["State Name"],df1["Total Area (1000 ha)"])
    plt.xticks(rotation=90)
    fig1 = plt.figure(figsize=(20,15))
    plt.pie(df1.groupby(['State Name'],as_index = False)['Total Area (1000 ha)'].sum()['Total Area (1000 ha)'], labels=df1.groupby(['State Name'],as_index = False)['Total Area (1000 ha)'].sum()['State Name'], colors=sns.color_palette('bright'), autopct='%.0f%%')
    plt.show()
    st.pyplot(fig)
    st.pyplot(fig1)

def q4():
    fig = sub(rows=1,cols=2,
                    subplot_titles=('Highest crop field districts', 'Least overall crop field districts'))


    temp = df.groupby(['Dist Name'],as_index = False)['Total Area (1000 ha)'].sum().sort_values('Total Area (1000 ha)',ascending=False).reset_index()[['Dist Name','Total Area (1000 ha)']]
    temp1 = temp.head()
    trace1 = go.Bar(x= temp1['Dist Name'], y=temp1['Total Area (1000 ha)'])

    temp1=temp.tail()
    trace2 = go.Bar(x= temp1['Dist Name'], y=temp1['Total Area (1000 ha)'])

    fig.append_trace(trace1,1,1)
    fig.append_trace(trace2,1,2)
    st.plotly_chart(fig)
    del temp,temp1

def q5():
    fig = sns.jointplot("Total Area (1000 ha)","Total Production (1000 tons)",data=df,kind="reg")
    st.pyplot(fig)
    fig1 = plt.figure(figsize=(10,6))
    sns.heatmap(df[["Total Area (1000 ha)","Total Production (1000 tons)"]].corr(),annot=True)
    st.pyplot(fig1)

def q6():
    temp = df.groupby(by='Year')['Total Production (1000 tons)'].sum().reset_index()
    fig = px.line(temp, 'Year', 'Total Production (1000 tons)')
    st.plotly_chart(fig)

def q7():
    temp = df1.sort_values(by='Total Yield (Kg per ha)')
    fig = px.bar(temp, 'State Name', 'Total Yield (Kg per ha)', color='Total Yield (Kg per ha)')
    st.plotly_chart(fig)

def q8():
    crops = (
        "Rice","Wheat","Kharif","Rabi","Year wise Analysis for All Four Crops Production"
    )
    crop = st.selectbox("Select Crop: ",crops)
    if crop == "Rice":
        rice()
    elif crop == "Wheat":
        wheat()
    elif crop == "Kharif":
        kharif()
    elif crop == "Rabi":
        rabi()
    else:
        all()



def q9():
    fig = sns.jointplot("Rainfall(mm)","Total Production (1000 tons)",data=df,kind="reg")
    st.pyplot(fig)
    fig1 = plt.figure(figsize=(10,6))
    sns.heatmap(df[["Rainfall(mm)","Total Production (1000 tons)"]].corr(),annot=True)
    st.pyplot(fig1)

def q10():
    temp = df1.groupby(['Year'],as_index = False)['GROSS STATE VALUE ADDED BY ECONOMIC ACTIVITY-AGRICULTURE(Average Prices)','GROSS STATE DOMESTIC PRODUCT (Average Prices)','Total Production (1000 tons)'].sum()
    fig = px.line(temp,x="Year",y=['GROSS STATE VALUE ADDED BY ECONOMIC ACTIVITY-AGRICULTURE(Average Prices)','GROSS STATE DOMESTIC PRODUCT (Average Prices)'],width=1000,height=400)
    st.plotly_chart(fig)
    fig1 = plt.figure(figsize=(15,15))
    sns.barplot(temp["Year"],temp["Total Production (1000 tons)"])
    plt.xticks(rotation=90)
    st.pyplot(fig1)

    temp1 = df1.groupby(['State Name'],as_index = False)['GROSS STATE VALUE ADDED BY ECONOMIC ACTIVITY-AGRICULTURE(Average Prices)','GROSS STATE DOMESTIC PRODUCT (Average Prices)','Total Production (1000 tons)'].sum()
    fig2 = plt.figure(figsize=(10,15))
    plt.pie(temp1['GROSS STATE VALUE ADDED BY ECONOMIC ACTIVITY-AGRICULTURE(Average Prices)'], labels=temp1['State Name'], colors=sns.color_palette('bright'), autopct='%.0f%%')
    fig3 = plt.figure(figsize=(10,15))
    plt.pie(temp1['GROSS STATE DOMESTIC PRODUCT (Average Prices)'], labels=temp1['State Name'], colors=sns.color_palette('bright'), autopct='%.0f%%')
    fig4 = plt.figure(figsize=(10,15))
    plt.pie(temp1['Total Production (1000 tons)'], labels=temp1['State Name'], colors=sns.color_palette('bright'), autopct='%.0f%%')
    st.write(('Statewise Agricultural GDP Distribution').center(115,'-'))
    st.pyplot(fig2)
    st.write(('Statewise Overall GDP Distribution').center(115,'-'))
    st.pyplot(fig3)
    st.write(('Statewise Crop Production').center(115,'-'))
    st.pyplot(fig4)

    fig5 = plt.figure(figsize=(15,15))
    sns.heatmap(df1.drop(['Year'],axis=1).corr(),annot=True)
    st.pyplot(fig5)



@st.cache
def load_data1():
    df = pd.read_csv("dataset.csv")

    return df

df = load_data1()

@st.cache
def load_data2():
    df1 = pd.read_csv("dataset1.csv")
    
    return df1

df1 = load_data2()

def show_explore_page():
    st.title("Data Visualization")

    st.write("""### Developed By Janojit Chakraborty""")

    questions = (
        "Analyse Total Production With States",
        "Find Most and Least crop producting districts",
        "Analyse Total Area with States",
        "Find Most and Least crop field districts",
        "Find Relation Between Total Area and Total Production",
        "Find Overall producting through years",
        "Find Productivity in different states",
        "Make and analysis on Rice, Wheat, Kharif and Rabi Crops",
        "Is Rainfall Really Effects Production",
        "Try to Analyse Economy and Find an insightfull relation between Economy and Crop Production"
    )

    question = st.selectbox("Select Questionary: ",questions)

    if question == "Analyse Total Production With States":
        q1()
    elif question == "Find Most and Least crop producting districts":
        q2()
    elif question == "Analyse Total Area with States":
        q3()
    elif question == "Find Most and Least crop field districts":
        q4()
    elif question == "Find Relation Between Total Area and Total Production":
        q5()
    elif question == "Find Overall producting through years":
        q6()
    elif question == "Find Productivity in different states":
        q7()
    elif question == "Make and analysis on Rice, Wheat, Kharif and Rabi Crops":
        q8()
    elif question == "Is Rainfall Really Effects Production":
        q9()
    elif question == "Try to Analyse Economy and Find an insightfull relation between Economy and Crop Production":
        q10()
    
