'''
Import libraries: pip install pandas plotly dash dash_core_components dash_html_components

'''

import dash
import dash_core_components as dcc
import dash_html_components as html

# Create a Dash Application
app = dash.Dash(__name__)

# Define the layout of the Dashboard
app.layout = html.Div(
    
    children = [
        
        html.H1('Dashboard'),
        dcc.Graph(
            
            id = 'Graph',
            figure = {
                
                'data':[
                    
                    {'x':[1, 2, 3], 'y':[4, 1, 2], 'type': 'bar', 'name': 'Bar chart'},
                    {'x':[1, 2, 3], 'y':[2, 4, 5], 'type': 'line', 'name': 'Line chart'},
                    
                ],
                
                'layout': {
                    
                    'title': 'Graph title',
                    'xaxis': {'title': 'x-axis'},
                    'yaxis': {'title': 'y-axis'}
                    
                }
                
            }
            
        )
        
    ]
    
)

# Run the application
if __name__ == '__main__':
    
    app.run(debug = True)