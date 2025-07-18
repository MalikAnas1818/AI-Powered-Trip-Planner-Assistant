from TravelAgents import guide_expert, location_expert, planner_expert
from TravelTasks import location_task, guide_task, planner_task
from crewai import Crew, Process
from_city = "Lahore"
destination_city = "Rome"
date_from = "2025-08-10"
date_to = "2025-08-20"
interests = ["history", "food", "museums"]
# Initialize Tasks
loc_task = location_task(location_expert, from_city, destination_city, date_from, date_to)
guid_task = guide_task(guide_expert, destination_city, interests, date_from, date_to)
plan_task = planner_task([loc_task, guid_task], planner_expert, destination_city, interests, date_from, date_to),
crew = Crew(
            agents=[location_expert, guide_expert, planner_expert],
            tasks=[loc_task, guid_task, plan_task],
            process=Process.sequential,
            full_output=True,
            verbose=True,
        )