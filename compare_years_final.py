import rasterio
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import os
import warnings
warnings.filterwarnings('ignore')

print("=" * 70)
print("CHIRPS Precipitation Comparison: 2022, 2023, 2024")
print("Equal Earth Projection WITH Geographic Labels")
print("=" * 70)

# Load data
years = [2022, 2023, 2024]
print("\nLoading data...")
data = {}
for year in years:
    filename = f"chirps-v2.0.{year}.tif"
    if os.path.exists(filename):
        with rasterio.open(filename) as src:
            raw_data = src.read(1)
            data[year] = np.ma.masked_where(raw_data == -9999, raw_data)
            print(f"  ✓ Loaded {year}")

# Calculate statistics
print("\nCalculating statistics...")
stats = {}
for year, arr in data.items():
    stats[year] = {
        'mean': float(np.ma.mean(arr)),
        'median': float(np.ma.median(arr)),
        'min': float(np.ma.min(arr)),
        'max': float(np.ma.max(arr)),
        'std': float(np.ma.std(arr))
    }

# Print global statistics
print("\n" + "=" * 70)
print("GLOBAL PRECIPITATION STATISTICS (mm)")
print("=" * 70)
for year in sorted(stats.keys()):
    s = stats[year]
    print(f"\n{year}:")
    print(f"  Mean:   {s['mean']:>8.2f} mm")
    print(f"  Median: {s['median']:>8.2f} mm")

# Calculate year-over-year changes
print("\n" + "=" * 70)
print("YEAR-OVER-YEAR CHANGES")
print("=" * 70)
if 2022 in data and 2023 in data:
    change_22_23 = stats[2023]['mean'] - stats[2022]['mean']
    pct_22_23 = (change_22_23 / stats[2022]['mean']) * 100
    print(f"\n2022 → 2023: {change_22_23:+.2f} mm ({pct_22_23:+.2f}%)")

if 2023 in data and 2024 in data:
    change_23_24 = stats[2024]['mean'] - stats[2023]['mean']
    pct_23_24 = (change_23_24 / stats[2023]['mean']) * 100
    print(f"2023 → 2024: {change_23_24:+.2f} mm ({pct_23_24:+.2f}%)")

print("\n" + "=" * 70)

# Create comparison visualizations with Equal Earth Projection
print("\nCreating Equal Earth projection visualizations with lat/lon labels...")

# Set up projection
projection = ccrs.EqualEarth()

# Create figure with 3 subplots
fig = plt.figure(figsize=(24, 8), dpi=150)
gs = fig.add_gridspec(1, 3, width_ratios=[1, 1, 1], hspace=0.3, wspace=0.2)

# Coordinate arrays
lons = np.linspace(-180, 180, data[list(data.keys())[0]].shape[1])
lats = np.linspace(50, -50, data[list(data.keys())[0]].shape[0])

# Plot each year
for idx, year in enumerate(sorted(data.keys())):
    ax = fig.add_subplot(gs[idx], projection=projection)
    
    # Subsample for plotting
    data_sub = data[year][::2, ::2]
    lons_sub = lons[::2]
    lats_sub = lats[::2]
    
    LON, LAT = np.meshgrid(lons_sub, lats_sub)
    
    # Plot data with PlateCarree transform
    im = ax.pcolormesh(LON, LAT, data_sub, cmap='YlGnBu', vmin=0, vmax=3000, 
                       shading='auto', transform=ccrs.PlateCarree(), alpha=0.9)
    
    # Add map features
    ax.coastlines(linewidth=0.8, color='black', alpha=0.6)
    ax.add_feature(cfeature.BORDERS, linewidth=0.4, color='gray', alpha=0.4)
    
    # Add gridlines (without labels to avoid issues)
    ax.gridlines(linewidth=0.3, color='gray', alpha=0.3, draw_labels=False)
    
    # Add coordinate text annotations on the map
    # Longitude labels at top
    for lon in np.arange(-180, 181, 60):
        lon_label = f'{int(-lon)}°W' if lon < 0 else (f'{int(lon)}°E' if lon > 0 else '0°')
        ax.text(lon, 48, lon_label, transform=ccrs.PlateCarree(), 
               fontsize=9, ha='center', fontweight='bold',
               bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.7, edgecolor='none'))
    
    # Latitude labels on left
    for lat in np.arange(-50, 51, 25):
        lat_label = f'{int(-lat)}°S' if lat < 0 else (f'{int(lat)}°N' if lat > 0 else '0°')
        ax.text(-175, lat, lat_label, transform=ccrs.PlateCarree(), 
               fontsize=9, ha='right', va='center', fontweight='bold',
               bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.7, edgecolor='none'))
    
    # Set title with year and mean
    ax.set_title(f'{year}\nMean: {stats[year]["mean"]:.0f} mm', 
                fontsize=14, fontweight='bold', pad=15)

# Add single colorbar
cbar_ax = fig.add_axes([0.92, 0.2, 0.012, 0.6])
cbar = fig.colorbar(im, cax=cbar_ax, orientation='vertical')
cbar.set_label('Annual Precipitation (mm)', fontsize=12, fontweight='bold')

# Main title
fig.suptitle('CHIRPS Annual Precipitation Comparison: 2022 - 2024\nEqual Earth Projection', 
             fontsize=18, fontweight='bold', y=0.98)

plt.savefig('chirps_comparison_2022_2024_equalearth.png', dpi=150, bbox_inches='tight', facecolor='white')
print("  ✓ Saved: chirps_comparison_2022_2024_equalearth.png")
plt.close()

# Create difference maps with Equal Earth Projection
if len(data) >= 2:
    print("Creating difference maps with Equal Earth projection and labels...")
    fig = plt.figure(figsize=(20, 8), dpi=150)
    gs = fig.add_gridspec(1, 2, width_ratios=[1, 1], hspace=0.3, wspace=0.2)
    
    plot_idx = 0
    im_for_cbar = None
    
    if 2022 in data and 2023 in data:
        ax = fig.add_subplot(gs[plot_idx], projection=projection)
        plot_idx += 1
        
        diff_22_23 = data[2023][::2, ::2] - data[2022][::2, ::2]
        LON, LAT = np.meshgrid(lons[::2], lats[::2])
        
        im1 = ax.pcolormesh(LON, LAT, diff_22_23, cmap='RdBu_r', 
                            vmin=-500, vmax=500, shading='auto', 
                            transform=ccrs.PlateCarree(), alpha=0.9)
        im_for_cbar = im1
        
        ax.coastlines(linewidth=0.8, color='black', alpha=0.6)
        ax.add_feature(cfeature.BORDERS, linewidth=0.4, color='gray', alpha=0.4)
        ax.gridlines(linewidth=0.3, color='gray', alpha=0.3, draw_labels=False)
        
        # Add labels
        for lon in np.arange(-180, 181, 60):
            lon_label = f'{int(-lon)}°W' if lon < 0 else (f'{int(lon)}°E' if lon > 0 else '0°')
            ax.text(lon, 48, lon_label, transform=ccrs.PlateCarree(), 
                   fontsize=9, ha='center', fontweight='bold',
                   bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.7, edgecolor='none'))
        
        for lat in np.arange(-50, 51, 25):
            lat_label = f'{int(-lat)}°S' if lat < 0 else (f'{int(lat)}°N' if lat > 0 else '0°')
            ax.text(-175, lat, lat_label, transform=ccrs.PlateCarree(), 
                   fontsize=9, ha='right', va='center', fontweight='bold',
                   bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.7, edgecolor='none'))
        
        ax.set_title('2023 - 2022 (Difference in mm)', fontsize=13, fontweight='bold', pad=10)
    
    if 2023 in data and 2024 in data:
        ax = fig.add_subplot(gs[plot_idx], projection=projection)
        
        diff_23_24 = data[2024][::2, ::2] - data[2023][::2, ::2]
        LON, LAT = np.meshgrid(lons[::2], lats[::2])
        
        im2 = ax.pcolormesh(LON, LAT, diff_23_24, cmap='RdBu_r', 
                            vmin=-500, vmax=500, shading='auto', 
                            transform=ccrs.PlateCarree(), alpha=0.9)
        im_for_cbar = im2
        
        ax.coastlines(linewidth=0.8, color='black', alpha=0.6)
        ax.add_feature(cfeature.BORDERS, linewidth=0.4, color='gray', alpha=0.4)
        ax.gridlines(linewidth=0.3, color='gray', alpha=0.3, draw_labels=False)
        
        # Add labels
        for lon in np.arange(-180, 181, 60):
            lon_label = f'{int(-lon)}°W' if lon < 0 else (f'{int(lon)}°E' if lon > 0 else '0°')
            ax.text(lon, 48, lon_label, transform=ccrs.PlateCarree(), 
                   fontsize=9, ha='center', fontweight='bold',
                   bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.7, edgecolor='none'))
        
        for lat in np.arange(-50, 51, 25):
            lat_label = f'{int(-lat)}°S' if lat < 0 else (f'{int(lat)}°N' if lat > 0 else '0°')
            ax.text(-175, lat, lat_label, transform=ccrs.PlateCarree(), 
                   fontsize=9, ha='right', va='center', fontweight='bold',
                   bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.7, edgecolor='none'))
        
        ax.set_title('2024 - 2023 (Difference in mm)', fontsize=13, fontweight='bold', pad=10)
    
    # Add colorbar
    if im_for_cbar is not None:
        cbar_ax = fig.add_axes([0.92, 0.2, 0.012, 0.6])
        cbar = fig.colorbar(im_for_cbar, cax=cbar_ax, orientation='vertical')
        cbar.set_label('Difference in Precipitation (mm)', fontsize=12, fontweight='bold')
    
    fig.suptitle('Precipitation Difference Maps\nEqual Earth Projection', 
                fontsize=18, fontweight='bold', y=0.98)
    
    plt.savefig('chirps_difference_maps_equalearth.png', dpi=150, bbox_inches='tight', facecolor='white')
    print("  ✓ Saved: chirps_difference_maps_equalearth.png")
    plt.close()

# Create bar chart
print("Creating summary chart...")
fig, ax = plt.subplots(figsize=(11, 7), dpi=150)

years_list = sorted(stats.keys())
means = [stats[year]['mean'] for year in years_list]
colors = ['#FFD700', '#90EE90', '#4169E1']

bars = ax.bar(years_list, means, color=colors, edgecolor='black', linewidth=2.5, alpha=0.85, width=0.6)

# Add value labels on bars
for bar, mean in zip(bars, means):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height,
            f'{mean:.0f} mm',
            ha='center', va='bottom', fontsize=14, fontweight='bold')

# Add trend line
if len(years_list) > 1:
    z = np.polyfit(years_list, means, 1)
    p = np.poly1d(z)
    ax.plot(years_list, p(years_list), "r--", linewidth=2, alpha=0.7, label='Trend')
    ax.legend(fontsize=11)

ax.set_ylabel('Mean Annual Precipitation (mm)', fontsize=13, fontweight='bold')
ax.set_xlabel('Year', fontsize=13, fontweight='bold')
ax.set_title('Global Mean Annual Precipitation Trend (2022-2024)', fontsize=15, fontweight='bold', pad=20)
ax.grid(True, alpha=0.3, axis='y', linestyle='--')
ax.set_ylim(0, max(means) * 1.2)
ax.set_xticks(years_list)

plt.tight_layout()
plt.savefig('chirps_trend_chart.png', dpi=150, bbox_inches='tight', facecolor='white')
print("  ✓ Saved: chirps_trend_chart.png")
plt.close()

print("\n" + "=" * 70)
print("✅ ANALYSIS COMPLETE!")
print("=" * 70)
print("\nGenerated files:")
print("  1. chirps_comparison_2022_2024_equalearth.png")
print("     → Equal Earth projection with lat/lon labels")
print("  2. chirps_difference_maps_equalearth.png")
print("     → Precipitation changes with lat/lon labels")
print("  3. chirps_trend_chart.png")
print("     → Mean precipitation trend chart")
print("\n" + "=" * 70)
