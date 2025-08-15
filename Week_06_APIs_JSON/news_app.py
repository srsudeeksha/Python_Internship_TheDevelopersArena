# news_app.py
# Week 6 Task – News App using API and JSON

import requests

def get_top_headlines(api_key, country="us", category=None):
    """
    Fetch top headlines using NewsAPI.
    
    Args:
        api_key (str): Your NewsAPI API key
        country (str): Country code (e.g., 'us', 'in', 'gb')
        category (str): Optional category (e.g., 'technology', 'sports')
    
    Returns:
        list: List of articles (each as a dictionary)
    """
    base_url = "https://newsapi.org/v2/top-headlines"
    params = {
        "country": country,
        "apiKey": api_key
    }
    if category:
        params["category"] = category

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()
        return data.get("articles", [])
    except requests.exceptions.RequestException as err:
        print(f"⚠️ Error fetching news: {err}")
        return []


def display_news(articles, limit=5):
    """
    Display a list of news articles.
    
    Args:
        articles (list): List of article dictionaries
        limit (int): Maximum number of articles to display
    """
    if not articles:
        print("❌ No news articles found.")
        return

    print(f"\n📰 Top {limit} News Headlines:\n" + "-" * 40)
    for i, article in enumerate(articles[:limit], start=1):
        title = article.get("title", "No Title")
        source = article.get("source", {}).get("name", "Unknown Source")
        url = article.get("url", "No URL")
        print(f"{i}. {title}")
        print(f"   🏷 Source: {source}")
        print(f"   🔗 Read more: {url}\n")


def main():
    print("📰 News App (Week 6 Project)")
    api_key = input("Enter your NewsAPI API Key: ").strip()
    country = input("Enter country code (default: us): ").strip() or "us"
    category = input("Enter category (optional, e.g., technology): ").strip() or None

    articles = get_top_headlines(api_key, country, category)
    display_news(articles, limit=5)


if __name__ == "__main__":
    main()
