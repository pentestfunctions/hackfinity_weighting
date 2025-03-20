import requests
import json
from collections import defaultdict

def get_scoreboard_page(room_code, page, limit=10):
    """
    Fetch a page of the scoreboard from the TryHackMe API
    
    Args:
        room_code (str): The room code
        page (int): The page number to fetch
        limit (int): Number of results per page
        
    Returns:
        dict: The JSON response from the API
    """
    url = f"https://tryhackme.com/api/v2/rooms/scoreboard?roomCode={room_code}&limit={limit}&page={page}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching page {page}: Status code {response.status_code}")
        return None

def extract_top_players(room_code, total_pages=5, limit=10):
    """
    Extract player data from multiple pages of the scoreboard
    
    Args:
        room_code (str): The room code
        total_pages (int): Number of pages to fetch
        limit (int): Number of results per page
        
    Returns:
        list: List of all team/player data from the scoreboard
    """
    all_data = []
    
    for page in range(1, total_pages + 1):
        print(f"Fetching page {page}...")
        data = get_scoreboard_page(room_code, page, limit)
        
        if data and data["status"] == "success" and "docs" in data["data"]:
            all_data.extend(data["data"]["docs"])
        else:
            print(f"Failed to fetch page {page} or no data returned")
            
    return all_data

def get_difficulty_multiplier(score):
    """
    Determine the difficulty multiplier based on the task score
    
    Args:
        score (int): The score value of the task
        
    Returns:
        float: The difficulty multiplier
    """
    if score == 15:  # Beginner
        return 1.0
    elif score == 30:  # Easy
        return 1.5
    elif score == 60:  # Medium
        return 2.0
    elif score in [40, 90]:  # Hard
        return 3.0
    else:
        # Default case if score doesn't match known difficulties
        return 1.0

def get_difficulty_name(score):
    """
    Get the difficulty name based on the score
    
    Args:
        score (int): The score value of the task
        
    Returns:
        str: The difficulty name
    """
    if score == 15:
        return "Beginner"
    elif score == 30:
        return "Easy"
    elif score == 60:
        return "Medium"
    elif score in [40, 90]:
        return "Hard"
    else:
        return "Unknown"

def calculate_user_scores(scoreboard_data):
    """
    Calculate total scores and weighted scores for each user based on task submissions
    
    Args:
        scoreboard_data (list): The scoreboard data from the API
        
    Returns:
        dict: A dictionary of user data keyed by username
    """
    user_data = defaultdict(lambda: {
        "total_score": 0,
        "weighted_score": 0,
        "correct_answers": 0,
        "avatar": "",
        "teams": set(),
        "task_submissions": [],
        "difficulty_breakdown": {
            "Beginner": 0,
            "Easy": 0,
            "Medium": 0,
            "Hard": 0,
            "Unknown": 0
        }
    })
    
    for entry in scoreboard_data:
        # Get team information if available
        team_id = entry.get("team", {}).get("_id", "individual")
        team_name = entry.get("team", {}).get("name", "Individual")
        
        # Process all tasks
        tasks = entry.get("tasks", {})
        for task_id, submissions in tasks.items():
            for submission in submissions:
                if submission.get("correct", False):
                    # Extract user info - handle both object and string formats
                    answerer = submission.get("answeredBy", {})
                    
                    # Check if answeredBy is a string or an object
                    if isinstance(answerer, str):
                        username = answerer
                        avatar = ""
                    else:
                        username = answerer.get("username", "unknown")
                        avatar = answerer.get("avatar", "")
                    
                    score = submission.get("score", 0)
                    difficulty = get_difficulty_name(score)
                    multiplier = get_difficulty_multiplier(score)
                    weighted_score = score * multiplier
                    
                    # Update user data
                    user_data[username]["total_score"] += score
                    user_data[username]["weighted_score"] += weighted_score
                    user_data[username]["correct_answers"] += 1
                    user_data[username]["difficulty_breakdown"][difficulty] += 1
                    
                    if avatar:  # Only update avatar if we have one
                        user_data[username]["avatar"] = avatar
                    
                    user_data[username]["teams"].add((team_id, team_name))
                    
                    # Add submission details
                    user_data[username]["task_submissions"].append({
                        "task_id": task_id,
                        "score": score,
                        "weighted_score": weighted_score,
                        "difficulty": difficulty,
                        "multiplier": multiplier,
                        "attempts": submission.get("attempts", 1),
                        "time": submission.get("timeCorrect", "")
                    })
    
    # Convert sets to lists for JSON serialization
    for username, data in user_data.items():
        data["teams"] = [{"id": team[0], "name": team[1]} for team in data["teams"]]
    
    return user_data

def main():
    # Configuration
    room_code = "HackfinityBattle"
    total_pages = 5
    limit = 10  # This will get us 50 players total across 5 pages
    output_file = "tryhackme_scoreboard_results.json"
    
    # Fetch and extract data
    scoreboard_data = extract_top_players(room_code, total_pages, limit)
    print(f"Extracted data for {len(scoreboard_data)} entries")
    
    # Process user data
    user_data = calculate_user_scores(scoreboard_data)
    print(f"Processed scores for {len(user_data)} unique users")
    
    # Sort users by weighted score (primary) and then by raw score (secondary)
    sorted_users = sorted(
        [{"username": username, **data} for username, data in user_data.items()],
        key=lambda x: (x["weighted_score"], x["total_score"]),
        reverse=True
    )
    
    # Display all users and their rankings
    print("\nAll Users Ranked by Weighted Points (with difficulty multipliers):")
    print("=" * 100)
    print(f"{'Rank':<5}{'Username':<25}{'Raw Points':<12}{'Weighted':<12}{'B/E/M/H':<15}{'Team':<30}")
    print("-" * 100)
    
    for i, user in enumerate(sorted_users, 1):
        if user["teams"]:
            teams = ", ".join([team["name"] for team in user["teams"]])
        else:
            teams = "Individual"
        
        # Format the output in columns for better readability
        username = user['username'][:23] + ".." if len(user['username']) > 23 else user['username']
        teams_display = teams[:28] + ".." if len(teams) > 28 else teams
        
        # Get difficulty breakdown
        breakdown = user["difficulty_breakdown"]
        diff_str = f"{breakdown['Beginner']}/{breakdown['Easy']}/{breakdown['Medium']}/{breakdown['Hard']}"
        
        print(f"{i:<5}{username:<25}{user['total_score']:<12}{user['weighted_score']:<12.1f}{diff_str:<15}{teams_display:<30}")
    
    # Save results
    results = {
        "top_users": sorted_users,  # All users
        "total_users": len(user_data),
        "room_code": room_code,
        "timestamp": "2025-03-21",
        "difficulty_weights": {
            "Beginner": 1.0,
            "Easy": 1.5,
            "Medium": 2.0,
            "Hard": 3.0
        }
    }
    
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to {output_file}")

if __name__ == "__main__":
    main()
