# Differential Geometry of Plane Curves

Interactive notes on the differential geometry of plane curves with beautiful Plotly visualizations.

## Features

- **Interactive Figures**: Dynamic Plotly visualizations showing tangent and acceleration vectors
- **Dark Theme**: Elegant, professional design optimized for mathematical content
- **Comprehensive Examples**: Circle, ellipse, parabola, semicubical parabola (cusp), and cycloid
- **Mathematical Rigor**: Proper definitions, formulas, and geometric interpretations
- **Responsive Design**: Works on desktop and mobile devices

## Mathematical Topics Covered

1. **Introduction to Plane Curves**
   - Parametric representation
   - Smoothness and regularity conditions
   - Basic properties and examples

2. **Curve Examples**
   - Circle: $p(t) = (R\cos t, R\sin t)$
   - Ellipse: $p(t) = (a\cos t, b\sin t)$
   - Parabola: $p(t) = (t, t^2)$
   - Semicubical Parabola: $p(t) = (t^2, t^3)$ (non-regular)
   - Cycloid: $p(t) = R(t - \sin t, 1 - \cos t)$

3. **Key Concepts**
   - Tangent vectors and velocity
   - Acceleration vectors
   - Regularity condition and its importance
   - Cusps and singularities

## How to Use

### View the Notes
Simply open `differential-geometry-notes.html` in your web browser. All figures are embedded and will load automatically.

### Generate New Figures
If you want to modify or regenerate the figures:

1. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the figure generation script:
   ```bash
   python generate_figures.py
   ```

3. The script will create/update all figures in the `figures/` directory

### Customize the Content
- Edit `differential-geometry-notes.html` to modify the mathematical content
- Modify `generate_figures.py` to change figure parameters, colors, or add new curves
- The figures use Plotly, so they're fully interactive (zoom, pan, hover)

## Technical Details

- **Frontend**: HTML5, CSS3 (Bulma framework), MathJax for mathematical notation
- **Visualizations**: Plotly.js for interactive figures
- **Backend**: Python with Plotly and NumPy for figure generation
- **Styling**: Custom dark theme with professional mathematical typography

## File Structure

```
geometry-notes/
├── differential-geometry-notes.html  # Main notes page
├── generate_figures.py               # Python script for figures
├── differential-geometry-plan.md     # Project planning document
├── requirements.txt                  # Python dependencies
├── README.md                         # This file
└── figures/                          # Generated Plotly figures
    ├── circle.html
    ├── ellipse.html
    ├── parabola.html
    ├── cusp.html
    ├── cycloid.html
    └── combined.html
```

## Mathematical Notation

- $p(t)$ - position vector of the curve
- $p'(t)$ - velocity vector (tangent vector)
- $p''(t)$ - acceleration vector
- $\mathbf{T}(t)$ - unit tangent vector
- $\mathbf{N}(t)$ - unit normal vector
- $\kappa$ - curvature

## Contributing

Feel free to:
- Add new curve examples
- Improve the mathematical explanations
- Enhance the visualizations
- Fix any issues or typos

## License

This project is open source and available under the MIT License.
