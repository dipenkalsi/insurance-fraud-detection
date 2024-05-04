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

# Load the pickled model
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Define the function to predict fraud
def predict_fraud(inputs):
    # Assuming model.predict() takes a list of inputs and returns prediction
    prediction = model.predict(inputs)
    return prediction

def main():
    st.title('AI Insurance Fraud Detection')

    # Inputs
    months_as_customer = st.text_input("Enter the no. of months since you have been a customer: ")
    age = st.text_input("Enter your age: ")
    policy_number = st.text_input("Enter your policy number: ")
    policy_bind_date = st.text_input("Enter your policy Bind date: ")
    policy_state = st.text_input("Enter the state where you bought the policy: ")
    policy_csl = st.text_input("Enter policy CSL: ")
    policy_deductable = st.text_input("Enter the deductible amount: ")
    policy_annual_premium = st.text_input("Enter your policy annual premium: ")
    umbrella_limit = st.text_input("Enter your umbrella limit: ")
    insured_zip = st.text_input("Enter your insured ZIP code: ")
    insured_sex = st.text_input("Enter your gender: ")
    insured_education_level = st.text_input("Enter your education level: ")
    insured_occupation = st.text_input("Enter your occupation: ")
    insured_hobbies = st.text_input("Enter your hobbies: ")
    insured_relationship = st.text_input("Enter your relationship status: ")
    capital_gains = st.text_input("Enter your capital gains: ")
    capital_loss = st.text_input("Enter your capital loss: ")
    incident_date = st.text_input("Enter the date of the incident: ")
    incident_type = st.text_input("Enter the type of incident: ")
    collision_type = st.text_input("Enter the type of collision: ")
    incident_severity = st.text_input("Enter the severity of the incident: ")
    authorities_contacted = st.text_input("Enter the authorities contacted: ")
    incident_state = st.text_input("Enter the state of the incident: ")
    incident_city = st.text_input("Enter the city of the incident: ")
    incident_location = st.text_input("Enter the location of the incident: ")
    incident_hour_of_the_day = st.text_input("Enter the hour of the day of the incident: ")
    number_of_vehicles_involved = st.text_input("Enter the number of vehicles involved: ")
    property_damage = st.text_input("Enter property damage details: ")
    bodily_injuries = st.text_input("Enter the number of bodily injuries: ")
    witnesses = st.text_input("Enter the number of witnesses: ")
    police_report_available = st.text_input("Enter if police report is available: ")
    total_claim_amount = st.text_input("Enter the total claim amount: ")
    injury_claim = st.text_input("Enter the injury claim amount: ")
    property_claim = st.text_input("Enter the property claim amount: ")
    vehicle_claim = st.text_input("Enter the vehicle claim amount: ")
    auto_make = st.text_input("Enter the make of your vehicle: ")
    auto_model = st.text_input("Enter the model of your vehicle: ")
    auto_year = st.text_input("Enter the year of your vehicle: ")

    inputs = [
        [months_as_customer, age, policy_number, policy_bind_date, policy_state, policy_csl, policy_deductable,
         policy_annual_premium, umbrella_limit, insured_zip, insured_sex, insured_education_level, insured_occupation,
         insured_hobbies, insured_relationship, capital_gains, capital_loss, incident_date, incident_type,
         collision_type, incident_severity, authorities_contacted, incident_state, incident_city, incident_location,
         incident_hour_of_the_day, number_of_vehicles_involved, property_damage, bodily_injuries, witnesses,
         police_report_available, total_claim_amount, injury_claim, property_claim, vehicle_claim, auto_make,
         auto_model, auto_year]
    ]

    # Predict button
    if st.button('Predict'):
        prediction = predict_fraud(inputs)
        st.write('Fraudulent Claim' if prediction == 1 else 'Legitimate Claim')

if __name__ == '__main__':
    main()
