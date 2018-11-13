import pandas as p

data = p.read_csv("data/CRDC2013_14.csv",encoding ="Latin-1")

data["total_enrollment"]= data["TOT_ENR_M"]+data["TOT_ENR_F"]

all_enrollment = data["total_enrollment"].sum()

total_M= (data["TOT_ENR_M"].sum()/all_enrollment)*100

total_F= (data["TOT_ENR_F"].sum()/all_enrollment)*100

total_H = ((data["SCH_ENR_HI_M"].sum()+data["SCH_ENR_HI_F"].sum()) /all_enrollment)*100

total_AM = ((data["SCH_ENR_AM_M"].sum()+data["SCH_ENR_AM_F"].sum()) /all_enrollment)*100

total_AS = ((data["SCH_ENR_AS_M"].sum()+data["SCH_ENR_AS_F"].sum()) /all_enrollment)*100

total_HP = ((data["SCH_ENR_HP_M"].sum()+data["SCH_ENR_HP_F"].sum()) /all_enrollment)*100

total_BL = ((data["SCH_ENR_BL_M"].sum()+data["SCH_ENR_BL_F"].sum()) /all_enrollment)*100

total_WH = ((data["SCH_ENR_WH_M"].sum()+data["SCH_ENR_WH_F"].sum()) /all_enrollment)*100

total_TR = ((data["SCH_ENR_TR_M"].sum()+data["SCH_ENR_TR_F"].sum()) /all_enrollment)*100

races={"Female":total_F,"Male":total_M, "Hispanic":total_H, "American Indian":total_AM, "Asian": total_AS, "Hawaiian or Pacific Islander" : total_HP, "Black": total_BL,"White":total_WH, "Two or more races": total_TR}

for k,v in races.items():
    #value="total_"+k
   
    print("The ratio of total {} population is {}".format(k,v))
