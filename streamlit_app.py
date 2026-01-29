import streamlit as st

st.title("Sign Up")

def convertFtoC(temp):
    return (temp - 32) * 5/9

def convertCtoF(temp):
    return temp * 9/5 + 32

temp_input = st.slider("Select the temperature value",
                       min_value =-100,
                       max_value=200,
                       value=32)
conv_type = st.radio("Select conversion type:",options=
                     ["Fahrenheit to celsius"
                      "Celsius to Fahrenheit"])

if conv_type == "Fahrenheit to Celsius":
    output = convertFtoC(temp_input)
    st.metric(label="Converted Temperature", value=output)

elif conv_type == "Celsius to Fahrenheit":
    output = convertCtoF(temp_input)
    st.metric(label="Converted Temperature", value=output)

if "history" not in st.session_state:
    st.session_state["history"] = []

    st.session_state.history.append((temp_input, conv_type))
    print(st.session_state.history)

    st.divider()
    history_data = st.session_state.history

    rev = list(reversed(st.session_state.history[-5:]))

    st.subheader("Recent conversions:")

    for i, (temp,conv, output) in enumerate(rev,1):
        st.write(f"{i}, {temp} ({conv})->{output}")
