import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import os

# Create figures directory
os.makedirs('figures', exist_ok=True)

# Set dark theme for consistency with HTML
dark_template = {
    'layout': {
        'paper_bgcolor': '#1a1a1a',
        'plot_bgcolor': '#1a1a1a',
        'font': {'color': '#ffffff'},
        'xaxis': {
            'gridcolor': '#4a5568',
            'linecolor': '#ffffff',
            'tickcolor': '#ffffff'
        },
        'yaxis': {
            'gridcolor': '#4a5568',
            'linecolor': '#ffffff',
            'tickcolor': '#ffffff'
        }
    }
}

# 1. Circle
t_circle = np.linspace(0, 2*np.pi, 100)
R = 2
x_circle = R * np.cos(t_circle)
y_circle = R * np.sin(t_circle)

fig_circle = go.Figure()
fig_circle.add_trace(go.Scatter(
    x=x_circle, y=y_circle,
    mode='lines',
    name='Circle',
    line=dict(color='#63b3ed', width=3)
))

# Add some tangent vectors
t_tangents = np.linspace(0, 2*np.pi, 16, endpoint=False)
for t in t_tangents:
    x_point = R * np.cos(t)
    y_point = R * np.sin(t)
    dx = -R * np.sin(t)
    dy = R * np.cos(t)
    
    fig_circle.add_trace(go.Scatter(
        x=[x_point, x_point + 0.5*dx], 
        y=[y_point, y_point + 0.5*dy],
        mode='lines+markers',
        line=dict(color='#68d391', width=2),
        marker=dict(size=4),
        showlegend=False
    ))

# Add acceleration vectors
for t in t_tangents:
    x_point = R * np.cos(t)
    y_point = R * np.sin(t)
    ddx = -R * np.cos(t)
    ddy = -R * np.sin(t)
    
    fig_circle.add_trace(go.Scatter(
        x=[x_point, x_point + 0.3*ddx], 
        y=[y_point, y_point + 0.3*ddy],
        mode='lines+markers',
        line=dict(color='#f6e05e', width=2),
        marker=dict(size=4),
        showlegend=False
    ))

fig_circle.update_layout(
    title='Circle: p(t) = (R cos t, R sin t)',
    xaxis_title='x',
    yaxis_title='y',
    template=dark_template,
    width=600,
    height=400,
    margin=dict(l=50, r=50, t=50, b=50),
    xaxis=dict(scaleanchor="y", scaleratio=1),
    yaxis=dict(constrain='domain')
)

fig_circle.write_html('figures/circle.html')

# 2. Ellipse
t_ellipse = np.linspace(0, 2*np.pi, 100)
a, b = 3, 2
x_ellipse = a * np.cos(t_ellipse)
y_ellipse = b * np.sin(t_ellipse)

fig_ellipse = go.Figure()
fig_ellipse.add_trace(go.Scatter(
    x=x_ellipse, y=y_ellipse,
    mode='lines',
    name='Ellipse',
    line=dict(color='#63b3ed', width=3)
))

# Add some tangent vectors
t_tangents = np.linspace(0, 2*np.pi, 16, endpoint=False)
for t in t_tangents:
    x_point = a * np.cos(t)
    y_point = b * np.sin(t)
    dx = -a * np.sin(t)
    dy = b * np.cos(t)
    
    fig_ellipse.add_trace(go.Scatter(
        x=[x_point, x_point + 0.3*dx], 
        y=[y_point, y_point + 0.3*dy],
        mode='lines+markers',
        line=dict(color='#68d391', width=2),
        marker=dict(size=4),
        showlegend=False
    ))

# Add acceleration vectors
for t in t_tangents:
    x_point = a * np.cos(t)
    y_point = b * np.sin(t)
    ddx = -a * np.cos(t)
    ddy = -b * np.sin(t)
    
    fig_ellipse.add_trace(go.Scatter(
        x=[x_point, x_point + 0.2*ddx], 
        y=[y_point, y_point + 0.2*ddy],
        mode='lines+markers',
        line=dict(color='#f6e05e', width=2),
        marker=dict(size=4),
        showlegend=False
    ))

fig_ellipse.update_layout(
    title='Ellipse: p(t) = (a cos t, b sin t)',
    xaxis_title='x',
    yaxis_title='y',
    template=dark_template,
    width=600,
    height=400,
    margin=dict(l=50, r=50, t=50, b=50),
    xaxis=dict(scaleanchor="y", scaleratio=1),
    yaxis=dict(constrain='domain')
)

fig_ellipse.write_html('figures/ellipse.html')

# 3. Parabola
t_parabola = np.linspace(-3, 3, 100)
x_parabola = t_parabola
y_parabola = t_parabola**2

fig_parabola = go.Figure()
fig_parabola.add_trace(go.Scatter(
    x=x_parabola, y=y_parabola,
    mode='lines',
    name='Parabola',
    line=dict(color='#63b3ed', width=3)
))

# Add some tangent vectors
t_tangents = np.linspace(-2.5, 2.5, 16)
for t in t_tangents:
    x_point = t
    y_point = t**2
    dx = 1
    dy = 2*t
    
    fig_parabola.add_trace(go.Scatter(
        x=[x_point, x_point + 0.5*dx], 
        y=[y_point, y_point + 0.5*dy],
        mode='lines+markers',
        line=dict(color='#68d391', width=2),
        marker=dict(size=4),
        showlegend=False
    ))

# Add acceleration vectors
for t in t_tangents:
    x_point = t
    y_point = t**2
    ddx = 0
    ddy = 2
    
    fig_parabola.add_trace(go.Scatter(
        x=[x_point, x_point + 0.3*ddx], 
        y=[y_point, y_point + 0.3*ddy],
        mode='lines+markers',
        line=dict(color='#f6e05e', width=2),
        marker=dict(size=4),
        showlegend=False
    ))

fig_parabola.update_layout(
    title='Parabola: p(t) = (t, t²)',
    xaxis_title='x',
    yaxis_title='y',
    template=dark_template,
    width=600,
    height=400,
    margin=dict(l=50, r=50, t=50, b=50),
    xaxis=dict(scaleanchor="y", scaleratio=1),
    yaxis=dict(constrain='domain')
)

fig_parabola.write_html('figures/parabola.html')

# 4. Non-regular curve: Semicubical parabola (cusp)
t_cusp = np.linspace(-2, 2, 100)
x_cusp = t_cusp**2
y_cusp = t_cusp**3

fig_cusp = go.Figure()
fig_cusp.add_trace(go.Scatter(
    x=x_cusp, y=y_cusp,
    mode='lines',
    name='Semicubical Parabola',
    line=dict(color='#63b3ed', width=3)
))

# Add some tangent vectors (avoiding t=0 where derivative is zero)
t_tangents_cusp = np.concatenate([
    np.linspace(-2, -0.3, 8),
    np.linspace(0.3, 2, 8)
])
for t in t_tangents_cusp:
    x_point = t**2
    y_point = t**3
    dx = 2*t
    dy = 3*t**2
    
    fig_cusp.add_trace(go.Scatter(
        x=[x_point, x_point + 0.4*dx], 
        y=[y_point, y_point + 0.4*dy],
        mode='lines+markers',
        line=dict(color='#68d391', width=2),
        marker=dict(size=4),
        showlegend=False
    ))

# Add acceleration vectors
for t in t_tangents_cusp:
    x_point = t**2
    y_point = t**3
    ddx = 2
    ddy = 6*t
    
    fig_cusp.add_trace(go.Scatter(
        x=[x_point, x_point + 0.2*ddx], 
        y=[y_point, y_point + 0.2*ddy],
        mode='lines+markers',
        line=dict(color='#f6e05e', width=2),
        marker=dict(size=4),
        showlegend=False
    ))

fig_cusp.update_layout(
    title='Semicubical Parabola: p(t) = (t², t³) - Non-regular at t=0',
    xaxis_title='x',
    yaxis_title='y',
    template=dark_template,
    width=600,
    height=400,
    margin=dict(l=50, r=50, t=50, b=50),
    xaxis=dict(scaleanchor="y", scaleratio=1),
    yaxis=dict(constrain='domain')
)

fig_cusp.write_html('figures/cusp.html')

# 5. Cycloid
t_cycloid = np.linspace(0, 4*np.pi, 200)
R = 1  # radius of rolling circle
x_cycloid = R * (t_cycloid - np.sin(t_cycloid))
y_cycloid = R * (1 - np.cos(t_cycloid))

fig_cycloid = go.Figure()
fig_cycloid.add_trace(go.Scatter(
    x=x_cycloid, y=y_cycloid,
    mode='lines',
    name='Cycloid',
    line=dict(color='#63b3ed', width=3)
))

# Add some tangent vectors (avoiding cusp points where derivative is zero)
t_tangents_cycloid = np.concatenate([
    np.linspace(0.1, 2*np.pi-0.1, 16),
    np.linspace(2*np.pi+0.1, 4*np.pi-0.1, 16)
])
for t in t_tangents_cycloid:
    x_point = R * (t - np.sin(t))
    y_point = R * (1 - np.cos(t))
    dx = R * (1 - np.cos(t))
    dy = R * np.sin(t)
    
    fig_cycloid.add_trace(go.Scatter(
        x=[x_point, x_point + 0.3*dx], 
        y=[y_point, y_point + 0.3*dy],
        mode='lines+markers',
        line=dict(color='#68d391', width=2),
        marker=dict(size=4),
        showlegend=False
    ))

# Add acceleration vectors
for t in t_tangents_cycloid:
    x_point = R * (t - np.sin(t))
    y_point = R * (1 - np.cos(t))
    ddx = R * np.sin(t)
    ddy = R * np.cos(t)
    
    fig_cycloid.add_trace(go.Scatter(
        x=[x_point, x_point + 0.2*ddx], 
        y=[y_point, y_point + 0.2*ddy],
        mode='lines+markers',
        line=dict(color='#f6e05e', width=2),
        marker=dict(size=4),
        showlegend=False
    ))

fig_cycloid.update_layout(
    title='Cycloid: p(t) = R(t - sin t, 1 - cos t)',
    xaxis_title='x',
    yaxis_title='y',
    template=dark_template,
    width=600,
    height=400,
    margin=dict(l=50, r=50, t=50, b=50),
    xaxis=dict(scaleanchor="y", scaleratio=1),
    yaxis=dict(constrain='domain')
)

fig_cycloid.write_html('figures/cycloid.html')

# 6. Combined comparison figure
fig_combined = go.Figure()

# Circle
fig_combined.add_trace(go.Scatter(
    x=x_circle, y=y_circle,
    mode='lines',
    name='Circle: R=2',
    line=dict(color='#63b3ed', width=2)
))

# Ellipse
fig_combined.add_trace(go.Scatter(
    x=x_ellipse, y=y_ellipse,
    mode='lines',
    name='Ellipse: a=3, b=2',
    line=dict(color='#68d391', width=2)
))

# Parabola (scaled down)
t_parabola_scaled = np.linspace(-2, 2, 50)
x_parabola_scaled = t_parabola_scaled
y_parabola_scaled = t_parabola_scaled**2

fig_combined.add_trace(go.Scatter(
    x=x_parabola_scaled, y=y_parabola_scaled,
    mode='lines',
    name='Parabola',
    line=dict(color='#f6e05e', width=2)
))

fig_combined.update_layout(
    title='Comparison of Plane Curves',
    xaxis_title='x',
    yaxis_title='y',
    template=dark_template,
    width=700,
    height=500,
    margin=dict(l=50, r=50, t=50, b=50),
    xaxis=dict(scaleanchor="y", scaleratio=1),
    yaxis=dict(constrain='domain')
)

fig_combined.write_html('figures/combined.html')

print("Figures generated successfully!")
print("Generated files:")
print("- figures/circle.html")
print("- figures/ellipse.html") 
print("- figures/parabola.html")
print("- figures/cusp.html")
print("- figures/cycloid.html")
print("- figures/combined.html")
