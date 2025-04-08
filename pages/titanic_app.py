import streamlit as st
import requests

st.title("Titanic Survival Prediction App")

# --- Initialising SessionState ---
if "job_id" not in st.session_state:
    st.session_state.job_id = None

st.header("Synchronous Request")
with st.expander("Show/hide values"):
    pclass = st.pills("Passenger Class", [1, 2, 3])
    sex = st.radio("Sex", ["Male", "Female"])
    age = st.slider("Age", 0, 100, 30)
    fare = st.number_input("Fare", value=15.0)

    if st.button("Predict"):
        sync_data = {
            "Pclass": pclass,
            "Sex": 0 if sex == "Male" else 1,
            "Age": age,
            "Fare": fare
        }
        response = requests.post("http://localhost:8000/titanic_sync", json=sync_data)
        if response.status_code == 200:
            result = response.json()
            st.success(f"Predicted survival probability: {result['survival_probability']:.2%}")
        else:
            st.error("Something went wrong. Check the API.")

st.header("Asynchronous Request")
with st.expander("Show/hide values"):
    pclass_async = st.pills("Passenger Class", [1, 2, 3], key="pclass_async")
    sex_async = st.radio("Sex", ["Male", "Female"], key="sex_async")
    age_async = st.slider("Age", 0, 100, 30, key="age_async")
    fare_async = st.number_input("Fare", value=15.0, key="fare_async")

    if st.button("Submit Async Job"):
        async_data = {
            "Pclass": pclass_async,
            "Sex": 0 if sex_async == "Male" else 1,
            "Age": age_async,
            "Fare": fare_async
        }
        submit_response = requests.post("http://localhost:8000/titanic_async", json=async_data)

        if submit_response.status_code == 200:
            st.session_state.job_id = submit_response.json().get("job_id")
            st.info(f"Job submitted. Job ID: {st.session_state.job_id}")
        else:
            st.error("Failed to submit async request.")

    if st.session_state.job_id and st.button("Check Job Result"):
        result_response = requests.get(f"http://localhost:8000/titanic_async/{st.session_state.job_id}")
        if result_response.status_code == 200:
            result_json = result_response.json()
            if result_json.get("status") == "Done":
                st.success(f"Predicted survival probability: {result_json['survival_probability']:.2%}")
            else:
                st.warning("Job is still processing. Try again in a moment.")
        else:
            st.error("Failed to fetch job result.")
