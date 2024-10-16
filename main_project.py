import time
import pandas as pd
import sys
import matplotlib.pyplot as plt

pd.set_option("display.max_columns",None)
pd.set_option("display.max_rows",None)
#Reading csv
global df
df=pd.read_csv("student_data.csv")
E_no=int(input("Enter Enrollment no.  : "))
s_name=input("Enter University name :")
branch=input("Enter Branch :")

# MENU DESIGN
def menu():
    while True:
        print("------------------------------------------------------------------------------")
        print("Name :",s_name,"                                            Enrollment no.-",E_no)
        print("Branch :",branch)
        print("------------------------------------------------------------------------------")
        print('''                              ITM (SLS) BARODA UNIVERSITY
*******************************************************************************
           
            1- DISPLAY RESULT SHEET
            2- TOTAL VS PASS ANALYSIS ( SUBJECT WISE )
            3- 90% AND ABOVE ( SUBJECT WISE )
            4- TOP 10 STUDENTS
            5- GRADE ANALYSIS
            6- PIE GRAPH FOR OVERALL PERFORMANCE
            7- EXIT ''')

        ch=int(input("\nEnter your Choice (1-7):"))
        if ch==1:
            result_sheet()
        elif ch==2:
            passed()
        elif ch==3:
            ninety_above()
        elif ch==4:
            top_10()
        elif ch==5:
            grade_analysis()
        elif ch==6:
            overall()
        else:
            my_chance=input("Do you really want to exit?(y/n)")
            if my_chance=='y' or my_chance=='Y':
                str="THANK YOU FOR USING THIS PROJECT. EXITING....."
                for k in str:
                    print(k,end='')
                    time.sleep(0.1)
                sys.exit()
            else:
                print("\nInvalid choice. Try again")
                continue
         
#Display result sheet
def result_sheet():
    print('---------- RESULT SHEET -----------')
    print(E_no,"-",s_name,"     Branch:",branch)
    print("---------------------------------------------------------------------------------------------")
    print(df)
    print()
    print()


# Creating Pie graph overall performance
def overall():      
    Total_Appear=df.Result.count()
    passeddf=df[df['Result']=='PASS']
    faildf=df[df['Result']=='FAIL']
    passed=passeddf.Result.count()
    fail=faildf.Result.count()
    comp=Total_Appear-(passed+fail)
    print("Total Passed=",passed)
    print("Total Compartment=",comp)
    print("Total Failed=",fail)
    print("Total Appeared=",Total_Appear)
    print()
    print()
    data=[passed,comp,fail]
    lbl=["Passed","Comp","Fail"]
    gtitle=s_name+"\nOverAll School Result "+branch
    plt.title(gtitle,fontsize=16,color='r')
    plt.grid()
    plt.pie(data,labels=lbl,autopct='%1.1f%%',startangle=15, shadow = True,explode=[0,0.15,0])
    plt.legend()
    plt.show()

# For grade analysis
def header():
    plt.xlabel('Grade ->',color='g',fontsize=12)
    plt.ylabel('No.of Students->',color='g',fontsize=12)
    gtitle1=s_name+"\nGrade Analysis "+branch
    plt.title(gtitle1,fontsize=16,color='b')
    plt.grid()
    plt.show()

#Grade analysis
def grade_analysis():
 #python grade calculation 
    count_Python_a=0    
    count_Python_b=0
    count_Python_c=0
    count_Python_d=0
    count_Python_e=0
    for i in range(len(df)):
        if df.GradePy[i]=='A':
            count_Python_a+=1
        if df.GradePy[i]=='B':
            count_Python_b+=1
        if df.GradePy[i]=='C':
            count_Python_c+=1
        if df.GradePy[i]=='D':
            count_Python_d+=1
        elif df.GradePy[i]=='E':
            count_Python_e+=1
    Python=[count_Python_a,count_Python_b,count_Python_c,count_Python_d,count_Python_e]

#C grade calculation
    count_C_Programming_a=0
    count_C_Programming_b=0
    count_C_Programming_c=0
    count_C_Programming_d=0
    count_C_Programming_e=0
    for i in range(len(df)):
        if df.GradeCP[i]=='A':
            count_C_Programming_a+=1
        if df.GradeCP[i]=='B':
            count_C_Programming_b+=1
        if df.GradeCP[i]=='C':
            count_C_Programming_c+=1
        if df.GradeCP[i]=='D':
            count_C_Programming_d+=1
        elif df.GradeCP[i]=='E':
            count_C_Programming_e+=1
    C_Programming=[count_C_Programming_a,count_C_Programming_b,count_C_Programming_c,count_C_Programming_d,count_C_Programming_e]

#DSA grade calculation
    count_DSA_a=0
    count_DSA_b=0
    count_DSA_c=0
    count_DSA_d=0
    count_DSA_e=0
    for i in range(len(df)):
        if df.GradeDSA[i]=='A':
            count_DSA_a+=1
        if df.GradeDSA[i]=='B':
            count_DSA_b+=1
        if df.GradeDSA[i]=='C':
            count_DSA_c+=1
        if df.GradeDSA[i]=='D':
            count_DSA_d+=1
        elif df.GradeDSA[i]=='E':
            count_DSA_e+=1
    DSA=[count_DSA_a,count_DSA_b,count_DSA_c,count_DSA_d,count_DSA_e]

#DMP grade calculation
    count_DMP_a=0
    count_DMP_b=0
    count_DMP_c=0
    count_DMP_d=0
    count_DMP_e=0
    for i in range(len(df)):
        if df.GradeDMP[i]=='A':
            count_DMP_a+=1
        if df.GradeDMP[i]=='B':
            count_DMP_b+=1
        if df.GradeDMP[i]=='C':
            count_DMP_c+=1
        if df.GradeDMP[i]=='D':
            count_DMP_d+=1
        elif df.GradeDMP[i]=='E':
            count_DMP_e+=1
    DMP=[count_DMP_a,count_DMP_b,count_DMP_c,count_DMP_d,count_DMP_e]

    dict1={'Python':Python,'C_Programming':C_Programming,'DSA':DSA,'DMP':DMP}
    dfgrade=pd.DataFrame(dict1,index=['A','B','C','D','E'])
    dfgrade1=dfgrade
    while True:
        print('''
        1- All Subjects Together
        2- Python
        3- C Programming
        4- DSA
        5- DMP
        6- Total Grades
        7- All subjects in grid
        8- Exit ''')
        choice=int(input("Enter Choice 1 to 8 : "))
        if choice==1:
            print(dfgrade1)
            dfgrade1.plot(kind='bar')
            header()
        elif choice==2:
            dfgrade1.plot(kind='bar',y='Python',color='r')
            header()
        elif choice==3:
            dfgrade1.plot(kind='bar',y='C_Programming',color='b')
            header()
        elif choice==4:
            dfgrade1.plot(kind='bar',y='DSA',color='g')
            header()
        elif choice==5:
            dfgrade1.plot(kind='bar',y='DMP',color='m')
            header()
        elif choice==6:
            dfgrade['Total']=dfgrade['Python']+dfgrade['C_Programming']+dfgrade['DSA']+dfgrade['DMP']
            print(dfgrade)
            dfgrade.plot(kind='bar',y='Total')
            header()
        elif choice==7:
            plt.subplot(3,2,1)
            plt.bar(dfgrade.index,dfgrade.Python,color='r')
            plt.subplot(3,2,2)
            plt.bar(dfgrade.index,dfgrade.C_Programming,color='b')
            plt.subplot(3,2,3)
            plt.bar(dfgrade.index,dfgrade.DSA,color='g')
            plt.subplot(3,2,4)
            plt.bar(dfgrade.index,dfgrade.DMP,color='m')
            plt.subplot(3,2,5)
            plt.show()
        else:
            print("Exiting......")
            break


# Subject wise Total vs Pass Analysis
def passed():
    Python_t=0
    C_Programming_t=0
    DSA_t=0
    DMP_t=0

    Python_p=0
    C_Programming_p=0
    DSA_p=0
    DMP_p=0

    for i in range(len(df)):
        if df.Python[i]>=35:
            Python_p+=1
        if df.C_Programming[i]>=35:
            C_Programming_p+=1
        if df.DSA[i]>=35:
            DSA_p+=1
        if df.DMP[i]>=35:
            DMP_p+=1

    sub_tot=[Python_t,C_Programming_t,DSA_t,DMP_t]
    sub_pass=[Python_p,C_Programming_p,DSA_p,DMP_p]
    pass_df=pd.DataFrame({"Total Appear":sub_tot, "Total Pass":sub_pass})
    pass_df.index=['Python','C_Programming','DSA','DMP']
    print(pass_df)
    print()
    print()
    while True:
        choice=input("Enter type of chart : L-Line, B-Bar, X-Exit :")
        if choice=='L':    
            pass_df.plot(kind="line",rot=30,linewidth=3,linestyle='dashed',marker='^',markeredgecolor='r')
        elif choice=='B':
            pass_df.plot(kind="bar",color=['purple','red'],rot=30)
        else:
            print("Exiting......")
            break
        plt.xlabel('Subject ->',color='r',fontsize=12)
        plt.ylabel('No.of Students->',color='r',fontsize=12)
        gtitle1=s_name+"\nSubject Wise Total vs Pass Analysis "+branch
        plt.title(gtitle1,fontsize=16,color='b')
        plt.grid()
        plt.show()

   
# Subject wise 90% and above Analysis
def ninety_above():
    Python_t=df.Python.count()
    C_Programming_t=df.C_Programming.count()
    DSA_t=df.DSA.count()
    DMP_t=df.DMP.count()
    Python_90=df.loc[(df.Python>=90),'Python'].count()
    C_Programming_90=df.loc[(df.C_Programming>=90),'C_Programming'].count()
    DSA_90=df.loc[(df.DSA>=90),'DSA'].count()
    DMP_90=df.loc[(df.DMP>=90),'DMP'].count()

    sub_tot=[Python_t,C_Programming_t,DSA_t,DMP_t]
    sub_ab_90=[Python_90,C_Programming_90,DSA_90,DMP_90]
    ab_90_df=pd.DataFrame({"Total Appear":sub_tot, "90 & Above":sub_ab_90})
    ab_90_df.index=['Python','C_Prgramming','DSA','DMP']
    print(ab_90_df)
    print()
    print()
    while True:
        choice=input("Enter type of chart : L-Line, B-Bar, X-Exit :")
        if choice=='L':    
            ab_90_df.plot(kind="line",rot=30,linewidth=3,linestyle='dashed',marker='^',markeredgecolor='r')
        elif choice=='B':
            ab_90_df.plot(kind="bar",color=['purple','red'],rot=30)
        else:
            print("Exiting......")
            break
        plt.xlabel('Subject ->',color='r',fontsize=12)
        plt.ylabel('No.of Students->',color='r',fontsize=12)
        gtitle1=s_name+"\nSubject Wise Total vs Above 90% Analysis "+branch
        plt.title(gtitle1,fontsize=16,color='b')
        plt.grid()
        plt.show()
def subject_mean():
    print("-"*80)
    print("\t\tSUBJECT WISE MEAN")
    print("\t\t-----------------")
    print("\t Python                : ",round(df.Python.mean(),2))
    print("\t C Programming         : ",round(df.C_Programming.mean(),2))
    print("\t DSA                   : ",round(df.DSA.mean(),2))
    print("\t DMP                   : ",round(df.DMP.mean(),2))
    overallmean=(df.Python.sum()+df.C_Programming.sum()+df.DSA.sum()+df.DMP.sum()
    )/(df.Python.count()+df.C_Programming.count()+df.DSA.count()+df.DMP.count())
    print("\t\t SCHOOL OVERALL MEAN")
    print("\t\t--------------------")
    print("\t\t\t",round(overallmean,2))
    print("\t\t-------------------")
    print("-"*80)
    print("Hit Enter to continue........")
    key=input()


# Top 10 Students
def top_10():
    df_top10=df.sort_values(by='Grade').head(10)
    print("-------------- TOP 10 STUDENTS (GRADE WISE) ---------------")
    print(E_no,"-",s_name,"                  Branch :",branch)
    print("----------------------------------------------------------------")
    print(df_top10[['Name','Grade']])
    print()
    print()
    print("Hit Enter to continue........")
    key=input()

# EXECUTING MAIN PROGRAM
menu()