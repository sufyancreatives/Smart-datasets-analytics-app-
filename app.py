import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as  plt
import seaborn as sns
st.title("Data anaylsis application")
st.header("Welcome to the Data Analysis App")

dataset_choice = st.selectbox(
    "Select a dataset:",
    ["iris", "titanic", "tips" , "diamonds" , "flights" , "grocery_store"]
)

if dataset_choice == "iris":
    df = sns.load_dataset("iris")
elif dataset_choice == "titanic":
    df = sns.load_dataset("titanic")
elif dataset_choice == "tips":
    df = sns.load_dataset("tips")
elif dataset_choice == "diamonds":
    df = sns.load_dataset("diamonds")
elif dataset_choice == "flights":
    df = sns.load_dataset("flights")
elif dataset_choice == "grocery_store":
    df = sns.load_dataset("grocery_store")

st.subheader("Or upload your own dataset")
uploaded_file = st.file_uploader("Choose a CSV file", type=["csv", "xlsx" , ])

if uploaded_file is not None:
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)
    st.success("Dataset uploaded successfully!")


st.write(df.head(10))

st.write(f"Dataset contains {df.shape[0]} rows and {df.shape[1]} columns.")


st.write('Column Names and Data Types:' , df.dtypes)
st.write(df.dtypes)

if df.isnull().sum().sum() > 0:
    st.write("Null Values in Each Column:")
    st.write(df.isnull().sum().sort_values(ascending=False))
else :
    st.write("No null values in the dataset.")

st.write('Summary Statistics:', df.describe())

st.subheader("Data Visualization")
x_axis = st.selectbox("Select X-axis:", df.columns) 
y_axis = st.selectbox("Select Y-axis:", df.columns)
plot_type = st.selectbox("Select Plot Type:", ["scatter", "line", "bar", "histogram", "box", "pie", "kde", "violin", "area"])

if plot_type == "scatter":
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x=x_axis, y=y_axis)
    st.pyplot(plt)
elif plot_type == "line":
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=df, x=x_axis, y=y_axis)
    st.pyplot(plt)
elif plot_type == "bar":
    plt.figure(figsize=(10, 6))
    sns.barplot(data=df, x=x_axis, y=y_axis)
    st.pyplot(plt)
elif plot_type == "histogram":
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df, x=x_axis, bins=30)
    st.pyplot(plt)
elif plot_type == "box":
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df, x=x_axis, y=y_axis)
    st.pyplot(plt)
elif plot_type == "pie":
    plt.figure(figsize=(8, 8))
    df[y_axis].value_counts().plot.pie(autopct='%1.1f%%')
    st.pyplot(plt)  
elif plot_type == "kde":
    plt.figure(figsize=(10, 6))
    sns.kdeplot(data=df, x=x_axis, y=y_axis, fill=True)
    st.pyplot(plt)
elif plot_type == "violin":
    plt.figure(figsize=(10, 6))
    sns.violinplot(data=df, x=x_axis, y=y_axis)
    st.pyplot(plt)
elif plot_type == "area":
    plt.figure(figsize=(10, 6))
    df.set_index(x_axis)[y_axis].plot.area()
    st.pyplot(plt)
else:
    st.write("Plot type not recognized.")



st.subheader("Pair Plot")
hue_option = st.selectbox("Select hue (optional):", [None] + list(df.columns))
st.pyplot(sns.pairplot(data=df, hue=hue_option))
st.subheader("Correlation Heatmap")
plt.figure(figsize=(10, 8))
numeric_df = df.select_dtypes(include=[np.number])
if not numeric_df.empty:
    sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm")
    st.pyplot(plt)
else:
    st.write("No numeric columns available for correlation heatmap.")
st.subheader("Download Modified Dataset")
@st.cache_data
def convert_df_to_csv(dataframe):
    return dataframe.to_csv(index=False).encode('utf-8')
csv_data = convert_df_to_csv(df)
st.download_button(
    label="Download data as CSV",
    data=csv_data,
    file_name='modified_dataset.csv',
    mime='text/csv',
)
st.success("You can now download the modified dataset!")

st.subheader("Additional Input Widgets")
st.text_input("Enter your name")
age = st.number_input("Enter your age", min_value=0, max_value=120, value=25)
st.write("You are ", age, " years old")
rating = st.slider("Rate your experience", min_value=0, max_value=10, value=5)
st.write("You rated your experience as ", rating)
if st.checkbox("I agree to the terms and conditions"):
    st.write("Thank you for agreeing!")
gender = st.radio("Select your gender", ("Male", "Female", "Other"))
st.write("You selected: ", gender)
if st.button("Submit"):
    st.write("Thank you for using the Data Analysis App! We hope you enjoyed it.")
