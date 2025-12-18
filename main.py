from pyscript import display, document

club_info = {
            "army": {
                "name": "Dumbledore's Army",
                "description": "A secret group for Defense Against the Dark Arts training.",
                "meeting_time": "Every Tuesday and Friday 3:30-6:00 PM",
                "location": "Room of Requirement",
                "advisor": "Harry Potter",
                "members": "30",
                "category": "Exclusive"
            },
            "dueling": {
                "name": "Dueling Club",
                "description": "For students to practice spells and combat. ",
                "meeting_time": "Every Monday and Thursday 4:00-6:00 PM",
                "location": "Chamber of Secrets ",
                "advisor": "Remus Lupin",
                "members": "67",
                "category": "Academic"
            },
            "potions": {
                "name": "Potions Club",
                "description": "Focused on practical potion-making and magical plants.",
                "meeting_time": "Every Tuesday 3:30-4:30 PM",
                "location": " Potions Classroom",
                "advisor": "Severus Snape",
                "members": "32",
                "category": "Academic"
            },
            "dragon": {
                "name": "Dragon Club",
                "description": "For adventurers, focusing on Quidditch, dueling, and DADA. ",
                "meeting_time": "Every Friday 3:30-5:00 PM",
                "location": "Training Grounds",
                "advisor": "Rolanda Hooch",
                "members": "16",
                "category": "Academic"
            },
            "hippogriff": {
                "name": "Hippogriff Club",
                "description": "For nature lovers, involving Care of Magical Creatures, Divination, and food. ",
                "meeting_time": "Every Wednesday 3:30-5:00 PM",
                "location": "Grounds at Hagrid's Hut",
                "advisor": "Rubeus Hagrid",
                "members": "14",
                "category": "Academic"
            },
            "gobstones": {
                "name": "Gobstones Club",
                "description": "A club for playing the wizarding game Gobstones. ",
                "meeting_time": "Every Friday 3:45-5:15",
                "location": "Classroom 22b",
                "advisor": "Sybill Trelawney",
                "members": "20",
                "category": "Arts"
            }
}
def show_club_info(e):
    selected_club = document.getElementById("club-select").value
    info = club_info.get(selected_club, club_info)
            
    output = f"""
            {info['name']}
            Description:{info['description']}
            Meeting Time: {info['meeting_time']}
            Location: {info['location']}
            Advisor: {info['advisor']}
            Number of Members: {info['members']}
            Category: {info['category']}
            """
    display(output, target="club-info")