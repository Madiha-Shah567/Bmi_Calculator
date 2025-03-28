import streamlit as st

st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Raleway:wght@300;400;600&display=swap');
        
        html, body, [data-testid="stAppViewContainer"] {
            background: linear-gradient(to right, #E3FDFD, #FFE6FA) !important;
            background-attachment: fixed;
            background-size: cover;
            font-family: 'Raleway', sans-serif;
            color: black;
        }

        .title {
            text-align: center;
            font-size: 50px;
            font-weight: 700;
            color: #FF4500;
            text-shadow: 2px 2px 10px rgba(0, 0, 0, 0.3);
            padding: 20px;
        }

        .stNumberInput input {
            background-color: white !important;
            border-radius: 12px !important;
            border: 2px solid #FF4500 !important;
            padding: 12px !important;
            box-shadow: 0px 4px 12px rgba(255, 69, 0, 0.4);
            font-size: 18px !important;
            color: black !important;
        }

        .stButton>button {
            background: linear-gradient(to right, #ffcc00, #ff6699) !important;
            color: white !important;
            border-radius: 30px !important;
            padding: 15px 40px !important;
            font-size: 22px !important;
            font-weight: bold !important;
            border: none !important;
            box-shadow: 0px 5px 15px rgba(255, 102, 153, 0.6);
            transition: all 0.3s ease-in-out;
        }

        .stButton>button:hover {
            transform: scale(1.1);
            box-shadow: 0px 6px 20px rgba(255, 102, 153, 0.8);
        }

        .footer {
            text-align: center;
            font-size: 18px;
            font-weight: 400;
            color: black;
            margin-top: 40px;
            padding: 15px;
            background: rgba(255, 69, 0, 0.2);
            border-radius: 12px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<h1 class="title">🔥 BMI Calculator 🔥</h1>', unsafe_allow_html=True)

col1, col2 = st.columns([1, 1])

with col1:
    weight = st.number_input("⚖️ Enter your weight (kg)", min_value=1.0, format="%.2f", key="weight")

with col2:
    height_cm = st.number_input("📏 Enter your height (cm)", min_value=1.0, format="%.2f", key="height")

height_m = height_cm / 100

if st.button("💪 Calculate BMI"):
    if height_m > 0:
        bmi = weight / (height_m ** 2)
        st.success(f"🎯 Your BMI is: {bmi:.2f}")

        if bmi < 18.5:
            st.warning("⚠️ You are Underweight. Consider a balanced diet and strength training.")
        elif 18.5 <= bmi < 25:
            st.success("✅ You have a Normal Weight. Keep maintaining a healthy lifestyle!")
        elif 25 <= bmi < 30:
            st.warning("⚠️ You are Overweight. Regular exercise and a balanced diet can help.")
        else:
            st.error("🚨 You are Obese. Consult a healthcare professional for guidance.")
    else:
        st.error("❌ Please enter a valid height.")

st.markdown('<div class="footer">🚀 Created with ❤️ by Madiha Shah</div>', unsafe_allow_html=True)
