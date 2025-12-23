import sys
from rich.prompt import Prompt
from rich.console import Console
from rich.markdown import Markdown

console = Console()

def create_europe_itinerary(days, budget, family_size, month):
    """Create a basic Europe travel itinerary with links"""
    
    daily_budget = budget / days
    per_person_daily = daily_budget / family_size
    
    # Suggest countries based on budget with links
    if per_person_daily > 100:
        countries = [
            "[Switzerland](https://www.myswitzerland.com/)",
            "[Norway](https://www.visitnorway.com/)", 
            "[Denmark](https://www.visitdenmark.com/)"
        ]
        tier = "Luxury"
    elif per_person_daily > 60:
        countries = [
            "[Germany](https://www.germany.travel/)",
            "[France](https://www.france.fr/en)", 
            "[Netherlands](https://www.holland.com/)",
            "[Austria](https://www.austria.info/)"
        ]
        tier = "Mid-range"
    else:
        countries = [
            "[Poland](https://www.poland.travel/)",
            "[Czech Republic](https://www.czechtourism.com/)", 
            "[Hungary](https://www.gotohungary.com/)",
            "[Portugal](https://www.visitportugal.com/)"
        ]
        tier = "Budget-friendly"
    
    weather_note = "Great weather for sightseeing!" if month.lower() in ["april", "may"] else "Check weather conditions"
    
    itinerary = f"""
# Europe Travel Itinerary - {days} Days

## Trip Overview
- **Family Size**: {family_size} people
- **Total Budget**: ${budget:,}
- **Duration**: {days} days
- **Daily Budget**: ${daily_budget:.2f} (${per_person_daily:.2f} per person)
- **Tier**: {tier}
- **Weather**: {weather_note}

## Recommended Countries
Based on your budget, consider these countries:
{chr(10).join([f"- {country}" for country in countries])}

## Sample 15-Day Itinerary

### Days 1-3: Capital City Exploration
- **Accommodation**: [Booking.com](https://www.booking.com/) or [Airbnb](https://www.airbnb.com/)
- **Activities**: 
  - City walking tours: [GetYourGuide](https://www.getyourguide.com/)
  - Museums: [Eurail Museum Pass](https://www.eurail.com/)
  - Local markets and food tours
- **Maps**: [Google Maps](https://maps.google.com/)
- **Budget**: ${daily_budget*3:.2f}

### Days 4-6: Cultural Sites
- **Activities**: 
  - Historical landmarks: [UNESCO World Heritage Sites](https://whc.unesco.org/)
  - Castles and palaces
  - Cultural experiences
- **Transportation**: [Eurail Pass](https://www.eurail.com/) or [FlixBus](https://www.flixbus.com/)
- **Budget**: ${daily_budget*3:.2f}

### Days 7-9: Nature & Relaxation
- **Activities**: 
  - National parks and nature reserves
  - Lakes and scenic areas
  - Family-friendly outdoor activities
- **Resources**: [AllTrails](https://www.alltrails.com/) for hiking
- **Budget**: ${daily_budget*3:.2f}

### Days 10-12: Local Experiences
- **Activities**: 
  - Local festivals and events: [Eventbrite](https://www.eventbrite.com/)
  - Food tours: [Viator](https://www.viator.com/)
  - Shopping districts
- **Budget**: ${daily_budget*3:.2f}

### Days 13-15: Final Destinations
- **Activities**: 
  - Last-minute sightseeing
  - Souvenir shopping
  - Relaxation before departure
- **Budget**: ${daily_budget*3:.2f}

## Budget Breakdown
| Category | Estimated Cost | Booking Links |
|----------|----------------|---------------|
| Accommodation (15 nights) | ${budget*0.4:.2f} | [Booking.com](https://www.booking.com/), [Hotels.com](https://www.hotels.com/) |
| Food & Dining | ${budget*0.3:.2f} | [TripAdvisor](https://www.tripadvisor.com/), [Yelp](https://www.yelp.com/) |
| Transportation | ${budget*0.2:.2f} | [Skyscanner](https://www.skyscanner.com/), [Eurail](https://www.eurail.com/) |
| Activities & Tours | ${budget*0.1:.2f} | [GetYourGuide](https://www.getyourguide.com/), [Viator](https://www.viator.com/) |

## Useful Travel Resources
- **Flight Booking**: [Skyscanner](https://www.skyscanner.com/), [Kayak](https://www.kayak.com/)
- **Train Travel**: [Eurail Pass](https://www.eurail.com/), [Trainline](https://www.trainline.com/)
- **City Guides**: [Lonely Planet](https://www.lonelyplanet.com/), [Rick Steves](https://www.ricksteves.com/)
- **Maps & Navigation**: [Google Maps](https://maps.google.com/), [Maps.me](https://maps.me/)
- **Translation**: [Google Translate](https://translate.google.com/), [Duolingo](https://www.duolingo.com/)
- **Weather**: [Weather.com](https://weather.com/), [AccuWeather](https://www.accuweather.com/)
- **Currency**: [XE Currency](https://www.xe.com/), [Revolut](https://www.revolut.com/)

## Planning Tips
- **Book early** for better prices on flights and accommodation
- **Consider rail passes** for multiple country travel
- **Pack layers** for April/May weather variations
- **Download offline maps** and translation apps
- **Check visa requirements** at [VisaHQ](https://www.visahq.com/)

## Family Travel Tips
- Look for family discounts at attractions
- Consider apartment rentals for longer stays
- Pack entertainment for travel days
- Research kid-friendly restaurants: [KidFriendly](https://kidfriendly.com/)
- Emergency contacts: [Travel.State.Gov](https://travel.state.gov/)

## Google Maps Links for Major Cities
- **Paris**: [Google Maps](https://goo.gl/maps/paris)
- **Rome**: [Google Maps](https://goo.gl/maps/rome)
- **Berlin**: [Google Maps](https://goo.gl/maps/berlin)
- **Amsterdam**: [Google Maps](https://goo.gl/maps/amsterdam)
- **Prague**: [Google Maps](https://goo.gl/maps/prague)

---
*This is a basic itinerary with helpful links. For detailed planning with real-time prices and bookings, use the provided resources.*
"""
    
    return itinerary

if __name__ == "__main__":
    console.print("[bold green]Simple Europe Travel Planner[/bold green]")
    console.print("This planner works without API keys!\n")
    
    while True:
        user_input = Prompt.ask('Enter your travel details (or "exit" to quit)')
        
        if user_input.lower() in ['exit', 'quit']:
            console.print("Happy travels!")
            sys.exit()
        
        # Simple parsing - you can enhance this
        if ("family of" in user_input.lower() and 
            ("$" in user_input or "budget" in user_input.lower()) and 
            "days" in user_input.lower() and 
            "europe" in user_input.lower()):
            
            # Extract family size
            import re
            family_match = re.search(r'family of (\d+)', user_input.lower())
            family_size = int(family_match.group(1)) if family_match else 4
            
            # Extract budget
            budget_match = re.search(r'\$?(\d+)', user_input)
            budget = int(budget_match.group(1)) if budget_match else 5000
            
            # Extract days
            days_match = re.search(r'(\d+)\s*days', user_input.lower())
            days = int(days_match.group(1)) if days_match else 15
            
            itinerary = create_europe_itinerary(days, budget, family_size, "April")
            console.print(Markdown(itinerary))
        else:
            console.print("[yellow]Please provide: family size, budget, duration, and destination[/yellow]")
            console.print("[dim]Example: 'family of 4, $5000 budget, 15 days in Europe'[/dim]")