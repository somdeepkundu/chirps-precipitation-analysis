# Contributing to CHIRPS Precipitation Analysis

Thank you for your interest in contributing! This guide will help you get started.

## 🎯 How to Contribute

### Reporting Issues
Found a bug? Have a suggestion? Please [open an issue](https://github.com/yourusername/chirps-precipitation-analysis/issues) with:
- Clear description of the problem
- Steps to reproduce (if applicable)
- Python version and OS
- Error messages or screenshots

### Improving Documentation
- Fix typos or unclear explanations
- Add examples or use cases
- Improve README or docstrings
- Translate to other languages

### Adding Features
Suggested improvements:
- [ ] **Jupyter Notebook versions** of each script
- [ ] **Interactive Streamlit dashboard** for exploration
- [ ] **Regional analysis scripts** (India, Africa, Americas)
- [ ] **Precipitation anomaly** (deviation from historical mean)
- [ ] **Drought/flood detection** algorithms
- [ ] **Time series analysis** (seasonality, trends)
- [ ] **Machine learning models** for precipitation forecasting
- [ ] **Google Colab notebooks** for cloud computing
- [ ] **Xarray integration** for easier multidimensional data handling
- [ ] **Unit tests** and validation scripts

### Code Improvements
- Performance optimizations
- Better error handling
- Code simplification
- Security improvements

## 🔧 Development Setup

### 1. Fork and Clone
```bash
# Fork on GitHub, then clone your fork
git clone https://github.com/yourusername/chirps-precipitation-analysis.git
cd chirps-precipitation-analysis
```

### 2. Create a Branch
```bash
# Create feature branch
git checkout -b feature/your-feature-name
# or bug fix branch
git checkout -b bugfix/issue-description
```

### 3. Install Development Dependencies
```bash
# Install all dependencies
uv sync

# Activate virtual environment
source .venv/bin/activate  # Linux/macOS
# or on Windows:
.venv\Scripts\activate
```

### 4. Make Your Changes
- Keep commits small and focused
- Write clear commit messages
- Test your code thoroughly
- Update documentation

### 5. Commit and Push
```bash
# Stage changes
git add .

# Commit with descriptive message
git commit -m "Add feature: description of what was added"

# Push to your fork
git push origin feature/your-feature-name
```

### 6. Create Pull Request
- Go to GitHub
- Create PR from your branch to `main`
- Fill in the PR template
- Link related issues
- Wait for review

## 📝 Commit Message Guidelines

Use clear, descriptive commit messages:

```
# Good
git commit -m "Add India regional precipitation analysis script"
git commit -m "Fix: Handle no-data values in difference maps"
git commit -m "Docs: Improve COG explanation in README"

# Avoid
git commit -m "fixed stuff"
git commit -m "update"
git commit -m "asdf"
```

**Format:**
```
[Type]: Brief description (50 chars max)

Longer explanation if needed (wrap at 72 chars).
Explain WHY, not just WHAT.

Fixes #123
Relates to #456
```

**Types:**
- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation only
- `refactor:` Code refactoring
- `perf:` Performance improvement
- `test:` Adding tests
- `chore:` Maintenance tasks

## 🎨 Code Style

### Python Style Guide
We follow PEP 8:

```python
# Good
def calculate_precipitation_statistics(data):
    """Calculate mean, median, std of precipitation data."""
    mean_precip = np.ma.mean(data)
    median_precip = np.ma.median(data)
    std_precip = np.ma.std(data)
    return mean_precip, median_precip, std_precip

# Avoid
def calc_prcp(d):
    m=np.ma.mean(d);md=np.ma.median(d);s=np.ma.std(d)
    return m,md,s
```

### Naming Conventions
```python
# Variables
precipitation_data  # not precip_d or p
year_range = [2022, 2023, 2024]  # not years or yr

# Functions
def load_chirps_data(filepath):  # not load_data() or loadData()
    pass

# Classes
class PrecipitationAnalyzer:  # not Analyzer or ANALYZER
    pass

# Constants
MAX_PRECIPITATION = 10000  # not max_p or maxPrecip
```

### Docstrings
```python
def create_equal_earth_map(data, title="Precipitation Map"):
    """
    Create a precipitation map using Equal Earth projection.
    
    Parameters
    ----------
    data : numpy.ndarray
        2D array of precipitation values (mm)
    title : str, optional
        Map title (default: "Precipitation Map")
    
    Returns
    -------
    matplotlib.figure.Figure
        The created figure object
    
    Example
    -------
    >>> data = load_data('chirps-v2.0.2024.tif')
    >>> fig = create_equal_earth_map(data, title="2024 Precipitation")
    """
    pass
```

## 🧪 Testing

Before submitting, test your changes:

```bash
# Run your script
uv run python 05_compare_years.py

# Check for errors
python -m py_compile your_script.py

# Validate GeoTIFF output (if applicable)
uv run rio cogeo validate output.tif
```

## 📚 Documentation Updates

When adding features, please update:
1. **README.md** - Add to overview
2. **Script docstrings** - Document parameters and outputs
3. **CHIRPS_VISUALIZATION_CONTEXT.md** - Add any new requirements
4. **Examples** - Include usage examples

## 🚀 Performance Considerations

When writing geospatial code:
- ✅ Use subsampling for visualization: `data[::2, ::2]`
- ✅ Avoid loading full resolution data unnecessarily
- ✅ Use masked arrays for no-data values
- ✅ Comment on performance-critical sections
- ❌ Don't loop over pixels (use NumPy vectorization)
- ❌ Avoid converting between formats unnecessarily

## 🔍 Review Process

Your PR will be reviewed for:
1. **Functionality** - Does it work as intended?
2. **Code quality** - Is it clean and maintainable?
3. **Documentation** - Is it well documented?
4. **Tests** - Does it handle edge cases?
5. **Performance** - Is it efficient?

Reviewers may request changes. That's normal! We're here to help.

## 📋 PR Checklist

Before submitting, ensure:
- [ ] Code follows style guide (PEP 8)
- [ ] Docstrings are complete
- [ ] Changes tested locally
- [ ] README updated (if needed)
- [ ] No large files committed (only code)
- [ ] No credentials or API keys in code
- [ ] Commit messages are descriptive
- [ ] No merge conflicts

## 🎓 Learning Resources

New to geospatial data?
- [Rasterio Documentation](https://rasterio.readthedocs.io/)
- [Cartopy Tutorial](https://scitools.org.uk/cartopy/docs/latest/tutorials.html)
- [GIS with Python Course](https://www.datacamp.com/courses/spatial-data-science-with-geopandas)
- [Cloud-Optimized GeoTIFF](https://www.cogeo.org/)

## 💬 Questions?

- Check existing issues
- Ask in PR comments
- Start a discussion
- Email maintainers

## 🙏 Thank You!

Your contributions make this project better for everyone. Thank you for helping! 🌍

---

## Code of Conduct

Please be respectful and inclusive. We're a community dedicated to learning and climate science.

**Expected behavior:**
- ✅ Be respectful of differing opinions
- ✅ Welcome newcomers
- ✅ Focus on the code, not the person
- ✅ Help others learn

**Unacceptable behavior:**
- ❌ Harassment or discrimination
- ❌ Disrespectful comments
- ❌ Spam or self-promotion
- ❌ Off-topic discussions

Report issues to project maintainers.

---

Happy contributing! 🚀
