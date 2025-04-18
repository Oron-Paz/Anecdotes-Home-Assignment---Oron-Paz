from apiClient import ApiClient

#plugin that inherets from APIClient
class DummyJsonPlugin(ApiClient):
    def __init__(self):
        super().__init__("https://dummyjson.com")
    
    #use parent class to authenticate 
    def test_connectivity(self, username, password):
        return self.authenticate("auth/login", {
            "username": username,
            "password": password
        })
    
    def collect_user_details(self):
        return self.get("auth/me")
    
    def collect_posts(self, limit=60):
        response = self.get("posts", params={"limit": limit})
        return response.get("posts", []) if response else []
    
    def collect_posts_with_comments(self, limit=60):
        posts = self.collect_posts(limit)
        
        for post in posts:
            post_id = post.get("id")
            comments_data = self.get(f"posts/{post_id}/comments")
            post["comments"] = comments_data.get("comments", []) if comments_data else []
        
        return posts
    
    def collect_all_evidence(self, post_limit=60):
        return {
            "E1_user_details": self.collect_user_details(),
            "E2_posts": self.collect_posts(post_limit),
            "E3_posts_with_comments": self.collect_posts_with_comments(post_limit)
        }