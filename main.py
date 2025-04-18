import requests
import json

#tested api connection, dont need this but im keeping it so you can see my work process :)
response = requests.get("https://dummyjson.com/test")
print (response.json())

# login with user / test connectivity
def connectivity_test(username: str, password: str):
    payload = {
        "username": username,
        "password": password
    }

    response = requests.post('https://dummyjson.com/auth/login', json=payload)
    if response.status_code == 200:
        data = response.json()
        print("Response data:", data)
        return data
    else:
        print(f"Login error with code: {response.status_code}")
        print(f"Response: {response.text}")
        return None

# evidence collection (E1,E2,E3)
def collect_evidence(accessToken):
    headers = {
        "Authorization": accessToken,
        "Content-Type": "application/json"
    }

    def collect_E1_user_details():
        response = requests.get('https://dummyjson.com/auth/me', headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to collect user details: {response.status_code}")
            return None
        
    def collect_E2_posts():
        response = requests.get('https://dummyjson.com/posts/?limit=60', headers=headers)
        if response.status_code == 200:
            data = response.json()
            return data.get("posts", [])
        else:
            print(f"Failed to collect posts: {response.status_code}")
            return []
        
    def collect_E3_posts_with_comments():
        posts = collect_E2_posts()

        for post in posts:
            post_id = post.get("id")
            response = requests.get(f'https://dummyjson.com/posts/{post_id}/comments', headers=headers)
            if response.status_code == 200:
                comments_data = response.json()
                # Add comments to the post
                post["comments"] = comments_data.get("comments", [])
            else:
                print(f"Failed to get comments for post {post_id}: {response.status_code}")
                post["comments"] = []
        
        return posts

    return {
        "E1_user_details": collect_E1_user_details(),
        "E2_posts": collect_E2_posts(),
        "E3_posts_with_comments": collect_E3_posts_with_comments()
    }


if __name__ == "__main__":
    # get connection 
    valid_login = connectivity_test("emilys", "emilyspass")

    if valid_login and "accessToken" in valid_login:
        
        evidence = collect_evidence(valid_login["accessToken"])
        
        # save evidence to files
        with open("E1_user_details.json", "w") as f:
            json.dump(evidence["E1_user_details"], f, indent=2)
        
        with open("E2_posts.json", "w") as f:
            json.dump(evidence["E2_posts"], f, indent=2)
        
        with open("E3_posts_with_comments.json", "w") as f:
            json.dump(evidence["E3_posts_with_comments"], f, indent=2)
        
        print("Evidence collection completed successfully!")
    else:
        print("Cannot collect evidence due to failed connectivity test.")