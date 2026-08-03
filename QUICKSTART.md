# Quick Start Guide

Get started in 5 minutes! 🚀

## Installation (2 minutes)

### 1. Prerequisites
- Python 3.10+ (check: `python --version`)
- 5 GB free disk space
- Internet connection

### 2. Clone Repository
```bash
git clone https://github.com/yourusername/chirps-precipitation-analysis.git
cd chirps-precipitation-analysis
```

### 3. Install Dependencies
```bash
# Install UV package manager (if not already installed)
pip install uv

# Install project dependencies
uv sync
```

That's it! ✅

---

## Run Your First Script (3 minutes)

### Option A: Quick Visualization (Recommended for first-time users)
```bash
# Download data and create a single-year map
uv run python 04_visualize_single_year.py
```

**Output:** `chirps_2024_map.png` - A beautiful global precipitation map!

### Option B: Full Analysis
```bash
# Download data, validate, convert to COG, and create comparison maps
uv run python 05_compare_years.py
```

**Output:** 
- `chirps_comparison_2022_2024_equalearth.png` - 3-year comparison
- `chirps_difference_maps_equalearth.png` - What changed?
- `chirps_trend_chart.png` - Trend visualization

---

## Understanding the Output

### The Maps
- **Blue areas** = High precipitation (wet)
- **Yellow areas** = Low precipitation (dry)
- **White areas** = Coast/no data

### The Statistics
```
2022: Mean precipitation = 898 mm
2023: Mean precipitation = 854 mm (4.9% decrease)
2024: Mean precipitation = 887 mm (3.9% increase)
```

### The Files Created
```
data/
  chirps-v2.0.2024.tif        ← Downloaded data
  chirps-v2.0.2024_cog.tif    ← Cloud-optimized version

output/
  chirps_2024_map.png         ← Your visualizations
  chirps_comparison*.png
  chirps_difference*.png
  chirps_trend_chart.png
```

---

## Exploring Data

### Check What the Data Contains
```bash
uv run python 03_explore_data.py
```

Output:
```
Data shape: 7200 x 2000 pixels
Coverage: Global (-180° to 180°, -50° to 50°)
Resolution: 0.05° (~5.5 km)
Mean precipitation: 898 mm
Range: 0 - 9825 mm
```

### View Cloud-Optimization
```bash
uv run python 02_convert_to_cog.py
```

Confirms your data is optimized for cloud storage ☁️

---

## Customization

### Change Years to Compare
Edit `05_compare_years.py`:
```python
years = [2020, 2021, 2022]  # Change this line
```

### Extract Your Region (e.g., India)
```bash
uv run python 06_extract_region.py
```

### Modify Colors
In any script, change the colormap:
```python
# Line with: cmap='YlGnBu'
# Change to: cmap='viridis'  # or 'plasma', 'RdYlGn', etc.
```

---

## Troubleshooting

### "Module not found" error
```bash
# Make sure you're in the right directory
pwd  # Linux/macOS
cd   # Windows

# Reinstall dependencies
uv sync
```

### "Out of memory" error
Data is large (~300 MB per file). Use subsampling:
```python
# In scripts, change:
data_sub = data[::2, ::2]  # To: data[::4, ::4]
```

### Maps look weird
Check that you have 5GB free space:
```bash
df -h  # Linux/macOS
dir C:\  # Windows - check available space
```

### "urllib3" or other import errors
```bash
uv sync --refresh
```

---

## Next Steps

1. ✅ Run Step 4 (single year visualization)
2. ✅ Look at the output maps
3. ✅ Run Step 5 (comparison)
4. ✅ Try Step 6 (regional analysis)
5. ✅ Modify scripts for your own data!

---

## What Can I Do With This?

### Research
- Publish climate analysis papers
- Study precipitation patterns
- Analyze drought/flood events
- Climate change impacts

### Education
- Teach geospatial analysis
- Climate science curriculum
- Environmental courses
- Data visualization training

### Applications
- Build climate dashboards
- Agricultural forecasting
- Water resource management
- Disaster risk assessment

### And more!

---

## Key Concepts (In Simple Terms)

**GeoTIFF**
- Image format for geographic data
- Stores latitude/longitude with pixel values
- Like a photo, but with coordinates

**Cloud-Optimized GeoTIFF (COG)**
- Regular GeoTIFF, but organized for cloud storage
- Faster to read from cloud services
- Like a book with good bookmarks!

**Equal Earth Projection**
- Shows Earth accurately (areas preserved)
- Better than flat maps
- Africa is actually big!

**Precipitation**
- Rainfall + snowfall (in mm per year)
- CHIRPS measures this globally
- Used to track droughts and floods

---

## Useful Links

- 📊 **Data**: https://www.chc.ucsb.edu/data/chirps
- 🗺️ **Maps**: https://chc.ucsb.edu/ACE/CHIRTSimg/
- 📚 **Learning**: https://rasterio.readthedocs.io/
- 🌍 **Projections**: https://scitools.org.uk/cartopy/

---

## Still Need Help?

1. Check [README.md](README.md) for full documentation
2. Read [CHIRPS_VISUALIZATION_CONTEXT.md](CHIRPS_VISUALIZATION_CONTEXT.md) for details
3. Browse [existing issues](https://github.com/yourusername/chirps-precipitation-analysis/issues)
4. [Open a new issue](https://github.com/yourusername/chirps-precipitation-analysis/issues/new)

---

## You're All Set! 🎉

Now you have:
- ✅ Working Python geospatial environment
- ✅ Real climate data
- ✅ Professional visualization tools
- ✅ Framework for your own analysis

Go create something amazing! 🌍🚀

---

**Happy learning!**

---

*Estimated time: 5-10 minutes* ⏱️  
*Data download time: 5-15 minutes* (depends on internet speed)
