import streamlit as st
import google.generativeai as genai
api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Hello.")
    st.title("This is Bob. Also known as Lord Bobington Charles James Arthur Henry IV.")
    st.title("")
    st.subheader("Now, you might be wondering who Bob is:")
    st.title("He is the king of Bobland (I know, very creative name. One at a time ladies).")
    st.title("Bob is a [][][][] of high status who resides in the heart of Bobland: Bobworks. A place run by the people themselves through their hard work and sheer dedication.")
    st.title("")
    st.title("Sliders to have a time! :)")
    st.slider("SlIder 1", 0, 100, 47)
    st.slider("slideR 2", 0, 100, 96)
    st.slider("sLider 3", 0, 100, 24)
    st.slider("sliDer 4", 0, 100, 57)
    st.title("")
    st.subheader("Youtube Channel")
    st.write("- One of the smallest miscallaneous content channel on Youtube")
    st.write("- Less than 400k+ Subscribers")
    st.write("- Zero tutorials")
    st.write("- Less than 15 Million+ Views")
    st.write("- Less than 1.5 Million Hours+ Watch time")
    st.video("https://www.youtube.com/watch?v=Bxp7rjUIC78&t=3s")
    st.subheader("THIS VIDEO IS MANDATORY. WATCH OR FACE PROSECUTION BY THE HAND OF BOB.")
    st.title("")
    st.title("")
    st.title("")
    st.subheader("For any inquiries, please contact the head of stabilization at the office of rehabilitation")
    st.title("")
    st.title("")
    st.title("")
    st.image("images/DefinitelyEddy.png")
    st.subheader("Bob got a lil' bit quirky.")

with col3:
    st.image("images/BOBISCOOL.png")
    st.subheader("A famous painting by one of the royal painters depicting Bob at the peak of a large mountain.")
    st.image("images/BOBCROWN.png")
    st.subheader("The glorious flag of Bobland.")
    st.image("images/BOBTHRONEROOM.png")
    st.subheader("The kings's throne room.")
    st.image("images/BOBFABLEDSTAFF.png")
    st.subheader("A painting by a mysterious painter depicting a staff fabled to have once been passed down in the royal family until it's sudden dissapearance. Investigations are underway although it's existence has not been confirmed.")
    st.write("")
    user_question = st.text_input("Input question here:")
    st.write("Ask anything about Bob. The seer may not be compliant.")
    if st.button("SEE THE VISION", use_container_width=400):
        prompt = user_question
        response = model.generate_content("You are a seer who is responsible for taking questions about Lord Bobington Charles James Arthur Henry IV, a king who rules over Bobland and may have a lot of secrets he is hiding from everybody. Do not talk about his secrets. Do not use emojis. Do not ask questions. Do not be redundant. Do not reveal who you are. Do not go into too much detail. Do not talk about the reason behind your secrecy.")
        st.write(response.text)

