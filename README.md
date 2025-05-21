A grab-bag of no-fluff utilities I use in day-to-day geotechnical and data-science work. Each one started life as a *“do this once, never again by hand”* hack; they’re now battle-tested and ready for whoever wants to save some time.

---
## Contents

- **notebooks/3DsurfaceGenerator.ipynb**  
  Builds an interactive 3-D surface (TIN or raster grid) from raw XYZ point clouds, adds slope shading, and exports to **PLY** + PNG for LiDAR/drone QA.  
  _Tech:_ `numpy`, `scipy.spatial`, `plotly`

- **notebooks/resistivitylog_xyz2csv.ipynb**  
  Converts AGI EarthImager XYZ inversion logs into a clean, depth-aligned CSV table and plots sanity-check resistivity sections.  
  _Tech:_ `pandas`, `matplotlib`

- **notebooks/Visualisation_SlopeSuperposition.ipynb**  
  Overlays sequential slope scans or FEM displacement outputs. Adds slider-driven transparency and Δ-elevation heatmaps.  
  _Tech:_ `plotly`, `ipywidgets`

- **notebooks/Visualisation_XML.ipynb**  
  Parses **LandXML** files and generates plan-, profile-, and section-view plots—no need for Civil 3D.  
  _Tech:_ `xml.etree`, `pandas`, `matplotlib`

- **notebooks/XML converter.ipynb**  
  Batch-converts LandXML alignments and surfaces into GIS-ready CSVs and Shapefiles.  
  _Tech:_ `geopandas`, `shapely`

- **scripts/XML to separate CSV.py**  
  Command-line script that splits each `<Profile>` from a LandXML into separate CSVs and PNG plots.  
  _Tech:_ `xml.etree`, `pandas`, `matplotlib`

- **scripts/ripDataFromChart.bas**  
  A VBA macro that extracts data series directly from Excel charts—perfect when the original data ranges are missing.  
  _Tech:_ VBA

---

## Quick-Start

```bash
# 1 – grab the repo
git clone https://github.com/zohuruzzaman/UsefulScript.git
cd UsefulScript

# 2 – spin up a fresh environment
python -m venv venv           # or conda create -n usefulscript python=3.11
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt

# 3 – launch notebooks
jupyter lab notebooks/

## Contributing
PRs welcome; open an issue first if you’re planning a big change. Stick to PEP-8, keep dependencies minimal, and include a one-liner in the table above.

## License
MIT—use it, break it, ship it, just don’t sue me.