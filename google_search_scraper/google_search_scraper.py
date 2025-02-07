import requests
import json

# Replace with your free SerpAPI key (https://serpapi.com/)
API_KEY = "c2f9608dd6bae29729ae3581907f90ff5f0f2daf0e9a4bb154b431cb694c558d"
SEARCH_QUERY = "best laptop 2024"

def scrape_google_results(query):
    url = f"https://serpapi.com/search?engine=google&q={query}&api_key={API_KEY}"
    response = requests.get(url)
    results = response.json()

    search_results = []
    for result in results.get("organic_results", [])[:10]:
        search_results.append({
            "Title": result.get("title"),
            "Link": result.get("link"),
            "Snippet": result.get("snippet", "No description available")
        })

    return search_results

# Scrape Google search results
search_data = scrape_google_results(SEARCH_QUERY)

# Save results to a JSON file
with open("google_results.json", "w", encoding="utf-8") as file:
    json.dump(search_data, file, indent=4)

print("✅ Google search results saved to google_results.json")

