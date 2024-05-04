# import streamlit as st
# import pickle
# import string
# # from nltk.corpus import stopwords
# # import nltk
# # nltk.download('punkt')
# # nltk.download('stopwords')
# # from nltk.stem.porter import PorterStemmer

# # ps = PorterStemmer()


# # def transform_text(text):
# #     text = text.lower()
# #     text = nltk.word_tokenize(text)

# #     y = []
# #     for i in text:
# #         if i.isalnum():
# #             y.append(i)

# #     text = y[:]
# #     y.clear()

# #     for i in text:
# #         if i not in stopwords.words('english') and i not in string.punctuation:
# #             y.append(i)

# #     text = y[:]
# #     y.clear()

# #     for i in text:
# #         y.append(ps.stem(i))

# #     return " ".join(y)

# tfidf = pickle.load(open('vectorizer.pkl','rb'))
# model = pickle.load(open('model.pkl','rb'))

# st.title("Insurance Fraud Detection")
# st.write("Project created by Dipen Kalsi(01514812721), Paras Jain(02014812721) and Raghav Agarwal(01414812721)")
# st.write("Submitted to: Dr.Pooja Gupta")

      
# months_as_customer = st.text_area("Enter the no. of months since you have been a customer: ")
# age = st.text_area("Enter your age: ")
# policy_number = st.text_area("Enter your policy number: ")
# policy_bind_date = st.text_area("Enter your policy Bind date: ")
# policy_state = st.text_area("Enter the state where you bought the policy: ")
# policy_csl = st.text_area("Enter policy CSL: ")
# policy_deductable = st.text_area("Enter the deductable amount: ")
# policy_annual_premium = st.text_area("Enter your policy annual premium: ")

# umbrella_limit = st.text_area("Enter your umbrella limit: ")
# insured_zip = st.text_area("Enter your insured ZIP code: ")
# insured_sex = st.text_area("Enter your gender: ")
# insured_education_level = st.text_area("Enter your education level: ")
# insured_occupation = st.text_area("Enter your occupation: ")
# insured_hobbies = st.text_area("Enter your hobbies: ")
# insured_relationship = st.text_area("Enter your relationship status: ")
# capital_gains = st.text_area("Enter your capital gains: ")
# capital_loss = st.text_area("Enter your capital loss: ")
# incident_date = st.text_area("Enter the date of the incident: ")
# incident_type = st.text_area("Enter the type of incident: ")
# collision_type = st.text_area("Enter the type of collision: ")
# incident_severity = st.text_area("Enter the severity of the incident: ")
# authorities_contacted = st.text_area("Enter the authorities contacted: ")
# incident_state = st.text_area("Enter the state of the incident: ")
# incident_city = st.text_area("Enter the city of the incident: ")
# incident_location = st.text_area("Enter the location of the incident: ")
# incident_hour_of_the_day = st.text_area("Enter the hour of the day of the incident: ")
# number_of_vehicles_involved = st.text_area("Enter the number of vehicles involved: ")
# property_damage = st.text_area("Enter property damage details: ")
# bodily_injuries = st.text_area("Enter the number of bodily injuries: ")
# witnesses = st.text_area("Enter the number of witnesses: ")
# police_report_available = st.text_area("Enter if police report is available: ")
# total_claim_amount = st.text_area("Enter the total claim amount: ")
# injury_claim = st.text_area("Enter the injury claim amount: ")
# property_claim = st.text_area("Enter the property claim amount: ")
# vehicle_claim = st.text_area("Enter the vehicle claim amount: ")
# auto_make = st.text_area("Enter the make of your vehicle: ")
# auto_model = st.text_area("Enter the model of your vehicle: ")
# auto_year = st.text_area("Enter the year of your vehicle: ")
# # fraud_reported = st.text_area("Enter if fraud was reported: ")
# _c39 = 'N/A'

# if st.button('Predict'):

    
#     # # 2. vectorize
#     # vector_input = tfidf.transform([transformed_sms])
#     # # 3. predict
#     result = model.predict(vector_input)[0]
#     # # 4. Display
#     # if result == 1:
#     #     st.header("Spam")
#     # else:
#     #     st.header("Not Spam")





import streamlit as st
import pickle

# Load the trained model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# Define the input form
st.title("Insurance Fraud Detection")
st.write("Project created by Dipen Kalsi(01514812721), Paras Jain(02014812721) and Raghav Agarwal(01414812721)")
st.write("Submitted to: Dr.Pooja Gupta")


months_as_customer = st.text_area("Enter the number of months since you have been a customer: ")
age = st.text_area("Enter your age: ")
policy_number = st.text_area("Enter your policy number: ")
policy_bind_date = st.text_area("Enter your policy Bind date: ")
policy_state = st.text_area("Enter the state where you bought the policy: ")
policy_csl = st.text_area("Enter policy CSL: ")
policy_deductable = st.text_area("Enter the deductable amount: ")
policy_annual_premium = st.text_area("Enter your policy annual premium: ")
umbrella_limit = st.text_area("Enter your umbrella limit: ")
insured_zip = st.text_area("Enter your insured ZIP code: ")
insured_sex = st.text_area("Enter your gender: ")
insured_education_level = st.text_area("Enter your education level: ")
insured_occupation = st.text_area("Enter your occupation: ")
insured_hobbies = st.text_area("Enter your hobbies: ")
insured_relationship = st.text_area("Enter your relationship status: ")
capital_gains = st.text_area("Enter your capital gains: ")
capital_loss = st.text_area("Enter your capital loss: ")
incident_date = st.text_area("Enter the date of the incident: ")
incident_type = st.text_area("Enter the type of incident: ")
collision_type = st.text_area("Enter the type of collision: ")
incident_severity = st.text_area("Enter the severity of the incident: ")
authorities_contacted = st.text_area("Enter the authorities contacted: ")
incident_state = st.text_area("Enter the state of the incident: ")
incident_city = st.text_area("Enter the city of the incident: ")
incident_location = st.text_area("Enter the location of the incident: ")
incident_hour_of_the_day = st.text_area("Enter the hour of the day of the incident: ")
number_of_vehicles_involved = st.text_area("Enter the number of vehicles involved: ")
property_damage = st.text_area("Enter property damage details: ")
bodily_injuries = st.text_area("Enter the number of bodily injuries: ")
witnesses = st.text_area("Enter the number of witnesses: ")
police_report_available = st.text_area("Enter if police report is available: ")
total_claim_amount = st.text_area("Enter the total claim amount: ")
injury_claim = st.text_area("Enter the injury claim amount: ")
property_claim = st.text_area("Enter the property claim amount: ")
vehicle_claim = st.text_area("Enter the vehicle claim amount: ")
auto_make = st.text_area("Enter the make of your vehicle: ")
auto_model = st.text_area("Enter the model of your vehicle: ")
auto_year = st.text_area("Enter the year of your vehicle: ")

# Create a list of all input features
input_features = [
    months_as_customer, age, policy_number, policy_bind_date, policy_state,
    policy_csl, policy_deductable, policy_annual_premium, umbrella_limit,
    insured_zip, insured_sex, insured_education_level, insured_occupation,
    insured_hobbies, insured_relationship, capital_gains, capital_loss,
    incident_date, incident_type, collision_type, incident_severity,
    authorities_contacted, incident_state, incident_city, incident_location,
    incident_hour_of_the_day, number_of_vehicles_involved, property_damage,
    bodily_injuries, witnesses, police_report_available, total_claim_amount,
    injury_claim, property_claim, vehicle_claim, auto_make, auto_model, auto_year
]

# Predict button
if st.button("Predict"):
    # Ensure numerical input features are correctly processed
    # Adjust the types of the features according to your model needs
    processed_features = [float(f) if f.replace('.', '', 1).isdigit() else f for f in input_features]
    
    # Predict the output using the loaded model
    prediction = model.predict([processed_features])[0]
    
    # Display the result
    if prediction == 1:
        st.write("The claim is fraudulent.")
    else:
        st.write("The claim is not fraudulent.")