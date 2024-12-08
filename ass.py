import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import webbrowser

# Load the dataset
file_path = "metadata.csv"  
df = pd.read_csv(file_path)

# Inspecting data
print(df.head())


df['Cycle'] = range(1, len(df) + 1)
df['Battery_impedance'] = df['Re'] + df['Rct']
df.dropna(subset=['Re', 'Rct'], inplace=True)

# Generate plots
fig_impedance = px.line(
    df,
    x='Cycle',
    y='Battery_impedance',
    title='Battery Impedance Over Charge/Discharge Cycles',
    labels={'Cycle': 'Cycle', 'Battery_impedance': 'Impedance (Ohms)'}
)
fig_impedance.write_html("Battery_Impedance.html")

fig_re = px.line(
    df,
    x='Cycle',
    y='Re',
    title='Electrolyte Resistance (Re) Over Charge/Discharge Cycles',
    labels={'Cycle': 'Cycle', 'Re': 'Re (Ohms)'}
)
fig_re.write_html("Re_Resistance.html")

fig_rct = px.line(
    df,
    x='Cycle',
    y='Rct',
    title='Charge Transfer Resistance (Rct) Over Charge/Discharge Cycles',
    labels={'Cycle': 'Cycle', 'Rct': 'Rct (Ohms)'}
)
fig_rct.write_html("Rct_Resistance.html")

fig = go.Figure()

# Add Battery Impedance
fig.add_trace(go.Scatter(x=df['Cycle'], y=df['Battery_impedance'],
                         mode='lines', name='Battery Impedance'))

# Add Re
fig.add_trace(go.Scatter(x=df['Cycle'], y=df['Re'],
                         mode='lines', name='Re (Electrolyte Resistance)'))

# Add Rct
fig.add_trace(go.Scatter(x=df['Cycle'], y=df['Rct'],
                         mode='lines', name='Rct (Charge Transfer Resistance)'))


fig.update_layout(
    title='Battery Parameters Over Charge/Discharge Cycles',
    xaxis_title='Cycle',
    yaxis_title='Resistance (Ohms)',
    legend_title='Parameters'
)
fig.write_html("Combined_Battery_Parameters.html")

# Generate main HTML 
index_content = """
<!DOCTYPE html>
<html>
<head>
    <title>Battery Analysis </title>
</head>
<body>
    <h1 style="color:Blue" align="center">Battery Analysis Results</h1>
    <ul>
        <li ><a href="Battery_Impedance.html" target="_blank">Battery Impedance Plot</a></li>
        <br>
        <li ><a href="Re_Resistance.html" target="_blank">Electrolyte Resistance (Re) Plot</a></li>
        <br>
        <li ><a href="Rct_Resistance.html" target="_blank">Charge Transfer Resistance (Rct) Plot</a></li>
        <br>
        <li><a href="Combined_Battery_Parameters.html" target="_blank">Combined Parameters Plot</a></li>
        <br>
    </ul>
</body>
</html>
"""

# Save the index.html file
with open("index.html", "w") as f:
    f.write(index_content)

#opens index.html on loading
webbrowser.open("index.html")

print(" Open 'index.html' to view the results.")






