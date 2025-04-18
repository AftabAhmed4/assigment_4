import streamlit as st

# ---- Page Configuration ----
st.set_page_config(page_title="Quick Portfolio", page_icon="💼", layout="centered")

# ---- Sidebar ----
st.sidebar.title("Navigation")
section = st.sidebar.radio("Go to", ["Home", "About", "Contact"])

# ---- Home Section ----
if section == "Home":
    st.title("👋 Welcome to My Streamlit Website")
    st.subheader("Built in 15 minutes with Python & Streamlit")

    name = st.text_input("Enter your name:")
    mood = st.selectbox("How are you feeling today?", ["Happy 😊", "Sad 😔", "Excited 🤩", "Tired 😴"])

    if name:
        st.success(f"Hello, {name}! It's great to know you're feeling {mood} today.")

    st.markdown("---")
    st.markdown("### 🔧 Technologies Used")
    st.markdown("- Python")
    st.markdown("- Streamlit")
    st.markdown("- Markdown + HTML")

# ---- About Section ----
elif section == "About":
    st.title("📄 About This App")
    st.write("""
        This is a simple yet professional demo of a web app built using **Streamlit**.
        It's perfect for quick prototypes, dashboards, data visualization, or even portfolios.
        
        Built by: *Your Name Here Aftab Ahmed*  
        GitHub: [https://github.com/AftabAhmed4]
    """)

# ---- Contact Section ----
elif section == "Contact":
    st.title("📬 Contact Me")
    st.write("Have a question or want to collaborate? Drop your message below.")

    with st.form("contact_form"):
        user_email = st.text_input("Your Email")
        user_message = st.text_area("Your Message")
        submitted = st.form_submit_button("Send")

        if submitted:
            st.success("✅ Message sent successfully! (This is a demo — no actual message was sent.)")

# ---- Footer ----
st.markdown("---")
st.markdown("© 2025 | Built with ❤️ using Streamlit")
