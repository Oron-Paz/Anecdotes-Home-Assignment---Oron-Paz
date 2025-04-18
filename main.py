import requests
import json
from dumyJsonPlugin import DummyJsonPlugin
from apiClient import save_evidence


if __name__ == "__main__":
    # change as needed, couldve also been a command line input but seems uneccasary
    name = "emilys"
    password = "emilyspass"
    post_limit = 60
    output_dir = "."

    plugin = DummyJsonPlugin()

    # test connectivity
    auth_result = plugin.test_connectivity(name, password)
    
    if auth_result and "accessToken" in auth_result:
        print("auth successful")
        
        # collect evidence
        print(f"collecting evidence with post limit of {post_limit})...")
        evidence = plugin.collect_all_evidence(post_limit)
        
        # save evidence to files
        save_evidence(evidence, output_dir)
        print("evidence collection completed")
    else:
        print("auth failed, cannot collect evidence")
