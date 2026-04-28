agents = []

def add_agent(**kwargs):
    name = kwargs.get("name")
    agent = {"name": name, "missions": []}
    agents.append(agent)
    print("Agent added successfully!")

def assign_mission(name, *scores):
    for agent in agents:
        if agent["name"] == name:
            for score in scores:
                agent["missions"].append(score)
            print("Mission scores added!")
            return
    print("Agent not found!")

def view_agents():
    for agent in agents:
        print(agent)

def calculate_average(agent):
    if len(agent["missions"]) == 0:
        return 0
    return sum(agent["missions"]) / len(agent["missions"])

def top_agent():
    top = None
    highest = 0

    for agent in agents:
        avg = calculate_average(agent)
        if avg > highest:
            highest = avg
            top = agent

    if top:
        print("Top Agent:", top["name"], "Score:", highest)

def assign_rank(avg):
    if avg >= 90:
        return "Elite Agent"
    elif avg >= 75:
        return "Senior Agent"
    elif avg >= 50:
        return "Junior Agent"
    else:
        return "Failed Agent"

def generate_report():
    for agent in agents:
        avg = calculate_average(agent)
        rank = assign_rank(avg)
        print("\nName:", agent["name"])
        print("Missions:", agent["missions"])
        print("Average:", avg)
        print("Rank:", rank)

while True:
    print("\n--- Spy Mission System ---")
    print("1. Add Agent")
    print("2. Assign Mission")
    print("3. View Agents")
    print("4. Show Top Agent")
    print("5. Generate Report")
    print("6. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Enter agent name: ")
        add_agent(name=name)

    elif choice == 2:
        name = input("Enter agent name: ")
        scores = list(map(int, input("Enter mission scores: ").split()))
        assign_mission(name, *scores)

    elif choice == 3:
        view_agents()

    elif choice == 4:
        top_agent()

    elif choice == 5:
        generate_report()

    elif choice == 6:
        print("Exiting...")
        break

    else:
        print("Invalid choice!")