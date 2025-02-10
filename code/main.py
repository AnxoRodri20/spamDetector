import joblib

loaded_model = joblib.load('model/sms_spam_model.pkl')
vectorizer = joblib.load('model/sms_spam_vectorizer.pkl')
new_sms = input("Enter an sms: ")
new_sms = vectorizer.transform([new_sms])
prediction = loaded_model.predict(new_sms)

if prediction[0] == "spam":
    print("This email is spam.")
else:
    print("This email is not spam.")
