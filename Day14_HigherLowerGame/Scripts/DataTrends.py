from pytrends.request import TrendReq
import random
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)

data_trends = [
    "Cryptocurrency", "NFTs", "Metaverse", "Remote work", "Sustainable living", "Climate change",
    "Mental health awareness", "Veganism", "Plant-based diets", "Home workouts", "Meditation",
    "Mindfulness", "Self-care", "Digital nomad lifestyle", "Cybersecurity", "Artificial intelligence",
    "Machine learning", "Data privacy", "Electric vehicles", "Renewable energy", "Green energy",
    "Space exploration", "Mars colonization", "Virtual reality", "Augmented reality",
    "Blockchain technology", "DeFi (Decentralized Finance)", "Web3", "Remote learning",
    "Online courses", "E-learning", "DIY projects", "Gardening", "Indoor plants", "Minimalism",
    "Zero waste living", "Tiny houses", "Sustainable fashion", "Ethical shopping", "Secondhand clothing",
    "Thrifting", "Local travel", "Staycations", "Road trips", "Adventure travel", "Solo travel",
    "Digital art", "Crypto art", "NFTs art", "Streetwear", "Sneaker culture", "Gaming", "Esports",
    "Twitch streaming", "Mobile gaming", "Console gaming", "Retro gaming", "Board games", "Cooking",
    "Baking", "Food photography", "Food blogging", "Plant-based recipes", "Sustainable cooking",
    "Fitness challenges", "Yoga", "Pilates", "HIIT", "Bodyweight workouts", "CrossFit", "Cycling",
    "Running", "Hiking", "Kayaking", "Surfing", "Skiing", "Snowboarding", "Skateboarding",
    "Photography", "Nature photography", "Portrait photography", "Landscape photography",
    "Street photography", "Astrophotography", "Fashion photography", "Wildlife photography",
    "Travel photography", "Drone photography", "Mobile photography", "Interior design",
    "Home renovation", "DIY home decor", "Feng shui", "Scandinavian design", "Bohemian decor",
    "Mid-century modern", "Industrial design", "Minimalist design", "Sustainable architecture",
    "Urban gardening", "Healthy eating", "Zero-waste lifestyle", "Remote jobs", "Minimalist lifestyle", "Eco-friendly products",
    "Green living", "Outdoor activities", "Eco-travel", "Sustainable tourism", "Eco-conscious fashion",
    "Mindful living", "Digital detox", "Self-improvement", "Personal development", "Sustainable transportation",
    "Renewable energy sources", "Clean energy", "Eco-friendly home", "Recycling", "Upcycling",
    "Circular economy", "Eco-conscious consumerism", "Sustainable beauty", "Clean beauty", "Natural skincare",
    "Eco-friendly packaging", "Minimalist wardrobe", "Capsule wardrobe", "Ethical fashion", "Fair trade",
    "Slow fashion", "Sustainable textiles", "Eco-friendly materials", "Organic farming", "Community gardening",
    "Permaculture", "Eco-friendly living", "Zero-waste kitchen", "Composting", "Eco-friendly cleaning products",
    "Sustainable architecture", "Passive solar design", "Green building", "Renewable energy systems",
    "Energy-efficient homes", "Sustainable cities", "Green spaces", "Urban farming", "Community-supported agriculture (CSA)",
    "Local food", "Farmers markets", "Sustainable seafood", "Ocean conservation", "Marine biodiversity",
    "Coral reef protection", "Wildlife conservation", "Endangered species protection", "Animal welfare",
    "Environmental activism", "Climate action", "Sustainable development goals (SDGs)", "Circular fashion",
    "Sustainable accessories", "Eco-friendly jewelry", "Ethical diamonds", "Green weddings", "Sustainable event planning",
    "Eco-conscious travel", "Responsible tourism", "Sustainable accommodations", "Eco-friendly transportation",
    "Carbon offsetting", "Ecotourism", "Sustainable food systems", "Regenerative agriculture", "Food forests",
    "Green technology", "Clean technology", "Renewable energy innovations", "Sustainable innovations",
    "Environmental education", "Conservation education", "Green careers", "Environmental sustainability",
    "Eco-friendly businesses", "Corporate sustainability", "Sustainable finance", "Impact investing",
    "Socially responsible investing", "Green bonds", "Climate finance", "Carbon trading", "Eco-tourism"
]

def return_random_index():
    index = random.randint(0, len(data_trends))
    topic_name = data_trends[index]
    topic_score = return_score_from_index(index)
    return topic_name, topic_score

def return_score_from_index(index):
    index = min(index, len(data_trends))
    topic_name = data_trends[index]
    pytrends = TrendReq(hl='en-US', tz=360)
    pytrends.build_payload([topic_name], cat=0, timeframe='today 5-y', geo='', gprop='')
    interest_over_time_df = pytrends.interest_over_time()
    return interest_over_time_df[topic_name].sum()