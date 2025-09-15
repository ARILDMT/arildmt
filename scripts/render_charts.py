import json
from pathlib import Path
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

# Set up paths
root = Path(__file__).resolve().parents[1]
data_file = root / "data" / "school21.json"
assets_dir = root / "assets"
assets_dir.mkdir(exist_ok=True, parents=True)

# Load data
try:
    with open(data_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
except FileNotFoundError:
    print(f"Data file not found: {data_file}")
    exit(1)

# Set style for better looking charts
plt.style.use('dark_background')

# XP Progress Chart
if "xp_over_time" in data:
    months = [entry[0] for entry in data["xp_over_time"]]
    xp_values = [entry[1] for entry in data["xp_over_time"]]
    
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(months, xp_values, marker='o', linewidth=3, markersize=8, 
            color='#00ff88', markerfacecolor='#00cc66')
    ax.fill_between(months, xp_values, alpha=0.3, color='#00ff88')
    
    ax.set_title('School 21 XP Progress', fontsize=16, fontweight='bold', color='white')
    ax.set_xlabel('Month', fontsize=12, color='white')
    ax.set_ylabel('XP Points', fontsize=12, color='white')
    ax.grid(True, alpha=0.3)
    
    # Styling
    ax.tick_params(colors='white')
    ax.spines['bottom'].set_color('white')
    ax.spines['top'].set_color('white')
    ax.spines['right'].set_color('white')
    ax.spines['left'].set_color('white')
    
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(assets_dir / "xp_graph.png", dpi=300, bbox_inches='tight', 
                facecolor='#0d1117', edgecolor='none')
    plt.close()
    print("✓ XP graph generated")

# Skills Chart
if "skills" in data:
    skills = list(data["skills"].keys())
    scores = list(data["skills"].values())
    
    # Create color gradient
    colors = ['#ff6b6b', '#4ecdc4', '#45b7d1', '#96ceb4', '#feca57', '#ff9ff3']
    
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(skills, scores, color=colors[:len(skills)], alpha=0.8, edgecolor='white', linewidth=2)
    
    # Add value labels on bars
    for bar, score in zip(bars, scores):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 0.5,
                f'{score}%', ha='center', va='bottom', fontweight='bold', color='white')
    
    ax.set_title('School 21 Skills Progress', fontsize=16, fontweight='bold', color='white')
    ax.set_xlabel('Skills', fontsize=12, color='white')
    ax.set_ylabel('Progress (%)', fontsize=12, color='white')
    ax.set_ylim(0, max(scores) + 10)
    ax.grid(True, alpha=0.3, axis='y')
    
    # Styling
    ax.tick_params(colors='white')
    ax.spines['bottom'].set_color('white')
    ax.spines['top'].set_color('white')
    ax.spines['right'].set_color('white')
    ax.spines['left'].set_color('white')
    
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(assets_dir / "skills_chart.png", dpi=300, bbox_inches='tight',
                facecolor='#0d1117', edgecolor='none')
    plt.close()
    print("✓ Skills chart generated")

print("All charts generated successfully!")
