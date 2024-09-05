from os import write

from click import option
from mysql.connector import connect
import streamlit as st
try:
    obj=connect(user='root',password='Harshit123@',database='july',host='localhost',port=3306)
    if (obj.is_connected()):
        print('Connected')
except:
    print('unable to connect')

myc=obj.cursor()
myc.execute('select * from table2')
data=myc.fetchall()
for i in data:
    print(i)
import pandas as pd
st.title('MySQL Dataset')
df=pd.DataFrame(data)
st.write(df)

def main():
    st.title("Operations With MySQL");
    option=st.sidebar.selectbox("Select an Operation",("Create","Read","Update","Delete"))
    if option=="Create":
        st.subheader("Create a Record")
        name=st.text_input("Enter Name")
        age=st.number_input("Enter age")
        if st.button("Create"):
            sql= "insert into table2(name,age) values(%s,%s)"
            val= (name,age)
            myc.execute(sql,val)
            obj.commit()
            st.success("Record Created Successfully!!!")
    elif option=="Read":
        st.subheader("Read Record")
        myc.execute("select * from table2")
        result = myc.fetchall()
        for row in result:
            st.write(row)
    elif option == "Update":
        st.subheader("Update a Record")
        age = st.number_input("Enter age", min_value=1)
        name = st.text_input("Enter New Name")
        if st.button("Update"):
            sql = "update table2 set name=%s where age =%s"
            val = (name, age)
            myc.execute(sql, val)
            obj.commit()
            st.success("Record Updated Successfully!!!")
    elif option == "Delete":
        st.subheader("Delete a Record")
        age = st.number_input("Enter age", min_value=1)
        if st.button("Delete"):
            sql = "delete from table2 where age =%s"
            val = (age,)
            myc.execute(sql, val)
            obj.commit()
            st.success("Record Deleted Successfully!!!")
if __name__ == "__main__":
    main()