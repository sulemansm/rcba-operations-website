import streamlit as st
from utils import parse_names
from report_generator import generate_report
from docx_builder import build_docx
from database import save_report

st.title("Create Event Report")

title=st.text_input("Event Title")
venue=st.text_input("Venue")
chief_guest=st.text_input("Chief Guest")

description=st.text_area("Event Description")

pre_event=st.text_area("Pre Event Work")
on_day=st.text_area("On Day Work")
post_event=st.text_area("Post Event Work")

outcome=st.text_area("Outcome")

names_input=st.text_area("Member Names")

names,attendance=parse_names(names_input)

st.metric("Attendance",attendance)

income=st.number_input("Income",0)
expenditure=st.number_input("Expenditure",0)

profit_loss=income-expenditure

if st.button("Generate Draft"):

    report=generate_report({
        "title":title,
        "venue":venue,
        "chief_guest":chief_guest,
        "description":description,
        "pre_event":pre_event,
        "on_day":on_day,
        "post_event":post_event,
        "outcome":outcome
    })

    st.session_state.report=report


if "report" in st.session_state:

    edited=st.text_area("Edit Draft",st.session_state.report,height=400)

    drive_link=st.text_input("Drive Link")
    avenue=st.text_input("Avenue")
    project_level=st.text_input("Project Level")
    project_hours=st.text_input("Project Hours")

    days=st.number_input("Days",1)
    man_hours=days*24

    created_by=st.text_input("Project Chairperson")

    if st.button("Generate DOCX"):

        docx=build_docx(
            {
                "title":title,
                "venue":venue,
                "start_time":"",
                "end_time":"",
                "chief_guest":chief_guest
            },
            edited,
            {
                "Attendance":attendance,
                "Income":income,
                "Expenditure":expenditure,
                "Profit/Loss":profit_loss,
                "Drive Link":drive_link,
                "Avenue":avenue,
                "Project Level":project_level,
                "Project Hours":project_hours,
                "Man Hours":man_hours,
                "Created By":created_by
            }
        )

        st.download_button("Download DOCX",docx,file_name=f"{title}.docx")

        save_report([
            title,venue,"","",
            attendance,income,expenditure,profit_loss,
            drive_link,avenue,project_level,
            project_hours,str(man_hours),created_by
        ])