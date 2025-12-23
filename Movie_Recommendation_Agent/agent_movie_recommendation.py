import sys
from rich.prompt import Prompt
from rich.console import Console
from rich.markdown import Markdown

console = Console()

def get_tollywood_movies():
    return """
# 🎬 Telugu Movies Perfect for Date Night (2024-2025)

## Top Romantic Telugu Movies

### 1. **Kushi** (2023)
- **Genre**: Romance/Drama
- **Cast**: Vijay Deverakonda, Samantha Ruth Prabhu
- **Director**: Shiva Nirvana
- **Rating**: ⭐ 7.2/10
- **Plot**: A heartwarming tale of love, relationships, and family bonds set against beautiful backdrops.
- **Why Perfect**: Great chemistry between leads, beautiful songs, family-friendly content
- **Streaming**: Netflix, Amazon Prime Video

### 2. **Pushpa 2: The Rule** (2024)
- **Genre**: Action/Romance
- **Cast**: Allu Arjun, Rashmika Mandanna
- **Director**: Sukumar
- **Rating**: ⭐ 8.2/10
- **Plot**: Pushpa Raj continues his rise with intense action and romantic moments with Srivalli.
- **Why Perfect**: Blockbuster entertainment, great music, Allu Arjun's charisma
- **Streaming**: Amazon Prime Video (post-theatrical)

### 3. **Kalki 2898 AD** (2024)
- **Genre**: Sci-Fi/Action
- **Cast**: Prabhas, Deepika Padukone
- **Director**: Nag Ashwin
- **Rating**: ⭐ 7.8/10
- **Plot**: A futuristic epic blending mythology with advanced technology.
- **Why Perfect**: Visual spectacle, unique concept, star power
- **Streaming**: Netflix, Amazon Prime Video

### 4. **Family Star** (2024)
- **Genre**: Family/Romance
- **Cast**: Vijay Deverakonda, Mrunal Thakur
- **Director**: Parasuram
- **Rating**: ⭐ 6.8/10
- **Plot**: A family entertainer about relationships, responsibilities, and finding love.
- **Why Perfect**: Light-hearted, family-friendly, romantic elements
- **Streaming**: Amazon Prime Video

### 5. **Devara: Part 1** (2024)
- **Genre**: Action/Drama
- **Cast**: Jr. NTR, Janhvi Kapoor
- **Director**: Koratala Siva
- **Rating**: ⭐ 7.5/10
- **Plot**: A coastal warrior protects his village in this visually stunning epic.
- **Why Perfect**: Jr. NTR's powerful performance, great cinematography
- **Streaming**: Netflix

## 🎭 Why These Movies Are Perfect for Date Night:
- **Great Music**: Telugu cinema is known for melodious soundtracks
- **Visual Appeal**: High production values and stunning cinematography
- **Emotional Stories**: Perfect blend of romance, action, and family values
- **Star Power**: Top Telugu actors with great screen presence
- **Cultural Experience**: Authentic Telugu storytelling and traditions

## 🍿 Date Night Tips:
- **Subtitles**: All movies have English subtitles available
- **Snacks**: Prepare some South Indian snacks for authentic experience
- **Music**: Don't skip the songs - they're integral to Telugu cinema
- **Comfort**: These are longer movies (2.5-3 hours), so get comfortable!

## 📺 Where to Watch:
- **Netflix**: Kalki 2898 AD, Devara
- **Amazon Prime Video**: Pushpa 2, Kushi, Family Star
- **Disney+ Hotstar**: Regional Telugu content
- **Theaters**: For latest releases

Enjoy your Telugu movie night! 🎭✨
"""

def get_bollywood_movies():
    return """
# 🎬 Bollywood Movies for Date Night (2024-2025)

### 1. **Bade Miyan Chote Miyan** (2024)
- **Cast**: Akshay Kumar, Tiger Shroff
- **Genre**: Action/Comedy
- **Rating**: ⭐ 7.0/10
- **Streaming**: Netflix

### 2. **Khel Khel Mein** (2024)
- **Cast**: Akshay Kumar, Taapsee Pannu
- **Genre**: Comedy/Drama
- **Rating**: ⭐ 6.8/10
- **Streaming**: Amazon Prime Video

### 3. **Stree 2** (2024)
- **Cast**: Rajkummar Rao, Shraddha Kapoor
- **Genre**: Horror/Comedy
- **Rating**: ⭐ 7.5/10
- **Streaming**: Disney+ Hotstar

### 4. **Sarfira** (2024)
- **Cast**: Akshay Kumar, Radhika Madan
- **Genre**: Drama/Biography
- **Rating**: ⭐ 7.2/10
- **Streaming**: Disney+ Hotstar

### 5. **Munjya** (2024)
- **Genre**: Horror/Comedy
- **Rating**: ⭐ 6.9/10
- **Streaming**: Disney+ Hotstar
"""

def get_hollywood_movies():
    return """
# 🎬 Hollywood Movies for Date Night (2024-2025)

### 1. **Dune: Part Two** (2024)
- **Cast**: Timothée Chalamet, Zendaya
- **Genre**: Sci-Fi/Adventure
- **Rating**: ⭐ 8.6/10
- **Streaming**: HBO Max

### 2. **Inside Out 2** (2024)
- **Genre**: Animation/Family
- **Rating**: ⭐ 7.8/10
- **Streaming**: Disney+

### 3. **Bad Boys: Ride or Die** (2024)
- **Cast**: Will Smith, Martin Lawrence
- **Genre**: Action/Comedy
- **Rating**: ⭐ 6.8/10
- **Streaming**: Netflix

### 4. **Deadpool & Wolverine** (2024)
- **Cast**: Ryan Reynolds, Hugh Jackman
- **Genre**: Action/Comedy
- **Rating**: ⭐ 8.2/10
- **Streaming**: Disney+

### 5. **A Quiet Place: Day One** (2024)
- **Genre**: Horror/Thriller
- **Rating**: ⭐ 7.1/10
- **Streaming**: Paramount+
"""

if __name__ == "__main__":
    console.print("[bold green]Movie Recommendation Agent (Offline Mode)[/bold green]")
    console.print("Get movie recommendations from Bollywood, Tollywood & Hollywood!")
    console.print("Type 'exit' to quit\n")
    
    while True:
        query = Prompt.ask('What kind of movies are you looking for?')
        
        if query.lower() in ['exit', 'quit']:
            console.print("Happy watching!")
            sys.exit()
        
        query_lower = query.lower()
        
        if any(word in query_lower for word in ["tollywood", "telugu", "girlfriend", "date"]):
            console.print(Markdown(get_tollywood_movies()))
        elif any(word in query_lower for word in ["bollywood", "hindi"]):
            console.print(Markdown(get_bollywood_movies()))
        elif any(word in query_lower for word in ["hollywood", "english"]):
            console.print(Markdown(get_hollywood_movies()))
        else:
            console.print("[yellow]Try asking for:[/yellow]")
            console.print("- 'Telugu movies for girlfriend'")
            console.print("- 'Bollywood movies 2024'")
            console.print("- 'Hollywood movies for date night'")
        
        console.print("\n" + "="*50 + "\n")