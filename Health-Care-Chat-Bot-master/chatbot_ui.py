import streamlit as st
import pandas as pd
import os


USER_DATA_FILE = "user_data.csv"

if not os.path.exists(USER_DATA_FILE):
    pd.DataFrame(columns=["username", "password"]).to_csv(USER_DATA_FILE, index=False)

def load_users():
    return pd.read_csv(USER_DATA_FILE)

def save_user(username, password):
    # Ensure usernames are unique
    users = load_users()
    if username.strip() in users["username"].values:
        return False  # User already exists

   
    new_user = pd.DataFrame([[username.strip(), password.strip()]], columns=["username", "password"])
    users = pd.concat([users, new_user], ignore_index=True)
    users.to_csv(USER_DATA_FILE, index=False)
    return True

def authenticate_user(username, password):
    users = load_users()
    user = users[users["username"].str.strip() == username.strip()]
    if not user.empty and user.iloc[0]["password"].strip() == password.strip():
        return True
    return False

def main():
    st.title("Healthcare Chatbot with Account Management")

    
    page = st.sidebar.radio("Navigation", ["Login", "Register", "Chatbot"])

    if page == "Register":
        st.subheader("Register")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Register"):
            if username and password:
                if save_user(username, password):
                    st.success("Registration successful! You can now log in.")
                else:
                    st.error("Username already exists. Please choose a different one.")
            else:
                st.error("Please fill out both fields.")

    elif page == "Login":
        st.subheader("Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            if authenticate_user(username, password):
                st.session_state["logged_in"] = True
                st.session_state["username"] = username
                st.success(f"Welcome back, {username}!")
            else:
                st.error("Invalid username or password.")

    elif page == "Chatbot":
        if "logged_in" in st.session_state and st.session_state["logged_in"]:
            st.subheader(f"Welcome to the Chatbot, {st.session_state['username']}!")

            # Chatbot interaction code
            st.write("Chatbot functionality is coming soon...")

        else:
            st.warning("You need to log in to access the chatbot.")
            st.sidebar.warning("Please log in to access the Chatbot.")

if __name__ == "__main__":
    main()
# import streamlit as st
# import pandas as pd
# import os

# # Simulated user data storage
# USER_DATA_FILE = "user_data.csv"

# if not os.path.exists(USER_DATA_FILE):
#     pd.DataFrame(columns=["username", "password"]).to_csv(USER_DATA_FILE, index=False)

# def load_users():
#     return pd.read_csv(USER_DATA_FILE)

# def save_user(username, password):
#     # Ensure usernames are unique
#     users = load_users()
#     if username.strip() in users["username"].values:
#         return False  # User already exists

#     # Save new user
#     new_user = pd.DataFrame([[username.strip(), password.strip()]], columns=["username", "password"])
#     users = pd.concat([users, new_user], ignore_index=True)
#     users.to_csv(USER_DATA_FILE, index=False)
#     return True

# def authenticate_user(username, password):
#     users = load_users()
#     user = users[users["username"].str.strip() == username.strip()]
#     if not user.empty and user.iloc[0]["password"].strip() == password.strip():
#         return True
#     return False

# def main():
#     st.title("Healthcare Chatbot with Account Management")

#     # Navigation
#     page = st.sidebar.radio("Navigation", ["Login", "Register", "Chatbot"])

#     if page == "Register":
#         st.subheader("Register")
#         username = st.text_input("Username")
#         password = st.text_input("Password", type="password")
#         if st.button("Register"):
#             if username and password:
#                 if save_user(username, password):
#                     st.success("Registration successful! You can now log in.")
#                 else:
#                     st.error("Username already exists. Please choose a different one.")
#             else:
#                 st.error("Please fill out both fields.")

#     elif page == "Login":
#         st.subheader("Login")
#         username = st.text_input("Username")
#         password = st.text_input("Password", type="password")
#         if st.button("Login"):
#             if authenticate_user(username, password):
#                 st.session_state["logged_in"] = True
#                 st.session_state["username"] = username
#                 st.success(f"Welcome back, {username}!")
#             else:
#                 st.error("Invalid username or password.")

#     elif page == "Chatbot":
#         if "logged_in" in st.session_state and st.session_state["logged_in"]:
#             st.subheader(f"Welcome to the Chatbot, {st.session_state['username']}!")

#             # Chatbot interaction code
#             st.write("Chatbot functionality is coming soon...")

#         else:
#             st.warning("You need to log in to access the chatbot.")
#             st.sidebar.warning("Please log in to access the Chatbot.")

# if __name__ == "__main__":
#     main()
