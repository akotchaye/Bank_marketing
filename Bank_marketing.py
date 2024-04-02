import pandas as pd
import numpy as np
import datetime as dt
# Start coding here...
#convert the csv file into dataframe
df=pd.read_csv("bank_marketing.csv")

#subset client dataframe
client=df.iloc[:,0:7]

#cleaning operations


#convert the datatype into int
client["client_id"]=client["client_id"].astype("int")
#convert the datatype into int
client["age"]=client["age"].astype("int")

#replace "." by "_"
client["job"]=client["job"].str.replace(".","_")

#replace "." by "_"
client["education"]=client["education"].str.replace(".","_")

#replace "unknown" by "np.NaN"
client.loc[client["education"]=="unknown","education"]=np.NaN

#replace "yes" to "1"
client["credit_default"]=client["credit_default"].str.replace("yes","1")

#replace "unknown" to "1"
client["credit_default"]=client["credit_default"].str.replace("unknown","0")
#replace "no" to "0"
client["credit_default"]=client["credit_default"].str.replace("no","0")
#convert the datatype into int
client["credit_default"]=client["credit_default"].astype("int")
#convert the datatype into bool
client["credit_default"]=client["credit_default"].astype("bool")

#replace "yes" to "1"
client["mortgage"]=client["mortgage"].str.replace("yes","1")
#replace "unknown" to "1"
client["mortgage"]=client["mortgage"].str.replace("unknown","0")
#replace "no" to "0"
client["mortgage"]=client["mortgage"].str.replace("no","0")
#convert the datatype into int
client["mortgage"]=client["mortgage"].astype("int")
#convert the datatype into bool
client["mortgage"]=client["mortgage"].astype("bool")

#subset campaign dataframe 
campaign=df.loc[:,["client_id","number_contacts","contact_duration","previous_campaign_contacts","previous_outcome","campaign_outcome"]]
#cleaning and add the last column

#change "success" by "1"
campaign["previous_outcome"]=campaign["previous_outcome"].str.replace("success","1")
#replace other values to "0"
campaign["previous_outcome"]=campaign["previous_outcome"].str.replace("nonexistent","0")
campaign["previous_outcome"]=campaign["previous_outcome"].str.replace("failure","0")


#convert the datatype into integer
campaign["client_id"]=campaign["client_id"].astype("int")
#convert the datatype into integer
campaign["number_contacts"]=campaign["number_contacts"].astype("int")
#convert the datatype into integer
campaign["contact_duration"]=campaign["contact_duration"].astype("int")
#convert the datatype into integer
campaign["previous_campaign_contacts"]=campaign["previous_campaign_contacts"].astype("int")

#convert the datatype into int
campaign["previous_outcome"]=campaign["previous_outcome"].astype("int")

#convert the datatype into bool
campaign["previous_outcome"]=campaign["previous_outcome"].astype("bool")

#change "yes" by "1"
campaign["campaign_outcome"]=campaign["campaign_outcome"].str.replace("yes","1")

#replace other values to "0"
campaign["campaign_outcome"]=campaign["campaign_outcome"].str.replace("no","0")
#convert the datatype into int
campaign["campaign_outcome"]=campaign["campaign_outcome"].astype("int")

#convert the datatype into bool
campaign["campaign_outcome"]=campaign["campaign_outcome"].astype("bool")

# campaign["year"]="2022"

# campaign["day"]=df["day"].astype("str")
day=df["day"].astype("str")
# campaign["last_contact_date"]=campaign["day"]+"-"+df["month"]+"-"+campaign["year"]
campaign["last_contact_date"]=day+"-"+df["month"]+"-"+"2022"

campaign["last_contact_date"]=pd.to_datetime(campaign["last_contact_date"],infer_datetime_format=True,errors = 'coerce')
# formatting the date
campaign["last_contact_date"]=campaign["last_contact_date"].dt.strftime("%Y-%m-%d")
# campaign["last_contact_date"]=campaign["last_contact_date"].astype(str)
# # converting to datetime
campaign["last_contact_date"]=pd.to_datetime(campaign["last_contact_date"])

#subset economics dataframe (ok)
economics=df.loc[:,["client_id","cons_price_idx","euribor_three_months"]]

#economics dataframe into csv
economics.to_csv('economics.csv',index=False)
#compaign dataframe into csv
campaign.to_csv('campaign.csv',index=False)
#client dataframe into csv
client.to_csv('client.csv',index=False)