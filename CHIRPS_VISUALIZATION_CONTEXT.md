# CHIRPS Precipitation Visualization - Project Context

## Project Overview
Analyzing and visualizing global precipitation data from CHIRPS v2.0 for years 2022-2024.
Location: Mumbai, India (Reference point)

---

## Critical Visualization Requirements

### 1. **Projection Requirements**
- ✅ **PRIMARY: Equal Earth Projection** (ccrs.EqualEarth())
  - Equal-area projection showing true continental sizes
  - Africa appears 14x larger than Greenland (accurate)
  - Better than Mollweide for this application
  - Used in all main comparison visualizations
  
- ❌ **AVOID**: 
  - Mercator projection (distorts area, especially poles)
  - Simple equirectangular without projection context

### 2. **Geographic Labels - MANDATORY**
- ✅ **Latitude/Longitude labels MUST be visible**
- ✅ **Proper coordinate notation:**
  - Longitude: "180°W", "90°W", "0°", "90°E", "180°E"
  - Latitude: "50°N", "25°N", "0°", "25°S", "50°S"
- ✅ **Gridlines must be shown** (draw_labels=True)
- ✅ **Coastlines and borders** for geographic context
- ❌ **NEVER use pixel coordinates (0, 500, 1000, etc.)**

### 3. **Colormap Requirements**
- ✅ **Primary: YlGnBu** (Yellow-Green-Blue)
  - Yellow = Dry/Low precipitation
  - Blue = Wet/High precipitation
  - Scientific standard for precipitation
  
- ✅ **Difference maps: RdBu_r** (Red-Blue reversed)
  - Red = Wetter than reference year
  - Blue = Drier than reference year

### 4. **Data Range/Scaling**
- ✅ **Precipitation maps:**
  - vmin=0, vmax=3000 (mm)
  
- ✅ **Difference maps:**
  - vmin=-500, vmax=500 (mm)

### 5. **Subsampling Strategy**
- ✅ **Use subsampling to speed up plotting**
  - Every 2nd pixel: `data[::2, ::2]`
  - Every 3rd pixel: `data[::3, ::3]`
  - Every 4th pixel: `data[::4, ::4]`
- ✅ **Apply same subsampling to coordinates**
  ```python
  data_sub = data[::2, ::2]
  lons_sub = lons[::2]
  lats_sub = lats[::2]
  LON, LAT = np.meshgrid(lons_sub, lats_sub)
  ```

### 6. **Transform Handling**
- ✅ **Data is in PlateCarree (lat/lon)**
- ✅ **Use `transform=ccrs.PlateCarree()`** when plotting on Equal Earth
- ✅ **Always add map features:**
  ```python
  ax.coastlines(linewidth=0.5, color='black', alpha=0.5)
  ax.add_feature(cfeature.BORDERS, linewidth=0.3, color='gray', alpha=0.3)
  ax.gridlines(linewidth=0.3, color='gray', alpha=0.3, draw_labels=True)
  ```

### 7. **Metadata & Annotations**
- ✅ **Always include:**
  - Title with year and metric
  - Mean precipitation value on maps
  - Data source (CHIRPS v2.0)
  - Resolution (0.05°)
  - Colormap scale label
  
- ✅ **Format:** Scientific and professional

### 8. **Output Quality**
- ✅ **DPI: 150 (minimum)**
- ✅ **File format: PNG**
- ✅ **Figure size: 20-22 x 8-10 inches** for multi-panel
- ✅ **Tight layout with bbox_inches='tight'**

---

## Python Code Template for Equal Earth + Lat/Lon

```python
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import numpy as np
import matplotlib.pyplot as plt

# Set up projection
projection = ccrs.EqualEarth()

# Create figure
fig, ax = plt.subplots(figsize=(16, 10), subplot_kw={'projection': projection}, dpi=150)

# Prepare data and coordinates
data_sub = data[::2, ::2]  # Subsample
lons_sub = lons[::2]
lats_sub = lats[::2]
LON, LAT = np.meshgrid(lons_sub, lats_sub)

# Plot with PlateCarree transform
im = ax.pcolormesh(LON, LAT, data_sub, cmap='YlGnBu', vmin=0, vmax=3000,
                   shading='auto', transform=ccrs.PlateCarree(), alpha=0.9)

# Add map features
ax.coastlines(linewidth=0.5, color='black', alpha=0.5)
ax.add_feature(cfeature.BORDERS, linewidth=0.3, color='gray', alpha=0.3)
ax.gridlines(linewidth=0.3, color='gray', alpha=0.3, draw_labels=True)

# Colorbar and labels
cbar = plt.colorbar(im, ax=ax, orientation='vertical', pad=0.02)
cbar.set_label('Annual Precipitation (mm)', fontsize=12, fontweight='bold')

ax.set_title('CHIRPS Precipitation\nEqual Earth Projection', fontsize=14, fontweight='bold')

plt.tight_layout()
plt.savefig('output.png', dpi=150, bbox_inches='tight', facecolor='white')
```

---

## Files Currently Generated

1. **chirps_2024_map.png** - Single year (equirectangular, has lat/lon labels)
2. **chirps_comparison_2022_2024_equalearth.png** - Equal Earth comparison (NEEDS LAT/LON LABELS)
3. **chirps_difference_maps_equalearth.png** - Equal Earth differences (NEEDS LAT/LON LABELS)
4. **chirps_trend_chart.png** - Bar chart with trend line

---

## Next Steps

- [ ] Fix lat/lon labels on Equal Earth projection maps
- [ ] Use `draw_labels=True` in gridlines() call
- [ ] Test with draw_labels parameter on all Equal Earth plots
- [ ] Verify coordinate labels display properly

---

## Important Notes

- **Data coordinates:** -180° to 180° (lon), 50°N to 50°S (lat)
- **Resolution:** 0.05° (approximately 5.5 km)
- **Shape:** 7200 x 2000 pixels
- **No-data value:** -9999 (masked in all visualizations)
- **Cartopy requirement:** Must have scipy and pykdtree for proper warping

---

**Last Updated:** 2026-08-04
**Created by:** Claude
**Project Owner:** Somdeep Kundu, Mumbai, India
