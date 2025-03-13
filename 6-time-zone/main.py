# Import required libraries
import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo

# List of available time zones
TIME_ZONES = [
    "UTC",
    "Asia/Karachi",
    "America/New_York",
    "Europe/London",
    "Asia/Tokyo",
    "Australia/Sydney",
    "America/Los_Angeles",
    "Europe/Berlin",
    "Asia/Dubai",
    "Asia/Kolkata",
]

# Create app title
st.title("Time Zone App")

# Create a multi-select dropdown for choosing time zones
selected_timezone = st.multiselect(
    "Select Timezones", TIME_ZONES, default=["UTC", "Asia/Karachi"]
)

# Display current time for selected time zones
st.subheader("Selected Timezones")
for tz in selected_timezone:
    # Get and format current time for each selected timezone with AM/PM
    converted_time = datetime.now(ZoneInfo(tz)).strftime("%y-%m-%d %H-%M-%S")
    st.success(f"Converted Time in {tz}: {converted_time}")

# Create convert time between timezones section
st.subheader("Convert Time Between Timezones")
# Create time input field with current time as default
current_time = st.time_input("Current Time", value=datetime.now().time())
# Dropdown to select source timezone
from_tz = st.selectbox("From Timezone", TIME_ZONES, index=0)
to_timezone = st.selectbox("To Timezone", TIME_ZONES, index=1)

if st.button("Convert Time"):
    dt = datetime.combine(datetime.today(), current_time, tzinfo=ZoneInfo(from_tz))
    converted_time = dt.astimezone(ZoneInfo(to_timezone)).strftime("%y-%m-%d %H-%M-%S")
    st.success(f"Converted time in {to_timezone}: {converted_time}")