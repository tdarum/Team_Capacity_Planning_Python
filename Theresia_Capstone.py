# Dummy data for redistributed task
team_1 = {
    "1001": {"name": "Ferzi", "workload": 28, "tasks": [{"name": "Task A", "workload": 2}, {"name": "Task B", "workload": 3},{"name": "Task D", "workload": 4},{"name": "Task E", "workload": 5},{"name": "Task F", "workload": 6},{"name": "Task G", "workload": 8}], "capacity": 15, "remaining_capacity":-13 },
    "1002": {"name": "Aries", "workload": 8, "tasks": [{"name": "Task C", "workload": 8},], "capacity": 10,"remaining_capacity":2},
    "1003": {"name": "Rifqi", "workload": 0, "tasks": [], "capacity": 12,"remaining_capacity":12},
    "1004": {"name": "There", "workload": 5, "tasks": [{"name": "Task K", "workload": 5}], "capacity": 12,"remaining_capacity":7}
}

team_2 = {
    "2001": {"name": "Adit", "workload": 7, "tasks": [{"name": "Task X", "workload": 3},{"name": "Task Y", "workload": 4}], "capacity": 20,"remaining_capacity":13},
    "2002": {"name": "Valen", "workload": 6, "tasks": [{"name": "Task Z", "workload": 6}], "capacity": 15,"remaining_capacity":9},
    "2003": {"name": "Edo", "workload": 3, "tasks": [{"name": "Task Q", "workload": 3}], "capacity": 18,"remaining_capacity":15}
}

def show_tabulate_team(team):
    print('+------------+----------+-----------+---------+---------+--------------------')
    print('| {:<10} | {:<8} | {:<8} | {:<8} |{:<8} |{:<12} |'.format('Member ID','Name', 'Workload', 'Tasks', 'Capacity','Remaining Capacity'))
    print('+------------+----------+-----------+---------+---------+--------------------')

    # Print  data item.
    for member, val in team.items():
        print('| {:<10} | {:<8} | {:<8} | {:<8} |{:<8} |{:<18} |'.format(member,val["name"], val["workload"], len(val["tasks"]), val["capacity"], val["remaining_capacity"]))

    # Print the footer
    print('+------------+----------+-----------+---------+---------+--------------------')
    return

# Calculate team workload
def calculate_team_workload(team):
    team_workload_update = sum(member["workload"] for member in team.values())
    return team_workload_update

# Calculate team capacity
def calculate_team_capacity(team):
    team_capacity_update = sum(member["capacity"] for member in team.values())
    return team_capacity_update

# Calculate remaining capacity
def calculate_remaining_team_capacity(team):
    team_remaining_capacity = calculate_team_capacity(team) - calculate_team_workload(team)
    return team_remaining_capacity

# Add a team member
def add_team_member(team):
    member_id = input("Enter Member ID: ")
    if member_id in team:
        print(f"Member ID {member_id} already exists.")
    else:
        name = input("Enter Member Name: ")
        
        capacity = int(input("Enter Capacity: "))

        confirmation = input(f"Are you sure you want to add member '{member_id}':'{name}' with capacity '{capacity}'(yes/no)? ").lower()

        if confirmation == 'yes':
        
            #add remaining capacity here 
            #-----------------------
            team[member_id] = {"name": name, "workload": 0, "tasks": [], "capacity": capacity, "remaining_capacity": capacity}
            #calculcate team workload and capacity
            team_workload = calculate_team_workload(team)
            team_capacity = calculate_team_capacity(team)
            #add team reminaing capacitty
            team_remaining_capcity = calculate_remaining_team_capacity(team)
            print(f"Added new member: {name} (ID: {member_id})")
            print(f"Team workload has been updated to {team_workload}")
            print(f"Team capacity has been updated to {team_capacity}")
            print(f"Team remaining capacity has been updated to {team_remaining_capcity}")


# Add a task to a team member, with task name and workload as input
def add_task(team, member_id):

    if member_id in team:
        print(f"{team[member_id]['name']} has remaining capacity {team[member_id]['remaining_capacity']}")
        task_name = input("Enter Task Name : ")
        task_workload = int(input("Enter Task Workload : "))

        team[member_id]["tasks"].append({"name": task_name, "workload": task_workload})
        #Add the task workload to the member total workload
       # team[member_id]["workload"] += task_workload 
        
       # team[member_id]["remaining_capacity"] = team[member_id]["capacity"] - team[member_id]["workload"]

        confirmation = input(f"Are you sure you want to add task '{task_name} to {team[member_id]['name']}' (yes/no)? ").lower()
        
        if confirmation == 'yes':
            
            #Add the task workload to the member total workload
            team[member_id]["workload"] += task_workload 
        
            team[member_id]["remaining_capacity"] = team[member_id]["capacity"] - team[member_id]["workload"]
            team_workload = calculate_team_workload(team)
            team_capacity = calculate_team_capacity(team)
            #add team remianing capacity
            #add team reminaing capacitty
            #team[member_id] = {"name": name, "workload": 0, "tasks": [], "capacity": capacity, "remaining_capacity": capacity}
            team_remaining_capcity = calculate_remaining_team_capacity(team)
            print(f"Added task '{task_name}' with workload {task_workload} to {team[member_id]['name']}.")
            print(f"Team workload is {team_workload}")
            print(f"Maximum team capacity is  {team_capacity}")
            print(f"Team remaining capacity has been updated to {team_remaining_capcity}")
        else :
            print(f'Task addition is cancled')
    else:
        print(f"Member ID {member_id} not found.")


# Function to update a task for a team member
def update_task(team, member_id):
    if member_id in team:
        tasks = team[member_id]["tasks"]
        
        # Check if the member has tasks
        if len(tasks) <= 0:
            print(f"{team[member_id]['name']} has no tasks.")
            return
        
        print(f"{team[member_id]['name']} has remaining capacity {team[member_id]['remaining_capacity']}")
        # Show the tasks with the task index
        print(f"Tasks for {team[member_id]['name']}:")
        index = 0
        for task in tasks:
            print(f"{index}: Task Name : {task['name']}, Workload : {task['workload']}")
            index += 1  # Increment index
        
        # Input Task index from member that was chosen
        try:
            task_index = int(input("Enter the index of the task that you want to update: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            return
        
        # Check if the index is valid
        if 0 <= task_index < len(tasks):
            old_task = tasks[task_index]
            # Get new task details from the user
            new_task_name = input("Enter the new task name: ")
            new_task_workload_input = input("Enter the new task workload: ")
            
            # Check if the input for workload is valid
            while not new_task_workload_input.isdigit():
                print("Invalid input for workload. Please enter a valid number.")
                new_task_workload_input = input("Enter the new task workload: ")

            # Convert to int
            new_task_workload = int(new_task_workload_input)
            
            # Update the task: sact old task's workload, then add the new one
            team[member_id]["workload"] -= old_task["workload"]
            tasks[task_index] = {"name": new_task_name, "workload": new_task_workload}
            team[member_id]["workload"] += new_task_workload 
            
            # Update remaining capacity
            team[member_id]["remaining_capacity"] = team[member_id]["capacity"] - team[member_id]["workload"]
            print(f"Updated task '{old_task['name']}' to '{new_task_name}' for {team[member_id]['name']}.")

            # Calculate team workload and capacity again
            team_workload = calculate_team_workload(team)
            team_capacity = calculate_team_capacity(team)
            team_remaining_capacity = calculate_remaining_team_capacity(team)

            print(f"Team workload is {team_workload}")
            print(f"Maximum team capacity is {team_capacity}")
            print(f"Team remaining capacity has been updated to {team_remaining_capacity}")
        else:
            print("Task not found.")
    else:
        print(f"Member ID {member_id} not found.")

# Delete a task from a member with confirmation and task selection
def delete_task(team, member_id):
    if member_id in team:
        member = team[member_id]
        
        # Check if the member has any tasks
        if len(member["tasks"]) == 0:
            print(f"{member['name']} has no tasks to delete.")
            return
        
        # Display tasks and their indices
        print(f"Tasks for {member['name']} (ID: {member_id}):")
        for i in range(len(member["tasks"])):
            task = member["tasks"][i]
            print(f"{i+1}: Task name : {task['name']}, Workload : {task['workload']}")
        
        # Ask user to choose a task by index
       # try:
        task_index = int(input("Enter the task number you want to delete: ")) - 1
        if task_index < 0 or task_index >= len(member["tasks"]):
            print("Task number is not found.")
            return
       # except ValueError:
        #    print("Invalid input. Please enter a valid number.")
        #   return

        # Confirm deletion
        selected_task = member["tasks"][task_index]
        confirmation = input(f"Are you sure you want to delete task '{selected_task['name']}' (yes/no)? ").lower()
        
        if confirmation == 'yes':
            # Delete the task and update workload
            member["workload"] -= selected_task["workload"]
            del member["tasks"][task_index]
            print(f"Deleted task '{selected_task['name']}' from {member['name']}.")

            team[member_id]["remaining_capacity"] = team[member_id]["capacity"] - team[member_id]["workload"]
            team_workload = calculate_team_workload(team)
            team_capacity = calculate_team_capacity(team)
            #add team remianing capacity
            #add team reminaing capacitty
            team_remaining_capcity = calculate_remaining_team_capacity(team)
            #print(f"Added task '{task_name}' with workload {task_workload} to {team[member_id]['name']}.")
            print(f"Team workload is {team_workload}")
            print(f"Maximum team capacity is  {team_capacity}")
            print(f"Team remaining capacity has been updated to {team_remaining_capcity}")
        else:
            print("Task deletion canceled.")
    else:
        print(f"Member ID {member_id} not found.")

# Delete a team member with confirmation
def delete_team_member(team, member_id):
    if member_id in team:
        # Display member information and ask for confirmation
        print(f"Member found: {team[member_id]['name']} (ID: {member_id})")
        #input proceed to cancle and the input from user will be change to lower case
        confirmation = input(f"Are you sure you want to delete {team[member_id]['name']} (ID: {member_id})? (yes/no): ").lower()

        if confirmation == 'yes':
            del team[member_id]
            print(f"Team member with ID {member_id} is deleted.")
            team_workload = calculate_team_workload(team)
            team_capacity = calculate_team_capacity(team)
            #add team remianing capacity
            #add team reminaing capacitty
            team_remaining_capcity = calculate_remaining_team_capacity(team)
            #print(f"Added task '{task_name}' with workload {task_workload} to {team[member_id]['name']}.")
            print(f"Team workload is {team_workload}")
            print(f"Maximum team capacity is  {team_capacity}")
            print(f"Team remaining capacity has been updated to {team_remaining_capcity}")
        else:
            print("Delete canceled.")
    else:
        print(f"Member ID {member_id} not exist or not foundd.")

# Automaticaly Redistribute tasks from one member to another
# Redistribute tasks based on team capacity
def redistribute_tasks_across_member(team):
    # find overcapcity menmber
    over_capacity_members = [member for member in team.values() if member["workload"] > member["capacity"]]
    #find undercapacity member
    under_capacity_members = [member for member in team.values() if member["workload"] < member["capacity"]]

    # Sorting over_capacity_members by most over capacity and under_capacity_members by most available capacity
    over_capacity_members.sort(key=lambda x: x["workload"] - x["capacity"], reverse=True)

    under_capacity_members.sort(key=lambda x: x["remaining_capacity"], reverse=True)

    for over_member in over_capacity_members:
        while over_member["workload"] > over_member["capacity"] and under_capacity_members:
            # Pick the first under-capacity member (who has the most remaining capacity)
            under_member = under_capacity_members[0]
            task_to_transfer = over_member["tasks"][0]  # Transfer the first task from the overburdened member
            over_member["tasks"] = over_member["tasks"][1:]

            # Update the workload and capacity of both members
            over_member["workload"] -= task_to_transfer["workload"]
            under_member["tasks"].append(task_to_transfer)
            under_member["workload"] += task_to_transfer["workload"]

            # Update remaining capacities
            over_member["remaining_capacity"] = over_member["capacity"] - over_member["workload"]
            under_member["remaining_capacity"] = under_member["capacity"] - under_member["workload"]

            # If the under_capacity member is now at capacity, remove them from the list
            if under_member["workload"] >= under_member["capacity"]:
                #under_capacity_members.pop(0)
                under_capacity_members = under_capacity_members[1:]
    
    print("Tasks have been redistributed based on member capacities.")

    team_workload = calculate_team_workload(team)
    team_capacity = calculate_team_capacity(team)
    #add team remianing capacity
    #add team reminaing capacitty
    team_remaining_capcity = calculate_remaining_team_capacity(team)
#print(f"Added task '{task_name}' with workload {task_workload} to {team[member_id]['name']}.")
    print(f"Team workload is {team_workload}")
    print(f"Maximum team capacity is  {team_capacity}")
    print(f"Team remaining capacity has been updated to {team_remaining_capcity}")


def display_team_member_capacity(team):
    # Calculate team capacity and workload
    team_capacity = calculate_team_capacity(team)
    team_workload = calculate_team_workload(team)
    team_remaining_capcity = calculate_remaining_team_capacity(team)

    # Display team workload and capacity
    print(f"Workload: {team_workload} , Maximum team capacity : {team_capacity}, Reaminig Capacity : {team_remaining_capcity}")

    # Choice for sorting or filtering choice
    print("Choose an option to sort of filter members:")
    print("1. Sort by workload (highest to lowest)")
    print("2. Sort by workload (lowest to highest)")
    print("3. Filter members with no tasks")


    choice = input("Enter your choice (1, 2, or 3): ")

    # Sort or filter based on user input
    if choice == "1":
        # To sort by workload (from highest to lowest)
        members = sorted(team.items(), key=lambda x: x[1]["workload"], reverse=True)

    elif choice == "2":
        # To sort by workload from lowest to highest
        members = sorted(team.items(), key=lambda x: x[1]["workload"], reverse=False)
        
    elif choice == "3":
        # Filter members with no tasks
        members = [(member_id, member) for member_id, member in team.items() if not member["tasks"]]
    else:
        print("Invalid choice please choose .")
        return

    # Display sorted/filtered team members
    print('+------------+----------+-----------+---------+---------+--------------------')
    print('| {:<10} | {:<8} | {:<8} | {:<8} |{:<8} |{:<18} |'.format('Member ID', 'Name', 'Workload', 'Tasks', 'Capacity', 'Remaining Capacity'))
    print('+------------+----------+-----------+---------+---------+--------------------')

    # Print each member's data
    for member_id, member in members:
        tasks_count = len(member['tasks'])
        print('| {:<10} | {:<8} | {:<8} | {:<8} |{:<8} |{:<18} |'.format(
            member_id, member["name"], member["workload"], tasks_count, member["capacity"], member["remaining_capacity"]
        ))

    print('+------------+----------+-----------+---------+---------+--------------------')



def main():
    while True:
        #print option menu
        print("1. Add Team Member")
        print("2. Add Task")
        print("3. Redistribute Tasks")
        print("4. Display Member ")
        print("5. Delete Team Member")
        print("6. Delete Task")
        print("7. Update Task")
        print("0. Exit")
        choice = input("Select menu that you want to choose: ")
        
        if choice == "1":
            team_choice = input("Select Team (1/2): ")
            if team_choice == "1":
                add_team_member(team_1)
                show_tabulate_team(team_1)
            elif team_choice == "2":
                add_team_member(team_2)
                show_tabulate_team(team_2)

        elif choice == "2":
            team_choice = input("Select Team (1/2): ")
            member_id = input("Enter Member ID : ")
            if team_choice == "1":
                add_task(team_1, member_id)
                show_tabulate_team(team_1)
            elif team_choice == "2":
                add_task(team_2, member_id)
                show_tabulate_team(team_2)

        elif choice == "3":
            team_choice = input("Select Team (1/2): ")
            if team_choice == "1":
                redistribute_tasks_across_member(team_1)
                show_tabulate_team (team_1)
            elif team_choice == "2":
                redistribute_tasks_across_member(team_2)
                show_tabulate_team(team_2)

        elif choice == "4":
            team_choice = input("Select Team (1/2): ")
            if team_choice == "1":
                display_team_member_capacity(team_1)
            elif team_choice == "2":
                display_team_member_capacity(team_2)

        elif choice == "5":
            team_choice = input("Select Team (1/2): ")
            member_id = input("Enter Member ID : ")
            if team_choice == "1":
                delete_team_member(team_1, member_id)
                show_tabulate_team (team_1)
            elif team_choice == "2":
                delete_team_member(team_2, member_id)
                show_tabulate_team (team_2)

        elif choice == "6":
            team_choice = input("Select Team (1/2): ")
            member_id = input("Enter Member ID : ")
            if team_choice == "1":
                delete_task(team_1, member_id)
                show_tabulate_team (team_1)
            elif team_choice == "2":
                delete_task(team_2, member_id)
                show_tabulate_team (team_2)
                
        elif choice == "7":
            team_choice = input("Select Team (1/2): ")
            member_id = input("Enter Member ID : ")
            if team_choice == "1":
                update_task(team_1, member_id)
                show_tabulate_team (team_1)
                #update_task(team_1)
            elif team_choice == "2":
                update_task(team_2, member_id)
                show_tabulate_team (team_2)
        elif choice == "0":
            break
        else:
            print("The menu do not exists. Please choose 0-7.\n")

main()